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

