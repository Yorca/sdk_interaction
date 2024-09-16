SDK name: PubNative(verve)
Documentation:
Jump to Content

[![Verve Group](https://files.readme.io/6594076-small-verve-
logo.png)](https://verve.com/)

[ __API Reference](/reference)

v3.0

* * *

[Log In](/login?redirect_uri=/reference/hybid-android-configuration)[![Verve
Group](https://files.readme.io/6594076-small-verve-
logo.png)](https://verve.com/)

 __API Reference

[Log In](/login?redirect_uri=/reference/hybid-android-configuration)

Moon (Dark Mode)Sun (Light Mode)

v3.0[ __API Reference](/reference) HyBid Android SDK - HyBid Configuration

Search

JUMP TO

## [PUBLISHER] Before Getting Started

  * [Getting Started](/reference/before-getting-started)
  * [App-ads.txt for Verve](/reference/app-adstxt-for-pubnative)

## [PUBLISHER] API Documentation

  * [OpenRTB API](/reference/openrtb-api)
  * [VAST APIget](/reference/pubnative-vast-tag)
  * [Reporting API](/reference/reporting-api)

## [PUBLISHER] HyBid Cloud

  * [HyBid Cloud | Documentation](/reference/hybid-cloud-documentation)

## [PUBLISHER] HyBid SDK

  * [HyBid Android SDK - standalone](/reference/hybid-android-sdk)
  * [HyBid iOS SDK - standalone](/reference/hybid-ios-sdk)
  * [iOS 14+ and SKAdNetwork](/reference/ios14-and-skadnetwork)
  * [Google Play Data Safety Guidance](/reference/data-safety-guidance)
  * [Publisher | ATOM via HyBid](/reference/publisher-atom-via-hybid)

## Ad Experience

  * [SKOverlay](/reference/skoverlay)
  * [Autostorekit](/reference/storekit-auto-open)
  * [Custom End Card](/reference/custom-end-card)
  * [Custom Call-to-Action (CTA)](/reference/custom-call-to-action-cta)

## [PUBLISHER] Mediation

  * [GAD / Admob (Android)](/reference/hybid-android-sdk-adapter-for-admob)
  * [GAD / AdMob (iOS)](/reference/hybid-ios-sdk-adapter-for-admob)
  * [Google Ad Manager (iOS & Android)](/reference/google-ad-manager-adops-mediation-setup)
  * [IronSource LevelPlay iOS](/reference/ironsource-levelplay)
  * [IronSource LevelPlay Android](/reference/ironsource-levelplay-android)

## [PUBLISHER] Header Bidding

  * [AppLovin MAX (Android) Bidding](/reference/applovin-max-android-bidding)
  * [AppLovin MAX (iOS) Bidding](/reference/applovin-max-ios-bidding)
  * [Prebid - Adding Verve as bidder](/reference/prebid-adding-pubnative-as-a-bidder)
  * [Google Ad Manager Header Bidding (iOS & Android)](/reference/google-ad-manager-adops-header-bidding-setup)

## [PUBLISHER] Advanced Setup

  * [GDPR Configurations](/reference/gdpr-configurations)
  * [CCPA Configurations](/reference/ccpa-configurations)
  * [Contextual App Targeting](/reference/contextual-app-targeting)

## [DSP] Open RTB 2.6

  * [Overall Integration Process](/reference/overall-integration-process)
  * [Technical Integration Guide](/reference/dsp-openrtb-technical-integration)
  * [Demand Reporting API](/reference/reporting-api-for-dsp)
  * [Bid Loss Notification](/reference/bid-loss-notification)
  * [Win Notification & Minimum Bid To Win](/reference/win-notification-minimum-bid-to-win)
  * [DSP | ATOM via HyBid](/reference/dsp-atom-via-hybid)

Powered by [ __](https://readme.com?ref_src=hub&project=verve)

JUMP TO

## [PUBLISHER] Before Getting Started

  * [Getting Started](/reference/before-getting-started)
  * [App-ads.txt for Verve](/reference/app-adstxt-for-pubnative)

## [PUBLISHER] API Documentation

  * [OpenRTB API](/reference/openrtb-api)
  * [VAST APIget](/reference/pubnative-vast-tag)
  * [Reporting API](/reference/reporting-api)

## [PUBLISHER] HyBid Cloud

  * [HyBid Cloud | Documentation](/reference/hybid-cloud-documentation)

## [PUBLISHER] HyBid SDK

  * [HyBid Android SDK - standalone](/reference/hybid-android-sdk)
  * [HyBid iOS SDK - standalone](/reference/hybid-ios-sdk)
  * [iOS 14+ and SKAdNetwork](/reference/ios14-and-skadnetwork)
  * [Google Play Data Safety Guidance](/reference/data-safety-guidance)
  * [Publisher | ATOM via HyBid](/reference/publisher-atom-via-hybid)

## Ad Experience

  * [SKOverlay](/reference/skoverlay)
  * [Autostorekit](/reference/storekit-auto-open)
  * [Custom End Card](/reference/custom-end-card)
  * [Custom Call-to-Action (CTA)](/reference/custom-call-to-action-cta)

## [PUBLISHER] Mediation

  * [GAD / Admob (Android)](/reference/hybid-android-sdk-adapter-for-admob)
  * [GAD / AdMob (iOS)](/reference/hybid-ios-sdk-adapter-for-admob)
  * [Google Ad Manager (iOS & Android)](/reference/google-ad-manager-adops-mediation-setup)
  * [IronSource LevelPlay iOS](/reference/ironsource-levelplay)
  * [IronSource LevelPlay Android](/reference/ironsource-levelplay-android)

## [PUBLISHER] Header Bidding

  * [AppLovin MAX (Android) Bidding](/reference/applovin-max-android-bidding)
  * [AppLovin MAX (iOS) Bidding](/reference/applovin-max-ios-bidding)
  * [Prebid - Adding Verve as bidder](/reference/prebid-adding-pubnative-as-a-bidder)
  * [Google Ad Manager Header Bidding (iOS & Android)](/reference/google-ad-manager-adops-header-bidding-setup)

## [PUBLISHER] Advanced Setup

  * [GDPR Configurations](/reference/gdpr-configurations)
  * [CCPA Configurations](/reference/ccpa-configurations)
  * [Contextual App Targeting](/reference/contextual-app-targeting)

## [DSP] Open RTB 2.6

  * [Overall Integration Process](/reference/overall-integration-process)
  * [Technical Integration Guide](/reference/dsp-openrtb-technical-integration)
  * [Demand Reporting API](/reference/reporting-api-for-dsp)
  * [Bid Loss Notification](/reference/bid-loss-notification)
  * [Win Notification & Minimum Bid To Win](/reference/win-notification-minimum-bid-to-win)
  * [DSP | ATOM via HyBid](/reference/dsp-atom-via-hybid)

Powered by [ __](https://readme.com?ref_src=hub&project=verve)

# HyBid Android SDK - HyBid Configuration

Requirements:

  * PubNative **App Token** from the PubNative Publisher Dashboard 

##

Install using Gradle

Add PubNative Maven repo to your project level **build.gradle** file:

Groovy

    
    
    buildscript {
        repositories {
            // Other dependencies
            maven { url 'https://verve.jfrog.io/artifactory/verve-gradle-release' }
        }
        dependencies {
            // ...
        }
    }
    
    allprojects {
        repositories {
            // Other dependencies
            maven { url 'https://verve.jfrog.io/artifactory/verve-gradle-release' }
        }
    }
    

Add HyBid SDK dependency to the module level **build.gradle** file:

Groovy

    
    
    implementation 'net.pubnative:hybid.sdk:3.0.2'
    implementation 'net.pubnative:hybid.adapters.dfp:3.0.2'
    implementation 'net.pubnative:hybid.adapters.admob:3.0.2'
    

##

Manifest Permissions

To enable the basic features of the PN Lite SDK, the following permissions
must be added in the **AndroidManifest.xml** file:

XML

    
    
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    

For improved targeting and therefore higher eCPMs you can add this other
permissions but keep in mind that the user needs to approve them explicitly on
Android versions 6 or higher.

XML

    
    
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    
    <!-- For location use one of the following permissions -->
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <!-- or -->
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    

##

SDK initialisation

On your main Activity or your Application class **onCreate** method you should
initialise the SDK using the app token that was provided to you in the
PubNative Publisher Dashboard.

Java

    
    
    HyBid.initialize("APP_TOKEN", this);
    

##

Advanced configurations

##

Proguard

If you are using Proguard in your gradle build, you should add these lines to
your proguard file:

Java

    
    
    -keepattributes Signature
    -keep class net.pubnative.** { *; }
    -keep class com.iab.omid.library.pubnativenet.** { *; }
    

##

Test mode

During development and testing of the SDK integration it is recommended to
enable test mode. This will make the impressions and click not count on the
PubNative side. Testing without enabling this mode could result in your
account getting blocked because the traffic will be considered fraudulent.

Test mode is disabled by default. To enable test mode, you should use this
line in the same location where you initialise the SDK:

Java

    
    
    HyBid.setTestMode(true);
    

##

Location tracking

If the user has given location permissions, HyBid SDK will use the available
user location to provide better targeted ads.  
This feature is enabled by default, but can be disabled by setting the
**setLocationTrackingEnabled** on the HyBid class:

Java

    
    
    HyBid.setLocationTrackingEnabled(false);
    

##

Location updates

The SDK refreshes the user location after every ad request if the user has
given permission for location tracking. This is done to keep the best accuracy
possible. However if the app will do many requests in a short time it might
display location updates very often which can be intrusive for some users.

You can disable this behaviour by setting the **setLocationUpdatesEnabled** on
the HyBid class:

Java

    
    
    HyBid.setLocationUpdatesEnabled(false);
    

Keep in mind that if location tracking is disabled, anything you set in here
will have no effect since location tracking will be disabled globally for
HyBid SDK

##

Enable COPPA compliance

If your app is intended for children you should enable the
**[COPPA](https://en.wikipedia.org/wiki/Children%27s_Online_Privacy_Protection_Act)**
compatibility in order to protect the privacy of the information in their
devices. It is disabled by default.

Java

    
    
    HyBid.setCoppaEnabled(true);
    

##

Targeting parameters

You can add extra information to the requests the SDK makes to the ad server.
This can result in higher eCPMs and more accurate ads for the users.

You can set the age, gender and some related keywords that can help improve
the audience targeting in the delivered ads.

Java

    
    
    HyBid.setAge("30");
    HyBid.setGender("female");
    HyBid.setKeywords("sports,racket,tennis");
    

  * __Table of Contents
  *     * Install using Gradle
    * Manifest Permissions
    * SDK initialisation
    * Advanced configurations
    * Proguard
    * Test mode
    * Location tracking
    * Location updates
    * Enable COPPA compliance
    * Targeting parameters

window.dataLayer = window.dataLayer || []; function
gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config',
'G-3VGRZZGHXS');

