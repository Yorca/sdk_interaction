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

# Automatic data collection

By default, the Batch SDK will automatically collect some data related to the
user's device:

Native data| Description| Default collection status  
---|---|---  
Device Model| The user's device model information| false  
Device Brand| The user's device brand information| false  
Installation ID| The installation identifier| true  
Session ID| The user's session identifier| true  
Custom User ID| The user's custom identifier| true  
API Level| The Batch SDK api level| true  
Messaging API Level| The Batch SDK Messaging api level| true  
Device Language| The user's device language| true  
Device Region| The user's device region| true  
Device Timezone| The user's device timezone| true  
OS Version| The Android version| true  
App Version (String)| The application version (string)| true  
App Version (Build Number)| The application version (number)| true  
Bundle Name| The application package name| true  
Device Date| The current device date| true  
First Installation Date| The date at which the app was last updated.| true  
Last Installation Date| The date at which the app was first installed| true  
Device Installation Date| The Batch installation date| true  
SDK Level| The Android API level| true  
Bridge Version| Version of the batch bridge (for cross-plateform plugin only)|
true  
Plugin Version| Version of the batch plugin (for cross-plateform plugin only)|
true  
GeoIP| Whether Batch should resolve the user's location from ip address| false  
  
Some of this data are disabled by default and can be toggled on/off according
to the user consent:

  * Device model
  * Device brand
  * GeoIP

Use the following API to fine-tune what you want to enable:

  * Kotlin
  * Java

    
    
    Batch.updateAutomaticDataCollection {
      it.apply {
        setGeoIPEnabled(true) // Enable GeoIP resolution on server side
        setDeviceBrandEnabled(true) // Enable automatic collection of the device brand information
        setDeviceModelEnabled(true) // Enable automatic collection of the device model information
      }
    }

> Note: This API can be used at any time in your application lifecycle and
> Batch will remember these values, even if your Application reboots.

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

