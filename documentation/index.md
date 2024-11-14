
| **Interaction Designer** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence)                                                                                                                                   |
|--|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Visual Designer** | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence)                                                                                                                                             |
| **PM** | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence)<br>[Mohammad Babamahmoudi](https://tomtom.atlassian.net/wiki/people/712020:710d380e-571a-4770-84e8-d3c8d129556f?ref=confluence) |
| **ENG OWNER** | [Michał Słonina](https://tomtom.atlassian.net/wiki/people/70121:30dcc9c2-9716-4606-81a9-709ec084944b?ref=confluence)                                                                                                                                  |
|  | UX review ticket [![](https://tomtom.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium)NAV\-151489](https://tomtom.atlassian.net/browse/NAV-151489)                                                              |

The start of the guidance session is accomplished by Departure instruction. The instruction serves two goals: first - indicating to the driver the start of the guidance session, and second - providing a direction of initial movement. If the navigation system knows the initial car heading, the departure instruction could be more informative. This design covers various scenarios and provides departure instructions for all of them. 

Initial Conditions
==================

Vehicle can be parked under following conditions:

1.  A car is parked on the road which is part of road network recognised by the map.

2.  A car is parked outside of road network recognised by the map -  at the parking lot or in the field

3.  GPS position is unknown. This could be caused by various reasons, such as car parked inside a garage.

4.  Car is already driving.


On top of this there are two possible states of car initial heading:

1.  Car's heading is unknown. This is bound to the technical capabilities of the vehicle.

2.  Car's heading is known.


Different combination of those factors dictate the following possible scenarios

Scenarios
=========

There are several possible scenarios involving different car initial position in relation to the first road segment which is recognised by the map. 

| **ID** | **Scenario** | **NIP** | **Manoeuvre arrow**                                                                                                                                                                                                                                                                                                                                                                                                | **Cardinal direction** | **Audio** | **Notes** |
|---|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|---|
| 1 | Car is parked inside road network recognised by the map. Current road is identified. | 1. Heading is known![](images/157717909.png)  2\. Heading is unknown![Dep_7.png](images/310750097.png) | Manoeuvre arrow is pointing to the direction of the route along the current road the route, if vehicle heading is known (1\)<br><br>    If vehicle heading is unknown, the arrow is not shown (2\), but after heading is gathered through the movement it should reflect real direction.<br><br>This heading should be updated in real time through the duration of the departure instruction, if changed during the movement. | Cardinal direction indicates direction aligned with the route on the current road.<br><br>N \- North<br>  S \- South<br>  E \- East <br> W \- West <br> SW \- South\-West <br> SE \- South\-East <br> NW \- North\-West <br> NE \- North\-East | ***Starting route. Head South\-West on Richard\-Strauss\-Straße*** | Distance is not used in this scenario |
| 2 | Car is parked outside of road network recognised by the map \- in the field, private parking etc. | 1. Heading is known![](images/157717910.png)  2\. Heading is unknown![Dep_6.png](images/311430460.png) | Manoeuvre arrow is pointing towards the point of intersection with the target road, if vehicle heading is known (1\).<br><br>If vehicle heading is unknown, the arrow is not shown (2\), but after heading is gathered through the movement it should reflect real direction. <br><br>   This heading should be updated in real time through the duration of the departure instruction, if changed during the movement.            | Cardinal direction indicates direction towards the point of intersection of the current track with the recognised by the map road.<br><br>This value should be updated in real time, if changed | ***Head South\-West towards Richard\-Strauss\-Straße*** | In order to start guidance vehicle must first be brought to the closest road through the field with the help of off\-road guidance. Distance shown is distance till the intersection with the target road point \- the point of the shortest path to the road.<br><br>At the moment of reaching this point the the instruction should be replaced with the appropriate turn instruction (if it can be gathered) or replaced with scenario \#1 instruction (if it cant).<br><br>NOTE: exact logic when it should happen TBD on engineering side. |
| 3 | Car is parked in underground garage or GPS position is unknown for whatever reason | ![](images/157717932.png) | Indicates the absence of GPS signal.                                                                                                                                                                                                                                                                                                                                                                               |  | ***~~OLD: No GPS signal. Drive outside of garage to start guidance.~~***   <br><br> ***NEW: No GPS signal. Drive the car to an open area.*** | IMPORTANT: This instruction should only be announced **after sufficient time is passed** to detect the lack of GPS connection reliably. |
| 4 | Car is not parked but in motion and route is being calculated during driving. | ![](images/273188802.png) | Manoeuvre arrow is pointing up \- in the direction of driving                                                                                                                                                                                                                                                                                                                                                      | \-\- | ***Starting route. Follow the A one hundred*** | This instruction stays on as long as needed for the system to calculate the next instruction, but preserving minimal duration (to avoid flickering) of 3 sec.  <br><br>  This instruction is not really needed by UX, but it exists to cover slow route calculation process, as real instruction cannot be displayed.<br><br>If car is in motion but offroad \- scenario \#2 is used. |

Departure instruction duration.
===============================

Any standard instruction refers to the point on the road - _**manoeuvre point**_. After passing this manoeuvre point, the instruction is not relevant anymore and is replaced by the next instruction. However, the departure instruction is different in this regard. It doesn't have manoeuvre point as such and therefore it must be specified till when the instruction remains active and when it gets replaced by the next instruction. As a general rule, the departure instruction should remain active until the point when next instruction becomes possible. Lets clarify this logic per use case we described above:

| **ID** | **Scenario** | **Duration of instruction** |
|---|---|---|
| 1 | Car is parked inside road network recognised by the map. Current road is identified. | As vehicle starts moving, the heading direction is gathered. Heading direction will be reflected in manoeuvre arrow in the NIP and adjusted to reflect real heading.  After gathering the heading, **3 sec duration** of the departure instruction must be preserved. After that the departure instruction is replaced by the next instruction on the route.  EXCEPTION: If next instruction is very close to the initial car position, there might be not enough time to show departure instruction for 3sec. In this case the departure instruction must be replaced by the next instructions at the point of 30m before the next instruction. |
| 2 | Car is parked outside of road network recognised by the map \- in the field, private parking etc. | As vehicle starts moving, the heading direction is gathered. Heading direction will be reflected in manoeuvre arrow in the NIP and adjusted to reflect real heading. The departure instruction is ***active till the point of intersection*** with the target road. After that it is replaced by the next instruction. |
| 3 | Car is parked in underground garage or GPS position is unknown for whatever reason | Departure instruction remains active till the GPS position is gathered and then it follows use cases \#1 or 2\. |

NOTE: Audio instruction for departure is only announced once and not repeated.

Strings
=======

| **ID** | **Proposed String** | **Description** | **Reviewed String** |
|---|---|---|---|
| 1 | ***Starting route. Head (Cardinal Direction) on (Road Name/Number)*** | Specifies direction of movement on specific road. |  |
| 2 | ***Head (Cardinal direction) towards (Road Name/Number)*** | Guides vehicle toward specific road when car is parked in the open field, and indicates direction of movement |  |
| 3 | ***No GPS signal. Drive outside of garage to start guidance.*** | explains the reason, why guidance cannot be started. GPS signal is obscured by something. |  |
|  | ***Starting route. Follow the A one hundred*** |  |  |
| 4 | ***N*** | Cardinal direction NORTH |  |
| 5 | ***S*** | Cardinal direction SOUTH |  |
| 6 | ***E*** | Cardinal direction EAST |  |
| 7 | ***W*** | Cardinal direction WEST |  |
| 8 | ***NE*** | Cardinal direction NORTH\-EAST |  |
| 9 | ***NW*** | Cardinal direction NORTH\-WEST |  |
| 10 | ***SE*** | Cardinal direction SOUTH\-EAST |  |
| 11 | ***SW*** | Cardinal direction SOUTH\-WEST |  |

* * *
[test](./test.md)
END OF DOCUMENT
===============