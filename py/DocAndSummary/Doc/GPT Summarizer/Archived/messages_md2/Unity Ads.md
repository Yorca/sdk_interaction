SDK name: Unity Ads
Documentation:
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
  2. Child data law compliance, CARU compliance, and contextual ads

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# Child data law compliance, CARU compliance, and contextual ads#

Child data laws, including but not limited to the Children’s Online Privacy
Protection Act ([COPPA](https://www.ftc.gov/enforcement/rules/rulemaking-
regulatory-reform-proceedings/childrens-online-privacy-protection-rule)),
impose restrictions on how data can be collected and used from age-restricted
users (for example, children under the age of 13, 16, or 18 depending on the
applicable laws). Unity Ads provides game-level and user-level features to
help publishers provide a safe and positive user experience to those users
protected by relevant child data laws. Each Unity Ads-enabled project must
specify whether their game targets age-restricted users.

**Attention** : It is your responsibility to ensure your App-level and User-
level age designations are set up accurately in the Unity Ads Monetization
dashboard.

There are two types of ads that can appear in your game:

  * **Personalized** ads leverage behavioral user data to serve content that is more likely to interest the user. For example, if a user has played a series of sport-themed games, ads for other games with similar sports themes might appear. Games targeting age-restricted users cannot serve personalized ads. Games that serve personalized ads tend to accrue more revenue than games that allow contextual ads.
  * **Contextual** ads are only based on the game that the user is currently playing. For example, if the user is playing a game that features basketball, other games that feature basketball are likely to appear, regardless of other games the user has played. Games that target age-restricted users can only serve contextual ads. Games that only serve contextual ads tend to accrue less revenue than games that allow personalized ads.

## Setting game-level age designations#

Selecting an age designation or compliance option determines how ad requests
are processed in your project. At the game-level, all ad requests are treated
as all child traffic or all adult traffic, depending on if your audience is
children (as defined by applicable child data laws) or adults.

If your project is aimed at both children and adults, you can implement age
designations at the user-level so you can specify the ad served by the user’s
age group. Refer to [Implementing user-level age designations](/ads/en-
us/manual/COPPACompliance#UserLevel) for details.

These are the [Child data law compliance
options](https://docs.unity.com/monetization-
dashboard/ProjectSettings.html#PrivacySettings) available through the
[Monetization dashboard](http://cloud.unity.com/monetization):

  * **This project is directed to children** means the game falls under relevant child data law restrictions, and can therefore only serve contextual (non-targeted) ads to all users. This designation permits you to [enable user-specific age](/ads/manual/COPPACompliance#UserLevel) designations solely for applications you also designate as mixed audience applications.
  * **This project is not directed to children** means the game does not fall under relevant child data law restrictions, and can therefore serve behavioral (targeted) ads to all users.
  * **Mixed audience** means that the project is directed to both children and adult users, as defined by relevant child data laws. For mixed audience projects, instead of handling all users uniformly and serving personalized ads or contextual ads to all regardless of their age, you can detect at the individual level what age group your users are and serve each user ads accordingly, following COPPA or other applicable child data law restrictions.

**Note** : To enable a Mixed Audience designation to your project, you must
first select your project to be directed to children at the game-level age
designation section.

## Implementing user-level age designations#

**Note** : You are only able to implement user-level age designations if your
project is enabled for a mixed audience.

In the Monetization dashboard, game-level age designations treat ad requests
uniformly as if all users are children or adults. When you select the option
that your project has a mixed audience, you are able to track your users’
individual signals and treat them as if they are a child or an adult, and
serve contextual ads or personalized ads, respectively. If a signal is
unspecified for any reason, contextual ads are served by default.

If your app is directed to children but you want to more appropriately
represent a mixed audience, you can programmatically assign users an age
designation according to a flag passed to the Unity Ads SDK.

To do this, implement the nonbehavioral metadata API according to your
specific use case in the following sections.

**Important** : When the nonbehavioral field is **true** , the user cannot
receive personalized ads. When the nonbehavioral field is **false** , the user
can receive personalized ads. You must communicate the appropriate age-
restricted status every time the SDK initializes to ensure that Unity Ads does
not incorrectly treat a user as a child, as an adult opting out of
personalized ads, or an adult consenting to personalized ads during their
session.

### Unity Ads exclusive and self-mediated customers#

If your project sends signals to Unity directly instead of through a partner
mediator (MAX, ironSource, or AdMob) and you want to implement user-level age
designations:

  1. Implement a way to determine if the user should receive personalized ads. How you do this is up to your discretion.
  2. Communicate the age-restricted status of each user to Unity by implementing the nonbehavioral metadata API.
  3. Rebuild your application.
  4. In the Monetization dashboard, go to your project settings, then the **Privacy settings** section, and set the Game-level age designation to **This app is directed to children** , and **Is this a Mixed Audience Game?** to **Yes**.

### Third-party mediation customers#

If your project uses a supported mediation platform and you want to implement
user-level age designations:

  1. Implement a way to determine if the user should receive personalized ads. How you do this is up to your discretion.

  2. Follow your mediation provider’s documentation on how to communicate that information to their platform. We currently support [ironSource](https://developers.is.com/ironsource-mobile/general/ironsource-mobile-child-directed-apps/#step-2), [MAX](https://dash.applovin.com/documentation/mediation), and [AdMob](https://support.google.com/admob/answer/6223431?hl=en) as third-party mediation solutions for user-level age designations.

**Note** : For more information on initializing Unity Ads for your project and
selecting a provider, refer to the [mediation
partner](https://docs.unity.com/monetization-
dashboard/EnablingUnityAds.html#Mediation_partner) documentation.

  3. In the Monetization dashboard, go to your project settings, then the **Privacy settings** section, and set the Game-level age designation to **This app is directed to children** , and **Is this a Mixed Audience Game?** to **Yes**.

### Third-party mediation platforms#

If you are a third-party mediation provider that wants to support sending
user-level age-restricted signals to Unity on behalf of developers, reach out
to customer support or your managing partner.

**Note** : We currently support
[ironSource](https://developers.is.com/ironsource-mobile/general/ironsource-
mobile-child-directed-apps/#step-2),
[MAX](https://dash.applovin.com/documentation/mediation), and
[AdMob](https://support.google.com/admob/answer/6223431?hl=en) as third-party
mediation solutions for user-level age designations. For more information on
initializing Unity Ads for your project and selecting a provider, refer to the
[mediation partner](https://docs.unity.com/monetization-
dashboard/EnablingUnityAds.html#Mediation_partner) documentation.

## Tracking user-specific age-restricted signals#

From the Project Settings page of the Monetization dashboard, after setting
the game-level age designation to be a mixed audience and implementing user-
level age designations in your app, you can then track the following:

  * User signal statuses in your app, per platform, if applicable
  * What the audience breakdown is between adult traffic and child traffic

Considering the age gate implementation in your app code correctly follows the
age-restricted group definition of children (as defined by applicable child
data laws) and adults, all unspecified traffic is composed of users who do not
consent in sharing their age or age group in your app. In this case,
unspecified traffic is treated as child traffic to be compliant with child
data law restrictions. As a result, the sum of child traffic and unspecified
traffic makes up the total of users who will be served contextual ads.

**Important** : It is your responsibility as the publisher to ensure your age
gate implementation is compliant with applicable law and the intent of this
user-level age-restricted feature. It’s not the responsibility of Unity or the
Unity Ads SDK to validate your age gate mechanism, or how the relevant signal
information gets translated and passed to Unity for processing.

### Nonbehavioral metadata API implementation#

_Unity (C#) example_

    
    
    // If the user opts out of personalized ads:
    MetaData userMetaData = new MetaData("user");
    userMetaData.Set("nonbehavioral", "true");
    Advertisement.SetMetaData(userMetaData);
    
    // If the user opts in to personalized ads:
    MetaData userMetaData = new MetaData("user");
    userMetaData.Set("nonbehavioral", "false");
    Advertisement.SetMetaData(userMetaData);

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

_Android (Java) example_

    
    
    // If the user opts out of personalized ads:
    MetaData userMetaData = new MetaData(this);
    userMetaData.set("user.nonbehavioral", true);
    userMetaData.commit();
    
    // If the user opts in to personalized ads:
    MetaData userMetaData = new MetaData(this);
    userMetaData.set("user.nonbehavioral", false);
    userMetaData.commit();

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

_iOS (Objective-C) example_

    
    
    // If the user opts out of personalized ads:
    UADSMetaData *userMetaData = [[UADSMetaData alloc] init];
    [userMetaData set:@"user.nonbehavioral" value:@YES];
    [userMetaData commit];
    
    // If the user opts in to personalized ads:
    UADSMetaData *userMetaData = [[UADSMetaData alloc] init];
    [userMetaData set:@"user.nonbehavioral" value:@NO];
    [userMetaData commit];

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

If a user takes no action to confirm their age (for example, they close a
prompt), we recommend that you re-prompt them at a later time. Users with an
undefined individual age-restricted status will see ads consistent with the
[default behavior](https://docs.unity.com/monetization-
dashboard/ProjectSettings.htm#DefaultBehavior) as defined in the Monetization
dashboard.

## CARU compliance#

The Children’s Advertising Review Unit (CARU) promotes responsible advertising
and privacy practices to children under the age of 13. To assist with our
customers’ compliance with CARU guidelines, all COPPA ads have a watermark
that identifies the ad as an “Advertisement” and have bolded the exit and skip
buttons.

  * Child data law compliance, CARU compliance, and contextual ads
  * Setting game-level age designations
  * Implementing user-level age designations
  * Unity Ads exclusive and self-mediated customers
  * Third-party mediation customers
  * Third-party mediation platforms
  * Tracking user-specific age-restricted signals
  * Nonbehavioral metadata API implementation
  * CARU compliance

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
  2. Implementing custom age gates

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# Implementing custom age gates#

If a publisher or mediator implements a custom age gate solution, they can use
the following API to pass an age gate flag to the Unity Ads SDK. If Unity
receives this flag, its built-in age gate will not appear.

## Unity (C#)#

    
    
    // If the user is over the specified age limit:
    MetaData ageGateMetaData = new MetaData("privacy");
    ageGateMetaData.Set("useroveragelimit", "true");
    Advertisement.SetMetaData(ageGateMetaData);
     
    // If the user is under the specified age limit:
    MetaData ageGateMetaData = new MetaData("privacy");
    gdprMetaData.Set("useroveragelimit", "false");
    Advertisement.SetMetaData(ageGateMetaData);

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value. The second parameter is an object (a
string in this example). Using a boolean value will result in an error.

## iOS (Objective-C)#

    
    
    // If the user is over the specified age limit:
    				UADSMetaData *ageGateMetaData = [[UADSMetaData alloc] init];
    				[ageGateMetaData set:@"privacy.useroveragelimit" value:@YES];
    				[ageGateMetaData commit];
    				 
    				// If the user is under the specified age limit:
    				UADSMetaData *ageGateMetaData = [[UADSMetaData alloc] init];
    				[ageGateMetaData set:@"privacy.useroveragelimit" value:@NO];
    			[ageGateMetaData commit];

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

## Android (Java)#

    
    
    // If the user is over the specified age limit:
    MetaData ageGateMetaData = new MetaData(this);
    ageGateMetaData.set("privacy.useroveragelimit", true);
    ageGateMetaData.commit();
     
    // If the user is under the specified age limit:
    MetaData ageGateMetaData = new MetaData(this);
    ageGateMetaData.set("privacy.useroveragelimit", false);
    ageGateMetaData.commit();

**Note** : You must commit the changes to the `MetaData` object for each value
before trying to set another value.

  * Implementing custom age gates
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
  2. Apple privacy survey for Unity Ads

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

English日本語 (日本)한국어(대한민국)中文（中国）Tiếng Việt (Việt Nam)

# Apple privacy survey for Unity Ads#

As of December 8, 2020, iOS publishers must define what data their apps
collect, including the data collected by integrated third-party SDKs such as
Unity Ads. For your convenience, Unity Ads provides information on its data
collection practices as of August 2021 in the following sections.

**Important** : The data disclosures in the following sections are only for
the Unity Ads SDK. You are also responsible for providing any additional
disclosures for your app, including other third-party SDKs used in your app.

For more information on Apple's data collection disclosure policies, including
terminology definitions, refer to the [Apple
documentation](https://developer.apple.com/app-store/app-privacy-details/).

**Contact info data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Name** For example, first or last name.| No| Not applicable| Not applicable  
**Email Address** Including, but not limited to a hashed email address.| No|
Not applicable| Not applicable  
**Phone Number** Including, but not limited to a hashed phone number.| No| Not
applicable| Not applicable  
**Physical Address** Such as home address, physical address, or mailing
address.| No| Not applicable| Not applicable  
**Other User Contact Info** Any other information that can be used to contact
the user outside the app.| No| Not applicable| Not applicable  
**Health and Fitness data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Health** Health and medical data, including but not limited to from the
Clinical Health Records API, HealthKit API, MovementDisorder APIs, or health-
related human subject research or any other user-provided health or medical
data.| No| Not applicable| Not applicable  
**Fitness** Fitness and exercise data, including but not limited to the Motion
and Fitness API.| No| Not applicable| Not applicable  
**Financial data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Payment Info** Such as form of payment, payment card number, or bank account
number.| No| Not applicable| Not applicable  
**Credit Info** Such as a credit score.| No| Not applicable| Not applicable  
**Other Financial Info** Such as salary, income, assets, debts, or any other
financial information.| No| Not applicable| Not applicable  
**Location data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Precise Location** Information that describes the location of a user or
device with the same or greater resolution as a latitude and longitude with
three or more decimal places.| No| Not applicable| Not applicable  
**Coarse Location** Information that describes the location of a user or
device with lower resolution than a latitude and longitude with three or more
decimal places, such as approximate location services.| Yes| Not applicable|
Third-party advertising, and analytics

> **Note** : For example, Unity collects country-level information for
> regulatory compliance and campaign targeting.  
  
**Sensitive data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Sensitive Info** Such as racial or ethnic data, sexual orientation,
pregnancy or childbirth information, disability, religious or philosophical
beliefs, trade union membership, political opinion, genetic information, or
biometric data.| No| Not applicable| Not applicable  
**Contact data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Contacts** Such as a list of contacts in the user’s phone, address book, or
social graph.| No| Not applicable| Not applicable  
User content| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Emails or Text Messages** Including subject line, sender, recipients, and
contents of the email or message.| No| Not applicable| Not applicable  
**Photos or Videos** The user's photos or videos.| No| Not applicable| Not
applicable  
**Audio Data** The user's voice or sound recordings.| No| Not applicable| Not
applicable  
**Customer Support** Data generated by the user during a customer support
request.| May collect data| Not linked to user| App functionality

> **Note** : Unity Ads may collect this information if a user submits a report
> of an ad creative.  
  
**Other User Content** Any other user-generated content.| No| Not applicable|
Not applicable  
**Browsing data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Browsing History** Information about the content the user has viewed that is
not part of the app, such as websites.| No| Not applicable| Not applicable  
**Search data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Search History** Information about searches performed in the app.| No| Not
applicable| Not applicable  
**Identifier data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**User ID** Such as screen name, handle, account ID, assigned user ID,
customer number, or other user- or account-level ID that can be used to
identify a particular user or account.| Yes| Linked to user| App Functionality  
**Device ID** Such as the device's advertising identifier, or other device-
level ID.| Yes| Linked to user| Third-party advertising, tracking, and
analytics

> **Note** : For tracking, enable ATT.  
  
**Purchase data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Purchase History** An account’s or individual’s purchases or purchase
tendencies.| Yes| Linked to user| Third-party advertising, and analytics  
**Usage data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Product Interaction** Such as app launches, taps, clicks, scrolling
information, music listening data, video views, saved place in a game, video,
or song, or other information about how the user interacts with the app.| Yes|
Not applicable| Third-party advertising, and analytics  
**Advertising Data** Such as information about the advertisements the user has
seen.| Yes| Linked to user| Third-party advertising, and analytics  
**Other Usage Data** Any other data about user activity in the app.| Yes|
Linked to user| Third-party advertising, and analytics  
**Diagnostic data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Crash Data** Such as crash logs.| No| Not applicable| Not applicable  
**Performance Data** Such as launch time, hang rate, or energy use.| Yes|
Linked to user| App functionality and analytics

> **Note** : For example, Unity collects initialization speeds and energy use
> to analyze, develop, and improve the SDK.  
  
**Other Diagnostic Data** Any other data collected for the purposes of
measuring technical diagnostics related to the app.| No| Not applicable| Not
applicable  
**Other data**| **Collected?**| **Linked to user?**| **Purpose**  
---|---|---|---  
**Other Data Types** Any other data types not mentioned.| Yes| Linked to user|
App functionality, third-party advertising, and analytics

> **Note** : For example, Unity collects data like device language, make,
> model, screen size, and connection type, to deliver compatible
> advertisements.  
  
  * Apple privacy survey for Unity Ads

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

