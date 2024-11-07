Skip to main content

This browser is no longer supported.

Upgrade to Microsoft Edge to take advantage of the latest features, security
updates, and technical support.

[Download Microsoft Edge](https://go.microsoft.com/fwlink/p/?LinkID=2092881 )
[More info about Internet Explorer and Microsoft
Edge](https://learn.microsoft.com/en-us/lifecycle/faq/internet-explorer-
microsoft-edge)

Table of contents Exit focus mode

Language

  *   * 

Read in English Save [ ](https://github.com/MicrosoftDocs/appcenter-
docs/blob/live/docs/sdk/analytics/android.md "Edit This Document")

Table of contents Read in English Save Add to Plan [ Edit
](https://github.com/MicrosoftDocs/appcenter-
docs/blob/live/docs/sdk/analytics/android.md "Edit This Document")

* * *

#### Share via

Facebook x.com LinkedIn Email

* * *

Print

Table of contents

# App Center Analytics (Android)

  * Article
  * 03/14/2024
  * 11 contributors

Feedback

## In this article

Important

Visual Studio App Center is scheduled for retirement on March 31, 2025. While
you can continue to use Visual Studio App Center until it is fully retired,
there are several recommended alternatives that you may consider migrating to.

[Learn more about support timelines and
alternatives.](https://aka.ms/appcenter/retire)

  * [Android](android)
  * [iOS](ios)
  * [React Native](react-native)
  * [Windows](windows)
  * [MAUI/Xamarin](xamarin)
  * [Unity](unity)
  * [macOS](macos)
  * [tvOS](tvos)
  * [Cordova](cordova)

App Center Analytics helps you understand user behavior and customer
engagement to improve your app. The SDK automatically captures session count
and device properties like model, OS version, etc. You can define your own
custom events to measure things that matter to you. All the information
captured is available in the App Center portal for you to analyze the data.

Follow the [SDK Getting started](../getting-started/android) section if you
haven't set up the SDK in your application yet.

## Session and device information

Once you add App Center Analytics to your app and start the SDK, it will
automatically track sessions and device properties like OS Version, model,
etc. without writing any additional code.

### Country Code

The SDK automatically reports a user's country code if the device has a mobile
data modem and a SIM card installed. WiFi-only devices won't report a country
code by default. To set the country code of those users, you must retrieve
your user's location yourself and use the `setCountryCode:` method in the SDK:

    
    
    AppCenter.setCountryCode("en");
    
    
    
    AppCenter.setCountryCode("en")
    

Note

For country code to be displayed on Analytics sessions,
`AppCenter.setCountryCode` must be called prior to calling `AppCenter.start`.

## Custom events

You can track your own custom events with **up to 20 properties** to
understand the interaction between your users and the app.

Once you've started the SDK, use the `trackEvent()` method to track your
events with properties. You can send **up to 200 distinct event names**. Also,
there's maximum character limits:

  * 256 characters per `event name`.
  * 125 characters per `event property name` & `event property value`.

    
    
    Map<String, String> properties = new HashMap<>();
    properties.put("Category", "Music");
    properties.put("FileName", "favorite.avi");
    
    Analytics.trackEvent("Video clicked", properties);
    
    
    
    val properties = hashMapOf("Category" to "Music", "FileName" to "favorite.avi")
    Analytics.trackEvent("Video clicked", properties)
    

Properties for events are entirely optional â if you just want to track an
event, use this sample instead:

    
    
    Analytics.trackEvent("Video clicked");
    
    
    
    Analytics.trackEvent("Video clicked")
    

## Event priority and persistence

You can track business critical events that have higher importance than other
events.

  * Developers can set priority of events as **Normal** (`Flags.NORMAL` in the API) or **Critical** (`Flags.CRITICAL` in the API).
  * Events with priority set as **Critical** will be retrieved from storage first and sent before **Normal** events.
  * When the local storage is full, and new events need to be stored, the oldest events with the lowest priority are deleted first.
  * If the storage is full of logs with **Critical** priority, then tracking an event with **Normal** priority will fail as the SDK can't make room in that case.
  * If you also use the **Crashes** service, crash logs are set as **Critical** and share the same storage as events.
  * The transmission interval is only applied to **Normal** events, **Critical** events will be sent after 3 seconds.

You can use the following API to track an event as **Critical** :

    
    
    Map<String, String> properties = new HashMap<>();
    properties.put("Category", "Music");
    properties.put("FileName", "favorite.avi");
    
    Analytics.trackEvent("eventName", properties, Flags.CRITICAL);
    
    // If you're using name only, you can pass null as properties.
    
    
    
    val properties = hashMapOf("Category" to "Music", "FileName" to "favorite.avi")
    Analytics.trackEvent("Video clicked", properties, Flags.CRITICAL)
    
    // If you're using name only, you can pass null as properties.
    

## Pause and resume sending logs

Pausing the event transmission can be useful in scenarios when the app needs
to control the network bandwidth for more business critical needs. You can
pause sending logs to the App Center backend. When paused, events can still be
tracked and saved, but they aren't sent right away. Any events your app tracks
while paused will only be sent once you call `resume`.

    
    
    Analytics.pause();
    Analytics.resume();
    
    
    
    Analytics.pause()
    Analytics.resume()
    

## Enable or disable App Center Analytics at runtime

You can enable and disable App Center Analytics at runtime. If you disable it,
the SDK won't collect any more analytics information for the app.

    
    
    Analytics.setEnabled(false);
    
    
    
    Analytics.setEnabled(false)
    

To enable App Center Analytics again, use the same API but pass `true` as a
parameter.

    
    
    Analytics.setEnabled(true);
    
    
    
    Analytics.setEnabled(true)
    

The state is persisted in the device's storage across application launches.

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](../other-apis/android) guide.

Note

This method must only be used after `Analytics` has been started.

## Check if App Center Analytics is enabled

You can also check if App Center Analytics is enabled or not.

    
    
    Analytics.isEnabled();
    
    
    
    Analytics.isEnabled()
    

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](../other-apis/android) guide.

Note

This method must only be used after `Analytics` has been started, it will
always return `false` before start.

## Manage start session

By default, the session ID depends on the lifecycle of the application. If you
want to control the start of a new session manually, follow the next steps:

Note

Pay attention that each call of **Analytics.StartSession()** API will generate
a new session. If in manual session tracker mode this API will not be called
then all sending logs will have a null session value.

Note

Pay attention that after a new application launch the session id will be
regenerated.

  * Call the following method before the SDK start:

    
    
    Analytics.enableManualSessionTracker();
    
    
    
    Analytics.enableManualSessionTracker()
    

  * Then you can use the `startSession` API after the `AppCenter.start`:

    
    
    Analytics.startSession();
    
    
    
    Analytics.startSession()
    

## Local storage size

By default, the SDK stores all the event logs up to 10 MB. Developers can use
an API to increase the [storage size](../other-apis/android#storage-size) and
the SDK will keep storing logs until the storage is full.

## No internet access

When there's no network connectivity, the SDK saves up to 10 MB of logs in the
local storage. Once the storage is full, the SDK starts discarding old logs to
make room for the new logs. Once network connectivity returns, the SDK sends
logs in the batch of 50 or after every 6 seconds (by default).

Note

The logs older than 25 days won't be accepted by the backend.

## Batching event logs

The App Center SDK uploads logs in a batch of 50 and if the SDK doesn't have
50 logs to send, it will still send logs after 6 seconds (by default). There
can be a maximum of three batches sent in parallel. The transmission interval
can be changed:

    
    
    // Change transmission interval to 10 seconds.
    Analytics.setTransmissionInterval(10000);
    
    
    
    // Change transmission interval to 10 seconds.
    Analytics.setTransmissionInterval(10000)
    

The transmission interval value must be between 6 seconds and 86400 seconds
(one day) and this method must be called before the service is started.

## Retry and back-off logic

App Center SDK supports back-off retries on recoverable network errors. Below
is the retry logic:

  * 3 tries maximum per request.
  * Each request has its own retry state machine.
  * All the transmission channels are disabled (until next app process) after one request exhausts all its retries.

Back-off logic

  * 50% randomization, first retry between 5 and 10 seconds, next try between 2.5 and 5 minutes, last try between 10 and 20 minutes.
  * If network switches from off to on (or from wi-fi to mobile), retry states are reset and requests are retried immediately.

* * *

## Feedback

Was this page helpful?

Yes No

[ Provide product feedback
](https://docs.microsoft.com/appcenter/help#accessing-app-center-free-support)

* * *

## Additional resources

[ California Consumer Privacy Act (CCPA) Opt-Out Icon Your Privacy Choices
](https://aka.ms/yourcaliforniaprivacychoices)

Theme

  * Light
  * Dark
  * High contrast

  *   * [Previous Versions](/en-us/previous-versions/)
  * [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
  * [Contribute](/en-us/contribute/)
  * [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Terms of Use](/en-us/legal/termsofuse)
  * [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
  * (C) Microsoft 2024

## Additional resources

### In this article

[ California Consumer Privacy Act (CCPA) Opt-Out Icon Your Privacy Choices
](https://aka.ms/yourcaliforniaprivacychoices)

Theme

  * Light
  * Dark
  * High contrast

  *   * [Previous Versions](/en-us/previous-versions/)
  * [Blog](https://techcommunity.microsoft.com/t5/microsoft-learn-blog/bg-p/MicrosoftLearnBlog)
  * [Contribute](/en-us/contribute/)
  * [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
  * [Terms of Use](/en-us/legal/termsofuse)
  * [Trademarks](https://www.microsoft.com/legal/intellectualproperty/Trademarks/)
  * (C) Microsoft 2024

