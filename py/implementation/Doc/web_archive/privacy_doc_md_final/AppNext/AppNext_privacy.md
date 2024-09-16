Jump to Content

[![Appnext Developers
Hub](https://files.readme.io/e863419-All_logos_Colorfor_white_bg_3.svg)](/)

[ __Home](/)[ __Documentation](/docs)[ __Announcements](/changelog)

* * *

[Login](https://www.appnext.com/sign-
in/)[Wiki](https://wiki.appnext.com/hc/en-us)[Go to Main
Site](https://www.appnext.com)[![Appnext Developers
Hub](https://files.readme.io/e863419-All_logos_Colorfor_white_bg_3.svg)](/)

 __Documentation

[Login](https://www.appnext.com/sign-
in/)[Wiki](https://wiki.appnext.com/hc/en-us)[Go to Main
Site](https://www.appnext.com)

[ __Home](/)[ __Documentation](/docs)[ __Announcements](/changelog) Appnext
and the GDPR

Search

## Welcome!

  * [Start here](/docs/start-here-appnext)
  * [Change Log](/docs/change-log)
  * [Legal](/docs/legal)

## Android SDK

  * [ __Getting Started with the Android SDK](/docs/android-sdk-installation)
    * [ Manual Integration](/docs/manual-integration)
  * [Native Ads](/docs/appnext-android-native-ads)
  * [Banners](/docs/appnext-android-banners)
  * [Interstitial](/docs/appnext-android-interstitial)
  * [Rewarded and Fullscreen Video](/docs/appnext-android-rewarded-fullscreen)
  * [Suggested Apps](/docs/suggested-apps)
  * [ __Admob Adapter Installation](/docs/appnext-android-admob-adapter-installation)
    * [ Banners](/docs/banners)
    * [Interstitial](/docs/interstitial)
    * [Rewarded](/docs/rewarded)
    * [Fullscreen Video](/docs/fullscreen-video)
  * [MAX Applovin Adapter Integration](/docs/max-applovin-adapter-integration)
  * [Appnext and the GDPR](/docs/appnext-android-sdk-gdpr)

## REACT NAtive

  * [React Native SDK](/docs/react-native-sdk)

## OOBE

  * [Preload](/docs/getting-started-with-the-oobe)

## Plugins

  * [ __Unity Plugin](/docs/appnext-unity-plugin)
    * [ Interstitial](/docs/appnext-unity-plugin-interstitial)
    * [Rewarded and Fullscreen Video](/docs/appnext-unity-rewarded-fullscreen-video)
  * [ __Adobe Air Plugin](/docs/appnext-adobe-air-plugin)
    * [ Interstitial](/docs/appnext-adobe-air-plugin-interstitial)
    * [Rewarded and Fullscreen](/docs/appnext-adobe-air-plugin-rewarded-fullscreen-video)
    * [Banners](/docs/appnext-adobe-air-plugin-banners)
    * [Native Ads](/docs/appnext-adobe-air-plugin-native-ads)

## API

  * [ __Native Ads API](/docs/api-new-page)
    * [ Requesting raw ad data for Android and iOS](/docs/requesting-raw-ad-data-for-android-and-ios)
    * [Campaigns response](/docs/campaigns-response)
    * [Server Side & Client Side](/docs/server-side-client-side)
    * [Measurement and reporting](/docs/measurement-and-reporting)
  * [VAST API](/docs/appnext-vast-api)
  * [Media Partners API](/docs/appnext-media-partners-api)

# Appnext and the GDPR

Appnext Android SDK and the GDPR

[ __Suggest Edits](/edit/appnext-android-sdk-gdpr)

##

Appnext and the GDPR

On May 25th, 2018, the new EU data protection regulatory framework – the
General Data Protection Regulation ("GDPR") – will come into effect.

Appnext takes considerable efforts to ensure that its privacy practices comply
with data protection laws and the industry's best practices.

For publishers who are implementing CMP ("Consent Management Platform") - It
is possible to forward the end-user consent status to Appnext SDK - see below.

For publishers who don't implement CMP or are not require consent from their
end-users, Appnext is GDPR compliant under the "Legitimate Interest" legal
basis; On this case, the publisher is required to provide a transparency to
the end-user indicating that Appnext SDK is in use.

> ## 🚧
>
> Please Note!
>
> The text in this page is provided for guidance and educational purposes
> only. The responsibilities and liabilities of Appnext to its partners and
> customers are controlled by Appnext agreements. For more information,
> contact your success manager/Appnext support.

##

Working with Appnext SDK directly

It is possible to forward the consent status to Appnext SDK on each time the
SDK is initialized using a dedicated `setConsent` function;

The consent boolean value should be passed on each SDK session.

Example:

Java

    
    
    Appnext.init(context);
    // The publisher should check the consent status on each SDK session;
    if (...) {
      //Positive consent is provided by the end-user
     Appnext.setConsent(context, true);
    } else {
      //Negative consent is provided by the end-user
     Appnext.setConsent(context, false);
    }
    

##

Working with Mopub SDK

Appnext is not an official Mopub partner. This means that you will have to
forward the negative consent to Appnext manually;

Mopub's `MoPub.canCollectPersonalInformation()` can provide the boolean status
of the end-user's consent

Example:

Java

    
    
    //Initilize the Appnext SDK
    Appnext.init(context);
    
    //Forward the end-user consent from the MoPub SDK;
    PersonalInfoManager personalInfoManager = MoPub.getPersonalInformationManager();
    if (personalInfoManager != null && personalInfoManager.gdprApplies()) {
     boolean userProvidedConsent = personalInfoManager.canCollectPersonalInformation();
     Appnext.setParam("consent", String.valueOf(userProvidedConsent));
    }
    

Please refer to Mopub's website for more information about working with
Mopub's consent CMP

##

Working with Google Consent SDK

Google will introduce its own consent SDK (CMP) by the end of May 2018. Once
the SDK will be released, Appnext will publish integration instructions on how
to pass a negative consent to its Android SDK.

##

Working with the IAB consent framework

IAB Europe is in the process of releasing a unified framework for getting the
end-users consent when working with in-apps. The framework is still in draft
status, pending final requirements. Appnext is constantly monitoring the
framework maturity level. Once the IAB will get the framework to a final
status Appnext will implement it on its SDK.

##

Support & Integration

Should you have any problems integrating the product, log a ticket with us by
emailing [[email protected]](/cdn-cgi/l/email-
protection#1d6e686d6d726f695d7c6d6d73786569337e7270).

__Updated 2 months ago

* * *

  * __Table of Contents
  *     * Appnext and the GDPR
    * Working with Appnext SDK directly
    * Working with Mopub SDK
    * Working with Google Consent SDK
    * Working with the IAB consent framework
    * Support & Integration

SOLUTION

  * [Publishers](https://www.appnext.com/publishers/)
  * [Adverisers](https://www.appnext.com/advertisers/)
  * [OEMs](https://www.appnext.com/oems-operators/)
  * [Technonogy](https://www.appnext.com/technology/)

Company

  * [About Us](https://www.appnext.com/about-us/)
  * [Careers](https://www.appnext.com/career/)
  * [Contact Us](https://www.appnext.com/contact-us/)

Resources

  * [Blog](https://blog.appnext.com/)
  * [Events](https://www.appnext.com/events/)
  * [News](https://www.appnext.com/news/)
  * [Case Studies](https://www.appnext.com/case-studies-app/)

Legal

  * [Privacy Policy](https://www.appnext.com/privacy-policy-oem-operators/)
  * [General Terms & Conditions](https://www.appnext.com/terms-of-service/)
  * [DPA](https://www.appnext.com/dpa/)
  * [GDPR](https://www.appnext.com/gdpr/)

Copyright © Appnext 2023

[![](//theme.zdassets.com/theme_assets/647305/0bed995b9012c634a94894c8692eb2dbe21bd88f.svg)](https://www.facebook.com/Appnext)
[![](//theme.zdassets.com/theme_assets/647305/fc98092984f07aac541b2b6ba591ca2dfee5407f.svg)](https://www.linkedin.com/company/appnext/)
[![](//theme.zdassets.com/theme_assets/647305/c261af6c9093812fa9a52cad6c0030a369e13240.svg)](https://twitter.com/appnext_updates)

