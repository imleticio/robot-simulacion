# University robot practical — route validation pending

## Current priority

**User explicitly selects the original3/4configuration and SAMEreactivefile.**
38,3reads lights3/4, preserves A/Cand1/2pictured setup, logs on non-navigation1.
Swap correction pairing to match actual3left/4right andAright/Cleft; not a blind
port renumber. Add743sampledA-Cceiling for a persistent SAMEone-sided correction,
reset on reacquisition/opposite/white, not a mandatory90turn or whole-leg budget.
No map/18turns/graycornerguess.239testsPASS;38,3NBC/runtime pending. Current
REACTIVO_SIMPLE.md section overrides the earlier1/2instructions below.

**Active file updated to38,2, not another variant.**38,1log showedreason2/samples0,
readings49/49twiceand49/0last. Startup wrongly required bothblack despite a follower
that can correct one-sided contact. Startup/marker rearm now use3consecutive
non-white samples with at least one black; both-white confirmation still3. Keep
gray/graystop, same powers/configuration/port3telemetry. Fault logs now preserve
the rejecting sample;38,1used post-stop values.234testsPASS;38,2NBC/powered
runtime pending. Do not turn knobs or ask for another unchanged execution.

**User authorized choosing the simpler adaptation. Active candidate is now the
standalone `robot_reactivo_simple.nxc`, paired with the friend's downward1/2sensor
arrangement.** No scripted route/18turns/encoder-angle target. Preserve old3/4knobs
and111files; move telemetry off active1to unused3. Read REACTIVO_SIMPLE.md before
reconfiguration/compilation.230testsPASS; newNBC/runtime/actualgeometry pending.
Returning to white is only a candidate, not full-branch or two-lap proof. Previous
3/4route work below is historical and not the next experiment.

**116changes the navigation handoff, not another numeric B seed.** User objects
that repeated turn/exit trials never deliver a lap and accepts another route order
if all black branches are covered. Latest115again reached the B pivot but stopped
reason15at200exit intervals despite both totals>=180(stable3/2, not5). New
`robot_vuelta_integrada_continua.nxc` retains first exit/B450origin, then follows
continuously after later pivots, tracking pending progress until the next trigger
or final marker.214testsPASS;116NBC/runtime pending. Preserve all real fault guards
and full-branch goal; do not call mocked flow a physical completed lap.

**Next is115: `robot_vuelta_integrada_cruce_tardio.nxc`.**114did order the second
right pivot and reachedA0/C744or745, but its exit failed twice at200intervals:
A340/C169stable0 andA371/C202stable1. Do not confuse this with incomplete pivot
or a reason to increase rotation/exit budgets.115tests ONLY firstB370->450as a
later-placement hypothesis; it does not prove the old entry was early.203testsPASS;
115NBC/runtime pending. Shared controller, first pivot, route and all guards unchanged.

**Next is114: `robot_vuelta_integrada_cruce.nxc`.** Review of the user's24.54s
recording shows straight passage through the intended second branch before the
far bend stop. Multiple113terminal means710.5..760never reached1200.114changes
only firstBreference to370(~half observed available leg, NOT measured B position)
and revision. Shared controller/return450/pivot/exit/route unchanged.198testsPASS;
114NBC/runtime pending. One integrated supervised attempt, not another corner test.

**113supersedes112as the next integrated run.** User reported stopping at the
first bend; actual112frame reason19phase2turn0had A528/C466,sensors0/50,pivot0/0.
The short continuation's60-count difference guard was incorrectly applied to the
entire approach. `robot_vuelta_integrada_aproximacion.nxc` restores11120/10/25
approach and keeps the60budget only after white entry, with a separate baseline.
First leg cap400; pivot/exit/route/Breferences unchanged.193testsPASS;113NBC/runtime
pending. Keep the before-white integrated starting position; do not resume isolated
corner tests. Current details in VUELTA_INTEGRADA.md and CONTINUIDAD.md.

**Integrated attempt prepared:** `robot_vuelta_integrada.nxc` (37,112) now targets
the user's red route, using the photographs rather than requiring a saved track.
See [VUELTA_INTEGRADA.md](VUELTA_INTEGRADA.md) before running: start before white,
not on the isolated-corner approach. The18turn sequence, two unmeasured B reference
seeds1200/450 and upper shared-region interpretation are hypotheses for one
supervised integrated run.181host/audit tests pass; NBC/RoboSim validation is
pending. The37,111baseline is preserved. Older isolated-corner next-run sections
below are historical; do not request another unchanged corner trial.

The user clarified this is a university practical demonstration, not a prize
competition. Favor a simple, explainable solution over performance tuning or
contest polish. Existing two-lap/counterclockwise/full-coverage requirements have
not been waived; do not silently relax them. Historical competition wording
below reflects earlier framing, not a new requirement to optimize for prizes.

The user subsequently clarified that the entire circuit must be covered without repeating the route. Treat every branch and both loops as required; do not use a perimeter-only solution. The official wording also prohibits repeating any part of the track within each lap. The remaining ambiguity is the boundary of the extended upper intersection: whether the short A1-A2 connector is a separately required segment. Do not optimize speed or claim a competition route is valid yet.

## Image-based provisional topology

Reference: the user's full-track image with the marker at bottom-left and the upper-loop close-up provided afterward. These screenshots are conversation evidence, not image files stored in this repository.

| Node | Location in that reference |
|---|---|
| A1 | Upper central vertical strip, side entrance from the right |
| A2 | Same strip, lower side entrance from the inner left path |
| B | Main central junction, reached from the marker via the bottom bend |
| C | Main right junction, adjacent to the large right loop |

Collapse ordinary corners into edges, but provisionally keep the short A1-A2 connector separate:

| Edge | Endpoints | Physical path |
|---|---|---|
| e1 | A1-A2 | Short central connector between staggered entrances |
| e2 | A1-A2 | Small upper loop, excluding e1 |
| e3 | A1-B | Outer left path including the white marker |
| e4 | A2-B | Inner left path |
| e5 | B-C | Direct horizontal middle path |
| e6 | B-C | Raised rectangular detour above e5 in the reference image |
| e7 | C-C | Large right loop, excluding its shared junction |

This is a provisional graph inferred from images, not a surveyed metric map. In particular, whether e1 counts as a separate required segment or as movement inside one extended intersection is unresolved.

Later close-ups confirmed staggered side entrances but did not establish contest semantics for the shared region. The earlier assertion that these must be two separate T junctions was too strong. Keep both the node split and edge e1 provisional; do not equate the conditional Euler result with a demonstrated impossibility of the actual contest.

## Coverage constraint check

Under the seven-edge model, degrees are A1=3, A2=3, B=4, C=4 (the C self-loop contributes two). A connected undirected graph admits a closed walk using every edge exactly once only when every vertex has even degree. This model has two odd vertices, so that particular full-coverage closed walk is impossible.

This does NOT prove the contest is impossible. It identifies a rule/model ambiguity: full segment coverage may not be required, or the short connector may belong to one intersection area rather than be a separately counted segment. Do not silently omit a loop, repeat the connector, or invent a connection to bypass this question. The previously discussed route is not validated.

A small Python degree-count calculation was run successfully during analysis. This is mathematical verification of the provisional model, not RoboSim movement validation.

## Verified baseline and control choice

- Initial stationary observations: black 0/0, gray 50/50 (49 also observed), white 100/100.
- Paired edge tests identified sensor 3 as robot-left and sensor 4 as robot-right.
- Output tests with the user's configured side assignments support C as left drive and A as right drive; positive power on A/C together moves forward.
- User observed straight travel and realignment from initial deviations in both directions at low power. No quantified repeatability data or steering-event telemetry yet.
- Use the existing low-power nested-branch follower as the baseline. PD remains an experiment until edge-position readings show useful resolution; three distinct surface values alone do not establish that.
- No AND/OR, display text, string formatting or task-end behavior may be assumed supported merely because NBC compiles it. Runtime logs exposed ignored instructions. The current follower avoids boolean AND/OR and stays in a silent stationary loop after stopping.

## Next validation steps

**111runtime observed:** latestreason17phase5,pivotA0/C746in200samples,200progress/
0flat;200RESET_NONEcommandrefreshes,0power mismatches,latest15/15.No ignored
messages. Exit163criterionthencontinuation83,sampledA124/C180,final0/0,programmed
segmentendpoint. Threepriorreason2initialrejections49/49or0/49hadNOmotion;not
cornerfailures. NewAPI/fullRXEpathworksinthisrun,butnopowerlosswasobserved,so
notproofrefreshcausedimprovementorallstallsfixed. No duplicate run requested,
no code/settings changes. Keep111ascurrenttestedlocalbaseline;fullroutepending.
Fullframe/currentstate atopCONTINUIDAD;pending111runtime notes superseded.

**Current111 active pivot command:** `robot_prueba_codo_mando.nxc` preserves110
parameters/guards and reasserts Cforward15 each pivot interval usingRESET_NONE,
without resetting original encoder baseline. Reads MotorPower before/after;
stop22if after!=15,existing21if40flat samples. This is a bounded hypothesis, not
proof the previous failure lost a command. Power15readback is not actual motion;
frozen/lifted physics can still stop.76fields=72+refresh/mismatch/before/after.
Officialdocs/bundledmacros and actualx86resetdispatch checked; flags07doesnot
dispatch counter resets,unlikelegacy2f.156auditvenvtestsPASS;NBC/fullRXE111runtime
PENDING. Same patched window/sensors,already-openBricx,one supervisedrunfromoriginal
straight with NEW111RXE. No calibration/retuning/video. Evidence/addresses in
`evidence/robosim-pivot-command-refresh-2026-11-06.json`;instructionsatopCONTINUIDAD.

**110runtime observed:** first run stopsreason21with40zero-Csamples(progress0,
flat40,longest40), not expandedhardcap. Latestreason17completespivotC745in197
samples(progress197/flat0),exit146criterion,continuation81sampledA131/C182,
final0/0. No ignored messages. Bigger cap did not cause this pass(<240samples).
Read-only investigation: normal pause also gates VM; a different lifted-input
state bypasses normal encoder integration, but its activation during failure was
NOT observed. No user blame/cause claim, no new patch/parameter edits or identical
rerun requested. Fullframes/addresses/limits in
`evidence/robosim-110-runtime-and-input-state-2026-11-06.json` and atopCONTINUIDAD.
Zero-progress cause and repeatablealignedcorner remain unresolved;routepending.

**Current37,110 pivot budget correction:** inspected ordinary motor model gives
150counts/s atpower15;C743requires~4.953s/248ideal20msintervals, whereas old240cap
gives4.8nominalseconds/720idealcounts. New `robot_prueba_codo_tiempo.nxc` preserves
109geometry/powers/target/exit/continuation and uses375samplehardwatchdog plus
reason21after40consecutive unchangedCreads; backwardsdelta jumps stop7. This is a
model-based budget correction, NOT an explanation of C165 or a guarantee against
all stalls. New72fieldframe=68+progress/flat/longestflat/limit40.146auditvenvtests
PASS, NBCcompile/runtime110PENDING. Same patched window/sensors, already-open
BricxCC, one supervised run from originalstraight. Do not reopen normal shortcut,
retune sensors or recalibrate. Assumptions/evidence and instructions atopCONTINUIDAD.

**109runtime observed on hash-verified patch, remaining partial-pivot failure:**
PID72609yield matches audited SHA256. Live10591bytes first109frame reason4phase1
C165at240samples(noexit),latestreason17phase5pivotC746/199samples,exit164criterion
passedTHEN85continuationintervals52both+33right,sampledA126/C180,final0/0.
No ignored messages afterlatest,stderr empty. Latest segment endpoint is intentional,
but the patch has NOT eliminated all partial-pivot behavior; cause remains unproven.
No code/settings/limits changed and no identical rerun requested. Investigate
remaining pivot-progress discrepancy separately before claiming reliability or
adding route decisions. Evidence `evidence/robosim-yield-109-runtime-2026-11-06.json`;
full context atopCONTINUIDAD. Pending109runtime notes below are superseded.

**Current37,109 continuation on the patched runtime:** second108run inPID64680
yieldcopyalso passedreason16:pivotC746in200samples,exit151(75both76left),sampled
A327/C190,stable5final0/0;live7926bytes,noignoredmessages. Two patchedpasses,
NOTproofgeometry/alignment/historicalcause. No thirdidenticaltrial. New
`robot_prueba_codo_continuo_sin_avance.nxc` preserves108position0/pivot/powers/
criteria and enables ONLY the existing106boundedcontinuation afterreason16.
No reintroduced60advance, no retuning, secondturn or markerintegration.68field
frameversion109,position0; continuationlimits180firsttrack/+/-60difference/
120samplesunchanged.135auditvenvtestsPASS;NBCcompile/runtime109PENDING. Keep
currentpatchedwindow/sensors;one supervisedrunfromoriginalstraightwithNEW109RXE.
Evidenceforsecond108runandfullinstructionsatopCONTINUIDAD;oldernextactions
superseded. Fullcorner/containment/twoCCWfullcoverage route remain unvalidated.

**First patched GUI run observed:** existing37,108RXE ran in verified
`legosimulator-yield.exe` PID64680, launched through the existing Wineskin CMD,
without changing wrapper startup or NXC. Paired panel close-ups visually matched;
exact angles/pose equivalence not measured. Fresh log3963bytes: reason16, pivot
A0/C746in192samples,exit152(78both+74left),sampledA317/C191,freshboth-black5,
final0/0. No ignored messages. One pass does NOT prove patch repeatability,
historical-stall attribution, geometric alignment or route validity; old executable
also had passes. Keep patched window/configuration/108RXE fixed and perform one
supervised confirmation run, no recompile/calibration/video or parameter tuning.
Evidence: `evidence/robosim-yield-first-runtime-2026-11-06.json`; fullframe/current
instructions atopCONTINUIDAD. Older pending-deployment/runtime notes superseded.

**Scheduler audit supersedes old next-run instructions:** a VM scheduler defect
was reproduced using actual x86 runner bytes: multiple Wait20 intervals can expire
before physics updates within one long VM batch. Separate `legosimulator-yield.exe`
changes one branch displacement to recheck the existing wait gate after each step.
Original simulator/NXC/RXE and all motor settings/guards preserved.133hosttestsPASS
with audit dependencies, including7machine-code/patch tests and2entry-geometry
counterexamples. Full simulator runtime remains pending; historical C193/C683
attribution is a hypothesis without frame timing. No claim of solved corner.

Entry geometry remains underdetermined: contact does not constrain entry yaw;
relative quarter-turn retains that yaw error, and omitting advance changes position,
not heading. Do not tune743/power/caps or resume laps. First open the alternative
executable WITHOUT running or closing the current simulator, preserving current
scene/configuration for exact migration. Details, rollback and limitations at top
of CONTINUIDAD and `evidence/robosim-scheduler-audit-2026-11-06.json`.

**37,108 runtime observed:** latestreason16,position0,pivotA0/C743,exit169intervals
(75both+94left-only),sampledA349/C192,5freshboth-blackafterboth>=180,final0/0.
Earlier108reason4stoppedpartialpivotC683at240samples, noexit. Live125734bytes,
no freshignoredmessages. No-pre-advance did NOTeliminateone-sidedcorrectionsor
partialpivotfailures; no provenfix/improvement/rankingagainst105withoutmatched
poses. Criterionpassisstillintentionalendpoint,notfullcorner/routevalidation.
No source/settings/cap changes or identical rerun requested for this review.
Separate investigation of pivot progress variability and outgoing correction
remains;do not assume their cause or alterangle/removeguards. Fullframesatop
CONTINUIDAD;olderpending108notes superseded.

**Current37,108 combined no-advance corner/exit:**107latestreason14showed
positionTarget0,A0/C746andstationaryboth-black3;earlier107reason4stoppedC193at240
samplesBEFOREfullpivot,causeunknown. No freshignoredmessages;onecontactpassdoes
notproveafix. `robot_prueba_codo_salida_sin_avance.nxc` preserves105pivot/exit
criterion,powers/guards/caps,changesONLYposition60->0relative105,andenablesexisting
controlledexitcomparedwithobservation-only107. No continuation/secondturn/search/
reverse/sounds.50fieldlayoutversion108/positionTarget0,reason16boundedcriterion
only,15inconclusivewatchdog.124hostchecksPASSinclpreprocessing105equivalence
afterpositionstage;NBCcompile/runtime108PENDING. Samecurrentwidersensors,
originalapproachstraight,bothblack,onesupervisedrun. No newcalibration/video.
Full107frames and runinstructions atopCONTINUIDAD. Older next-actions superseded.

**Current37,107 isolated corner geometry test:** user redirects focus to corner.
`robot_prueba_codo_sin_avance.nxc` omits the experimental60countpre-pivot advance,
keeps approach/pivotC743A-braked15/cap240/contact check unchanged, and stops after
the check (no outgoing/continuation stages). Relative to observation-only101,
only pre-pivot translation changes. Translation along approach changes lateral
position relative to an ideal quarter-turn exit; this motivates testing omission,
NOT claiming the cause or a fix. Keep current wider sensor settings unchanged.
39fieldframe,version107,positionTarget0/unusedpositionfields;reason14observation
stopmaystillbeone-sided,notalignmentvalidation.120hosttestsPASS including actual
preprocessing equivalence after the positioning stage. NBCcompile/runtime107
PENDING. One supervised run from original approach straight, no recalibration.
Expected deliberate stop after pivot; do not ask why it does not drive onward.
Fresh106reason20/phase5final49/0 was recorded before edits (log111502bytes), not
promoted to success. See currentCONTINUIDAD for fullframe/runinstructions.

**37,106 runtime reviewed:** live106226bytes has earlierreason15/phase3exit200,
174right-only,A58/C355,so continuation correctly blocked. Latestreason17/phase5
actually executed77continuationintervals(49both+28right-only),sampledA128/C180,
entry/final0/0,status1,thenhitdeliberatelyshortfirst-track180endpoint. No ignored
messages; function-call/runtimepathworked. This does not prove a long aligned
straight or fix earlier repeatability failures. User reports little/no visible
change: do not dismiss that or claim a large measured distance. No code/settings
changes, no duplicate run requested, no arbitrary capextension as a fix. Full
frames/currentinterpretation atopCONTINUIDAD;olderpendingruntime notes superseded.

**Current37,106 bounded local continuation:** `robot_prueba_continuacion.nxc`
preserves105 and enters phase5 ONLY after reason16/finalboth-black. Helper
`robot_continuation_stage.nxc` rechecks entry and follows with the same powers,
using separate sampled totals. Stop at first track180, signed difference+/-60,
120interval watchdog, or existing white/loss/encoder guards. Final sensor sample
catches last-interval loss and downgrades one-sided endpoint contact. Reasons
17segmentlimit,18watchdog,19differenceguard,20inconclusivecontact are NOT route
success. These provisional sampled references do not guarantee distance, heading,
containment or identify junctions. No second turn/marker integration/sounds.
New68fieldframe=105first50+18continuationfields (schema/currentruninstructions
atopCONTINUIDAD).116hosttestsPASS, including17actualhelper tests with simulated
APIs and preprocessing checks. NBC/function-call/runtime106validation pending.
Keep current sensors, original approach straight, one supervised run. Earlier
105failures still matter; no complete corner/fullroute/two-lap claim is supported.

**Current video105 review:** accessible Desktop024435clip shows approach/rightarc,
short outgoing motion andstop. Fournew105logframesallreason16/final0/0withexit
144/130/124/148,bothsampledtotals>=180,stable5before200cap;latestA318/C188.
TheseareINTENTIONALdiagnosticcriterionstops,notnewline-lossfailures. Exactvideo
framepairunknown. Do notaskforanothersamevideoorclaimthisclipcapturespriorfailed
pivot. Evidence `evidence/robosim-video-review-2026-11-06-024435.json`.
Earlierreason6/15failuresremainunresolved;noexactheading/containment/fullroute
validation. Motioncodeunchanged;markerworkparked. Nextfunctionalsteprequires
boundedcontinuationaftercriterionwithguardsandexplicitjunction/routeconstraints,
notarbitrarysecondturnsoranothercounterchange. See current CONTINUIDAD.

**Priority reset: fix corner landing before marker/route integration.** Fresh105
evidence atlive79846bytes includesreason15exitwatchdog(A57/C417,178right-onlyoutof200)
andlaterreason6phase2(position64/64,pivotC743,stationary49/49,exit0). Theearlier
reason16passisnotrepeatable. AtleastonefailureisBEFOREexitcontrol,soexitcriteria
orlapcountercannotrepairit. Parkmarkerwork;retainwhite/lossguards,no capextension
orblindretuning. Investigateapproach/position/pivotgeometrywithspecificfailed-turn
evidence,notgenericcamerachanges/recalibration. FullframesatopCONTINUIDAD.

**Marker logic increment completed (not integrated):** `robot_marker_tracker.nxc`
adapts the user's reference without its high-power single-sensor follower. It
requires confirmed black release and confirmed two-sensor white detection, counts
start + two finishes correctly, and accepts lap crossings only when a validated
route controller authorizes them. Premature crossings and invalid readings emit
fault events, not laps. No sounds or motor commands. The caller must stop on
finish/fault and reset route progress between laps; the module cannot verify
route coverage itself. README documents its contract.

99 host tests PASS, including 21 that compile and execute the actual API-free
NXC module as native C. NBC compilation, marker timing/coverage in RoboSim and
integration remain pending. No existing motion diagnostic changed and no new
user run is required for this increment. Full-route graph/intersection semantics
must be resolved before wiring route permission; never substitute a constant1.

**37,105 first valid criterion pass:** reason16 at132exitintervalsBEFORE200watchdog;sampledA279/C189,both>=180,5freshboth-blackreadingsandfinal0/0. Exit80both+52left;position60/60,pivotA0/C745. Onepriorinvalidstart49/0separate. Live stdout60018bytes,nofreshignoredmessages. Criterionpassedonce,NOTexactalignment/containment/legalcorner/fullroutevalidation. Freezecode/settings;oneconfirmationrunofsame105fromoriginalapproachstraightbeforeintegration,no recompile/calibration/parameterchanges. Fullframe/currentinstructionsatopCONTINUIDAD;olderpendingnotesaresuperseded.

**Current37,105 controlled-exit criterion:** `robot_prueba_salida_controlada.nxc` nowrequiresbothsampledexitmotortotals>=180,THEN5freshboth-blackreadings,andboth-blackafterstop. Reason16=boundedprogress/contactcriterionONLY,notalignment/routevalidation. Persistentonesidedorzerowheelprogresscannotpass;reason15watchdog/inconclusive. Exitwatchdog200(previous100)permitsboundedreacquisitionbeyondoldcutoff,NOTcap-success. Steeringpowersandallapproach/position/pivotconstantsunchanged;white/loss/encoderstopsretained,no secondturn/search/reverse/sounds. Thisdoesnotguaranteerealignment;sampled180isaprovisionalmotorreferenceNOTphysicalexitdistance. New50fieldframe=10447fields+target180/confirm5/actualfreshstablecount.78hostmodel/staticchecksPASS;NBCcompile/runtime105PENDING. Samecurrentsensorconfiguration,originalapproachstraight,onesupervisedrun. FulltwoCCWlapsstillnotimplemented;detailsatopCONTINUIDAD.

**37,104 executed: measurement not motion change.** Threecompleteframesexit100/status1/measuredSamples100. SampledtotalsA/C218/155,0/171,221/122; latest44both+56left-only/final0/49. Middleframewas100right-only,zeroboth-blackintervals,final49/0,Abrakedthroughout. Thisprovesblackcontact+capcanrepresentonlybrakedtrackcorrectionarcsratherthanalignedforwardfollowing. No fullodometry/headingclaimfromsampledcounts. Do NOTrequestanotheridenticalmeasurementrunorcalibration. No newmotioneditsmade;nextdesignmustseparatealignment/reacquisitionfromcap/contactbeforefullrouteintegration. Currentlog52094bytes,nofreshignoredmessages;fullframeatopCONTINUIDAD. Pending-runtimeinstructionsbelowaresuperseded.

**Current37,104 measurement diagnostic:** new `robot_prueba_salida_medida.nxc` keeps103motion/cap100/powers/geometry/safety unchanged; adds per-interval exit A/C post-commandbaselines and pre-resetcurrentreads, accumulatingnonnegativedeltas. New47fieldframe=old39+8measurementfields (schemaatopCONTINUIDAD). Sentinel/signfaultstopreason8/7inphase3;zeroisreported,nottravelvalidation. Reads add runtimeoverhead; sampledcountsarenotfullodometry/heading/distance and do NOTyetcontroltermination.67Pythonmodel/staticchecksPASS includingclangpreprocessorframe/commandchecks;NBCcompile/runtimePENDING. User compile/loadNEW104RXE,samecurrentwidersensors,originalapproachstraightbothblack,runonce supervised. No newvideo/recalibration/capextension. Inspectfresh104logbeforemorechanges. Earliernextactionsbelowaresuperseded.

**Video review completed:**10.623333s clip shows rightarc followed by short outgoingtranslation, thenstop; not merely stuck/in-place spin, but no longstraight/fullcorner validation. Two new37,103logframesbothcap100/final0/49; latest52both+48left-only,position62/62,pivotC745. Exactvideo/framepairingunknown; bothconsistentwithprogrammedstop. Evidence `evidence/robosim-video-review-2026-11-06-020337.json`. No code/settings/capchanges and no newvideo/calibration requested. Preserve current setup; next design work should define meaningful bounded outgoingtravel/alignment evidence rather than keep extending arbitrary sample caps or add secondturns. Details atopCONTINUIDAD.

**37,103 executed:** latestreason10phase3,position62/62,pivotA0/C747,stable3both-black,exit100intervals49both+51left-only,final0/49. Earlier same-revision run aborted positioningcap with0/0progress; do not omit that failure or assert its cause. Contact persisted to100cap in latest run, but intervalcounts do NOT measure forwarddistance/heading; braked-trackleft-only correction can rotate while retaining contact. NO furthercapextension or secondturn yet. Next inspect short fixed-camera video of existing103approach/turn/exit throughstop, with corner/outgoing strip visible, to distinguish translation from prolonged correction arc. No configuration/code/calibrationchanges. Details/fullframes atopCONTINUIDAD; log34611bytes, nofreshignoredmessages. Earlier pending-runtime notes are superseded.

**Current37,103 extended observation:** second valid37,102 run after sensor spread reached50exit intervals allboth-black/final0/0 (position61/61,pivotA0/C744,stable3). Previousnewconfigurationrun reached50withfinal0/49,5left-only corrections. Two valid bounded runs justify observing beyond50, NOT declaring solved. `robot_prueba_salida_extendida.nxc` changes ONLY cap50->100 relative to37,102, retaining12/12andbraked9corrections, allmaneuverconstants/guards and silent stop. Same39field telemetry,revision103,exitStepLimit100. No secondturn/search/retry or driving on gray.57hostmodel/static testsPASS; NXCcompile/runtimePENDING. User run once supervised from original straight with current approximate sensor spread unchanged; seeCONTINUIDAD for instructions. All older next-actions below are superseded.

**First37,102 run after approximate sensor-spread change:** reason10/phase3, position63/63,pivotA0/C745,stable3both-black,exit50intervals (45both-black,5left-only),final0/49. Fresh log22025bytes, no ignored messages in appended frame suffix. One-sided correction now occurred and one sensor retained black at cap, but this does not prove recovery/repeatability/containment or full corner traversal. Keep configuration/code fixed and repeat once from original approach straight to check newly changed setup before extending behavior. No cap/power/angle edits, no calibration, no second turn. Earlier next-action sections below are historical.

**Current investigation: sensor observability, no new run.** User objects to repeated inconclusive tuning. Static EXE/PDB evidence confirms integer-coordinate light-cell lookup and constructor port3/4 default angles+5/-5 (NOT verified active angles). Ideal radius1.15 mount model gives separation~0.20046 at5degrees; wider spread changes both separation and forward offset, so no angle should be changed based solely on this model. Evidence: `evidence/robosim-sensor-geometry-2026-11-06.json`;53offline tests PASS. Actual active GUI angles/placement remain unverified. No desktop-control tools available. Do not continue blind speed/cap tuning or claim this audit proves the departure cause. Motion configuration remains unchanged; no repeated identical run requested.

37,102 runtime: one valid run reached50exit cap allboth-black/final0/0, but latest lost black after8exit intervals ALLboth-black/final49/49,reason11. No one-sided corrections occurred in either valid run. Therefore slower exit is not a demonstrated repeatable fix; do not tune correction power on this evidence, increase cap or remove loss guards. Keep current motion unchanged and investigate geometry/trajectory; do not request another identical rerun merely to accumulate samples. Live stdout18881bytes; current frames recorded atopCONTINUIDAD. All pending-runtime notes below are superseded.

**Current37,102 slow-exit experiment:** user delegates tuning decisions; no technical-choice questions. `robot_prueba_salida_lenta.nxc` preserves approach/position/pivot/contact and scales only exit powers20/20->12/12,0/15->0/9,15/0->9/0. Same50interval cap and loss/white stop guards, no sounds/search/second turn.49hostmodel/static tests PASS; NXC compile/runtime pending. This tests slower sampled exit, not a proven fix; at unchanged cap it likely covers less distance, so cap completion alone cannot prove improved tracking. Existing37,100/101 defaults preserved. See current CONTINUIDAD section for run instructions. Following next-run instructions are historical.

37,101 runtime observed: reason14/phase2, positioning60/60, pivotA0/C744, stationary0/0 stable3, exitSamples0. User reports a good-looking stopped pose. This isolates one acceptable pre-exit observation, NOT a repaired maneuver or repeatable corner traversal. Geometry was unchanged; keep pivot parameters fixed while investigating the bounded exit. Log was truncated/recreated to6297bytes; prior byte offsets must not be reused. No new motion changes made for this result.

**Current next run: 37,101 observation-only diagnostic.** Latest37,100 executed and lost black after8exit intervals (4both-black,4right-only), with positioning60/60, pivotA0/C744 and stationary both-black confirmed. User reports departure in the corner. Before more geometry/control changes, `robot_prueba_pose_codo.nxc` preserves the maneuver but stops BEFORE exit: reason14/phase2/exitSamples0 after confirmed contact. Existing safety failures remain unchanged. No recalibration or blind recovery. This isolates end-of-pivot pose; it is NOT an alignment fix or corner validation.45host model/static tests pass; NXC compile/runtime pending. All next-run paragraphs below are historical.

**CURRENT37,100 exit-steering experiment:** user confirms returningrobottoapproachstraight. Keep approach,position60,pivot743,confirmationandallcaps/guardsUNCHANGED. ChangeONLYone-sidedEXITsteering: left-onlyblackCbraked/A15;right-onlyblackAbraked/C15;bothblackstill20/20. Thisreducesforwardadvance andtightensidealcurvature comparedwithold10/25or25/10, withoutreverse/search/secondroutecorner. Hypothesisonly,notprovenrootcause.39fieldtelemetryunchangedexceptversion37,100.43hostmodel/statictestsPASS,NXCcompile/runtimepending. Lostblack/whitestillstop; do notpresentcapcompletionaslegalcorner/fullroute. Earlierparagraphsbelowarehistory.

37,99runtimeupdate: latestposition61/61countsthenpivotC745,stationaryblackconfirmed,exit14intervals(13bothblack+1right-only)then49/49reason11. Previoussameversionrunposition63/63andexit50capfinal0/0(19left-onlycorrections); anotherframepositioncapwithzeromotorprogress. Strongrunvariation,notvalidatedrepeatability. Askwhetherinitialplacement/heading/configwasmatchedbeforeadditionaltuning; nofurtherlimits/geometrychangeswithoutcontrollingthatvariable. Lateststopisline-losssafety,notanunimplementedsecondturn.

**CURRENT37,99 authorized positioning experiment:** user approved a small forward reposition BEFORE the pivot, not more exitduration/angle changes. After original approach loses black, BOTH motors forward15 until first60relativecount threshold; allow pivot ONLY if both>=60. Separate30sample20ms cap, white/sentinel/wrongsign/unequalprogress aborts, then stop and take fresh pivot baselines. Gray is allowed only in this explicit short positioning experiment; after pivot, normal contact confirmation/white/neitherblack guards remain. Keep pivotC743/Abraked, cap240, exit50, no secondturn/search/reverse/sounds. Adds phase4 and reasons12positioncap/13unequalpositionprogress; new37,99 frame39fields appends11positionfields (schema atopCONTINUIDAD).41hostmodel/static testsPASS; NXCcompile/runtimepending.60motorcounts is exploratory, not measured offset/containment/legality; supervise. Restore sameoriginalstraightbothblack before each run, not stoppedpose. All following experiment paragraphs are historical and superseded by this current summary.

Latest37,98 exit50test stopsreason11after26intervalsallbothblackthen49/49,wellbefore50cap. PivotA0/C743andstationaryblackconfirmed. Exitstillnotstable; no morecapextensions. Discuss changingpivotentryposition viaasmallencoder-boundedforwardrepositionbeforeturn, notchangingangleagainoradvancingafterexitloss. This isanunprovengeometryhypothesiswithpotentialedge-clearancecost,notimplemented/authorizedyet andnotroutevalidation.

**CURRENT37,98 longer exit observation:** video reviewed via sampled/fullresolutionframes, with separate newlogframes. Latest37,97 run completed25exitintervals allbothblack and final0/0, reason10programmedcap; previousrunlostline23intervals, reason11, so not repeatable. No definitevideo/logrunpairingfromfilenamealone; evidence in `evidence/robosim-video-review-2026-11-06.json`. ChangeONLYexitlimit25->50, keepC743/A0pivot,powers,confirmationandwhite/lossstops; nosecondturn. New37,98 frame28fields includesexitStepLimit50.31hostmodel/statictestsPASS; NXCcompile/runtimepending. This extends observation, not authorization to traverse gray or a claim of successful/legallyvalidatedcorner/fullroute.

Latest37,97 run: reference reachedA0/C747,stationary0/0 confirmed,but exitlostline after5intervals (4bothblack,1right-only), ending49/49 reason11. Angularreference correction did NOT solve exittracking. No validatedcorner/fullroute. Obtain a short fixed-camera video of turn-to-stop to locate the loss relative to outgoingstrip/nextedge before another geometry/control change; do not keep guessing motor targets or enable both-gray driving.

**CURRENT37,97 correction:** read-only PE/PDB inspection identifies actual physics constants (width1.65, distance/count0.4*pi/360) and per-stepatan integration. The earlier720count pivot reference was near87.27degrees, not90. Target is now743motorcounts (theoretical742.5roundedup), samepower15,stoppedA,240samplecap, allsensor/exitguards retained. Evidence and limitations are in `evidence/robosim-physics-2026-11-06.json`.29hostmodel/statictestsPASS, NXCcompile/runtimepending. This corrects angularreference, NOT proven solecause of failedexit or a guaranteeof90degree runtimepose/containment. User clarification does not establish anothercorner; do not add automaticsecondturns. Full route remains unresolved.

Latest37,96 runtime now exercised exit: pivotA0/C721,3stationarybothblack,state3;14exit intervals allbothblack then49/49, reason11 (NOT25-stepcap). User reports turn+advance but nosecondturn; program intentionally has onlyone turn. Determine whether loss is at a nextcorner or on outgoingstraight before changing navigation. Do not equate this one run with fullcorner legality/containment or automatically turn on everyloss.

**CURRENT37,96 geometry experiment:** new perspective suggests the center rotation leaves the robot position offset from the exit. No collision/exact offset proven. Replace center rotation with a forward right pivot (A braked, Cforward15). TargetC720 is derived from ideal yaw difference C-A, matching the provisional center calibration(-360,+360); it is NOT a measured90degree pivot. Separate240sample20ms cap; any A encoder movement or negative C stops. Keep initialbothblack, stationary3same-nonzero-contact confirmation,25-step bounded follower exit, and white/neitherblack stops. No reverse/search or blind forward motion on gray after pivot. Frame37,96 preserves28-field layout, with A0/C720 reference.27Python model/static tests pass; NXC compilation/runtime pending. Runtime must establish whether the arc actually positions the robot over outgoing black without departure. Earlier paragraphs below describe superseded center-turn tests.

Latest37,95 run also blocked exit: encoder deltas-364/+364 but final49/49, no stable contact and0exit intervals. The one-sided-contact relaxation did not solve this execution. Forward exit remains UNEXERCISED; do not enable it on both-gray or present stopped rotation as a complete corner. Explain expected test phases to the user; revisit placement/trajectory/termination rather than repeating identical trials or weakening contact validation again.

**Current revision superseding37,94:** user confirms changed perspective was camera only, not another run. Stable0/49 was blocked by the earlier both-black gate, although the follower supports one-sided contact. `robot_prueba_codo.nxc` now experimentally accepts three stationary samples of the SAME nonzero contact state (left-only/right-only/both), AFTER both encoder thresholds; state changes reset confirmation, never bypass encoder gating. Initial placement still requires both-black. Existing25-step bounded follower exit and all white/loss/encoder guards retained. New37,95 frame28fields appends confirmationState.26Python model/static checks pass; compilation/runtime pending. Stable contact is permission for a supervised bounded correction test, NOT proof of alignment, branch identity, legal corner or full route. Source/telemetry details atop `CONTINUIDAD.md`; older paragraphs below are history.

**Current next revision:** `robot_prueba_codo.nxc` now adds a short sensor-followed exit ONLY after encoder reference and three stationary both-black confirmations. At most25intervals20ms with original low-power follower, then stop and re-read sensors. White or neither-black stops without another turn/search/retry. All initial/approach/turn guards retained. New frame37,94 has27fields (schema atop `CONTINUIDAD.md`). Reason10 means exit cap, NOT successful route;11 means exit black loss.21 Python model/static checks pass, but compilation/runtime of this exit revision are PENDING. User-side run below refers to previous37,93 stop-only revision. Exact yaw, containment, legality, repeatability and full route still unvalidated. Following paragraphs are historical progression, not instructions to rerun earlier files.

Execution update: one combined run ended reason5 with A=-360/C=+360 and three stationary0/0 samples (approach index333, turn91samples). User image appears side-on after the right turn. The programmed stop is intentional, not timeout;75both-black samples during rotation did not finish early. No forward exit has been tested. Next consider only a short bounded sensor-followed exit after confirmed reference+black, without another turn or route decision. Containment, legality, repeatability and full route still require validation.

Exit-revision runtime update: latest37,94 ends reason6, phase2, A=-362/C=+362, stationary sensors0/49, stable0, exitSamples0. Thus compile/runtime observed but the gated forward exit was not exercised. Obtain final heading observation before modifying the strict both-black requirement; one-sensor black is normal for following but does not alone prove correct branch/heading. Previous single0/0 corner pass is not evidence of repeatable alignment.

Current local experiment: stopped-track right pivots failed to reacquire black within both 60 and 90 samples. Center-turn diagnostics reacquired both-black prematurely, without outgoing alignment in the user's image; both-black alone is not a valid 90-degree completion rule. Entry history showed simultaneous loss, not an earlier one-sided cue. Forward encoder probe demonstrated increasing A/C rotation counts, but motor counts have not been calibrated to chassis yaw. Next run `robot_prueba_encoders_giro.nxc`: a silent 200 ms nominal center-turn pulse to verify reverse encoder sign/progression, not a 90-degree maneuver. Retain supervision and strict bounds; do not integrate a forward exit or full route yet. Detailed frames and execution status are in `CONTINUIDAD.md`.

Update: reverse encoder probe verified A=-30/C=+30 with user-observed robot-right rotation. Next diagnostic is `robot_calibracion_giro.nxc`, stopping at the first motor reaching 90 relative motor counts, with a separate 60-sample safety cap. This target is exploratory, NOT 90 chassis degrees. Observe final heading relative to the initial straight and inspect paired signed deltas/fresh opcodes before deriving a yaw reference. No corner-entry or forward-exit integration yet.

Current calibration revision supersedes those historical targets: 90-count and 180-count runs stopped by encoders at approximately93/94 and182 counts respectively, but images still show underturn relative to a chassis quarter turn. Next exploratory target is360 motor counts, power15 unchanged, separate120-sample20ms watchdog. New37,92 telemetry identifies the revision. No precise motor-to-yaw conversion established; restore the same initial alignment for each run, do not sum uncontrolled reruns. Sensor/encoder corner integration and route validation remain pending.

Latest360-target run stopped at A=-362/C=+362 after95samples; image appears approximately perpendicular to initial heading. Use360 only as a provisional quarter-turn reference for this configuration. Repeat from the restored initial alignment before any corner integration; exact yaw, containment, corner success and full route remain unvalidated.

Repeat completed: paired before/after images again show a visually near-perpendicular turn; second run stopped at A=-360/C=+360 after93samples. Two-run qualitative repeatability supports a provisional360-count reference, not an exact angle measurement. Next separate diagnostic should combine bounded corner approach, encoder-progress gating and sensor exit confirmation, stopping rather than continuing if confirmation is absent. No legal corner or full route validated yet.

1. Full branch coverage is now required by the user's clarification. Resolve treatment of the staggered upper junction and verify the provisional graph before selecting turn decisions.
2. Validate the exact route edge by edge and its counterclockwise departure from the marker.
3. Test one sensor-terminated corner maneuver, with bounded motion and no reverse search.
4. Add intersection entry/exit confirmation and route-index checks; do not classify every both-black sample as a junction.
5. Add marker transition confirmation, route-progress gating, three crossing events for two laps, and final stop.
6. Validate two complete laps repeatedly before increasing power.

No full lap, legal corner maneuver, intersection decision, marker event, competition time or speed optimum has been demonstrated yet. Sound output works according to the user's test; tracking diagnostics are intentionally silent because repeated tones caused discomfort.
