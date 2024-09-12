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
  2. GDPR compliance

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# GDPR compliance#

All versions of the Unity Ads SDK are compliant with the General Data
Protection Regulation (GDPR), which took effect in the European Economic Area
(EEA) on May 25, 2018.

Visit our legal site for more information on [Unity's approach to
privacy](https://unity.com/legal).

## Implement Unity's built-in consent solution#

The recommended best practice is to update to the latest version of the Unity
Ads SDK, but this is not required for GDPR compliance.

SDK versions earlier than 2.0 now only serve contextual ads to users, strictly
based on geographic location and in-app actions.

SDK versions 2.0 and later automatically present affected users with an
opportunity to opt in to targeted advertising, with no implementation needed
from the publisher. On a per-app basis, the first time a Unity ad displays, a
banner provides the option to opt in to behaviorally targeted advertising.
Thereafter, the user can select an information button to manage their privacy
choices.

## Implement a custom consent solution#

If you implement a custom consent solution in your app, you must send your
users’ consent statuses to the Unity Ads SDK.

The following sections describe the guidelines for handling custom consent
implementations as a non-TCF user and as a TCF user with an integrated CMP.

### Non-TCF users#

If you’re using a mediation provider, refer to their documentation to
determine if they support sharing user consent status with the Unity Ads SDK.
Some mediators, such as LevelPlay, have APIs that let you set the consent
status of a user and automatically communicate the consent status to Unity Ads
on your behalf.

**Note** : Some mediators might also support Google’s Additional Consent mode,
which is a mechanism to share consent with non-TCF vendors like Unity Ads.
Mediators, such as LevelPlay, read the Additional Consent string and pass the
consent status to Unity Ads where applicable.

Otherwise, use the [Developer Consent API](/ads/en-
us/manual/GDPRCompliance#Custom_consent_implementation_using_Developer_Consent_API)
to directly pass the consent status to the Unity Ads SDK.

### TCF users#

#### Consent support for Google UMP and CMPs compatible with Google’s
Additional Consent#

If you’re using Google UMP, refer to Google’s [Manage GDPR ad
partners](https://support.google.com/admob/answer/10113004) documentation to
complete your setup on the AdMob platform.

If you’re not using Google UMP, refer to the documentation of your CMP for
configuration support in implementing Google’s Additional Consent.

During the setup, do the following to ensure Unity Ads is included as a custom
ad partner in AdMob:

  1. Sign into your AdMob account.
  2. Go to **Privacy & messaging**.
  3. Select **Personalized ads** as the type of ads you want to show.
  4. Go to the Review your ad partners section, then edit the **Commonly used ad partners**.
  5. Select **Custom ad partners** in the ad partners page, then enable Unity Ads.

**Important** : Unity Ads is not a registered TCF vendor, which means that
Unity does not directly read the `TCString` to determine user consent. To the
extent you are collecting consent for Unity Ads via the Additional Consent (or
similar) mechanism, some mediators, like LevelPlay, read this string and
communicate consent to Unity Ads. In all cases, you’ll still need to share the
consent status of the user through your mediator (if supported) or using the
[Developer Consent API](/ads/en-
us/manual/GDPRCompliance#Custom_consent_implementation_using_Developer_Consent_API).

#### Consent support for integrations with other CMPs#

When using another integrated CMP, set up your unregistered TCF networks
according to the CMP guidelines. Ensure that you add Unity Ads as a non-TCF
vendor to your CMP.

If you’re using a mediation provider, refer to their documentation to
determine if they support sharing user consent statuses with the Unity Ads
SDK. Some mediators, such as LevelPlay, [have
APIs](https://developers.is.com/ironsource-mobile/unity/regulation-advanced-
settings/#step-1) that let you set the consent status of a user and
automatically communicate the consent status to Unity Ads on your behalf.

If you’re not using a mediator and intend to process user consent yourself,
read the relevant consent value for the user according to their CMP provider,
then pass the consent status to the Unity Ads SDK via our [Developer Consent
API](/ads/en-
us/manual/GDPRCompliance#Custom_consent_implementation_using_Developer_Consent_API).

The following table details where to find instructions for passing user
consent statuses to the Unity Ads SDK:

| **TCF CMP users**| **Non-TCF users**  
---|---|---  
**Using a mediation provider**|  Refer to your mediator’s documentation to
learn if and how they support sharing user consent status with the Unity Ads
SDK, which is usually done through APIs or Google’s Additional Consent mode.|
Refer to your mediator’s documentation to learn if and how they support
sharing user consent status with the Unity Ads SDK, which is usually done
through APIs.  
**Without a mediation provider**|  Refer to the [Developer Consent
API](/ads/en-
us/manual/GDPRCompliance#Custom_consent_implementation_using_Developer_Consent_API)
to pass the consent status directly to the Unity Ads SDK.| Refer to the
D[Developer Consent API](/ads/en-
us/manual/GDPRCompliance#Custom_consent_implementation_using_Developer_Consent_API)
to pass the consent status directly to the Unity Ads SDK.  
  
## Custom consent implementation using Developer Consent API#

If a publisher or mediator sends us a value via our [Developer Consent
API](/ads/en-
us/manual/GDPRCompliance#Custom_consent_implementation_using_Developer_Consent_API),
the Unity opt-in does not display. Note that users can still request opt-out
or data deletion, and can access their data at any time during an ad display
by selecting the Unity Data Privacy icon.

Use the following API to pass a consent flag to the Unity Ads SDK.

**Tip** : If the user takes no action to agree or disagree with targeted
advertising (for example, closing the prompt), the recommended best practice
is to re-prompt them at a later time.

### Unity (C#)#

    
    
    // If the user opts in to targeted advertising:
    MetaData gdprMetaData = new MetaData("gdpr");
    gdprMetaData.Set("consent", "true");
    Advertisement.SetMetaData(gdprMetaData);
    
    // If the user opts out of targeted advertising:
    MetaData gdprMetaData = new MetaData("gdpr");
    gdprMetaData.Set("consent", "false");
    Advertisement.SetMetaData(gdprMetaData);

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value. The second parameter is an object (a
string in this example). Using a Boolean value will result in an error.

### iOS (Objective-C)#

    
    
    // If the user opts in to targeted advertising:
    UADSMetaData *gdprConsentMetaData = [[UADSMetaData alloc] init];
    [gdprConsentMetaData set:@"gdpr.consent" value:@YES];
    [gdprConsentMetaData commit];
    
    // If the user opts out of targeted advertising:
    UADSMetaData *gdprConsentMetaData = [[UADSMetaData alloc] init];
    [gdprConsentMetaData set:@"gdpr.consent" value:@NO];
    [gdprConsentMetaData commit];

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

### Android (Java)#

    
    
    // If the user opts in to targeted advertising:
    MetaData gdprMetaData = new MetaData(this);
    gdprMetaData.set("gdpr.consent", true);
    gdprMetaData.commit();
    
    // If the user opts out of targeted advertising:
    MetaData gdprMetaData = new MetaData(this);
    gdprMetaData.set("gdpr.consent", false);
    gdprMetaData.commit();

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

  * GDPR compliance
  * Implement Unity's built-in consent solution
  * Implement a custom consent solution
  * Non-TCF users
  * TCF users
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

