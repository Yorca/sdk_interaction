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

