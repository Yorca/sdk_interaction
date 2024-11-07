[ ![](/assets/tappx_logo.svg) ](/en)

  * [Log In](https://dashboard.tappx.com)
  * [Join Now](https://dashboard.tappx.com/signup)

[ __ Search ](/en/search)

  * [ES](/es)
  * [EN](/en)

__

  * [ ![](/assets/sidebar/android.svg) Android ](/en/android/sdk-integration-android-studio)
  * [ ![](/assets/sidebar/apple.svg) iOS ](/en/ios/before-you-start)
  * [ ![](/assets/sidebar/unity.svg) Unity ](/en/unity/before-starting)
  * [ ![](/assets/sidebar/phonegap.svg) Phonegap ](/en/phonegap/phonegap-integration-guide)
  * [ ![](/assets/sidebar/amob.svg) AdMob ](/en/admob/app-ads-txt-integration)
  * [ ![](/assets/sidebar/gam.svg) GAM ](/en/gam/app-ads-txt-integration)
  * [ ![](/assets/sidebar/iron_source.svg) Iron Source ](/en/ironsource/app-ads-txt-integration)
  * [ ![](/assets/sidebar/applovin.svg) AppLovin ](/en/applovin/app-ads-txt-integration)

__

  * [ SDK Integration - Android Studio ](/en/android/sdk-integration-android-studio/)
  * [ App-ads.txt Integration ](/en/android/app-ads-txt-integration/)
  * [ SDK Tappx Android GDPR â EU ](/en/android/sdk-tappx-android-gdpr-eu/)
  * [ SDK Tappx Android GPP ](/en/android/sdk-tappx-android-gpp/)
  * [ SDK Tappx Android CCPA ](/en/android/sdk-tappx-android-ccpa/)
  * [ COPPA ](/en/android/COPPA/)
  * [ AndroidManifest.xml ](/en/android/android-manifest-xml-android-studio/)
  * [ Installation tracking ](/en/android/installation-tracking/)
  * [ Request Ads ](/en/android/request-ads/)
  * [ Interstitials/Full Screen for Static or Video ads ](/en/android/interstitials-full-screen/)
  * [ Banners ](/en/android/banners/)
  * [ Rewarded Video ](/en/android/rewarded/)
  * [ Error Codes ](/en/android/error-codes/)
  * [ Additional information in the requests (interstitials and banners) ](/en/android/additional-information-in-the-requests-interstitials-and-banners/)
  * [ Proguard ](/en/android/proguard/)

[Home ](/en) / [Android](/en/android) / [COPPA ](/en/android/COPPA/)

# COPPA

##

### COPPA (Children's Online Privacy Protection Act)

The Children's Online Privacy Protection Act is a regulation, passed in the
United States in 1998, that requires websites and mobile apps to protect data
belonging to children under the age of 13 through clear and accessible privacy
policies and by requesting parental consent. This law also requires the
deletion of children's personal information after a specified period of time,
depending on the purpose of the processing, and prohibits impacting them with
advertising. As an app developer, by using the child-targeted content tag, you
are instructing Tappx and its demand partners to take the necessary steps to
have data tracking and remarketing advertising disabled when an ad request is
made on child-tagged content.  
You must set the child-specific content tag before you start the SDK
integration.

### COPPA integration for Android

In the application of the COPPA regulations, to indicate that the content of
your app is intended for children under 13 years of age, you must use the
following code:

    
    
    Tappx.setCoppaCompliance(context, true);

The value you set (true or false) will determine whether advertising
restrictions will be activated or not.

Tappx Â© 2024

