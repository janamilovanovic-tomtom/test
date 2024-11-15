| **Interaction Designer** | [Alexey Opokin](https://tomtom.atlassian.net/wiki/people/70121:e8cb7861-9079-4b92-b96d-bfe8cd882680?ref=confluence) |
|---|---|
| **User Research Support** | [Harry Haladjian](https://tomtom.atlassian.net/wiki/people/70121:959a5e6c-c2bf-440b-ac34-ae6504265652?ref=confluence) |
| **Amigo Support** | [Kersti Rimmeld](https://tomtom.atlassian.net/wiki/people/70121:1b18439d-4aab-430a-833e-3e2722e76c0e?ref=confluence) |
| PM | [Joost Pennings](https://tomtom.atlassian.net/wiki/people/712020:a6d50cb1-97be-4a9a-a279-3fbb3e2e1799?ref=confluence) |

  

Table of Contents
=================

*   [Table of Contents](#Table-of-Contents)
*   [Need to Full Guidance-dedicated user testing](#Need-to-Full-Guidance-dedicated-user-testing)
*   [Moderated Drive Test](#Moderated-Drive-Test)
    *   [Requirements for Drive Test](#Requirements-for-Drive-Test)
*   [Questions to be answered](#Questions-to-be-answered)
*   [Analytics based test (unmoderated)](#Analytics-based-test-unmoderated)
    *   [Requirements for Analytics](#Requirements-for-Analytics)
    *   [Questionary for Analytics](#Questionary-for-Analytics)
*   [Competition benchmark (Internal)](#Competition-benchmark-Internal)
*   [Target System status](#Target-System-status)

Need to Full Guidance-dedicated user testing
============================================

NIE is a new navigation design that must be tested not only by internal team, but by real users. This is nessasary to ensure the performance one new system and measuring how it stacks up with the older (NK1) and competition. The purpose of this page is to set up a requirements of such testing, consolidate all related information and eventually, to capture the results. There are 3 types of Testing that can be done in parellel:  
  
**1\. Moderated driving test**  
**2\. Analytics based unmoderated test including questionary.**  
**3\. Internal benchmark against competition and NK1.**

  

  
Moderated Drive Test
=======================

This type of User test requires setting up a moderated driving sessions alongs predefined and persistent routes. During such tests moderator can capture user's problems and difficulties, even if driver himself is not reflection on those. This makes it extremely effective course of information. Additionally, driving along the same route with multiple people could reveal consistent issues.

Requirements for Drive Test
---------------------------

Following requirements are known at this point in time.

| Type of test | Users | Platforms | Regions coverage                                                                                            | Duration | Route requirements | Manoeuvres                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---|---|---|-------------------------------------------------------------------------------------------------------------|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Moderated driving: Users will drive along predefined route while being observed by moderator. | Car drivers of various ages. Quantity: 5\-10 | Amigo (Car play mode)Automotive UI (Later) | EU, US, APAC(Japan)  <br><br>  NOTE: For the first round, the easies location can be selected (Netherlands) | 1\-2 hours | Must include: Urban areas, Rural, Motorways | Roundabouts, <br> Big Roundabouts, <br> Motorway Forks and exits,<br>  Multi\-lane(\&gt;5\) roads , <br> Complex Intersections (Urban),<br>  Ambiguous Turns/Bears (Urban), <br> Double Exits (Motorways), <br> Chain instruction in quick succession,<br>  Tunnels,<br>  Follow the road for XX km,  <br>Mandatory turns, <br> Turning Left?Right on multi\-Lane(\>5\) Junction  Continuation straight on multi\-lane(\>5\) junction,<br>  HOV (in US)  Michigan Left (in US) |

  

  

Questions to be answered
========================

Following questions are known at this point in time.

| High Level Questions |  |
|---|---|
| How many Route deviations happened? Caused by? |  |
| How many ambiguous situations happened? Caused by? |  |
| Specific Questions |  |
| How well any of the mentioned Maneuvre types handled? i.e Roundabouts, Highway forks, etc |  |
| How SLG performs on Highways? |  |
|  |  |

  

  

Analytics based test (unmoderated)
==================================

This type of test is a constant evaluation of the product on real users. It doesn't need to be performed, but require initial setup (analytics) and data analysis system in place. At the moment this type of test could be set up on Amigo platform.

  

Requirements for Analytics
--------------------------

Following events should be captured by the analytics system.

| Type of event | Description |
|---|---|
| Route deviation | Not following the route |
| Slow speed in the absence of traffic | Speed below reasonable in the area without traffic. |
| Stops at intersection | vehicle stops before road splits (fork) |
| Audio ON/OFF | State of the Audio Guidance switch |

Questionary for Analytics
-------------------------

Following questions could be asked by the analytics system after completion of a route.

| Questions |  |
|---|---|
| How people rate Guidance experience compared to other navigation system they are familiar with (Apple Maps, Google Maps, Waze)? |  |
| What TT system does better? |  |
| What competitors system does better? |  |
| What problems have been encountered during drive? |  |

  

  

  

  

Competition benchmark (Internal)
================================

This type of test could be done internally, bu designers, user researcher, developers. Th purpose of this test is to capture advantages/disadvantages of NIE compared to other navigation systems. It could be setup with dual navigation device and session should be recorded and analysed later.

  

Following questions could be answered by this test

| High Level Questions |  |
|---|---|
| How good/bad NIE Guidance experience compared to NK1? |  |
| How good/bad NIE Guidance experience compared to Apple Maps? |  |
| How good/bad NIE Guidance experience compared to Waze? |  |
| How good/bad NIE Guidance experience compared to Google Maps? |  |
| What NIE does better? |  |
| What Competition does better? |  |

  

  

Target System status
====================

Before testing we need to ensure that target system is running the most uptodate version of NIE and all facilities are implemented. This table lists all important NIE components and their readiness status on Amigo platform.  
  
**Amigo NIE Readiness state**

| Facility | Status |  |
|---|---|---|
| NIE Triggering logic | v |  |
| NIE Instructions set | v |  |
| NIE Audio | v |  |
| SLG | v |  |
| Audio for SLG | ? |  |