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

