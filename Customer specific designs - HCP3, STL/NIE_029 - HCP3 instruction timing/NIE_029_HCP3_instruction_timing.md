| **Created by** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence), [Bohdan Soroka](https://tomtom.atlassian.net/wiki/people/712020:d6cafcbe-bb3a-4305-bba3-02e3350309bc?ref=confluence) [Oleh Kis](https://tomtom.atlassian.net/wiki/people/712020:bd4f4d9f-75d9-4d67-8408-8ace89f8fda6?ref=confluence) |
|---|---|
| PM | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |
| Code | [https://github.com/tomtom\-internal/nk2\-navigation\-triggering\-engine/tree/main/navigation\-triggering\-engine/src/triggering\_engine/config/HCP3](https://github.com/tomtom-internal/nk2-navigation-triggering-engine/tree/main/navigation-triggering-engine/src/triggering_engine/config/HCP3) |

  

Table of Contents
=================


*   [Table of Contents](#Table-of-Contents)
*   [Background](#Background)
*   [Minimal Distance values](#Minimal-Distance-values)
*   [Current timing implementation HCP3](#Current-timing-implementation-HCP3)
    *   [Rest of the world](#Rest-of-the-world)
    *   [NAR Region](#NAR-Region)

  

Background
==========

HCP3 team has requested custom configuration to be applied for them which differs from TT configuration. HCP3 team evaluates their system performance in their cars and those requests are based on this evaluation. Since in TT we have our own evaluation setup, the results from those evaluations often differ. This is the reason why we cannot unify HCP3 and TT configurations. this document covers those delta differences present in HCP3 configuration

Minimal Distance values
=======================

Following Tables define values of Minimal distance.   
  
Triggering points are not universal and differ by road classes. We currently differentiate between 4 types of roads:

1. Motorways in NAM region (controlled access or motorway)  

2. Motorways the rest of the world (controlled access or motorway)  

3. Rural roads (neither Motorways nor Urban)

4. Urban Roads

Current timing implementation HCP3
========================================

Rest of the world
-----------------

2 secs audio compensation  
Data source: [https://github.com/tomtom-internal/nk2-navigation-triggering-engine/blob/main/navigation-triggering-engine/src/triggering\_engine/config/HCP3/triggering\_configuration.json](https://github.com/tomtom-internal/nk2-navigation-triggering-engine/blob/main/navigation-triggering-engine/src/triggering_engine/config/HCP3/triggering_configuration.json)

|  | Prepare (early)  trigger distance (announcement) | Distance (main) | Call for action (now)                                           |
|---|---|---|-----------------------------------------------------------------|
| Controlled access / motorways | 2300 m (2 km) | 1300 m (1 km) | 550 m(Earliest)  <br/> 250 m(Recommended)                       |
| Rural (admin class \[0\-3]) | 800 m | 300 m | 140 m(Earliest) <br/> 100 m(Recommended)                             |
| Low Priority Rural (admin class \[4\-6]) | 800 m | 300 m | 100 m(Earliest)  <br/>70 m(Recommended)                              |
| Urban (admin class \[4\-6]) | 600 m | 300 m | 70 m(Earliest)  <br/>50 m (no audio compensation) \*                 |
| High speed Urban  (admin class \[0\-3]) | 600 m | 300 m | 100 m(Earliest) <br/> 65 m (Recommended) <br/> (no audio compensation) \* |

NAR Region
----------

2 secs audio compensation  
Source data: [https://github.com/tomtom-internal/nk2-navigation-triggering-engine/blob/main/navigation-triggering-engine/src/triggering\_engine/config/HCP3/triggering\_configuration\_NAR.json](https://github.com/tomtom-internal/nk2-navigation-triggering-engine/blob/main/navigation-triggering-engine/src/triggering_engine/config/HCP3/triggering_configuration_NAR.json)  

|  | Prepare (early)  trigger distance (announcement) | Distance (main) | Call for action (now) |
|---|---|---|---|
| Controlled access / motorways | 3379 m (2 mi) | 1770 m (1 mi) | 400 m\* (1300 ft) (Earliest)  <br/>263m\* (900 ft) (Recommended) |
| Rural (admin class \[0\-3]) | 1287 m (3/4 mi) | 482 m (1/4 mi) | 304 m (1000 ft) (Earliest)  <br/>91 m (300 ft) (Recommended) |
| Low Priority Rural (admin class \[4\-6]) |
| Urban (admin class \[4\-6]) | 1287 m (3/4 mi) | 482 m (1/4 mi) | 228 m (no audio compensation) \* (750 ft) (Earliest)  <br/>76 m (no audio compensation) \* (250 ft) (Recommended) |
| High speed Urban (admin class \[0\-3]) |

**Notes:** 

Follow instructions will be triggered before the Prepare phase.   
Instruction phases announcement distance values are rounded.   
Arrival instructions follow the values for other instructions with the exception that the audio duration compensation for Now is in place for arrival instruction.  
If maneuvers are close to each-other then instruction phases can be combined or skipped. 

* Triggering "now" on controlled access has been changed to give trigger 50m earlier (based on drive test feedback), see [HCP3-14648](https://tomtom.atlassian.net/browse/HCP3-14648?src=confmacro) 