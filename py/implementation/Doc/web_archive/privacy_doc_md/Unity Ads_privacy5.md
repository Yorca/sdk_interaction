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

