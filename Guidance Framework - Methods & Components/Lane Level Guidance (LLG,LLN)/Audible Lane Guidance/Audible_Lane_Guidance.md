| **created by** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) |
|---|---|
| **PM** | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |
| **ENG OWNER** | undefined |

This method is put on hold for the moment

Motivation
==========

With regards to Audio, there are two types of system setups need to be mentioned. First one is when lane level vehicle positioning is provided, and second when it is not. Let call it _**lane localisation**_ further on. Lane localisation allow for more precise an contextual audio guidance since lane position of the vehicle is known. When Lane GPS positioning is provided by the system, more precise audio guidance can be enabled. The purpose of Audio LLG is **to nudge driver towards correct lane/s** without reliance on the screen.  
  

Method
======

Audio LLG should only be activated if driver is on the wrong lane at the required time.

If Driver doesn't react to audio instruction, the instruction should be repeated after time out.  
  

**Possible Scenarios of Audio LLG**
Evo formatiranog teksta:

| **Scenario**                              | **Vehicle Position**                   | **Audio Instruction** |
|-------------------------------------------|----------------------------------------|------------------------|
| Exiting to the right                      | vehicle is on the straight direction lanes | Keep Right             |
| Continue straight while passing an exit   | vehicle is on the exit lanes           | Keep Left              |
| At a fork, continue to the right branch   | vehicle is on the left branch lanes    | Keep Right             |
| At a fork, continue to the left branch    | vehicle is on the right branch lanes   | Keep Left              |
| Lane dependent traffic jam tail on the right lane(s) | vehicle is on the right lane(s)     | Keep Left              |

  

\----------- END OF DOCUMENT -----------
========================================