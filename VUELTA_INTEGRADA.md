# Run the continuous integrated route attempt — 37,116

**Historical scripted-route program, not the active controller. Use the current
[REACTIVO_SIMPLE.md](REACTIVO_SIMPLE.md) instructions for the user's3/4robot and
the SAMEreactivefile38,3. Earlier1/2comparison instructions are superseded.**

Compile **`robot_vuelta_integrada_continua.nxc`** in the already-open BricxCC, then load
the newly generated matching RXE into the current patched RoboSim. Keep all three
entry point and its two NXC includes together. Do not compile an include by itself or load an old RXE
after a compiler error. The tested37,111 source, shared source and RXE are preserved.

This program attempts the entire red route, rather than stopping after one corner.
It is **experimental**:115again reached the second pivot but failed the repeated
exit-test gate.116changes the navigation handoff; compilation/run are pending.
A prior direct Wine compiler-help invocation exited with SIGFPE before
producing output; the existing simulator/BricxCC processes remained running.

##116is continuous following, not another entry-reference adjustment

115did not solve the reported halt. Its two observed B exits reached A345/C270
and A353/C233, both above180, but only3/2fresh both-black samples rather than5.
Both ended reason15at200intervals; the task then intentionally braked forever.
That was not evidence that the motor commands stopped working. Moving the B
reference again would not address this repeated diagnostic gate.

116keeps B450and the same route and pivots. It changes what happens afterward:

1. Keep the successful first exit unchanged, so B450has the same reference origin.
2. After the B pivot and every later pivot, hand off to the ongoing111line follower
   (20/10/25), including one-sided contact. Do not run a separate200interval exit
   test before allowing the next route leg to move.
3. Keep that outgoing turn **pending**. Credit its ordered progress only when
   following reaches the next configured trigger, or the final marker is confirmed.
   A pivot alone does not advance the completed counter.
4. Stop on sensor/encoder faults, unexpected white, insufficient entry contact,
   lack of progress or the existing leg watchdog. Do not search, reverse, retry,
   skip a pending step or call a failed exit test successful.

This replaces a blocking stage, not a200->larger timeout change. The first exit
still has its200/180/5guard; later outgoing legs have the existing2000sample leg
watchdog and40flat guard. The unchanged edge detector can still confuse an actual
bend with accidental lateral loss after forward progress. Branch identification,
heading and containment remain unvalidated and require manual supervision.

The user accepts a different route order but still wants every black branch
covered.116retains the candidate full-branch route rather than substituting only
the perimeter. Its trigger-based progress is not proof of physical coverage or
assignment compliance. No full physical lap has been observed yet.

Reference-origin caveat: first B450keeps its tested first-exit origin. Return
B450is still an unvalidated seed, but in116starts after the turn6pivot/contact,
not after a separate turn6exit. Its numeric value is unchanged, not its physical
origin. It may need adjustment if the run reaches that part; do not call it a
preserved calibrated distance.

## Previous115hypothesis: later entry, not more rotation

Two114started attempts reached the B370reference and then the full commanded
right-pivot reference: A0/C744or745,213/210samples. The subsequent exit stopped at
its200interval cap, reason15. First exit:A340/C169,stable0,final49/0. Second exit:
A371/C202,stable1,stage reading0/0but subsequent terminal reading49/0. A single
both-black reading is not the required five; even both motor totals above180do
not make this a pass. Neither run recorded a completed second turn/exit stage.

The photographs and excess sampled Aadvance are consistent with leftward exit
correction after the right pivot, but do not identify exact heading, contact
footprints or whether the entry was early/late. This is not evidence for raising
the pivot target/time, removing the exit criterion or increasing the exit cap.

115changes **only** firstB370->450and revision. The additional80sampled counts test
the hypothesis that starting the pivot slightly farther along the incoming strip
improves placement. Early entry is **not proven** by one-sided contact. No motor,
heading, watchdog, contact criterion or other route decision changes. Both first
and return B references now happen to be450, but have separate origins and remain
independent unmeasured hypotheses. If the same failure persists, do not keep
increasing either value or the pivot/exit budgets without new evidence.

## Previous114change: earlier first B reference

The supplied24.54second recording shows the first bend followed by straight
travel through the intended branch area and a stop facing gray at the far bend.
The camera changes during this passage. It is not valid to convert raw pixel
distances or video timestamps into an exact B encoder reference.

Four distinct113second-leg terminal frames give mean sampled totals736.5,760,
710.5and731, all below the original1200target. The controller therefore never
ordered the second pivot. No exact video-to-log execution pairing was established.

114changes **only** the revision and first B reference to370. This is a next,
earlier candidate at roughly half the observed available leg, **not a measured
position of B** or proof of a correct turn. It may still be early or late. The
return B450seed, approach, first pivot/exit, all guards, and route sequence remain
unchanged. If it loses black early, it still stops; it does not turn at the wrong
far corner as a fallback. Stop manually if the candidate turn leaves the track.

## Why112stopped, and what113changes

The latest complete112attempt that confirmed the marker ended at reason19,
phase2,turn0: samples243, A528/C466, sensors0/50, completedTurns0,pivotA/C0/0.
It stopped on the signed62-count difference, before issuing the first pivot.
The60-count budget belonged to a short continuation diagnostic and was wrongly
applied to an entire correcting approach. Other112attempts also reached that
guard in the unstarted marker phase. The screenshot does not identify an exact
heading, and the final frame does not reconstruct the individual sensor samples.

113restores111's20/10/25approach before bends and before white contact. It removes
the mis-scoped cumulative60-count stop from that approach, not from white crossing.
First white contact latches the crossing substage and its own difference baseline;
the crossing/release still uses12/9and a60-count budget. Gray/white/fault/progress
guards remain; there is no search/retry. The first bend approach watchdog is
reduced to111's400samples; later legs keep112's2000cap. Pivot, exit, route choices
and the two B references are unchanged. This fixes the demonstrated premature
termination condition, not a proven geometric failure or all navigation problems.

The old112entry point/RXE are retained. Its default build still emits24fields
and uses its original policy, for reproducibility; it is not the next run.

## First supervised run

1. Keep the current simulator window, motor assignments and sensor settings.
   Do not reopen the normal PortingKit shortcut or repeat calibration.
2. Start on black **before the white marker**, facing across white toward the
   bottom-right bend in the red photograph: the requested counterclockwise
   departure. Both sensors must initially read black. This is not the old isolated
   corner starting position. Close stale source tabs without saving over disk files.
3. Compile/load the new program and run once. It should cross white with one sound,
   follow the candidate turn sequence, and stop with a second sound at the next
   expected white only after all18turn/exit stages have passed.
4. Stop manually immediately if it leaves the track or takes the wrong branch.
   Record the first place where behavior differs from the red route. A recording
   of this integrated attempt is useful; another isolated-corner trial is not needed.
5. Read the fresh37,112frames and ignored-instruction messages before changing any
   parameter. If it stops early, report the location; do not restart it from there
   as if route state had been retained.

## What changed from the baseline

| Behavior | Integrated attempt |
|---|---|
| Right pivot | Same743target, power15,375sample cap,40flat guard andRESET_NONE refresh policy as111 |
| Left pivot | Explicit A/C mirror of that policy; new, unvalidated geometry |
| First exit | Same12/12, braked9 corrections, both sampled totals>=180, then5fresh both-black readings within200intervals and stopped final check; unchanged B reference origin |
| Later outgoing legs | No separate short exit-test gate; continuous20/10/25following with pending progress until next trigger/final marker |
| Between bends | Restored111approach20/10/25;400interval cap on first leg,2000on later legs,40flat guard; no short60-count cumulative stop on approach |
| White |3both-white confirmations;800interval/1800average-count watchdog;12/9and a separately based60-count difference guard once white contact is latched |
| Faults | Stop without reverse, search, retry, skipping a turn or automatic recovery |
| Completion | One candidate traversal only. Two laps and final assignment acceptance remain future work |

Sampled counts are sums of increments measured after each motor command and before
the next reset. They omit inter-command motion; they are not exact distance, heading
or containment measurements. Logging occurs only when stopped, not every sample.
No sensor/encoder rule here can guarantee that the whole robot stays on the track.

## Candidate route and explicit hypotheses

The red photograph is the only map evidence; no track file is required. The table
is a proposed motion interpretation of it, not surveyed geometry. `edge` means
both sensors lose black after some forward progress; it does not prove a corner
was reached rather than an accidental line departure.

| Index | Intended location | Turn | Trigger |
|---|---|---|---|
| 0 | Bottom-right bend after marker | Left | Edge |
| 1 | B, northbound arrival from start | Right toward C | Reference450 |
| 2–4 | Large right loop | Right, right, right | Edges; pass C eastbound |
| 5–6 | Raised rectangular detour | Left, left | Edges; pass C northbound |
| 7 | B, southbound arrival from detour | Right toward inner-left branch | Reference450 |
| 8–9 | Inner-left path | Right, right | Edges |
| 10 | Lower entry into upper loop | Right | Edge |
| 11–15 | Stepped upper loop | Left, left, right, left, left | Edges |
| 16 | Outer top-left bend | Left | Edge |
| 17 | Outer bottom-left bend | Left toward marker | Edge |

**Both450references are unmeasured tuning hypotheses.** FirstBwas1200, then370;
115tests450after the370pivot reached its target but its exit failed. ReturnB450
remains the original photograph-based seed. There
is no verified tile scale or counter-to-tile calibration supporting them. FirstB
begins after its preceding first exit;116returnBbegins after turn6pivot/contact,
not at a surveyed junction center. Both-black at their endpoint is only a contact check;
it cannot identify B.115overrides `ROUTE_FIRST_B_REFERENCE` in its entry point;
`ROUTE_RETURN_B_REFERENCE` remains in `robot_route_plan.nxc`. Change only the
intended build's reference during evidence-driven adjustment.
Do not describe these values as measured localization or extend a watchdog to
hide a wrong turn.

The small stagger where the upper loop joins the outer path is provisionally
treated as a shared region, with ordinary following rather than two extra blind
pivots. Whether this selects the correct branch must be checked visually. Tight
upper bends may also be shorter than the fixed exit stage; if so, the program
stops rather than suppressing that guard. All left pivots, crossing alignment and
the ordered branch choices still require runtime observation.

The existing `robot_marker_tracker.nxc` is intentionally untouched: its contract
requires validated coverage. This experimental program does not feed it a made-up
`routeComplete` flag. Its own terminal100means only that the18candidate stages
and expected white endpoint were observed. It is **not proof** of full coverage,
absence of repeated segments, legal containment, or the required two laps.

## Read the log

Each116stopped-stage frame has27numeric fields, starting `37,116`:

`37,116,reason,phase,turn,completedTurns,direction,trigger,reference,samples,`
`left,right,totalA,totalC,pivotA,pivotC,flatRun,stable,refreshes,powerMismatches,`
`powerBefore,powerAfter,started,candidate,markerEntered,markerDifferenceBase,pendingTurn`

- `direction`: -1left,1right. Negative bridge values may appear as32-bit hex.
- `trigger`:0edge,1provisional reference. Finish has turn18and the last turn's
  configuration. `pivotA/C` retain the most recent pivot snapshot between stages.
- `phase`:0start marker,1leave white,2following,3pivot,4stationary contact,
  5exit,6return marker. `samples`, totals and stable counts reset per stage.
- `markerEntered/differenceBase`: white-contact latch and signed sampled A-C
  baseline for its short crossing budget; mode1release begins latched. These
  fields retain the most recent marker stage while following/pivoting. Subtract
  the baseline from current marker A-C before comparing to60. Old112has24fields.
- `pendingTurn`: -1none; otherwise the pivot whose outgoing leg has not reached
  its next trigger yet. Thus phase2,turn2,pending1means following out of B toward
  the next trigger, not that a third pivot has already happened.113..115have26fields.
- `completedTurns`: first step credited by the preserved first exit; later steps
  credited only at their next accepted following trigger/final marker. This is
  ordered controller progress, not proof that the correct physical branch was used.
- `reason=0`: stage passed, not a lap claim. The final frame is repeated after a
  fault so the latest complete frame reports why the robot is stationary.

| Reason | Meaning |
|---|---|
| 1 / 2 | Unexpected white / invalid initial black contact |
| 3 / 4 | Straight-leg / pivot watchdog |
| 6 / 11 | Missing stationary pivot contact / unexpected loss of black |
| 7 / 8 | Encoder direction or braked-track motion / encoder or power sentinel |
| 15 / 19 | Exit criterion not established / signed60-count marker-crossing difference (113);112also applied19to full approaches |
| 21 / 22 | No sampled progress for40intervals / pivot power command not confirmed |
| 23 / 24 | Required endpoint contact absent / marker watchdog |
| 25 / 26 | Invalid route state / invalid sensor value |
| 100 | Candidate sequence endpoint; requires visual coverage review |

## Verification and rollback

`tests/test_integrated_route.py` compiles the actual NXC helpers as C and executes
them with mocked motor/sensor APIs.25new tests cover ordered full-sequence control
flow, faults, mirrored pivots, counter resets, stopped resampling, marker gating,
no skipped stages, and logging while stopped. These traces intentionally provide
the expected sensor events; they do **not** validate the photograph, junction
references, compiler, simulator physics or physical route coverage.

The full audit environment reports **214tests passing**, including12additional
113regressions in `tests/test_integrated_approach.py`. They compare old/new behavior
on hypothetical traces (not a reconstruction of the243observed samples), verify
restored motor commands, marker budget baselines and unchanged pivot/exit/route
configuration. Five additional tests in `tests/test_integrated_junction_reference.py`
check the single parameter change, earlier mock endpoint, unchanged return/route,
early-loss stop and mocked full-sequence flow. They do not prove B is at370.
Five115tests in `tests/test_integrated_later_entry.py` compile the actual entry
header/helper code with mocked APIs, check the one-reference change, unchanged
pivot/exit bounds and full mocked flow. They do not establish real alignment.
Eleven116tests in `tests/test_integrated_continuous_flow.py` verify continued
outgoing following past200on a hypothetical trace, deferred progress, no skipped
pending leg, preserved first-exit origin, final-marker gating and real-fault stops.
They do not reproduce physical alignment or prove a circuit lap.116NBC compilation
and the integrated run remain pending. Latest evidence:
`evidence/robosim-115-gated-stop-continuous-116-2026-11-06.json`.

Rollback: load the preserved `robot_prueba_codo_mando.rxe` for37,111, or the retained
112RXEfor its recorded behavior. No111file or simulator configuration needs reverting.
Do not run the old corner program from the marker
position and assume it is a route program.
