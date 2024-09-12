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
  2. Consumer privacy act compliance

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# Consumer privacy act compliance#

All versions of the Unity Ads SDK are compliant with the following consumer
privacy acts:

  * The California Consumer Privacy Act ([CCPA](https://oag.ca.gov/privacy/ccpa)), which is effective in California starting January 2019.
  * Brazilian General Data Protection Law ([LGPD](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm)), which is effective starting August 2021.
  * The Virginia Consumer Data Privacy Act ([VCDPA](https://law.lis.virginia.gov/vacode/title59.1/chapter53/)), which is effective in Virginia starting January 2023.
  * The Colorado Privacy Act ([CPA](https://leg.colorado.gov/bills/sb21-190)), which is efffective in Colorado starting July 2023.
  * The Connecticut Data Privacy Act ([CTDPA](https://portal.ct.gov/AG/Sections/Privacy/The-Connecticut-Data-Privacy-Act)), which is effective in Connecticut starting July 2023.
  * Quebec Law 25 ([QCLAW25](https://www.legisquebec.gouv.qc.ca/en/document/cs/p-39.1)), which is effective in Quebec, Canada starting September 2023.
  * Utah Consumer Privacy Act ([UCPA](https://le.utah.gov/~2022/bills/static/SB0227.html)), which is effective in Utah starting December 2023.
  * Florida Digital Bill of Rights ([FDBR](https://www.flsenate.gov/Session/Bill/2023/262/BillText/er/HTML)), which is effective in Utah starting July 2024.
  * Oregon Consumer Privacy Act ([OCPA](https://olis.oregonlegislature.gov/liz/2023R1/Downloads/PublicTestimonyDocument/59856#:~:text=The%20Act%20requires%20controllers%20to,data%3B%20and%20%E2%80%A2%20Contact%20information.)), which is effective in Oregon starting July 2024.
  * Texas Data Privacy and Security Act ([TDPSA](https://capitol.texas.gov/tlodocs/88R/billtext/pdf/HB00004F.pdf#navpanes=0)), which is effective in Texas starting July 2024.

Visit our legal site for more information on [Unity's approach to
privacy](https://unity.com/legal).

## Implement Unity's built-in consent solution#

The recommended best practice is to update to the latest version of the Unity
Ads SDK, but this is not required, but this is not required for CCPA, LGPD,
VCDPA, CPA, CTDPA, Quebec Law 25, UCPA, FDBR, OCPA, TDPSA compliance.

SDK versions 2.0 and later automatically present affected users with an
opportunity to opt in to targeted advertising, with no implementation needed
from the publisher. On a per-app basis, the first time a Unity ad displays, a
banner provides the option to opt in to behaviorally targeted advertising.
Thereafter, the user can select an information button to manage their privacy
choices.

## Implement a custom consent solution#

If you implement a custom consent solution in your app, you must send your
users’ consent statuses to the Unity Ads SDK.

### Custom consent implementation using Developer Consent API#

If a publisher or mediator sends us a value via the Developer Consent API, the
Unity opt-in does not display. Note that users can still request opt-out or
data deletion, and can access their data at any time during an ad display by
selecting the Unity Data Privacy icon.

Use the following API to pass a consent flag to the Unity Ads SDK.

**Note** : If you have already implemented the `gdpr` API to solicit consent,
you can also extend your implementation to users affected by CCPA, LGPD,
VCDPA, CPA, CTDPA, Quebec Law 25, UCPA, FDBR, OCPA, TDPSA. Similarly, the
privacy API can apply to GDPR when extended to affected users.

**Tip** : If the user takes no action to agree or disagree with targeted
advertising (for example, closing the prompt), the recommended best practice
is to re-prompt them at a later time.

### Unity (C#)#

    
    
    // If the user opts in to targeted advertising:
    MetaData privacyMetaData = new MetaData("privacy");
    privacyMetaData.Set("consent", "true");
    Advertisement.SetMetaData(privacyMetaData);
    
    // If the user opts out of targeted advertising:
    MetaData privacyMetaData = new MetaData("privacy");
    privacyMetaData.Set("consent", "false");
    Advertisement.SetMetaData(privacyMetaData);

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value. The second parameter is an object (a
string in this example). Using a Boolean value will result in an error.

### iOS (Objective-C)#

    
    
    // If the user opts in to targeted advertising:
    UADSMetaData *privacyConsentMetaData = [[UADSMetaData alloc] init];
    [privacyConsentMetaData set:@"privacy.consent" value:@YES];
    [privacyConsentMetaData commit];
    
    // If the user opts out of targeted advertising:
    UADSMetaData *privacyConsentMetaData = [[UADSMetaData alloc] init];
    [privacyConsentMetaData set:@"privacy.consent" value:@NO];
    [privacyConsentMetaData commit];

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

### Android (Java)#

    
    
    // If the user opts in to targeted advertising:
    MetaData privacyMetaData = new MetaData(this);
    privacyMetaData.set("privacy.consent", true);
    privacyMetaData.commit();
    
    // If the user opts out of targeted advertising:
    MetaData privacyMetaData = new MetaData(this);
    privacyMetaData.set("privacy.consent", false);
    privacyMetaData.commit();

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

  * Consumer privacy act compliance
  * Implement Unity's built-in consent solution
  * Implement a custom consent solution
  * Custom consent implementation using Developer Consent API
  * Unity (C#)
  * iOS (Objective-C)
  * Android (Java)

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

