

| **Reference dev. document** | [End of road landmark](https://tomtom.atlassian.net/wiki/spaces/~khandus/pages/213189056/End+of+road+landmark) |
|---|---|
| **Design** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) [Vadym Khandus](https://tomtom.atlassian.net/wiki/people/712020:2b00ecb1-a543-4410-818c-575056da8b84?ref=confluence) |
| **Visual Designer** | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence) |
| PO | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |



Table of Contents
=================

  

  


*   [Table of Contents](#Table-of-Contents)
*   [Introduction](#Introduction)
    *   ["end of the road" example](#end-of-the-road-example)
*   [Instruction design for the end of the road pointer](#Instruction-design-for-the-end-of-the-road-pointer)
*   [Break down of Use cases](#Break-down-of-Use-cases)
    *   [1\. Very Short road segments between manoeuvres](#1Very-Short-road-segments-between-manoeuvres)
    *   [2\. Parking lots, Pedestrian areas, Service Areas](#2-Parking-lots-Pedestrian-areas-Service-Areas)
*   [3\. Road splits before T-Junction](#3-Road-splits-before-T-Junction)
*   [4\. When main road turns](#4-When-main-road-turns)
    *   [5\. At complex intersections](#5-At-complex-intersections)
    *   [6\. At Exit ramps](#6-At-Exit-ramps)
*   [Short Summary of rules for filtering out "at the end of the road" pointer](#Short-Summary-of-rules-for-filtering-out-at-the-end-of-the-road-pointer)

  

**Introduction**
================

_**End of the road**_ refers to a _T-Junction_ type of intersection. When next manoeuvre (it could only be turn left/right) is placed at such location it is helpful to inform the driver about this _pointer_. Instead of tracking exact distance till the manoeuvre, driver can just drive till the road ends - this effectively reduces cognitive load for the driver and makes manoeuvre detection more reliable. The challenge lies in the detection of this _pointer_. While it should be used at _T-junctions_ and those are easy to detect, not all T-junctions should be applied. On this page we will break down use cases when _**end of the road**_ pointer should be used.  
  
NOTE: term _**Landmark**_ and _**Pointer**_ are used interchangeably here. They refer to the same object, but _**Landmark**_ refers to the object itself on the road in real world, while _**Pointer**_ is UI element (and audio component) which is pointing to it.

**"end of the road" example**
-----------------------------

| **Instruction** | **At the end of the road**, turn right |
|---|---|
| **Description** | This instruction is given when at a T junction |
| **Location** | 52°31'50\.3"N 13°31'00\.8"E |
| **Road Geometry** | ![](images/157711686.png) |
| **Visual Instruction** | ![](images/157711053.png) |
| **Audio Instruction** | **at the end of the road** turn right onto *street name* |

  

Instruction design for the end of the road pointer
==================================================

When _**end of the road**_ pointer is applied following deviations from the standard instruction design logic should be made:

1.  Instruction arrow should use special **T-junction arrow (1)**
2.  Pointer _end of the road_ should be only announced by Audio at **_main instruction phase_** (not _Early_).
3.  _**Distance announcement**_ at main instruction phase should be omitted.

  

| Visual Instruction \- NIP | Audio Instruction                                                                                                            |
|---|------------------------------------------------------------------------------------------------------------------------------|
| ![](images/157711053.png) | Main instruction phase:<br/>**at the end of the road** turn left onto *street name*  <br/><br/>Other instruction phases:<br/>**As normal** |

  

  

**Break down of Use cases**
===========================

Applying end of the road at every T-junction is not reasonable. We will look at the range of use cases where it is not desired. As a result we will come up with the rules for applying end of the road pointer. Here are some scenarios that don't require an end of the road pointer:  
  

1.  Very short road segments between two manoeuvres.
2.  Inside or at entering/exiting Parking lots, pedestrian areas, service areas.
3.  When road splits before the T-Junction.
4.  When Main road turns at a T-Junction.
5.  Generally at complex intersections where more roads are involved. Also when joining dual carriage road falls here.
6.  At exit ramps if they end with T-junction.
7.  At Roundabout entries
8.  At entries to Ferries or Car trains.

Lets look at each of them with examples.

  

  

1. Very Short road segments between manoeuvres
----------------------------------------------

Very short road segments don't require the end of the road because they aren't perceived as a significant roads by the drivers. They are seen as a connecting links between more significant road segments. **Distance of 100m or less** between last manoeuvre and T-Junction should not be considered for the end of the road pointer. Examples below illustrate this scenario:

| **Example 1** | **Example 2** | **Example 3** |
|---|---|---|
| ![](images/157711069.png) | ![](images/157711070.png) | ![](images/157711071.png) |

  

**RULE#1**  
If distance between last manoeuvre an T-Junction is **less then 100m**, end of the road pointer should not be used.

  
NOTE: More example of this and other scenarios as well as technical description of rules can be found at development documentation here: [End of road landmark](https://tomtom.atlassian.net/wiki/spaces/~khandus/pages/213189056/End+of+road+landmark)

  

  

2\. Parking lots, Pedestrian areas, Service Areas
-------------------------------------------------

Those specific environments don't really have roads clearly defined and usually consist of grid of very short undefined road segments or even no roads at all. End of the road pointer has no logical sense in such situations. Examples bellow illustrate this scenario:

| **Example 1** | **Example 2**                           | **Example 3** |
|---|-----------------------------------------|---|
| ![](images/157711074.png) | ![](images/157711075.png) | ![](images/157711083.png) |

  

**RULE #2**

The "End of road" landmark is not used if T-Junction manoeuvre is located in the following areas:

*   Is a part of a square. A square is a paved area where a car can travel but there are no legally defined traffic paths.
*   Is an entry, a part, or an exit of a service facility like motorway rest area, parking facility or golf course.
*   Is a part of pedestrian zone.
*   Is a pedestrian road.

  

NOTE: More example of this and other scenarios as well as technical description of rules can be found at development documentation here: [End of road landmark](https://tomtom.atlassian.net/wiki/spaces/~khandus/pages/213189056/End+of+road+landmark)

  

  

3\. Road splits before T-Junction
=================================

There are when the road splits before the actual T-junction. This is usually done to separate physical traffic streams from different directions. Such a road split is seen by drivers as a disturbing event and makes harder to detect where the actual road ends. To mitigate such confusion, we should not use the end of the road pointer in such scenarios.

| **Example 1** | **Example 2** |
|---|---|
| ![](images/157711079.png) | ![](images/157711080.png) |

  

**RULE #3**

Do not use end of the road If T-junction has a **road split** before the actual manoeuvre, or roads split an sharper angle.

  

  

4\. When main road turns
========================

When the current road (identified by road name) continues after the turn, we cannot say _**at the end of the road**_ because, technically, road doesn't end there. 

  

| Example 1 | Example 1 | Example 1 |
|---|---|---|
| ![](images/157711084.png) | ![](images/157711085.png) | ![](images/157711086.png) |

  

**RULE #4**

When the road before the intersection continues after the turn (has the same non-empty name after the intersection), we do not use end of the road pointer.

  

  

  

5\. At complex intersections
----------------------------

Any type of complexity found at T-junction: additional roads outcomes, non straight angles, proximity of another intersection, joining multi-lane or dual-carriage road... at all those scenarios end of the road should not be used because detection of the road end might not be possible or open for interpretations.

| Example 1 | Example 2 | Example 3 |
|---|---|---|
| ![](images/157711088.png) | ![](images/157711089.png) | ![](images/157711090.png) |

  

**RULE #5**

Do not use end of the road at complex scenarios when T-Junction topology is complicated by additional factors:

Additional T-intersection road outcomes at intersection or very close to it.

Joining big multi-lane or dual carriage road.

Geometry of T-intersection is not straight - any angle of the intersection deviates from 90° by more than 20°.

  

  

6\. At Exit ramps
-----------------

At exit ramps that are coming out of Motorways (or lower road class below Motorways) that utilise exit ramps. If exit ramp end up with T-junction, at this point at the end of the road should not be used.

| Example\-1 | Example\-2 | Example\-3 |
|---|---|---|
| ![](images/157711292.png) |  |  |

  

  

Short Summary of rules for filtering out "at the end of the road" pointer
=========================================================================

Following set of rules define conditions for **excluding** "at the end of the road" pointer:

| ID | Rule statement |  |
|---|---|---|
| 1 | If distance between last manoeuvre an T\-Junction is **less then 100m.** | ![](images/157711071.png) |
| 2 | If T\-Junction manoeuvre is located in the following areas:<br/><br/>* **Is a part of a square.** A square is a paved area where a car can travel but there are no legally defined traffic paths.<br/>* Is an entry, a part, or an exit of a **service facility** like motorway rest area, parking facility or golf course.<br/>* Is a part of **pedestrian zone**.<br/>* Is a **pedestrian road**. | ![](images/157711083.png) |
| 3 | If T\-junction has a **road split** before the actual manoeuvre, or roads split an sharper angle. | ![](images/157711080.png) |
| 4 | When **main road continues** after the turn (identical road ID). | ![](images/157711084.png) |
| 5 | If T\-Junction is **complicated** by additional factors:<br/><br/>* Additional T\-intersection road outcomes at intersection or very close to it.<br/>* Joining big multi\-lane or dual carriage road.<br/>* Geometry of T\-intersection is not straight. | ![](images/157711088.png) |
| 6 | If T\-junction entry is a ramp coming out of motorway (or even lower road class) exit. | ![](images/157711292.png) |
| 7 | At Roundabout entries |  |
| 8 | At entries to Car trains or Ferries. |  |

  

  

  

* * *

END OF THE DOCUMENT