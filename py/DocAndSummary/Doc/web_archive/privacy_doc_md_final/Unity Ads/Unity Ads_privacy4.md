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
  2. Google Play Families compliance

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# Google Play Families compliance#

If your Google application serves ads and is designed for children:

  1. It must comply with the [Google Play Families policy](https://support.google.com/googleplay/android-developer/answer/9900633).
  2. [Update its Game-level age designation setting](https://docs.unity.com/monetization-dashboard/ProjectSettings.html#PrivacySettings) in the Unity Ads Monetization dashboard to **This app is directed to children**.
  3. If your app is participating in Google's [Designed for Families](https://support.google.com/googleplay/android-developer/answer/9893335) program, [update its **App store compliance** setting](https://docs.unity.com/monetization-dashboard/ProjectSettings.html#AppStoreCompliance) in the Monetization dashboard to enable the Google **Designed for Families** flag.

**Important** : Unity Ads publishers with apps that only target children must
follow additional requirements for the Designed for Families program. These
apps must also enable the Google **Designed for Families** flag in the section
of the Monetization dashboard to avoid disruption of services.

## Implementing user-level age statuses with Google Families#

If you implement user-level age-restricted statuses, your app is still
eligible for the Google Families program. To do so:

  1. Follow the [Monetization dashboard instructions](https://docs.unity.com/monetization-dashboard/ProjectSettings.html#UserLevel) for enabling mixed audiences.
  2. [Implement the user-level age-restricted flag](/ads/en-us/manual/COPPACompliance#UserLevel) in your app code.
  3. If your app is participating in Google's Designed for Families program, [update its **App store compliance** setting](https://docs.unity.com/monetization-dashboard/ProjectSettings.html#AppStoreCompliance) in the Monetization dashboard to enable the Google **Designed for Families** flag.

  * Google Play Families compliance
  * Implementing user-level age statuses with Google Families

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

