| **Status**      | <mark>MOVED TO REVIEW</mark>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **IXD**         | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **VD**          | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **ENG. OWNER**  | [Agnieszka Sobczyk](https://tomtom.atlassian.net/wiki/people/712020:27737e77-b2fa-4ca4-9fbf-019cbab57789?ref=confluence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **PM**          | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **TICKET**      | [NAV-131044](https://jira.tomtomgroup.com/browse/NAV-131044) - [PRIO 2] Roundabout - critical tech debt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Reviewed by** | [NAV-151480](https://jira.tomtomgroup.com/browse/NAV-151480) - [REVIEW] Generic Roundabout Instruction Done<br>* [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) <br>* [Alex Levin](https://tomtom.atlassian.net/wiki/people/63e4cab2614cb4ba5303b527?ref=confluence) <br>* [Agnieszka Sobczyk](https://tomtom.atlassian.net/wiki/people/712020:27737e77-b2fa-4ca4-9fbf-019cbab57789?ref=confluence) <br>* [Robert Wu](https://tomtom.atlassian.net/wiki/people/5e79ca6959b34d0c3c21cee3?ref=confluence) <br>* [Maciej Tomasz Piotrowski](https://tomtom.atlassian.net/wiki/people/712020:9a48e539-50aa-491e-acff-bfff512d987e?ref=confluence) <br>* [Petru-Nicu Dumitrache](https://tomtom.atlassian.net/wiki/people/712020:3b938b6d-571d-4862-bde1-3e44b7cab69a?ref=confluence) |

Introduction
============

| **Issue**                                                                                                            | **Possible solution**                         |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Turn directions (turn right/ left) often reported as wrong/misleading. Turns only work in narrow range scenarios     | Remove turn directions at roundabouts         |
| Turn directions for big roundabouts are useless, as driver loses original perspective while driving along the curve. | Remove turn directions at roundabouts         |
| Lane guidance is misleading on a big roundabouts                                                                     | Provide SLG design for multi-lane roundabouts |
| Exit Roundabout instruction is not clear.                                                                            | Clarify exit instruction                      |

Roundabouts are complicated intersection type that require special instruction for handling. Typically driving through roundabouts poses following challenges: It is not easy to identify correct exit, especially if there are many and directions are not straight. The challenge is amplified by the fact that decision should be made very fast. To address this we must prepare the driver upfront and provide him necessary information that could be applied instantly. Typical method of guidance trough roundabouts is mentioning the **number of exit** (counted from the entry point) that has to be taken. It is relatively easy to count exits for the driver, however this could be complicated if exits are mixed up with entries. It is not always easy to distinguish entries from exits especially when it needs to be done very fast during counting.  

Roundabout Instruction Architecture
===================================

Unlike, general instruction template, roundabout manoeuvre doesn't take place at one point but has a stretch of the road with two key points: entry and exit. To reflect this, the instruction has different architecture and consists of two parts:

**Entry Roundabout instruction** \- Given for the entry as a manoeuvre point. Instructs how to perform whole Roundabout manoeuvre from entry to exit.   
**Exit roundabout instruction** \- Given for the exit as manoeuvre point. Only instructs how to perform the exit roundabout manoeuvre, while being already on the roundabout.

![5.svg](/Users/bogdan.arsic/Documents/5.svg)

**Roundabout Instruction schematic diagram.**  
Technically, Roundabout manoeuvre is a sequence of two independent manoeuvres: **Roundabout entry** and **Roundabout Exit**  reference point for the entry is entry point and for the exit - exit. Those two manoeuvres have associated with them instructions which are depicted in corresponding Blue and Green colors on the diagram above.

Next Instruction panel
----------------------

Design of Next instruction panel and Audio announcement depends on lane configuration at the roundabout, therefore we will be covering **single-lane** roundabouts and **multi-lane** separately.

**Single lane roundabout instruction design**

| **Phase** | **Visual**                                                                                                                                | **Audio**                                                              | **Notes**                                                                                                                                                |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Early     | <img title="" src="file:///Users/bogdan.arsic/Documents/d63357b0-6961-468a-acf2-5f23f0291fce.png" alt="" width="442" data-align="inline"> | _**In one kilometer, at the Roundabout, take the 3rd exit ...**_       |                                                                                                                                                          |
| Main      | <img title="" src="file:///Users/bogdan.arsic/Documents/2.png" alt="2.png" width="274">                                                   | _**In four hundred meters, at the Roundabout, take the 3rd exit ...**_ |                                                                                                                                                          |
| Conf3     | <img title="" src="file:///Users/bogdan.arsic/Documents/3.png" alt="3.png" width="284">                                                   | _**take the 3rd exit**_                                                | At the point of entry the distance counter gets down to 0 and then after entering roundabout, immediately restarts with the distance til the exit point. |
| Exit      | <img title="" src="file:///Users/bogdan.arsic/Documents/4.png" alt="4.png" width="365">                                                   | _**exit the roundabout**_                                              | Exit instructions don't mention the number of exit since it is not applicable for the current position of the vehicle                                    |

**Multi-lane roundabout instruction design**



| **Phase**    | **Visual**                                      | **Audio**                                                                                            | **Notes**                                                                                                                                                                        |
| ------------ | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Early        | ![8.png](/Users/bogdan.arsic/Documents/8.png)   | _**In one kilometer, at the Roundabout, take the 3rd exit ...**_                                     |                                                                                                                                                                                  |
| Main         | ![10.png](/Users/bogdan.arsic/Documents/10.png) | _**In four hundred meters, at the Roundabout, stay in the left two lanes to take the 3rd exit ...**_ | New design of Unified SLG replaces manoeuvre arrow with SLG at main, Confirmation instruction phases. SLG here depicts lane configuration at the entrance to the roundabout.     |
| Confirmation | ![10.png](/Users/bogdan.arsic/Documents/10.png) | _**take the 3rd exit**_                                                                              | At the point of entry the distance counter gets down to 0 and then after entering roundabout, immediately restarts with the distance til the exit point.                         |
| Exit8        | ![11.png](/Users/bogdan.arsic/Documents/11.png) | _**exit the roundabout**_                                                                            | New design of Unified SLG replaces manoeuvre arrow with SLG at main, Confirmation instruction phases. SLG here depicts lane configuration at the exit point from the roundabout. |

### SLG logic for multi-lane roundabouts

Multi-lane roundabouts lane recommendation should be gathered from lane connectivity data. Typically, the rightmost lane is connected with the first exit. Second and third to the second exit. Leftmost lane to the 3rd and further exits. This principle, however, could be broken and lane connectivity In those cases the only way to know which lane should be recommended is to read lane markings which are usually drawn on the surface of the road. Generally, when lane connectivity is in place it should be used for gathering recommended lane. And only when all lanes are connected to the target exit equally, we should apply generic lane logic.

**Generic Lane Logic**

| **Exit number** | **Recommended lane**          | **Notes**                        |
| --------------- | ----------------------------- | -------------------------------- |
| 1               | Rightmost                     |                                  |
| 2               | 2nd from the right            |                                  |
| 3               | 2nd or/and 3rd from the right | 3rd - if third lane is available |
| 4 - max         | Leftmost                      |                                  |

NOTE: this table is defined for standard driving road side (not UK, Japan). For those regions the side should be reversed.

**Example**

Following example illustrates lane guidance at multi-lane roundabout with 2 exits. Roundabout itself consists of 2 lanes that are not marked on the circle but assumed to be there because ther are 2 lanes at the entrance of the roundabout.

![15.png](/Users/bogdan.arsic/Documents/15.png)



**Instruction modelling for this scenario**

| **Exit No.** | **NIP**                                         | **Audio**                                            | **Notes**                                                                                                                                                                                                                       |
| ------------ | ----------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1            | ![20.svg](/Users/bogdan.arsic/Documents/20.svg) | Stay in the middle lane to take the first exit…      | Even though, it possible to change lanes while driving along the circle - it is not optimal. Therefore using our MPO (manoeuvre path optimisation) method we recommend the most optimal lane that doesn't require lane changes. |
| 2            | ![21.svg](/Users/bogdan.arsic/Documents/21.svg) | Stay in the left two lanes to take the second exit…. | Both left lanes are equally optimised for the second exit, therefore both are recommended                                                                                                                                       |

### Roundabout manoeuvre arrow

Visual Instruction represents Roundabout schematically.

| **First exit**                                  | **Third exit**                                  | **cross, second exit**                          | **take fifths exit**                            | **exit roundabout**                                                                       |
| ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------- |
| ![24.png](/Users/bogdan.arsic/Documents/24.png) | ![25.png](/Users/bogdan.arsic/Documents/25.png) | ![26.png](/Users/bogdan.arsic/Documents/26.png) | ![27.png](/Users/bogdan.arsic/Documents/27.png) | <img src="file:///Users/bogdan.arsic/Documents/28.png" title="" alt="28.png" width="187"> |

When Exit instruction is omitted?
---------------------------------

There are use cases when exit instruction doesn't have place. Those happen usually due to close proximity of the entry and exit points. They are so close to each other that can be considered as one.



Roundabouts types
=================

Different configurations of roundabouts require different instruction compositions, therefore, we define separately following categories of roundabouts:

1. **Small / Straight roundabouts** \- the most trivial traffic figures that require minimal instruction for the manoeuvre.

2. **Single lane roundabouts (excluding #1) -** the most common traffic figures that require moderate instruction for the manoeuvre.

3. **Multi-lane roundabouts -** the most complex traffic figures that require the most elaborative instruction for the manoeuvre.

1\. Small / straight roundabouts
--------------------------------

Small, straight (both conditions must be present to be classified as such) roundabout are trivial intersections and when crossing, don't require too elaborative instruction. Generic roundabout instruction is long and might be annoying especially if repeated in serial scenarios which are common for small roundabouts, therefore we use more natural format for such scenarios. We rely on _**cross the roundabout**_ when going straight and _**go around the roundabout**_ when going back. Street names announcements are also minimised at those traffic figures.

**Small, Straight Roundabouts detection algorithms** <mark>TO BE MOVED TO GITHUB</mark>

This sections should be moved to the GitHub and managed by **engineering owner**.

Small roundabouts must have less than 30m radius. Angle deviations from 90° should not exceed +-5° (both sides)

| **ID** | **Road Network**                                    | **Description**                                                                                                                         |
| ------ | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| #1     | ![21.png](/Users/bogdan.arsic/Documents/21.png)     | This is a small (supposedly less than 30m radius) roundabout with clear straight exits.                                                 |
| #2     | ![123.png](/Users/bogdan.arsic/Documents/123.png)   | Two successive roundabout: one of them is small and another is big. For small one we should use short version and for big one - normal. |
| #3     | ![1234.png](/Users/bogdan.arsic/Documents/1234.png) | This roundabout while small, **is not straight**, therefore id doesn't meet straight direction conditions.                              |



**Detection of straight direction.**

Straight direction for small roundabouts is identified from looking at the following attributes:

| **Attribute**               | **Value** | **Description**                                                                                                                                           |
| --------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multilane roundabouts       | Yes / No  | Multilane roundabouts are not qualified for having straight direction, as it is hard to keep sense of initial direction when travelling along big circle. |
| Amount of exits             | 2-8       | Only roundabouts  **with 2, 3 and 4 exits**  can be qualified for for having _Straight direction_.                                                        |
| deviation of crossing angle | \+\- 5°   | Only roundabouts with branches crossing at 90° or 180° angle can be qualified for for having _Straight direction_.                                        |

...