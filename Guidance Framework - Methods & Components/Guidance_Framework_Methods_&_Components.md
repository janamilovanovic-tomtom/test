| **Interaction Designer** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) |
|---|---|
| **PM** | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |

NIE Framework
=============

Instruction engine is build on foundation of components, methods and map data. Components include visual and audio based interfaces. Methods include design patterns that control those components. There are following methods and components defined in NIE:  

[Instruction architecture](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680070/Instruction+architecture)

[Next Instruction Panel - NIP](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157679965/Next+Instruction+Panel+-+NIP)

[Simple Lane Guidance - SLG](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157718677/Simple+Lane+Guidance+-+SLG)

[Lane Level Guidance (LLG/LLN)](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680334/Lane+Level+Guidance+LLG+LLN)

[Audio Instructions](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680007/Audio+Instructions)

[Instruction Triggering Logic](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157679961/Instruction+Triggering+Logic)

[Distance Formatting](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680264/Distance+Formatting)

[Directional Information (Road names, Road numbers)](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157686877/Directional+Information+-+Road+names+Road+numbers+Towards)

[Road Signposts](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157702310/Road+Signposts)

[Natural Continuation](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680361/Natural+Continuation)

[Consecutive manoeuvres (Chain Instructions)](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680675/Consecutive+manoeuvres+Chain+Instructions)

[Optical Driving Instruction (OFA)](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157695332/Optical+Driving+Instruction+OFA)

[Manoeuvre path optimisation](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680435/Manoeuvre+path+optimisation)

[Audio management](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157680448/Audio+management)

[Landmarks](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157686285/Landmarks)

Terminology used in this document
=================================

This page contains the definitions of some terms used in motorway guidance. The purpose is to bring them to alignment with the developers, the UX, and the product.

**Intersection** - is a point at which two or more roads cross or meet. From the developer's point of view, it's an NDS junction that has at least three outgoing arcs. Intersections are T-intersections, Y-intersections, forks, N-way intersections, and so on...

**Road situation** - is a route stretch at the junction where the instruction engine intentionally produces or suppresses the instruction. It's a pattern that consists of a set of rules. If rules are satisfied, then the road situation is detected.  Road situations may have the same names as intersections where they appear (e.g. bifurcation).

Important! It's possible to have different road situations at the same intersections depending on the route stretch.  
Let's analyze this intersection on the motorway as an example:  
[https://www.google.com/maps/place/51%C2%B014'02.3%22N+6%C2%B042'30.3%22E/@51.2338295,6.7084049,193m/data=!3m1!1e3!4m4!3m3!8m2!3d51.2339843!4d6.7084164?entry=ttu](https://www.google.com/maps/place/51%C2%B014)

This intersection type is a bifurcation since the road splits without interrupting the traffic flow.  
If the route goes through the right branch - then it's an exit road situation since it leads from a motorway to a non-motorway road:  
[https://www.google.com/maps/dir/51.2334091,6.7115605/51.2361533,6.7032187/@51.2346495,6.7048156,725m/data=!3m1!1e3!4m2!4m1!3e0?entry=ttu](https://www.google.com/maps/dir/51.2334091,6.7115605/51.2361533,6.7032187/@51.2346495,6.7048156,725m/data=!3m1!1e3!4m2!4m1!3e0?entry=ttu)

If the route continues straight - it's a natural continuation situation since the driver does not need any instruction to pass through this intersection:  
[https://www.google.com/maps/dir/51.2334091,6.7115605/51.2345804,6.7052171/@51.2338614,6.7071022,363m/data=!3m1!1e3!4m2!4m1!3e0?entry=ttu](https://www.google.com/maps/dir/51.2334091,6.7115605/51.2345804,6.7052171/@51.2338614,6.7071022,363m/data=!3m1!1e3!4m2!4m1!3e0?entry=ttu)

This way, it's possible to have a natural continuation road situation at the bifurcation intersection type. 

**Motorway** - is a road whose corresponding arc has either the IsMotorway flag set to true or the IsControlledAccess flag set to true and a specified minimum speed limit of 80 km/h.

**Fork** - is an intersection type where the road splits without interrupting the traffic flow.

**Bifurcation (intersection type)** - is a fork with two outgoing roads. 

**Bifurcation (road situation)** - is a road situation that happens on bifurcations (intersection type) only and always requires a fork(left, right) instruction to take one of the two possible options.

**Trifurcation (intersection type)**  - is a fork with three outgoing roads.

**Trifurcation (road situation)** \- is a road situation that happens on trifurcations (intersection type) only and always requires fork(left, middle, right) instruction to take one of the three possible options.

**Highway** **Switch** - is a road situation that happens on motorways and requires a special switch highway instruction to leave the current motorway (via exit or fork) in order to take another one.

**Exit** - is a road situation which happens at forks and requires special exit instruction to leave the current motorway.

**Natural** **Continuation** - is a group of road situations when the driver does not need any instruction to pass through the intersection and stay on the route.