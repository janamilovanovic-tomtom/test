| **Interaction Designer** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence)                                                                                                                                                    |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Visual Designer**      | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence)                                                                                                                                                              |
| **PM**                   | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence)                                                                                                                                                  |
| **ENG. OWNER**           | [Dennis Jakobsen](https://tomtom.atlassian.net/wiki/people/712020:c273d0e3-9a2a-456c-ad2f-6f56ca0e12b3?ref=confluence) → please assign                                                                                                                                 |
| **Refrerence**           | [Directional Information \- Road names, Road numbers, Towards](./../../Guidance%20Framework%20-%20Methods%20%26%20Components/Directional%20Information%20-%20Road%20names%2C%20Road%20numbers%2C%20Towards/Directional_Information-Road-names_Road-numbers_Towards.md) |

Motivation
==========

Directional information described here [Directional Information - Road names, Road numbers, Towards](./../../Guidance%20Framework%20-%20Methods%20%26%20Components/Directional%20Information%20-%20Road%20names%2C%20Road%20numbers%2C%20Towards/Directional_Information-Road-names_Road-numbers_Towards.md) varies drastically across world regions. The purpose of this page is to capture those differnces and specify regional design patterns in regards to **Road names/numbers, Towards information, Exit numbers, Intersection names.**

  

Spelling of numerical values
============================

Road numbers have special spelling in some areas. Here are some known local use cases that has been identified so far.

| **Road number** | **US** | **the rest of the world**  **(Unconfirmed)** | **Notes** |
|---|---|---|---|
| I\-248 | I two forty eight | I two hundred forty eight | In the US, 3 digit numbers without zero in the middle pronounced as: **(first single digit)** \+ **(two digits number)** |
| I\-105 | I one o five | I one hundred and five | In the US, 3 digit numbers with zero in the middle pronounced as: **(first single digit)** \+ **O** \+ **(third single digit)** |
| I\-2144 | I twenty one forty four | I two thousands one hundred forty four |  |
| I\-3405 | I thirty four o five | I three thousands four hundred and five |  |
| Interstate 345 | I three forty five | I three hundred forty five | **"Interstate"** is never pronounced and is converted to **"I"** |

Cardinal directions
===================

Sometimes Cardinal directions are indicated as part of road number.

| **Road number** | **Audio announcement** |
|---|---|
| I\-345 NE | i three forty five North\-East |
| I\-98 S | I ninety eight South |

Road numbers varieties
======================

Due to multiple standards that are often used simultaneously on signposts, there varieties of Road numbers refereeing to the same road segment.

| **Road Number format** | **Region** |  | **Priority** | **Notes** |
|---|---|---|---|---|
| A25 | EU | A \- standing for ***Autobahn*** is a european local standard for Motorways | High | When encountered at signpost both A and E\-types, A\-type of road number should always be used instead of E\-type. For both visual and Audio instructions |
| E45 | EU | E \- is international standard | Low | E\-type should only be used when no A\-type referring to the same road is present. |