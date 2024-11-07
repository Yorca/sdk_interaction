This app works best with JavaScript enabled.

[](/)Search

  * iOS
  * Android
    * [Prerequisites](/android/prerequisites/)
    * [SDK integration](/android/sdk-integration/)
    * [Mobile landings](/android/mobile-landings/)
    * [In-App Messaging](/android/in-app-messaging/)
    * [Inbox](/android/inbox/)
    * Custom data
    * Data privacy
      * [SDK opt-out (e.g. GDPR)](/android/data-privacy/opt-out/)
        * Opting-out
        * Disabling the SDK by default
        * Opting-in
      * [Automatic data collection](/android/data-privacy/data-collection/)
    * [Event dispatchers](/android/event-dispatchers/)
    * [Huawei Push](/android/huawei/)
    * [Troubleshooting](/android/troubleshooting/)
    * Advanced
    * [SDK changelog](/android/sdk-changelog/)
    * [API Reference](/android-api-reference/index.html)
  * Web
  * Cordova
  * Flutter
  * React Native
  * Dashboard
  * API
  * Guides
  * Third Party Integrations
  * [Help Center](https://help.batch.com)
  * [Download SDKs](/download/)
  * SDK Archive

##### [Documentation](/) > Android > Data privacy

# SDK opt-out (e.g. GDPR)

If you plan to send personal user data and have to comply with EU's GDPR, any
other data privacy law or simply want to give your users more control
regarding their privacy, these methods will help you plug your consent screen
to Batch.

There are two SDK operation modes:

  * **SDK enabled by default** , opting-out required via an explicit method call: this is the default mode.
  * **SDK disabled by default** , optin-in required

> **Important** : Disabling the SDK will also disable In-App messages, data
> collection and may not disable notifications if you are using a custom
> receiver. In case you simply want to implement a custom opt-out, we
> recommend you use Batch's native methods ([know more
> here](/android/advanced/customizing-notifications#_disabling-
> notifications)).

## Opting-out

In order to opt-out from SDK, simply call:

  * Kotlin
  * Java

    
    
    Batch.optOut(context)

Opting out will:

  * Prevent `Batch.onStart(Activity)` or `Batch.onServiceCreate(Context, boolean)` from doing anything at all.
  * Disable any network capability from the SDK.
  * Disable all In-App campaigns.
  * Make the Inbox module return an error immediately when used.
  * Make the SDK reject any `BatchProfileAttributeEditor.save()` calls.
  * Make the SDK reject calls to `Batch.Profile.trackEvent()`, `Batch.Profile.trackLocation()` and any related methods.

Even if you opt-in afterwards, data generated (such as user data or tracked
events) **while** opted out WILL be lost.

> Important note: Calling this method will stop Batch, effectively simulating
> calls to `Batch.onStop(Activity)`, `Batch.onDestroy(Activity)` and
> `Batch.onServiceDestroy(Context)`.

You can also wipe the SDK installation data:

  * Kotlin
  * Java

    
    
    Batch.optOutAndWipeData(context)

This will wipe the data locally and request a remote data removal for the
matching Installation ID and its associated data.  
Any user-level data associated with the Custom User ID (if any) set via our
server APIs will **not** be deleted. However, the Installation ID <> Custom
User ID association will be, effectively logging the user out before deleting
their installation data.  
Sending notifications to this user using their Advertising ID (via the
Transactional API or a Custom Audience) will not be possible for a month.

> Note: Opting out is not possible while the SDK hasn't started. Make sure
> you've called `Batch.onStart(Activity)` beforehand.

## Disabling the SDK by default

In order to disable the SDK by default, you need to add a meta-data entry to
your AndroidManifest's `<application>` tag:

    
    
    <meta-data android:name="batch_opted_out_by_default" android:value="true" />

## Opting-in

Once you've opted-out (either programmatically, or by default), you can re-
enable the SDK by calling the following:

  * Kotlin
  * Java

    
    
    Batch.optIn(context)
    Batch.onStart(activity)

> Note: Even if you've already done so before opting-out, you are **required**
> to call `Batch.onStart()` or the SDK won't work until the next start.

[](https://batch.com)

Platform

[Differentiators](https://batch.com/differentiators)[Blog](https://batch.com/blog)[Partners](https://batch.com/partners)

Company

[About](https://batch.com/about)[Jobs](https://www.welcometothejungle.com/en/companies/batch)[Legal
Notice](https://batch.com/legal-notice)[Privacy
Policy](https://batch.com/privacy-policy)[Service
Agreement](https://batch.com/service-agreement)

Resources

[SDKs](https://doc.batch.com/download/)[Help Center](https://help.batch.com)

Contact

[hello@batch.com](mailto:hello@batch.com)

[](tel:)

