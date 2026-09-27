HEALTHMATE
AI-Assisted Personalized Health Monitoring and Wellness Management System
Project Proposal
Your family's health, in one place.

HealthMate: Project Proposal Part 1: Project Planning and Definition
Table of Contents
1. Project Overview ..................................................................................................................................... 3
2. Background and Real-World Context ....................................................................................................... 3
2.1 Background ..................................................................................................................................................... 3
2.2 Market Context ............................................................................................................................................... 3
3. Problem Statement ................................................................................................................................. 4
4. Existing Solution Gap ............................................................................................................................... 5
4.1 Common Approaches and Their Limitations ................................................................................................... 5
4.2 Competitor Capability Comparison ................................................................................................................. 6
5. Product Positioning and Differentiation ................................................................................................... 7
5.1 Why HealthMate Is Different .......................................................................................................................... 7
5.2 Positioning Statement .................................................................................................................................... 7
5.3 Market Entry Strategy ..................................................................................................................................... 7
6. Proposed Solution ................................................................................................................................... 8
6.1 Core Workflow ................................................................................................................................................ 8
6.2 Conceptual Architecture ................................................................................................................................. 8
6.3 Alert Severity Model ....................................................................................................................................... 9
6.4 Data Entry Strategy ......................................................................................................................................... 9
7. Intelligent System Strategy .................................................................................................................... 10
8. Target Users and Stakeholders .............................................................................................................. 11
8.1 Target Users .................................................................................................................................................. 11
8.2 Stakeholders ................................................................................................................................................. 11
9. Use-Case Scenarios ................................................................................................................................ 12
10. Project Objectives ............................................................................................................................... 13
10.1 General Objective ....................................................................................................................................... 13
10.2 Specific Objectives ...................................................................................................................................... 13
11. Scope and Boundaries ......................................................................................................................... 14
11.1 Initial Capstone MVP .................................................................................................................................. 14
11.2 Planned Enhancements (Time Permitting) ................................................................................................. 14
11.3 Future Scope ............................................................................................................................................... 14
12. Project Boundary, Safety and Regulatory Considerations ..................................................................... 14
12.1 The System Will and Will Not ..................................................................................................................... 15
12.2 Security and Privacy Framework ................................................................................................................. 15
12.3 Regulatory Considerations .......................................................................................................................... 15
13. Requirements Analysis ........................................................................................................................ 16
13.1 Functional Requirements (Summary) ......................................................................................................... 16
13.2 Non-Functional Requirements .................................................................................................................... 16
13.3 Feature-to-Problem Mapping ..................................................................................................................... 17
14. Feasibility Analysis .............................................................................................................................. 19
14.1 Feasibility Assessment ................................................................................................................................ 19
14.2 What Is Implemented Now and What Remains Future .............................................................................. 19
15. Development Methodology ................................................................................................................. 20
16. Resource, Time and Budget Planning ................................................................................................... 20
16.1 Resources .................................................................................................................................................... 21
16.2 Time Plan .................................................................................................................................................... 21
16.3 Budget Approach ........................................................................................................................................ 21
Department of Software Engineering, Daffodil International University Page 1

HealthMate: Project Proposal Part 1: Project Planning and Definition
17. Risk Analysis ........................................................................................................................................ 22
18. Scalability and Product Vision .............................................................................................................. 23
18.1 Roadmap ..................................................................................................................................................... 23
18.2 Architectural Provisions for Scale ............................................................................................................... 23
18.3 Business Model Outline (Vision) ................................................................................................................. 24
19. Expected Value and Impact ................................................................................................................. 24
19.1 Individual User Value .................................................................................................................................. 24
19.2 Family Value ................................................................................................................................................ 24
19.3 Healthcare Interaction Value ...................................................................................................................... 24
19.4 Product Value ............................................................................................................................................. 25
20. Part 1 Conclusion ................................................................................................................................. 25
References ................................................................................................................................................ 25
Appendix A: Detailed Functional Requirements ........................................................................................ 27
A.1 Account and Access Management ............................................................................................................... 27
A.2 Health Profile ................................................................................................................................................ 27
A.3 Health Data Recording .................................................................................................................................. 27
A.4 Dashboard, Trends and Alerts ...................................................................................................................... 28
A.5 Personalized Guidance ................................................................................................................................. 28
A.6 AI Health Assistant and Navigation .............................................................................................................. 28
A.7 Family Monitoring and Permissions ............................................................................................................. 28
A.8 Emergency-Aware Escalation ....................................................................................................................... 29
A.9 Consultation Support (Enhancements) ........................................................................................................ 29
A.10 Localization ................................................................................................................................................. 29
Appendix B: Requirements Traceability ..................................................................................................... 30
Appendix C: Glossary ................................................................................................................................. 30
Department of Software Engineering, Daffodil International University Page 2

HealthMate: Project Proposal Part 1: Project Planning and Definition
PART A
THE PROBLEM
1. Project Overview
HealthMate is a personalized health companion rather than an AI doctor. It organizes relevant health and
wellness information, analyzes personal trends, provides context-aware guidance, identifies potentially
unusual patterns, and connects users with trusted family or healthcare support when appropriate.
The product philosophy is simple: health information should not remain passive data. Where appropriate, it
should be converted into understandable information, timely reminders and responsible next-step guidance.
Vision. To become the daily health companion for Bangladeshi families, helping people understand their
own health and stay connected to the health of the people they love.
Terminology. This proposal describes HealthMate as a health and wellness companion. The term "medical
assistant" is deliberately avoided because it implies clinical decision-making, which is outside the product's
boundary (Section 12).
2. Background and Real-World Context
This section sets out the real-world context, and the market it sits in, before Section 3 states the specific
problems that follow from it.
2.1 Background
Users increasingly obtain health-related information from several sources: manual records, smartphones,
fitness applications, wearable devices and home-monitoring equipment. Access to data does not mean that
users understand what individual measurements mean in relation to their own long-term patterns. A person
may know today's blood pressure yet fail to notice a gradual rise over several weeks.
Health information also becomes fragmented across applications, devices and paper records, and family
context is rarely connected to personal monitoring. The challenge is greater when elderly family members
need additional attention while their children or caregivers live separately.
HealthMate addresses this context by bringing personal monitoring, family health history, lifestyle tracking,
longitudinal analysis, personalized guidance, elderly monitoring, healthcare navigation and emergency-
aware support into one platform.
2.2 Market Context
The figures below come from public sources listed in the References section and were accessed on
September 20, 2026. Several are provisional or are news reports of official data, so the original publications
should be consulted for final citation.
Department of Software Engineering, Daffodil International University Page 3

HealthMate: Project Proposal Part 1: Project Planning and Definition
Indicator Value Source
Population aged 60 and above About 15.3 million people, around 9.28% of the population (Census [1]
2022), up from 7.48% in 2011. UNFPA projects about 36 million by 2050
Internet users 77.7 million users, 44.5% of the population (January 2025) [2]
Bangladeshi workers going abroad 1,130,757 workers migrated for employment in 2025 (up from [3], [4]
1,011,969 in 2024). BMET data reported by the press indicates more
than 13 million have gone abroad since 1976
Remittance inflow US$35.56 billion in FY2025-26 (provisional), up 17.3% from US$30.32 [5]
billion the previous year
Hypertension among adults (18+) 27.4% crude prevalence (BDHS 2017-18). Only 42.5% of those affected [6]
were aware of it, and 37.0% were on treatment
Diabetes among adults (20-79) 13.9 million adults, 13.2% age-standardised prevalence (2024), of whom [7]
39.1% are undiagnosed. Projected 23.1 million by 2050
Local digital health apps Telemedicine apps already have sizable user bases (for example, [8]
Sebaghar reported over 500,000 downloads in 2024) but focus on
consultations, appointments and medicine delivery
These figures point to three conclusions. First, a large and growing older population, with high rates of
hypertension and diabetes that are often undiagnosed or poorly controlled, creates a real need for routine
monitoring and early awareness. Second, a very large number of Bangladeshis work abroad and send money
home, and many have parents living in Bangladesh, which is the situation the family-alert feature is designed
for. Third, existing local apps concentrate on booking and consultation rather than continuous monitoring
with family-aware alerts.
Market sizing approach. The total addressable market (TAM) is internet-using adults in Bangladesh (77.7
million users [2]). The serviceable market (SAM) is smartphone users who are, or have parents who are, aged
40 and above. The obtainable market (SOM) is the first-year adoption within the launch segment (Section
5.3), to be set after user interviews and a pilot.
3. Problem Statement
Building on this context, the problems below are the specific pain points HealthMate is designed to solve.
Each is assigned an ID so that it can be traced to objectives, requirements, design components and test cases
in later parts and in Appendix B.
ID Problem HealthMate response
P-01 Fragmented health information. Users obtain Centralized personal health profile and longitudinal
information from different sources, making it hard to health timeline.
keep a unified view of their health.
P-02 Limited personalization. Many systems display Context-aware personalized wellness guidance.
measurements without considering age, lifestyle, goals,
previous patterns or family context.
P-03 Difficulty recognizing gradual changes. A single Historical analysis and comparison with the user's
measurement may not reveal a meaningful long-term established pattern.
change.
P-04 Disconnected family health context. Relevant family Family history used as a contextual factor for health
history may be forgotten or unused in personal awareness.
monitoring.
Department of Software Engineering, Daffodil International University Page 4

HealthMate: Project Proposal Part 1: Project Planning and Definition
ID Problem HealthMate response
P-05 Difficulty maintaining healthy habits. General advice is Context-aware reminders for hydration, sleep, activity
easy to ignore when it is not connected to actual and wellness goals.
behavior.
P-06 Elderly monitoring gap. Families have difficulty Consent-based caregiver alerts for selected events.
monitoring older relatives who live separately.
P-07 Uncertainty about professional care. Users may not General healthcare-navigation guidance without
know when to seek advice or which specialist category diagnosis.
is appropriate.
P-08 Emergency communication gap. A sudden incident is User verification, emergency-contact notification and
harder to manage when the affected person cannot authorized location sharing where supported.
respond, for example while travelling.
P-09 Poor preparation for consultations. Patients forget Health timeline and doctor-visit summary.
recent measurements and symptoms.
4. Existing Solution Gap
Before presenting HealthMate's own solution in Part B, this section checks whether existing tools already
solve the nine problems above.
Digital-health technologies make personal health tracking and wearable monitoring feasible, but users may
still face fragmented information, limited personalization, difficulty translating measurements into action,
privacy concerns and limited family-centered support. HealthMate focuses on the gap between health-data
collection and meaningful health action.
4.1 Common Approaches and Their Limitations
Existing approach Common limitation HealthMate direction
Fitness and health Strong tracking, but broader context may be Connect measurements with personal, family and
trackers limited lifestyle context
Separate health apps Information can remain fragmented Centralized personal health profile and longitudinal
view
Generic health May not reflect individual patterns or goals Context-aware personalized wellness notifications
advice
Manual family Often reactive and dependent on direct Consent-based caregiver alerts
checking communication
General AI assistants May lack structured longitudinal user Controlled AI interaction grounded in available
context HealthMate data
Department of Software Engineering, Daffodil International University Page 5

HealthMate: Project Proposal  Part 1: Project Planning and Definition
4.2 Competitor Capability Comparison
Fitness apps
Local health apps
|             | Apple Health /  | (e.g.,  | General AI  |     |             |
| ----------- | --------------- | ------- | ----------- | --- | ----------- |
| Capability  |                 |         |             |     | HealthMate  |
(e.g., Sebaghar,
|     | Google Health  | Samsung  | chatbots  |     |     |
| --- | -------------- | -------- | --------- | --- | --- |
LifePlus, Zaynax)
Health)
|     | Yes  | Yes  | No  | Partial  | Yes  |
| --- | ---- | ---- | --- | -------- | ---- |
Personal measurement
tracking
|     | Partial  | Partial  | No  | Limited  | Yes  |
| --- | -------- | -------- | --- | -------- | ---- |
Long-term trend
analysis
| Uses family health  | No  | No  | Only if re-   | Limited  | Yes  |
| ------------------- | --- | --- | ------------- | -------- | ---- |
| history             |     |     | entered each  |          |      |
time
Consent-based family  Partial (tied to one  Limited  No  None identified  Yes (core
| alerts  | device ecosystem)  |              |     |          | feature)  |
| ------- | ------------------ | ------------ | --- | -------- | --------- |
|         | Not a focus        | Not a focus  | No  | Limited  | Yes       |
Elderly-friendly
simplified experience
|     | Limited  | Limited  | Partial  | Varies  | Yes  |
| --- | -------- | -------- | -------- | ------- | ---- |
Bangla-language
support
| Conversational       | No               | No       | Not with    | Limited  | Yes            |
| -------------------- | ---------------- | -------- | ----------- | -------- | -------------- |
| assistant using the  |                  |          | persistent  |          |                |
| user's own records   |                  |          | records     |          |                |
|                      |                  | Limited  | No          | Limited  |                |
| Emergency contact    | Limited (device- |          |             |          | Yes (basic in  |
| escalation workflow  | dependent)       |          |             |          | MVP)           |
|                      | No               | No       | No          | Yes      |                |
| Doctor consultation  |                  |          |             |          | No (out of     |
| and e-prescription   |                  |          |             |          | scope)         |

Google announced in May 2026 that Google Fit is being retired and replaced by the Google Health app,
which also replaces the Fitbit app [9]. Feature sets change quickly, so this comparison reflects the sources
reviewed on September 20, 2026.
No existing option in this comparison combines personalized, longitudinal, family-aware and safety-bounded
guidance in one Bangla-friendly product. This is the gap Part B addresses.
Department of Software Engineering, Daffodil International University  Page 6

HealthMate: Project Proposal Part 1: Project Planning and Definition
PART B
THE SOLUTION
5. Product Positioning and Differentiation
The gap identified in Section 4 sets the bar HealthMate must clear. Before the detailed solution is presented
in Section 6, this section states in one place what makes HealthMate different and how it will reach its first
users.
5.1 Why HealthMate Is Different
HealthMate's advantage is not a single feature. It is the combination of personal context, family awareness
and safe guidance in one system that the existing options do not provide together.
Dimension Typical alternative HealthMate
Personalized rather than generic The same advice for every user Guidance based on profile, goals, lifestyle and
family context
Longitudinal rather than single- Shows the latest measurement Compares readings with the user's own baseline
reading and long-term trend
Family-aware Data stays with one user Consent-based family and caregiver alerts, and
family-assisted entry
Supportive of older adults Complex interface, English only Simple Bangla and English interface, accessibility
mode, caregiver support
Alert, guidance and navigation in Separate tracker, chatbot and One flow from measurement to alert to next-
one system booking apps step guidance
Safety-bounded Unrestricted advice Explainable rule-based alerts, constrained AI, no
diagnosis
HealthMate supports older adults as one important design principle, but it is built for the whole family:
adults tracking their own health, older parents, and the relatives who care for them.
5.2 Positioning Statement
For individuals and families who want to understand and support their health, HealthMate is a health and
wellness companion that turns everyday measurements into personalized guidance and family-aware alerts.
Unlike general fitness trackers and general-purpose AI chatbots, HealthMate connects personal history,
family context and consent-based family support in one Bangla-friendly platform.
5.3 Market Entry Strategy
A broad vision needs a focused entry point. The proposed sequence is:
Department of Software Engineering, Daffodil International University Page 7

HealthMate: Project Proposal Part 1: Project Planning and Definition
Stage Segment Rationale
Stage 1 (capstone MVP Adults with parents or relatives who require Clear pain, strong motivation to adopt, clear
and pilot) health monitoring, including families separated value from family alerts
by distance
Stage 2 Individuals with hypertension, diabetes or Regular data entry, high retention potential
other conditions requiring routine monitoring
Stage 3 General adult population seeking daily Broader market once trust and usage are
wellness support established
6. Proposed Solution
With differentiation and market entry established, this section describes how HealthMate actually works.
HealthMate collects or receives user-provided health and lifestyle information, organizes it into a
longitudinal profile, analyzes patterns, and generates appropriate wellness guidance and alerts.
6.1 Core Workflow
Personal Information + Family Health History + Health Measurements
+ Lifestyle Data + Historical Records
↓
HealthMate Analysis Engine
↓
Trend Analysis + Personalized Wellness + Abnormal-Pattern Awareness
↓
User Guidance + Family Alerts + Healthcare Navigation
6.2 Conceptual Architecture
The figure shows the conceptual structure of the system. Users provide or share data, an analysis layer
interprets it, and an action layer turns the result into alerts, guidance or an escalation workflow, all under
cross-cutting security and privacy controls. Part 2 presents the detailed architecture.
Department of Software Engineering, Daffodil International University Page 8

HealthMate: Project Proposal  Part 1: Project Planning and Definition

Figure 1. Conceptual architecture of HealthMate. Dashed border marks an optional component.
6.3 Alert Severity Model
HealthMate uses five alert levels. Severity is decided by predefined rules, and the recipients are decided by
the user's consent settings.
| Level  Name  | Typical trigger  | System behavior  | Recipients  |
| ------------ | ---------------- | ---------------- | ----------- |
0  Normal  Reading and behavior within the  No alert. Positive feedback where  User
|     | user's expected pattern  | relevant  |     |
| --- | ------------------------ | --------- | --- |
1  Wellness  Routine lapse or goal reminder  Friendly, personalized nudge  User
| Reminder  | (hydration, sleep, activity, missed  |     |     |
| --------- | ------------------------------------ | --- | --- |
reading)
2  Attention  Minor deviation from the  In-app notification with a non- User
|     | personal baseline  | diagnostic message  |     |
| --- | ------------------ | ------------------- | --- |
3  Concern  Significant or persistent  Notification with a suggestion to  User and authorized
deviation, or an out-of-range  consult a professional. Family  family or caregiver
|     | reading  | alert if authorized  |     |
| --- | -------- | -------------------- | --- |
4  Emergency  Critical reading or reported  Verification prompt, then  User, then emergency
| escalation  |                              |                                  | contacts  |
| ----------- | ---------------------------- | -------------------------------- | --------- |
|             | symptom, unanswered safety   | emergency-contact notification,  |           |
|             | check-in, or manual trigger  | with location if authorized      |           |

Emergency principle. HealthMate does not clinically determine an emergency. It detects predefined
abnormal signals or events and initiates a configured escalation workflow.
6.4 Data Entry Strategy
Manual data entry is a known adoption risk, particularly for older adults. The product addresses it through:
Department of Software Engineering, Daffodil International University  Page 9

HealthMate: Project Proposal Part 1: Project Planning and Definition
• quick-entry interfaces requiring the fewest possible taps;
• scheduled reminders at the user's preferred times;
• family-assisted entry, where an authorized caregiver records readings on behalf of an older adult; and
• optional import from devices and wearables in future versions.
7. Intelligent System Strategy
The architecture in Section 6.2 referred to an analysis layer with several components. This section states
exactly which of them use artificial intelligence, and which do not, so that the design remains explainable.
HealthMate does not use AI as a project label. Each component is selected according to the problem it is
intended to solve, and explainable methods are preferred. The processing pipeline runs from rule-based
logic, to statistical analysis, to anomaly detection, to the recommendation engine, and finally to the
language-model assistant.
Component Category Approach Role in HealthMate
Rule-based alert Conventional logic Configurable thresholds derived Classifies readings into alert
engine (MVP core) from published clinical guidance levels from the first entry. Every
and reviewed by a qualified alert can state the rule that
healthcare professional before triggered it
deployment
Statistical trend Statistics Moving averages, rate of change Reveals gradual changes. Works
analysis (MVP core) and deviation from the personal with a small amount of data
baseline
Anomaly detection Machine learning A method such as Isolation Flags "unusual compared with
(enhancement) Forest once enough history your recent pattern". Never a
exists, validated on test or diagnosis
synthetic data against the rule-
based baseline
Recommendation Conventional logic, with Rule-based selection from user Personalized reminders that
engine (MVP) optional generative wording context, goals and trends, with remain controllable
optional language-model
rewording
AI health assistant Generative AI (language A language model operating Explains the user's records and
(MVP) model) behind a guardrail layer supports healthcare navigation
Only two of the five components use artificial intelligence: anomaly detection (machine learning, optional)
and the language-model assistant (with optional wording in the recommendation engine). The alert engine,
trend analysis and recommendation selection are conventional software logic and statistics. This separation
keeps the system explainable and makes clear where AI is, and is not, used.
The guardrail layer consists of input classification (for example emergency, diagnosis request or medication
request), constrained prompts, output checks for prohibited content, mandatory disclaimers, and redirection
to emergency help when emergency language is detected. Data sent to any external AI service is minimized
and free of direct identifiers wherever possible.
Department of Software Engineering, Daffodil International University Page 10

HealthMate: Project Proposal  Part 1: Project Planning and Definition

PART C
WHO IT IS FOR

8. Target Users and Stakeholders
Having described what HealthMate does, this section defines who it is for.
8.1 Target Users
| User type  | Description  | Key needs  |     |
| ---------- | ------------ | ---------- | --- |
Primary user (self-managing  Adult who wants to track health, habits and  Simple recording, clear trends, useful
| adult)  | goals  | reminders  |     |
| ------- | ------ | ---------- | --- |
Older adult  Person aged approximately 60 and above,  Large text, Bangla interface, minimal steps,
|     | possibly with chronic conditions  | ability to receive help from family  |     |
| --- | --------------------------------- | ------------------------------------ | --- |
Family member / caregiver
|     | Adult child, relative or caregiver, possibly  | Timely, relevant alerts. No overwhelming  |     |
| --- | --------------------------------------------- | ----------------------------------------- | --- |
|     | living abroad                                 | detail. Clear permission boundaries       |     |
|     | Doctor or nurse                               | Structured health summary                 |     |
Healthcare professional
(secondary, future)
Healthcare ecosystem  Hospitals, telemedicine, device providers,  Standard integration interfaces
| partners (future)  | emergency services  |     |     |
| ------------------ | ------------------- | --- | --- |

Illustrative personas, to be validated through user interviews:
•  Rahim, 32, works in another country. His father, 64, has hypertension and lives in Dhaka. Rahim wants
to know if something changes without calling every day.
•  Mrs. Sultana, 61, measures her blood pressure occasionally, prefers Bangla and is not comfortable
with complex apps.
•  Nabila, 27, wants to improve sleep, hydration and activity, and her family has a history of
hypertension.

8.2 Stakeholders
| Stakeholder  | Role  | Interest  | Influence  |
| ------------ | ----- | --------- | ---------- |
Individual user  Primary user  Understand and improve own  High
health
| Older adult  | Primary user  | Simple, safe monitoring  | High  |
| ------------ | ------------- | ------------------------ | ----- |
Family member / caregiver  Alert recipient  Timely awareness of a relative's  High
health
Project team  Design, development, testing  Deliver a working, well- High
documented system
Project supervisor  Academic guidance and evaluation  Quality, rigor and scope control  High
Department of Software Engineering, Daffodil International University  Page 11

HealthMate: Project Proposal Part 1: Project Planning and Definition
Stakeholder Role Interest Influence
Healthcare professional Potential recipient of summaries Accurate, well-structured Medium
(future) information
Hospital / provider (future) Potential integration partner Referral and data exchange Low (currently)
Emergency services (future) Potential escalation partner Reliable, verified information Low (currently)
Regulators Oversight of health data and health Compliance and safety Medium
software
Future investors / business Funding and scale Market, traction and Medium
partners sustainability (future)
9. Use-Case Scenarios
The scenarios below show the users of Section 8 and the solution of Section 6 working together in practice.
Names are illustrative and will be validated through user interviews.
Scenario Situation How HealthMate helps Key requirements
1. Young user with Nabila, 27, has a family history of Records the family history as FR-10, FR-12, FR-13,
family history hypertension. Her own readings are context, suggests periodic blood- FR-40
normal pressure checks, and sends
reminders about activity, sleep and
hydration. It does not predict disease
2. Elderly parent Mrs. Sultana, 61, lives in Dhaka. Her She records readings with a quick- FR-22, FR-23, FR-60
living alone son Rahim works abroad entry screen, or a caregiver enters to FR-64, FR-66
them. When two days of readings
rise, or a routine check-in is missed,
Rahim receives an alert that shows
only what she has authorized
3. Critical reading An older user records a reading in a The system reaches Level 4, asks the FR-33, FR-70 to FR-
and no response critical range user to confirm their status, and if 75
there is no reply within the set time
notifies the emergency contact, with
the last known location if the user
has authorized it
4. Gradual long- A user's blood pressure rises slowly Trend analysis against the personal FR-31 to FR-33, FR-
term change over six weeks, and every single baseline moves the alert from 52, FR-81
reading looks acceptable Attention to Concern, explains the
change in non-diagnostic language,
and suggests seeing a general
physician. A visit summary can be
prepared
Automatic detection of incidents while a person is travelling or driving is not part of the prototype. It would
require wearable or vehicle data and is listed as future scope (Section 11.3).
Department of Software Engineering, Daffodil International University Page 12

HealthMate: Project Proposal Part 1: Project Planning and Definition
PART D
GOALS, SCOPE AND REQUIREMENTS
10. Project Objectives
The scenarios in Section 9 describe the experience HealthMate should deliver. This section turns that
experience into measurable objectives.
10.1 General Objective
To design and develop an intelligent personalized health monitoring and wellness management system that
helps users understand health patterns, receive personalized wellness guidance, identify potentially unusual
changes, and connect with trusted family or healthcare support when appropriate.
10.2 Specific Objectives
The five objectives below are measurable. The targets are proposed and will be confirmed with the
supervisor together with the testing approach.
ID Objective Measure Target
O-01 Provide fast, easy health recording Acceptance tests of core recording 100% of scenarios pass. Median
for general and older users scenarios, and usability sessions time to record a reading under 30
with at least 8 participants seconds. At least 85% task
completion and a SUS score of at
least 70
O-02 Detect meaningful trends and Trend and rule-engine outputs 100% of defined test cases match
unusual readings, assign the correct checked against reference test the expected result. Reminders
alert level, and provide cases (Levels 0 to 4), and reminders correct across at least 10 profile
personalized reminders checked across defined user profiles scenarios
O-03 Provide a safe AI assistant Safety test set, for example 100% of prohibited requests receive
requests for diagnosis or a safe redirect
medication changes
O-04 Provide consent-based family alerts Access-control tests, and 0 unauthorized disclosures.
and a basic emergency workflow emergency scenario tests Escalation completes in all defined
(verification, then contact scenarios
notification)
O-05 Protect sensitive data and stay Security review, documented No critical or high-severity findings
modular for future integrations interfaces and a simulated device open. Each engine replaceable
feed without changing the others. One
simulated feed accepted through
the interface
Department of Software Engineering, Daffodil International University Page 13

HealthMate: Project Proposal Part 1: Project Planning and Definition
11. Scope and Boundaries
Not every capability that supports these objectives can be built in one semester. This section defines what is,
and is not, part of the capstone MVP.
11.1 Initial Capstone MVP
• User registration, authentication and profile management
• Personal health profile and family health history
• Health-data recording, dashboard and historical records
• Trend analysis and rule-based alerts with alert levels
• Personalized wellness reminders and recommendations
• AI health assistant with safety guardrails
• Symptom-based healthcare navigation (category of professional only)
• Elderly monitoring, family and caregiver authorization, family alerts and family-assisted entry
• Privacy and permission management, and audit logging
• Basic emergency-aware escalation workflow (user verification and emergency-contact notification)
• Bangla and English interface for core screens
• System testing and evaluation
11.2 Planned Enhancements (Time Permitting)
• Health timeline and doctor-visit summary
• Medication and appointment reminders
• Anomaly detection using a machine-learning model
• More advanced personalization
11.3 Future Scope
• Smartwatch, wearable and IoT device integration
• Continuous real-time monitoring and automatic incident detection
• Advanced time-series prediction and fall-risk monitoring
• Telemedicine and e-prescription
• Hospital, healthcare-provider and emergency-service integration
• Voice-based Bangla interaction
• Large-scale healthcare ecosystem integration
The prototype demonstrates the emergency workflow through software-triggered and manually triggered
events. It does not claim automatic detection of incidents and does not connect to real emergency services.
12. Project Boundary, Safety and Regulatory Considerations
The scope above deliberately excludes clinical functions. This section states that boundary explicitly,
together with the security, privacy and regulatory controls that make it enforceable.
Department of Software Engineering, Daffodil International University Page 14

HealthMate: Project Proposal Part 1: Project Planning and Definition
HealthMate maintains a strict boundary between software assistance and clinical decision-making.
12.1 The System Will and Will Not
• The system will: analyze user-provided information, identify potentially unusual patterns, provide
wellness guidance, support healthcare navigation, notify authorized family members, and support
emergency-aware workflows.
• The system will not: diagnose diseases, prescribe medication, instruct users to stop prescribed
treatment, replace doctors, make autonomous clinical decisions, or claim certainty from imperfect
consumer health measurements.
HealthMate does not clinically determine an emergency. It detects predefined abnormal signals or events
and initiates a configured escalation workflow.
12.2 Security and Privacy Framework
Sensitive health information is handled with the following controls, each traceable to requirements.
Control What it means for HealthMate Requirements
Authentication Verified accounts, secure login, password reset and secure sessions FR-01 to FR-03, NFR-02
Authorization Server-side enforcement of who may see or change each record FR-04, NFR-03
Consent Explicit, revocable, per-category consent for family sharing and FR-60 to FR-63, FR-70
emergency notification
Role-based access Individual, caregiver and administrator roles with least privilege FR-04, NFR-03
Encryption TLS for data in transit and encryption of sensitive data at rest NFR-01
Data minimization Only necessary data is collected or sent to external services. Users can NFR-04
export and delete their data
Audit and logging Access to shared health data is recorded and visible to the data owner FR-65, NFR-05
These controls follow four principles: consent, purpose limitation, minimization and transparency.
12.3 Regulatory Considerations
The main legal development relevant to HealthMate is Bangladesh's Personal Data Protection Ordinance,
2025 (Ordinance No. 61 of 2025), issued on November 6, 2025 as the country's first standalone personal-
data-protection law [10]. According to published summaries, it treats individuals as owners of their personal
data, requires explicit consent, applies stricter rules to sensitive personal data such as health records and to
cross-border transfers, and creates enforcement through a national data authority, with a compliance period
of about 18 months for some provisions.
HealthMate's design is consistent with these principles. Explicit and revocable consent for family sharing (FR-
60 to FR-63), data export and deletion (NFR-04), and minimization of data sent to external AI services
address the main obligations. The team will confirm the ordinance's current legal status and commencement
dates, and whether any medical-device, telemedicine or digital-health guidelines apply to a wellness
application of this type, before the final proposal. The prototype uses no real patient data. Testing uses
synthetic data or data from consenting volunteers.
Department of Software Engineering, Daffodil International University Page 15

HealthMate: Project Proposal  Part 1: Project Planning and Definition
13. Requirements Analysis
The objectives, scope and safety boundary above are now translated into concrete, testable requirements.
Requirements are identified by ID and prioritized with four levels: Must have (capstone MVP), Should have,
Could have (planned enhancement) and Future (outside the capstone, see Section 11.3). The full functional
requirement list is in Appendix A.
13.1 Functional Requirements (Summary)
| Module  | IDs  | Main capabilities  | Priority  |
| ------- | ---- | ------------------ | --------- |
Account and access  FR-01 to  Registration, secure login, password reset, roles (individual,  Must
|     | FR-04  | caregiver, administrator)  |     |
| --- | ------ | -------------------------- | --- |
Health profile  FR-10 to  Personal profile, BMI, existing conditions, family health  Must
|     | FR-13  | history used only as context  |     |
| --- | ------ | ----------------------------- | --- |
Health data recording  FR-20 to  Blood pressure, heart rate, weight, sleep, activity, water,  Must
|     | FR-24  | mood. Validation, quick entry, family-assisted entry  |     |
| --- | ------ | ----------------------------------------------------- | --- |
Dashboard, trends and alerts  FR-30 to  Dashboard, trend periods, personal baseline, rule-based  Must
|     | FR-35  | alert levels, non-diagnostic wording  |     |
| --- | ------ | ------------------------------------- | --- |
Personalized guidance  FR-40 to  Personalized reminders, wellness goals, configurable  Must /
|     | FR-42  | reminder times  | Should  |
| --- | ------ | --------------- | ------- |
AI assistant and navigation  FR-50 to  Natural-language questions, explanation of records,  Must
|     | FR-55  | specialist-category guidance, refusal of diagnosis requests,  |     |
| --- | ------ | ------------------------------------------------------------- | --- |
safety checks
Family monitoring and  FR-60 to  Invite caregivers, per-category permissions, revocation,  Must /
permissions  FR-66  family alerts, audit log, missed check-in alert  Should
Emergency-aware escalation  FR-70 to  Emergency contacts, user verification prompt, contact  Must /
|     | FR-75  | notification, optional location, manual trigger, escalation  | Should  |
| --- | ------ | ------------------------------------------------------------ | ------- |
log
Consultation support  FR-80 to  Health timeline, doctor-visit summary, medication and  Could
|     | FR-82  | appointment reminders  |     |
| --- | ------ | ---------------------- | --- |
Localization  FR-90 to  Bangla and English interface, accessibility mode for older  Must /
|     | FR-91  | adults  | Should  |
| --- | ------ | ------- | ------- |

13.2 Non-Functional Requirements
| ID  Category  | Requirement  |     |     |
| ------------- | ------------ | --- | --- |
NFR-01  Security  All data in transit shall be encrypted (TLS). Sensitive health data at rest shall be
encrypted.
NFR-02  Security  Passwords shall be stored using a modern salted hash. Authentication shall use secure
session or token management.
NFR-03  Access control  Access to any health record shall be enforced server-side through role-based access and
explicit user consent.
NFR-04  Privacy  The system shall collect only the data required for its functions (data minimization).
Users shall be able to export and delete their data.
NFR-05  Auditability  Access to health data by anyone other than the owner shall be logged.
NFR-06  Performance  Dashboard pages shall load within 3 seconds under normal load. Alert evaluation shall
occur within 10 seconds of data submission.
Department of Software Engineering, Daffodil International University  Page 16

HealthMate: Project Proposal Part 1: Project Planning and Definition
ID Category Requirement
NFR-07 Reliability Alert delivery shall be retried on failure. Failed deliveries shall be recorded.
NFR-08 Usability Recording a routine measurement shall be completable in a small number of steps and
within the target in O-01.
NFR-09 Accessibility The interface shall follow accessibility good practices for older users (font size, contrast,
touch target size).
NFR-10 Localization All user-facing text shall be externalized to support multiple languages.
NFR-11 Maintainability The system shall be modular, with documented interfaces between components, and
automated tests for core logic.
NFR-12 Scalability The architecture shall allow horizontal scaling of stateless services and shall not depend
on a single-user-per-server design.
NFR-13 Safety Alert and assistant behavior shall comply with the boundary defined in Section 12.
NFR-14 Cost awareness Cost per active user (hosting, notifications, AI API usage) shall be estimated in the design
phase.
13.3 Feature-to-Problem Mapping
The table below closes the loop back to Section 3: for each HealthMate feature, the real-life problem it
addresses and the value it provides.
Problem
HealthMate feature Real-life problem Proposed value
ID
Personal health profile Health information is scattered Centralized personal health P-01
context
Family health history Family health risks may be ignored Better health awareness P-04
Health monitoring Users lack organized health records Continuous personal tracking P-01
Trend analysis Gradual changes are difficult to notice Better understanding of long-term P-03
patterns
Abnormal-pattern Unusual changes may go unnoticed Early awareness P-03
detection
Personalized notifications Generic advice is easy to ignore Context-aware guidance P-02, P-05
AI health assistant Users may struggle to understand health Easier interaction P-07
information
Healthcare navigation Users may not know which specialist to Better healthcare direction P-07
consult
Elderly monitoring Children may live far from elderly parents Remote family awareness P-06
Family alerts Important changes may remain unnoticed Faster family response P-06
Permission system Family monitoring may create privacy User-controlled sharing P-06
concerns
Health timeline Health history may be scattered Organized longitudinal record P-01, P-09
Doctor-visit summary Users may forget previous measurements Better preparation for P-09
consultation
Medication and Users may forget routine healthcare tasks Better adherence support P-05, P-09
appointment support
Department of Software Engineering, Daffodil International University Page 17

HealthMate: Project Proposal Part 1: Project Planning and Definition
Problem
HealthMate feature Real-life problem Proposed value
ID
Emergency escalation Unresponsive users may be difficult to Faster communication pathway P-08
reach
Department of Software Engineering, Daffodil International University Page 18

HealthMate: Project Proposal Part 1: Project Planning and Definition
PART E
HOW WE WILL BUILD IT
14. Feasibility Analysis
With the requirements defined, this section checks whether they can realistically be delivered.
14.1 Feasibility Assessment
Dimension Assessment
Technical Feasible using standard web and mobile technologies, a relational database, rule-based logic,
statistical methods and an external language-model API. The design avoids complex clinical AI
that requires large proprietary datasets.
Schedule Feasible with iterative delivery. Core monitoring and alerts are prioritized first. Enhancements
are deferred if needed so that a working MVP is always available.
Economic Feasible using open-source tools, student cloud credits and limited API usage. Hardware and
provider integrations are excluded from the MVP.
Operational Feasible through a simple interface, Bangla support, understandable notifications and user-
controlled sharing.
Legal and ethical Feasible with the boundary in Section 12, use of synthetic or consented data, and no clinical
claims. Requires confirmation of applicable regulations.
14.2 What Is Implemented Now and What Remains Future
Feasibility is shown by separating available technology, what the capstone implements, and what stays in
future scope. For example, direct wearable integration is future scope, but manual and family-assisted entry
and a simulated device feed are part of the MVP.
Capability Available technology In the capstone MVP Remains future scope
Health data input Entry forms, caregiver entry, Manual and family-assisted entry, Direct integration with Health
integration interface plus a simulated device feed Connect, smartwatches and
through the documented Bluetooth blood-pressure devices
interface
Trend analysis Standard statistical libraries Moving averages and baseline Advanced time-series forecasting
comparison
Alerts Configurable rule engine Threshold rules and five alert Thresholds personalized from
levels real usage data
Anomaly Isolation Forest and similar Evaluated on test or synthetic Models trained on real usage
detection methods data (enhancement) data
AI assistant Language-model API with Explanation, navigation and safe Domain-specific models and
guardrails refusal Bangla voice interaction
Notifications Push notifications, SMS Push notifications and limited Reliable SMS and voice-call
gateway SMS for the demonstration escalation
Department of Software Engineering, Daffodil International University Page 19

HealthMate: Project Proposal  Part 1: Project Planning and Definition
Capability  Available technology  In the capstone MVP  Remains future scope
Location sharing  Continuous tracking
|     | Device location with user  |     | Optional last known location,  |     |
| --- | -------------------------- | --- | ------------------------------ | --- |
|     | permission                 |     | permission-based               |     |
Software workflow
Emergency  Verification prompt and contact  Automatic incident detection and
| workflow  |     |     | notification  | emergency-service integration  |
| --------- | --- | --- | ------------- | ------------------------------ |
Standard export formats
Healthcare  Doctor-visit summary export  Provider dashboards,
| connection  |     |     | (enhancement)  | telemedicine and hospital  |
| ----------- | --- | --- | -------------- | -------------------------- |
integration

15. Development Methodology
Given that the project is feasible, this section explains how the team will deliver it.
Selected SDLC model: Agile (iterative and incremental). Agile is selected because HealthMate contains
several interconnected modules and technically uncertain components that benefit from iterative
refinement, supervisor feedback, usability testing and incremental validation. It allows the team to keep a
working product while progressively adding monitoring, analytics, AI assistance, elderly monitoring and
integration capabilities.
Working practices: iterations with a defined goal and deliverable, a prioritized product backlog based on
Appendix A, an iteration review with the supervisor, version control with reviewed changes, and automated
tests for core logic (alert rules, trend calculations and access control).
| Iteration  | Focus  | Main requirements  |     | Deliverable  |
| ---------- | ------ | ------------------ | --- | ------------ |
1  Foundation  FR-01 to FR-04, FR-10 to FR-13, NFR- Architecture, database schema,
|     |     | 01 to NFR-03  |     | authentication, profile  |
| --- | --- | ------------- | --- | ------------------------ |
2  Monitoring  FR-20 to FR-24, FR-30, FR-41  Data recording, dashboard, history
3  Analysis and alerts  FR-31 to FR-34, FR-40  Trend analysis, rule-based alert engine,
reminders
| 4   | Assistant  | FR-50 to FR-55  |     |     |
| --- | ---------- | --------------- | --- | --- |
AI assistant with guardrails, navigation
guidance
| 5   |             | FR-60 to FR-66, FR-70 to FR-75  |     |                                     |
| --- | ----------- | ------------------------------- | --- | ----------------------------------- |
|     | Family and  |                                 |     | Consent management, family alerts,  |
|     | emergency   |                                 |     | emergency workflow                  |
6  Integration and  FR-90, FR-91, all NFRs  Localization, security review, usability testing,
|     | evaluation  |     |     | final evaluation, documentation  |
| --- | ----------- | --- | --- | -------------------------------- |

16. Resource, Time and Budget Planning
The methodology above is now scheduled against the available 14-week semester and the team's resources.
Department of Software Engineering, Daffodil International University  Page 20

HealthMate: Project Proposal Part 1: Project Planning and Definition
16.1 Resources
Resource area Purpose Planning approach
Development System design and implementation Prefer open-source and existing academic tools
tools
Database Health and user data storage Relational database such as MySQL or PostgreSQL
AI and API Conversational and intelligent functions Limited, controlled usage within budget
services
Notification Push notifications and limited SMS for the Free or low-cost tiers
services demonstration
Hosting Prototype deployment and testing Basic cloud or server resources, student credits
where available
Testing devices Functional and usability testing Available team devices. External hardware optional
Development Iterative implementation Agile iterations with MVP-first prioritization
time
16.2 Time Plan
The project runs over a 14-week semester. Proposal documentation takes place in weeks 1 to 4, and each of
the six development iterations is planned at two weeks, starting in week 2 as the design is completed.
Usability sessions and evaluation run in weeks 11 to 13, the final report and presentation in weeks 13 to 14,
and week 14 is kept as a buffer. A supervisor review is held at the end of each iteration. Because the plan is
MVP-first, later enhancements can be deferred without losing a working system.
Figure 2. 14-week project schedule (Gantt chart). W = week of the semester.
16.3 Budget Approach
The prototype is designed to run on open-source software, student environments and free or low-cost cloud
tiers. The main variable costs are hosting, AI API usage and SMS delivery. AI usage and message volumes are
limited to testing and demonstration. A cost-per-active-user estimate will be prepared in the design phase
(NFR-14). Costly hardware and external integrations remain future considerations.
Department of Software Engineering, Daffodil International University Page 21

HealthMate: Project Proposal Part 1: Project Planning and Definition
17. Risk Analysis
No plan is risk-free. This section identifies what could go wrong in the plan above, and how the team will
respond.
Ratings: L = Low, M = Medium, H = High.
ID Risk Likelihood Impact Mitigation
R-01 Users do not enter data consistently H H Quick entry, reminders, family-assisted
(low engagement) entry, usability testing, optional device
import later
R-02 Insufficient data for machine-learning H M Rule-based alerts as the core. ML
anomaly detection treated as an optional enhancement,
tested on synthetic data
R-03 AI assistant gives unsafe or incorrect M H Guardrail layer, constrained prompts,
health information prohibited-request test set, disclaimers,
emergency redirection
R-04 False alerts cause anxiety or alert fatigue M M Configurable thresholds, alert levels,
review of thresholds by a qualified
professional, feedback loop
R-05 Missed alerts (a real concern is not M H Conservative rules, retry logic, explicit
flagged) statement that the system is not a
substitute for medical care
R-06 Privacy breach or unauthorized access to L H Encryption, server-side access control,
health data audit logs, security testing, minimal data
collection
R-07 Regulatory or legal issues around health M H Non-diagnostic boundary, no clinical
software and personal data claims, alignment with the Personal Data
Protection Ordinance 2025, review of
applicable regulations, synthetic data in
testing
R-08 Scope creep due to the breadth of H M MoSCoW priorities, iteration plan,
features supervisor scope reviews
R-09 Third-party service limits or outages M M Abstraction layers, fallback providers or
(SMS, AI API) mock services, retry logic
R-10 Difficulty recruiting participants for user M M Start recruitment early, use family and
validation community networks, define a minimum
viable sample
R-11 Team capacity or schedule slippage M M Iterative delivery, defined MVP, regular
progress tracking
R-12 Older adults find the interface difficult M H Accessibility mode, Bangla interface,
simplified flows, testing with older users
Several of these risks are already reduced by decisions made earlier in this proposal, rather than left for
later: R-01 (inconsistent data entry) is addressed by the quick-entry and family-assisted entry design in
Section 6.4; R-02 (insufficient data for machine learning) is addressed by relying on rule-based alerts as the
MVP core rather than machine learning (Section 7); R-03 (unsafe AI output) is addressed by the guardrail
layer (Section 7); R-06 (privacy breach) is addressed by the security and privacy framework (Section 12.2);
and R-07 (regulatory issues) is addressed by the alignment with the Personal Data Protection Ordinance in
Section 12.3.
Department of Software Engineering, Daffodil International University Page 22

HealthMate: Project Proposal Part 1: Project Planning and Definition
PART F
LOOKING AHEAD
18. Scalability and Product Vision
Beyond the risks of delivering the MVP, this section looks past the capstone toward how HealthMate could
grow.
Although the initial HealthMate system is a capstone prototype, its architecture is designed with future
scalability in mind.
Wearable Devices
↓
HealthMate Platform
↓
Personalized Analytics
↓
Family / Caregiver Support
↓
Healthcare Providers
↓
Telemedicine / Emergency Ecosystem
18.1 Roadmap
Stage Focus Example capabilities
Stage 1: Capstone Core monitoring, alerts, family sharing, Everything in Section 11.1
MVP assistant
Stage 2: Connected Reduce manual entry Blood pressure device and smartwatch integration,
data import from Health Connect and similar platforms
Stage 3: Deeper Improve personalization Anomaly detection trained on real usage data,
intelligence advanced time-series prediction, fall-risk awareness
Stage 4: Care Connect to healthcare Provider-facing summaries, telemedicine, hospital
ecosystem and pharmacy integration
Stage 5: Emergency Reliable escalation Emergency-service integration, multilingual and
and scale voice-based Bangla interaction, privacy-preserving
analytics at scale
18.2 Architectural Provisions for Scale
• Stateless backend services that can be scaled horizontally (NFR-12).
• A documented integration interface so that a new data source, such as a wearable, can be added
without changing the core engines (O-05).
• Configurable alert rules and externalized text to support new clinical guidance and languages (NFR-
10).
Department of Software Engineering, Daffodil International University Page 23

HealthMate: Project Proposal Part 1: Project Planning and Definition
These are future product possibilities rather than promises of the capstone prototype.
18.3 Business Model Outline (Vision)
This outline describes the long-term vision. It is not implemented in the capstone, and all revenue
assumptions are hypotheses to be validated through user research.
Element Hypothesis
Customer Individuals and families. The family member who wants to support a relative is a likely
paying customer
Value Family-aware health awareness, guidance and alerts in Bangla
Model options Freemium with a paid family plan (more family members, richer alerts, history export).
Possible future B2B partnerships with clinics, telemedicine services and device providers
Costs Hosting, notification and SMS costs, AI API usage, support, compliance
Key metrics (future) Weekly active users, retention, families connected per account, alert-to-action rate, cost
per active user
Go-to-market (future) Start with families separated by distance, then people managing chronic conditions, then
the general adult population
19. Expected Value and Impact
If the vision above is realized, this is the value it creates for the people HealthMate serves.
19.1 Individual User Value
• Better understanding of personal health trends.
• More consistent wellness habits through timely reminders.
• Greater awareness of potentially unusual changes.
• More organized health information.
• Better preparation for professional consultations.
19.2 Family Value
• Better awareness of elderly family members.
• Consent-based health alerts controlled by the person being monitored.
• Reduced uncertainty when family members live apart.
• Structured communication during potentially concerning situations.
19.3 Healthcare Interaction Value
HealthMate can help users organize relevant information before a professional consultation and provides a
foundation for future healthcare-provider integration.
Department of Software Engineering, Daffodil International University Page 24

HealthMate: Project Proposal Part 1: Project Planning and Definition
19.4 Product Value
The long-term opportunity lies in connecting monitoring, personalization, prevention awareness, family
safety and healthcare navigation in one digital-health platform.
20. Part 1 Conclusion
This planning phase establishes HealthMate as a feasible, user-centered and scalable digital-health project
rather than a simple health-data tracking application. The project is grounded in real-life problems involving
fragmented health information, limited personalization, difficulty recognizing changes, elderly safety, family
communication and healthcare navigation.
The proposed solution combines monitoring, analysis, personalized wellness guidance, responsible AI
assistance, family support and emergency-aware workflows, while maintaining clear medical and ethical
boundaries.
This planning foundation, together with the requirement identifiers (P, O, FR, NFR and R) and the traceability
set out in Appendix B, guides the subsequent parts.
Part Focus
Part 2 System design: architecture, data model, interaction flows and interface design
Part 3 To be confirmed with the supervisor
Part 4 Consolidated final project proposal, including the executive summary
References
Accessed September 20, 2026. Several sources are news reports of official data.
1. Bangladesh Bureau of Statistics, Population and Housing Census 2022, as reported in The Daily Star
editorial, "The state must take better care of elderly citizens."
https://www.thedailystar.net/opinion/editorial/news/the-state-must-take-better-care-elderly-
citizens-3099226
2. DataReportal, "Digital 2025: Bangladesh." https://datareportal.com/reports/digital-2025-bangladesh
3. RMMRU, "Trends and Dynamics of Labour Migration from Bangladesh 2025," as reported by The
Financial Express. https://thefinancialexpress.com.bd/national/bangladeshs-overseas-labour-
migration-up-12pc-in-2025-rmmru
4. Bureau of Manpower, Employment and Training (BMET) data on cumulative overseas employment, as
reported by The Financial Express. https://thefinancialexpress.com.bd/trade/over-200000-
bangladeshis-go-abroad-with-jobs-this-year-1624071884
5. Bangladesh Bank remittance data, as reported by UNB, "Remittance inflows hit historic high of
$35.56b in FY26." https://unb.com.bd/category/Business/remittance-inflows-hit-historic-high-of-
3556-billion-in-fy26/189623
6. Analysis of BDHS 2017-18 data on hypertension prevalence, awareness, treatment and control in
Bangladeshi adults, Journal of Clinical Hypertension.
https://pmc.ncbi.nlm.nih.gov/articles/PMC8678656/table/jch14363-tbl-0002
7. International Diabetes Federation, IDF Diabetes Atlas, Bangladesh country report.
https://diabetesatlas.org/data-by-location/country/bangladesh/
Department of Software Engineering, Daffodil International University Page 25

HealthMate: Project Proposal Part 1: Project Planning and Definition
8. UNB, "Best Free Bangladeshi Online Doctor Apps for Android, iOS in 2024."
https://unb.com.bd/category/Tech/best-free-bangladeshi-online-doctor-apps-for-android-ios-in-
2024/142054
9. Google Fit retirement and replacement by the Google Health app (announced May 2026).
https://en.wikipedia.org/wiki/Google_Fit
10. Bangladesh Personal Data Protection Ordinance, 2025 (Ordinance No. 61 of 2025). Summaries: The
Daily Star, "Bangladesh's Personal Data Protection Ordinance 2025: key takeaways."
https://www.thedailystar.net/tech-startup/news/bangladeshs-personal-data-protection-ordinance-
2025-key-takeaways-4015401 and Digital Policy Alert. https://digitalpolicyalert.org/change/18756-
personal-data-protection-ordinance-2025-ordinance-no-61-of-2025
Department of Software Engineering, Daffodil International University Page 26

HealthMate: Project Proposal Part 1: Project Planning and Definition
Appendix A: Detailed Functional Requirements
Priority key: M = Must have (MVP), S = Should have, C = Could have (planned enhancement). Items marked
Future are listed in Section 11.3 and are not in this table. The problem link column refers to the problem IDs
in Section 3.
A.1 Account and Access Management
ID Requirement Priority Problem link
FR-01 The system shall allow users to register and verify an account. M P-01
FR-02 The system shall allow users to log in and log out securely. M P-01
FR-03 The system shall support password reset. M P-01
FR-04 The system shall support role types: individual user, family member/caregiver, M P-06
and administrator.
A.2 Health Profile
ID Requirement Priority Problem link
FR-10 The system shall store age, gender, height, weight, calculated BMI, lifestyle M P-01, P-02
information and wellness goals.
FR-11 The system shall allow users to record existing health conditions and current S P-02
medications as user-provided information.
FR-12 The system shall allow users to record relevant family health history. M P-04
FR-13 The system shall use family health history only as a contextual input for M P-04
awareness and personalization, and shall not present it as a prediction of disease.
A.3 Health Data Recording
ID Requirement Priority Problem link
FR-20 The system shall allow recording of blood pressure, heart rate, weight, sleep M P-01, P-05
duration, physical activity, water intake and mood/stress.
FR-21 The system shall validate entries (valid ranges, units, timestamps) and warn on M P-01
implausible values.
FR-22 The system shall allow an authorized caregiver to record measurements on behalf S P-06
of another user.
FR-23 The system shall provide a quick-entry interface designed for minimal steps. M P-05, P-06
FR-24 The system shall allow users to edit or delete their own records. M P-01
Department of Software Engineering, Daffodil International University Page 27

HealthMate: Project Proposal Part 1: Project Planning and Definition
A.4 Dashboard, Trends and Alerts
ID Requirement Priority Problem link
FR-30 The system shall display current measurements, history, trends, goals and M P-01, P-03
notifications on a dashboard.
FR-31 The system shall compute trends over selectable periods (for example 7, 30 and M P-03
90 days).
FR-32 The system shall compare recent readings with the user's own baseline. M P-03
FR-33 The system shall classify readings and patterns into five alert levels (Level 0 M P-03
Normal to Level 4 Emergency escalation) using configurable, rule-based
thresholds.
FR-34 The system shall use non-diagnostic language in all alerts. M P-03
FR-35 The system shall support anomaly detection using a statistical or machine- C P-03
learning method once sufficient data exists for a user.
A.5 Personalized Guidance
ID Requirement Priority Problem link
FR-40 The system shall generate personalized reminders (hydration, sleep, activity and M P-05
goals) based on profile and recorded behavior.
FR-41 The system shall allow users to set and track wellness goals. S P-05
FR-42 The system shall allow users to configure reminder times and types. S P-05
A.6 AI Health Assistant and Navigation
ID Requirement Priority Problem link
FR-50 The system shall allow users to ask questions about their own records in natural M P-01, P-07
language (Bangla and English).
FR-51 The assistant shall provide general wellness information and explain the user's M P-07
recorded data.
FR-52 The assistant shall suggest a category of healthcare professional based on user- M P-07
described symptoms, and shall not state or imply a diagnosis.
FR-53 The assistant shall decline requests for diagnosis, medication changes or M P-07
treatment discontinuation, and shall redirect the user to a qualified professional.
FR-54 The system shall apply input and output safety checks to assistant interactions. M P-07
FR-55 The system shall show a clear notice that assistant responses do not replace M P-07
professional advice.
A.7 Family Monitoring and Permissions
ID Requirement Priority Problem link
FR-60 The system shall allow a user to invite and authorize a family member or M P-06
caregiver.
FR-61 The system shall allow the user to control which data categories each authorized M P-06
person may view.
Department of Software Engineering, Daffodil International University Page 28

HealthMate: Project Proposal Part 1: Project Planning and Definition
ID Requirement Priority Problem link
FR-62 The system shall allow the user to choose whether each authorized person M P-06
receives alerts only, summaries, or detailed data.
FR-63 The system shall allow the user to revoke access at any time, with immediate M P-06
effect.
FR-64 The system shall notify authorized family members of Concern and Urgent alerts M P-06
according to the user's permissions.
FR-65 The system shall record all access to shared health data in an audit log visible to S P-06
the data owner.
FR-66 The system shall raise an alert for a missed routine check-in, based on a user- S P-06, P-08
configured schedule.
A.8 Emergency-Aware Escalation
ID Requirement Priority Problem link
FR-70 The system shall allow a user to configure one or more emergency contacts and M P-08
give explicit consent for emergency notifications.
FR-71 On a Level 4 (Emergency escalation) event, the system shall prompt the user to M P-08
confirm their status within a configurable time window.
FR-72 If the user does not respond, the system shall notify the emergency contact(s) M P-08
with the reason for the alert.
FR-73 If the user has authorized it, the system shall include the last known location in S P-08
the notification.
FR-74 The user shall be able to trigger the emergency workflow manually. M P-08
FR-75 The system shall log the complete escalation sequence (trigger, prompt, S P-08
response, notifications).
Scope note: The MVP demonstrates the escalation workflow using software-triggered and manually triggered
events. It does not claim to detect incidents automatically (for example, loss of consciousness while driving),
and does not integrate with real emergency services.
A.9 Consultation Support (Enhancements)
ID Requirement Priority Problem link
FR-80 The system shall present a chronological health timeline. C P-01, P-09
FR-81 The system shall generate a doctor-visit summary of recent measurements, alerts C P-09
and reported symptoms.
FR-82 The system shall support medication and appointment reminders. C P-05, P-09
A.10 Localization
ID Requirement Priority Problem link
FR-90 The system shall provide the core user interface in Bangla and English. M P-06
FR-91 The system shall provide an accessibility mode for older adults (large text, high S P-06
contrast, simplified navigation).
Department of Software Engineering, Daffodil International University Page 29

HealthMate: Project Proposal  Part 1: Project Planning and Definition
Appendix B: Requirements Traceability
This matrix links every problem (Section 3) to the objectives (Section 10) and requirements (Section 13,
Appendix A) that address it. Parts 2 and 3 extend it with design components and test cases.
| Problem  | Objective(s)  | Requirements  |
| -------- | ------------- | ------------- |
P-01 Fragmented information  O-01  FR-01 to FR-03, FR-10, FR-20 to FR-24, FR-30, FR-80
P-02 Limited personalization  O-02  FR-10, FR-11, FR-40, FR-41
| P-03 Gradual changes unnoticed    | O-02        | FR-30 to FR-35  |
| --------------------------------- | ----------- | --------------- |
| P-04 Family history disconnected  | O-01, O-02  | FR-12, FR-13    |
P-05 Habit consistency  O-01, O-02  FR-20, FR-23, FR-40 to FR-42, FR-82
P-06 Elderly monitoring gap  O-01, O-04  FR-04, FR-22, FR-60 to FR-66, FR-90, FR-91
| P-07 Where to seek care           | O-03  | FR-50 to FR-55         |
| --------------------------------- | ----- | ---------------------- |
| P-08 Emergency communication gap  | O-04  | FR-66, FR-70 to FR-75  |
| P-09 Consultation preparation     | O-01  | FR-80 to FR-82         |
Cross-cutting (security and privacy)  O-05  NFR-01 to NFR-05, FR-65
| Cross-cutting (extensibility and scale)  | O-05  | NFR-10 to NFR-14  |
| ---------------------------------------- | ----- | ----------------- |

Appendix C: Glossary
| Term  | Definition  |     |
| ----- | ----------- | --- |
Alert level  A classification from Level 0 (Normal) to Level 4 (Emergency escalation) describing
how far a reading or pattern deviates from expectation and what action follows
Escalation workflow  A configured sequence of software actions (verification prompt, contact
notification, optional location sharing) started by a predefined event. It is not a
clinical determination
Baseline  A user's own typical range of measurements, calculated from their history
Cold start  The period when there is too little data for a statistical or machine-learning
method to be reliable
Guardrail layer  Software controls that filter and constrain the inputs and outputs of the AI
assistant
Family-assisted entry  Data entry by an authorized caregiver on behalf of another user
Health and wellness companion  A non-diagnostic system that provides monitoring, guidance and support, and
does not replace clinical care
MoSCoW  A prioritization method: Must, Should, Could, Won't (now)
| MVP  | Minimum Viable Product  |     |
| ---- | ----------------------- | --- |
Isolation Forest  An unsupervised machine-learning algorithm used to detect outliers
| PDPO  | Personal Data Protection Ordinance, 2025 (Bangladesh)  |     |
| ----- | ------------------------------------------------------ | --- |
| RBAC  | Role-Based Access Control                              |     |
SMART  Specific, Measurable, Achievable, Relevant, Time-bound

Department of Software Engineering, Daffodil International University  Page 30

HealthMate: Project Proposal Part 1: Project Planning and Definition
End of Part 1
Department of Software Engineering, Daffodil International University Page 31
