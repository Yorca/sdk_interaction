Skip to main content

[![Appodeal logo](/img/logo.svg)![Appodeal logo](/img/logo.svg)**Help
Center**](/)

SDK Guides

  * [Android SDK](/android/get-started)
  * [iOS SDK](/ios/get-started)
  * [Unity Plugin](/unity/get-started)

* * *

  * [React-Native Plugin](https://github.com/appodeal/react-native-appodeal)
  * [Flutter Plugin](https://github.com/appodeal/Appodeal-Flutter-Plugin)

* * *

  * [SDK Deprecation Policy](/advanced/sdk-deprecation-policy)

General

  * [Network Setup](/networks-setup/introduction)
  * [FAQ & Troubleshooting](/faq-and-troubleshooting/faq/generate-the-json-file-in-google-cloud)
  * [Reporting](/reporting/reporting-api)
  * [Advanced](/advanced/ad-revenue-attribution)
  * [Accelerator Soft Launch](/accelerator/introduction)

[DashboardArrow Forward](https://app.appodeal.com/analytics/overview)

Search

English

  * [English](/android/data-protection/coppa)
  * [Русский](/ru/android/data-protection/coppa)

[Sign in](https://app.appodeal.com/signin)

#### Android SDK

[3.3.2](/android/get-started)

  * [3.3.2](/android/data-protection/coppa)
  * Archived versions
  * [3.2.1](https://0e7e302e.appodeal-sdk-docs-prod.pages.dev/android/get-started)
  * [3.1.3](https://c3798d39.appodeal-sdk-docs-prod.pages.dev/android/3.1.3/get-started)

  * [Get Started](/android/get-started)
  * [Ad Types](/android/ad-types/interstitial)

    * [Interstitial](/android/ad-types/interstitial)
    * [Rewarded Video](/android/ad-types/rewarded-video)
    * [Banner](/android/ad-types/banner)
    * [MREC](/android/ad-types/mrec)
    * [Native](/android/ad-types/native)
  * [Services](/android/services/adjust)

    * [Adjust](/android/services/adjust)
    * [AppsFlyer](/android/services/appsflyer)
    * [Firebase](/android/services/firebase)
    * [Meta](/android/services/meta)
  * [Data Protection](/android/data-protection/gdpr-and-ccpa)

    * [GDPR and CCPA](/android/data-protection/gdpr-and-ccpa)
    * [App Privacy Details on the Google Play](/android/data-protection/app-privacy-details)
    * [COPPA](/android/data-protection/coppa)
  * [Advanced](/android/advanced/configure-mediated-networks)

    * [Configure Mediated Networks](/android/advanced/configure-mediated-networks)
    * [Segments and Placements](/android/advanced/segments-placements)
    * [User Data](/android/advanced/user-data)
    * [Testing](/android/advanced/testing)
    * [Ad Revenue Callbacks](/android/advanced/ad-revenue-callback)
    * [Ad Revenue Forwarding to MMP/BI](/android/advanced/ad-revenue-forwarding)
    * [Event Tracking](/android/advanced/event-tracking)
    * [In-App purchases](/android/advanced/in-app-purchases)
    * [Launching a tROAS campaign in Google Ads](/android/advanced/launching-troas)
  * [Changelog](/android/changelog)
  * [Upgrade guide](/android/upgrade-guide)
  * [SDK Deprecation Policy](/android/sdk-deprecation-policy)

  * [](/)
  * Data Protection
  * COPPA

Version: 3.3.2

# COPPA

For purposes of the [Children's Online Privacy Protection Act
(COPPA)](https://business.ftc.gov/privacy-and-security/children%27s-privacy)
there is a setting called childDirectedTreatment. If your app is designed for
kids you can disable sending user data to ad networks by calling the method
below.

Should be called before the SDK initialization.

  * Kotlin
  * Java

    
    
    Appodeal.setChildDirectedTreatment(value: Boolean?)  
    
    
    
    Appodeal.setChildDirectedTreatment(@Nullable Boolean value);  
    

info

Call `setChildDirectedTreatment` with `true` to indicate that you want your
content treated as child-directed for purposes of COPPA.

Call `setChildDirectedTreatment` with `false` to indicate that you don't want
your content treated as child-directed for purposes of COPPA.

Call `setChildDirectedTreatment` with `null` to indicate that you want to use
the COPPA parameter from your application's settings on the
[appodeal.com](http://appodeal.com/).

* * *

[PreviousApp Privacy Details on the Google Play](/android/data-protection/app-
privacy-details)[NextConfigure Mediated Networks](/android/advanced/configure-
mediated-networks)

![Appodeal logo](/img/logo.svg)![Appodeal logo](/img/logo.svg)

Copyright © 2023 Appodeal, Inc.

  * [Terms of service](https://www.appodeal.com/home/terms-of-service/)
  * [Privacy Policy](https://appodeal.com/privacy-policy)
  * [SDK License Agreement](https://appodeal.com/sdk-license-agreement)

