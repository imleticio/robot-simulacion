# Session handoff — updated 2026-11-06

## Active next run — SAMEreactivefile38,3for explicitly selected original3/4robot

User clarifies target `robot_reactivo_simple.nxc` (NOTSim_Robot) and requires the
supplied ORIGINALpanel:3/4light/down,1/2pictured non-navigation/touch setup, A/C
side bars unchanged,Bunused. Do not push friend's1/2arrangement or ask again.
Source hash beforeedit matched38,2evidence; no user source changes overwritten.

Updated SAMEfileto38,3: Sensor/SetSensorLight3/4only. Previouspairedtests3left/4right,
Arightdrive/Cleftdrive determine CORRECTED pairing: left3blackA+25/C-7;right4black
A-7/C+25. Bothblack25/25,white20/20unchanged. Not a simple port-number substitution.
No reconfiguration/read of1/2for navigation; numericloggingIN1onlywhileoff, no
sensor type/mode change on1/2. Keep the whole panel as photo; do not infer exact
angles or turn perillas to match code.111andfriendfiles unchanged.

Uses old corner encoder knowledge only as SAFETYCEILING: sum signed sampledA-C
difference during same uninterrupted one-sided correction; atabs>=743stopreason11
ONLYif the NEXTcontactreading stillneedsSAMEcorrection. Bothblack/white/opposite
releasesresetsbudget. Shortcorrective turns do NOTwaitfor743orcommand90degrees.
Not oldbadwhole-leg60budget, not blocking200exitgate, not C743singletracktarget.
Inter-commandmotion/quantization meansnotexactbodyangle/containment guarantee.
Persistentlostalignmentstopsconservatively; do notraisebudgetblindly.

Gray/graystillSTOP(reason1afterstart/2initial) not automaticcorner/turn. Twofrontal
grayreadingscannotdecideleftversusrightorcorner/lateraldeparture. No defaultturn,
reverse-search,18script,estimatedjunctionposition or fakecoverageproof added.
Reactive corrections do intentionally reverseinnertrack,continuouslyguidedbyknown
blackcontact. Userwantsoldrobotwithreactivebehavior; fullcircuitstillunvalidated.

38,3frames26fields onPORT0zero-based(IN1), not oldport2. Prior24layout sensorfields
are nowleft3/right4, APPEND correctionState(0none/1left/2right),signedDifference.
Retainlastsnapshotonfaults; sensor1/2diagnosticsneverwriteactive3/4. Firstwhite
starts,nextrearmedreturncandidate stops; notvalidatedallbranches/twolaps. Startup
3nonwhitesampleswithatleastoneblack and markerblackcontactrule from38,2retained.

239audit testsPASS,25reactivetests. Five new cases ensureboundedpersistentturn,
recoveryATceilingnotfalsestopped,earlyrecoverywithouttarget,directionreset,white
reset. Updatedport/configisolation and actualleft/rightpairing tests. EntireNXC
compiledasCmockIO,NOTNBC/physics.38,3compilation/poweredruntime PENDING.

Next: keep/restoretheEXACTrequestedpanel(light3/4down,1/2asphoto,ACsame), do not
turnknobsagain. Close stale samefiletabWITHOUTsaving,reopenupdatedfilefromdisk,
compile/loadonlysuccessfulmatchingRXE,centeredbeforewhite,onesupervisedINTEGRATED
attempt;stopmanuallyondeparture/wrongbranch. Inspect26field38,3port0streambefore
adjustinganything. No isolatedcorner/calibrationtrial. CurrentguideREACTIVO_SIMPLE.md.
Engramwritesstillfail; localhandoffauthoritative.

## User redirects — original robot, reactive movement, reuse corner findings

User says they dislike the present result, prefer the original robot, and asks
to update "this code" with the prior corner findings but reactive movement.
Interpret preference as returning to verified original3/4light/A/Crobot, NOT
continuing to require friend's1/2arrangement. Original3=left,4=right mapping was
tested; do not blindly replace current1/2IDs without correcting motor pairing.
Preserve111files and Sim_Robotuserwork. Do not assume physical3/4knob settings
were preserved exactly or tell user to run an old program on the current1/2setup.

No source or pasted attachment identifies "this code" in this message. Ask ONE
clarification whether target is Sim_Robot.nxc adapted to original robot, rather
than overwrite friend's code or create another variant silently. Wait after asking.
Proposed intent only: simpler continuous reactive following, incorporate verified
sensor/motor/counter/safety knowledge; no18turnscript/unmeasuredjunctiondistances,
and no automatic equation of any gray loss with a real corner. Do not promise
two-sensorcorner/branch observability or full coverage without evidence. No new
controller/configuration change or trial requested yet.

## Current next run — SAMEreactivefile38,2fix one-sided startup rejection

User reports no start, supplies panel/pose image. ReadNEWport2zero-based log:
626473bytes,SHA256a47f7ae54748b4f507b806d7f1b38a97d7a65fe832db927588d79a0694cd9c10.
Threecomplete38,1frames allreason2samples0,TERMINALreadings49/49,49/49,49/0. Allcommands/deltas0,
no motion attempted. No ignoredmessages afterlatest.38,1NBC/startup/port3logging
are observed; actualpowered/reversecontrol was NOT entered/validated here.

Important:38,1unconditionallyreread sensors afterOff, so terminal49/0is NOTproof
it was the actual rejected startup sample.38,2now preserves failing sample on
faults; successful return/watchdog final resampling retained. Regression test
changes a later reading from49/49to49/0and confirms it cannot overwrite evidence.

Bug: both-black startup gate contradicted the reactive controller's validone-sided
corrections. Updated SAME `robot_reactivo_simple.nxc` to38,2(no new variantfile):
startup requires3consecutive non-white samples with at least one black sensor.
Marker arm/rearm uses SAMEknown-blackcontact rule; both-white confirmation remains
3. Mixedwhite+black,gray/grayandonly2qualifying samples cannotrearm. This also
ends white-release mode on3knownblackcontactsamples, not onlybothblack. Never feed
these candidates to a validated-coverage lapcounter. Candidate return not fullgoal.

Both-gray stillrejects/halts: reading49/49alonecannotdistinguishcenteredstraddling
footprintsfromactualofftrack; do not enableblindgrayforward, force00pose or tweak
perillas blindly. Latest49/0is a valid reactive contact case, but exact screenshot
toframe pairing not established. No evidence of motorstall or power loss.

Same1/2down arrangement,25/-7correctionpairing,white20,40flatperdrive,6000/400caps,
logIN3(port2zero-based),24fieldlayout,111andSimfilespreserved. BlackRunfieldnow
counts known non-whiteblackcontact,not bothblack. Mainstoppedloopstillforfaults.

234audit testsPASS,20reactivetests (4new regressions for one-sided startup/rearm,
no mixedwhite rearm and preserving rejecting sample), plus frameheader38,2check. EntireactualsourcecompiledasC
withmockAPIs,NOTNBC/physics.38,2compilation/poweredruntime PENDING. Updatedguide
REACTIVO_SIMPLE.md; new evidence records observedstartupframesandfix.

Next: keep currentconfiguration, close stale `robot_reactivo_simple.nxc` tab
WITHOUTsaving, reopenupdatedfilefromdisk, compile/loadsuccessfulmatchingRXE.
Samecenteredbeforewhiteintegratedstart; no calibration/isolatedcorner/knobchange
requested. Inspectnew38,2port2stream. Ifstill49/49do not removeguardblindly; if
49/0or0/49canbeginwithnormalcorrection. Fullphysicalroute/coverageunvalidated.
Engramwritesstillfail; localhandoffauthoritative.

## Active next run — standalone reactive38,1with friend's1/2sensor arrangement

User authorizes choosing replication/adaptation. Chose to replicate the friend's
downward1/2arrangement as a pair with a NEW standalone reactive controller, not
keep the guessed18turn route. Added `robot_reactivo_simple.nxc`, no includes,
map, angle targets, feature flags or forced90turn when both gray. Preserved all
111source/RXE and Sim_Robotuser files. No actual GUI reconfiguration/run performed.

Setup instruction: preserve current3/4panel reference; DO NOT turn3/4knobs or change
A/Cmotor side assignments. Set1/2to light/down, needles visually as friend image
(1upper-right,2upper-left; NOT exact numeric angles or independently measured
physical sides). Disable3/4with X, leave their angles untouched. A/Cassigned,Bunused.
Only compile/load NEW `robot_reactivo_simple.nxc` after this setup, before-white
original counterclockwise departure, both1/2footprints initially black. Restoring
old111/116requires previous3/4configuration, not merely loading an old RXE.
Stop the currently loaded program before reconfiguration/positioning.
Start CENTEREDonblackbeforewhite, not at an arbitrary pose chosen to force00.
Startuprequiresbothblack; if centerednew1/2setuprejects, inspect recordedvalues
without blindknobtuning. A straddling sensor arrangement can readgray/gray while
chassis is overblack; photo alone does NOT establish footprint placement. Gray
stop is a conservative compatibility guard, not proof body lefttrack. Do not
enable unconditionalgrayforward without resolving that observability issue.

Reactive rules preserve Sim_Robot's correction PAIRING BY ID, not its possibly
misnamedleft/right comments: bothblackA25/C25; only1blackAreverse7/Cforward25;
only2blackAforward25/Creverse7. White/release20/20. This is lower-power adaptation,
not exact reproduction of friend's70/20/forced60/gray40behavior. BOTHGRAYSTOPS;
no blind forward search, no fake next-corner declaration. Signed encoder baselines
AFTERcommands/readBEFOREOff; sentinel/sign faults and40flat intervals on either
commandeddrive stop; overall6000poweredinterval/white400sample watchdogs. Sample
budgets are not measured wall time/physical motion. Reverse correction is deliberate
as in friend's controller; containment/no-repeat compliance not asserted.

Threebothblackarm/rearm,threebothwhiteconfirm; firstconfirmedwhite sounds/start,
nextrearmedwhite sounds/STOPas RETURN CANDIDATE(reason100),NOT validatedlap/all
branches/twolaps. Existingvalidatedcoverage marker module NOT fed a fake flag.
If returnsbyshortloop/perimeteronly, objective is NOT completed; add only minimal
branch policy once actualfollowing/geometryevidence supports it. This is explicitly
a reactive comparison, not a claimed final assignment solution.

IMPORTANT LOG CHANGE: unusedIN_3(port2zero-based) numeric bridge, NEVER active1/2.
24fields38,1: reason,event,samples,s1,s2,started,candidate,armed,blackRun,whiteRun,
straight,correction1,correction2,markerIntervals,whiteAge,flatRun,deltaA,deltaC,
lastCommandA,lastCommandC,6000,400after38,1. Fullschema/reasonsREACTIVO_SIMPLE.md.
Read this stream, not oldport0/37frames. Logging only stopped. MainkeepsOffloop,
no taskend/strings/arrays/ANDORsourceoperators. ActualVMcompatibilitystillpending.

230audit testsPASS,16newtests compile ENTIRE actualNXCsource as C(mockAPIs,task
renamed not executed),including port isolation, graystop, reverse/sign/stall,
debounce/rearm and markerfinalresample. NOT NBC/physics/fullcoverage validation.
Qualitative scope/design8/10: onebounded program+setup comparison, excludes map/
script/angles/graysearch/complianceclaims;10needs sensor-side/correctioncontract
and observedminimalcoveragepolicy. Do not sell scores/tests as robot performance.

Next USERaction: physical setup above; compile one file in already-openBricxCC,
load only successfulmatchingRXE; ONESUPERVISEDINTEGRATED attempt frombeforewhite,
manualstopondeparture/steeringaway/wrongbranch. No isolated corner/calibration
trial requested. NBC/RoboSim38,1pending. No more choice menu; decision is made.
CurrentguideREACTIVO_SIMPLE.md. Engramstillfails; local continuityauthoritative.

## Friend configuration received — compare the program/setup pair

User supplied a close-up of the friend's robot panel. Sim_Robot source still
confirms IN_1/IN_2andSetSensorLight for both. In the capture1/2point downward,
their knob needles visibly lean in opposite directions; no exact numeric angles
or independently tested left/right sensor assignment can be read. Source comments
LEFT/RIGHTare not a physical-side measurement. Ports3/4are unused by that source;
A/Chave side bars and Bhas none. Do not infer absolute chassis left/right solely
from side-bar screen positions. Current verified program uses3/4for readings and
port1as SetInput numeric telemetry. A1/2adaptation must move/disable that bridge.

Do not blindly swap port numbers, copy70power/reverse/gray-forward logic or claim
the screenshot validates all-branch coverage. Proposed next step is an explicitly
separate simpler reactive controller paired with the friend's sensor arrangement,
preserving111source/RXE and documenting that its validation belongs to the OLD
3/4configuration. Physical reconfiguration has not been performed or authorized
unambiguously by this capture alone. Ask one question to confirm whether to
replicate this arrangement before changing robot setup. No newcode/117/runtime
or additional calibration trial requested this turn.

## Current discussion — simplify after comparison with friend's reactive follower

User clarifies Sim_Robot belongs to a friend, reportedly completes a lap with a
different robot configuration; asks whether our approach is overcomplicated.
Treat successful lap as USER-REPORTED, not independently verified full coverage.
Re-read sources: Sim_Robot is reactive sensor-based steering with no route map,
white-pass counter only, no visited-branch validation, and forward motion even
when neither sensor is black. It cannot by code alone establish all-black-branch
coverage, no repeated segment or three distinct valid marker crossings. Do not
equate this with saying the friend's observed run cannot work.

Our integration added18scripted turns/provisional B references and diagnostic
exit gates before solving reliable following/junction recognition. This exposed
configuration/temporal coupling and made correction burdensome. Friend's physical
sensor/motor setup is part of the controller; do not copy source/powers/reverse/
ports blindly into our verified3/4A/Cconfiguration or overwrite user work.

Design diagnostic (not runtime quality):2of8confirmed passes,2.5/10simplicity.
Pass: module purposes describable, intent comments exist. Fail/unverified rows
and specific fixes: interface simplicity -> one stable runnable controller rather
than exposed feature-flag/revision combinations; implementation independence ->
encapsulate mounting/motor config and reference origins; design-review habit ->
review simplification before new parameter patches; ownership of decisions ->
separate sensor-following from minimal branch-choice policy; newcomer-visible
boundaries -> document a single active program/config contract; strategic effort
-> replace patch accumulation with one measured integrated behavior baseline.
This is a qualitative design review, NOT an empirical performance score.

Recommended next direction is simpler continuous reactive following plus only
the junction decisions actually needed for all-branch coverage, not another
18turn/angle script. Proposed, not yet implemented/agreed or physically validated.
Next one question: request a capture of the EXACT robot configuration with which
the friend's program works, to compare the program+hardware setup as a pair.
No new117/source/config changes, no repeat execution or isolated turn requested.
111and Sim_Robot files preserved. Existing116route-cut evidence still applies.

## Current review —116cuts across route; executable identity needs clarification

User supplies several screenshots and says robot turns but cuts across black
route. Do not claim this is a valid lap or keep blind parameter-version changes.
Read stdout518024bytes,SHA256840df6ce4950b794e5ec8d94e4d8a813cb1b2826d530228bc061efc68f38d3ff.
Three started116attempt sequences reach turn3then reason6phase4(no stationary
black after full pivot). Latest: first exitpasses, B450followA365/C538thenright
pivotC743/A0; outgoing turn2follow107samplesA529/C378ends49/49and is accepted as
EDGE, so pendingBcredited. Then pivot2C745contact0/0; outgoingturn3s178A645/C935
ends49/49and is accepted as EDGE; pivot3C743ends49/49reason6. Earlier two started
attempts show same turn3contact failure, with different follow counts. These are
not matched poses or physical coverage proof.116NBC/runtime/continuous handoff
are now observed, superseding pending notes below. False edge attribution remains
possible: both-gray after progress is not independent proof of next corner.

Important new user/unfamiliar files: `Sim_Robot.nxc` and `.rxe` appeared locally;
RXEmtime11:57:05versus116RXE11:55:22. Source uses light ports1/2(not verified3/4),
booleanAND/OR, high70power, reverse corrections and40/40forward even if neither
sensor is black. Preserve this possible user work; NO edits/overwrites/deletes.
Do not assume its behavior/log belongs to116. Fullstdoutcontains4150ignoredor/and
messages in one inter-run block offsets392768..440400, between first116terminal
reason6and a later116invalid-start frame. No proof which RXE emitted this block;
do not blame116or user or assertSim_Robotruntime without confirmation.

Next single question: whether supplied screenshots are from
`robot_vuelta_integrada_continua.rxe` or `Sim_Robot.rxe`. This is an actual
configuration/program fork, not another request for a nonexistent track file.
Wait for user reply before changing controller/sensors or requesting a run.
No new117, source/RXE/reference/config changes made during this review.111preserved.

## Current next run — 37,116 continuous handoff, stop chaining exit diagnostics

User strongly objects to hours of trials without one complete lap, wants every
black branch covered and accepts any route order. Do not respond with another
small B-reference/angle change, more test-count reassurance or an isolated corner
trial. Acknowledge that motor/sensor work provided a base but navigation is NOT
delivered. No explicit waiver of official no-repeat/containment rules inferred.

Latest log373788bytes/hash in evidence/robosim-115-gated-stop-continuous-116-2026-11-06.json.
18complete115frames/no ignored messages. B450full pivots reachC744/745,A0;
exit200A345/C270stable3andA353/C233stable2,stage0/0then terminal49/0,reason15.
Both motors above180stilllack5freshbothblack. Thus370->450didnotresolve repeated
exit gate. Program explicitly braked in terminal loop; not observed lost-command
or physical stall. Do not claim cause of diagonal heading is proven, or raisecap.

Added `robot_vuelta_integrada_continua.nxc` revision37,116 and optional
ROUTE_CONTINUOUS_FLOW=1in shared route stages(default0retains112..115policy).
Keep first successful exit exactly as before to preserve B450reference origin.
For turns1..17, same full pivot/stationary contact -> continuous11120/10/25follower
on outgoing leg, NOT another blocking200interval180/5exit diagnostic. This is a
controller handoff redesign, not200->largertimeout or a failed exit relabeledPASS.

New pending state: after B/later pivot, pendingTurn=currentturn, completed count
does NOT advance. Only accepted next following trigger credits previous pending
step; final pending step credited only at confirmed expected white. Pending index
must equal completed count or fault25; cannot skip or finish incomplete sequence.
At phase2turn2pending1, robot is following OUT OF B toward next trigger, not yet
executing third pivot. First exit stillcredits first step only if its oldguardpasses.

Sensor/encoder/sign/sentinel/unexpectedwhite/40flat/firstleg400/laterleg2000/marker
guards remain. No reverse/search/retry. Existing edge trigger can still mistake
lateral loss for a planned corner; manual supervision remains essential. Counts
and pending triggers do NOT prove correct physical branch/no-repeat/containment.
Candidate full-branch route/B450/return450/powers/pivot743/375/40/RESET_NONE/sensors
unchanged.111baseline and priorRXEs preserved. First full physical lap unobserved.

Important origin change: FIRSTB450stillstarts after preservedexit0. RETURNB450,
previously afterexit6, nowstarts afterpivot6/contact in continuousflow. Value450
is unchanged but physical origin is not. This seed was never validated; observe
and fit if the run reaches it, do not claim it is a preserved calibrated distance.

116frames27fields: prior26layout with version116, APPEND pendingTurn(-1none).
Phase5exit logs only on first turn0; B/later successfulpivot logs carrypending,
then phase2following logs. Prior112..115frame lengths/policy retained bydefaultflag.

214audit testsPASS,11newtests compile actual116header/helpers as C with mockedIO.
Hypothetical outgoing tracecontinues230samplespastold200gate to next trigger;
pending/malformedstate/finalmarker/fault/firstexitguards verified. No realphysics
or coverage claim.116NBCcompilation/RoboSim PENDING. Do NOT sell unit tests as laps.

Next user action: compile/load NEW `robot_vuelta_integrada_continua.nxc` in ALREADY
OPENBricxCC, close stale shared-source buffers WITHOUT saving, only successfulRXE.
Same before-white departure/currentpatchedsimulator/sensors, ONEsupervisedINTEGRATED
attempt; stop manually on wrongbranch/departure. Inspect27field116frames and first
physical failure before more changes. GuideVUELTA_INTEGRADA.md. Engram stillfails;
local continuity authoritative.

## Current next run — 37,115 later B entry hypothesis after114exit failures

User reports turn followed by diagonal drift, supplies three screenshots. Actual
stdout302002bytes/hash in `evidence/robosim-114-exit-later-entry-115-2026-11-06.json`
has18complete26field114frames/two started attempts/no ignored messages. Second
turn DOES execute atB370: firstfollowA361/C379 -> pivotA0/C744in213samples,
contact0/49stable3 -> exit200A340/C169stable0final49/0reason15. Nextattempt:
followA352/C393 -> pivotA0/C745in210samples/contact0/49stable3 -> exit200A371/C202,
stable1,stage0/0then terminal49/0,reason15. Both retaincompletedTurns1. No lost
power mismatch observed; this is NOT incomplete second pivot or motor watchdog.
Single both-black at exit endpoint is NOT five fresh confirmations or alignment.

Counts/contact are compatible with leftward exit correction, matching qualitative
diagonal observation, but do NOT establish exact yaw, branch identity, early/late
entry or matched screenshot-to-phase timestamps. In particular, do not raise the
743target,375pivotcap or200exitcap to hide this contact/placement failure.

Added `robot_vuelta_integrada_cruce_tardio.nxc` revision37,115: ONLY revision and
firstB370->450relative to114. Extra80mean sampled counts tests slightly later
entry POSITION. Early-entry explanation remains a hypothesis, not proven cause
or measured B coordinate. Shared controller, successful first pivot/exit, route,
returnB450,marker/pivot/exit/caps/guards/sensors unchanged. First and returnB450
are separate unmeasured references, not one validated physical distance.111base
and112/113/114sources/RXEs preserved; no simulator commands/config changes.

203audit testsPASS,5newtests in tests/test_integrated_later_entry.py compile actual
115header/helpers as C, verify450reference, same pivot bounds, same failed-exit
guard, full mocked sequence and parameter-only entry diff. NOT runtime/geometry
validation.115NBCcompilation/RoboSim PENDING; first complete physical lap unseen.

Next: compile/load NEW `robot_vuelta_integrada_cruce_tardio.nxc` in ALREADY OPEN
BricxCC, close stale relevant buffers WITHOUT saving, only successfulmatchingRXE.
Before-white original departure, same sensors/currentpatchedsimulator, ONE
supervised INTEGRATED attempt; stop manually on departure/wrong branch. Inspect
26field37,115frames/first physical deviation before any further adjustment. No
unchanged114rerun or isolated-turn test requested. CurrentguideVUELTA_INTEGRADA.md.
Engram writes still fail; local continuity remains authoritative.

## Current next run — 37,114 advance provisional B reference after video review

User supplied Desktop `Grabación de pantalla 2026-11-06 a las 11.18.08 a. m..mov`.
Reviewed24.538s2184x128460fpsclip via2fpssheet,1fpsdetailfrom14s and full16.5/18.5s
frames. It shows first bend then straight-through passage at intended B branch
area and a gray-facing stop at far bend. Camera changes during passage; raw pixels
or timestamps cannot give an exact encoder/axle reference. Do NOT claim calibrated
B position, containment or an exact video-to-log run match.

Live log249022bytes/hash in `evidence/robosim-video-first-B-114-2026-11-06.json`.
Four distinct113phase2turn1/completed1/target1200line-loss endpoints give sampled
means736.5,760,710.5,731. Later started attempts also executed first left pivot/exit.
No ignored messages inspected. This supports that1200is unusable before the
observed far-edge stop, not a precise replacement B measurement or all-pose proof.

Added `robot_vuelta_integrada_cruce.nxc` revision37,114. Compared to113entry, ONLY
revision and first B reference1200->370change.370is the next earlier candidate at
roughly half the observed available following leg; NOT measured B location. It
can still be early/late. Origin remains after preceding exit. Shared113controller,
returnB450,markerbudgets,approach,firstpivot/exit,powers/angles/caps/guards/route/
sensors untouched. No reverse/search/retry or wrong-far-corner fallback added.
111baseline and112/113artifacts preserved. Do not tune the successful first pivot.

198audit testsPASS including5newtests in tests/test_integrated_junction_reference.py.
They show old1200miss/new370endpoint on a hypothetical trace, early loss still
aborts without wrong turn, returnreference/turn order unchanged, full mocked flow,
and entrypoints differing only revision/firstBmacro/comments. NOT physics/junction
validation.114NBCcompilation/RoboSimrun PENDING; first full physical lap unseen.

Next user action: compile/load NEW `robot_vuelta_integrada_cruce.nxc` in already
openBricxCC, only successfulmatchingRXE, unchanged sensors/currentpatchedsimulator.
Start BEFORE WHITE facing the original red departure. ONEsupervised integrated
attempt; manually stop on wrong branch/departure. Read26field37,114frames and
whether the right B turn is early/at-junction/late before further adjustment.
No unchanged113run or isolated corner trial requested. Current guide:
VUELTA_INTEGRADA.md. Engram writes still fail; local continuity authoritative.

## Latest113runtime — first pivot/exit observed; B reference not reached

User reports passing the second intended turn, continuing along the straight,
then stopping at its far bend; supplied a new endpoint screenshot. Read live log
ONCE at187573bytes,SHA256a41d2332a46992643a4a518bfbe489ea500f8195274cb18e33e65b1c2b257f01.
13complete26field113frames, no ignored messages in inspected log. These frames
include stage/final duplicates and initial rejections, NOT13complete attempts.

Started attempt: marker0phase0s45both100, releasephase1s198A506/C519final0/0;
first followphase2turn0s121A551/C531final49/50 -> LEFTpivotphase4s203A745/C0,
stationary contact3final0/49,203refreshes,0power mismatches,15/15latest ->
exitphase5s90A214/C191,5freshboth-black,final0/0,completedTurns1.
Thus113NBC/runtime and first LEFTpivot/exit criterion are OBSERVED, superseding
pending113notes below. This is not proof of exact heading/containment/route.

Next FOLLOW: reason11,phase2,turn1,completed1,right/reference1200,samples165,
totalsA713/C760,final49/49. Mean sampled total736.5 is below1200, so the controller
never scheduled the second pivot before stopping on loss of black. Retained
pivotA745/C0andrefresh203in this frame describe the PREVIOUS pivot, not a second
turn. This is not a pivot stall or sample watchdog. Later frames are reason2
invalid starts and reason11unstarted marker-stage losses; do not mix them with
the started attempt. Exact screenshot-to-frame timestamp pairing remains unknown.

The provisional1200Bseed was not usable before this observed line-loss endpoint.
Endpoint counts alone do NOT locate B, establish that loss was the geometric
end rather than lateral departure, or prove B was not already passed during the
mandatory exit. Do not pick a replacement number and label it measured, increase
pivot budgets, fall back to turning at the wrong far corner, or mark B covered.
No source/RXE/config/route/reference changes made for this review. Preserve111.
Next clarification: ask whether an EXISTING recording of this integrated attempt
shows departure through B to the stop; this would identify where the intended
second turn was passed. Do not request another unchanged run or isolated corner
trial. First full lap remains unvalidated; log/frame evidence saved separately.

## Current next run — 37,113 fix approach guard after first integrated failure

User reported robot remained at first curve and supplied screenshot. Actual112
log at143582bytes had11complete24field frames. Latest started attempt: marker
confirmed(s72,100/100), released(s207,0/0), THENreason19phase2turn0,samples243,
A528/C466,difference62,sensors0/50,completedTurns0,pivotA/C0/0,refreshes0. Thus
the stop happened BEFORE the first pivot, not because the left pivot stalled.
Image-to-frame timestamp pairing and individual sample history are unmeasured.
No ignored messages in inspected log.112NBC/runtime marker/following path observed.

While working, further112frames appeared without requesting another execution:
later snapshot157295bytes/18complete112frames includes unstarted-marker reason19
stops A457/C397,A383/C322,A365/C304,all0/50. Started0does not prove no white was
ever touched; only no marker was confirmed. Duplicated stage/final frames are
NOT separate runs.112initial rejection frames2/phase0have no motion. Root cause
of demonstrated termination is a controller error: the short continuation's
cumulative60difference budget was copied onto an entire correcting approach.
Do not attribute the pose to an unproven sensor setting, dragging or pivot failure.

Added `robot_vuelta_integrada_aproximacion.nxc` revision37,113. It restores111's
approach20/20both black,C10/A25left-only,C25/A10right-only before bends AND before
white contact. That approach has no short cumulative60stop; sensor/encoder/sign/
40flat guards remain. First bend leg watchdog REDUCED from2000to111's400samples;
later legs keep2000. No pivot target/sample/power increase or geometric retuning.

Marker stages retain800interval/1800average-count watchdog. White contact now
latches a crossing substage and records its own signed A-C baseline. ONLY this
crossing/release uses12/9and60relative difference budget, so prior approach
correction is not charged to crossing. Release starts latched after confirmed
startwhite. No auto-retry, reverse, search or skip added. Pivot/exit/route plan/
Bseeds1200/450 unchanged; actual full-route validity remains provisional.

New113frames have26fields:112's first24with version113, APPEND markerEntered,
markerDifferenceBase. Both retain the latest marker stage during following.
Inside a marker stage, compare current(A-C)-markerDifferenceBase to60.112default
featureflag0retains24fields and original policy;112entry point/RXE preserved.
All111baseline hashes match original evidence; no sensor/simulator changes.

193audit testsPASS, including12new113regressions executing actual helper code
as C. Hypothetical contact traces show old premature stop versus new edge/marker
arrival, NOT exact replay of the243unrecorded samples. New tests cover baseline
commands, marker budget origin, faults/caps, full mocked control flow and unchanged
pivot/exit/route preprocessing.113NBCcompilation/RoboSimrun STILL PENDING.

Next: compile/load NEW `robot_vuelta_integrada_aproximacion.nxc` in ALREADY OPEN
BricxCC; close stale shared-source tabs WITHOUT saving. Use only successful
matchingRXE, before-white start facing bottom-right departure, unchanged sensors,
ONEsupervised INTEGRATED attempt. Stop manually on wrong branch/departure. Do NOT
keep running112or ask for an isolated corner trial. Inspect fresh26field113frames
and first observed failure before edits. Detailed run instructions now in
VUELTA_INTEGRADA.md; evidence/frames/hashes in
`evidence/robosim-integrated-approach-113-2026-11-06.json`. Engram writes still fail;
this local handoff remains authoritative. First complete physical lap not yet seen.

## Current next run — 37,112 integrated first-route attempt, compile/runtime pending

User confirmed proceeding with photograph-based provisional references. Added
`robot_vuelta_integrada.nxc`, `robot_route_plan.nxc`, `robot_route_stages.nxc` and
`VUELTA_INTEGRADA.md`. All37,111baseline NXC/shared source/RXE preserved; hashes in
`evidence/robosim-integrated-route-112-2026-11-06.json`. This supersedes the earlier
integration-blocked notes below: no saved track file is required or available.

Program: stationary initial both-black3 -> expected white3with sound -> release
white/both-black3 ->18candidate ordered turn/exit stages -> expected white3with
sound and stop. Start BEFORE WHITE, pointing across it toward the bottom-right
bend in the user's red photograph (counterclockwise departure), NOT the old
isolated-corner start. Two full laps are intentionally not implemented yet.

Right pivot adapts111target743,power15,375samplecap,40flatguard,RESET_NONErefresh
and3stationary contact criterion; left pivots mirror A/C and are NEW/unvalidated
runtime geometry. Exit retains12/9,200intervals,both sampled totals>=180then5fresh
both-black readings and stopped resample. Following is ongoing12/9with2000interval
watchdog,40flatguard and signed60-count difference guard; no180diagnostic endpoint.
White is permitted only in marker stages, each bounded800intervals/1800average
sampledcounts. No reverse, search, retry, skip, strings, arrays, AND/OR or sounds
except accepted marker passages. Silent stopped task loop remains.

B branch references1200(index1)/450(index7) are UNMEASURED tuning seeds suggested
by relative photograph lengths, not surveyed distances or junction recognition.
Their origin is after the preceding controlled exit. Both-black is necessary
contact only, not proof of B. Upper stagger provisionally uses ordinary following
through a shared region, without two additional blind pivots; tight bends may
stop before the existing exit criterion completes. Check these hypotheses in the
integrated run rather than claim physically validated full coverage. Unexpected
line loss can resemble an expected corner; manual supervision is essential.

Fixed24field frames37,112log each stopped stage and terminal fault. Schema/reasons
in VUELTA_INTEGRADA.md. Reason100means CANDIDATE sequence plus expected marker,
NOT validated route/containment/no-repeat/assignment success. Existing validated-
coverage marker module remains untouched; no invented routeComplete flag supplied.

181testsPASS in auditvenv, including25new tests compiling/executing the actual
NXC helpers as C with mocked IO. Full mocked sequence has18completed stages and
2tones; faults cannot skip stages/claim finish. This is NOT NBC/RXE/physics or
photograph/branch validation. A direct existingwine64/nbc.exe -help probe exited
SIGFPEwithoutoutput; no new RXE generated. Verified BricxCCPID70692and patched
yieldPID72609stillrunning afterward. Do not retry/relaunch normal wrapper.

Live stdout was92507bytes/hash recorded in evidence, with12complete111frames.
Latest111reason19phase5: pivotA0/C748in192samples, exitcriterionpassed, THEN
continuation74/A104C165stopped on difference-61, final49/0. Another additional
111frame endedreason20one-sided continuation contact. These are NOT112runs and
do not establish a new root cause. Preserve the60guard; do not claim111reliable.

Next user action: use ALREADY OPEN BricxCC, close stale relevant tabs WITHOUT
saving, compile NEW `robot_vuelta_integrada.nxc` with its includes in this folder,
load only the successfully generated matchingRXE. Keep current simulator/sensor
settings, restore before-white departure, run ONCE supervised and stop immediately
on departure/wrong branch. Report first actual deviation/location; inspect fresh
112frames/ignored instructions before edits. No isolated turn rerun requested.
Engram writes still fail unknown_project; local continuity remains authoritative.

## User-confirmed red route — integration authorized, not implemented yet

User clarification: the track was built manually in RoboSim. There is NO saved
track file available; the supplied perspective photographs are the available map
evidence. Do not ask again for a track file or make one a prerequisite. The prior
assistant blocked integration on requesting such a file; that was not a useful
next step. Any image-derived junction distances remain explicit hypotheses to
check in the integrated supervised run, not measured/validated geometry.

The user supplied the official assignment image and then a red annotated route,
and explicitly authorized implementation. Follow that route rather than reopening
the upper-intersection semantics question: marker eastward -> B -> C -> right
loop -> C -> raised B-C detour -> B -> inner-left branch -> upper loop -> outer
left branch -> marker. Preserve37,111 unchanged as the tested local baseline.
The official text requires two traversals, initial counterclockwise departure,
no departure/repeated portion within each traversal, and a sound at each passage
over the white marker. A first-lap development milestone is not final acceptance.

Source inspection found an integration blocker:37,111 has only a both-gray
corner-entry trigger and ordinary black-contact following. It has no junction
detector, branch selector, or measured junction approach references. Both-black
also occurs on ordinary straights and cannot by itself identify B/C. A route
drawing defines desired branches but does not supply that runtime observation.
Do not silently substitute line-loss events for intersections or invent encoder
distances from perspective. No new NXC/RXE or simulator configuration was changed.
Bundled PDB contains EnvironmentEditor::writeToSerialization/loadFromSerialization;
no saved environment file was found in the simulator installation, its Desktop
copy, or the Wineskin application bundle. No GUI save/load or robot run occurred.
Engram writes still fail unknown_project; this local handoff is authoritative.

## User-directed next session — prioritize an end-to-end circuit attempt

The user wants to continue in another chat and explicitly redirects the work:
stop iterating on the isolated corner as the main objective. Build an integrated
circuit attempt, observe its actual failures, then adjust from runtime evidence.
They consider the current work too assumption-driven. Preserve revision37,111 as
the tested local baseline, not a validated navigation solution. Next session must
inspect the existing route evidence and assignment constraints, identify any
unresolved topology without inventing junction decisions, and work toward a first
complete circuit traversal with safety stops. Then address the required two laps.
Do not request another unchanged corner trial or claim full traversal already
works. This is a priority change, not evidence that local diagnostics were useless
or that a full lap alone proves repeatability. No navigation code changed here.

## Latest111 runtime — complete bounded path; command/RESET_NONE path observed

User reports execution (repeated message refers to the same review; do not request
another execution automatically). Live45358bytes, yieldPID72609 and BricxPID70692.
Four new complete76field111frames: firstthree reason2/phase0 rejected initial
49/49,0/49,0/49 with NO motion/approach/pivot, not failed corner attempts.
LATEST [37,111,17,5,232,200,0,0,3,0,0,0,746,0,746,44,743,375,49,49,163,75,88,0,0,0,200,3,0,30000,30000,30000,30000,0,0,0,30,30000,30000,163,338,189,0,0,2,2,1,180,5,5,83,52,0,31,124,180,0,0,0,2,1,180,120,60,0,0,0,0,200,0,0,40,200,0,15,15].
PivotA0/C746in200samples,progress200/flat0/longest0;200reassertions with ZERO
power mismatches,latestbefore15/after15. Thus MotorPower/OnFwdExRESET_NONE ran
without resetting the cumulative pivot encoder; no ignored messages afterlatest.
No lost-command event was observed in this pass, so do NOT claim command loss
was proven or that refresh fixed all earlier zero-progress failures.

Exit163(75both+88left),sampledA338/C189,freshstable5,thencontinuation83(52both+
31right),sampledA124/C180,entry/final0/0,status1,reason17programmedsegmentendpoint.
This run completed the bounded turn/exit/continuation, not fullcorner/legalheading/
containment/repeatability/twolaps.111NBCcompile/runtime now observed, superseding
pendingnotesbelow. No new source/config/angle/cap changes or duplicate trial
requested by this review. Keep111ascurrenttestedlocalbaseline;route/marker parked.

## Current next run — 37,111 maintain pivot command without resetting encoder

User asks what to do next; prepared an actual bounded control change, not another
unchanged110trial. `robot_prueba_codo_mando.nxc` revision37,111 preserves all110
geometry, powers, target743,375sample watchdog,40flat guard, exit and continuation.
Before each pivotWait, read MotorPower(C), reassert SAMEforward15 through
OnFwdEx(C,15,RESET_NONE), then read commanded power back. Keep the ORIGINAL
post-start C baseline; do not reset/restart/retry the pivot. A remains braked.
If before-power outside[-100,100], stop8; if after-power!=15, stop22 immediately.
If power15 but no physical/count progress, existingreason21 still stops; other
sensor/encoder/final guards remain. No auto search, secondturn, reverse or sounds.

This tests whether actively maintaining a command helps; NO evidence yet shows
the earlier40zero-progress run had power0 or a lost command. Power readback is
commanded state, NOT physical movement. Cannot fix a frozen/lifted physics state
by reasserting. Do NOT present it as an established root-cause fix.

Verified compatibility evidence before implementation: official NXC output docs
and bundledNBC define OnFwdEx and RESET_NONE0,Powerfield2. Actualx86setOutput
dispatcher tested with stubbackend: flags07 calls only commit slots7/8, whereas
legacyOnFwd flags2f also calls reset slots9/10. Direct power write and TachoLimit0
do not reset program rotation counter; getOutputfield2 implemented. This justifies
not repeating ordinaryOnFwd (which resets simulator counters). Evidence/addresses:
`evidence/robosim-pivot-command-refresh-2026-11-06.json`.

76fieldframe=110first72(version111)+turnRefreshCount,turnPowerMismatches,
turnPowerBefore,turnPowerAfter. Before/after are latest raw snapshots, initialized
30000 if unentered. Refreshes count commands, which can exceed turnSamples by1
if readback fails beforeWait. Mismatches count before-power!=15; after mismatch
stops22, not a success. Progress counters remain separate and unchanged.

156testsPASS in auditvenv, including wrapper/preprocessing checks, hypothetical
lost-command-vs-frozen-physics models, and3tests executing the realx86outputflag
dispatcher with a stubbackend. NOT a complete RXE/physics run. NBCcompile and
RoboSim111runtime PENDING, particularly newMotorPower/OnFwdEx path in real VM.
Legacy versions disable the feature and retain original telemetry/commands.

Next user action: use already-openBricxCC (doNOTrelaunchnormalPortingKitshortcut),
close stale shared-source tab WITHOUTsaving if open, compile/load NEW
`robot_prueba_codo_mando.rxe`. Keep currentyield.exe window/current sensor settings;
originalapproachstraight/bothblack,runONCEsupervised,stopondeparture. No newvideo,
calibration or knob adjustment. Read fresh76field111frame and ignored messages
before changing anything. FulltwoCCW university assignment still not implemented;
marker/route parked. Engram writes unavailable;localhandoffauthoritative.

## Latest110 runtime — successful continuation and explicit zero-progress failure

110compiled/ran in verifiedyieldPID72609; live21772bytes, TWOcomplete72fieldframes.
Firstreason21/phase1/approach25: turn40samples, A0/C0, progress0/flat40/longest40,
noexit/continuation. This is observed NO encoder progress, not hard375watchdog.
Latestreason17/phase5/approach194: pivotA0/C745in197samples, progress197/flat0/
longest0;exit146(72both+74left),sampledA323/C190,criterionstable5;continuation81
(51both+30right),sampledA131/C182,entry/final0/0,status1,firsttrack180endpoint.
No ignored messages after latest. New guard/counters executed; do not call the
latest motion a failure or claim bigger cap caused its success(it needed<240).
Evidence/fullframes: `evidence/robosim-110-runtime-and-input-state-2026-11-06.json`.

Read-only follow-up did NOT support the simple normal-pause hypothesis: togglePause
sets runner+0x34 and runner0x40a41e..0x40a422 stops VM execution when paused.
Separate mechanism identified: Single::setIsLifted0x41ae20 sets robot+0x294;
Robot::updatePhysics branches on it at0x411398, bypassing normal encoder integration
when lifted. Mouse manipulation begin/release dispatch this state (addresses in
evidence). This is NOT proof it happened during the failed run: no live lifted/
pause flag, input sequence or motor power trace exists. DO NOT blame user, assume
dragging/held-click, or present releasing the mouse as a verified fix. Normal
pause is not proven cause either. No new binary patch, source/config/limits
changes, calibration or identical run requested by this review. Keep university
demo focus; remaining zero-progress runtime/input-state cause unresolved.
Bounded successful110path does not certify fullcorner/repeatability/route/twolaps.
Older pending110runtime notes below superseded. Engram writes fail;localhandoff.

## Current goal clarification — university practical, not a prize contest

User clarified this is a university assignment assessed by demonstrating that it
works, not a prize competition. Prioritize a simple, explainable implementation
that fulfills the assignment; do not pursue speed optimization or contest polish.
This does NOT waive the previously stated two counterclockwise laps, starting
before white, full branch coverage and no repeated segment rules. Their route
interpretation remains unresolved; do not silently simplify away requirements.

## Current next run — 37,110 corrected nominal pivot budget and no-progress guard

Found a concrete budget inconsistency using the inspected motor model: ordinary
power15 =>150counts/s; target743 needs~4.953s. Old240Wait20samples give only4.8s
nominal and720idealcounts; ideal minimum is248samples. Actual cadence/physics is
not measured by those numbers. This DOES NOT explain C165at240samples or prove
all remaining stops are due to this budget. Evidence/assumptions:
`evidence/robosim-pivot-watchdog-budget-2026-11-06.json`.

Prepared `robot_prueba_codo_tiempo.nxc` revision37,110. Relative to109, keep the
same no-pre-advance geometry, power15, pivot target743, sensors, exit criterion
and bounded continuation. ONLY changes: pivot hard sample watchdog375(~7.5s
nominal, about1.5x248minimum) and optional observed-progress guard. Stop at target
as before, NOT at375. Stopreason21 if C fails to increase40consecutive samples;
reason7 if positive relativeC jumps backwards. These diagnose observed counts,
not motor-stall cause or wall-time. White/A-motion/sign/sentinel/other guards
remain. No new motor commands, APIs, angles, calibration, retry/search or sounds.
Historical wrappers default240 and omit the new guard/counters entirely.

72fieldframe=109first68(version110,turnSampleLimit375)+4pivot fields:
turnProgressSamples,turnFlatSamples,turnLongestFlat,TURN_NO_PROGRESS_LIMIT(40).
For normal valid motion progress+flat=turnSamples. Sensor/encoder faults before
classification may leave the sum smaller; no fabricated classification of those
samples. Any reason4/7/8/21 phase1 blocks exit/continuation. The new counters help
distinguish continuous slow progress from long repeated reads; they do not prove
why either happened. Reason17/phase5 remains the local-segment endpoint, not a lap.

146testsPASS in the existing auditvenv. Tests include the ideal20ms trace where
old240cap rejects C720 and newbudget reachesC744at248; zero/frozen/backwards/
sentinel/continuousslow cases, and preprocessing old68/new72field layouts with
identical motion/API-call counts. NBCcompile/runtime110PENDING. Latestlive log
still10591bytes with the two109frames recorded below; inspected BEFORE edits.

Next user action: use ALREADY OPEN BricxCC (do not relaunch normal PortingKit
shortcut, which previously coincided with closing the patched simulator), close
stale shared-source tabs WITHOUTsaving if open, compile/load NEW
`robot_prueba_codo_tiempo.rxe`. Keep the CURRENTyield.exe window and sensor settings,
restore original approach straight/both-black, runONCE supervised,stopondeparture.
No new video/calibration initially. Inspect fresh72field110frame before changes.
Scheduler-patch limitations and earlier incomplete pivots still matter. FulltwoCCW
route not implemented; marker parked. Engram writes fail; local handoff authoritative.

## Latest109 runtime — continuation passed once, partial-pivot symptom persists on patch

User compiled109 in BricxCC, reopened yield through Wineskin CMD after the earlier
simulator closed, and executed it. Currentprocesses:BricxCCPID70692,yieldPID72609.
Verified yield SHA256c16bc269df63aa2771477e942d8e315b68e4d2360eed241da2bd28c342423b0f
matches the audited patchedcopy. Do NOT diagnose an old original EXE as the cause
of the following failure. Exact pose/angles after reopening remain unmeasured.

Fresh log10591bytes has TWOcomplete68field109frames:
- Firstreason4/phase1: approach120,pivot240samples,A0/C165,turnBoth0,final49/0;
  no exit/continuation. Partial-pivot behavior STILL OCCURRED on the correct
  patched executable. Patch fixed a reproduced scheduler defect, not all symptoms.
- Latestreason17/phase5: approach180,pivotA0/C746in199samples,exit164(76both+88left),
  sampledexitA333/C190,freshstable5; THENcontinuation85(52both+33right),sampled
  A126/C180,entry0/0,final0/0,status1. Firsttrack180segmentlimit,notline-loss.
  Continuation difference-54 stays within60guard. No ignored messages afterlatest,
  stderr empty.109compile/runtime and phase5 executed; not a silent include/call
  failure or old RXE. Fullframes/hash/limitations:
  `evidence/robosim-yield-109-runtime-2026-11-06.json`.

No code/config/powers/caps changed after this review and no identical repeat run
requested. Report BOTH outcomes: latest completed its bounded extra segment, but
corner reliability remains unresolved because earlier pivot stoppedC165 before743.
Do not claim the scheduler patch fixes all stalls, infer an unproven cause, add
arbitrary cap extensions or represent the segment endpoint as a full route.
Marker/route work remains parked; no twoCCWlaps implemented. If further work is
authorized, investigate the remaining pivot-progress discrepancy independently
of the working continuation stage rather than repeat the same local tests blindly.
Engram writes unavailable; local handoff authoritative. Older pending109runtime
and PID64680 deployment notes are superseded by this new process/run evidence.

## Current next run — 37,109 no-advance corner plus existing local continuation

Second patched108run observed atlive7926bytes; PID64680stilltheyieldcopy:
[37,108,16,3,203,200,0,0,3,0,0,0,746,0,746,31,743,240,49,49,151,75,76,0,0,0,200,3,0,30000,30000,30000,30000,0,0,0,30,30000,30000,151,327,190,0,0,3,3,1,180,5,5].
PivotA0/C746in200samples;exit151(75both+76left),sampledA327/C190,stable5,
final0/0,reason16. No ignored messages after latest. First patched108run also
passed(exit152); no third identical trial requested. These TWOcriterionpasses
support trying continuation, NOT claiming repaired geometry/precise alignment,
matchedposes,all-loadschedulerproof,historicalstallattributionorfullroute.
Evidence `evidence/robosim-yield-second-runtime-2026-11-06.json`.

Prepared `robot_prueba_codo_continuo_sin_avance.nxc` revision37,109. It differs
from108 ONLY by revision and enabling the EXISTING106localcontinuation. Keep
POSITION_COUNT_TARGET0, all powers/pivot/contact/exitcriteria/caps, current sensor
setup and patchedsimulatorunchanged. Unlike106,109doesNOTreintroduce60pre-advance.
Phase5 ONLY after reason16/finalboth-black. The helper still stops atfirsttrack
180sampledcounts, difference+/-60 or120intervalwatchdog, with white/loss/fault
guards and finalresample. Reasons17endpointwithbothblack,18watchdog,19difference,
20inconclusivecontact are not route/corner/legalalignment successes. No second
turn, junction decision, marker counter, reverse, search or sounds.

68fieldframe=theexisting106layout,version109,positionTarget0. First50fields
retain108layout; appended18describeonlycontinuation (schema in106sectionbelow).
135testsPASS in auditvenv including realx86schedulerstubtests and2newwrapper/
preprocessing tests. New tests confirm108unchangedexceptcontinuationflag and
postpositioncodeidenticalto106exceptversion/positiontelemetry. This is NOT
NBCcompilation or109RoboSimvalidation: both are PENDING.

Next user action: compile/load NEW `robot_prueba_codo_continuo_sin_avance.rxe`
from matchingNXC (close stale shared-source tabs WITHOUTsaving if open). Use
CURRENTlegosimulator-yield.exe window, do not reopen/reset/retune. Restoreoriginal
approachstraight/bothblack,runONCEsupervised,stopondeparture. Expected existing
no-advancecorner/controlledexit -> short extra boundedfollowing -> stop. No new
video/calibrationinitially. Readfresh68field109framebeforeedits. Markerworkparked;
fulltwoCCWcoverage route unimplemented. Engramunavailable;localhandoffauthoritative.

## Current runtime — first patched RoboSim run completed the108criterion

Scheduler-patch deployment and first GUI run are now OBSERVED, superseding pending
instructions below. User opened the native embedded Wineskin utility at
`/Users/leonel/Applications/Simulador LEOG NXT.app/Contents/Wineskin.app`, then
Advanced > Tools > Command Line. CMD used `cd /d` into the simulator directory
viaZ: (verified prefix mapping to/) and launched `legosimulator-yield.exe`.
Process inspection confirms PID64680 runs the alternate executable. No default
wrapper startup change, EXE replacement, NXC/RXE edit, retuning or recalibration.

User supplied paired new/prior panel close-ups: A/C and3/4needlepositions agree
visually. Earlier assistant claim that the new angles were narrower was not
supported by these clearer images; explicitly corrected it. Do NOT request
further knob matching. Numeric angles and exact matched initial pose remain
unverified; do not silently treat image agreement as surveyed configuration.

First fresh patched log3963bytes contains ONE complete50field108frame:
[37,108,16,3,212,192,0,0,3,0,0,0,746,0,746,39,743,240,49,49,152,78,74,0,0,0,200,3,0,30000,30000,30000,30000,0,0,0,30,30000,30000,152,317,191,0,0,2,2,1,180,5,5].
PivotA0/C746in192samples,stableboth-black3,exit152intervals(78both+74left),
sampledA317/C191,status1,freshstable5afterboth>=180,final0/0,reason16before200cap.
No ignored messages anywhere in the reviewed fresh log. This demonstrates ONE
patched-runtime criterion pass, not that all scheduler timing/history/geometry
problems are fixed. Original also had passes, so do not infer improvement from
152vs169 or192vs196 without matched evidence.74one-sidedcorrections remain.
Evidence: `evidence/robosim-yield-first-runtime-2026-11-06.json`.

Next action: keep patched window, current sensor setup and existing108RXE fixed;
one supervised confirmation run from the original approach straight/both-black.
No recompile, new code, sensor calibration or video initially. This checks the new
patched runtime, not another geometry tuning cycle. Stop manually on departure.
Read fresh log before edits. Reason16 still intentionally stops the diagnostic;
no continuing route or two laps is implemented. Prior log archived separately,
since launching the new executable recreated the shared stdout. Marker work stays
parked; exactalignment/containment/legalcorner/fullroute remain unvalidated.
Engram writes still fail; local handoff authoritative.

## Current priority — scheduler correction prepared; GUI deployment pending

Read this section before older next-run instructions. Live stdout was checked
BEFORE any edits:125734bytes, latest108frames exactly match the two recorded below.
No new NXC revision, RXE compilation, motion tuning or user execution this session.

**Concrete defect:** the simulator VM runner can busy-spin across several Wait20
deadlines before returning to physics. A long interpreter batch therefore permits
multiple control samples with unchanged physics. Controller calls the VM before
Simulation::update. This invalidates assuming one Wait interval guarantees a new
physical state. Actual x86 runner emulation with deterministic clock/stub VM step:
120msbudget, original6samples/119stepcalls, fixed1sample/1stepcall before return.
This reproduces a scheduler defect, NOT the exact historical C193/C683 runs:
their log has no frame timing. Do not claim all variation is now explained.

Prepared a separate executable alongside the original:
`/Users/leonel/Downloads/BricxCC Simulator/legosimulator/legosimulator-yield.exe`.
One displacement byte changes: branch0x40a4a4, EBAF->EBA3, returning the runner
loop to its existing wait gate. Positive Wait yields to the controller; powers,
target743, sample guards and physics remain unchanged. Original EXE/resources,
ALL NXC/RXE preserved. Rollback is using original `legosimulator.exe`.
Version/hash-locked, exclusive-output builder: `tools/patch_robosim_yield.py`.
No live process patch or Windows launch performed. Runtime of copy is PENDING.

**Geometry investigated separately:** a relative90degree pivot preserves entry
heading error. Both-black start and simultaneous both-gray entry do not establish
zero heading or a unique axle location. Analytical terminal-edge counterexamples
give the same both-lost event but outgoing80/90/100degree headings. Omitting60counts
changes lateral placement (~0.20944units for ideal zero entry yaw), not heading.
Exit steering has the correct differential sign for C-left/A-right. No measured
active angles/map/pose justify changing geometry. Scheduler fix does NOT certify
alignment, containment, corner legality, route or two laps. Marker work stays parked.

**Verification:**133testsPASS using the temporary audit venv Python (124prior +
7scheduler/patch +2geometrycounterexamples). Scheduler tests execute real runner
machine code with mocked clock/VM payload, NOT fullRXE/GUI/physics. They require
unicorn+pefile; default Python skips7 if absent. Full command, hashes, addresses,
limits and evidence: `evidence/robosim-scheduler-audit-2026-11-06.json`.
Pre-deployment stdout preserved in `evidence/robosim-before-yield-2026-11-06.stdout.txt`.
Engram resolved the workspace correctly but reads/writes still fail unknown_project;
local continuity remains authoritative.

**Next single GUI intervention:** open `legosimulator-yield.exe` without closing
the existing simulator and WITHOUT running the robot. Preserve the current window
as the reference for scene/configuration; do not reset or retune sensors. First
establish that the alternate executable launches and how the exact existing scene
and sensor setup can be retained before any motion comparison. Do not silently
run on constructor-default angles or ask for approximate knob matching. Both
executables may share stdout; the prior log is already archived. No new video or
calibration requested. NXC unchanged, so no compile/reload instruction yet. If later
changing NXC, close stale buffers WITHOUT saving and compile/load the new RXE.

## Latest37,108 execution — one criterion pass, one incomplete pivot

Reviewed live stdout125734bytes. Two complete50field108frames, no ignored
messages after latest:
- Earlier [37,108,4,1,87,240,0,0,0,0,0,0,683,0,683,190,743,240,49,49,0,0,0,0,0,0,200,0,0,30000,30000,30000,30000,0,0,0,30,30000,30000,0,0,0,30000,30000,30000,30000,0,180,5,0].
  Pivot reached onlyC683/A0 at240samplewatchdog, reason4, no stationary check
  or exit. Both-black DURING partial pivot did not bypass angular reference.
  Cause of slower reported progress remains unproven; not a measured bad angle
  or authorization to remove the watchdog/change the target.
- LATEST [37,108,16,3,115,196,0,0,3,0,0,0,743,0,743,29,743,240,49,49,169,75,94,0,0,0,200,3,0,30000,30000,30000,30000,0,0,0,30,30000,30000,169,349,192,0,0,2,2,1,180,5,5].
  No pre-advance, pivotA0/C743, stationaryboth-black3, thenexit169intervals
  (75both-black,94left-only),sampledA349/C192,status1,5freshboth-black readings
  AFTERboth>=180,finalstopped0/0,reason16before200cap.

Thus108compile/runtime observed and latest bounded progress/contact criterion
passed. Omitting the advance did NOT eliminate prolonged one-sided correction
or the observed incomplete-pivot behavior. It is NOT a demonstrated positional
fix or improvement over105: initialposes were not measured/matched, so do not
rank runs by169vs132intervals or imply regression. Reason16 remains a deliberately
programmed endpoint, not continued route or fullcorner/heading/containment proof.
No new code/config/caps changed after review, no identical repeat run requested.
Keep focus on corner reliability and distinguish incomplete pivot timing/progress
from residual exit correction; do not treat these as one proven root cause.
Marker/continuation work remains parked, fulltwoCCWroute unimplemented.

## Current next run — 37,108 controlled exit without pre-pivot advance

107 DID execute; live stdout117804bytes contains two complete39fieldframes:
- Earlier [37,107,4,1,294,240,0,49,0,0,0,0,193,0,193,48,743,240,49,49,0,0,0,0,0,0,50,0,0,30000,30000,30000,30000,0,0,0,30,30000,30000].
  C193 after240samples, reason4 partial-pivot watchdog, never reached743/contact
  gate/exit. Cause unproven, NOT evidence of a fully rotated pose; do not blame
  the user or increase the pivot cap to conceal it.
- Latest [37,107,14,2,205,196,0,0,3,0,0,0,746,0,746,31,743,240,49,49,0,0,0,0,0,0,50,3,0,30000,30000,30000,30000,0,0,0,30,30000,30000].
  C746/A0 and three stationaryboth-black readings, reason14 intentional stop.
  PositionTarget0/samples0 and unused positioning fields confirm no pre-advance.
  No ignored messages after latest. This is ONE valid no-advance contact result,
  not a proven positional fix, exactheading, repeatable/legal corner or route.

Prepared `robot_prueba_codo_salida_sin_avance.nxc` revision37,108. Relative to105,
ONLY motion-geometry change remains POSITION_COUNT_TARGET0; all approach/pivot/
contact/exit powers, encoder accounting, guards and exitcriterion are identical.
Relative to107, enable the EXISTING controlled exit instead of observation-stop.
No continuation stage, secondturn, reverse/search/sounds, new caps or angle tuning.
Same50fieldlayout as105,version108,positionTarget0/unusedpositionfields30000.
Reason16=bothsampledexitmotortotals>=180 THEN5freshboth-blackreadings and final
both-black afterstop; NOT exactalignment/containment/routecompletion. Reason15
means criterion not established within200intervalwatchdog. Earlier incomplete
pivot/contact failures cannot enterexit; preserve reasons4/6/7/8 and white/loss.

124hosttestsPASS via `python3 -B -m unittest discover -s tests -p 'test_*.py'`.
New tests verify108differsfrom105onlyversion/position, preprocessed pivot+exit
matches105, and the observed partialpivot/one-sided counterexamples cannot pass.
NBCcompile/runtime108PENDING. Existing107/105/106sources and RXEs preserved.

Next user action: compile/load NEW `robot_prueba_codo_salida_sin_avance.rxe`
from its matchingNXC, same sensor spread/window, original approach straight with
both-black, runONCEsupervised,stopondeparture. Close stale shared-source editor
WITHOUTsaving if open. Expected approach -> pivotWITHOUTpre-advance -> stationary
check -> bounded existingexitONLYifcontactconfirmed -> stop. No recalibration,
newvideo or continuation requested. Inspectfresh50field108framebeforemoreedits.
TwoCCWfullcoverage lapsstillunimplemented;markerworkparked. Engramunavailable;
localhandoffauthoritative. Older next-run/pending107 notes below are superseded.

## Current next run — 37,107 corner-only, omit pre-pivot advance

User explicitly redirects work to the corner. Pause marker, lap and continuation
development. Prepared `robot_prueba_codo_sin_avance.nxc`, revision37,107: use the
existing original approach and A-braked/C743 pivot at15/cap240, but OMIT the entire
60-count positioning command. Then use the unchanged stationary three-same-contact
check and STOP, with no follower exit or continuation. This compares corner pose
against observation-only101, not route distance against106. Only the pre-pivot
movement changes relative to101; all sensor/motor settings stay unchanged.

Rationale: translating along the approach changes lateral placement relative to
an ideal perpendicular outgoing direction. The previous60counts correspond to
~0.20944sceneunits under the inspected scale; removing them changes position, not
the provisional743angle reference. This is an ISOLATED GEOMETRY HYPOTHESIS, not
proof of the failure cause or a guaranteed better pose. Exact yaw, current sensor
angles/footprints, starting pose and containment remain unverified. Old no-offset
tests predated the wider sensor configuration and do not validate this build.

Shared source now permits overriding POSITION_COUNT_TARGET; default60 unchanged.
When zero, preprocessing removes the positioning motor command, encoder reads
and Wait entirely, then enters the existing pivot. No zero-target pulse. Frame
layout39fields,version107,positionTarget0,positionSamples/deltas0; unused raw
position/sensor fields30000. Reason14=deliberate stable-contact observation stop
(may be one-sided), NOT alignment/corner completion. Reason6=reference reached
but no stable contact. Existing white/sign/sentinel/watchdog guards remain.

120 host tests PASS, including preprocessing comparison that all code after the
position stage matches101 apart from version/position telemetry. NBCcompile and
107runtime PENDING. New geometry has NOT run yet. User close stale shared-source
tab WITHOUT saving, compile/load NEW `robot_prueba_codo_sin_avance.rxe`, preserve
current sensor spread/window, restore original approach straight/both-black, run
ONCE supervised and stop manually on departure. Expected: approach -> pivot
WITHOUT extra pre-pivot advance -> stationary check -> silent stop. No forward
exit is expected in this isolated test. No sensor/motor recalibration requested.

Before editing, fresh log111502bytes also showed an additional106result:
[37,106,20,5,85,181,49,0,3,0,0,0,744,0,744,28,743,240,49,49,121,69,52,0,0,0,200,3,16,0,0,65,65,65,65,60,30,49,49,121,291,191,0,0,2,2,1,180,5,5,71,56,0,15,155,180,0,0,3,3,1,180,120,60,0,0,49,0].
Earlier criterion passed; continuation71intervals/A155C180 ended one-sided49/0,
so reason20 correctly remained inconclusive, not a completed aligned segment.
This does not prove that removing the advance fixes it. Preserve these106files
and results. Inspect fresh39field107frame BEFORE another change. Full twoCCWlaps
remain unimplemented, route/legal corner unvalidated. Engram writes unavailable;
local handoff is authoritative. Older next-run sections below are historical.

## Latest37,106 runtime — continuation executed in latest run; earlier run blocked

User says motion still looks the same/no continuation. Verified live stdout at
106226bytes: TWOcomplete68field106frames, not an old105RXE. No ignored messages
after latest. New helper function-call/encoder/telemetry path executed in latest
run; do not falsely diagnose an ignored helper or failure to load106.

Earlier106frame: [37,106,15,3,204,196,49,0,3,0,0,0,745,0,745,0,743,240,49,49,200,26,0,174,49,0,200,2,18,0,0,64,64,64,64,60,30,49,49,200,58,355,0,0,0,1,1,180,5,0,0,0,0,0,0,0,30000,30000,30000,30000,0,180,120,60,30000,30000,30000,30000].
Reason15/phase3:200exitintervals,174right-only,A58/C355,stable0. The preceding
exit criterion did not pass, so phase5 correctly remained unentered/sentinels.
This is another repeatability failure, not a continuation-code fault.

LATEST106frame: [37,106,17,5,119,192,0,0,3,0,0,0,745,0,745,45,743,240,49,49,157,75,82,0,0,0,200,3,16,0,0,62,62,62,62,60,30,49,49,157,347,197,0,0,5,5,1,180,5,5,77,49,0,28,128,180,0,0,3,3,1,180,120,60,0,0,0,0].
Reason17/phase5: earlierexit157intervals/criterionpassed,THEN77independent
continuationintervals(49both-black,28right-only),sampledtotalsA128/C180,
entry0/0,final0/0,status1. It stopped at the deliberately short FIRST-track180
reference, not a sensor fault or ignored command. Totaldifference-52 stayed
inside60guard. These are sampled motor increments, not proof of exact visible
distance, heading, legal corner/fullroute. Do not deny the user's visual impression
or claim a long straight was traversed. The test was deliberately short and still
does not implement ongoing route navigation.

No code/parameter/config changes made for this review. Do not request another
identical run/video or extend arbitrary bounds as if that fixed the unreliable
exit. Explain the difference between the blocked earlier run and latest phase5
endpoint. Earlier105/106one-sided failures remain unresolved; marker work parked,
twoCCWfullcoverage route unimplemented. All pending106runtime notes below are
superseded by this evidence.

## Current next run — 37,106 bounded continuation after the exit criterion

User authorized actual continuation beyond the intentional 105 endpoint. New
`robot_prueba_continuacion.nxc` preserves all 105 approach/position/pivot/exit
settings and enables phase5 ONLY after reason16 and its stopped both-black check.
New helper `robot_continuation_stage.nxc` rechecks both-black entry, follows with
the same12/12 and braked9 corrections, and uses INDEPENDENT per-interval encoder
baselines/totals. Original exit measurements remain separate. No sensor settings,
pivot constants, marker integration, second turn, reverse, search or sounds added.

Continuation bounds (experimental motor references, not physical distances):
- Stop at FIRST sampled track total>=180, not after compensating for the other.
- Stop when signed sampled A-C difference reaches +60 or -60; this limits sampled
  turning tendency, not exact yaw. Net difference cannot prove alignment.
- Stop at120interval watchdog if progress criteria have not stopped it earlier.
- White/neither-black stop1/11; sentinel/negative increments stop8/7. Baseline
  sentinel stops before waiting. Post-stop sensor checks catch final-interval
  loss/white and downgrade one-sided endpoint contact.

New reasons in phase5:17=sampled segment limit WITH finalboth-black,18=watchdog,
19=sampled track-difference guard,20=inconclusive entry/endpoint contact.
None means next-corner arrival, legal alignment, full containment or lap success.
The stage cannot identify junctions and must not be treated as route navigation.
Supervise and stop manually on departure; sampled counts omit inter-command
motion and quantization, so these bounds do not guarantee exact footprint travel.

68-field frame: first50 retain105layout (version106, final reason/phase/readings
may now refer to phase5). Append18: continueSamples,continueBothSamples,
continueLeftSamples,continueRightSamples,continueTotalA,continueTotalC,
continueStartA,continueStartC,continueCurrentA,continueCurrentC,
continueEncoderStatus,CONTINUE_COUNT_LIMIT(180),CONTINUE_SAMPLE_LIMIT(120),
CONTINUE_DIFFERENCE_LIMIT(60),continueEntryLeft,continueEntryRight,
continueFinalLeft,continueFinalRight. Unentered raw/entry/final fields30000,
counts0/status0. Status1valid(includingzero),2sentinel,3negative. Statecounts
describe completed command intervals; baseline fault beforeWait counts no interval.
Phase5 implies the earlier reason16 passed; no independent route claim follows.

116 host tests PASS: `python3 -B -m unittest discover -s tests -p 'test_*.py'`.
17 new tests compile and execute the actual helper as C with simulated APIs,
including resets, correction bounds, zero/stall/faults, final resamples and entry
rejection. Preprocessing confirms105still50fields and106has68, gateonlyreason16.
NOT NBC compilation or RoboSim validation: the new helper function-call boundary
and simulator behavior remain pending along with the motion stage itself.

Next user action: close stale shared-source tabs WITHOUT saving, compile/load NEW
`robot_prueba_continuacion.rxe`, keep the same sensor spread/window, restore the
original approach straight/both-black and run ONCE supervised. Never load an old
RXE after compilation errors. Expected: existing turn/exit -> short extra local
following ONLY if criterion passed -> safe stop. No new calibration/video needed
initially. Last observed live log95657bytes; inspect fresh68field106frame and
ignored instructions before more edits. Older105failures remain unresolved;
corner legality/fullroute/twoCCWlaps are NOT validated. Marker work stays parked.
Engram writes still fail; this local handoff is authoritative.

## Latest controlled-exit video — intentional criterion stop, not a new failure

Reviewed accessible Desktop video `Grabación de pantalla 2026-11-06 a las 2.44.35 a. m..mov`
(14.89s,2184x1284) at2fps plus fullresolution endpoint14.3s. Shows approach,
rightward arc, short outgoing translation and stop. It does not demonstrate
continued tracking to another corner, exact parallel heading or containment.
Evidence/hash/fullframes: `evidence/robosim-video-review-2026-11-06-024435.json`.
Do not ask for another generic video of this same successful-stop behavior.

Live stdout95657bytes has FOURnew105frames since79846: allreason16/final0/0,
exitintervals144,130,124,148,eachbothsampledtotals>=180andfreshstable5before200cap.
Latest [37,105,16,3,115,195,0,0,3,0,0,0,746,0,746,42,743,240,49,49,148,72,76,0,0,0,200,3,16,0,0,62,62,62,62,60,30,49,49,148,318,188,0,0,3,3,1,180,5,5].
No ignored messages since latest. Exactvideo/framepairunknown,butALLnewframes
areintentionalcriterionstops,notloss/confirmationfailures. Explain clearly:
thecodeINTENTIONALLYendsitsmotionhere;lookingstationaryatendpointdoesnotmean
itgotstuck. Do NOT claimthisspecificvideoconfirmstheearlierreason6failure.

Fournewpassesstrengthenevidenceforboundedprogress/contactbutdoNOTeraseprior
105reason15exitandreason6contactfailures,norproveexactheading,fullcornerlegality,
matchedstartposesorfullroute. No new code/config changes. Marker work remains
parked. Next functional work needs explicitly scoped continuation beyond the
diagnostic endpoint with safety guards and route/junction constraints; do NOT
blindlyaddsecondturnsorencodeunvalidatedfullcoveragepaths. CurrentprogramhasNO
suchcontinuation. TwoCCWfullcoverage lapsstillnotimplemented.

## PRIORITY RESET — corner not repeatable; marker work parked

User correctly objects that corner reliability must precede marker/route work.
Fresh live log review at79846bytes found FIVEadditional105frames aftertheprevious
60018byteread: threeinvalidstarts(no motion), oneexitwatchdogfailure,andonepivot
contactfailure. These supersede any suggestionthat105isreliablyworking.

- Exit failure: [37,105,15,3,370,174,49,0,3,0,0,0,746,0,746,0,743,240,49,49,200,22,0,178,49,0,200,2,14,0,0,60,60,60,60,60,30,49,49,200,57,417,0,0,0,2,1,180,5,0].
  Reason15,exit200with178right-onlycorrections,sampledA57/C417,nevermetboth-track
  reference. Contactalonewasnotalignedexit; no capextension.
- Latest actual maneuver (latest overall frame isinvalidstart):
  [37,105,6,2,52,197,49,49,0,0,0,0,743,0,743,0,743,240,49,49,0,0,0,0,0,0,200,0,16,0,0,64,64,64,64,60,30,49,49,0,0,0,30000,30000,30000,30000,0,180,5,0].
  Position64/64,pivotA0/C743,stationarybothgray,stable0,exit0. Thus a real remaining
  failure occurs BEFORE exit steering; the new exit criterion cannot fix pivot
  landing/contact. Exact heading/placement/cause unproven; do not blame user.

No fresh ignored messages in inspected maneuver suffixes.105hasoneearlierreason16
pass,butlaterfailuresshowitISNOTrepeatable. Stopmarker/lapintegrationandfurther
exitcap/powerchanges. Focus investigation on approach/position/pivot trajectory
and outgoing contact. Existing103video doesnotcapturethisspecific105failure;
ifadditionalvisualevidenceisneeded,itmustshowthefailed105turnthroughthefirststop,
notanothergenericstoppedimageorsensorcalibration. No code/settingschangedinthis
review; no identicalblindrerun requested. TwoCCWlapgoal unchanged.

## Latest development — guarded marker tracker from the user's reference

User authorized using the supplied simpler follower as a reference, not replacing
the existing model. Added `robot_marker_tracker.nxc`: an API-free reusable include
with no task, motion, sound, sensor calls or GUI changes. Do not ask the user to
compile/load this module as a standalone executable.

Behavior:
- Start disarmed; three consecutive both-black samples arm a crossing.
- Three consecutive both-white samples confirm it. Gray, mixed readings or
  fewer than three black samples never rearm a consumed crossing.
- First accepted crossing starts the run (zero laps). The next two accepted
  crossings finish laps 1 and 2; finished state latches.
- After start, `routeComplete == 1` is required at the confirmed crossing.
  The caller must derive this from validated per-lap route coverage and advance
  or reset its route state on START/LAP/FINISH. Never hardcode permission to 1.
- Premature crossings produce REJECTED and are consumed, so setting permission
  later while parked on white cannot count the same crossing.
- Inputs outside scaled range0..100 produce INVALID, clear debounce and disarm.
  State machine reports events; future caller must stop on faults/finish.

`tests/test_marker_tracker.py` compiles the actual API-free NXC module as C using
Clang and executes it via ctypes: 21 new tests. Full suite: **99 PASS**, using
`python3 -B -m unittest discover -s tests -p 'test_*.py'`. This is stronger than
a separate Python model, but is NOT NBC compilation or RoboSim runtime validation.
Three-sample both-white coverage/debounce remains provisional for the real marker.

No existing corner source/RXE, motor parameters, caps or sensor settings changed.
37,105 has ONE observed valid criterion pass; its optional confirmation run was
not reported after that result. Marker module is NOT integrated into a moving
route; corner diagnostics still stop on white. Route topology, legal intersection
decisions, counterclockwise coverage and two-lap competition program remain
unresolved. README records the integration contract. No new user execution is
needed for this host-side increment; do not resume calibration or invent a route.
Engram writes still fail; this local handoff is authoritative.

## Latest37,105 result — bounded progress/contact criterion PASSED once

Live stdout60018bytes: oneinvalidstart49/0(no motion),thenlatestcomplete50fieldframe [37,105,16,3,100,192,0,0,3,0,0,0,745,0,745,29,743,240,49,49,132,80,52,0,0,0,200,3,15,0,0,60,60,60,60,60,30,49,49,132,279,189,0,0,3,3,1,180,5,5]. Position60/60,pivotA0/C745,stationaryboth-black3,exit132intervals(80both+52left),sampledtotalsA279/C189,132validmeasurements/status1,5freshboth-blackreadingsAFTERboth>=180,andfinalstopped0/0. Reason16meanscriterionpassedBEFORE200watchdog,NOTcapcompletion/routecompletion. No freshignoredmessages. 105compile/runtimeobserved;thisisfirstvalidpassofthenewcriterion,notexactheading/containment/legalcorner/fullroutevalidation. Thepreviousinvalidstartisnotamaneuverfailureandmustnotbeconfusedwithlatest.

Keepcode/powers/caps/sensorsunchanged. NextoneconfirmationrunofSAME105fromoriginalapproachstraight/both-black,supervisedstopondeparture,tocheckthisnewcriterionisrepeatablebeforeintegratinganything. No recompile/calibration/newvideo/settingschanges;no additionalparameterexperimentsbasedonthispass. TwoCCWfullcoverage lapsandintersectionroute remainunimplemented/unvalidated. Inspectfresh105logbeforechanges. Allpending-runtimenotesbelowaresuperseded.

## Current next run — 37,105 bounded two-track progress/contact criterion

User delegates implementation after104showed100right-onlycorrectioncounterexample. New `robot_prueba_salida_controlada.nxc` revision37,105 keeps sensor spread, approach,position60,pivot743,stationarycontactgate,andexitpowers12/12/braked9. Replaces cap-as-endpoint with diagnostic criterion: BOTH sampledexitmotor totals>=180, THEN5freshconsecutiveboth-black samples, followedbyboth-blackagainafterbraking. Reason16meansONLYthisboundedprogress/contactcriterionpassed, NOT exactheading, containment, fullcorner or routecompletion. One-sidedcontactresetsconfirmation; allblackbeforebothprogressreferencesdoesnotcount. Sampledcountsremainincompleteodometry,notphysicaldistance/bodydegrees.180isaprovisionalmotorreferencechosenaboveweakertrackprogressinthe104runswherebothtracksadvanced(122and155),notameasuredsafeexitdistance.

Watchdog200exitintervals (previous100) gives boundedopportunitytoreacquirecontactbeyondoldcutoff; it is NOT success andnominaldurationisnotmeasuredruntime. Reason15=criterionnotestablishedwithincap ORlostonecontactaftercriterionstop. White/neitherblackstillreason1/11atnextsampleandafterfinalinterval;encoderfaults7/8retained. Ifallright-onlypersists,onewheelzeroortotalszero,itcannotpasscriterion. No secondturn/search/blindgrayadvance/reverse/sounds. This changes termination and maximumobservationwindow, NOT the steeringlaw, and doesnotguaranteealignmentwillrecover. Superviseandstopondeparture.

New50fieldframe=104first47unchangedexceptversion105/exitStepLimit200,append3:EXIT_PROGRESS_TARGET(180),EXIT_CENTER_SAMPLES(5),exitCenteredSamples. Stablecontactsamplesareonlycollectedafterbothmotorreferences; statecounts/exitSamplescontinuecountingcommandedintervals,sostopcriteriareadingitselfdoesnotaddamotioninterval. Originalposition/turnfieldsremainindependent. Default100..104wrapperspreservetheirpreviouscriteria/layouts.78Pythonmodel/staticchecksPASS,includingclangpreprocessing39/47/50layoutsandguard/counterexample/finalresampletests;NBCcompile/runtime105PENDING.

Next user action: close stale shared-sourcebufferWITHOUTsaving,compile/loadNEW `robot_prueba_salida_controlada.rxe`,samecurrentsensors/simulatorwindow,restoreoriginalapproachstraightbothblack,runONCE supervised. No calibration/newvideoinitially. Lastobservedlog52094bytes;inspectfresh50field105frameandignoredmessagesbeforeadditionalchanges. TwoCCWfullcoverage lapsfrombeforewhitemarkerremainUNIMPLEMENTED;105isNOTcompetitioncode. Engramwritesunavailable;localhandoffauthoritative. Olderpendingnext-runnotesbelowaresuperseded.

## Latest37,104 runtime — sampled movement works, cap is not an exit-success criterion

User ran `robot_prueba_salida_medida.nxc` and observes no visual difference; explain that104intentionallypreserved103motion and onlyaddedmeasurements. Live stdout52094bytes contains THREEcomplete47field104frames, allreason10phase3exit100/status1/measuredSamples100, nofreshignoredmessages. First approach180/position65/65/pivotC743/exit61both+39left/final0/49/totalsA218C155. Middle approach67/position60/60/pivotC744/confirmed49/0(state2)/exit0both+0left+100right/final49/0/totalsA0C171. LATEST [37,104,10,3,109,190,0,49,3,0,0,0,747,0,747,46,743,240,49,49,100,44,56,0,0,0,100,3,14,0,0,62,62,62,62,60,30,49,49,100,221,122,0,0,0,0,1]. Latestexit44both+56left,final0/49,sampledtotalsA221C122,lastinterval0/0reported,status1(zerosvalidnottravel). Source/RXE104compilation/runtime now observed. This supports sampledmotorreadsduringexit,notlosslessfullodometry/preciseheading/distance.

Crucialcounterexample: middlevalidcontactrun spent ALL100exitintervals inright-only correction, withA0/C171sampledcounts. Existingbrakedtracksteeringcanconsumeentireobservationwindowwithoutanyboth-blackforwardcommand. Therefore reason10blackcontactdoesNOTmeanaline-recoveredoutgoingstraight; prior100capresults mustnotbepromotedtocornersuccess. Persistentone-sidedcontactisanunresolvednavigationstate,notsuccess. Causeofpose/configvariationnotidentified. No newcode/configchanges basedonthisreview; do notrequestanidenticalmeasurementrerun/recalibration. Needseparatealignment/reacquisitioncriterionfromsamplecapanddrivetravelbeforeintegratingroute. Usergoalremainstwocounterclockwisefullcoverage laps fromstartbeforewhitemarker;104isdiagnosticonly.

## Current next run — 37,104 sampled exit encoder measurement

User asks for code to continue; prepared `robot_prueba_salida_medida.nxc` revision37,104. Same approach/position60/pivot743/contact check/exit100 and powers12/12,braked9 as37,103; no extra turn/search/reverse/sounds. ONLY optional exit-encoder accounting added. Commands can reset counts, so EVERY exit interval reads fresh A/C baselines AFTER all motor commands, Wait20, then reads A/C BEFORE any next command or Off. Adds nonnegative differences to separate A/C totals. These are SAMPLED motor increments, NOT full outgoing odometry, physical distance, total yaw, or alignment: motion outside sampling windows and quantization are omitted. Extra reads may affect runtime timing. Do not set a distance stop from these numbers until runtime support/progress verified.

New47-field frame: first39positions unchanged exceptrevision104. Append8: exitMeasuredSamples,exitTotalA,exitTotalC,exitStartA,exitStartC,exitCurrentA,exitCurrentC,exitEncoderStatus. Raw finalinterval values are separate from original TURN snapshots. Status0=no measurement,1=validinclzero,2=sentinel,3=negativeintervaldelta. After each20msinterval, any baseline/current30000 stopsreason8; anynegativedeltastopsreason7 (phase3). Totals include ONLY priorvalidintervals; failedintervalstillcounts in exitSamples and statecounts, so exitMeasuredSamples=exitSamples-1onmeasurementfault. Zero is reported aszero, NOTproofofworkingodometryortravel, and existing100capboundsstall. No measurement ifexitblocked. White/neitherblack guards and finalstoppedsensorresamplingretained. Defaultsource/103andearlierwrappers compilewithout optionalencoderblocks and retain39fields.

67Pythonmodel/statictestsPASS via `python3 -B -m unittest discover -s tests -p 'test_*.py'`. Includes intervalreset/nonzerobaseline/one-sided/zero/sentinel/sign cases and actualclangPREPROCESSING39vs47fields, unchangedmotioncommandcounts/cap. This is NOT NBC/NXC compilation or RoboSimexecution. NXCcompile/runtime104PENDING. User close stale shared-sourceeditorWITHOUTsaving, compile/load NEW `robot_prueba_salida_medida.rxe` fromsamefolderasinclude. Keep current sensor spread/window unchanged, restoreoriginalapproachstraightbothblack, runONCE supervised, stop manuallyondeparture. No newvideo/calibrationneeded initially. Latestpretestruntimelog40901bytes (append/truncationnotguaranteed). Inspect fresh47field104frame and freshignoredmessages BEFORE furtheredits. Engramwritesunavailable;thishandoffauthoritative. Allnext-runsectionsbelowhistorical.

## Latest video review — short outgoing translation observed, no new revision

Reviewed user's10.623333s2184x1284video `/Users/leonel/Desktop/Grabación de pantalla 2026-11-06 a las 2.03.37 a. m..mov` via2fps contact sheet/largerframes/final10.4sframe. Shows approach,rightwardarc,SHORToutgoingtranslation,thenstationary. Not a wholly stuck chassis or uninterrupted in-place spin; does NOT establish a long aligned exit, fullcontainment or nextcorner. Final rendered housings cannot prove sensor footprints. Evidence/hash/limitations saved `evidence/robosim-video-review-2026-11-06-020337.json`.

Live stdout40901bytes adds TWO37,103frames, bothreason10cap100/final0/49. Latest [37,103,10,3,139,192,0,49,3,0,0,0,745,0,745,35,743,240,49,49,100,52,48,0,0,0,100,3,16,0,0,62,62,62,62,60,30,49,49]; precedingvalidnewframeapproach159/turn195/position64/64/exit49both+51left. Latestexit52both+48left. No ignored messages since latest. Exactvideo-to-framepair not established; both newruns are consistent with programmedcapstop, not freshline-loss. Together with priorvalid103, THREEvalid100caprunsretainleftblack under currentapproximatewiderspread, but earlierpositionstall remains unresolved and these are not fullroute/containment/longstraight validation. No new code/config changes, no recalibration or repeatvideo requested by this review. Do not portray longer cap alone as a solution; next development needs a meaningful bounded outgoing-travel/alignment criterion before adding navigation or anotherturn.

## Latest result — 37,103 executed, do not extend cap again yet

Live stdout34611bytes contains two new37,103 frames. Earlier [37,103,12,4,57,0,49,0,0,30000,30000,30000,30000,0,0,0,743,240,49,49,0,0,0,0,0,0,100,0,30,0,0,0,0,0,0,60,30,49,0]: positioningcap30 with reported0/0encoderprogress, no pivot/exit; cause unproven, do not hide or blame user. LATEST [37,103,10,3,195,201,0,49,3,0,0,0,747,0,747,44,743,240,49,49,100,49,51,0,0,0,100,3,17,0,0,62,62,62,62,60,30,49,49]: position62/62,pivotA0/C747,stationaryboth-blackstable3,exit100intervals (49both-black,51left-only,0right-only),final0/49,reason10programmedcap. No ignored messages after latestframe. Compile/runtime of103 now observed. This demonstrates contact retained to extended cap in one run, NOT sustained forward exit, actual distance, heading, containment, correction recovery, repeatability or fullcorner/fullroute. Exit encoders are NOT logged and motor fields remain pivot snapshots; left-only commands brakeC/advanceA9, so100intervals cannot be called100forwardsteps. Counts alone do not reveal state ordering or whether a stationary-track arc dominates trajectory.

Next evidence: short fixed-camera video of ONE existing37,103 run, from original approach straight through final stop, showing THIS corner and outgoing strip. No new compilation, sensor/power/angle/cap changes or calibration. Stop manually on departure. Purpose: distinguish actual outgoing translation from turning near the corner while one sensor retains black; cannot decide this from aggregatecounts or another stopped image. Do NOT extendcap again or add secondturn based solely on reason10. User delegates technical choices, only operates/reviews simulator; make evidence request concrete, not tuning questions. All next-run instructions below are historical.

## Current next run — 37,103 extended slow-exit observation

SECOND valid run after approximate sensor spread also reached50cap: latest complete frame [37,102,10,3,154,197,0,0,3,0,0,0,744,0,744,28,743,240,49,49,50,50,0,0,0,0,50,3,15,0,0,61,61,61,61,60,30,49,49]. One preceding fresh invalid-start frame0/49 had no motion; distinguish it. Live stdout28323bytes, no ignored messages after latest frame. Thus TWO valid runs under the new approximate sensor configuration reached50cap retaining black (previousfinal0/49with5left-onlycorrections, latestfinal0/0allboth-black). This is limited sampled repeat evidence, not exact alignment/containment/fullcorner/fullroute or proof of a root cause.

Prepared `robot_prueba_salida_extendida.nxc` revision37,103: ONLY exitcap50->100 relative to slow-exit wrapper37,102; SAME exit12/12 and0/9 or9/0, unchanged approach/position60/pivot743/confirmation and all safety stops. Shared source now permits EXIT_STEPS override, default50 unchanged. Same39-field schema with revision103 and exitStepLimit100. Purpose: test whether contact persists beyond the short observation window, not remove a safety stop or add another corner. Reason10 is the programmed cap, NOT route completion. Loss/white still stops; no secondturn/search/retry/reverse/sounds. Sensor/encoder samples cannot guarantee containment; supervise and stop manually on departure.

57 Python model/static tests PASS via `python3 -B -m unittest discover -s tests -p 'test_*.py'`. NXC compile/runtime37,103 PENDING. User close any stale shared-source editor WITHOUT saving, compile/load NEW `robot_prueba_salida_extendida.rxe`; never oldRXEaftercompilefailure. Keep SAME simulator window/sensor spread unchanged, restore original approach straight/both-black and executeONCE supervised. Do not start from last stopped corner pose. Next assistant action: inspect fresh37,103 log before further modifications. Engram writes still unavailable; local handoff authoritative. All next-run notes below are historical.

## Current investigation — sensor geometry, no new motion revision

FIRST RUN AFTER ACCEPTED SENSOR SPREAD: fresh appended37,102 frame at live stdout22025bytes: [37,102,10,3,195,194,0,49,3,0,0,0,745,0,745,46,743,240,49,49,50,45,5,0,0,0,50,3,16,0,0,63,63,63,63,60,30,49,49]. Position63/63,pivotA0/C745,stationaryboth-black stable3,exit50intervals (45both-black,5left-only,0right-only),final0/49,reason10programmed cap. No ignored messages since fresh frame. Thus widened configuration exercised one-sided correction and retained black on one sensor at the cap in THIS run. NOT proof the correction recovered both-black, exact alignment, equal-distance improvement, legal corner or fullroute. Exact angles unknown. Next: keep sensors/source/powers/caps unchanged, restore original approach straight/both-black and repeat ONCE supervised to check this newly changed configuration's repeatability, not another tuning/calibration cycle. Do not increase cap/add turns based on this single result. Await fresh log before edits.

Latest user screenshot after two manual adjustments shows row3/4 needles closer to vertical and diverging in the requested directions. Accept as APPROXIMATE spread for one controlled experiment; exact numeric angles remain unknown. Light/down indicators still appear retained. Stop requesting finer visual tuning. Next run uses EXISTING `robot_prueba_salida_lenta.rxe` revision37,102 unchanged, from original approach straight/both-black, once supervised with stop on departure. Do not run from current stopped corner pose. No new compilation required if same matching37,102 RXE remains loaded. This is a changed sensor-configuration experiment, not an identical rerun, not calibration or validated fix. Inspect fresh log before further motion/code changes; old geometry evidence cannot validate this setup.

User supplied close-up of active sensor panel after hover request: no numeric tooltip is visible. Needles3/4 are near vertical, but exact angles CANNOT be read reliably from pixels. Read-only UIKnob::mouseDown0x41dbf0/mouseDragged0x41dc80/mouseUp0x41dd30 confirms angle adjustment by held drag relative to knob center, not a simple click or tooltip numeric entry. Next proposed controlled CONFIGURATION experiment: spread row3 needle about20degrees screen-left of vertical and row4 about20degrees screen-right, preserving light/down modes and A/C side assignments. This is APPROXIMATE visual placement, NOT a verified exact+/-20 setting or a proven fix. Request stopped panel review BEFORE any motion; no run/compile/calibration yet. Current actual settings remain unchanged/unconfirmed until user evidence. Wider spread changes forward offset and must not silently reuse prior corner validation (there was none).

User objects to hours of inconclusive tuning. Stop chaining speed/cap/angle changes. Read-only PDB/EXE inspection now identifies light readings as discrete cell lookups: Robot::updatePhysics type1 branch computes ray-hit coordinates, truncates two coordinates to integers, then indexes cell data (0x411625..0x4117bc). Robot constructor initializes port3/4 angles+5/-5 degrees; these are DEFAULTS, NOT verified active GUI settings. setSensorAngle builds a radius1.15/height0.2 mount transform. Ideal symmetric5degree geometry gives only~0.20046scene-unit lateral separation;20degrees would give~0.78665 but ALSO changes forward offset. This supports investigating observability/actual sensor spread before more controller changes, NOT claiming the cause is proven or prescribing an unverified angle.

Evidence/addresses/limitations: `evidence/robosim-sensor-geometry-2026-11-06.json`. Four new offline model tests demonstrate same-cell contact at different headings, simultaneous loss without one-sided samples, and separation/forward-offset dependence. All53tests PASS via `python3 -B -m unittest discover -s tests -p 'test_*.py'`. No runtime sensor angles, scene, RXEs or motion sources changed. Computer-use tool discovery returned no tools; cannot inspect/change live GUI directly in this session. Next evidence needed is exact active sensor angles and runtime placement, not another identical movement trial. Do not use constructor defaults as active configuration, blame placement, remove loss guards or claim corner/route fixed.

## Current next run — 37,102 slower exit

37,102 EXECUTED; latest review live stdout18881bytes. Three complete frames: invalid start49/0; then [37,102,10,3,104,195,0,0,3,0,0,0,743,0,743,37,743,240,49,49,50,50,0,0,0,0,50,3,16,0,0,61,61,61,61,60,30,49,49]; LATEST [37,102,11,3,218,195,49,49,3,0,0,0,744,0,744,95,743,240,49,49,8,8,0,0,0,0,50,3,16,0,0,64,64,64,64,60,30,49,49]. First valid run reached50cap allboth-black final0/0; latest lost black after8intervals ALLboth-black, with NO one-sided correction. No ignored messages in inspected37,102 suffix. Thus lower exit power did not establish repeatability and changing one-sided steering cannot explain/fix the latest loss because that branch never executed. Do not increase cap, weaken loss stop, claim speed fix or equate cap completion with corner success. Additional37,101 observation frame also appears (reason14, stable right-only49/0, position65/65,pivotC744), confirming variable stationary contact across executions but NOT identifying its cause. Keep motion unchanged pending geometry/trajectory evidence; no new run requested just to repeat identical tests. Runtime now observed, superseding pending notes below.

User delegates technical decisions to assistant and does not want tuning questions; user only compiles/runs/reviews RoboSim. New `robot_prueba_salida_lenta.nxc` wrapper selects revision102 and scales ONLY exit powers by0.6: both-black12/12, left-only Cbraked/A9, right-only Abraked/C9. Command-space curvature is unchanged; lower sampled travel may help observation/control, but actual power-speed response and tracking benefit are unverified. Approach, position60, pivot743, stationary confirmation,50interval cap and all safety guards unchanged. No sounds/reverse/search/second turn. Main source defaults remain37,100; observation wrapper remains37,101 via CORNER_REVISION default expression.39-field schema unchanged.

49 Python model/static checks PASS (`python3 -B -m unittest discover -s tests -p 'test_codo*.py'`). NXC compilation and37,102 runtime PENDING. Smaller exit distance at the unchanged time/sample cap is expected in an ideal power model, so cap completion is NOT proof of improved equal-distance tracking or legal corner traversal. Unknown low-power response/stall remains a runtime risk, bounded by existing cap. Compile/load NEW `robot_prueba_salida_lenta.rxe`; close stale main-source buffer without saving if open. Restore original straight/both-black and run once supervised. Stop manually on departure. Assistant should inspect fresh log before additional edits; latest measured log size6297bytes, but log truncation occurred and offsets cannot be trusted. Engram writes fail; local continuity is authoritative.

## Current observation diagnostic — supersedes next-run instructions below

37,101 EXECUTED: live stdout was truncated/recreated (6297 bytes, so old byte offsets are invalid). First frame invalid start49/0; latest complete frame [37,101,14,2,147,195,0,0,3,0,0,0,744,0,744,78,743,240,49,49,0,0,0,0,0,0,50,3,16,0,0,60,60,60,60,60,30,49,49]. Reason14 is the deliberate pre-exit observation stop: position60/60, pivotA0/C744, three stationary both-black samples, exitSamples0. No ignored messages since inspected frames. User says it now looks right and supplies stopped image. This supports a qualitatively acceptable pre-exit pose in THIS run, not repeatability, exact heading or a traversed corner. No motion/source changes after this result; do not claim disabling exit repaired the turn, because geometry was unchanged. Next investigate bounded exit behavior without changing the pivot or removing loss guards.

Revision 37,100 DID execute. Live stdout at 109453 bytes contains an invalid-start frame followed by a complete frame: [37,100,11,3,177,194,49,49,3,0,0,0,744,0,744,97,743,240,49,49,8,4,0,4,0,0,50,3,15,0,0,60,60,60,60,60,30,49,49]. Positioning60/60, pivotC744/A0, stationary both-black confirmation, then eight exit intervals (four both-black, four right-only), loss49/49. User reports leaving black during the corner and supplied a stopped image. This does not establish the exact point of departure or sensor footprints.

Next executable: `robot_prueba_pose_codo.nxc`, revision37,101, a wrapper including the existing corner source with CORNER_STOP_AFTER_CONFIRMATION=1. SAME approach/position60/pivot743/contact check; NO exit. Successful contact check becomes reason14, phase2, exitSamples0, deliberate silent observation stop, NOT corner success. Earlier failure reasons remain unchanged. Same39-field schema. Default `robot_prueba_codo.nxc` remains behaviorally37,100 (flag0); telemetry revision expression selects100/101. No calibration, geometry/power changes, sounds, retry or search. Purpose: isolate end-of-pivot pose before exit steering; do not assume this fixes alignment.

45 Python model/static tests pass: `python3 -B -m unittest discover -s tests -p 'test_codo*.py'`. NXC compilation/runtime of wrapper and include handling remain PENDING. User should compile/load NEW `robot_prueba_pose_codo.rxe`, never an old RXE after errors. Restore original approach straight, both sensors black, run once supervised and stop on departure. Observe whether stopped robot points along outgoing black or remains offset/diagonal. No generic extra camera request. Corner containment and route remain unvalidated. Engram project writes still fail; local handoff is authoritative.

## Start here

Continue incremental NXC/RoboSim competition development. Do not restart calibration or ask the user to count beeps. Read this file, `robot_prueba_linea.nxc`, and `PLAN_OPTIMIZACION.md` before making changes. The competition solution is NOT complete.

**Next practical milestone:** implement and validate one bounded, sensor-terminated 90-degree corner maneuver in a separate diagnostic, using the existing silent follower as the baseline. Keep route legality unresolved until supported by a validated graph and intersection interpretation. Do not add arbitrary route decisions.

## Current executable handoff (supersedes historical next-test notes below)

CHAT TRANSFER: user explicitly requests continuing in a NEW chat because current context is too large. Last prepared revision is37,100 in `robot_prueba_codo.nxc`; user has NOT reported execution of this revision. Do not edit again or repeat calibration before checking whether it was compiled/run and reading the fresh live log. Read current summary here, source and PLAN first; historical sections below contain superseded instructions. Keep diagnostics silent. Next expected evidence is a complete39-value37,100 frame, not earlier37,99 results. Only exit one-sided corrections changed in the latest revision; all entry/pivot settings remain unchanged. Do not claim corner/fullroute validated.

- CURRENT NEXT RUN: `robot_prueba_codo.nxc`, revision37,100,39-field layout UNCHANGED exceptversion. User confirms robot was put back on straight; exactposeequalitynotverified. Do not keepaskingwhetherstartedfromstoppedpose orblameuser. No extra camera evidence requested.
- Local EXIT steering experiment only: latest37,99 loss followed13bothblack samples then1right-only andbothgray. Stop geometry and baselines remainunchanged: positioning60at15/cap30; forwardpivotA-braked/C743at15/cap240; confirmation3same-nonzerostate; exitcap50; allwhite/neitherblack/sign/sentinelguardsretained. Approach powersunchanged20/20,10/25,25/10.
- NEW exit corrections: BOTHblack stillC20/A20; LEFT-onlyblack brakesC andadvancesA15; RIGHT-onlyblack brakesA andadvancesC15. Comparedwithold10/25or25/10 this preservesdirection/differentialcommand15 but reducesmeanforwardcommand17.5->7.5and tightensidealcurvature. Hypothesis: givecorrectionmoreheadingchangeperforwarddistance beforelosingcontact; NOT provenrootcause/line recovery. Thisis ordinarysensorsteeringinsideexistingboundedexit, notanotherroutecorner orsearch. Ifbothgrayorwhite,stillSTOP.
- Telemetry prefix37,100; full39positionssameas37,99below. MotorsfieldsstillPOSITIONandTURN snapshots, NOT exitdistancemeasurement; repeatedOff/OnFwdexitcommandsnotusedforodometry. Compareexitstatecounts/finalreadings andactualmotion,notjustcapreached. Initialbothblackrequired,noautomaticresume/retry.
- 43 Python hostmodel/statictestsPASS: `python3 -B -m unittest discover -s tests -p 'test_codo_control_model.py' -v`. Addedstopafteronesidedlossandcommand-spacecurvaturechecks; updatedcorrectionmodel/sourcebrakingchecks. NXCcompile/runtimeof37,100PENDING. No exactyaw/containment/legalcorner/fullroutevalidation.
- Preteststdout102884bytes,append-onlycaveat. UserclosecodoeditorWITHOUTsavingstalecontents,reopencompile/loadmatchingNEW RXE,restoreoriginalapproachstraightbothblack,executeONCEsupervised;stopondeparture. Expectedrecta->smallentryadvance->arc->contactcheck->boundedexitwithtightersteering->stop. Engramstillunknown_project;handoffhere/PLAN.

## Prior handoff and experiment history (37,99 and earlier; not current run instructions)

LATEST37,99 RUNTIME OBSERVED:3completeframes. First reason12phase4,approach10,position30samples with0/0encoderprogress (stall/cap),no pivot; exactcauseunproven. Second [37,99,10,3,122,188,0,0,3,0,0,0,745,0,745,62,743,240,49,49,50,31,19,0,0,0,50,3,16,0,0,63,63,63,63,60,30,49,49]: positioning63/63,turnC745,exit50limitwithfinal0/0(31both+19left-onlycorrections). LATEST [37,99,11,3,192,191,49,49,3,0,0,0,745,0,745,84,743,240,49,49,14,13,0,1,0,0,50,3,17,0,0,61,61,61,61,60,30,49,49]: positioning61/61,turnC745,exit14(13both+1right-only)then49/49reason11. Thusstageexecutedandoneboundedexitcompleted,butnotrepeatable; lateststopissafetyline-lossNOTpositionstallorcap. User says stays there and supplies stoppedimagewithconfigpanel. No automaticresume expected. Need establish matchedinitialplacement/heading/config acrossruns before moreparameterchanges; logdoesnotidentifyexactglobalpose. Do not blameuserorclaiminitialdifferencesasprovenrootcause. No newcodechangebasedonthisresult.

- CURRENT NEXT RUN: `robot_prueba_codo.nxc`, revision37,99. User explicitly approved a small encoder-bounded forward positioning advance BEFORE the pivot. NXC compilation/runtime of THIS revision pending.
- Sequence: initialbothblack -> original bounded follower approach -> both lose black -> phase4positioning -> phase1forwardpivot -> phase2stationarycontact -> phase3boundedexit. Initialgray/white still rejects motion. No second turn, search/retry, reverse or sounds. Full route unresolved.
- Positioning is an EXPERIMENTAL geometry adjustment: BOTH motors forward15, commands once, separate post-command encoder baselines. Stop at FIRST motor reaching60relativecounts; ONLY if BOTH>=60 permit pivot. Wrong direction7, sentinel8, white1,30sample20ms cap12, or unequalthreshold crossing13 abort WITHOUT pivot. Gray during this explicitly authorized short positioning stage is expected/allowed, NOT a general line-loss recovery or permission to advance on gray during exit. Nominal cap0.6s, not measuredtime.60counts is a provisional offset (~0.209sceneunits from inspected scale, NOT physical centimetres or a measured safe offset); could reduce edgeclearance. Supervise and stop on departure.
- Afterpositioning, stop motors and establish independent TURN baselines before A-braked/Cforward15 pivot to743relativeCcounts, cap240samples. Absolute TURN readings need not start0 after positioning; interpret DELTAS. DeltaA must stay0. Three stationary samples of SAME nonzero contact state gate existing50step follower exit; white/neitherblack stops as before. No contact after pivot -> no exit. Positioning does NOT prove alignment or containment.
- New39-value frame:37,99,reason,phase,approachIndex,turnSamples,left,right,stable,startA,startC,currentA,currentC,deltaA,deltaC,turnBothSamples,motorTarget,turnSampleLimit,entryLeft,entryRight,exitSamples,exitBothSamples,exitLeftSamples,exitRightSamples,confirmedLeft,confirmedRight,exitStepLimit,confirmationState,positionSamples,positionStartA,positionStartC,positionCurrentA,positionCurrentC,positionDeltaA,positionDeltaC,positionTarget,positionSampleLimit,positionLeft,positionRight. First28 positions unchanged except version; append11positionfields. PositionLeft/Right are last actual positioning sample,30000ifnevermeasured. Turn and position values are separate. Phaseorder0->4->1->2->3; reason12positioncap,13unequalpositionprogress; earlierreasons unchanged (7invalidmotioninterpreted by phase,9reserved,10exitcap notroutecompletion,11exitloss).
- 41 Python hostmodel/static tests PASS: `python3 -B -m unittest discover -s tests -p 'test_codo_control_model.py' -v`. Added10positioning tests: gray boundedadvance, firstmotorstop, imbalance/stall/sign/white/sentinel aborts, independentbaselines, blacknotshorteningoffset, overshootstop. Structuralchecks verify approach cannot bypass phase4 and position motors stop before pivot. NOT NXC compilation/simulation.
- Preteststdout93453bytes (append-only/no-truncation caveat). During work, existing37,98 logs grew to7frames: recentvalidattempt lostlineexit34, last2invalidstart50/50,no motion. These are OLDrevisionresults, not37,99 validation. AlwaysrestoreoriginalstraightBOTHsensorblackbeforeeachrun; do NOT just rerun from stoppedpose.
- User close editor WITHOUT saving stalebuffer,reopen/compile/loadNEWmatchingRXE,restoreoriginalapproachstraightbothblack,runONCE supervised. Expectedapproach -> SMALL extra forward shift -> arc -> contactcheck -> boundedexitifconfirmed -> stop. No genericnewcamera requests. Continuity persisted here/PLAN because Engram stillfailsunknown_project.

## Prior handoff and experiment history (37,98 and earlier; not current run instructions)

LATEST37,98 RUN: [37,98,11,3,168,181,49,49,3,0,0,0,743,0,743,52,743,240,49,49,26,26,0,0,0,0,50,3]. User compilation/runtime of exit50revision observed. A0/C743 pivot,stationary3bothblack/state3 confirmed, exit26intervals ALLbothblack then49/49 reason11, BEFORE50cap. Thus extendingcap revealed loss, not sustainedexit; do NOTextendagain orclaimsolution. No freshignoredopcodes. Priorvideo/staticreviewdoesnotproveexactphysicalfootprints or nextcorner. Next hypothesis to discuss: SMALLencoder-boundedforward reposition BEFOREpivot to changeaxlelocation, NOTangle orblindexitaftergray; mayreducetrackedgeclearance andmustbeexplicitlyscoped as supervised diagnostic with unresolvedcontainment. No suchstageimplemented/authorizedyet; do not moveonuser'sbehalf. Existingwhite/lossguardsandfullrouteuncertaintyretained.

CURRENT37,98 NEXT RUN: source `robot_prueba_codo.nxc` now changes ONLY exit cap25->50intervals, same20ms/powers, unchangedforwardpivotA0/C743, allwhite/loss/confirmationguards retained. No automaticsecondturn. Reason10stillmeans observationcap, NOT routecompletion; reason11line-lossmuststop. New37,98 has same28-field schema, final exitStepLimit50.31Pythonhostmodel/statictestsPASS, NXCcompile/runtimepending. Preteststdout77123bytes (append-only caveat). User close staleeditor WITHOUT saving,reopencompile/loadnewRXE,restore sameoriginalapproachstraightbothblack,runonce supervised. Expectedonepivot thena longerbutboundedexit, stopifwhite/neitherblack. No fullroute/containment/legalityclaims.

VIDEO REVIEW RESULT: user supplied `/Users/leonel/Desktop/Grabación de pantalla 2026-11-06 a las 12.27.01 a. m..mov`,6.601667s,2184x1284,nominal60fps. Inspected2fpscontactsheet and fullframes0.2/4.5/5.3/6.2/6.55s usingFFmpeg, no sourcechanges. Showsrightforwardarc,shortleft-screen displacement,stationaryendpoint; no secondturn. CrucialNEWlogdata: preceding37,97 frame [37,97,11,3,78,193,49,49,3,0,0,0,743,0,743,65,743,240,49,49,23,23,0,0,0,0,25,3] lostlineafter23; LATESTframe [37,97,10,3,79,197,0,0,3,0,0,0,743,0,743,51,743,240,49,49,25,25,0,0,0,0,25,3] reached25capwithfinal0/0. Therefore NOT everyrecentstopisfault: latestisprogrammedcap, butprecedinglossmeansrepeatabilityNOTestablished. Do not inferactualsensorfootprintsfromdrawnhousings or conclusivelypairMOVtoaparticularrunwithouttimestamps. Evidence/hashes/limitationssaved `evidence/robosim-video-review-2026-11-06.json`; extractedframesaretemporary. Do not requestmoregenericperspectives orchangeangleagainbasedonlyonastoppedimage.

LATEST37,97 execution: [37,97,11,3,275,199,49,49,3,0,0,0,747,0,747,94,743,240,49,49,5,4,0,1,0,0,25,3]. PivotA0/C747 reaches reference,3stationarybothblack confirms; exit only5commandintervals (4bothblack,1right-only) then49/49 reason11, before25cap. Earlier37,97 frameinvalidstart49/49 hasno motion; separate. No fresh ignoredopcodes in inspected appendedinterval. The743physicsreference correction DID NOT resolve outgoing tracking in this run. Do not claim rootcause fixed, exactyaw validated or compare performance quantitatively against prior14intervalrun without matchedinitialpose. Need observe actual trajectory to distinguish lateral departure, anotheredge/corner, or translation/entry mismatch; no blindthreshold/anglechanges. Next request a SHORT video from before the turn until stop with camera FIXED, rather than more generic static perspectives; same source, no recompile needed. Maintain silent/supervisedstopondeparture. No new codechange based on this result.

CURRENT ANGULAR REFERENCE CORRECTION37,97: user clarifies robot turned, attempted a small exit, then stopped. Treat exit as unvalidated/uncertain, not a reason to add automatic second turns. Read-only review of bundled PDB/EXE found Robot::updatePhysics at0x411320, width1.649999976 at0x427300, scaling0.40000000596 at0x427210 times0.008726646192 at0x427308. Heading accumulates atan of per-step distance difference/width (_CIatan import verified). Thus720single-trackcounts predicts~87.27degrees in small steps, not90; theoreticalquarterturn742.49998 -> target743. This explains a reference inaccuracy, NOT proven sole cause of exit loss. Static evidence incl addresses/hash/limitations saved in `evidence/robosim-physics-2026-11-06.json`; no liveprocess access performed. Updatedsource frame37,97 same28fields, activeCtarget743, stoppedA0, allpowers/guards/caps unchanged.29Python hostmodel/static testsPASS incl evidence-derivedtarget and per-stepatanexample; NXCcompile/runtimepending. Preteststdout67793bytes (append-only caveat). User must close staleeditor WITHOUT saving,reopencompile/loadmatchingnewRXE,restoreoriginalapproachstraightbothblack,runonce supervised. Expectedapproach->forwardpivot->stationarycontactcheck->boundedexitonlyifconfirmed->stop. No secondturn/retry/search or blindgrayexit; no claim exactruntimeyaw, containment, corner success, branch identity or fullroute.

LATEST37,96 RUN (2026-11-06): user reports start on straight, right turn and forward advance, then no second turn. Latest frame [37,96,11,3,245,189,49,49,3,0,0,0,721,0,721,75,720,240,49,49,14,14,0,0,0,0,25,3]. Forward pivot target reached (deltaA0/deltaC721), stationarybothblack3/state3 confirmed, exit actually entered and completed14command intervals ALLbothblack, then bothgray49/49 -> reason11 BEFORE25cap. No second turn exists by design. This demonstrates one approach/pivot/contact/shortadvance execution, NOT a repeatable legalcorner or route. Must determine whether final loss occurred at NEXTcodo or during outgoingstraight before adding another turn; do not automatically turn on all losses. Earlier37,96 frame is invalidstart49/49, no motion; distinguish fromlatest. No fresh ignored-opcode text in inspected interval. No code changes yet for this result.

LATEST37,95 EXECUTION: [37,95,6,2,257,91,49,49,0,0,0,-364,364,-364,364,66,360,120,49,49,0,0,0,0,0,0,25,0]. Both encoders reached reference but stationary sensors BOTH gray49/49, stable0/state0, exitSamples0. Thus relaxing to stable one-sided black did NOT enable exit in this run; do not relax to both-gray or drive blind. User asks what program is supposed to do and why it keeps stopping: explain explicitly expected approach -> turn -> stationary check -> short exit ONLY if contact -> final programmed stop. Actual run stopped at failed check; corner placement/exit contact not repeatable, despite provisional rotation calibration. Do not imply user did anything wrong or that this is a working route; no more identical rerun requested. Need revisit maneuver geometry/termination with evidence, not merely remove gate.

- CURRENT NEXT RUN: `robot_prueba_codo.nxc`, revision37,98, unchangedC743, exitlimit50 (see current summary above). Compilation/runtime of THIS revision pending.37,97 latestended25capblackbutprecedingrunlostline23; no reliablecornerexit yet. Collision and exactgeometry NOT proven.
- Trajectory: brake A (right) and advance C (left) at15, one command each. Forward pivot translates the chassis on an arc instead of center rotation. The OLD720target came from ideal C-A equivalence to the approximate center calibration; inspected physics now corrects it to743 as detailed above. This remains a model-based reference, not a measured90degree pivot. Geometry/offset/containment still require runtime validation. Old timed forward-pivot failures never established a full quarter-turn at that geometry; do not equate their60/90iterations with a measured angle.
- Turn cap240samples20ms (nominal4.8s, not success criterion). Relative deltaA must stay0; any reported A motion or negative C stops reason7, sentinel stops8. C reaching743 stops rotation and enters stationary confirmation. No compensating motion. Early black cannot finish rotation. Initial start still requires both-black; three stationary samples of SAME nonzero state (1left-only,2right-only,3both) gate50-step exit. White/neither-black still stop. No reverse commands, second turn, retry/search, sounds, extra gray forward advance, or route decisions. Supervise and stop on departure.
- New28-value frame:37,98,reason,phase,approachIndex,turnSamples,left,right,stable,startA,startC,currentA,currentC,deltaA,deltaC,turnBothSamples,motorTarget,turnSampleLimit,entryLeft,entryRight,exitSamples,exitBothSamples,exitLeftSamples,exitRightSamples,confirmedLeft,confirmedRight,exitStepLimit,confirmationState. Same positions as37,97, expected TURN deltas A0/C>=743,target743,cap240,exitStepLimit50. Motor fields remain captured TURN values before Off/exit. confirmationState is latest nonzero stationary state, not success alone; stable must be3. confirmedLeft/Right meaningful only if phase3 entered. Exit state counts sum to exitSamples. Phase0approach,1pivot,2confirmation,3exit. Reasons1white,2invalid start,3approach cap,4pivot cap,5stable-contact gate internally permits exit,6missing/unstable contact,7invalid pivot progress (A movement or C reverse),8sentinel,9reserved historical,10exit cap NOT route completion,11exit loss.
- 31 Python host-model/static tests PASS: `python3 -B -m unittest discover -s tests -p 'test_codo_control_model.py' -v`. Added extendedexit50cap and regressionsforlossatold25capandprior23intervalrun. Staticphysicsreference tests retained. NOT NXC compilation/simulation.
- Pretest stdout77123bytes, useful only if appended/no truncation. User close editor WITHOUT saving stale buffer, reopen source, compile/load matching NEWRXE, restore SAME original corner-approach straight with BOTH sensors black, run once supervised. Do NOT resume from stopped codo pose. Expected: approach -> forward arc -> stopped contact check -> boundedexit ONLY if confirmed -> stop. If gray remains, exit stays blocked. Route/exact angle/containment remain unvalidated.
- Engram writes still fail unknown_project; continuity persisted here and in PLAN_OPTIMIZACION.md.

## Previous executable handoff (37,94; historical, not current instructions)

Latest exit-revision run37,94: [37,94,6,2,362,95,0,49,0,0,0,-362,362,-362,362,67,360,120,49,49,0,0,0,0,0,0,25]. Reason6: reached paired encoder reference but stationary check saw left0/right49 immediately, stable0, so exit was correctly BLOCKED (exitSamples0). This does not establish a successful exit or repeatable corner geometry. Prior37,93 both-black pass is not repeated here. One earlier37,94 frame in new log interval is reason1 phase0 approach217 left100/right0: white encountered during approach, no turn; do not confuse with latest run. No fresh ignored-opcode text. Next ask whether robot is aligned with outgoing branch or diagonal, before weakening both-black gate or adding correction/search. One black sensor is a normal follower state but current gate deliberately requires both; do not silently reinterpret as success.

Latest `robot_prueba_codo.nxc` execution: user reports approach along straight, turn, stop, with side-on/screen-left final image. Complete37,93 frame [37,93,5,2,333,91,0,0,3,0,0,-360,360,-360,360,75,360,120,49,49]. Reason5: encoder reference and three stationary both-black samples confirmed, NOT safety timeout. Entry49/49 after approach index333, turn91samples, paired deltas-360/+360,75both-black samples during turn (correctly did not terminate early). No ignored opcode text in newly appended interval. Diagnostic intentionally stops without forward exit. This is ONE combined approach/turn/confirmation run, with qualitative near-perpendicular final heading, NOT proven containment, legal traversal, exact90degrees, repeatability or route. Next scoped behavior could be a SHORT bounded sensor-followed exit on reason5 only, with immediate stop on uncertainty and no second turn; do not auto-claim completion of route or competition program.

- CURRENT SOURCE: updated `robot_prueba_codo.nxc`, frame37,94, with a short gated exit. User compilation/runtime now observed, but latest run blocked exit on missing both-black confirmation; the37,93 pass above is the previous stop-only revision.
- Two standalone calibration runs at360motor target ended at A/C=-362/+362 and-360/+360; paired user images are qualitatively near perpendicular. This is a provisional reference, not exact yaw measurement or a legal corner.
- New test validates initial both-black, follows the original20/20,10/25,25/10 approach up to400iterations, and triggers one robot-right center rotation on simultaneous loss. Cforward15/Areverse15 commands issued ONCE; post-command baselines and relative deltas; maximum120turn samples of20ms.
- Early0/0 is counted but never terminates rotation. Stop at FIRST motor crossing+/-360. Only if BOTH satisfy their directional360thresholds proceed to three stationary both-black confirmations. Slight unequal target crossing is conservatively rejected, not compensated with further motion.
- ONLY after reason5 (full stationary confirmation), phase3 follows black for up to25intervals20ms using SAME approach powers20/20,10/25,25/10. Re-sample sensors after the final interval while stopped. Stop on white or neither-black immediately at next sample, never trigger another turn/retry/search.25intervals is a nominal0.5s cap, not a measured distance/elapsed time or successful route. Sensor sampling cannot guarantee containment; supervise and stop on departure.
- No extra reverse in exit, sounds, AND/OR, displays, route integration. Earlier failures cannot enter exit. All approach/turn guards retained. Sensor/encoder confirmation does not prove exit identity or legality.
- New27-value frame:37,94,reason,phase,approachIndex,turnSamples,left,right,stable,startA,startC,currentA,currentC,deltaA,deltaC,turnBothSamples,motorTarget,turnSampleLimit,entryLeft,entryRight,exitSamples,exitBothSamples,exitLeftSamples,exitRightSamples,confirmedLeft,confirmedRight,exitStepLimit. First20positions unchanged except version. Signed motor fields remain TURN readings, captured before Off/exit commands. Confirmed sensor fields meaningful only if phase3 entered. ExitSamples counts commanded/completed intervals, and three exit state counts should sum to it. Finalleft/right re-read after exit stop. Phase0approach,1turn,2confirmation,3exit. Reasons1white,2invalid start,3approach limit,4turn limit,5confirmation internally enables exit,6reference/missing black,7wrong direction,8sentinel,9unequal threshold crossing,10exit cap (NOT route completion),11neither-black during/after exit.
- `tests/test_codo_control_model.py`:21 host-side model/static checks PASS via `python3 -B -m unittest discover -s tests -p 'test_codo_control_model.py' -v`. These do NOT compile/run NXC; added exit gating on all failures,25command cap, white/loss stops, no second turn, matching corrections, final-interval resample and boundary checks.
- Pre-run live stdout byte size53988, useful only if appended/no truncation. Preserve old diagnostics and user RXEs. User must close codo editor WITHOUT saving stale contents, reopen source from disk, compile/load matching NEW RXE, start from SAME straight leading into specified robot-right corner, both sensors on black; not from last stopped/rotated position or distant calibration. No new screenshots needed initially.
- Engram writes continue failing unknown_project; continuity saved here and in PLAN_OPTIMIZACION.md.

## Goal and rules

- NXT differential/tracked robot in BricxCC go4IT and RoboSim; NXC compiled by bundled NBC.
- macOS on MacBook Air M4, Porting Kit 7.0.2/Wine. The user operates the GUI; the assistant has inspected local files/logs, not directly controlled or observed live motion.
- Start stationary before the white marker, departing counterclockwise. Complete two consecutive laps without leaving the track or repeating segments within a lap.
- The user subsequently clarified that ALL branches and loops must be covered. Do not offer a perimeter-only shortcut.
- Intended marker events: initial crossing starts timing, second completes lap 1, third completes lap 2 and stops. Prevent repeated events while remaining over white. Sound must not block driving.
- Priority: rule compliance, complete route, robust navigation, marker reliability, two laps, then speed.
- Final requested deliverables: `robot_competicion.nxc`, `robot_calibracion.nxc`, `robot_prueba_motores.nxc`, `README.md`, `PLAN_OPTIMIZACION.md`. The first file does not exist yet; do not create a misleading finished entry.

## Interaction constraints

- Speak Spanish, concise and concrete; explain screen-left versus robot-left explicitly. One question at a time.
- User needs small GUI steps, not long option lists or unexplained parameter tuning.
- Repeated beeping caused stress; user muted RoboSim. Keep further diagnostics SILENT. Do not ask the user to unmute or count pulses. Competition sounds can be enabled/tested separately later.
- Source code and current project documentation are in English.
- Do not ask for more general perspective screenshots: many were already provided. If an indispensable ambiguity remains, identify the exact location and explain what evidence would resolve it.
- BricxCC can retain a stale editor buffer: after assistant edits, ask user to close the tab WITHOUT saving the old contents, reopen from disk, compile, then load the new RXE. Never run an older RXE after compilation failed.
- User reports configuration can change on closing/reopening RoboSim. Keeping the same simulator window open avoided that in later tests. Exact persistence behavior is not established.

## Paths and available evidence

- Workspace: `/Users/leonel/Developer/sistemas-int-robot` (not a Git repository at initial inspection).
- Original package: `/Users/leonel/Downloads/Simulador Lego.rar`.
- Extracted installed package exists at `/Users/leonel/Downloads/BricxCC Simulator`.
- Runtime log successfully read at `/Users/leonel/Downloads/BricxCC Simulator/legosimulator/stdout.txt`.
- Compiler in package: `nbc.exe`; simulator: `legosimulator/legosimulator.exe`, with `legosimulator.pdb`.
- `bsdtar` can list/extract the RAR. An inspection copy was extracted under the session temp directory; do not rely on that temporary path surviving.
- No `nbc`, `wine` or `wine64` was found in PATH during initial inspection. Do not claim assistant-side compilation. User-side compilation and simulation have been performed on diagnostics.
- Track and robot screenshots were attached in chat, not saved as project images. A new chat may need the user to attach the full track image and upper-junction close-up again; do not pretend this file contains their pixels.
- A copy of the current runtime log is stored as `evidence/robosim-session-2026-11-05.stdout.txt` for historical analysis. It is not the live log and contains old failures as well as later successful runs.

## Simulator compatibility: proven gotchas

1. `TextOut`/`NumOut` diagnostics did not appear. Live log explicitly says `Ignoring syscall d (NXTDrawText)`, `ignored numtostring`, `ignored strcat`, and ignored drawing calls. The display calibration is obsolete for this simulator, even if it compiles.
2. `&&`/`||` compiled but produced `ignored and` / `ignored or` at runtime. The current follower uses only simple comparisons and nested branches. Do not introduce these operators without a dedicated capability test. PID/arithmetic/encoder APIs are not validated merely because they exist in NXC.
3. Bundled NBC uses `ScaledValue` (field 4), NOT newer `ScaledValueField`. The latter caused four real compilation errors. Inspection of strings in bundled `nbc.exe` confirmed `#define ScaledValue 4`.
4. Numeric diagnostic bridge works experimentally: `SetInput(IN_1, ScaledValue, number)` produces `Set input configuration for port 0 property 4 (IO_IN_SCALED_VAL) to 0x...` in stdout. It writes an UNUSED port, not the measured ports. Reserve port 1 for this diagnostic. This is a simulator-specific side effect, not portable NXT file logging.
5. Sensor ports in the log are zero-based: physical 3/4 appear as ports 2/3. Bridge writes to physical port 1 appear as port 0. Read numbers after `to 0x` as HEXADECIMAL.
6. Existing probe frame: decimal 37, 82 (hex 25,52), then sensor 3 and sensor 4. Follower frame: 37,82, stop reason, step count, sensor 3, sensor 4. Reasons: 1=white, 2=neither black, 3=step limit.
7. Log sometimes contains NUL padding and historical runs. Strip NULs before parsing and inspect the last complete frame, distinguishing fresh execution from old lines. Do not infer failures in a new run from old ignored-opcode lines.
8. `ignored finclump` appears at task end. User experienced repeated tones; exact cause was not proven. Current follower avoids task-end dependence by entering `while(true) { Off(OUT_AC); Wait(100); }` and has no sound calls. Earlier sound/motor/log probes do not have that safeguard.
9. A three-tone compatibility test was audible according to the user. This establishes basic sound output, not calibrated durations, nonblocking timing, or marker behavior.

## Confirmed configuration and initial measurements

| Component | Working mapping / observation |
|---|---|
| Sensor 3 | Robot-left, LIGHT icon (sun), arrow DOWN |
| Sensor 4 | Robot-right, LIGHT icon (sun), arrow DOWN |
| Motor A | Assigned to left strip in GUI output panel; observed to turn robot-left alone; follower treats it as RIGHT drive |
| Motor C | Assigned to right strip in GUI output panel; observed to turn robot-right alone; follower treats it as LEFT drive |
| Motor B | No side assignment in the working configuration |
| A+C positive `OnFwd` | User observed forward motion toward the sensors |

GUI strips denote side assignments, not merely enabled/disabled motors. C originally had no side assignment while B had one; assigning the right strip beside C restored C motion. Do not confuse GUI strip positions, screen directions and physical drive mapping.

Port 4 initially had SOUND selected despite the downward arrow. It read a misleading constant 100 on black/gray. Selecting the SUN icon fixed its black reading to 0. Those earlier 100 readings are invalid light calibration data.

| Surface | Port 3 | Port 4 |
|---|---:|---:|
| Black | 0 | 0 |
| Gray | 50 (49 also observed) | 50 (49 also observed) |
| White | 100 | 100 |
| Opposite edge position 1 | 0 | 49 |
| Opposite edge position 2 | 49 | 0 |

Opposite-edge screenshots support 3=robot-left, 4=robot-right. These are initial observations, not statistical noise bounds or evidence of continuous lateral resolution. Thresholds 25 and 75 are provisional midpoints. No PD/PID benefit has been demonstrated.

## Working code and test results

- `robot_prueba_linea.nxc`: latest baseline; low-speed nested-branch controller, A right/C left. Both black: 20/20; left black only: C=10, A=25; right black only: C=25, A=10. Stops on either white, neither black, or 400 iterations with `Wait(20)` (nominal 8 seconds, NOT measured wall time). Initial wait 1500 ms. Logs final state, then stays silently stopped.
- User compiled and ran the revised follower. A straight run ended with reason 2, 203 iterations, readings 49/49; user and image indicate arrival at a corner/end of the straight, not a completed turn.
- Another run ended reason 2, 244 iterations, 49/49. User reported realignment after small initial deviations in BOTH directions. This is qualitative user observation, not measured success rate. No correction counters or continuous trace were collected.
- Straight movement and stopping are demonstrated; legal corner traversal and intersection navigation are NOT. Do not call this a completed competition follower.
- `robot_prueba_motores.nxc`: user changed TEST_PORT during A, C, AC tests; inspect current file before assuming the selected port. Short timed pulses are diagnostic only, not route navigation.
- `robot_prueba_registro.nxc`: successful stationary one-shot log bridge. Ends with a tone; avoid further repetitive use without making it silent and holding safely at end.
- `robot_prueba_sonido.nxc`: audible three-tone compatibility diagnostic, no movement.
- `robot_calibracion_sonora.nxc`: numeric beep encoding; REJECTED as too cumbersome. Do not resume that workflow.
- `robot_calibracion.nxc`: original display-based min/average/max sampling; OBSERVATION METHOD UNSUPPORTED here. Must eventually be replaced/adapted, not presented as the working calibration deliverable.
- `prueba_seguidor_linea_nxt.nxc` and original RXE: user-provided prototype, preserved. Assumed A left/C right, fixed threshold 40, startup beep, boolean operators; not the working baseline.
- RXE files and a motor `.bak` exist; preserve user work. Source/RXE synchronization must be verified, not assumed by filename existence.

## Route issue — explicitly unresolved

Reference orientation for the following: full screenshot with white marker near bottom-left, small loop top-center/right, large loop on the right.

- B: central junction reached by moving right from the marker along black and then up the vertical strip.
- C: junction farther right along the middle horizontal strip, next to the large right loop.
- A: upper central vertical strip next to the small upper loop. Its right entrance is higher in the screenshot than its inner-left entrance. They are visibly staggered.

The provisional split model in `PLAN_OPTIMIZACION.md` uses A1 (right entrance), A2 (lower left entrance), B, C; edges are short A1-A2 connector, small-loop A1-A2 path, outer marker A1-B path, inner-left A2-B path, two B-C paths, C self-loop. Degrees 3,3,4,4 prohibit a closed Euler traversal IF that connector is a distinct mandatory edge. A Python degree count verified only this conditional graph result.

IMPORTANT CORRECTION: the assistant first treated A1/A2 as definitely separate junctions, then acknowledged that the extended-intersection boundary is unverified. Do NOT promote the provisional graph to ground truth or tell the user the competition is impossible. More generic perspective screenshots will not establish the professor's definition of a segment inside the intersection.

Previously floated route: marker -> B -> C -> right loop -> C -> other B-C path -> B -> inner-left A path -> upper loop -> outer path -> marker. This has NOT been validated: the upper connector/intersection treatment, full coverage, and exact maneuvers remain unresolved. Do not encode it as a proven sequence or claim counterclockwise legality has been checked.

## Next-session execution plan

### Right-corner diagnostic (instrumented revision pending compilation/run)

Repeat360 calibration completed with paired user before/after images (frontal initial, side-on screen-left final). Second37,92 frame [37,92,1,93,0,0,-360,360,-360,360,360,120]; previous run±362 at95samples. Thus TWO runs stop at360/362motor counts and appear near perpendicular qualitatively. Small sample-count difference is not yaw or measured-time evidence. Accept360 as provisional encoder reference for next separate sensor/encoder corner diagnostic; no exact90degree measurement, track containment, navigation legality or full route validation. Next implement bounded approach+turn with encoder progress gating to avoid premature0/0 completion, and stop on missing exit confirmation; do not automatically drive onward or treat straight calibration as corner success. No new source change made in this evaluation.

Latest360-target calibration executed:37,92 frame decoded [37,92,1,95,0,0,-362,362,-362,362,360,120]. Encoder-target stop at95samples, overshoot2counts, no ignored opcodes in fresh appended interval from49682. User image shows approximately side-on/screen-left heading, visually near perpendicular to initial frontal/vertical alignment. Treat360motor target as a PROVISIONAL quarter-turn reference in current configuration, NOT exact measured yaw or validated corner. Next repeat SAME360-target calibration once, restoring original initial alignment, to check qualitative repeatability before integrating sensors/entry. No code change needed; no cumulative rotation/reload of old file. Track containment/legal corner and full route remain unvalidated.

CURRENT NEXT CALIBRATION revision: user authorizes continuation after180-count underturn. `robot_calibracion_giro.nxc` now targets+/-360 MOTOR counts, unchangedpower15 and20ms sampling, watchdog120samples (nominal2.4s, not success criterion). Rationale:180target took48samples; double target needs additional watchdog allowance, NOT a claimed yaw conversion. Frame37,92 same12fields as37,91; final target360/sampleLimit120 identifies loaded version. Only constants/frame comments changed, no new motion/API. Static checks and9 Python model cases pass, NXC compile/run pending. Pretest stdout49682bytes (append-only caveat). User reopen source from disk without saving stale buffer, compile/load matching RXE, RESTORE original straight alignment before one supervised run; no cumulative rerun from rotated pose. Report whether heading remains short of/perpendicular to/beyond starting reference. Stop immediately on departure.360motor counts does NOT mean360bodydegrees or a calibrated90degree maneuver; route and corner containment still unvalidated. Older target/status notes below are historical.

Latest180-motor-count calibration run:37,91 decoded [37,91,1,48,0,0,-182,182,-182,182,180,60]. Ctarget stop at48samples, 2-count overshoot; no ignored-opcode text after byte48785. User final image shows diagonal heading, still not perpendicular to original frontal/vertical reference. Qualitative underturn only; do not assign precise body degrees from perspective or assume a linear yaw ratio. Encoder threshold works in these90/180 tests; no calibrated90degree chassis target yet. No further source change made after this result. Need a justified next yaw calibration step, not a claim of completed corner. Keep route and sensor/encoder integration unvalidated.

Latest user supplied paired calibration images showing initially frontal robot then small right rotation, not perpendicular to initial straight. Latest old37,90 frame [37,90,1,24,0,0,-93,93,-93,93,90,60], corroborating previous94-count run. No exact chassis angle measured; do not infer a precise ratio from perspective images. CURRENT source `robot_calibracion_giro.nxc` now uses +/-180 MOTOR-count exploratory targets, SAME power15 and60sample20ms cap (no time-bound extension), new frame37,91 with same12-field layout. It is NOT a90degree robot target. Compile/run of this revision pending. User must reopen source WITHOUT saving stale buffer, compile/load matching RXE, restore initial alignment on same clear straight rather than repeat from last rotated pose. Observe qualitative heading change; supervise and stop on departure. Pretest stdout48785bytes, useful only if appended. Do not integrate corner follower until yaw reference and containment validated.

Latest exploratory encoder calibration executed:37,90 decoded frame [37,90,1,24,0,0,-94,94,-94,94,90,60]. Reason1 C motor target reached after24samples; A=-94/C=+94 (4-count threshold overshoot), baselines0. No ignored opcode text in appended interval from46991. Supports relative subtraction/comparisons and encoder-triggered stop in this scenario, NOT measured90degree yaw. User only said execution complete; final body orientation relative to starting straight still REQUIRED before choosing next target or integrating sensors. Ask one question about perpendicular versus short/beyond; no rerun yet.

CURRENT NEXT TEST: `robot_calibracion_giro.nxc`, separate silent encoder-terminated exploratory yaw calibration. Start aligned with a clear straight reference, away from junction/corner; no approach follower. Cforward15/Areverse15 commands ONCE, take post-command baselines, sample20ms, compute signed relative deltas, stop when EITHER C>=+90 or A<=-90 relative motor counts. Also stop on wrong sign, unassigned30000 sentinel, or60sample cap (nominal1.2s only). This is90 MOTOR counts, NOT90 chassis degrees or a calibrated turn target. No auto-exit/retry, no sound. First reaching target stops both to limit extra rotation if other drive stalls; paired telemetry still needs inspection, not a success guarantee. Twelve-value frame37,90,reason,samples,startA,startC,currentA,currentC,deltaA,deltaC,motorTarget,sampleLimit. Reasons1 C target,2 A target,3 wrong direction,4 cap,5 sentinel. Reads collected before Off; logging only after stop. New signed subtraction and comparison behavior must be checked in fresh runtime, not assumed from Python model. Static checks plus9 Python model cases pass, no NXC compile/run yet. Pretest stdout46991bytes (only useful if append). User compile/load NEW file, run supervised from same reference alignment; report whether final heading is short of/perpendicular to/beyond initial straight reference, not arbitrary degree estimate. No need another generic camera screenshot. Do not rerun from last rotated pose. Previous diagnostics preserved. Full route still unresolved.

Reverse encoder probe executed: user confirms robot-right rotation. Fresh37,89 frame raw [37,89,0,0,0,0,0xfffffff0,16,0xffffffe2,30], signed motor fields [0,0,0,0,-16,16,-30,30]. No ignored opcodes in appended interval starting byte46243. Confirms A negative/C positive progression during observed right rotation. This does NOT establish body angle or90degree target. IMPORTANT bridge precision correction: this execution printed negative longs as full32-bit hex (fffffff0=-16), not merely16-bit words. Prior blanket16-bit-only bridge claim was too strong; signed16 masking is equivalent for these small observed values, but do not truncate arbitrary future longs. Next determine motor-count to robot-yaw conversion independently before setting corner threshold. No repetition of this capability test needed.

CURRENT NEXT TEST: `robot_prueba_encoders_giro.nxc`, separate SILENT center-turn encoder direction probe authorized by user. Place on clear black straight, NOT at corner/junction. Cforward15 / Areverse15, commands issued ONCE, Wait100 + Wait100 (nominal200ms), reads before/start/mid/end BEFORE stopping, telemetry AFTER stop, then silent stationary loop. Same window as proven forward probe; only drive directions and frameID differ. Ten-field frame37,89,beforeA,beforeC,startA,startC,middleA,middleC,endA,endC. Inspect encoder fields signed16 (mask0xffff, subtract65536 if>=32768);30000 sentinel is invalid. Runtime sign/bridge behavior must still be checked; do not assume reverse works from compiler support. Motor progress is NOT yaw calibration, and this does NOT attempt a90degree turn. Static checks pass:8reads,10fields,one command each,sampling sequence matches previous probe; six Python signed-decoder cases pass. NXC compile/run PENDING. Pre-test stdout byte size46243 (use only if append/no truncation). Existing sources preserved. Ask user to compile/load THIS new file, run once supervised, report whether it rotates robot-right; no more screenshots required initially. Full route/90degree/containment remain unvalidated.

Encoder probe executed: user observes only a small movement, as intended. Four new complete37,88 frames appended since byte43303: midpoint/end pairs A=C (17/34),(12/30),(16/33),(15/31); before/start all0. Latest frame [37,88,0,0,0,0,15,15,31,31]. No ignored-opcode text in appended interval. This supports live forward MotorRotationCount readings on BOTH motors; does NOT calibrate robot yaw, wheel diameter, track spacing, reset semantics, reverse signs or reverse encoder operation. Do not equate31 motor degrees with31 body degrees, and do not set motor target90 as90-degree robot turn. Next step: use/test rotation progress during center rotation and determine yaw conversion independently, retaining sensor validation and strict bounds. No additional execution needed for this same forward probe.

CURRENT NEXT TEST (supersedes center-turn reruns): `robot_prueba_encoders.nxc`, silent one-shot forward AC15 pulse with Wait100+Wait100 (nominal200ms), on clear black straight, NOT at stopped corner. Logs rotation counts before motor start, immediately after start, after100ms, after200ms BEFORE motor stop. Ten-value frame37,88,beforeA,beforeC,startA,startC,middleA,middleC,endA,endC. Long vars initialized30000 as sentinel, not valid result; bridge is16-bit, cannot be assumed lossless for arbitrary long counts. Must inspect fresh ignored opcodes and actual movement; stable zeros/sentinels do not validate encoders. Compiler strings verify MotorRotationCount maps GetOutput(...,RotationCount) with field14. Also found OnFwd and Off default RESET_BLOCKANDTACHO; avoid adding per-loop encoder control without understanding reset behavior and rotation-count semantics. No runtime support claimed. Static checks pass; NXC compilation/run pending. Pre-test live stdout size43303 bytes, usable only if log appended without truncation. Existing motion files unchanged. User should compile/load new encoder file and run on straight, supervise, no screenshots needed initially.

User's follow-up center-turn image shows robot still approximately along approach direction, not aligned with screen-left outgoing branch. Therefore reason5 /0,0 after19 samples is a PREMATURE success criterion for a 90-degree maneuver: both-black confirms surface only, not exit heading. Do not call this a successful corner or blindly resume forward. Exact sampled black region (old strip/corner/exit) cannot be identified from those two values alone. Next investigate an independent rotation/progress reference (e.g. whether encoders actually work in bundled RoboSim) before choosing another termination rule; encoder support/kinematic calibration unverified. Do not mask with an arbitrary minimum turn time.

Latest center-turn execution (37,87): [37,87,5,1,257,18,0,0,3,19,3,14,3,17,19,6,19,90]. User reports execution complete; frame confirms reason5 both-black stationary confirmation after19 turn samples, approach257. Right sensor first black6, left17; both-black17-19. Did NOT hit90 limit. Confirms numeric telemetry/source executed, NOT correct heading, reverse direction, center rotation, track containment or legal corner; user visual observation still required. Next ask whether stopped aligned along outgoing screen-left branch or still diagonal. Do not automatically add forward exit based only on0/0.

CURRENT NEXT TEST: user explicitly authorized a center-turn diagnostic, including reverse on one track (local test ONLY, not route legality approval). New separate `robot_prueba_giro_central.nxc` preserves approach exactly, then C forward15 / A reverse15, at most90 samples20ms, stops on white or three both-black confirmations while stationary. No automatic exit/retry/sounds. Previous diagnostics untouched. Equal/opposite drive predicts center rotation ideally; simulator reverse behavior and actual geometry remain unvalidated. Bundled nbc.exe strings confirm `#define OnRev(_ports, _pwr) OnRevEx(_ports, _pwr, RESET_BLOCKANDTACHO)`; no compiler execution performed. Context7 had no relevant NXC library. Frame37,87 has18 fields with same layout as37,85 (configured limit last). Static checks: approach identical,18 fields,reverse onlyA,no sound/AND/OR; five Python model cases for confirmation/reset/timeout/white/single contact pass. These are NOT NXC runtime tests. User must compile/load NEW central file, start from same straight both black, supervise and stop immediately on departure. Reverse does not imply route compliance or authorize a search loop. Await fresh37,87 log and observed motion. Engram still fails unknown_project; continuity here is authoritative.

Trajectory review: current corner code stops A (robot-right drive) and advances C, so under ideal differential-drive kinematics its rotation center is at the stopped right track, NOT the robot center. Mesh bounds from local ressources/*.obj were inspected, but mesh-local geometry alone does not establish runtime sensor placement/transforms, contact footprint, track width or degrees per iteration. Thus no proven geometric correction is available from those files alone. A center-turn diagnostic (left forward/right reverse) would change pivot geometry without translating the ideal drive midpoint, but introduces reverse drive and must be explicitly discussed before implementation; it does NOT guarantee containment or route legality. No code/motion change made in this review. Do not claim the stopped-track pivot itself is proven root cause.

Entry-only test executed: latest 37,86 frame [37,86,2,365,49,49,366,9,0,9,0,3,365,0,1]. Both sensors stayed black for 365 samples then both became nonblack on sample366 (final49/49); no left-only/right-only run in this execution. This does NOT provide an earlier one-sensor cue to trigger the turn. User supplied front-view stop image. Hypothesis: sensor-to-drive-axis offset and pivot trajectory matter; physical cause/offset not measured. Do not blindly turn earlier based on ordinary single-sensor corrections or advance onto gray to align the axle. Entry test compilation/runtime observed; corner still not validated.

NEXT TEST: `robot_prueba_entrada.nxc`, separate SILENT entry-only diagnostic. Same follower motor decisions as baseline, stops on neither black/white/400-step bound, NO pivot. Logs last four sensor-state runs only after stopping, without arrays/new API dependencies. Frame of 15 values: 37,86,reason,step,left,right,samples,oldestState,oldestLength,nextState,nextLength,previousState,previousLength,currentState,currentLength. States 0 neither black, 1 left-only, 2 right-only, 3 both-black, 4 white; 9/0 absent history. Lengths are sample counts, not measured time. Purpose: inspect transitions immediately preceding loss, NOT prove heading or corner classification. Static checks and Python models passed (10,201 reading-pair decision equivalence to baseline; three history examples), but NXC compilation/runtime PENDING. User must reopen source from disk and compile/load this file, not rerun `robot_prueba_giro.nxc`. Start from same straight with both sensors on black; supervise and stop on departure. Existing line and turn files preserved. Do not raise pivot limit again.

90-step experiment executed from the straight (user-confirmed). Latest complete frame [37,85,4,1,360,90,49,49,0,90,0,0,0,0,0,0,0,90]: timeout, ZERO black contacts on either sensor throughout 90 samples. User screenshot shows diagonal final heading, not aligned with outgoing branch. Single extension did not reacquire; DO NOT increase limit again or resume forward. Revisit corner entry/pivot geometry; exact causal geometry still unproven. Consider recording approach sensor transitions before changing entry trigger; single-sensor loss also occurs during normal corrections, so it cannot alone classify a corner. No legal corner validated.

Current experiment supersedes the 60-step source described below: user explicitly confirms latest failed run started from the straight. That run's 37,84 frame is [37,84,4,1,258,60,49,49,0,60,0,0,0,0,0,0,0]: neither sensor sampled any black during the pivot. A single controlled extension changes ONLY the motion limit from 60 to 90 samples, still power 15 and sensor-terminated, no reverse, silent. This tests insufficient pivot travel as a hypothesis, not a proven cause; 90 samples does NOT mean 90 degrees. Do not keep extending if this fails; reconsider entry/pivot geometry. Supervise and stop immediately on track departure. New frame 37,85 preserves all 17 previous positions and appends configured limit (18 values total), distinguishing the loaded revision. Compilation/run pending. Previous reason-5 run with 12 approach iterations is not accepted as equivalent to the long-straight scenario.

Latest instrumented execution: complete 37,84 frame = [37,84,5,1,12,23,0,0,3,24,3,15,3,22,24,10,24]. Confirms user-side compilation/execution of the telemetry revision and both-black stop (reason 5), NOT timeout: right sensor first black sample 10, left 22, both black samples 22-24 with final stationary confirmation. Only 12 approach iterations before pivot, unlike previous long-approach tests; initial placement/scenario equivalence is unconfirmed. Ask whether it finished pointing along the outgoing branch, without requesting another generic screenshot. No validated 90-degree angle, containment, or full route yet.

Latest source revision keeps motion unchanged (power 15, 60 turn iterations) and adds per-sensor black counts and first/last black sample positions, emitted only after motor stop. New 17-value frame: 37,84,reason,phase,approachIndex,turnIndex,left,right,stable,turnSamples,leftBlackCount,rightBlackCount,bothBlackCount,firstLeft,lastLeft,firstRight,lastRight. First/last positions are one-based; 0 means never observed. Counts include stationary confirmation samples. Static checks passed; this revision has NOT been compiled or simulated. Earlier 37,83 runtime results below belong to the previous version. User cannot raise camera further; do not insist on more top-down screenshots. Counters detect sampled contact, not exact heading, containment, or definitive geometric cause of failure.

Update after user execution: user reports corner rotation followed by stop and supplies a head-on screenshot. Latest complete 37,83 frame: reason 4, phase 1, approach index 230, turn index 60, readings 49/49, stable 0. Thus the pivot exhausted its bound without confirmed reacquisition; do not call the corner successful or automatically resume forward. An earlier frame has reason 5, approach index 0, turn index 58, readings 0/0, stable 3: it started pivoting immediately and is NOT evidence of the same straight-to-corner scenario. Current heading/containment and safe pivot geometry remain unvalidated. Do not blindly increase the turn limit.

- User confirms this test corner turns robot-right, screen-left in the head-on view. This is NOT a full-route decision.
- `robot_prueba_giro.nxc` preserves the straight follower separately, then triggers a right forward pivot on both-gray/no-black. A is stopped and C advances at 15, bounded by 60 iterations of 20 ms (nominal only). No reverse or sounds.
- Stops at white, approach limit, pivot limit, or three stationary both-black samples after reacquisition. Reacquisition does NOT establish 90-degree heading or containment; supervised visual verification remains required. Stop the simulator immediately if leaving the track.
- Frame: decimal 37,83,reason,phase,approach index,turn index,left,right,stable count. Reasons: 1 white, 3 approach limit, 4 turn limit, 5 both-black confirmation only. Indices are zero-based. Do not parse this as the baseline 37,82 frame.
- Last live log inspected before this change ends with baseline reason 2, 258 iterations, 49/49. No new corner runtime evidence yet.
- Engram project detection matched the workspace, but reads/writes failed with `unknown_project`; rely on this file for continuity.

1. Read the latest sources and inspect the current live log. Establish only genuinely new evidence; do not repeat all calibration.
2. Build a separate SILENT corner diagnostic for the previously tested straight ending at a visible 90-degree bend. Ask for the local initial view only if necessary to choose the real outgoing branch and turning direction.
3. Use sensor-confirmed reacquisition plus a strict motion bound; do not rely on a fixed turn duration as success. Avoid reversing/search loops that could repeat segments. Stop on uncertainty. Even forward arc/pivot motion must be checked for leaving the black surface.
4. Verify the selected NXC instructions against BOTH this older compiler and the runtime; compile through the user's proven workflow unless a local runner is actually found. Capture runtime evidence in the log, not strings or beeps.
5. Separately resolve intersection-zone semantics and a legal full-coverage route. Then add entry/exit confirmation, navigation progress, gated marker detection, two laps and final stop.
6. Only then tune speed and repeatability. No measured competition times currently exist.

## Acceptance status

Observed: diagnostic user-side compilation, motors forward, black/gray/white distinction, sensor side mapping, stdout telemetry, qualitative straight tracking/corrections, bounded silent stop. Pending: corner legality, junction recognition/decisions, validated full route, counterclockwise departure, no repeated segments, three correct marker sounds, two complete laps, valid final stopping position, repeatability, speed/time measurements.

## Suggested new-chat request

> Continue this RoboSim/NXC project. Read CONTINUIDAD.md, robot_prueba_linea.nxc and PLAN_OPTIMIZACION.md first. Keep diagnostics silent; do not repeat calibration or assume the provisional route is valid. Next implement and validate one bounded, sensor-terminated 90-degree corner test before integrating intersections and two laps.
