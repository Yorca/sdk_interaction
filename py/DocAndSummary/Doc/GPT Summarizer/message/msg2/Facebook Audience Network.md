SDK name: Facebook Audience Network
Documentation:
[Meta Audience Network](/docs/audience-network)

  * [How To Use This Site](/docs/audience-network/how-to-use-this-site)
  * [Bidding Integration](/docs/audience-network/bidding-integration)
  * [Platform Setup](/docs/audience-network/setting-up/platform-setup)
  * [Ad Setup](/docs/audience-network/setting-up/ad-setup)
  * [Testing Your Setup](/docs/audience-network/setting-up/testing)
  * [Best Practices](/docs/audience-network/optimization/best-practices)
  * [APIs](/docs/audience-network/optimization/apis)
  * [Instant Games](/docs/audience-network/instant-games)
  * [Help](/docs/audience-network/support)

# Information for Child-Directed Apps and Services

When you participate in Meta Audience Network and use the Facebook SDKs in
apps or services that are directed to children, or where you knowingly collect
personal information from children, you are responsible for complying with all
applicable laws. For example, in the United States, operators of web sites,
apps or services that are directed to children under 13 or that knowingly
collect personal information from children under 13 must comply with the [U.S.
Children’s Online Privacy Protection Act
(“COPPA”).](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.business.ftc.gov%2Fprivacy-
and-
security%2Fchildren%2527s-privacy%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR0E0Vay6LoaG9lxitxMhmA514t69CmSKz8_AX94ElewSudttV5i5DPF1eg_aem_-
MVngzvxgGiupTY1vJKDaQ&h=AT320OXBtyrRDktY6JljowmGNbTPTwUBM3mS8i5owsR-
Wc_IXO1yiQ9xcjd7aEGKKV-
cPVljJTwJHat6-U9G6kopEQYZosWpjfMoQ3ako8SEN6Ekw4hNO1H501zehsrgBFge7JJcnIw)

Under the [COPPA
Rule](https://l.facebook.com/l.php?u=http%3A%2F%2Fwww.ecfr.gov%2Fcgi-
bin%2Ftext-
idx%3FSID%3Ded5f76ab1e38b07607347f089c048eb8%26node%3Dse16.1.312_12%26rgn%3Ddiv8%26fbclid%3DIwZXh0bgNhZW0CMTEAAR1D2_zHFRs3cOSNnImc1yikTYzVM4zDorwZzkVxpEvrWsu6v1R-krM02TI_aem_TVWO0NvZSzYi66D5DToWNQ&h=AT0e5G26xStq_PiZUU5t-5ZYW-
ES-
OAmnAr7teBjo6niynwy6Lth1U22UDrkvCtHMaCsdpnszaGeCeAM7NAZYpUM_2E6P102AQtg8mjUKmsZEO5Ix_t-
xQRlcl3fXa2hF6BWTM4Dw9c) and per FTC guidance, developers are responsible for
determining whether or not an app is child directed by looking to “its subject
matter, visual content, use of animated characters or child-oriented
activities and incentives, music or other audio content, age of models,
presence of child celebrities or celebrities who appeal to children, language
or other characteristics of the Web site or online service, as well as whether
advertising promoting or appearing on the Web site or online service is
directed to children . . . [and] competent and reliable empirical evidence
regarding audience composition, and evidence regarding the intended audience.”

If the app is child directed and children under the age of 13 are the primary
audience, then it is “primarily child directed.”

Apps that are child directed, but do not target children as the primary
audience, are “child directed, but mixed audience” services under the COPPA
Rule. If an app is child directed but mixed audience, it can choose to
implement an age gate, a mechanism that asks users to provide their age or
date of birth in an age-neutral way. Child directed, but mixed audience apps
that implement age gates are permitted to differentiate among users for
purposes of COPPA compliance.

This document provides the additional code you are required to use for the
Facebook SDKs if you have determined that your site, app, or service has
obligations under COPPA. Where you use this code depends on your determination
of which of the following categories applies to your site, app, or service.

  1. [Primarily child-directed](/docs/plugins/restrictions#child-directed). Your site, app, or service is [directed to children](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR11_X7uOWmClLEDKaEAltXqcXuMY2iY0v0MPvSrhQ4y3tALI12fhaH-67M_aem__8qBIZXmTCxwQBmqrzFeJw&h=AT1Xbj9ZB8jS87LHjgx1GXyJ4NXTu9kKHbKxuFAGRYnaSUhuVO4mwv_1ArWlnQNUU8zeetNJoN3tR_JKjbiUCNvS3YoW6Fj3sH3DAaIJv0ccq7qA6VT8Uidquezmi2ncy9ncJ0rUEm0) whose primary target audience is children under the age of 13. 
  2. [Mixed audience without age gate](/docs/plugins/restrictions#mixed-no-age-gate). Your site, app, or service is [directed to children](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR1L_JhlqFrN-PxZvg7X1TnVBYLlE98xDhW3hsOKgEngHYnF72hefKYFiAY_aem_YLiRMns8xHhAcPdqhTNAmQ&h=AT2FCxzT1SLjoftLd4qUzGpBXtIWDnQzwnxJiMjSxlHWZzuA3uzcH0BQ434yrrlhH3zwvOBAxwTREBaxjgIfCTew167t7K01ZkAEU3MHbeysAyZNyqOjFE0QYRvfxbGNledyg4rlO64) but its primary target audience is people who are at least 13 years old. Your site, app or service does not include an age gate. An “age gate” generally is a mechanism that asks users to provide their age or date of birth in a non-leading way before they access a website or service. For more information [click here](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR2fc2Ww0ru_JEmR1CbYNBdrJ5PWi7IDLl59NeJgkZ95JlpRwHeDVT_fq3w_aem_KAv5iN-XbqjcQgBFFOxCpA&h=AT0smBVOxgAy1sKanfmQ_LQTaQdV9DNWr2FDJxm8QaG9kGWhOwtoGvpIh1_IOkquzlDZ3SkkthfhSDG9KIUMeDmg0o-0ZDI7ClbXs3VYRFIAraHbWLwTVZz1XQt4byl7WoSQagm-nXo).
  3. [Mixed audience with age gate](/docs/plugins/restrictions#mixed-with-age-gate). Your site, app, or service is [directed to children](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR2C7BIA83CjsamVgArYJZF1ZvH1xTvkgSEQp0EgAGVlkhyUSlTN98T38s4_aem_wG11XviEuGBjNCND7aW2vw&h=AT1woZJPAC0x3A8AVVBiix65PLFyvNLRs03B5-Wqv7KlSH3u0-EngfEv8PcHZJIdeD-9uYjAYVZxhB3KL-jgHeS5VwhKhCXBe39YsZqu6WsHuEqQxhz-7S-cvIWRuDAQ6Zgh7SR1CEk) but its primary target audience is people who are at least 13 years old. Your site, app or service uses an age gate. An “age gate” generally is a mechanism that asks users to provide their age or date of birth in a non-leading way before they access a website or service. For more information [click here](https://l.facebook.com/l.php?u=https%3A%2F%2Fbusiness.ftc.gov%2Fdocuments%2FComplying-with-COPPA-Frequently-Asked-Questions%3Ffbclid%3DIwZXh0bgNhZW0CMTEAAR11Doj2ky65-E5KaOTBxOgYFTejWpiQiyq5W7K7KQXjUqIqopOq2789NZ4_aem_D2-KTtPP3v78NS5j1su-vg&h=AT1w2jUSubBrKkIdmbuP-LcyxQPmo5smJEzl1vulLcLnJrcaqL26ADciEiV2IWykMmiBYBJIvcrRCDADe71OPxr81ZW2q0XKR9cW0lTh1fsJBBFUdeP7aLC6STcaImBCGM6ibJTSnkE).

If your app or service is **Primarily Child-Directed** , then you may not use
the Facebook Audience Network SDKs.

If your app or service is **Mixed Audience without an Age Gate** , then you
may use the Facebook Audience Network SDKs only if you set the
`setMixedAudience` flag for all users. When an app or service tells Facebook
that the `setMixedAudience` flag is set in the Audience Network SDK, Facebook
will only serve ads to non-United States users of that app through the
Audience Network services.

◦ iOS:
<https://developers.facebook.com/docs/reference/ios/4.6/class/FBAdSettings/>

◦ Android:
[https://developers.facebook.com/docs/reference/android/current/class/AdSettings/#setMixedAudience](/docs/reference/android/current/class/AdSettings/#setMixedAudience)

For apps or services that are **Mixed Audience with an Age Gate** and where an
individual user represents that they are under 13, you may not issue an ad
request to the Audience Network by ensuring that the Audience Network is not
being requested in your view controller (iOS), activity class (Android), or
any respective app function. Where an individual represents that they are at
least 13 years old, you may use the Audience Network SDK without setting the
`setMixedAudience` flag.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1668333663438923&ev=PageView&noscript=1)

``

``

``

``

![](https://facebook.com/security/hsts-pixel.gif?c=3.2.5)

[Meta App Events](/docs/app-events)

  * [Overview](/docs/app-events/overview)
  * [Getting Started](/docs/app-events/getting-started)
  * [Guides](/docs/app-events/guides)
  * [Best Practices](/docs/app-events/best-practices)
  * [Reference](/docs/app-events/reference)
  * [FAQ](/docs/app-events/faq)

# Advertiser Tracking Enabled

This guide shows you how to enable and disable advertising tracking. Please
use the guidance below for setting up the Advertiser Tracking Enabled
depending on the iOS version.

## Guidance for setting up the ATE parameter in the Facebook SDK for iOS
version 14.5 to 16.3.1, Conversions API for app events, and the App Events API

If you don’t set the Advertiser Tracking Enabled parameter indicating that an
iOS 14.5 and later event is opted-in for tracking, we may restrict our use of
that event. You should review your own legal obligations, platform terms, and
commitments you've made to your users to determine which events should be sent
with the Advertiser Tracking Enabled parameter indicating they are opted-in
for tracking.

Please follow Conversions API best practices and how to set up required and
recommended parameters [here](/docs/marketing-api/conversions-api/app-events).

## Guidance for FB SDK for iOS 17.0.0 or later versions

For iOS 17.0 and later devices, you are no longer required to set the
Advertiser Tracking Enabled parameter for Facebook SDK for iOS 17.0.0 and
later versions. We now rely on Apple’s App Tracking Transparency (ATT) system
API to determine ATT permission status for app events sent through Facebook
SDK for iOS 17.0.0 and later versions.

## Limitations

  * `AdvertiserTrackingEnabled` is only available for iOS 14 and up to 17.0 versions.
  * Limit Ad Tracking can be used for versions prior to iOS 14.5 that support Limit Ad Tracking.

## Get Device Permission

If permission is provided, call the `setAdvertiserTrackingEnabled` method of
the `FBSDKSettings` class and set it to `YES` for Objective-C or `true` for
Swift. If a device does not allow tracking, set `setAdvertiserTrackingEnabled`
to `NO` for Objective-C or `false` for Swift. The method will return a boolean
value to indicate whether the method is set successfully or not.

####  Allow Advertiser Tracking

  

Swift

    
    
    // Set isAdvertiserTrackingEnabled to true if a device provides permission
    Settings.shared.isAdvertiserTrackingEnabled = true

  

####  Do Not Allow Advertiser Tracking

  

Swift

    
    
    // Set isAdvertiserTrackingEnabled to false if a device does not provide permission
    Settings.shared.isAdvertiserTrackingEnabled = false

After a user assents to advertiser tracking and you enable events, be sure to
initialize the SDK before sending events.

#### Setting ATE Flag in FB iOS SDK versions 17.0.0+

    
    
    Settings.shared.isAdvertiserTrackingEnabled = true

**Warning** : Setter for `isAdvertiserTrackingEnabled` is deprecated: The
`setAdvertiserTrackingEnabled` flag is not used for FBSDK v17+ on iOS 17+ as
the FBSDK v17+ now relies on ATTrackingManager.trackingAuthorizationStatus.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

``

``

``

![](https://facebook.com/security/hsts-pixel.gif?c=3.2.5)

[Meta App Events](/docs/app-events)

  * [Overview](/docs/app-events/overview)
  * [Getting Started](/docs/app-events/getting-started)
  * [Guides](/docs/app-events/guides)
  * [Best Practices](/docs/app-events/best-practices)
  * [Reference](/docs/app-events/reference)
  * [FAQ](/docs/app-events/faq)

# Facebook SDK Best Practices for GDPR Compliance

After you integrate Facebook SDK, certain App Events are automatically logged
and collected for [Events Manager](https://www.facebook.com/events_manager),
unless you disable Automatic App Event Logging. You may change this in your
app code or through a toggle under App Events in the App Dashboard or Events
Manager. Please note in the event of conflicting values between the
`AutoLogAppEventsEnabled` flag and the toggle, we will honor the value in the
‘Automatic event logging for the Facebook SDK’ toggle. For details about what
information is collected and how to disable Automatic App Event Logging, see
[Automatic App Event Logging](https://www.developers.facebook.com/docs/app-
events/automatic-event-collection-detail).

When you use the FB SDK for App Events, our business terms require that you
have an appropriate legal basis to collect and process User information. Under
GDPR and other EU data protection regulations, you are required to obtain end
User consent before sending data via our SDK. Thus, you need to ensure that
your SDK implementation meets these consent requirements.

The SDK by default automatically logs common mobile events from your app like
app installs and app launches. These events are transmitted to Facebook when
an app is opened to provide you insights into your app's User behavior and ad
campaign performance.

To help you implement consent mechanisms to meet the legal obligations under
EU data protection law and our Business Tools Terms, we offer the following
resources.

## Consent Guide

You can review our [consent
guide](https://developers.facebook.com/docs/privacy) for practical guidance
and best practices on asking for consent on your websites and apps. If you
choose to obtain a User's informed consent prior to the app install via a
separate User registration flow, as noted in the above consent guide, you will
not need to make any changes to continue using the Facebook SDK and its auto-
logging feature.

## Delaying Automatic Event Collection

If you don't a pre-install mechanism for obtaining User consent, you will need
to take additional step to fulfill the legal obligations for using FB SDK. We
provide tools to delay the transmission of data from the SDK until a User has
had the opportunity to go through an in-app consent flow.

### Requirements

  * Facebook SDK v.5.0 or higher. Learn how to upgrade your app to the latest SDK version by visiting our [upgrade guide](https://developers.facebook.com/docs/app-events/upgrade-guide). 

### For Android

Set the `AutoLogAppEventsEnabled` flag to `false` in your
`AndroidManifest.xml` file.

    
    
    <application>
      ...
      <meta-data android:name='com.facebook.sdk.AutoLogAppEventsEnabled'
               android:value='false'/>
      ...
    </application>

Then, re-enable auto-logging after an end User provides consent by calling the
`setAutoLogAppEventsEnabled()` method of the `FacebookSdk` class and set it to
`true`.

    
    
    FacebookSdk.setAutoLogAppEventsEnabled(true);

### For iOS

Open the application's `.plist` as code in Xcode and add the following XML to
the property dictionary.

    
    
    <key>FacebookAutoLogAppEventsEnabled</key><false/>

  * Then, re-enable auto-logging after an end-user provides consent by calling the `setAutoLogAppEventsEnabled`method of the `FBSDKSettings` class and set it to `true` for Swift or `YES` for Objective-C. 

For Swift:

    
    
    Settings.isAutoLogAppEventsEnabled = true

For Objective-C:

    
    
    [FBSDKSettings setAutoLogAppEventsEnabled:YES];

## Disabling Automatic Event Collection

You can also disable automatic event logging entirely to stop transmitting any
data to Facebook when an app is opened. **_Note: If you leave automatic event
logging disabled, you are no longer tracking app install and app launch
events. Add additional code manually to log these events._**

### Android

Add the following line to your `AndroidManifest.xml` file.

    
    
    <application>
      ...
      <meta-data android:name='com.facebook.sdk.AutoLogAppEventsEnabled'
               android:value='false'/>
      ...
    </application>

### iOS

Open the application's `.plist` as code in Xcode and add the following XML to
the property dictionary.

    
    
    <key>FacebookAutoLogAppEventsEnabled</key>
    <false/>

## Disabling Automatic SDK Initialization

The Facebook SDK for Android automatically initializes when the app is opened.
When the SDK is initializing, it fetches app settings from Facebook. If you
want to block all network requests to Facebook, you can disable automatic
initialization.

### Android

Set the `AutoInitEnabled` flag to `false` in your `AndroidManifest.xml` file.

    
    
    <application>
      ...
      <meta-data android:name="com.facebook.sdk.AutoInitEnabled"
               android:value="false"/>
      ...
    </application>

Then, re-enable automatic initialization after an end User provides consent by
calling the `setAutoInitEnabled()` method of the `FacebookSdk` class and
setting it to `true`.

    
    
    FacebookSdk.setAutoInitEnabled(true);
    FacebookSdk.fullyInitialize();

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

``

``

``

![](https://facebook.com/security/hsts-pixel.gif?c=3.2.5)

[Meta App Events](/docs/app-events)

  * [Overview](/docs/app-events/overview)
  * [Getting Started](/docs/app-events/getting-started)
  * [Guides](/docs/app-events/guides)
  * [Best Practices](/docs/app-events/best-practices)
  * [Reference](/docs/app-events/reference)
  * [FAQ](/docs/app-events/faq)

# Data Processing Options for US Users

Starting June 1, 2023, Limited Data Use for people in Colorado and Connecticut
via Meta Business Tools and Meta Audience Network will be effective. Starting
June 1, 2023, Limited Data Use for people in California via customer list
custom audiences will also be effective. To give businesses time to prepare,
Limited Data Use’s expanded features are available to explore as of May 1,
2023, but won’t go into effect until June 1, 2023. Please note that any
Limited Data Use flag sent for these updated states and products prior to June
1, 2023, will not be implemented.

Limited Data Use is a data processing option that gives you more control over
how your data is used in Meta’s systems and better supports your compliance
efforts with various US state privacy regulations. To utilize this feature,
you must proactively enable Limited Data Use. When Meta receives data with
Limited Data Use enabled from people in the states where Limited Data Use
applies, we will process that data in accordance with our role as a service
provider or processor, as applicable, and limit the use of that data as
specified in our [State-Specific
Terms](https://www.facebook.com/legal/terms/state-specific).

For [Business Tools](https://www.facebook.com/help/331509497253087) and
Audience Network, Limited Data Use is available only for people in California,
Colorado or Connecticut. If a business enables Limited Data Use but does not
set the location parameters to US and California, Colorado or Connecticut, we
will determine if the event is from one of those states. If Limited Data Use
is enabled for an event in California, Colorado or Connecticut, we will
process data in accordance with our role as a service provider or processor
and limit the use of that data in accordance with our [State-Specific
Terms](https://www.facebook.com/legal/terms/state-specific).

Businesses may notice an impact to campaign performance and effectiveness, and
retargeting and measurement capabilities will be limited when Limited Data Use
is enabled.

## Implementation

### Graph API

To implement Data Processing Options using the Graph API, add
`data_processing_options`, `data_processing_options_country`, and
`data_processing_options_state` to your API call.

To explicitly not enable LDU, send an empty `data_processing_options` array:

    
    
    {
      "event": "CUSTOM_APP_EVENTS",
      "application_tracking_enabled": "1",
      "advertiser_tracking_enabled": "1",
      "custom_events": ["fb_mobile_purchase"],
      "data_processing_options": []
    }  

To enable LDU and have Meta perform geolocation, you can send an event with
the following code:

    
    
    {
      "event": "CUSTOM_APP_EVENTS",
      "application_tracking_enabled": "1",
      "advertiser_tracking_enabled": "1",
      "custom_events": ["fb_mobile_purchase"],
      "data_processing_options": ["LDU"],
      "data_processing_options_country": 0,
      "data_processing_options_state": 0
    }  

To enable LDU and manually specify the location, e.g., for California, you can
send an event with the following code:

    
    
      {
      "event": "CUSTOM_APP_EVENTS",
      "application_tracking_enabled": "1",
      "advertiser_tracking_enabled": "1",
      "custom_events": ["fb_mobile_purchase"],
      "data_processing_options": ["LDU"],
      "data_processing_options_country": 1,
      "data_processing_options_state": 1000
    }  

### Mobile SDKs

We recommend using our latest versions to ensure the functionality of Data
Processing Options. The below implementation instructions are accurate for the
following SDK versions:

  * iOS Facebook SDK v7.1.1 or higher
  * Android Facebook SDK v7.1.0 or higher
  * Unity SDK v7.21.0 or higher

Please update if you are using any versions below the ones listed above.

As of July 1, 2023, we are ending the Transition Period for older versions of
App Events via the Facebook SDK, whereby we applied Limited Data Use to all
personal information shared about people in California. The ability to enable
default Limited Data Use will no longer be available for any versions below
iOS Facebook SDK v7.1.1, Android Facebook SDK v7.1.0 and Unity SDK v7.21.0. If
you choose to use Limited Data Use for a person in California, Colorado,
Connecticut, Florida, Texas, or Oregon on or after July 1, 2023, you must
update your SDK and implement Data Processing Options as set forth in this
document.

Implementation| Adding Data Processing Options| Facebook SDK for iOS v7.1.1+ (Objective-C) | With Objective-C, use `FBSDKSettings setDataProcessingOptions`.   
To explicitly not enable Limited Data Use (LDU), use:

    
    
    [FBSDKSettings setDataProcessingOptions:@[]];

To enable LDU and have Meta perform geolocation, use:

    
    
    [FBSDKSettings setDataProcessingOptions:@[@"LDU"] country:0 state:0]; 

To enable LDU and manually specify the location, e.g., for California, use:

    
    
    [FBSDKSettings setDataProcessingOptions:@[@"LDU"] country:1 state:1000];     
  
---|---  
Facebook SDK for iOS v7.1.1+ (Swift) | With Swift, use `setDataProcessingOptions`.   
To explicitly not enable LDU, use:

    
    
    Settings.setDataProcessingOptions(modes: [])   

To enable LDU and have Meta perform geolocation, use:

    
    
    Settings.setDataProcessingOptions(modes: ["LDU"], country: 0, state: 0)

To enable LDU and manually specify the location, e.g., for California, use:

    
    
    Settings.setDataProcessingOptions(modes: ["LDU"], country: 1, state: 1000)    
  
Facebook SDK for Android v7.1.0+ | Use the `setDataProcessingOptions` method.   
To explicitly not enable LDU, use:

    
    
    FacebookSdk.setDataProcessingOptions(new String[] {});   

To enable LDU and have Meta perform geolocation, use:

    
    
    FacebookSdk.setDataProcessingOptions(new String[] {"LDU"}, 0, 0);   

To enable LDU and manually specify the location, e.g., for California, use:

    
    
    FacebookSdk.setDataProcessingOptions(new String[] {"LDU"}, 1, 1000);    
  
Unity SDK v7.21.1+ | To explicitly not enable LDU, send an event with:
    
    
    FB.Mobile.SetDataProcessingOptions(new string[] {});

To enable LDU and have Meta perform geolocation, send an event with:

    
    
    FB.Mobile.SetDataProcessingOptions(new string[] {"LDU"}, 0, 0); 

To enable LDU and manually specify the location, e.g., for California, send an
event with:

    
    
    FB.Mobile.SetDataProcessingOptions(new string[] {"LDU"}, 1, 1000);    
  
![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

``

``

``

