![](images/157686367.png)


| **Interaction Designer** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence)                                                                                                                                  |
|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Visual Designer** | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence)                                                                                                                                            |
| PO | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence)                                                                                                                                |
| DEV | [Vadym Khandus](https://tomtom.atlassian.net/wiki/people/712020:2b00ecb1-a543-4410-818c-575056da8b84?ref=confluence)                                                                                                                                 |
| TICKETS | [GOSDK\-13065](https://tomtom.atlassian.net/browse/GOSDK-13065)<br>[NAV\-23334](https://tomtom.atlassian.net/browse/NAV-23334)<br>[NAV\-95745](https://tomtom.atlassian.net/browse/NAV-95745)<br>[NAV\-92335](https://tomtom.atlassian.net/browse/NAV-92335) |

  

Table of Contents
=================


*   [Table of Contents](#Table-of-Contents)
*   [Introduction to Landmarks](#Introduction-to-Landmarks)
*   [Impact on Instruction Design](#Impact-on-Instruction-Design)
*   [Supported landmarks](#Supported-landmarks)
*   [General Design Principle &amp; methods](#General-Design-Principle--methods)
    *   [Inform about Landmark when it is needed.](#Inform-about-Landmark-when-it-is-needed)
    *   [One Landmark at a time](#One-Landmark-at-a-time)
    *   [Visual &amp; Audio Pointers](#Visual--Audio-Pointers)
    *   [Serial Landmarks handling](#Serial-Landmarks-handling)
*   [Specific Landmarks designs](#Specific-Landmarks-designs)
*   [Future plans](#Future-plans)

  

**Introduction to Landmarks**
=============================

Landmarks is an object or feature of a landscape or town that is easily seen and recognised from a short distance, especially one that enables someone to determine their location. User research in Europe and Asia shows that users commonly explain routes in relation to **landmarks, junctions and paths.** **Landmarks** are recommended to be used as guiding _**Pointers**_ in Navigation. This is due to a more natural, human way of orientation in space that Landmarks provide.

NOTE: based on the EU Research project [Hardie Guidelines](https://tomtom.atlassian.net/wiki/pages/viewpage.action?pageId=87302106&amp;navigatingVersions=true)

**Impact on Instruction Design**
================================

Landmarks are manifested in Guidance in following ways:

*   Announced by Audio
*   Visualised in the NIP (not all Landmarks)
*   Landmarks are also rendered on the map (not all Landmarks)

NIE provides [modular Instruction architecture](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Guidance%20Framework%20-%20Methods%20%26%20Components/Instruction%20arhitecture/Instruction_architecture.md). There is a specific component in this architecture which is reserved for Landmarks - _**Pointer**_. Term _**Landmark**_ and _**Pointer**_ can be used interchangeably, but it is important to clarify, while _**Landmark**_ refers to the real object itself on the road in real world, _**Pointer**_ is a UI element (and audio component) which is pointing to it. 

  

  

**Supported landmarks**
=======================

NavSDK currently (Q1.2024) supports the following landmarks:

| Landmark | Supported | Notes |
|---|---|---|
| Traffic lights | YES | Visualisation is not supported |
| Bridges | NO | Regression due transition to NavSDK |
| Tunnels | NO | Regression due transition to NavSDK |
| End of road (T Junction) | YES |  |

  

  

**General Design Principle &amp; methods**
======================================

To effectively and unobtrusively communicate relevant for the moment Information to the driver, we follow those general principles for Landmark Pointers:

  

Inform about Landmark when it is needed.
----------------------------------------

Drivers are easily overloaded with information, therefore it is critical to provide it in time - not too early and not too late. There is no point to tell about Landmarks at large distances, but at the moment of a turn it is also too late. For those reasons we communicate Landmark information in Audio only at [Main Instruction phase](https://tomtom.atlassian.net/wiki/display/FlaminGO/NIE_004+-+Instruction+Triggering+Logic). Landmark **is not announced at Early and Confirmation phases**. This doesn't affect the visual representation of landmark in the NIP and Map. It can still be shown earlier, following general rules for the NIP and Map components.

  

One Landmark at a time
----------------------

Due to a nature of guidance, we can only use **one landmark at a time**. Therefore when multiple landmarks occur at the same location the highest priority landmark is included.

Some [external research](https://tomtom.atlassian.net/wiki/download/attachments/87294859/Burnett%2C%20G.E.%20%282000%29%20³Turn%20right%20at%20the%20traffic%20lights².pdf?version=1&amp;modificationDate=1519041512000&amp;api=v2) indicates that landmarks are most useful to users which are:

*   visible from a distance
*   unique in appearance
*   close to or part of the road
*   relatively permanent

Here is the table defining priorities of landmarks in case of conflicts of conflicts:

| Landmark | Priority |
|---|---|
| Tunnel | 1 |
| End of the road | 2 |
| Traffic light | 3 |
| bridge | 4 |

  

Visual &amp; Audio Pointers
-----------------------

Landmark can be represented by **visual** (element in the NIP, Map pointer) and **audio** (announcement "...at the Traffic Light... ") components. **Visual component is not always applicable**, due to the nature of some landmarks (bug bridges for example), while Audio should be always used.

  

Serial Landmarks handling
-------------------------

Some types of Landmarks (Traffic Lights) often come in successions, which makes it harder to refer to as they are multiple. There should be special methods applied to handle such situations and disambiguate multiplicity of landmarks for the driver.

  

  

  

  

**Specific Landmarks designs**
==============================

To dive into design details of each type of landmark, follow those pages:

1.  [End of the road](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Guidance%20Framework%20-%20Methods%20%26%20Components/Landmarks/Landmarks%20-%20End%20of%20the%20Road/Landmark_End_of_the_Road.md)
2.  [Traffic Light](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Guidance%20Framework%20-%20Methods%20%26%20Components/Landmarks/Landmarks%20-%20Traffic%20Light/Landmark_Traffic_Light.md)
3.  [Bridge](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Guidance%20Framework%20-%20Methods%20%26%20Components/Landmarks/Landmarks%20-%20Bridges/Landmark_Bridges.md)
4.  [Tunnel](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Guidance%20Framework%20-%20Methods%20%26%20Components/Landmarks/Landmarks%20-%20Tunnels/Landmark_Tunnels.md)

  

**Future plans**
================

At the moment (Q4.2023) there is very limited support for Landmark types

Below a full list of potential items to explore as a candidates for Landmarks: 

| Name | Landmark | Edge | District |
|---|---|---|---|
| Pelican crossing | ✓ |  |  |
| Bridge over road | ✓ |  |  |
| Hump\-backed bridge | ✓ |  |  |
| Petrol station | ✓ |  |  |
| Monument | ✓ |  |  |
| Railway station | ✓ |  |  |
| Road sign/signpost | ✓ |  |  |
| Point of Interest | ✓ |  |  |
| Stop sign | ✓ |  |  |
| Crosswalk | ✓ |  |  |
| Railroad crossing | ✓ |  |  |
| Tram lines |  | ✓ |  |
| River |  | ✓ |  |
| Canal |  | ✓ |  |
| Lake |  | ✓ |  |
| Sea |  | ✓ |  |
| Forest |  | ✓ |  |
| Park |  | ✓ |  |
| Grass |  | ✓ |  |
| Railway track |  | ✓ |  |
| City centre |  |  | ✓ |
| University campus |  |  | ✓ |

  

