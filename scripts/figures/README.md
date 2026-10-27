# Figure generators

Python scripts that draw the course's SVG diagrams and SMIL animations. Each one
writes its SVG(s) into `scripts/figures/out/` (gitignored); nothing here writes into
`static/` directly.

## Running

```bash
cd scripts/figures
python3 m12tri.py              # one figure
for f in [a-z]*.py; do python3 "$f"; done   # everything (frames.py needs an argument)
python3 frames.py out/l2-triangle-tries.svg 0 2 4 6   # contact sheet of frames at those seconds -> out/frames.png (size read from the SVG)
```

Then copy the result to its place under `static/img/`. **If the file is already
deployed, give the new one a new name** and update the lesson's `src` — the browser
caches the old URL (CLAUDE.md §12).

## Shared modules

| File | What it is |
|---|---|
| `_paths.py` | `OUTDIR`, `REPO`, `ROBOT_SRC` (the `#pcXRP` robot symbol is lifted from `static/img/lesson-m2-09/park-turn-left-then-right.svg`) |
| `common.py` | grid helper `G`, `svg()` wrapper, shared `DEFS` and palette |
| `gridanim.py` | robot driving a grid path (Modules 3-5) |
| `floorrun.py`, `bounce.py`, `kpsim.py`, `sim.py` | floor/line simulations for Module 2 |
| `pathanim.py` | robot following an arbitrary path with timed captions; `E()` escapes text |
| `frames.py` | Playwright preview: renders an SVG at chosen times |

SMIL rules learned the hard way: the last `keyTimes` entry must be 1; anything visible
at t=0 needs an animate whose first keyTime is 0 with value 1; `<PlayFigure>` reads
`data-hold` (pause on the final pose) and `data-modes` (one button per timeline
segment) from the SVG root.

## Which script makes which file

"—" means the output is not used on the site (a draft or an alternative). Some
deployed copies carry an extra C2PA `<metadata>` block from delivery; otherwise
they match the generator byte for byte. **Known stale:** the deployed
`lesson-m2-09/sensor-ended-turn.svg` (680x590) was edited after
`m2_sensor_ended_turn.py` (680x560) — reconcile before regenerating it.

| Script | Output | Installed at |
|---|---|---|
| diffdrive.py | motors-curve-arrows.svg | — |
| diffdrive.py | motors-curve-drive.svg | /img/lesson-06/motors-curve-drive.svg |
| diffdrive.py | motors-pivot-arrows.svg | — |
| diffdrive.py | motors-pivot-drive.svg | /img/lesson-06/motors-pivot-drive.svg |
| diffdrive.py | motors-spin-arrows.svg | — |
| diffdrive.py | motors-spin-drive.svg | /img/lesson-06/motors-spin-drive.svg |
| diffdrive.py | motors-straight-arrows.svg | — |
| diffdrive.py | motors-straight-drive.svg | /img/lesson-06/motors-straight-drive.svg |
| b23.py, b24.py | bounce-run.svg | /img/lesson-m2-03/bounce-run.svg |
| b24.py | random-bounce-run.svg | /img/lesson-m2-04/random-bounce-run.svg |
| circles.py | arcade-circles.svg | /img/lesson-06/arcade-circles.svg |
| coords.py | naming-intersections.svg | /img/lesson-m4-01/naming-intersections.svg |
| coords.py, f41.py, f43.py, f44.py, fmap.py, ftrace.py, ftrace2.py, g51.py, g52.py, g53.py, g55.py, g56.py, g59.py, g6.py, grings.py, m31.py, m32.py, m33.py, m34a.py, m34b.py, m3_grid_figures.py, m43.py, m44.py, m49.py, manhattan.py, phone.py, square.py, tuples.py | grid.svg | — |
| dictpic.py | word-dictionary.svg | /img/lesson-m5-02/word-dictionary.svg |
| edge.py | drive-to-line.svg | /img/lesson-m2-02/drive-to-line.svg |
| em.py | earth-moon-mission.svg | /img/lesson-06/earth-moon-mission.svg |
| f41.py | coordinates.svg | /img/lesson-m4-01/coordinates-xy.svg |
| f43.py | path-list.svg | — |
| f44.py, m44.py | four-loops.svg | /img/lesson-m4-04/four-loops-xy.svg |
| f47.py | headings.svg | /img/lesson-m4-07/headings-xy.svg |
| f47.py | short-way.svg | — |
| fharness.py | test-harness.svg | — |
| first.py | first-drive.svg | /img/lesson-08/first-drive.svg |
| fmap.py | delivery-overview.svg | /img/lesson-m4-00/delivery-overview-xy.svg |
| fmap.py | delivery-run.svg | /img/lesson-m4-09/delivery-run-xy.svg |
| fmap.py | told-not-remembered.svg | /img/lesson-m4-05/told-not-remembered-xy.svg |
| fpipe.py | two-halves.svg | — |
| fraise.py, fraise2.py | raise.svg | — |
| fraise2.py | raise-spin.svg | — |
| fshort.py | turn-shortcut.svg | /img/lesson-m4-08/turn-shortcut-xy.svg |
| ftrace.py | drive-path-trace.svg | — |
| ftrace2.py | drive-path-loop.svg | /img/lesson-m4-08/drive-path-loop-xy.svg |
| g51.py | detour.svg | /img/lesson-m5-01/detour-xy.svg |
| g51.py | graph-3x3.svg | /img/lesson-m5-01/graph-3x3-xy.svg |
| g51.py | graph-blocked.svg | /img/lesson-m5-01/graph-blocked-xy.svg |
| g52.py | bounds-checks.svg | /img/lesson-m5-02/bounds-checks-xy.svg |
| g52.py | graph-dict.svg | /img/lesson-m5-02/graph-dict-xy.svg |
| g53.py | bfs-ripple.svg | /img/lesson-m5-03/bfs-ripple-xy.svg |
| g53.py | wall-problem.svg | /img/lesson-m5-03/wall-problem-xy.svg |
| g54.py | append-vs-assign.svg | — |
| g54.py | blocked-list.svg | — |
| g55.py | bfs-vs-dfs.svg | /img/lesson-m5-05/bfs-vs-dfs-xy.svg |
| g55.py | code-pencil.svg | — |
| g56.py | path-properties.svg | /img/lesson-m5-06/path-properties-xy.svg |
| g56.py | planner-slot.svg | — |
| g57.py | rangefinder-ahead.svg | /img/lesson-m5-07/rangefinder-ahead-xy.svg |
| g58.py | run1-run2.svg | /img/lesson-m5-08/run1-run2-xy.svg |
| g58.py | until-arrive.svg | — |
| g59.py | capstone-thread.svg | /img/lesson-m5-09/capstone-thread-xy.svg |
| g6.py | break-even.svg | /img/lesson-m6-01/break-even-xy.svg |
| g6.py | closest-vs-oldest.svg | /img/lesson-m6-03/closest-vs-oldest-xy.svg |
| g6.py | cost-grid.svg | /img/lesson-m6-03/cost-grid-xy.svg |
| g6.py | cost-to-seconds.svg | /img/lesson-m6-04/cost-to-seconds.svg |
| g6.py | floor-vs-graph.svg | /img/lesson-m6-01/floor-vs-graph-xy.svg |
| g6.py | path-cost.svg | /img/lesson-m6-02/path-cost.svg |
| g6.py | slow-road.svg | /img/lesson-m6-00/slow-road-xy.svg |
| g6.py | three-planners.svg | /img/lesson-m6-05/three-planners.svg |
| grings.py | bfs-rings.svg | /img/lesson-m5-03/bfs-rings-xy.svg |
| hill.py | effort-vs-speed-hill.svg | /img/lesson-06/effort-vs-speed-on-a-hill.svg |
| kpanim.py | kp-tuning.svg | /img/lesson-m2-05/kp-tuning.svg |
| m12.py | square-goal.svg | /img/lesson-02/square-goal.svg |
| m12steps.py | l2-step1.svg | /img/lesson-02/l2-step1.svg |
| m12steps.py | l2-step2.svg | /img/lesson-02/l2-step2.svg |
| m12steps.py | l2-step3.svg | /img/lesson-02/l2-step3.svg |
| m12tri.py | l2-triangle-tries.svg | /img/lesson-02/l2-triangle-tries.svg |
| m12tri.py | l2-triangle-closes.svg | /img/lesson-02/l2-triangle-closes.svg |
| m2_error_sign.py | error-sign.svg | — |
| m2_four_positions.py | four-positions.svg | — |
| m2_sensor_ended_turn.py | sensor-ended-turn.svg | — |
| m31.py | m3-reach-and-turn.svg | /img/lesson-m3-01/reach-and-turn.svg |
| m32.py | m3-drive-run.svg | /img/lesson-m3-02/drive-run.svg |
| m33.py | m3-l-and-plan.svg | /img/lesson-m3-03/l-and-plan.svg |
| m34a.py | m3-square-buildup.svg | /img/lesson-m3-04/square-buildup.svg |
| m34b.py | m3-extensions.svg | /img/lesson-m3-04/extensions.svg |
| m3_grid_figures.py | l-path.svg | /img/lesson-m3-03/l-path-xy.svg |
| m3_grid_figures.py | square-path.svg | /img/lesson-m3-04/square-path-xy.svg |
| m3_second_track.py | second-track.svg | — |
| m43.py | build-path.svg | /img/lesson-m4-03/build-path.svg |
| m44.py | four-loops-run.svg | /img/lesson-m4-04/four-loops-run.svg |
| m49.py | delivery-drive.svg | /img/lesson-m4-09/delivery-drive.svg |
| manhattan.py | manhattan-grid.svg | /img/lesson-m4-00/manhattan-grid.svg |
| mission.py | final-project-mission.svg | — |
| phone.py | phone-route.svg | /img/lesson-m5-01/phone-route.svg |
| square.py | square-run.svg | — |
| toolkit.py | toolkit-by-hand.svg | /img/lesson-m2-07/toolkit-by-hand.svg |
| tuples.py | tuple-on-grid.svg | /img/lesson-m4-02/tuple-on-grid.svg |
| m28track.py | track-to-cross.svg | /img/lesson-m2-08/track-to-cross.svg |
| m21slide.py | slide-across-tape.svg | /img/lesson-m2-01/slide-across-tape.svg |
| m110nest.py | nest-two-squares.svg | /img/lesson-10/nest-two-squares.svg |
| m15poly.py | polygon-calls.svg | /img/lesson-05/polygon-calls.svg |
| m17map.py | course-map.svg | /img/lesson-07/course-map.svg |
| m13copy.py | copy-paste-vs-function.svg | /img/lesson-03/copy-paste-vs-function.svg |
| fanout.py | fanout-bfs.svg | /img/lesson-m5-03/fanout-bfs.svg |
| fanout.py | fanout-bfs-vs-dijkstra.svg | /img/lesson-m6-03/fanout-bfs-vs-dijkstra.svg |
