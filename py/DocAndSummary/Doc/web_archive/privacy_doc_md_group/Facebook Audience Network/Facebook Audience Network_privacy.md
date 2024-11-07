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

