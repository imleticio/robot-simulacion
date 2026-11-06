"""Version-locked scheduler fix. Always create a separate executable."""
import argparse
import hashlib
from pathlib import Path
import struct

ORIGINAL_SHA256 = "2729698c762c1850ae1abe903dc6d519418e5647b90fb5300bd7b1b2629684a4"
BRANCH_VA = 0x40A4A4
OLD_BRANCH = bytes.fromhex("eb af")  # loop to budget test, bypassing wait gate
NEW_BRANCH = bytes.fromhex("eb a3")  # loop to existing wait gate, then budget test


def file_offset(data, address):
    pe = struct.unpack_from("<I", data, 0x3C)[0]
    count = struct.unpack_from("<H", data, pe + 6)[0]
    optional = pe + 24
    base = struct.unpack_from("<I", data, optional + 28)[0]
    sections = optional + struct.unpack_from("<H", data, pe + 20)[0]
    for index in range(count):
        size, rva, raw_size, raw = struct.unpack_from(
            "<IIII", data, sections + index * 40 + 8
        )
        relative = address - base - rva
        if 0 <= relative < min(size, raw_size):
            return raw + relative
    raise ValueError("Address has no file-backed section")


def patched_bytes(original):
    if hashlib.sha256(original).hexdigest() != ORIGINAL_SHA256:
        raise ValueError("Unsupported executable: original SHA256 does not match")
    offset = file_offset(original, BRANCH_VA)
    if original[offset:offset + 2] != OLD_BRANCH:
        raise ValueError("Unexpected branch bytes")
    result = bytearray(original)
    result[offset:offset + 2] = NEW_BRANCH
    return bytes(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    result = patched_bytes(args.source.read_bytes())
    # Exclusive creation prevents overwriting an original or a prior build.
    with args.destination.open("xb") as output:
        output.write(result)
    print(hashlib.sha256(result).hexdigest(), args.destination)


if __name__ == "__main__":
    main()
