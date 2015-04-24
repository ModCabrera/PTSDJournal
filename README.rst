============
PTSD Journal
============

Personas:
=========

Sergeant McGee
--------------

Persona: McGee suffers from Post Traumatic Stress and is attending therapy at the local Veterans Administration Hospital after his Honorable Discharge.

Details: McGee is  a Post-911 combat war veteran of Afghanistan and Iraq. He led hundreds of patrols where he endured hazardous environments and constant firefights.

Goals: McGee wants to reintegrate into civilian life, but his separation doctors have advised him to participate in therapy led by a medical team to alleviate the issues that have made him angry over the past couple of months. 

Medical Team [Mike, Hannah]
---------------------------

Hannah - Medical Team Psychologist

Persona: Hannah is a psychologist and an expert in Post Traumatic Stress Disorder.

Details: Hannah has many patients and is unable to keep track of their progress between therapy sessions. She currently has patients write in notebooks but they always neglect to bring them to appointments.

Goals: Being able to automate the process by having patients log their moods and activities in a journal which she can quickly sort through to see of any alerting conditions between sessions. Also, to implement a formulated grounding techniques questionnaire before logging daily activities. 

Mike - Medical Team Patient Counselor

Persona: Mike is a counselor in the Medical Team, he works side by side with Hannah and the patients. Mike enjoys helping fellow veterans and as a volunteer is in constant communication with patients and progress.

Details: Mike helps patients between therapy or group sessions. He is concerned patients don't return because they isolate themselves. He wants to help patients feel comfortable about reaching out and speaking to him. He has no way of knowing when patients are not doing well. 

Goals: To keep and updated record of patients contact information, and a log of their progress to provide better suited services.


Problem Scenarios:
==================

McGee
-----

Problem Scenario: McGee forgets his notes and forgets to tell his doctor Hannah about the bad days between sessions.

Current Alternative: McGee has to recollect his moods and sometimes neglects to mention days because he doesn't want to remember them.

Value Proposition: A software that allows McGee to use his personal computer or provided tablet to input his mood and log a message he would like to share with Hannah and Mike about his day to improve the therapy sessions.

Medical Team (Hannah, Mike)
---------------------------

Problem Scenario: Hannah has unproductive therapy sessions because her patients neglect to bring journal of recorded moods between their sessions and Mike is unable to communicate with patients about potential services that can benefit their overall well-being.

Current Alternative: Hannah has patients quickly recap their main concerns briefly and if serious matters arise, she schedules another session. Hannah often re-schedules other patients because more serious matters arise, causing other patients to leave and not return for therapy.

Value Proposition: A software that allow patients to log their moods and daily events with grounding techniques to deter lapses in patients sessions. Since the journal is virtually submitted, patients don't need to remember to bring extra materials to therapy. The Team is able to observe progress and prepare for future events with more time for preparation.


User Stories:
=============


Self Observation - Reflection
-----------------------------

As Drill Sergeant McGee, I want to record my daily activities, and answer questions about grounding techniques
so that I can provide my medical team a better understanding of what my current mental health medical needs are.

Medical Progression Log
-----------------------

As The Medical Team Hannah and Mike, we want to record daily activites of patients, and have them answer formulated questions about
grounding techniques so that we can monitor patient progress, suit their needs better and deter situations where
a patient may be in danger of relapsing. 


Acceptance Stories:
^^^^^^^^^^^^^^^^^^^

Log Journal for w/ bad mood
``````````````````````````````````````

::

    Given that I want to write in my journal today
        And click on PTSD Journal Icon
        ...
    When I finish writing in journal for the day
    Then answer my doctor’s grounding technique questions
        And I’ve rated my overall mood below 5
	And I receive a suggestion to call Mike or the Hotline
	  And I am able to view a list of dates with logged entries and preview Journal text and mood rating number
        …

Log Journal w/ good mood
````````````````````````````````````

::

    Given that I want to write in my journal today
        And click on PTSD Journal Icon
        ...
    When I finish writing in journal for the day
    Then answer my doctor’s grounding technique questions
        And I’ve rated my overall mood above 5
	And I am able to view a list of
	And I click <Esc> so the Journal automatically closes. 
        …

Log Journal Average of Mood
```````````````````````````````````````

::

    Given that I want to write in my journal today
        And click on PTSD Journal Icon
        ...
    When I Click <Ctrl-A>
    Then view list of journal entries
        And I click <Ctrl-M>
	And I am able to view Doctor Hannah’s Comments and average mood rating/progress report. 
        …

