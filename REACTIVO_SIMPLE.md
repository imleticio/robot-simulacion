# Active comparison: one reactive follower, no scripted route

## Current38,3: original robot, same file

The user explicitly selected **`robot_reactivo_simple.nxc` and the original panel**.
Do not use the friend's1/2setup for this revision. Keep the robot as supplied:
lights **3and4point DOWN**, A/Cassignments unchanged, Bunassigned. Leave1/2as in
the picture; the program does not configure or read them for navigation. Do not
infer numeric knob angles from a screenshot or change them to make the code fit.

Close a stale editor tab WITHOUT saving, reopen this SAMEupdatedfile, compile in
the already-open BricxCC and load only its successfully generated RXE. Center the
robot on the original departure straight before white and run once supervised.
Stop on steering away, gray cutting or wrong branch; record the first deviation.
No stationary calibration or isolated corner trial is requested.

### Reactive corrections and corner knowledge

Original paired-edge/motor tests identified3left,4right,Arightdrive,Cleftdrive.
The previous friend's IDpairing therefore could not be fixed by port substitution
alone.38,3uses the following CONTINUOUS rules, without predefined turn positions:

| Contact | Command |
|---|---|
| Both black | A25/C25forward |
| Left3only black | Aforward25/Creverse7: correct left |
| Right4only black | Areverse7/Cforward25: correct right |
| White crossing/release | A20/C20, with the existing bounded marker protocol |
| Neither black nor white | Stop; do not infer a corner or choose a blind direction |

Encoder knowledge from the old corner work is used as a **safety ceiling**, not
a demanded maneuver: signed sampled A-Cdifference is accumulated only during the
same uninterrupted one-sided correction. At absolute743, stop reason11ONLYif the
new reading still requires that same correction. Both-black reacquisition, white
or the opposite correction releases/resets the local budget. A short correction
does not wait for743and is not forced to90degrees. This is NOT a whole-leg60-count
limit or another200sample exit-test gate.

743came from the prior stopped-track reference. Here it bounds sampled DIFFERENCE
between drives, not one absolute counter. Inter-command motion/quantization means
it is not an exact chassis angle or containment guarantee. It can conservatively
stop a correction that has not recovered contact; do not enlarge it blindly.

The40flat/sign/sentinel/6000overall/400marker protections and38,2startup rule remain.
Startup accepts3non-white samples with at least one black sensor. Marker arming
uses that same contact rule; both-white confirmation remains3. First white starts;
next rearmed white stops as a return CANDIDATE, not proven all-branch/two-lap success.

### Current telemetry and validation

Logging uses **IN_1, zero-basedport0** while stopped, without changing1/2sensor
type/orientation. They are not navigation inputs. NEVER log to the active3/4.
38,3has26fields: prior24layout, sensor fields now left3/right4, APPEND correction
state(0none,1left,2right) and signed correction difference. These are the last
correction snapshots, not live motor power after braking. New reason11means the
persistent correction exhausted its local budget. Preserve the rejecting sample
on faults; no later stopped read overwrites it.

239audit testsPASS,25reactive tests. Five new tests cover local correction ceiling,
reacquisition at the ceiling, early recovery without angle target, direction
switch reset and white release; port isolation and motor pairing tests updated.
Actual NXCsource compiled as C with mocked APIs is NOT NBC/physics validation.
38,3NBCcompilation and physical route still pending.111andfriendfiles preserved.

If both gray occurs at a true bend, these two readings alone still cannot identify
left versus right or distinguish a lateral departure. This version deliberately
does not reproduce the false-corner shortcut of the scripted versions. A repeated
stop there requires better observation, not an invented unconditional turn.

## Historical1/2comparison below — do not apply to38,3

Compile **`robot_reactivo_simple.nxc`**, a standalone file. It uses the friend's
sensor1/2arrangement and motor-correction pairing, not the old3/4configuration or
18turn route. No GUI setup change or robot execution has been performed by the
assistant. NBC compilation and RoboSim execution are still pending.

**Current revision is38,2in the same file.**38,1compiled/ran but rejected startup
before any motor command: terminal readings49/49,49/49and49/0,allreason2/samples0.
These were reread after braking, not necessarily the rejecting startup sample.
Independently, requiring both black was inconsistent with the valid one-sided
correction cases.38,2accepts at least one black sensor with neither white.
If your1/2setup is already in place, do not change it: reopen the updated file
from disk without saving a stale editor buffer, compile/load its successfulRXE.
38,2compilation and powered RoboSim motion remain pending.
Fault logs now preserve the actual failing sample rather than overwriting it with
a later stopped read; final successful return/watchdog resampling is retained.

## Set up once, then attempt the route

Stop the current program before changing ports or positioning the robot.

1. Preserve the current panel close-up as the old3/4reference. **Do not turn the
   3/4knobs or alter A/Cside assignments.** The37,111files remain untouched.
2. Configure ports **1and2as light sensors pointing DOWN**, using the friend's
   picture as the visual arrangement reference:1needle leaning upper-right,
   2upper-left. These are not measured numeric angles or independently verified
   left/right labels. Disable3/4with X, leaving their knob positions unchanged.
3. Keep **AandCassigned, Bunused**, as in the picture. This version intentionally
   uses short counter-rotation corrections (one track reverses), like the example.
4. Open the new standalone NXC in the already-open BricxCC. Compile, then load
   only the successfully generated matching `robot_reactivo_simple.rxe`.
5. Start **centered on the black straight before white**, pointing across white
   in the original counterclockwise departure direction. The startup check
   requires at least one1/2reading to be black, with neither white, for3samples.
   If it rejects the centered pose, keep the
   reported values; do not move the robot off the intended line to force a pass
   or tune knobs blindly. Run one supervised
   integrated attempt; stop immediately if it steers away, cuts gray or takes an
   undesired branch. Do not perform another isolated corner/calibration sequence.

Do not run37,111or116as if they used this new arrangement: they expect3/4and log
through port1. To restore the previous setup, disable1/2and reactivate the previous
3/4light/down configuration with the knob positions preserved above; restore its
proper starting pose. Merely loading a different RXE does not restore mounting.

## What this version does

| Contact | Command |
|---|---|
| Both black | A25/C25forward |
| Only sensor1black | Areverse7/Cforward25 |
| Only sensor2black | Aforward25/Creverse7 |
| White crossing/release | A20/C20forward, bounded |
| Neither black, neither white | Stop; no blind gray advance or forced90degree turn |

The correction pairing follows the friend's source by sensor ID. Its LEFT/RIGHT
comments are not independent measurements. Actual response must be observed with
the replicated arrangement; do not assume that swapping only port numbers works.

Some two-sensor arrangements intentionally straddle the black strip: both can
read gray while the chassis is centered over black. The photo alone does not
establish whether that is true here. Therefore the gray stop/startup check is a
conservative compatibility check, not proof the chassis is off track. If the
centered robot reads gray/gray, this controller's contact model must be revised
from that evidence; do not simply enable unconditional forward motion on gray.

Three consecutive non-white samples with at least one black sensor arm a passage;
three both-white samples accept it. First
passage emits a sound and continues. The next accepted passage, after a fresh
three-contact rearm, emits a sound and stops as a **return candidate**, not a validated
lap. Gray/gray, mixed white or fewer than three qualifying samples cannot rearm.

There are no junction coordinates, turn counters, encoder-angle targets, forced
corner searches, route includes or feature flags. Both-gray is not called a corner.
The program can still stop at a real bend if both footprints lose black; it does
not ignore this to force motion. A safe stop is not evidence the setup works.

## Differences from the friend's program

- Lower powers25/7rather than70/20; this is an adaptation, not an exact trajectory
  reproduction. White uses20rather than forced60for800ms.
- Nested conditionals avoid source AND/ORoperations known to be problematic in
  this simulator; the earlier ignored-message block was not tied to a specificRXE.
- Invalid readings, wrong signed encoder direction, unassigned counters and40flat
  intervals on either commanded drive stop the run. Baselines are sampled AFTER
  commands because these APIs can reset counters. No distance/angle is inferred.
-6000powered-interval overall watchdog and400sample white/release watchdog bound
  failure. At20msintervals these are nominal limits, not measured execution times.
- Marker debounce/rearm and stopped resampling replace a raw white-pass lap counter.

**Following black and returning to white does not establish visiting every branch,
no repeated segment, containment or the required two laps.** If the robot returns
by a short loop/perimeter only, that is not task completion. The all-black-branch
goal remains unchanged; navigation decisions must be added only if needed and
supported by actual trajectory evidence, not another guessed18turn sequence.

## Read the new log, without corrupting the active sensors

Telemetry moved to **unused port3**, printed as zero-based `port2` in stdout.
Do not parse only the old `port0` stream. All24field frames now start `38,2`:

`38,2,reason,event,samples,s1,s2,started,candidate,armed,blackRun,whiteRun,`
`straightIntervals,correction1Intervals,correction2Intervals,markerIntervals,`
`whiteAge,flatRun,lastDeltaA,lastDeltaC,lastCommandA,lastCommandC,6000,400`

Last command/delta fields describe the preceding interval, not live power after
braking. Negative values may be32-bit hex. Interval counters are commands, not
physical travel. Logging happens only while stopped, at start and terminal events;
the terminal frame may be repeated, not a separate execution.

| Reason | Meaning |
|---|---|
| 1 / 2 | Neither sensor black/white / no qualifying non-white initial black contact |
| 3 / 4 | Overall watchdog / invalid scaled sensor reading |
| 5 / 6 | Encoder sentinel / increment opposite commanded direction |
| 7 / 8 |40flat intervals on either drive / white-crossing/release watchdog |
| 10 | Marker not confirmed again while stopped |
| 100 | Rearmed return candidate, NOT all-branch/two-lap success |

## Evidence and scope

20reactive tests compile the actual standalone NXC as C with mocked APIs, including
its task declaration (not executing the infinite stopped task loop). They cover
pairing, signed reverse progress, stalls, input faults, gray stop, marker debounce,
stopped resampling and logging exclusively to unused port3. Full audit:234tests
pass. They do **not** validate sensor geometry, NXC compilation or RoboSim motion.
38,1startup/logging are observed, but it never entered its powered control loop
in the inspected frames; do not call the new reverse/following path validated.

Qualitative scope/design score: **8/10**, not a robot-performance score. This pass
chooses one program/configuration pair and excludes the map,18turn script, inferred
angles, blind gray search and automatic compliance claims. To reach10/10clarity,
confirm the actual sensor-side/correction contract and define the minimal coverage
decision policy from observed motion. No amount of host tests substitutes for that.
