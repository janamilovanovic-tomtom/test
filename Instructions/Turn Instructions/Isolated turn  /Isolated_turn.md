  

![](images/157696057.png)

  

| **Interaction Designer** | [User 3d941](https://tomtom.atlassian.net/wiki/people/712020:73555e9b-dcfa-442b-80ec-98ad0ea3d941?ref=confluence) |
|---|---|
| **Visual Designer** | [Georgios Koultouridis](https://tomtom.atlassian.net/wiki/people/5be2fd44649a737c2342afbe?ref=confluence) |
| PM |  |

  

Table of Contents
=================

*   [Table of Contents](#Table-of-Contents)
    *   [General goal](#General-goal)
    *   [Specific goal](#Specific-goal)
    *   [What is Isolated turn?](#What-is-Isolated-turn)
    *   [Conditions for Isolated turn](#Conditions-for-Isolated-turn)
    *   [Examples](#Examples)

  

  

**General goal**
----------------

Make audio annoucements more digestible

**Specific goal**
-----------------

Reduce the details of the audio announcement (street name + Towards) on _Isolated turn_ for Early and Main phase audio triggering logic

**What is Isolated turn?**
--------------------------

Isolated turn is a road network scenario where there are no intermediate turns between the driver and the target manoeuvre.

It can be conceptualise as an 'obvious turn' and this why audio announcement can be simplified.

**Conditions for Isolated turn**
--------------------------------

*   this applies to all road types except for controlled access roads  
    
*   there are not intermediate turns between the driver and the target manoeuvre
*   or there are intermediate turns but the distance between the first turn and the target turn is &gt;= 100m

When these conditions are true, the system will not announce:

*   street name
*   towards information 

**Examples**
------------

Take a look at a real scenario **[here](https://www.google.de/maps/dir/52.4995286,13.4814377/52.4981261,13.4830352/@52.4988863,13.4822696,18.71z/data=!4m9!4m8!1m5!3m4!1m2!1d13.4813768!2d52.4994665!3s0x47a84ee6780e9325:0x980c4cbc8700444e!1m0!3e2)** (Google Maps)

  

**No Intermediate turn**

*   You are driving on a long-straight road and you need to turn right
*   There are no other turns in between you and the turn  
    

  

  

![](images/157696059.png)

  

**Intermediate turn**

*   You are driving on a long-straight road and you need to turn right
*   there are intermediate turns but the distance between the first turn and the target turn is &gt;= 100m

  

  

![](images/157696062.png)