
| **created by** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) |
| --- | --- |
| PM  | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |





Table of Contents
=================


* [Table of Contents](#Table-of-Contents)
* [Introduction](#Introduction)
* [Fundamental, architectural topics](#Fundamental-architectural-topics)
* [Recent Issues - bugs](#Recent-Issues---bugs)


Introduction
============

For the sake of keeping track of things, we created this page that consolidates the most critical Guidance Improvements collected over long period of time. These issues were gathered by self evaluation, user drive testing sessions and external feedback. Some of them are not yet implemented features that were originally planned.





Fundamental, architectural topics
==================================

The issues listed here are debt from last year. The table below summarizes the selection made based on effort and value. Those topics represent fundamental building block of the Guidance framework that enable other thins. Those are not bugs or issues, but rather missing framework implementations.



| Topic | Description | UX  | Ticket | Size | Value (1..5 highest) | Relevance | Budget 2024 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Localization | Using locally recognized Roads and Intersections |     | [GOSDK-21554](https://tomtom.atlassian.net/browse/GOSDK-21554?src=confmacro) |     | 5   | Very relevant | Improvement bucket |
| Arrival experience | Entry point arrival |     | [GOSDK-16972](https://tomtom.atlassian.net/browse/GOSDK-16972?src=confmacro) |     | 4   |     | Improvement bucket |
| Departure experience | Current Departure experience is only partially implemented. | [NIE_015 - Departure Instruction](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Instructions/Departure%20Instruction/Departure_Instruction.md) | [GOSDK-21564](https://tomtom.atlassian.net/browse/GOSDK-21564?src=confmacro)  |     | 3   | Very relevant | Improvement bucket |
| Actions and Purpose (restructuring ![(question)](images/icons/emoticons/help_16.png) \+ switch HW) | Enabling modular instruction framework that will support future complex instructions | [NIE_013 - Motorway instructions (Forks & Exits)](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Instructions/Furcations%20-%20%20Bifurkations%2C%20Trifurcation%2C%20Exits%20%20/Furcations-Bifurkations_Trifurcation_Exits.md) | [NAV-76405](https://tomtom.atlassian.net/browse/NAV-76405?src=confmacro)  | XL  | 4   | Yes, still very relevant | As part of Audible lane guidance |
| Analytics | Enabling Analytics for guidance flywheel | links in the ticket | [NAV-54315](https://tomtom.atlassian.net/browse/NAV-54315?src=confmacro)  |     | 4   | Yes, still very relevant | Improvement bucket |
| Audible lane guidance | Supporting lane guidance by audio including design of all scenarios when it is required. | Some examples  <br>no spec yet, task inside epic | [NAV-49004](https://tomtom.atlassian.net/browse/NAV-49004?src=confmacro) | L   | 4   | Yes, still very relevant | Feature |
| Junction views |     |     | [GOSDK-14374](https://tomtom.atlassian.net/browse/GOSDK-14374?src=confmacro) |     |     |     | Feature |
| HOV lane improvements | HOV improvements |     | [GOSDK-16152](https://tomtom.atlassian.net/browse/GOSDK-16152?src=confmacro) |     |     |     | Improvement bucket ![(question)](images/icons/emoticons/help_16.png) |
| Ambiguous Turns handling | Refactor turn instructions to integrate ambiguous scenarios | [NIE_011 - Turn manoeuvres overview](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157679963/NIE_011+-+Turn+manoeuvres+overview) |     |     | 4   | Very relevant |     |
| Reflecting intersection geometry  <br>in maneuver arrow (different fork geometries) | Support alternative exits in manoeuvre arrow. exits should look greyed out. Design has to define which exits should be shown and which not. | In NIP examples in [NIE_011 - Turn manoeuvres overview](https://tomtom.atlassian.net/wiki/spaces/FlaminGO/pages/157679963/NIE_011+-+Turn+manoeuvres+overview) | [NAV-54312](https://tomtom.atlassian.net/browse/NAV-54312?src=confmacro)  | L   | 4   | Yes, still very relevant |     |
| Resolve ambiguity on close/nearby turns | Only on highways implemented (take the second) | * UX task created in epic | [NAV-53024](https://tomtom.atlassian.net/browse/NAV-53024?src=confmacro)  | M   | 4   | Yes, still very relevant |     |
| Landmark guidance improvements | End of road |     | [NAV-62523](https://tomtom.atlassian.net/browse/NAV-62523?src=confmacro)  |     | 3   |     |     |
| Trifurcations | Adds support for Trifurcation in NIE | With and without lane info | [NAV-69908](https://tomtom.atlassian.net/browse/NAV-69908?src=confmacro) |     |     | Yes, still very relevant | [NAV-131753](https://tomtom.atlassian.net/browse/NAV-131753?src=confmacro)  |
| Removing road names from trivial audio instructions | Simple instructions like turn right at a junction which allows only one turn right do not require mentioning road name. | [Isolated turn](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Instructions/Turn%20Instructions/Isolated%20turn%20%20/Isolated_turn.md) | ???? | S   | 4   | I could be done already... not sure. |     |
| Continue straight instruction | This needs to be validated against the specs. This instruction should not be selected based on "natural continuation" logic, but rather on use cases defined in the spec. | [Continue Straight](https://github.com/tomtom-internal/nie-ux-spec/blob/main/Instructions/Turn%20Instructions/Continue%20Straight%20%20/Continue_Straight.md) | [NAV-93550](https://tomtom.atlassian.net/browse/NAV-93550?src=confmacro) | S   | 5   | I could be done already... not sure. |     |
| Natural continuation on curved segments | Current NC methods fail at curved intersections when main road curves. This is because NC is primarily based on angles. Preliminary work has been done by [Maksym Osadchuk](https://tomtom.atlassian.net/wiki/people/712020:fb261b5b-de23-442e-854b-8b08f3e29b6f?ref=confluence) |     | [NAV-131950](https://tomtom.atlassian.net/browse/NAV-131950?src=confmacro) | ?   | 5   | Newly discovered. Very relevant |     |



Recent Issues - bugs
====================

The issues collected her are most recently discovered during drive tests

| Topic | Description | Ticket | Size | Value (1..5 highest) | 
| --- | --- | --- | --- | --- |
| Incorrect usage of U-turn when two successive turns are required | There are some types of geometry (usually at plural Junctions) where NIE decides to use U-turn while two successive turns should be rather used. This happens when performing a turn to a parallel road. U-turns should only be used when we stay on the same road, not parallel one. | [NAV-129839](https://tomtom.atlassian.net/browse/NAV-129839?src=confmacro)  | ?   | 3   |
| Next manoeuvre is announced during current manoeuvre. | When performing any manoeuvre that takes some time to complete, like a turn via curved path, the next instruction is announced during the manoeuvre and not after that. Next instruction should only be announced when driver has nothing to do. | [NAV-128144](https://tomtom.atlassian.net/browse/NAV-128144?src=confmacro)  | M   | 4   |
| Follow the Road Instruction fix | "Follow the road for XXkm" instruction shows next instruction arrow (exit) and corresponding to it data.   <br>The instruction appears too early, before the driver has reached the road. | [NAV-128147](https://tomtom.atlassian.net/browse/NAV-128147?src=confmacro)  | S   | 3   |
| 1.1km is announced instead of 1km | The issue is identified as a side effect of "time-based" triggering mechanism. | [NAV-128155](https://tomtom.atlassian.net/browse/NAV-128155?src=confmacro)  | M   | 5   |
| Incorrect usage of Road numbers on non-Motorways | Road numbers are used as main identity, while road names should be used | [NAV-129830](https://tomtom.atlassian.net/browse/NAV-129830?src=confmacro)  | S   | 3   |




 










/ END OF DOCUMENT




