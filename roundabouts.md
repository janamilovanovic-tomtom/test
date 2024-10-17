| **Status**     | <mark>MOVED TO REVIEW</mark>                                                                                             |
| -------------- |:------------------------------------------------------------------------------------------------------------------------ |
| **IXD**        | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence)      |
| **VD**         | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence)                |
| **ENG. OWNER** | [Agnieszka Sobczyk](https://tomtom.atlassian.net/wiki/people/712020:27737e77-b2fa-4ca4-9fbf-019cbab57789?ref=confluence) |
| **PM**         | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence)    |
| **TICKET**     | [NAV-131044](https://jira.tomtomgroup.com/browse/NAV-131044) - [PRIO 2] Roundabout - critical tech debt                  |

Introduction
============

| **Issue**                                                                                                            | **Possible solution**                         |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Turn directions (turn right/ left) often reported as wrong/misleading. Turns only work in narrow range scenarios     | Remove turn directions at roundabouts         |
| Turn directions for big roundabouts are useless, as driver loses original perspective while driving along the curve. | Remove turn directions at roundabouts         |
| Lane guidance is misleading on a big roundabouts                                                                     | Provide SLG design for multi-lane roundabouts |
| Exit Roundabout instruction is not clear.                                                                            | Clarify exit instruction                      |

Roundabouts are complicated intersection type that require special instruction for handling. Typically driving through roundabouts poses following challenges: It is not easy to identify correct exit, especially if there are many and directions are not straight. The challenge is amplified by the fact that decision should be made very fast. To address this we must prepare the driver upfront and provide him necessary information that could be applied instantly. Typical method of guidance trough roundabouts is mentioning the **number of exit** (counted from the entry point) that has to be taken. It is relatively easy to count exits for the driver, however this could be complicated if exits are mixed up with entries. It is not always easy to distinguish entries from exits especially when it needs to be done very fast during counting. Add new line.

Unlike, general instruction template, roundabout manoeuvre doesn't take place at one point but has a stretch of the road with two key points: entry and exit. To reflect this, the instruction has different architecture and consists of two parts:

**Entry Roundabout instruction** \- Given for the entry as a manoeuvre point. Instructs how to perform whole Roundabout manoeuvre from entry to exit.   
**Exit roundabout instruction** \- Given for the exit as manoeuvre point. Only instructs how to perform the exit roundabout manoeuvre, while being already on the roundabout.

![](images/5.svg)
<img src="images/5.svg" title="" alt="" width="965">
