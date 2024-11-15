| **IXD**        | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence)                                                                                                                                                                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VD**         | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence)                                                                                                                                                                                                   |
| **ENG. OWNER** | [User 57789](https://tomtom.atlassian.net/wiki/people/712020:27737e77-b2fa-4ca4-9fbf-019cbab57789?ref=confluence)                                                                                                                                                                                           |
| **PM**         | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence)                                                                                                                                                                                       |
| **TICKET**     | [NAV\-131044](https://tomtom.atlassian.net/browse/NAV-131044?src=confmacro) |

Introduction
============

This is a revision of the original design. As  a result of the evaluation of Roundabouts instructions we received the following feedback:

| **Issue**                                                                                                            | **Possible solution**                          |
| -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Turn directions (turn right/ left) often reported as wrong/misleading. Turns only work in narrow range scenarios     | Remove turn directions at roundabouts          |
| Turn directions for big roundabouts are useless, as driver loses original perspective while driving along the curve. | Remove turn directions at roundabouts          |
| Lane guidance is misleading on a big roundabouts                                                                     | Provide SLG design for multi\-lane roundabouts |
| Exit Roundabout instruction is not clear.                                                                            | Clarify exit instruction                       |

Roundabouts are complicated intersection type that require special instruction for handling. Typically driving through roundabouts poses following challenges: It is not easy to identify correct exit, especially if there are many and directions are not straight. The challenge is amplified by the fact that decision should be made very fast. To address this we must prepare the driver upfront and provide him necessary information that could be applied instantly. Typical method of guidance trough roundabouts is mentioning the **number of exit** (counted from the entry point) that has to be taken. It is relatively easy to count exits for the driver, however this could be complicated if exits are mixed up with entries. It is not always easy to distinguish entries from exits especially when it needs to be done very fast during counting.  

Roundabout Instruction Architecture
===================================

Unlike, general instruction template, roundabout manoeuvre doesn't take place at one point but has a stretch of the road with two key points: entry and exit. To reflect this, the instruction has different architecture and consists of two parts:

**Entry Roundabout instruction** - Given for the entry as a manoeuvre point. Instructs how to perform whole Roundabout manoeuvre from entry to exit.   
**Exit roundabout instruction** - Given for the exit as manoeuvre point. Only instructs how to perform the exit roundabout manoeuvre, while being already on the roundabout.

![Big Roundabouts Instruction.svg](images/306088039.svg)

**Roundabout Instruction schematic diagram.**  
Technically, Roundabout manoeuvre is a sequence of two independent manoeuvres: **Roundabout entry** and **Roundabout Exit**  reference point for the entry is entry point and for the exit - exit. Those two manoeuvres have associated with them instructions which are depicted in corresponding Blue and Green colors on the diagram above.

Next Instruction panel
----------------------

Design of Next instruction panel and Audio announcement depends on lane configuration at the roundabout, therefore we will be covering **single-lane** roundabouts and **multi-lane** separately.

**Single lane roundabout instruction design**

| **Phase** | **Visual**                   | **Audio**                                                              | **Notes**                                                                                                                                                |
| --------- | ---------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Early     | ![](images/157717722.png) | ***In one kilometer, at the Roundabout, take the 3rd exit ...***       |                                                                                                                                                          |
| Main      | ![](images/157717721.png) | ***In four hundred meters, at the Roundabout, take the 3rd exit ...*** |                                                                                                                                                          |
| Conf      | ![](images/157717719.png) | ***take the 3rd exit***                                                | At the point of entry the distance counter gets down to 0 and then after entering roundabout, immediately restarts with the distance til the exit point. |
| Exit      | ![](images/157717718.png) | ***exit the roundabout***                                              | Exit instructions don't mention the number of exit since it is not applicable for the current position of the vehicle                                    |

**Multi-lane roundabout instruction design**

| **Phase**    | **Visual**                   | **Audio**                                                                                            | **Notes**                                                                                                                                                                        |
| ------------ | ---------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Early        | ![](images/157717717.png) | ***In one kilometer, at the Roundabout, take the 3rd exit ...***                                     |                                                                                                                                                                                  |
| Main         | ![](images/157717715.png) | ***In four hundred meters, at the Roundabout, stay in the left two lanes to take the 3rd exit ...*** | New design of Unified SLG replaces manoeuvre arrow with SLG at main, Confirmation instruction phases. SLG here depicts lane configuration at the entrance to the roundabout.     |
| Confirmation | ![](images/157717714.png) | ***take the 3rd exit***                                                                              | At the point of entry the distance counter gets down to 0 and then after entering roundabout, immediately restarts with the distance til the exit point.                         |
| Exit         | ![](images/157717712.png) | ***exit the roundabout***                                                                            | New design of Unified SLG replaces manoeuvre arrow with SLG at main, Confirmation instruction phases. SLG here depicts lane configuration at the exit point from the roundabout. |

### SLG logic for multi-lane roundabouts

Multi-lane roundabouts lane recommendation should be gathered from lane connectivity data. Typically, the rightmost lane is connected with the first exit. Second and third to the second exit. Leftmost lane to the 3rd and further exits. This principle, however, could be broken and lane connectivity In those cases the only way to know which lane should be recommended is to read lane markings which are usually drawn on the surface of the road. Generally, when lane connectivity is in place it should be used for gathering recommended lane. And only when all lanes are connected to the target exit equally, we should apply generic lane logic.

**Generic Lane Logic**

| **Exit number** | **Recommended lane**          | **Notes**                         |
| --------------- | ----------------------------- | --------------------------------- |
| 1               | Rightmost                     |                                   |
| 2               | 2nd from the right            |                                   |
| 3               | 2nd or/and 3rd from the right | 3rd \- if third lane is available |
| 4 \- max        | Leftmost                      |                                   |

NOTE: this table is defined for standard driving road side (not UK, Japan). For those regions the side should be reversed.

**Example**

Following example illustrates lane guidance at multi-lane roundabout with 2 exits. Roundabout itself consists of 2 lanes that are not marked on the circle but assumed to be there because ther are 2 lanes at the entrance of the roundabout.

<img src="images/348362330.png" title="" alt="Group 1664678241.png" width="891">

**Instruction modelling for this scenario**

| **Exit No.** | **NIP**                                      | **Audio**                                            | **Notes**                                                                                                                                                                                                                        |
| ------------ | -------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1            | ![Multi_Main-1.svg](images/347936605.svg) | Stay in the middle lane to take the first exit…      | Even though, it possible to change lanes while driving along the circle \- it is not optimal. Therefore using our MPO (manoeuvre path optimisation) method we recommend the most optimal lane that doesn't require lane changes. |
| 2            | ![Multi_Main.svg](images/348036283.svg)   | Stay in the left two lanes to take the second exit…. | Both left lanes are equally optimised for the second exit, therefore both are recommended                                                                                                                                        |

### Roundabout manoeuvre arrow

Visual Instruction represents Roundabout schematically.

| **First exit**               | **Third exit**               | **cross, second exit**       | **take fifths exit**         | **exit roundabout**          |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| ![](images/275168609.png) | ![](images/275522882.png) | ![](images/275490391.png) | ![](images/275427078.png) | ![](images/275427248.png) |

When Exit instruction is omitted?
---------------------------------

There are use cases when exit instruction doesn't have place. Those happen usually due to close proximity of the entry and exit points. They are so close to each other that can be considered as one.

| **Type**                | **Diagram**                  | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First exit to the right | ![](images/157717759.png) | In typical roundabout geometry (but not always), the first exit goes to the right. That puts it in the position which is very close to the entry. Naturally, there is no time for the exit instruction ion this case. Similarly to "Small Roundabouts" handling, in this scenario, exit instruction should be omitted.                                                                                                                                                                         |
| Small Roundabout        | ![](images/157717758.png) | It could happen (usually on small roundabouts) that distance of traveling along the curve (S) could be so small that it will not leave enough time for exit instruction to be announced. For this scenario we should have a method of skipping the exit instruction if time is not sufficient for it. Threshold of travel distance from entry to exit should be defined. Initial value is: \~80m (is it correct value?). To be refined experimentally while driving through small roundabouts. |

Roundabouts types
=================

Different configurations of roundabouts require different instruction compositions, therefore, we define separately following categories of roundabouts:

1. **Small / Straight roundabouts** \- the most trivial traffic figures that require minimal instruction for the manoeuvre.

2. **Single lane roundabouts (excluding #1) -** the most common traffic figures that require moderate instruction for the manoeuvre.

3. **Multi-lane roundabouts -** the most complex traffic figures that require the most elaborative instruction for the manoeuvre.

1\. Small / straight roundabouts
--------------------------------

Small, straight (both conditions must be present to be classified as such) roundabout are trivial intersections and when crossing, don't require too elaborative instruction. Generic roundabout instruction is long and might be annoying especially if repeated in serial scenarios which are common for small roundabouts, therefore we use more natural format for such scenarios. We rely on _**cross the roundabout**_ when going straight and _**go around the roundabout**_ when going back. Street names announcements are also minimised at those traffic figures.

**Small, Straight Roundabouts detection algorithms** TO BE MOVED TO GITHUB

This sections should be moved to the GitHub and managed by _**engineering owner**_.

![](images/icons/grey_arrow_down.png)Detection of Small Roundabout

Small roundabouts must have less than 30m radius. Angle deviations from 90° should not exceed +-5° (both sides)

| **ID** | **Road Network**                                                                   | **Description**                                                                                                                          |
| ------ |------------------------------------------------------------------------------------| ---------------------------------------------------------------------------------------------------------------------------------------- |
| \#1    | <img src="images/157717736.png" title="" alt="" width="404">                       | This is a small (supposedly less than 30m radius) roundabout with clear straight exits.                                                  |
| \#2    | <img src="images/157717735.png" title="" alt="" width="421"> | Two successive roundabout: one of them is small and another is big. For small one we should use short version and for big one \- normal. |
| \#3    | <img src="images/157717733.png" title="" alt="" width="424">                    | This roundabout while small, **is not straight**, therefore id doesn't meet straight direction conditions.                               |

**Detection of straight direction.**

Straight direction for small roundabouts is identified from looking at the following attributes:

| **Attribute**               | **Value** | **Description**                                                                                                                                           |
| --------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Multilane roundabouts       | Yes / No  | Multilane roundabouts are not qualified for having straight direction, as it is hard to keep sense of initial direction when travelling along big circle. |
| Amount of exits             | 2\-8      | Only roundabouts **with 2, 3 and 4 exits** can be qualified for for having *Straight direction*.                                                          |
| deviation of crossing angle | \+\- 5°   | Only roundabouts with branches crossing at 90° or 180° angle can be qualified for for having *Straight direction*.                                        |

**Examples of Roundabouts that cannot have straight direction**

| **ID** | **Geometry**                                                    | **Reasons Why**                  |
| ------ |-----------------------------------------------------------------| -------------------------------- |
| 1      | <img src="images/157717753.png" title="" alt="" width="299">    | More then 4 exits.Non 90° angles |
| 2      | <img src="images/157717755.png" title="" alt="" width="299"> | Non 90° angles                   |
| 3      | <img src="images/157717752.png" title="" alt="" width="309"> | Radius is bigger then 30m        |
| 4      | <img src="images/157717749.png" title="" alt="" width="316"> | Non 90° angles                   |

**Examples of roundabouts qualified for having straight direction**

| **ID** | **Geometry**                                                    | **Reasons Why**     |
| ------ | --------------------------------------------------------------- | ------------------- |
| 1      | <img src="images/157717747.png" title="" alt="" width="319"> | 90° angles, 4 exits |
| 2      | <img src="images/157717746.png" title="" alt="" width="318"> | 90° angles, 3 exits |

Single-Lane Roundabouts (excluding Small/Straight)
---------------------------------------------------

Any roundabout that doesn't fall under category of Small, Straight roundabouts and doesn't have multiple lanes is single lane roundabout.  It uses generic instruction composition using _**take the num Exit**_ every time including straight and back directions. This is due to the fact that it is hard to rely on abstract directions when travelling along on medium/large circle.

Multi-Lane Roundabouts
----------------------

Roundabouts that have lane dividers along their circle. Those roundabouts are large in diameter and require correct lane selection at the entry point. Those roundabout instructions focus on lane guidance **Stay in/Take the** _**num**_ **Right/Left lanes to take the num Exit.** This composition could also be used for **Turbo roundabouts.**

Roundabout Instruction composition
==================================

 Based on the categorisation of roundabouts defined above, we will define instruction composition for each type separately.

Small/Straight Roundabout instruction composition
-------------------------------------------------

**(distance) + (pointer) + (action) + (purpose) + (direction)**  \- this general structure is used, however, as with all other instruction types some components are optional. The general principle of handling such roundabouts is usage of _**cross the roundabout**_ and _**go around the roundabout**_ actions which are only applicable for small roundabouts.

| **ID** | **Attribute**               | **Value**                          | **Notes**                                                                                                                                                                                                                                                                                                                                                                      |
| ------ | --------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \#1    | Distance                    | **in** ***num*** **meters**        | Distance to the entry point is used according to generic instruction template.                                                                                                                                                                                                                                                                                                 |
| \#2    | Pointer                     | **at the roundabout**              | This pointer is used when direction through the roundabout is **not straight or back** (\#3, \#4\)                                                                                                                                                                                                                                                                             |
| \#3    | Pointer                     | **cross the Roundabout**           | This pointer is used when direction through the roundabout **is straight.** Exit number is omitted in this case as, it is straightforward <br/> NOTE: This construction is an exception from general pointer syntax, as action is combined with the pointer \- this is a necessary concession made to comply with English language structure, but it doesn't affect the logic. |
| \#4    | Pointer                     | **go around the roundabout**       | This pointer is used only when direction through the roundabout is a U\-turn.  <br/>NOTE: This construction is an exception from general pointer syntax, as action is combined with the pointer \- this is a necessary concession made to comply with English language structure, but it doesn't affect the logic.                                                             |
| \#5    | Action                      | **take the** ***num*** **exit**    | This action is used every time when direction through the roundabout is not straight or back (\#3, \#4\)                                                                                                                                                                                                                                                                       |
| \#6    | Action                      | **,** ***num*** **exit**           | This action is only used to go around the roundabout (\#4\)                                                                                                                                                                                                                                                                                                                    |
| \#7    | Purpose                     | **to stay on**                     | This purpose is used only when incoming and outgoing roads are identical (except of "go around the roundabout")                                                                                                                                                                                                                                                                |
| \#8    | Direction (roadName/Number) | **onto** ***signpostRoadName***    | used only if provided by the signpost. In the presence of towards direction, this field is omitted.                                                                                                                                                                                                                                                                            |
| \#9    | Direction (Towards)         | **towards** ***signpostLocation*** | Used when there is a signpost with towards information related to the exit.                                                                                                                                                                                                                                                                                                    |
| \#10   | Action                      | **exit the roundabout**            | Used for exits                                                                                                                                                                                                                                                                                                                                                                 |

**Example of Instructions for simple / straight Roundabouts**

| **ID** | **NIP**                      | **distance**  | **pointer**              | **action**               | **purpose** | **direction**      | **reason**                             |
| ------ | ---------------------------- | ------------- | ------------------------ | ------------------------ | ----------- | ------------------ | -------------------------------------- |
| \#1    | ![](images/157717722.png) | in 1 km       | At the Roundabout        | take the third exit onto | \-\-        | *signpostRoadName* | Road name is provided by the signpost. |
| \#2    | ![](images/157717881.png) | in 500 meters | Cross the Roundabout     | \-\-                     | \-\-        | *\-\-*             | staying on the same road               |
| \#5    | ![](images/157717884.png) | in 500 meters | Go around the Roundabout | , second exit            | \-\-        | \-\-               | roadName is omitted.                   |

Single-lane roundabouts audio instruction attributes (excluding the small and straight roundabouts described above).
--------------------------------------------------------------------------------------------------------------------

**(distance) + (pointer) + (action) + (purpose) + (direction)**  \- this general structure is used, however, as with all other instruction types some components are optional

| **ID** | **Attribute**               | **Value**                          | **Notes**                                                                                                                                                                                                                                                                                                                                             |
| ------ | --------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \#1    | Distance                    | **in** ***num*** **meters**        | Distance to the entry point is used according to the generic instruction template.                                                                                                                                                                                                                                                                    |
| \#2    | Pointer                     | **at the roundabout**              | This action is used every time                                                                                                                                                                                                                                                                                                                        |
| \#3    | Action                      | **take the** ***num*** **exit**    | This action is used every time                                                                                                                                                                                                                                                                                                                        |
| \#4    | Purpose                     | **to stay on**                     | This purpose is used only when incoming and outgoing roads are identical                                                                                                                                                                                                                                                                              |
| \#5    | Direction (roadName/Number) | **onto** ***roadName***            | Used every time as long as towards is not provided. <br/> <br/>Road name/number coming from the signpost has priority over map data as defined globally [NIE\_016 \- Directional Information (Road names, Road numbers)](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Guidance%20Framework%20-%20Methods%20%26%20Components/Directional%20Information%20-%20Road%20names%2C%20Road%20numbers%2C%20Towards%20/Directional_Information-Road-names_Road-numbers_Towards.md) |
| \#6    | Direction (Towards)         | **towards** ***signpostLocation*** | Used when there is a signpost with towards information related to the exit.                                                                                                                                                                                                                                                                           |
| \#7    | Action                      | **exit the roundabout**            | Used for exits                                                                                                                                                                                                                                                                                                                                        |

NOTE:The main difference in handling of this group of roundabouts is not using "cross the roundabout" and "go around the roundabout" actions. Instead, only exit numbers are used.

**Example of Instructions for single lane Roundabouts**

| **ID** | **NIP**                      | **distance** | **pointer**       | **action**               | **purpose** | **direction**     | **reason**                                                     |
| ------ | ---------------------------- | ------------ | ----------------- | ------------------------ | ----------- | ----------------- | -------------------------------------------------------------- |
| \#1    | ![](images/157717722.png) | in 1 km      | At the Roundabout | take the third exit onto | \-\-        | *roadName*        | No signpost towards information available                      |
| \#2    | ![](images/157717870.png) | in 1 km      | At the Roundabout | take the second exit     |             | towards *Dresden* | Signpost information with Dresden is available in the signpost |
| \#6    | ![](images/157717718.png) | \-\-         | \-\-              | exit the roundabout      | \-\-        |                   |                                                                |

### Multi-lane roundabouts audio instruction components

**(distance) + (pointer) + (action) + (purpose) + (direction)**\- this general structure is used, however, as with all other instruction types some components are optional

| **ID** | **Component** | **Value**                                  | **Notes**                                                                                                                                                                                                                                                                                                                                             |
| ------ | ------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \#1    | Distance      | **In** ***num*** **meters**                | Distance is used according to generic instruction template.                                                                                                                                                                                                                                                                                           |
| \#2    | Pointer       | **at the roundabout**                      | This action is used every time                                                                                                                                                                                                                                                                                                                        |
| \#3    | **Action**    | **stay in** ***num*** **Right/Left lanes** | Amount of lanes (num) and their logic varies depending on the geometry and follow generic Lane guidance. This action is used at **Main instruction phase**                                                                                                                                                                                            |
| \#4    | **Purpose**   | **to take the** ***num*** **exit**         | This action is used at **Main instruction phase**                                                                                                                                                                                                                                                                                                     |
| \#5    | **Action**    | **take the** ***num*** **exit**            | This action is used at **Early instruction phase**                                                                                                                                                                                                                                                                                                    |
| \#6    | Direction     | **to** ***roadName***                      | Used every time as long as towards is not provided. <br/> <br/>Road name/number coming from the signpost has priority over map data as defined globally [NIE\_016 \- Directional Information (Road names, Road numbers)](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Guidance%20Framework%20-%20Methods%20%26%20Components/Directional%20Information%20-%20Road%20names%2C%20Road%20numbers%2C%20Towards%20/Directional_Information-Road-names_Road-numbers_Towards.md) |
| \#7    | Direction     | **towards** ***signpostLocation***         | Used when there is a signpost with towards information related to the exit                                                                                                                                                                                                                                                                            |
| \#8    | Action        | **exit the roundabout**                    | Used for exits                                                                                                                                                                                                                                                                                                                                        |

**Example of Instructions for multi-lane roundabouts:**

| **id** | **NIP**                      | **Phase** | **distance** | **pointer**       | **action**             | **purpose**            | **direction**              | **Reason**                                                                     |
| ------ | ---------------------------- | --------- | ------------ | ----------------- | ---------------------- | ---------------------- | -------------------------- | ------------------------------------------------------------------------------ |
| \#1    | ![](images/157717874.png) | Main      | in 400meters | At the Roundabout | stay in two left lanes | to take the third exit | to *roadName*              | No signpost towards information available                                      |
| \#2    | ![](images/157717875.png) | Main      | in 400meters | At the Roundabout | stay in two left lanes | to take the third exit | towards *signpostLocation* | Road name is replaced with the towards, because it is provided in the signpost |
| \#3    | ![](images/157717878.png) | Early     | in 2 km      | At the Roundabout | take the third exit    | \-\-                   | to *roadName*              | No signpost towards information available                                      |
| \#4    | ![](images/157717712.png) | \-\-      | \-\-         | \-\-              | exit the roundabout    | \-\-                   | to *roadName*              |                                                                                |

Roundabout exits counting (identifying _num_ parameter)
=======================================================

Roundabout exits can have various angles relative to the direction of entry. NIE supports max 8 exits. All possible directions must be mapped to 8(max.) directions.  Each exit is identified by a number which is going counterclockwise. NOTE: For Right handed driving countries (UK, Japan) the direction is inverted.

![](images/157717800.png)

### Dealing with Tangential exits

Tangential exits, technically, are not belongs to a roundabout as they bypass it via dedicated straight paths. Those exits should not be counted and should not even be considered as roundabout instructions. I

**Tangential exits**

| **Type**   | **Diagram**                                                                                                             | **Notes**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------- |-------------------------------------------------------------------------------------------------------------------------| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tangential | <img src="images/307203509.png" title="" alt="Screenshot 2024-08-22 at 09.53.42.png" width="450"> | Tangential lines that are passing by the roundabout ***without even touching the the circle perimeter.*** The instruction should not be *Roundabout instruction,* but rather *Turn, Bear, Keep* \- whatever is applicable for the given geometry. <br/> <br/>NOTE: If tangential line touches the perimeter (has a common segment), the exit is considered to be belongs to roundabout.  If the route passes through a roundabout (has at least one roundabout arc) then a roundabout instruction is generated. If the route just includes a roundabout junction and doesn't include a roundabout arc, roundabout instruction is not generated. |

\----- END OF DOCUMENT -----
============================