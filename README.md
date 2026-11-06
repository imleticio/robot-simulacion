# RoboSim university robot — diagnostic stage

## Active direction: standalone reactive comparison

**Use the SAME `robot_reactivo_simple.nxc`, now38,3, with the USER'S3/4configuration.**
Lights3/4down, A/Cas pictured; no1/2steering or reconfiguration. Left3black now
commands Aforward/Creverse; right4commands the mirror, matching tested motor sides.
One file, no18turn script or commanded encoder-angle target. A743sampled-difference
ceiling bounds a persistent one-sided correction; reacquisition releases it early.
Read [REACTIVO_SIMPLE.md](REACTIVO_SIMPLE.md). Logging is back on non-navigation
port1(zero-basedport0),26field38,3frames; never write diagnostics to active3/4.
The first rearmed return to white is a candidate, not proof of full branch coverage
or two laps.239host/audit testsPASS;38,3NBC/powered RoboSim pending.111and
Sim_Robotpreserved. Earlier1/2reactive instructions are historical, not this setup.
The older3/4route programs below are historical, not the next run on this setup.

**Continuing in a new chat? Read [CONTINUIDAD.md](CONTINUIDAD.md) first.** It records current working files, user-side tests, simulator limitations, discarded approaches and the unresolved route model.

## Historical3/4route and local continuation programs

**Next: `robot_vuelta_integrada_continua.nxc` (37,116).**115again stopped at the
repeated200interval exit-test gate after completing the B pivot.116replaces that
handoff: preserve the first exit/B450origin, then use ongoing111line following
after later pivots, with a pending step credited only at the next trigger/final
marker. No more B reference/angle/cap adjustment in this revision. Fault guards
remain;27field frames append pendingTurn.214host/audit testsPASS;116NBC/runtime
pending. Full physical lap/coverage is NOT established. See VUELTA_INTEGRADA.md.

**Previous integrated run: `robot_vuelta_integrada_cruce_tardio.nxc` (37,115).**
114reached the second pivot referenceA0/C744or745, but both observed exits stopped
at200intervals without the required stable contact.115changes ONLY firstB370->450
and revision, testing slightly later placement; early entry is not established.
No pivot angle/time, exit budget, sensor or shared-controller changes.203testsPASS;
115runtime now observed: second pivot completes, repeated exit gate still stops.
Use116next. See VUELTA_INTEGRADA.md;111baseline preserved.

**Previous integrated run: `robot_vuelta_integrada_cruce.nxc` (37,114).** Video/runtime
review shows113passed the intended B branch;1200was beyond all observed next-leg
loss endpoints(710.5..760mean sampled counts).114changes ONLY the first B seed to370
and revision;370is a candidate, not measured B localization.198host/audit tests pass;
114NBC/runtime now observed through the second pivot and failed exit. Use current
VUELTA_INTEGRADA.md instructions, not another
unchanged113run.26field frames;111/112/113artifacts preserved.

**Previous integrated run: `robot_vuelta_integrada_aproximacion.nxc` (37,113).**
112ran and stopped before its first pivot: a short diagnostic's60-count guard
was misapplied to the full approach.113restores111's20/10/25approach and scopes
that short budget to actual white crossing with a separate baseline. Pivot/exit
and route references remain unchanged;111and112RXEsare preserved.193host/audit
tests passed before runtime.113first left pivot/exit are now observed, but B was
missed before reference1200. See
[VUELTA_INTEGRADA.md](VUELTA_INTEGRADA.md);113frames have26fields.

**New integrated first-lap attempt: `robot_vuelta_integrada.nxc` (37,112).**
Read [VUELTA_INTEGRADA.md](VUELTA_INTEGRADA.md) for the different starting position,
candidate18turn route, provisional junction references, safety stops and24field
telemetry. Its original181host/audit tests passed; subsequent112runtime executed
marker/following paths but stopped before the first pivot. Use113next, not another
unchanged112trial. It does not implement two laps or establish validated coverage.
The37,111source/shared source/RXE remain the unchanged tested local baseline.
The older diagnostic instructions below do not replace the current116run instructions.

**Current executable: `robot_prueba_codo_mando.nxc` (37,111).** It preserves110
and maintains the same pivot command each interval using `OnFwdEx` with
`RESET_NONE`, retaining the encoder reference. Commanded power is checked before
and after; the existing no-progress and safety guards remain. This may recover
a lost command but cannot fix frozen physics; neither cause is proven for earlier
failures.156host/audit tests pass, including actual x86 flag-dispatch checks.
User-side111compilation/runtime now completed one bounded turn/exit/continuation:
200refreshes, no observed power mismatch or flat encoder samples, finalboth-black.
This does not prove all earlier failures are fixed or validate the full route.
Use already-openBricxCC and the current
patched simulator; do not reset sensors or relaunch the normal wrapper shortcut.

**Current executable: `robot_prueba_codo_tiempo.nxc` (37,110).** This university
practical prioritizes working, explainable behavior rather than contest speed.
The inspected ordinary motor model needs about4.953s to reach743counts atpower15;
the old240x20ms sample budget was only4.8nominalseconds. This revision uses a
375sample watchdog and stops separately after40consecutive unchanged encoder
samples. Geometry, motor commands, exit and continuation are unchanged. These
nominal calculations do not explain every earlier partial pivot or guarantee
alignment.146host/audit tests pass. User-side110runtime includes one completed
bounded continuation and one40-sample zero-encoder-progress stop; its cause is
still unresolved. Use the already
open BricxCC and patched simulator without resetting sensors. Older instructions
below are historical and do not override the current CONTINUIDAD section.

**Current executable: `robot_prueba_codo_continuo_sin_avance.nxc` (37,109).**
Run it in the already opened `legosimulator-yield.exe`, with current sensor
settings unchanged. Two 37,108 runs in that patched instance passed the bounded
progress/contact criterion. 37,109 preserves that no-pre-advance geometry and
enables only the existing short continuation after the criterion passes; it does
not add another turn or implement the route. 135 host/audit tests pass; NBC
compilation and RoboSim execution of 37,109 were subsequently observed: one run
completed its extra bounded segment, but another still stopped during a partial
pivot on the hash-verified patched simulator. Reliability remains unresolved.
The diagnostic history
below does not override the current instructions in CONTINUIDAD.md.

**Current priority: isolate the corner geometry.** The next executable is
`robot_prueba_codo_salida_sin_avance.nxc` (37,108). It omits the experimental
60-count advance before the existing pivot, then enables the unchanged controlled
exit after confirmed contact. It has no additional continuation or second turn.
The preceding 37,107 observation-only test had one both-black contact result and
one incomplete-pivot watchdog stop; a reliable fix is not established. Keep sensor
settings unchanged. This is not a new calibration. 124 host tests pass. User-side
37,108 runtime now shows one progress/contact criterion pass and one incomplete
pivot watchdog stop; a reliable geometric fix is still not established.
The 37,106 instructions below describe the previous continuation experiment.

**Current motion test:** use `robot_prueba_continuacion.nxc` (37,106), not the
marker module. It preserves 37,105 and adds a separately bounded local follower
segment only after the exit criterion passes. The new segment stops at the first
track's 180 sampled counts, a 60-count sampled track difference, a 120-interval
watchdog, or a sensor/encoder safety condition. These provisional bounds do not
prove physical distance, heading, containment or a legal junction traversal.
NBC compilation and RoboSim execution of 37,106 are pending. Keep diagnostics
silent, current sensor settings unchanged, and supervise the one-run test from
the original approach straight. Do not restart the historical calibration below.

## Marker counting module — not a competition executable

`robot_marker_tracker.nxc` adapts the supplied single-sensor example into a
silent, API-free state machine. It is a reusable include, **not a program to
load into RoboSim by itself**. The current corner diagnostics are unchanged.

- Three consecutive both-black readings arm a crossing. Gray or a short dip
  away from white does not rearm it.
- Three consecutive both-white readings confirm a crossing. The first accepted
  crossing starts the run; the next two accepted crossings finish laps 1 and 2.
- After the start, `routeComplete == 1` is required at the confirmed crossing.
  That permission must come from a separately validated controller covering
  every required segment for the current lap, not a constant or elapsed time.
- Rejected crossings are consumed until a new confirmed both-black release.
  Invalid scaled readings outside 0..100 report a fault and disarm the tracker.

The future controller calls `ResetMarkerTracker()` once before starting and
`UpdateMarkerTracker(leftReading, rightReading, routeComplete)` once per control
sample. `markerEvent` is cleared on the next call; `markerFinished` stays latched.

| Event | Caller responsibility |
|---|---|
| `MARKER_EVENT_START` | Start timing and initialize lap-route progress. No lap is completed. |
| `MARKER_EVENT_LAP` | Record lap 1 and reset route progress for lap 2. |
| `MARKER_EVENT_FINISH` | Stop driving and keep the robot silently stopped. |
| `MARKER_EVENT_REJECTED` | Treat the unexpected crossing as a navigation fault, not a lap. |
| `MARKER_EVENT_INVALID` | Stop safely on invalid sensor input. |

The module deliberately does not command motors, handle junctions, guarantee
counterclockwise travel, or replace the corner diagnostic's white-stop guard.
Integration must define how to cross the marker safely; simply including this
file in the current corner program would not implement two laps.

Verification: **156 host/audit tests pass**, including 21 tests compiling the actual
API-free module as C with Clang and executing it. This checks its logic, **not
NBC compilation or RoboSim behavior**. Confirmation lengths and both-sensor
white coverage still require runtime validation in the eventual route program.

## Current experimental findings

The initial pending checklist below is retained as the original measurement procedure; this section records subsequent evidence and takes precedence for observed items.

- The user compiled and ran the diagnostic programs in the supplied BricxCC/RoboSim installation. This is user-side validation, not a local compiler run by the assistant.
- Ports 3/4 are light sensors pointing down. Paired opposite-edge tests identified 3 as robot-left and 4 as robot-right.
- Stationary observed scaled values: black 0/0, gray 50/50, white 100/100. Other gray readings were 49. These are initial samples, not measured noise bounds or a complete calibration sweep.
- Port 4 initially had the sound sensor selected; its constant 100 was not a valid light calibration. Selecting the light icon changed its black reading to 0.
- The user observed A alone turning toward robot-left, C alone toward robot-right, and A/C together moving toward the sensors. The test follower therefore uses A as right drive and C as left drive. Output side assignments in the simulator panel matter; C initially had no side assigned.
- `stdout.txt` reports ignored text drawing, string conversions, AND/OR bytecodes and `finclump`. Avoid these operations in the current tested follower; hold the task in an explicit stationary loop at completion.
- This bundled NBC defines `ScaledValue` (4), not the newer `ScaledValueField`. Writes via `SetInput(IN_1, ScaledValue, value)` appear numerically in the simulator log. This is an experimentally verified simulator-specific diagnostic bridge, not a general NXT logging mechanism. Port 1 must remain unused.
- `robot_prueba_linea.nxc` is silent and logs a frame: 37, 82, stop reason, step count, left reading, right reading. Reasons: 1 white, 2 neither sensor black, 3 step limit. It has no junction navigation or recovery.
- A straight test ended after 203 cycles with both readings 49; the user reported reaching the end of the straight. A later run ended after 244 cycles with 49/49. Cycle counts are not wall-clock timing measurements.
- The user reported realignment after small initial deviations in both directions. This is qualitative evidence, not quantified repeatability; the current telemetry does not count steering corrections.
- Route topology, legal junction decisions, corner traversal, marker events, two laps, repeatability and speed optimization remain pending. No competition-completion claim is supported.

The initial display-based calibration below does not work as an observation method in this RoboSim version. Use the numeric diagnostic bridge instead; sound tests are optional and should remain muted for tracking work.

The competition solution is not implemented or validated yet. Start with stationary sensor measurements; do not use the existing prototype as a competition entry.

## Run the calibration

1. Keep motors A/C enabled and B disabled. Configure ports 3/4 as light sensors pointing at the floor. Do not change the orange rotary controls until their function has been verified.
2. Stop other programs. Place the robot so both sensor footprints are entirely over one uniform surface, away from tile seams and track edges.
3. Open `robot_calibracion.nxc` in BricxCC. Compile with the installed NXC/NBC compiler and run using the same RoboSim workflow as the existing prototype.
4. Inspect the NXT LCD if the simulator exposes it. Each row shows port, minimum, integer average and maximum for 100 readings. A window takes at least two seconds; simulator scheduling may make it longer.
5. After repositioning, discard the first two displayed updates. Record three complete windows on black, gray and white, for each port. Do not reposition by commanding the motors in this test.

The program commands A/C off and never commands forward or reverse motion. It does not classify surfaces, drive, beep or save measurements to a file. If no LCD is available, report that limitation: display API compatibility does not guarantee RoboSim renders the LCD. Do not interpret an invisible display as zero sensor readings.

| Surface | Port | Window 1 min/avg/max | Window 2 min/avg/max | Window 3 min/avg/max |
|---|---|---|---|---|
| Black | 3 | pending | pending | pending |
| Black | 4 | pending | pending | pending |
| Gray | 3 | pending | pending | pending |
| Gray | 4 | pending | pending | pending |
| White | 3 | pending | pending | pending |
| White | 4 | pending | pending | pending |

To identify sensor sides, place one footprint over black and the other over gray, then swap. Record which port changes. Do not assume port 3 is left solely because the prototype says so.

## Measurement decisions

- Use separate calibration values for each port.
- Only choose thresholds after checking ordering and separation of measured ranges. Gray/white overlap means a simple white threshold is not reliable.
- Repeat near track edges to determine whether readings vary progressively with position. Three distinguishable surfaces alone do not prove that PD steering has useful lateral resolution.
- Keep two sensors initially. Additional ports are visible in the configuration, but placement freedom and useful ground coverage remain unverified.

## Evidence and pending acceptance

| Item | Status |
|---|---|
| Existing prototype inspected | Confirmed; original files unchanged |
| NXC input/display APIs | Checked against published BricxCC NXC reference |
| Calibration compilation with installed NBC | Pending; no compiler available in PATH during initial inspection |
| Calibration execution and LCD visibility in RoboSim | Pending |
| Surface separation and left/right sensor mapping | Pending |
| Motor mapping and forward polarity | Pending |
| Exact route, required segment coverage and counterclockwise start | Pending |
| Line control, junction navigation and safe recovery | Not implemented |
| Start plus two finish beeps, two laps and final stop | Not implemented |
| Repeatability and measured competition time | Not tested |

The `.rxe` beside the original prototype is not proof that the new calibration program compiles or runs. No simulator results or timing measurements have been obtained.

## References

- Input functions: https://bricxcc.sourceforge.net/nbc/nxcdoc/nxcapi/group___input_module_functions.html (`SetSensorLight`, `Sensor`).
- Display functions: https://bricxcc.sourceforge.net/nbc/nxcdoc/nxcapi/group___display_module_functions.html (`ClearScreen`, `TextOut`, `NumOut`).

These references document NXC APIs, not RoboSim's implementation of those APIs. The remaining competition deliverables will be added incrementally after measurements and route validation, rather than filled with an invented route.
