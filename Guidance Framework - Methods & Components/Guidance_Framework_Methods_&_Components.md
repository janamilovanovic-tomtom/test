| **Interaction Designer** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) |
|---|---|
| **PM** | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |

NIE Framework
=============

Instruction engine is build on foundation of components, methods and map data. Components include visual and audio based interfaces. Methods include design patterns that control those components. There are following methods and components defined in NIE:  

[Instruction architecture](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Instruction%20arhitecture/Instruction_architecture.md)

[Next Instruction Panel - NIP](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Next%20Instruction%20panel%20-%20NIP/Next_Instruction_Panel.md)

[Simple Lane Guidance - SLG](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Simple%20Lane%20Guidance%20-%20SLG/Simple_Lane_Guidance.md)

[Lane Level Guidance (LLG/LLN)](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Lane%20Level%20Guidance%20(LLG%2CLLN)/Lane_Level_Guidance(LLG_LLN).md)

[Audio Instructions](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Audio%20Instructions/Audio_Instructions.md)

[Instruction Triggering Logic](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Instruction%20Triggering%20Logic/Instruction_Triggering_Logic.md)

[Distance Formatting](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Distance%20Fromatting/Distance_Formatting.md)

[Directional Information (Road names, Road numbers)](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Directional%20Information%20-%20Road%20names%2C%20Road%20numbers%2C%20Towards%20/Directional_Information-Road-names_Road-numbers_Towards.md)

[Road Signposts](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Road%20Signposts/Road_Signposts.md)

[Natural Continuation](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Natural%20Continuation%20/Natural_Continuation.md)

[Consecutive manoeuvres (Chain Instructions)](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Consecutive%20manoeuvres%20(Chain%20Instructions)/Consecutive_manoeuvres_(Chain_Instructions).md)

[Optical Driving Instruction (OFA)](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Optical%20Driving%20Instruction%20(OFA)/Optical_Driving_Instruction(OFA).md)

[Manoeuvre path optimisation](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Manoeuvre%20path%20optimisation/Manoeuvre_path_optimisation.md)

[Audio management](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Audio%20management/Audio_management.md)

[Landmarks](./../Guidance%20Framework%20-%20Methods%20%26%20Components/Landmarks/Landmarks.md)

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