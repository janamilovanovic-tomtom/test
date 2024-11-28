| **Interaction Designer** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) |
|---|---|
| **Visual Designer** | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence) |
| **PM** | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |
| **ENG. OWNER** | [Dennis Jakobsen](https://tomtom.atlassian.net/wiki/people/712020:c273d0e3-9a2a-456c-ad2f-6f56ca0e12b3?ref=confluence) → please assign |
| **Reference** | [Filter Low priority road numbers.](https://tomtom.atlassian.net/wiki/spaces/NAV/pages/104671604/NIE+Feature+filter+low+priority+road+numbers) |

Introduction
============

Navigation instructions, both visual and audio use **road identities** as one of the arguments. Road identity is a string or several strings that are used to identify the road segment in the map. Examples of Road Identities are: _**Oak St., Schoenhauser Allee, A100, B33**_. When road identity consists of text string - we call it **Road name**. If it is a number - **Road number.** Road numbers also have visual attributes, like colours and graphics. Road Identities that are reflected in the NIP and Audio instructions we also used to call - **Directional Information.** There are following types of Directional information: _**Road names, Road numbers, Towards information, Intersection names, exit numbers.**_  

Nested Identities
=================

Road is an object that has length and consists of segments.  **Road identities** can be assigned to individual segments and can vary by segment. There are different **orders of identity** which can be applicable to a segment. The following diagram illustrates the nested structure of road identities. Depending on the segment, it could have one identity (96a), or two identities (96a, Danziger Str.). Potentially more levels of nested identities are possible, however they are not encountered. Structure could be illustrated as: B96a - (Danziger str.) - (Schoenhauser Alee) - (Berlinerstr.) - B96a…

![](images/157688332.png)

In this example, **96a** is a higher order of road identity, while **Street name** is the lowest.  

Multiplicity of Identities
==========================

Those identities are assigned to each segment in NDS map data. In addition to this (optionally) there is **Signpost information** assigned to segments. Signpost information reflects what is shown on appropriate signpost and also contains Directional Information. As a result we are dealing with multiple sources for Directional information (one from Map data and another from Signpost). Navigation system must decide which information to use for Guidance, how to select the the right data fields. A logic must be provided for selecting correct road identities to be used by guidance in both visual instruction (NIP) and audio. This document provides this information.

**This document answers following questions:**

*   How do we know which Directional information to display in the NIP and announce by audio?
    
*   How to pronounce numerical road numbers in different parts of the world?
    
*   How to deal with Cardinal direction which is sometimes parts of Road identity. How to handle it in audio instructions?
    

Data provided for Directional Information
=========================================

Information about road identities comes from different sourced in from the map structure: 

|**Directional info from Map**|**Directional info from Signpost**|**Can be multiple**|
| --- | --- | --- |
|Road Name|Road Name| Yes|
|Road Number|Road Number| Yes|
| | Towards information| Yes|
| | Exit number| Yes|
| Intersection name| Intersection name|No|

NOTE: Directional information from map is taken from the road segment at the point after the manoeuvre (except of intersection name). In case this is a slip road (without identity) next significant road segment should be used. Directional information from Signpost is taken from road segment before the manoeuvre, where signpost is located.

Display Priority 
-----------------

Road numbers have an attribute called _**display priority**_ in NDS map. We use this attribute to filter out insignificant road numbers. The detailed logic of this filtering is not covered this document but it is specified here: [F](/wiki/pages/createpage.action?spaceKey=FlaminGO&amp;title=NIE&amp;linkCreation=true&amp;fromPageId=157686877)[ilter Low priority road numbers](https://tomtom.atlassian.net/wiki/spaces/NAV/pages/104671604/NIE+Feature+filter+low+priority+road+numbers).

Principles for selecting Directional Information for the purpose of Guidance
============================================================================

Directional information is used by Guidance. Here are the general rules that are applied for selection of Road identity for **the NIP and Audio.** 

QUANTITATIVE RULES
------------------

Only one Road name and towards information can be displayed in the NIP and announced by Audio.  
Multiple Road numbers can be displayed in the NIP.  
One road number should be announced by audio.

|  | **Road Name** | **Road Number** | **Towards** | **Intersection name** | **Exit number** |
|---|---|---|---|---|---|
| **NIP** | 1 | multiple (limited by the uI) | 1 | 1 | can be range of numbers |
| **Audio** | 1 | 1 | 1 | 1 | can be range of numbers |

SIGNPOST RULES
--------------

1.  Signpost information **has always priority** over map gathered information. if it is available and should be used instead of map data if they are conflicting.
    
2.  Road identity which is the part of the route has priority over the one which is not. (Currently we use "Display Priority" attribute for Road Numbers to select the one that has to be displayed)
    
3.  Location (which is part of Directional info) is treated as Towards information. The issue is considered to  be an NDS map data problem. To be followed up with NDS.   
    

MULTIPLE ROAD NUMBERS RULES (SIGNPOST)
--------------------------------------

When Multiple road numbers provided in Signpost and ...  

1.  ... some of them are part of the route while others are not, only display in the NIP those that are part of the route.
    
2.  ... none of them are part of the route, display all of them. (Max. amount of items is defined by NIP configuration.)
    
3.  ... and they refer to different roads (not different orders of the same road) only display those that are part of the route.
    
4.  ... some of them are different name standards corresponding to the same road (International and local) use only one (local) standard. 
    

  
  
MULTIPLE ROAD NAMES RULES (SIGNPOSTS)
-------------------------------------------

When Multiple road names are provided and ...  

... some of them are part of the route while others not, select the one (first one) which is the part of the route.  
... none of them are part of the route, select the first one.  
  

AUDIO RULES
-----------

Audio should announce all or partial information that is displayed in the NIP.

Matrix for selection of right road identity from provided combinations
======================================================================

Table below provides a detailed matrix of all possible combinations of directional information and in the right two columns is shown which attributes should be chosen for guidance(both NIP and Audio). This table provides another view to the rules described above.

| **ID** | **Road name**  **MAP** | **Road number**  **MAP** | **Road Name**  **SIGNPOST** | **Road Number**  **SIGNPOST** | **SHOW IN THE NIP** | **AUDIO \| Updated at**27 Mar 2024 | **Audio Examples** |
|---|---|---|---|---|---|---|---|
| **1** | x |  |  |  | road name | road name | turn left onto ***Wichertstrasse*** |
| **2** |  | \*x |  |  | road number  (highest order if multiple) | road number | turn left onto ***B96a*** |
| **3** | x | x |  |  | road name \+ road number | Road Name \- in Urban areas <br/> Road Number  \- Motorways and others | turn left onto ***Eisenstrasse*** |
| **4** | x |  | x |  | rNameSign | rNameSign | turn left onto ***Eisenstrasse*** |
| **5** | x |  |  | x | rNumSign | rNumSign | turn left onto ***B96a*** |
| **6** | x |  | x | x | rNumSign \+ rNameSign | rNameSign \+ rNumSign | turn left onto ***Eisenstrasse B96a*** |
| **8** | x | x | x |  | rNameSign | rNameSign | turn left onto ***Eisenstrasse*** |
| **9** | x | x | x | x | rNumSign \+ rNameSign | rNameSign \+ rNumSign | turn left onto ***Eisenstrasse B96a*** |
| **10** | x | x |  | x | rNumSign | rNumSign | turn left onto ***B96a*** |
| **11** |  |  | x |  | rNameSign | rNameSign | turn left onto ***Eisenstrasse*** |
| **12** |  |  |  | x | rNumSign | rNumSign | turn left onto ***B96a*** |
| **13** |  |  | x | x | rNumSign \+ rNameSign | rNameSign \+ rNumSign | turn left onto ***Eisenstrasse B96a*** |

\*NOTE: if road number is not the lowest display priority  

  
\- / END OF DOCUMENT /
=========================