SDK name: TappX
Documentation:
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
    * [ Introduction ](/en/android/sdk-tappx-android-ccpa/01_CCPA_Intro_And/)
    * [ Android ](/en/android/sdk-tappx-android-ccpa/01_CCPA_Android_And_Manual/)
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

[Home ](/en) / [Android](/en/android) / [SDK Tappx Android CCPA
](/en/android/sdk-tappx-android-ccpa/) / [Android ](/en/android/sdk-tappx-
android-ccpa/01_CCPA_Android_And_Manual/)

# SDK Tappx Android CCPA

## Android

    
    
      Tappx.getPrivacyManager(context).setUSPrivacy(User_Consent_String_Here);

(Where âUserConsentString_Hereâ must be a valid consent string from your
CMP or tool to get the final user consent)

[ < Previous Page ](/en/android/sdk-tappx-android-ccpa/01_CCPA_Intro_And/)

Tappx Â© 2024

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
    * [ Introduction ](/en/android/sdk-tappx-android-gdpr-eu/1_intro_gdpr_android/)
    * [ Custom / Manual method ](/en/android/sdk-tappx-android-gdpr-eu/1_manual_dev_android/)
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

[Home ](/en) / [Android](/en/android) / [SDK Tappx Android GDPR â EU
](/en/android/sdk-tappx-android-gdpr-eu/) / [Custom / Manual method
](/en/android/sdk-tappx-android-gdpr-eu/1_manual_dev_android/)

# SDK Tappx Android GDPR â EU

## Custom / Manual method

The developer must create their own consent management platform (CMP) or use a
third party and re-submit the information of the user's consent to the Tappx
SDK through the parameters enabled for that purpose. Using this system Tappx
will not show its consent request screen.

**If the user consents to the use of their data, this function should be
called:**

    
    
    Tappx.getPrivacyManager(context).grantPersonalInfoConsent();

In this case you should also pass the gdprConsentString:

    
    
    Tappx.getPrivacyManager(context).setGDPRConsent(String);

**If the user does NOT consent to use their data, this function should be
called:**

    
    
    Tappx.getPrivacyManager(context).denyPersonalInfoConsent();

For any questions regarding GDPR, you can find more information on our
specific GDPR page.

The consent must be requested before showing ads to the user.

If you donât send the consent, the SDK will assume **"DO NOT CONSENT"** by
default, this may cause a decrease in the number of ads being displayed.

[ < Previous Page ](/en/android/sdk-tappx-android-gdpr-
eu/1_intro_gdpr_android/)

Tappx Â© 2024

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
    * [ Introduction ](/en/android/sdk-tappx-android-gpp/1_intro_gpp_android/)
    * [ Custom / Manual method ](/en/android/sdk-tappx-android-gpp/1_manual_dev_android_gpp/)
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

[Home ](/en) / [Android](/en/android) / [SDK Tappx Android GPP
](/en/android/sdk-tappx-android-gpp/) / [Custom / Manual method
](/en/android/sdk-tappx-android-gpp/1_manual_dev_android_gpp/)

# SDK Tappx Android GPP

## Custom / Manual method

**IMPLEMENTATION CODE**

    
    
    Tappx.getPrivacyManager(context).setGlobalPrivacyPlatform("User_Consent_String_Here");

(Where âUserConsentString_Hereâ must be a valid consent string from your
CMP or tool to get the final user consent)

[ < Previous Page ](/en/android/sdk-tappx-android-gpp/1_intro_gpp_android/)

Tappx Â© 2024

