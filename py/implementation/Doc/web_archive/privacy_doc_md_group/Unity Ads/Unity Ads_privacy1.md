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
  2. PIPL compliance

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# PIPL compliance#

Starting November 1, 2021, China’s Personal Information Protection Law (PIPL)
policy will be enforced for users in mainland China.

## Implement Unity's built-in consent solution#

The recommended best practice is to update to the latest version of the Unity
Ads SDK, but this is not required, but it is not required for PIPL compliance.

Legacy versions (earlier than version 2.0) of the SDK now only serve
contextual ads to users, strictly based on geographic location and in-app
actions.

SDK versions 2.0 and later automatically present affected users with an
opportunity to opt in to targeted advertising, with no implementation needed
from the publisher. On a per-app basis, the first time a Unity ad displays, a
banner provides the option to opt in to behaviorally targeted advertising.
Thereafter, the user can select an information button to manage their privacy
choices.

## Implement a custom consent solution#

If a publisher or mediator manually requests a user opt-in by having their
account manager enable **Developer Consent** in the [Unity Ads Monetization
dashboard](http://cloud.unity.com/monetization), the Unity opt-in will not
appear.

**Note** : that users can still request opt-out or data deletion, and access
their data at any time by tapping the Unity Data Privacy icon when or after an
ad appears.

### Custom consent implementation using Developer Consent API#

Use the following API to pass the appropriate consent flags to the Unity Ads
SDK:

### Unity (C#)#

    
    
    // If the user opts in to sending their personal identifiable information outside of China:
    MetaData piplMetaData = new MetaData("pipl");
    piplMetaData.Set("consent", "true");
    Advertisement.SetMetaData(piplMetaData);
    
    // If the user opts in to targeted advertising:
    MetaData privacyMetaData = new MetaData("privacy");
    privacyMetaData.Set("consent", "true");
    Advertisement.SetMetaData(privacyMetaData);
    
    // If the user opts out of sending their personal identifiable information outside of China:
    MetaData piplMetaData = new MetaData("pipl");
    piplMetaData.Set("consent", "false");
    Advertisement.SetMetaData(piplMetaData);
    
    // If the user opts out of targeted advertising:
    MetaData privacyMetaData = new MetaData(this);
    privacyMetaData.set("privacy.consent", false);
    privacyMetaData.commit();

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value. You must also provide consent for sending
a user's personal identifiable information outside of China and to targeted
advertising for PIPL. The second parameter is an object (a string in this
example); using a boolean value will result in an error.

### iOS (Objective-C)#

    
    
    // If the user opts in to sending their personal identifiable information outside of China:
    UADSMetaData *piplConsentMetaData = [[UADSMetaData alloc] init];
    [piplConsentMetaData set:@"pipl.consent" value:@YES];
    [piplConsentMetaData commit];
    
    // If the user opts in to targeted advertising:
    UADSMetaData *privacyConsentMetaData = [[UADSMetaData alloc] init];
    [privacyConsentMetaData set:@"privacy.consent" value:@YES];
    [privacyConsentMetaData commit];
    
    // If the user opts out of sending their personal identifiable information outside of China:
    UADSMetaData *piplConsentMetaData = [[UADSMetaData alloc] init];
    [piplConsentMetaData set:@"pipl.consent" value:@NO];
    [piplConsentMetaData commit];
    
    // If the user opts out of targeted advertising:
    UADSMetaData *privacyConsentMetaData = [[UADSMetaData alloc] init];
    [privacyConsentMetaData set:@"privacy.consent" value:@NO];
    [privacyConsentMetaData commit];

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value. You must also provide consent for sending
their personal identifiable information outside of China and to targeted
advertising for PIPL.

### Android (Java)#

    
    
    // If the user opts in to sending their personal identifiable information outside of China:
    MetaData piplMetaData = new MetaData(this);
    piplMetaData.set("pipl.consent", true);
    piplMetaData.commit();
    
    // If the user opts in to targeted advertising:
    MetaData privacyMetaData = new MetaData(this);
    privacyMetaData.set("privacy.consent", true);
    privacyMetaData.commit();
    
    // If the user opts out of sending their personal identifiable information outside of China:
    MetaData piplMetaData = new MetaData(this);
    piplMetaData.set("pipl.consent", false);
    piplMetaData.commit();
    
    // If the user opts out of targeted advertising:
    MetaData privacyMetaData = new MetaData(this);
    privacyMetaData.set("privacy.consent", false);
    privacyMetaData.commit();

**Note** : You must commit the changes to the MetaData for each value before
trying to set another value. You must also provide consent for sending their
personal identifiable information outside of China and to targeted advertising
for PIPL.

### Handling inaction#

If the user takes no action to agree or disagree to targeted advertising (for
example, closing the prompt), Unity recommends re-prompting them at a later
time.

Visit Unity's legal site for more information on [Unity's approach to
PIPL](https://unity.cn/legal/privacy-policy).

  * PIPL compliance
  * Implement Unity's built-in consent solution
  * Implement a custom consent solution
  * Custom consent implementation using Developer Consent API
  * Unity (C#)
  * iOS (Objective-C)
  * Android (Java)
  * Handling inaction

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

