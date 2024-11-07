Jump to Content

[![MobileFuse
Documentation](https://files.readme.io/4a360f4-mf_logo.svg)](/docs)

[ __Home](/)[ __Guides](/docs)[ __API Reference](/reference)[
__Changelog](/changelog)

* * *

[Log In](/login?redirect_uri=/docs/android-location-privacy)[![MobileFuse
Documentation](https://files.readme.io/4a360f4-mf_logo.svg)](/docs)

 __Guides

[Log In](/login?redirect_uri=/docs/android-location-privacy)

[ __Home](/)[ __Guides](/docs)[ __API Reference](/reference)[
__Changelog](/changelog) Android Location Privacy

Search

## Getting Started

  * [Getting Started with MobileFuse](/docs/getting-started)
  * [Integration Types](/docs/integration-types)

## SDK Integration

  * [MobileFuse SDK](/docs/mobilefuse-sdk)
  * [ __iOS](/docs/ios)
    * [ Data Privacy](/docs/ios-sdk-data-privacy)
    * [Interstitial Ads](/docs/ios-interstitial-ads)
    * [Banner Ads](/docs/ios-banner-ads)
    * [Rewarded Ads](/docs/ios-rewarded-ads)
    * [Omni Unit Ads](/docs/ios-omni-ads)
    * [Native Ads](/docs/ios-native-ads)
  * [ __Android](/docs/android)
    * [ Data Privacy](/docs/android-sdk-data-privacy)
    * [Interstitial Ads](/docs/android-interstitial-ads)
    * [Banner Ads](/docs/android-banner-ads)
    * [Rewarded Ads](/docs/android-rewarded-ads)
    * [Omni Unit Ads](/docs/android-omni-ads)
    * [Native Ads](/docs/android-native-ads)
    * [Android Location Privacy](/docs/android-location-privacy)
  * [Testing SDK Integrations](/docs/testing-sdk-integrations)
  * [Advanced SDK Configuration](/docs/advanced-configuration)
  * [SDK Error Codes](/docs/error-codes)
  * [RampID and UID2](/docs/sdk-rampid-and-uid2)
  * [SDK Bidding](/docs/sdk-bidding)

## Applovin MAX Integration

  * [Overview](/docs/applovin-max)
  * [MAX Console Setup](/docs/max-console-setup)
  * [MAX Ad Units (Bidding)](/docs/max-ad-units-bidding)
  * [MAX Ad Units (Waterfall)](/docs/max-ad-units)
  * [Android](/docs/android-max-adapter)
  * [iOS](/docs/ios-max-adapter)
  * [Unity](/docs/unity-max-adapter)

## Chartboost Mediation Integration

  * [Overview](/docs/chartboost-mediation)

## AdMob/GAM Integration

  * [AdMob Mediation/GAM](/docs/admob-mediation)
  * [AdMob/GAM Console Setup](/docs/admob-console-setup)
  * [Android](/docs/android-admob-adapter)
  * [iOS](/docs/ios-admob-adapter)

## OpenRTB Integration

  * [Overview](/docs/openrtb)
  * [Bid Requests](/docs/bid-requests)
  * [Bid Responses](/docs/bid-responses)

## Prebid Integration

  * [Overview](/docs/prebid)

## VAST Tag Integration

  * [Client Side VAST Tags](/docs/client-side-vast-tags)
  * [Server Side VAST Tags](/docs/server-side-vast-tags)

## Additional Information

  * [Inventory Policies](/docs/inventory-policies)
  * [Privacy & Compliance](/docs/privacy-compliance)
  * [Leveraging Unique IDs: RampID, UID2, and CoreID](/docs/leveraging-rampid-and-uid2)
  * [app-ads.txt lines](/docs/app-adstxt)
  * [Apple SKAdNetwork IDs](/docs/apple-skadnetwork-ids)
  * [Supported Countries](/docs/supported-countries)
  * [Metric Glossary](/docs/metric-glossary)
  * [Impression TTL](/docs/impression-ttl)
  * [Impression Counting Methodology](/docs/impression-counting-methodology)
  * [Platform Macros](/docs/platform-macros)

Powered by [ __](https://readme.com?ref_src=hub&project=mobilefuse)

# Android Location Privacy

[ __Suggest Edits](/edit/android-location-privacy)

Your app data privacy consent dialog should allow users to opt-in to location
tracking. By default, the SDK and adapters will assume that your app is
running in a context which requires an opt-out for data usage for ad
personalization.

When a user opts out of personalized ad tracking, the SDK will by default not
collect or transmit any PII, and the MobileFuse server will automatically
scrub any potentially personal information from the bidstream when any opt-out
flags are set (OS level flags, US Privacy, GPP).

If you want to specifically disable location targeting within the Android SDK
then you can call the opt out method as follows:

JavaKotlin

    
    
    MobileFuseTargetingData.setAllowLocation(false);
    
    
    
    MobileFuseTargetingData.allowLocation = false
    

#

Opt-in configuration

If you are required to display a consent dialog to your users before location
information is used for ad personalization, then you can set the MobileFuse
SDK or adapter into an opt-in mode.

To do this, set the following flag in the Android Manifest:

XML

    
    
    <meta-data android:name="com.mobilefuse.sdk.disable_user_location" android:value="true" />
    

Once the SDK has been configured in this mode, you can then pass the user
location preferences to the MobileFuse SDK using the following calls:

JavaKotlin

    
    
    // User has opted in to location-based ad personalization:
    MobileFuseTargetingData.setAllowLocation(true);
    
    // User has opted out of location-based ad personalization:
    MobileFuseTargetingData.setAllowLocation(false);
    
    
    
    // User has opted in to location-based ad personalization:
    MobileFuseTargetingData.allowLocation = true
    
    // User has opted out of location-based ad personalization:
    MobileFuseTargetingData.allowLocation = false
    

__Updated 12 months ago

* * *

  * __Table of Contents
  *     * Opt-in configuration

