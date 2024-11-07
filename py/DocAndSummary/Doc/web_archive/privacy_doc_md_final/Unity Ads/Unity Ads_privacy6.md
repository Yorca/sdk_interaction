#### Search Unity

[Unity logo](https://www.unity.com) [Unity Documentation](/)

All Docs

  * [Unity Docs Home](/)
  * [Unity Editor Manual](https://docs.unity3d.com/Manual/index.html)
  * [Unity Gaming Services Docs](https://docs.unity.com/ugs-overview/unity-gaming-services-home.html)
  * [Unity Gaming Services REST API Docs](https://services.docs.unity.com/)

[Learning](https://unity.com/learn)

Community

  * [Blog](https://blog.unity.com/)
  * [Forums](https://forum.unity.com/)
  * [Answers](https://answers.unity.com/)

Support & Services

  * [Customer Service](https://support.unity.com/hc/en-us/requests/new)
  * [Knowledge Base](https://support.unity.com/hc/en-us)
  * [Technical Support](https://unity.com/success-plans)
  * [Consulting Services](https://unity.com/professional-services)

  * [Asset Store](https://assetstore.unity.com/)
  * [Connect](https://connect.unity.com/)
  * [Dashboard](https://dashboard.unity3d.com/)
  * [Distribute](https://distribute.dashboard.unity.com)
  * [Forum](https://forum.unity.com/)
  * [Learn](https://learn.unity.com/)

  * [Welcome to Unity Ads](/ads/en-us/manual/UnityAdsHome)

  * [News and updates](/ads/en-us/manual/news-and-updates)

  * [Creating a Unity project](/ads/en-us/manual/CreatingUnityProjects)

  * [Unity developer integration guides](/ads/en-us/manual/UnityDeveloperIntegrations)

  * [Android developer integration guides](/ads/en-us/manual/AndroidDeveloperIntegrations)

  * [iOS developer integration guides](/ads/en-us/manual/iOSDeveloperIntegrations)

  * [Cross-platform integration guides](/ads/en-us/manual/CrossPlatformIntegrations)

  * [Privacy consent and data APIs](/ads/en-us/manual/ImplementingDataPrivacy)
    * [Child data law compliance, CARU compliance, and contextual ads](/ads/en-us/manual/COPPACompliance)
    * [PIPL compliance](/ads/en-us/manual/PIPLCompliance)
    * [GDPR compliance](/ads/en-us/manual/GDPRCompliance)
    * [Consumer privacy act compliance](/ads/en-us/manual/CCPACompliance)
    * [Google Play Families compliance](/ads/en-us/manual/GoogleFamiliesCompliance)
    * [Implementing custom age gates](/ads/en-us/manual/ImplementingCustomAgeGates)
    * [Google Play data safety section for Unity Ads](/ads/en-us/manual/GoogleDataSafety)
    * [Apple privacy survey for Unity Ads](/ads/en-us/manual/ApplePrivacySurvey)

  * [Best practices](/ads/en-us/manual/BestPractices)

  * [References](/ads/en-us/manual/References)

  * [Changelog](/ads/en-us/manual/Changelog)

  1. [Privacy consent and data APIs](/ads/en-us/manual/ImplementingDataPrivacy)
  2. Google Play data safety section for Unity Ads

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# Google Play data safety section for Unity Ads#

Starting April 2022, Android developers publishing on the Google Play store
must define what data their apps collect, including the data collected by
integrated third-party SDKs such as Unity Ads. For your convenience, Unity Ads
provides information on its data collection practices in the following
sections.

**Important** : The following data disclosures are for the Unity Ads SDK only.
You are also responsible for providing any additional disclosures for your
app, including other Unity SDKs and/or third-party SDKs used in your app.

For more information on Google's data safety disclosure policies, including
terminology definitions, refer to the [Google
documentation](https://support.google.com/googleplay/android-
developer/answer/10787469).

## Data collection survey#

Does the SDK collect or share any of the required user data types?| Yes  
---|---  
Is all of the data collected by the SDK encrypted in transit?| Yes  
Does the SDK provide a way for users to request that their data is deleted?|
Yes  
  
### Data types#

**Location**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s approximate location?| Yes| Yes| No| Yes|
Advertising or marketing, analytics, app functionality, fraud prevention,
security, and compliance  
Does the SDK collect the user’s precise location?| No| Not applicable (N/A)|
N/A| N/A| N/A  
**Personal information**| **Collected**| **Shared**| **Ephemeral**|
**Required**| **Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s name?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s email address?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s personal identifiers?| Yes| Yes| No| Yes| App
functionality  
Does the SDK collect the user’s address?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s phone number?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s race and ethnicity?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s political or religious beliefs?| No| N/A| N/A|
N/A| N/A  
Does the SDK collect the user’s sexual orientation or gender identity?| No|
N/A| N/A| N/A| N/A  
Does the SDK collect any of the user’s other personal information?| No| N/A|
N/A| N/A| N/A  
**Financial info**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s purchase history?| Yes| Yes| No| Yes|
Advertising or marketing, analytics  
Does the SDK collect the user’s credit info?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s credit card, debit card, or bank account
number?| No| N/A| N/A| N/A| N/A  
Does the SDK collect any of the user’s other financial info?| No| N/A| N/A|
N/A| N/A  
**Health and fitness**| **Collected**| **Shared**| **Ephemeral**|
**Required**| **Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s health information?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s fitness information?| No| N/A| N/A| N/A| N/A  
**Messages**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s emails?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s SMS or MMS messages?| No| N/A| N/A| N/A| N/A  
Does the SDK collect any of the user’s other in-app messages?| No| N/A| N/A|
N/A| N/A  
**Photos and videos**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s photos?| No| N/A| N/A| N/A| N/A  
Does the SDK collect the user’s videos?| No| N/A| N/A| N/A| N/A  
**Audio files**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s voice or sound recordings?| No| N/A| N/A| N/A|
N/A  
Does the SDK collect the user’s music files?| No| N/A| N/A| N/A| N/A  
Does the SDK collect any of the user’s other audio files?| No| N/A| N/A| N/A|
N/A  
**Files and docs**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s files and or documents?| No| N/A| N/A| N/A|
N/A  
**Calendar**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s calendar events?| No| N/A| N/A| N/A| N/A  
**Contacts**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect the user’s contacts?| No| N/A| N/A| N/A| N/A  
**App activity**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect data on page views and taps in the app?| Yes*| Yes| No|
Yes| Advertising or marketing, analytics, fraud prevention, security, and
compliance  
Does the SDK collect in-app search history?| No| N/A| N/A| N/A| N/A  
Does the SDK collect data on installed apps?| No| N/A| N/A| N/A| N/A  
Does the SDK collect data on any other user-generated content?| No| N/A| N/A|
N/A| N/A  
Does the SDK collect data on any other app activity?| Yes**| Yes| No| Yes|
Advertising or marketing, analytics, fraud prevention, security, and
compliance  
  
* Unity Ads only collects data on page views and taps during the ad experience in the ad itself, not during gameplay.

** Unity Ads collects app usage times to measure the retention of users in
apps to serve more meaningful advertisements. Unity Ads only collects data on
app usage times when **Acquire Optimization** is enabled in the Monetization
dashboard.

**Web browsing**| **Collected**| **Shared**| **Ephemeral**| **Required**|
**Purpose**  
---|---|---|---|---|---  
Does the SDK collect data on the user’s web browsing history?| No| N/A| N/A|
N/A| N/A  
**App info and performance**| **Collected**| **Shared**| **Ephemeral**|
**Required**| **Purpose**  
---|---|---|---|---|---  
Does the SDK collect crash logs?| No| N/A| N/A| N/A| N/A  
Does the SDK collect app diagnostics?| Yes| Yes| No| Yes| App functionality,
analytics  
Does the SDK collect any other app performance data?| No| N/A| N/A| N/A| N/A  
**Device or other identifiers**| **Collected**| **Shared**| **Ephemeral**|
**Required**| **Purpose**  
---|---|---|---|---|---  
Does the SDK collect data on the user’s device or other identifiers?| Yes|
Yes| No| Yes| Advertising or marketing, analytics, app functionality, fraud
prevention, security, and compliance  
  
  * Google Play data safety section for Unity Ads
  * Data collection survey
  * Data types

[Unity logo Documentation](/)

Copyright © 2024 Unity Technologies

  * [Legal](https://unity3d.com/legal)
  * [Privacy Policy](https://unity3d.com/legal/privacy-policy)
  * [Terms Of Use](https://docs.unity3d.com/Manual/TermsOfUse.html)
  * [Cookies](https://unity3d.com/legal/cookie-policy)
  * [Do Not Sell or Share My Personal Information](https://unity3d.com/legal/do-not-sell-my-personal-information)
  * Your Privacy Choices (Cookie Settings)

"Unity", Unity logos, and other Unity trademarks are trademarks or registered
trademarks of Unity Technologies or its affiliates in the U.S. and elsewhere
([more info here](https://unity3d.com/legal/trademarks)). Other names or
brands are trademarks of their respective owners.

