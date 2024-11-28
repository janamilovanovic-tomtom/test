| **created by** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) |
|---|---|
| **PM** | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |
| **ENG. OWNER** | [Dennis Jakobsen](https://tomtom.atlassian.net/wiki/people/712020:c273d0e3-9a2a-456c-ad2f-6f56ca0e12b3?ref=confluence) → please define |

Lane Level Guidance Session
===========================

LLG is in fact a zoomed in view on the map that allows more precise lane guidance in real time. During LLG session Map vie is zoomed in enough to depict individual lanes. Vehicle precise position in regard to lanes is indicated (if provided). Recommended lanes are highlighted. 

![](images/157715690.png)

NOTE: Detailed design and visualisation methods of LLG are not covered in this document.

When LLG sessions are activated?
================================

LLG session are activated at certain conditions only when precise lane guidance might be required. It doesn't make sense to keep LLG permanently, as it limits the look ahead (due to a zoom level) and when LG is not necessary, doesn't provide any real value.  Therefore we need to define the use cases which activate LLG. There are following groups of use cases known at this point:

1.  **Manoeuvre at the intersection with multiple lanes**
    
2.  **Passing by intersections with multiple lanes (Interim exit scenario)**
    
3.  Lane-Level Traffic events
    
4.  Lane-level road closures
    

NOTE: At this point in time 23 May 2024 only first two are supported by the design, but in the near future other 2 use cases will be covered.

Lets take a look at both of these use cases.

Use case 1 - Manoeuvre at intersection with multiple lanes.
===========================================================

At any manoeuvre that involves selecting specific lanes, choosing the correct lane is crucial. As a preparation to the manoeuvre LG should start a bit earlier to give the driver time for understanding lane geometry. There are two possible methods for defining triggering entry/ext points for LLG sessions in regard to Manoeuvres:  Based on _**instructions triggering points**_ and based on _**road geometry** or **lane configuration change (LCC) points**_. The first method is more simple as it doesn't require any additional analysis since Instruction triggering points are readily available. Lets call **LLG session** starting point **LLG-S** and end point **LLG-E** for shortening.

LLG Session triggering based on instruction triggering points
-------------------------------------------------------------

Every instruction has triggering points (as described [here](../../Instruction%20Triggering%20Logic/Instruction_Triggering_Logic.md)) Triggering points are measured in relation to Manoeuvre point (or or MAN-S point). For Triggering LLG we use **Main instruction** triggering point.  As a result, the LLG session is activated at 400m - 1300m (depending on road class) distance from the manoeuvre according to Main triggering point definition. The disadvantage of this method - since triggering is not dependant on the lane geometry, it cannot guarantee that all lane configuration change points (LCC) will be embraced in LLG session, however given the significant stretch of the road, it is most likely is going to happen. 

| ![](images/157715694.png) |
|---|

NOTE: This example above illustrates simple scenario involving one manoeuvre at one intersection. Often we are dealing with serial intersections and manoeuvres and LLG session should cover those scenarios as well.

  

LLG triggering based on  LCC points
-----------------------------------

To mitigate the disadvantage of the first method, there is a more sophisticated approach - Triggering based on LCC points. This method instead of looking at the starting point of the manoeuvre, is looking backwards for LCC points. If they find those in the predefined threshold range, it will embrace those into LLG session. The search for LCC should be repeated max 3 times, each time restarting from the last LCC point. This way the algorithm scans the road for complexity before the manoeuvre and embrace those complex sections into LLG session and it helps driver navigating through multiple lane configurations. The algorithm is more involved however,  and probably makes sense to implement after the first one.

| ![](images/157715695.png) |
|---|

Use case 2 - Passing by Interim Exit
====================================

Passing by interim exit is identified as a major pain point by drivers, as normally, navigation systems ignore those scenarios. Usually happens on Motorways, but could also happen on any major road that is designed to have uninterrupted entities/exits via acceleration ramps. Interim exit is an exit that is leading off-route. Driver passes by those exit without taking them. Depending on the lane configuration of such exit it could pose the problem for the driver that is intended to stay on the main road. To illustrate it we need to analyse different types of such lane configurations:

Possible lane configurations of Exits
-------------------------------------

There are following lane configurations are available for exits. Lets take a look at each of them. Blue path indicated route lanes, while grey - off-route.

![](images/157717511.png)

**A - doesn't pose any problems** for drivers, generally, as exit lane appears just before the exit and in order to take it, driver must change lane. It is very unlikely in such situation that drivers will accidentally exit main road. In reality, though, the section of this new lane departure varies in length and if very long, this scenario **becomes scenario B**.

**B - is problematic**, as the exit lane is coming from existing right lane. It is common to drive in the rightmost lane in EU and this is prescribed by traffic rules. Therefore it is easy to take such exit accidentally, when not paying attention. This is confirmed by user research and various evaluations of the product.

**C - Same as B but more severe**, as chance of making mistake increases. This geometry is also could be **treated as a Fork**, and appropriate instruction issued, effectively eliminating the issue. 

**D - This special configuration** involves entry path and close exit from the same lane. Depending on the length of the common segment this scenario cold be more or less severe.

**E - Same as D but more severe**. This geometry is also could be **treated as a Fork**, and appropriate instruction issued, effectively eliminating the issue. 

NOTE: There could be more configurations of intersections which involve road splits that are not covered here. Those will be added lated upon discovery.

NOTE: Some of those scenarios would invoke a proper instruction, and in this case LLG session activates by the manoeuvre logic described above.

Triggering of LLS session at interim exit scenario
--------------------------------------------------

Given the various degrees of potential misguides in those scenarios, we should activate LLG session at all of those. For the reference point for activation we should use hypothetical manoeuvre point (manoeuvre that we are trying to avoid) and adding buffers to it from both sides. 

| **Upfront buffer** |**After buffer**|
|--------------------| --- |
| 400m               | 100m |

The diagram depicting interim exit scenario.

![](images/157717518.png)

MAN - is the point where manoeuvre that should be avoided, would take place.

\----------- END OF DOCUMENT -----------
========================================