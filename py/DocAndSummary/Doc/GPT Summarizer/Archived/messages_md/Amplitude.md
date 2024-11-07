SDK name: Amplitude
Documentation:
[ documentation](/docs)

[Get Started](/docs/get-started)

[Data](/docs/data)

[Analytics](/docs/analytics)

[Session Replay](/docs/session-replay)

[Experiment](/docs/experiment)

[Admin](/docs/admin)

Developers

[SDKs](/docs/sdks) [APIs](/docs/apis)

[Partners](/docs/partners)

[FAQ](/docs/faq)

[Analytics SDKs](/docs/sdks/analytics)

Browser

[Browser SDK 2](/docs/sdks/analytics/browser/browser-sdk-2) [Ampli for Browser
SDK 2.0](/docs/sdks/analytics/browser/ampli-for-browser-sdk-2-0) [Autocapture
Plugin](/docs/sdks/analytics/browser/autocapture-plugin) [Browser SDK
1](/docs/sdks/analytics/browser/browser-sdk-1) [Ampli for Browser SDK
1.0](/docs/sdks/analytics/browser/ampli-for-browser-sdk-1-0) [Migrate from
Browser SDK 1.0 to 2.0](/docs/sdks/analytics/browser/migrate-from-browser-
sdk-1-0-to-2-0)

Android

[Android-Kotlin SDK](/docs/sdks/analytics/android/android-kotlin-sdk) [Ampli
for Android-Kotlin SDK](/docs/sdks/analytics/android/ampli-for-android-kotlin-
sdk)

Node

[Node.js SDK](/docs/sdks/analytics/node/node-js-sdk) [Node.js Ampli
Wrapper](/docs/sdks/analytics/node/node-js-ampli-wrapper)

Go

[Go SDK](/docs/sdks/analytics/go/go-sdk) [Ampli for
Go](/docs/sdks/analytics/go/ampli-for-go)

Python

[Python SDK](/docs/sdks/analytics-sdks/python/python-sdk) [Ampli for Python
SDK](/docs/sdks/analytics-sdks/python/ampli-for-python-sdk)

iOS

[iOS Swift SDK](/docs/sdks/analytics/ios/ios-swift-sdk) [Ampli for iOS Swift
SDK](/docs/sdks/analytics/ios/ampli-for-ios-swift-sdk)

Flutter

[Flutter SDK](/docs/sdks/analytics/flutter/flutter-sdk) [Flutter SDK
4.0](/docs/sdks/analytics/flutter/flutter-sdk-4-0) [Flutter SDK 4.0 Migration
Guide](/docs/sdks/analytics/flutter/flutter-sdk-4-0-migration-guide)

Java

[JRE Java SDK](/docs/sdks/analytics/java/jre-java-sdk) [Ampli for Java
SDK](/docs/sdks/analytics/java/ampli-for-java-sdk)

React Native

[React Native SDK](/docs/sdks/analytics/react-native/react-native-sdk)
[Migrate to the latest React Native SDK](/docs/sdks/analytics/react-
native/migrate-to-the-latest-react-native-sdk) [Ampli for the React Native
SDK](/docs/sdks/analytics/react-native/ampli-for-the-react-native-sdk)

Unreal

[Unreal SDK](/docs/sdks/analytics/unreal/unreal-sdk)

Unity

[Unity SDK](/docs/sdks/analytics/unity/unity-sdk)

Maintenance SDKs

Marketing Analytics SDK

[Marketing Analytics SDK](/docs/sdks/analytics/browser/marketing-analytics-
sdk)

[Migrate from Marketing Analytics to Browser SDK
2.0](/docs/sdks/analytics/browser/migrate-from-marketing-analytics-to-browser-
sdk-2-0)

Javascript SDK

[Javascript SDK](/docs/sdks/analytics/browser/javascript-sdk)

[Ampli for Javascript SDK](/docs/sdks/analytics/browser/ampli-for-javascript-
sdk)

[Migrate from Javascript SDK to Browser SDK
1.0](/docs/sdks/analytics/browser/migrate-from-javascript-sdk-to-browser-
sdk-1-0)

[React Native SDK (maintenance)](/docs/sdks/analytics/react-native/react-
native-sdk-maintenance) [iOS SDK](/docs/sdks/analytics/ios/ios-sdk) Node SDK

[Node SDK](/docs/sdks/analytics/node/node-sdk)

[Ampli for Node SDK](/docs/sdks/analytics/node/ampli-for-node-sdk)

[Node.js SDK Migration Guide](/docs/sdks/analytics/node/node-js-sdk-migration-
guide)

Android SDK 1.0

[Android SDK](/docs/sdks/analytics/android/android-sdk)

[Migrate to the Android-Kotlin SDK](/docs/sdks/analytics/android/migrate-to-
the-android-kotlin-sdk)

[SDKs](/docs/sdks)

/

[Amplitude Analytics SDK Catalog](/docs/sdks/analytics)

/

[Android](/docs/sdks/analytics/android)

/

[Android-Kotlin SDK](/docs/sdks/analytics/android/android-kotlin-sdk)

# Android-Kotlin SDK

The Kotlin Android SDK lets you send events to Amplitude.

## Install the SDK

Amplitude recommends using Android Studio as an IDE and Gradle to manage
dependencies.

GradleMaven

If you use Gradle in your project, add the following dependency to
`build.gradle`, and sync your project with the updated file.

    
    
    1dependencies {
    
    2    implementation 'com.amplitude:analytics-android:1.+'
    
    3}

If you use Maven in your project, the .jar is available on Maven Central with
the following configuration in `pom.xml`.

    
    
    1<dependency>
    
    2    <groupId>com.amplitude</groupId>
    
    3    <artifactId>analytics-android</artifactId>
    
    4    <version>[1.0,2.0]</version>
    
    5</dependency>

## Configure the SDK

Configuration options

Name | Description | Default Value  
---|---|---  
`deviceId` | `String?`. The device ID to use for this device. If no deviceID is provided one will be generated automatically. Learn more [here](./#device-id-lifecycle). | `null`  
`flushIntervalMillis` | `Int`. The amount of time SDK will attempt to upload the unsent events to the server or reach `flushQueueSize` threshold. The value is in milliseconds. | `30000`  
`flushQueueSize` | `Int`. SDK will attempt to upload once unsent event count exceeds the event upload threshold or reach `flushIntervalMillis` interval. | `30`  
`flushMaxRetries` | `Int`. Maximum retry times. | `5`  
`minIdLength` | `Int`. The minimum length for user id or device id. | `5`  
`partnerId` | `Int`. The partner id for partner integration. | `null`  
`identifyBatchIntervalMillis` | `Long`. The amount of time SDK will attempt to batch intercepted identify events. The value is in milliseconds | `30000`  
`flushEventsOnClose` | `Boolean`. Flushing of unsent events on app close. | `true`  
`callback` | `EventCallBack`. Callback function after event sent. | `null`  
`optOut` | `Boolean`. Opt the user out of tracking. | `false`  
~~`trackingSessionEvents`~~ (Deprecated. Use `autocapture` instead.) | `Boolean`. Automatic tracking of "Start Session" and "End Session" events that count toward event volume. | `false`  
~~`defaultTracking`~~ (Deprecated. Use `autocapture` instead.) | `DefaultTrackingOptions`. Enable tracking of default events for sessions, app lifecycles, screen views, and deep links. | `DefaultTrackingOptions(sessions = true)`  
`autocapture` | `Set<AutocaptureOption>`. A `Set` of Options to enable tracking of default events for sessions, application lifecycles, screen and fragment views, deep links, and element interactions. | If the parameter isn't set, `AutocaptureOption.SESSIONS` is added to the `Set` by default. For more information, see Autocapture.  
`minTimeBetweenSessionsMillis` | `Long`. The amount of time for session timeout. The value is in milliseconds. | `300000`  
`serverUrl` | `String`. The server url events upload to. | `https://api2.amplitude.com/2/httpapi`  
`serverZone` | `ServerZone.US` or `ServerZone.EU`. The server zone to send to, will adjust server url based on this config. | `ServerZone.US`  
`useBatch` | `Boolean` Whether to use batch API. | `false`  
`useAdvertisingIdForDeviceId` | `Boolean`. Whether to use advertising id as device id. For more information, see Advertiser ID for required module and permission. | `false`  
`useAppSetIdForDeviceId` | `Boolean`. Whether to use app set id as device id. For more information, see Application ID for required module and permission. | `false`  
`trackingOptions` | `TrackingOptions`. Options to control the values tracked in SDK. | `enable`  
`enableCoppaControl` | `Boolean`. Whether to enable COPPA control for tracking options. | `false`  
`instanceName` | `String`. The name of the instance. Instances with the same name will share storage and identity. For isolated storage and identity use a unique `instanceName` for each instance. | `$default_instance`  
`migrateLegacyData` | `Boolean`. Available in `1.9.0`+. Whether to migrate [maintenance Android SDK](../android) data (events, user/device ID). Learn more [here](https://github.com/amplitude/Amplitude-Kotlin/blob/main/android/src/main/java/com/amplitude/android/migration/RemnantDataMigration.kt#L9-L16). | `true`  
`offline` | `Boolean | AndroidNetworkConnectivityCheckerPlugin.Disabled`. Whether the SDK is connected to network. Learn more [here](./#offline-mode) | `false`  
`storageProvider` | `StorageProvider`. Implements `StorageProvider` interface to store events. | `AndroidStorageProvider`  
`identifyInterceptStorageProvider` | `StorageProvider`. Implements `StorageProvider` interface for identify event interception and volume optimization. | `AndroidStorageProvider`  
`identityStorageProvider` | `IdentityStorageProvider`. Implements `IdentityStorageProvider` to store user id and device id. | `FileIdentityStorageProvider`  
`loggerProvider` | `LoggerProvider`. Implements `LoggerProvider` interface to emit log messages to desired destination. | `AndroidLoggerProvider`  
`newDeviceIdPerInstall` | Whether to generate different a device id every time when the app is installed regardless of devices. It's legacy configuration only to keep compatible with the old Android SDK. It works the same as `useAdvertisingIdForDeviceId`. | `false`  
`locationListening` | Whether to enable Android location service. Learn more [here](./#location-tracking). | `true`  
  
### Configure batching behavior

To support high-performance environments, the SDK sends events in batches.
Every event logged by the `track` method is queued in memory. Events are
flushed in batches in background. You can customize batch behavior with
`flushQueueSize` and `flushIntervalMillis`. By default, the `serverUrl` is
`https://api2.amplitude.com/2/httpapi`. For customers who want to send large
batches of data at a time, set `useBatch` to `true` to set `setServerUrl` to
batch event upload API `https://api2.amplitude.com/batch`. Both the regular
mode and the batch mode use the same events upload threshold and flush time
intervals.

KotlinJava

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  Configuration(
    
     5    apiKey = AMPLITUDE_API_KEY,
    
     6    context = applicationContext,
    
     7    flushIntervalMillis = 50000,
    
     8    flushQueueSize = 20,
    
     9  )
    
    10)
    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4configuration.setFlushIntervalMillis(1000);
    
    5configuration.setFlushQueueSize(10);
    
    6 
    
    7Amplitude amplitude = new Amplitude(configuration);

You can dynamically set the configuration after initialization.

KotlinJava

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  Configuration(
    
     5    apiKey = AMPLITUDE_API_KEY,
    
     6    context = applicationContext,
    
     7  )
    
     8)
    
     9 
    
    10amplitude.configuration.optOut = true
    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4Amplitude amplitude = new Amplitude(configuration);
    
    5 
    
    6amplitude.getConfiguration().setOptOut(true);

### EU data residency

You can configure the server zone when initializing the client for sending
data to Amplitude's EU servers. The SDK sends data based on the server zone if
it's set.

## Note

For EU data residency, the project must be set up inside Amplitude EU. You
must initialize the SDK with the API key from Amplitude EU.

KotlinJava

    
    
    1import com.amplitude.android.Amplitude
    
    2 
    
    3val amplitude = Amplitude(
    
    4  Configuration(
    
    5    apiKey = AMPLITUDE_API_KEY,
    
    6    context = applicationContext,
    
    7    serverZone = ServerZone.EU
    
    8  )
    
    9)
    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4configuration.setServerZone(ServerZone.EU);
    
    5 
    
    6Amplitude amplitude = new Amplitude(configuration);

## Track

Events represent how users interact with your application. For example, "Song
Played" may be an action you want to note.

    
    
    1amplitude.track("Song Played")

You can also optionally include event properties.

    
    
    1amplitude.track(
    
    2  "Song Played",
    
    3  mutableMapOf<String, Any?>("title" to "Happy Birthday")
    
    4)

For more complex events you can [create and track a `BaseEvent`
object](https://github.com/amplitude/Amplitude-
Kotlin/blob/8c3c39ce1f79485a0ce716bbf01de464a9afe9a8/core/src/main/java/com/amplitude/core/Amplitude.kt#L112).

    
    
    1var event = BaseEvent()
    
    2event.eventType = "Song Played"
    
    3event.eventProperties = mutableMapOf<String, Any?>("title" to "Happy Birthday")
    
    4event.groups = mutableMapOf<String, Any?>("test-group-type" to "test-group-value")
    
    5event.insertId = 1234
    
    6amplitude.track(event)

## Identify

## Note

Starting in release v1.7.0, the SDK batches `identify` events that contain
only `set` operiatons. This results in fewer sent events and doesn't impact
the running of the `set` operations. Use the `identifyBatchIntervalMillis`
configuration setting to manage the interval at which the SDK flushes batched
identify intercepts.

Identify is for setting the user properties of a particular user without
sending any event. The SDK supports the operations `set`, `setOnce`, `unset`,
`add`, `append`, `prepend`, `preInsert`, `postInsert`, and `remove` on
individual user properties. Declare the operations via a provided Identify
interface. You can chain together multiple operations in a single Identify
object. The Identify object is then passed to the Amplitude client to send to
the server.

## Note

If the Identify call is sent after the event, the results of operations will
be visible immediately in the dashboard user's profile area, but it will not
appear in chart result until another event is sent after the Identify call.
The identify call only affects events going forward.

You can handle the identity of a user using the identify methods. Proper use
of these methods can connect events to the correct user as they move across
devices, browsers, and other platforms. Send an identify call containing those
user property operations to Amplitude server to tie a user's events with
specific user properties.

    
    
    1val identify = Identify()
    
    2identify.set("color", "green")
    
    3amplitude.identify(identify)

## Autocapture

Starting from release v1.18.0, the SDK can track more events without manual
instrumentation. You can configure it to track the following events
automatically:

  * Sessions
  * App lifecycles
  * Screen views
  * Deep links
  * Element interactions

Autocapture options

Name | Type | Enabled by default | Description  
---|---|---|---  
`SESSIONS` | `AutocaptureOption` | Yes | Enables session tracking. If the option is set, Amplitude tracks session start and session end events otherwise, Amplitude doesn't track session events. When this setting isn't set, Amplitude tracks `sessionId` only. See Track sessions for more information.  
`APP_LIFECYCLES` | `AutocaptureOption` | No | Enables application lifecycle events tracking. If the option is set, Amplitude tracks application installed, application updated, application opened, and application backgrounded events. Event properties tracked includes: `[Amplitude] Version`, `[Amplitude] Build`, `[Amplitude] Previous Version`, `[Amplitude] Previous Build`, `[Amplitude] From Background`. See Track application lifecycles for more information.  
`SCREEN_VIEWS` | `AutocaptureOption` | No | Enables screen and fragment views tracking. If the option is set, Amplitude tracks screen viewed and fragment viewed events. Event properties tracked includes: `[Amplitude] Screen Name`, `[Amplitude] Fragment Class`, `[Amplitude] Fragment Identifier`, `[Amplitude] Fragment Tag`. See Track screen views for more information.  
`DEEP_LINKS` | `AutocaptureOption` | No | Enables deep link tracking. If the option is set, Amplitude tracks deep link opened events. Event properties tracked includes: `[Amplitude] Link URL`, `[Amplitude] Link Referrer`. See Track deep links for more information.  
`ELEMENT_INTERACTIONS` | `AutocaptureOption` | No | Enables element interaction tracking. If the option is set, Amplitude tracks user interactions with clickable elements. Event properties tracked includes: `[Amplitude] Action`, `[Amplitude] Target Class`, `[Amplitude] Target Resource`, `[Amplitude] Target Tag`, `[Amplitude] Target Source`, `[Amplitude] Hierarchy`, `[Amplitude] Screen Name`. See Track element interactions for more information.  
  
You can configure Amplitude to start tracking Autocapture events. Otherwise,
you can omit the configuration to keep only session tracking enabled.

KotlinJava

The `autocapture` configuration accepts a `Set` of `AutocaptureOption` values.
To create the Autocapture options, use the `autocaptureOptions` helper
function and add the options to the set with a unary plus sign (`+`) before
each option.

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  Configuration(
    
     5    apiKey = AMPLITUDE_API_KEY,
    
     6    context = applicationContext,
    
     7    autocapture = autocaptureOptions {
    
     8        +sessions               // or `+AutocaptureOption.SESSIONS`
    
     9        +appLifecycles          // or `+AutocaptureOption.APP_LIFECYCLES`
    
    10        +deepLinks              // or `+AutocaptureOption.DEEP_LINKS`
    
    11        +screenViews            // or `+AutocaptureOption.SCREEN_VIEWS`
    
    12    }
    
    13  )
    
    14)

By default, if the `autocapture` configuration isn't explicitly set during
`Configuration` initialization, `configuration.autocapture` automatically
includes `AutocaptureOption.SESSIONS`.

If you want to prevent automatic session events capture, set `autocapture`
without the `AutocaptureOption.SESSIONS` option.

    
    
    1import com.amplitude.android.Amplitude
    
    2 
    
    3val amplitude = Amplitude(
    
    4  Configuration(
    
    5    apiKey = AMPLITUDE_API_KEY,
    
    6    context = applicationContext,
    
    7    autocapture = setOf(AutocaptureOption.APP_LIFECYCLES)  // or use `setOf()` to disable autocapture.
    
    8  )
    
    9)

The `autocapture` configuration accepts a `Set` of `AutocaptureOption` values.

    
    
     1import com.amplitude.android.Amplitude;
    
     2 
    
     3import java.util.Arrays;
    
     4 
    
     5Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
     6configuration.getAutocapture().addAll(Arrays.asList(
    
     7    AutocaptureOption.APP_LIFECYCLES,
    
     8    AutocaptureOption.DEEP_LINKS,
    
     9    AutocaptureOption.SCREEN_VIEWS
    
    10));
    
    11 
    
    12Amplitude amplitude = new Amplitude(configuration);

By default, if the `autocapture` configuration isn't explicitly set during
`Configuration` initialization, `configuration.getAutocapture()` automatically
includes `AutocaptureOption.SESSIONS`.

To prevent automatic session event capture, remove the
`AutocaptureOption.SESSIONS` option from `autocapture`.

    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4configuration.getAutocapture().remove(AutocaptureOption.SESSIONS);
    
    5 
    
    6Amplitude amplitude = new Amplitude(configuration);

### Track sessions

Amplitude enables session tracking by default. Include
`AutocaptureOption.SESSIONS` in the `autocapture` configuration to explicitly
configure the SDK to track session events or to enable session event tracking
along with other Autocapture configurations.

KotlinJava

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  Configuration(
    
     5    apiKey = AMPLITUDE_API_KEY,
    
     6    context = applicationContext,
    
     7    autocapture = autocaptureOptions {
    
     8        +sessions    // or `+AutocaptureOption.SESSIONS`
    
     9    }
    
    10  )
    
    11)
    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3import java.util.Arrays;
    
    4 
    
    5Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    6// `AutocaptureOption.SESSION` is automatically set in `configuration.autocapture`.
    
    7 
    
    8Amplitude amplitude = new Amplitude(configuration);

For more information about session tracking, refer to User sessions.

### Track application lifecycles

You can enable Amplitude to start tracking application lifecycle events by
including `AutocaptureOption.APP_LIFECYCLES` in the `autocapture`
configuration. See the following code sample.

KotlinJava

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  Configuration(
    
     5    apiKey = AMPLITUDE_API_KEY,
    
     6    context = applicationContext,
    
     7    autocapture = autocaptureOptions {
    
     8        +appLifecycles    // or `+AutocaptureOption.APP_LIFECYCLES`
    
     9    }
    
    10  )
    
    11)
    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4configuration.getAutocapture().add(AutocaptureOption.APP_LIFECYCLES);
    
    5 
    
    6Amplitude amplitude = new Amplitude(configuration);

After enabling this setting, Amplitude tracks the following events:

  * `[Amplitude] Application Installed`, this event fires when a user opens the application for the first time right after installation.
  * `[Amplitude] Application Updated`, this event fires when a user opens the application after updating the application.
  * `[Amplitude] Application Opened`, this event fires when a user launches or foregrounds the application after the first open.
  * `[Amplitude] Application Backgrounded`, this event fires when a user backgrounds the application.

### Track screen views

You can enable Amplitude to start tracking screen and fragment view events by
including `AutocaptureOption.SCREEN_VIEWS` in the `autocapture` configuration.
See the following code sample.

KotlinJava

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  Configuration(
    
     5    apiKey = AMPLITUDE_API_KEY,
    
     6    context = applicationContext,
    
     7    autocapture = autocaptureOptions {
    
     8        +screenViews    // or `+AutocaptureOption.SCREEN_VIEWS`
    
     9    }
    
    10  )
    
    11)
    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4configuration.getAutocapture().add(AutocaptureOption.SCREEN_VIEWS);
    
    5 
    
    6Amplitude amplitude = new Amplitude(configuration);

After enabling this setting, Amplitude will track both `[Amplitude] Screen
Viewed` and `[Amplitude] Fragment Viewed` events. Both of these events include
a screen name property. For `[Amplitude] Fragment Viewed` events, Amplitude
captures additional fragment-specific properties.

Event properties descriptions

Event property | Description  
---|---  
`[Amplitude] Screen Name` | The activity label, application label, or activity name (in order of priority).  
`[Amplitude] Fragment Class` | The fully qualified class name of the viewed fragment.  
`[Amplitude] Fragment Identifier` | The resource ID of the fragment as defined in the layout XML.  
`[Amplitude] Fragment Tag` | The unique identifier assigned to the fragment during a transaction.  
  
### Track deep links

You can enable Amplitude to start tracking deep link events by including
`AutocaptureOption.DEEP_LINKS` in the `autocapture` configuration. See the
following code sample.

KotlinJava

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  Configuration(
    
     5    apiKey = AMPLITUDE_API_KEY,
    
     6    context = applicationContext,
    
     7    autocapture = autocaptureOptions {
    
     8        +deepLinks    // or `+AutocaptureOption.DEEP_LINKS`
    
     9    }
    
    10  )
    
    11)
    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4configuration.getAutocapture().add(AutocaptureOption.DEEP_LINKS);
    
    5 
    
    6Amplitude amplitude = new Amplitude(configuration);

After enabling this setting, Amplitude will track the `[Amplitude] Deep Link
Opened` event with the URL and referrer information.

### Track element interactions

Amplitude can track user interactions with clickable elements with support for
both classic Android Views as well as Jetpack Compose. To enable this option,
include `AutocaptureOption.ELEMENT_INTERACTIONS` in the `autocapture`
configuration.

## Note

The `AutocaptureOption.ELEMENT_INTERACTIONS` option is available as a beta
release for early feedback. Try it out and share your thoughts on our
[GitHub](https://github.com/amplitude/Amplitude-Kotlin).

KotlinJava

    
    
     1import com.amplitude.android.Amplitude
    
     2 
    
     3val amplitude = Amplitude(
    
     4  @OptIn(ExperimentalAmplitudeFeature::class)
    
     5  Configuration(
    
     6    apiKey = AMPLITUDE_API_KEY,
    
     7    context = applicationContext,
    
     8    autocapture = autocaptureOptions {
    
     9        +elementInteractions    // or `+AutocaptureOption.ELEMENT_INTERACTIONS`
    
    10    }
    
    11  )
    
    12)

The `AutocaptureOption.ELEMENT_INTERACTIONS` option is marked as
`@ExperimentalAmplitudeFeature`. To enable this feature, apply the
`@OptIn(ExperimentalAmplitudeFeature::class)` annotation to the configuration.

    
    
    1import com.amplitude.android.Amplitude;
    
    2 
    
    3Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    4configuration.getAutocapture().add(AutocaptureOption.ELEMENT_INTERACTIONS);
    
    5 
    
    6Amplitude amplitude = new Amplitude(configuration);

When you enable this setting, Amplitude tracks the `[Amplitude] Element
Interacted` event whenever a user interacts with an element in the
application.

Event properties descriptions

Event property | Description  
---|---  
`[Amplitude] Action` | The action that triggered the event. Defaults to `touch`.  
`[Amplitude] Target Class` | The canonical name of the target view class.  
`[Amplitude] Target Resource` | The resource entry name for the target view identifier within the context the view is running in.  
`[Amplitude] Target Tag` | The tag of the target view if the value is of primitive type, or the `Modifier.testTag` of the target `@Composable` function.  
`[Amplitude] Target Text` | The text of the target view if the view is a `Button` instance.  
`[Amplitude] Target Source` | The underlying framework of the target element, either `Android Views` or `Jetpack Compose`.  
`[Amplitude] Hierarchy` | A nested hierarchy of the target view's class inheritance, from the most specific to the most general.  
`[Amplitude] Screen Name` | See Track screen views.  
  
## Support for Jetpack Compose

Amplitude supports tracking user interactions with UI elements implemented in
Jetpack Compose. To track interactions, add a `Modifier.testTag` to the
`@Composable` functions of the elements that you want to track.

## User groups

Amplitude supports assigning users to groups and performing queries, such as
Count by Distinct, on those groups. If at least one member of the group has
performed the specific event, then the count includes the group.

For example, you want to group your users based on what organization they're
in by using an 'orgId'. Joe is in 'orgId' '10', and Sue is in 'orgId' '15'.
Sue and Joe both perform a certain event. You can query their organizations in
the Event Segmentation Chart.

When setting groups, define a `groupType` and `groupName`. In the previous
example, 'orgId' is the `groupType` and '10' and '15' are the values for
`groupName`. Another example of a `groupType` could be 'sport' with
`groupName` values like 'tennis' and 'baseball'.

Setting a group also sets the `groupType:groupName` as a user property, and
overwrites any existing `groupName` value set for that user's groupType, and
the corresponding user property value. `groupType` is a string, and
`groupName` can be either a string or an array of strings to indicate that a
user is in multiple groups.

## Example

If Joe is in 'orgId' '15', then the `groupName` would be '15'.

    
    
    1// set group with a single group name
    
    2amplitude.setGroup("orgId", "15");

If Joe is in 'sport' 'tennis' and 'soccer', then the `groupName` would be
'["tennis", "soccer"]'.

    
    
    1// set group with multiple group names
    
    2amplitude.setGroup("sport", arrayOf("tennis", "soccer"))

You can also set **event-level groups** by passing an `Event` Object with
`groups` to `track`. With event-level groups, the group designation applies
only to the specific event being logged, and doesn't persist on the user
unless you explicitly set it with `setGroup`.

    
    
    1val event = BaseEvent()
    
    2event.eventType = "event type"
    
    3event.eventProperties = mutableMapOf("event property" to "event property value")
    
    4event.groups = mutableMapOf("orgId" to "15")
    
    5amplitude.track(event)

## Group identify

Use the Group Identify API to set or update the properties of particular
groups. Keep these considerations in mind:

  * Updates affect only future events, and don't update historical events.
  * You can track up to 5 unique group types and 10 total groups.

The `groupIdentify` method accepts a group type string parameter and group
name object parameter, and an Identify object that's applied to the group.

    
    
    1val groupType = "plan"
    
    2val groupName = "enterprise"
    
    3 
    
    4val identify = Identify().set("key", "value")
    
    5amplitude.groupIdentify(groupType, groupName, identify)

## Track revenue

Amplitude can track revenue generated by a user. Revenue is tracked through
distinct revenue objects, which have special fields that are used in
Amplitude's Event Segmentation and Revenue LTV charts. This allows Amplitude
to automatically display data relevant to revenue in the platform. Revenue
objects support the following special properties, as well as user-defined
properties through the `eventProperties` field.

    
    
    1val revenue = Revenue()
    
    2revenue.productId = "com.company.productId"
    
    3revenue.price = 3.99
    
    4revenue.quantity = 3
    
    5amplitude.revenue(revenue)

Name | Description  
---|---  
`productId` | Optional. String. An identifier for the product. Amplitude recommends something like the Google Play Store product ID. Defaults to `null`.  
`quantity` | Required. Integer. The quantity of products purchased. Note: revenue = quantity * price. Defaults to 1  
`price` | Required. Double. The price of the products purchased, and this can be negative. Note: revenue = quantity * price. Defaults to `null`.  
`revenueType` | Optional, but required for revenue verification. String. The revenue type (for example, tax, refund, income). Defaults to `null`.  
`receipt` | Optional. String. The receipt identifier of the revenue. For example, "123456". Defaults to `null`.  
`receiptSignature` | Optional, but required for revenue verification. String. Defaults to `null`.  
  
## Custom user identifier

If your app has its login system that you want to track users with, you can
call `setUserId` at any time.

    
    
    1amplitude.setUserId("user@amplitude.com")

## Custom device identifier

You can assign a new device ID using `deviceId`. When setting a custom device
ID, make sure the value is sufficiently unique. Amplitude recommends using a
UUID.

    
    
    1import java.util.UUID
    
    2 
    
    3amplitude.setDeviceId(UUID.randomUUID().toString())

## Reset when a user logs out

`reset` is a shortcut to anonymize users after they log out, by:

  * setting `userId` to `null`
  * setting `deviceId` to a new value based on current configuration

With an empty `userId` and a completely new `deviceId`, the current user would
appear as a brand new user in dashboard.

    
    
    1amplitude.reset()

## SDK plugins

Plugins allow you to extend Amplitude SDK's behavior by, for example,
modifying event properties (enrichment type) or sending to third-party APIs
(destination type). A plugin is an object with methods `setup()` and
`execute()`.

### Plugin.setup

This method contains logic for preparing the plugin for use and has
`amplitude` instance as a parameter. The expected return value is `null`. A
typical use for this method, is to instantiate plugin dependencies. This
method is called when the plugin is registered to the client via
`amplitude.add()`.

### Plugin.execute

This method contains the logic for processing events and has `event` instance
as parameter. If used as enrichment type plugin, the expected return value is
the modified/enriched event. If used as a destination type plugin, the
expected return value is a map with keys: `event` (BaseEvent), `code`
(number), and `message` (string). This method is called for each event,
including Identify, GroupIdentify and Revenue events, that's instrumented
using the client interface.

### Enrichment type plugin example

Here's an example of a plugin that modifies each event that's instrumented by
adding extra event property.

    
    
     1import androidx.annotation.NonNull;
    
     2import androidx.annotation.Nullable;
    
     3 
    
     4import com.amplitude.core.Amplitude;
    
     5import com.amplitude.core.events.BaseEvent;
    
     6import com.amplitude.core.platform.Plugin;
    
     7 
    
     8import java.util.HashMap;
    
     9 
    
    10public class EnrichmentPlugin implements Plugin {
    
    11  public Amplitude amplitude;
    
    12  @NonNull
    
    13  @Override
    
    14  public Amplitude getAmplitude() {
    
    15    return this.amplitude;
    
    16  }
    
    17 
    
    18  @Override
    
    19  public void setAmplitude(@NonNull Amplitude amplitude) {
    
    20    this.amplitude = amplitude;
    
    21  }
    
    22 
    
    23  @NonNull
    
    24  @Override
    
    25  public Type getType() {
    
    26    return Type.Enrichment;
    
    27  }
    
    28 
    
    29  @Nullable
    
    30  @Override
    
    31  public BaseEvent execute(@NonNull BaseEvent baseEvent) {
    
    32    if (baseEvent.getEventProperties() == null) {
    
    33      baseEvent.setEventProperties(new HashMap<String, Object>());
    
    34    }
    
    35    baseEvent.getEventProperties().put("custom android event property", "test");
    
    36    return baseEvent;
    
    37  }
    
    38 
    
    39  @Override
    
    40  public void setup(@NonNull Amplitude amplitude) {
    
    41    this.amplitude = amplitude;
    
    42  }
    
    43}
    
    44 
    
    45amplitude.add(new EnrichmentPlugin());

### Destination type plugin example

In a destination plugin, you can overwrite the `track()`, `identify()`,
`groupIdentify()`, `revenue()`, `flush()` functions.

    
    
     1import com.amplitude.core.Amplitude;
    
     2import com.amplitude.core.events.BaseEvent;
    
     3import com.amplitude.core.platform.DestinationPlugin;
    
     4import com.segment.analytics.Analytics;
    
     5import com.segment.analytics.Properties;
    
     6 
    
     7public class SegmentDestinationPlugin extends DestinationPlugin {
    
     8  android.content.Context context;
    
     9  Analytics analytics;
    
    10  String writeKey;
    
    11  public SegmentDestinationPlugin(android.content.Context appContext, String writeKey) {
    
    12    this.context = appContext;
    
    13    this.writeKey = writeKey;
    
    14  }
    
    15  @Override
    
    16  public void setup(Amplitude amplitude) {
    
    17    super.setup(amplitude);
    
    18    analytics = new Analytics.Builder(this.context, this.writeKey)
    
    19    .build();
    
    20 
    
    21    Analytics.setSingletonInstance(analytics);
    
    22    }
    
    23 
    
    24  @Override
    
    25  public BaseEvent track(BaseEvent event) {
    
    26    Properties properties = new Properties();
    
    27    for (Map.Entry<String,Object> entry : event.getEventProperties().entrySet()) {
    
    28      properties.putValue(entry.getKey(),entry.getValue());
    
    29    }
    
    30    analytics.track(event.eventType, properties);
    
    31    return event;
    
    32    }
    
    33}
    
    34 
    
    35amplitude.add(
    
    36new SegmentDestinationPlugin(this, SEGMENT_WRITE_KEY)
    
    37)

## Debugging

Ensure that the configuration and payload are accurate and check for any
unusual messages during the debugging process. If everything appears to be
right, check the value of `flushQueueSize` or `flushIntervalMillis`. Events
are queued and sent in batches by default, which means they don't dispatch to
the server. Ensure that you have waited for the events to be sent to the
server before checking for them in the charts.

### Log

  * Set the log level to debug to collect useful information during debugging.
  * Customize `loggerProvider` class from the `LoggerProvider` and implement your own logic, such as logging error message in server in a production environment. For more information, see Set log callback.

### Plugins

You can take advantage of a destination plugin to print out the configuration
value and event payload before sending them to the server. You can set the
`logLevel` to debug, copy the following `TroubleShootingPlugin` into your
project, add the plugin into the Amplitude instance.

  * [Java TroubleShootingPlugin example](https://github.com/amplitude/Amplitude-Kotlin/blob/main/samples/java-android-app/src/main/java/com/amplitude/android/sample/TroubleShootingPlugin.java).
  * [Kotlin TroubleShootingPlugin example](https://github.com/amplitude/Amplitude-Kotlin/blob/main/samples/kotlin-android-app/src/main/java/com/amplitude/android/sample/TroubleShootingPlugin.kt).

### Event callback

The event callback executes after the event is sent, for both successful and
failed events. Use this method to monitor the event status and message. For
more information, the Callback configuration setting.

## Advanced topics

### User sessions

Amplitude starts a session when the app is brought into the foreground or when
an event is tracked in the background. A session ends when the app remains in
the background for more than the time set by
`setMinTimeBetweenSessionsMillis()` without any event being tracked. Note that
a session will continue for the entire time the app is in the foreground no
matter whether session tracking is enabled by
`configuration.trackingSessionEvents`, `configuration.defaultTracking`,
`configuration.autocapture` or not.

When the app enters the foreground, Amplitude tracks a session start, and
starts a countdown based on `setMinTimeBetweenSessionsMillis()`. Amplitude
extends the session and restarts the countdown any time it tracks a new event.
If the countdown expires, Amplitude waits until the next event to track a
session end event.

Amplitude doesn't set user properties on session events by default. To add
these properties, use `identify()` and `setUserId()`. Amplitude aggregates the
user property state and associates the user with events based on `device_id`
or `user_id`.

Due to the way in which Amplitude manages sessions, there are scenarios where
the SDK works expected but it may appear as if events are missing or session
tracking is inaccurate:

  * If a user doesn't return to the app, Amplitude does not track a session end event to correspond with a session start event.
  * If you track an event in the background, it's possible that Amplitude perceives the session length to be longer than the user spends on the app in the foreground.
  * If you modify user properties between the last event and the session end event, the session end event reflects the updated user properties, which may differ from other properties associated with events in the same session. To address this, use an enrichment plugin to set `event['$skip_user_properties_sync']` to `true` on the session end event, which prevents Amplitude from synchronizing properties for that specific event. See [$skip_user_properties_sync](/docs/data/converter-configuration-reference/#skip_user_properties_sync) in the Converter Configuration Reference article to learn more.

Amplitude groups events together by session. Events that are logged within the
same session have the same `session_id`. Sessions are handled automatically so
you don't have to manually call `startSession()` or `endSession()`.

You can adjust the time window for which sessions are extended. The default
session expiration time is 30 minutes.

KotlinJava

    
    
    1amplitude = Amplitude(
    
    2  Configuration(
    
    3    apiKey = AMPLITUDE_API_KEY,
    
    4    context = applicationContext,
    
    5    minTimeBetweenSessionsMillis = 10000
    
    6  )
    
    7)
    
    
    1Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    2configuration.setMinTimeBetweenSessionsMillis(1000);
    
    3 
    
    4Amplitude amplitude = new Amplitude(configuration);

By default, Amplitude automatically sends the '[Amplitude] Start Session' and
'[Amplitude] End Session' events. Even though these events aren't sent,
sessions are still tracked by using `session_id`. You can also disable those
session events.

KotlinJava

    
    
    1amplitude = Amplitude(
    
    2  Configuration(
    
    3    apiKey = AMPLITUDE_API_KEY,
    
    4    context = applicationContext,
    
    5    autocapture = setOf()
    
    6  )
    
    7)
    
    
    1amplitude = AmplitudeKt.Amplitude(AMPLITUDE_API_KEY, getApplicationContext(), configuration -> {
    
    2    configuration.getAutocapture().remove(AutocaptureOption.SESSION);
    
    3    return Unit.INSTANCE;
    
    4});

Use the helper method `getSessionId` to get the value of the current
`sessionId`.

KotlinJava

    
    
    1amplitude = Amplitude(
    
    2  Configuration(
    
    3    apiKey = AMPLITUDE_API_KEY,
    
    4    context = applicationContext,
    
    5    minTimeBetweenSessionsMillis = 10000
    
    6  )
    
    7)
    
    
    1Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    2configuration.setMinTimeBetweenSessionsMillis(10000);
    
    3 
    
    4Amplitude amplitude = new Amplitude(configuration);

You can also track events as out-of-session. Out-of-session events have a
`sessionId` of `-1` and behave as follows:

  1. Aren't part of the current session.
  2. Don't extend the current session.
  3. Don't start a new session.
  4. Don't change the `sessionId` for subsequent events.

A potential use case is for events tracked from push notifications, which are
usually external to the customers app usage.

Set the `sessionId` to `-1` in `EventOptions` to mark an event as out-of-
session when you call `track(event, options)` or `identify(identify,
options)`.

KotlinJava

    
    
     1val outOfSessionOptions = EventOptions().apply {
    
     2 sessionId = -1
    
     3}
    
     4amplitude.identify(
    
     5 Identify().set("user-prop", true),
    
     6 outOfSessionOptions
    
     7)
    
     8amplitude.track(
    
     9 BaseEvent().apply { eventType = "test event" },
    
    10 outOfSessionOptions
    
    11)
    
    
     1EventOptions outOfSessionOptions = new EventOptions();
    
     2outOfSessionOptions.setSessionId(-1L);
    
     3 
    
     4amplitude.identify(
    
     5 new Identify().set("user-prop", true),
    
     6 outOfSessionOptions
    
     7);
    
     8 
    
     9BaseEvent event = new BaseEvent();
    
    10event.eventType = "test event";
    
    11amplitude.track(event, outOfSessionOptions);

### Log level

Control the level of logs that print to the developer console.

  * `INFO`: Shows informative messages about events.
  * `WARN`: Shows error messages and warnings. This level logs issues that might be a problem and cause some oddities in the data. For example, this level would display a warning for properties with null values.
  * `ERROR`: Shows error messages only.
  * `DISABLE`: Suppresses all log messages.
  * `DEBUG`: Shows error messages, warnings, and informative messages that may be useful for debugging.

Set the log level by calling `setLogLevel` with the level you want.

KotlinJava

    
    
    1amplitude.logger.logMode = Logger.LogMode.DEBUG
    
    
    1amplitude.getLogger().setLogMode(Logger.LogMode.DEBUG);

### Logged out and anonymous users

Amplitude [merges user data](/docs/cdp/sources/instrument-track-unique-users),
so any events associated with a known `userId` or `deviceId` are linked the
existing user. If a user logs out, Amplitude can merge that user's logged-out
events to the user's record. You can change this behavior and log those events
to an anonymous user instead.

To log events to an anonymous user:

  1. Set the `userId` to null.
  2. Generate a new `deviceId`.

Events coming from the current user or device appear as a new user in
Amplitude. Note: If you do this, you can't see that the two users were using
the same device.

    
    
    1amplitude.reset()

### Disable tracking

By default the Android SDK tracks several user properties such as `carrier`,
`city`, `country`, `ip_address`, `language`, and `platform`. Use the provided
`TrackingOptions` interface to customize and toggle individual fields.

To use the `TrackingOptions` interface, import the class.

    
    
    1import com.amplitude.android.TrackingOptions

Before initializing the SDK with your `apiKey`, create a `TrackingOptions`
instance with your configuration and set it on the SDK instance.

KotlinJava

    
    
    1val trackingOptions = TrackingOptions()
    
    2trackingOptions.disableCity().disableIpAddress().disableLatLng()
    
    3amplitude = Amplitude(
    
    4  Configuration(
    
    5    apiKey = AMPLITUDE_API_KEY,
    
    6    context = applicationContext,
    
    7    trackingOptions = trackingOptions
    
    8  )
    
    9)
    
    
    1TrackingOptions trackingOptions = new TrackingOptions();
    
    2trackingOptions.disableCity().disableIpAddress().disableLatLng();
    
    3 
    
    4// init instance
    
    5amplitude = AmplitudeKt.Amplitude(AMPLITUDE_API_KEY, getApplicationContext(), configuration -> {
    
    6 configuration.setTrackingOptions(trackingOptions);
    
    7 return Unit.INSTANCE;
    
    8});

Tracking for each field can be individually controlled, and has a
corresponding method (for example, `disableCountry`, `disableLanguage`).

Method | Description  
---|---  
`disableAdid()` | Disable tracking of Google ADID  
`disableAppSetId()` | Disable tracking of App Set Id  
`disableCarrier()` | Disable tracking of device's carrier  
`disableCity()` | Disable tracking of user's city  
`disableCountry()` | Disable tracking of user's country  
`disableDeviceBrand()` | Disable tracking of device brand  
`disableDeviceModel()` | Disable tracking of device model  
`disableTrackDeviceManufacturer()` | Disable tracking of device manufacturer  
`disableDma()` | Disable tracking of user's designated market area (DMA).  
`disableIpAddress()` | Disable tracking of user's IP address  
`disableLanguage()` | Disable tracking of device's language  
`disableLatLng()` | Disable tracking of user's current latitude and longitude coordinates  
`disableOsName()` | Disable tracking of device's OS Name  
`disableOsVersion()` | Disable tracking of device's OS Version  
`disablePlatform()` | Disable tracking of device's platform  
`disableRegion()` | Disable tracking of user's region.  
`disableVersionName()` | Disable tracking of your app's version name  
`disableApiLevel` | Disable tracking of Android API level  
  
## Note

Using `TrackingOptions` only prevents default properties from being tracked on
newly created projects, where data has not yet been sent. If you have a
project with existing data that you want to stop collecting the default
properties for, get help in the [Amplitude
Community](https://community.amplitude.com/). Disabling tracking doesn't
delete any existing data in your project.

### Carrier

Amplitude determines the user's mobile carrier using [Android's
TelephonyManager](https://developer.android.com/reference/kotlin/android/telephony/TelephonyManager#getnetworkoperatorname)
`networkOperatorName`, which returns the current registered operator of the
`tower`.

### COPPA control

COPPA (Children's Online Privacy Protection Act) restrictions on IDFA, IDFV,
city, IP address and location tracking can all be enabled or disabled at one
time. Apps that ask for information from children under 13 years of age must
comply with COPPA.

KotlinJava

    
    
    1amplitude = Amplitude(
    
    2  Configuration(
    
    3    apiKey = AMPLITUDE_API_KEY,
    
    4    context = applicationContext,
    
    5    enableCoppaControl = true //Disables ADID, city, IP, and location tracking
    
    6  )
    
    7)
    
    
    1Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    2//Disables ADID, city, IP, and location tracking
    
    3configuration.setEnableCoppaControl(true);
    
    4 
    
    5Amplitude amplitude = new Amplitude(configuration);

### Advertiser ID

The Android Advertising ID is a unique identifier provided by the Google Play
store. As it's unique to every person and not just their devices, it's useful
for mobile attribution. This is similar to the IDFA on iOS. [Mobile
attribution](https://www.adjust.com/blog/mobile-ad-attribution-introduction-
for-beginners/) is the attribution of an installation of a mobile app to its
original source (such as ad campaign, app store search). Users can choose to
disable the Advertising ID, and apps targeted to children can't track at all.

Follow these steps to use Android Ad ID.

## Warning

As of April 1, 2022, Google allows users to opt out of Ad ID tracking. Ad ID
may return null or error. You can use an alternative ID called App Set ID,
which is unique to every app install on a device. [Learn
more](https://support.google.com/googleplay/android-
developer/answer/6048248?hl=en).

  1. Add `play-services-ads-identifier` as a dependency.
    
        1dependencies {
    
    2  implementation 'com.google.android.gms:play-services-ads-identifier:18.0.1'
    
    3}

  2. `AD_MANAGER_APP` Permission If you use Google Mobile Ads SDK version 17.0.0 or higher, you need to add `AD_MANAGER_APP` to `AndroidManifest.xml`.
    
        1<manifest>
    
    2    <application>
    
    3        <meta-data
    
    4            android:name="com.google.android.gms.ads.AD_MANAGER_APP"
    
    5            android:value="true"/>
    
    6    </application>
    
    7</manifest>

  3. Add ProGuard exception

Amplitude Android SDK uses Java Reflection to use classes in Google Play
Services. For Amplitude SDKs to work in your Android application, add these
exceptions to `proguard.pro` for the classes from `play-services-ads`. `-keep
class com.google.android.gms.ads.** { *; }`

  4. `AD_ID` Permission

When apps update their target to Android 13 or above will need to declare a
Google Play services normal permission in the manifest file as follows if you
are trying to use the ADID as a deviceId:

    
        1<uses-permission android:name="com.google.android.gms.permission.AD_ID"/>

Learn More [here](https://support.google.com/googleplay/android-
developer/answer/6048248?hl=en).

#### Use the advertising ID as the device ID

After you set up the logic to fetch the advertising ID, you can enable
`useAdvertisingIdForDeviceId` to use advertising id as the device ID.

KotlinJava

    
    
    1amplitude = Amplitude(
    
    2  Configuration(
    
    3    apiKey = AMPLITUDE_API_KEY,
    
    4    context = applicationContext,
    
    5    useAdvertisingIdForDeviceId = true
    
    6  )
    
    7)
    
    
    1Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    2configuration.setUseAdvertisingIdForDeviceId(true);
    
    3 
    
    4Amplitude amplitude = new Amplitude(configuration);

### App set ID

App set ID is a unique identifier for each app install on a device. App set ID
is reset by the user manually when they uninstall the app, or after 13 months
of not opening the app. Google designed this as a privacy-friendly alternative
to Ad ID for users who want to opt out of stronger analytics.

To use app set ID, follow these steps.

  1. Add `play-services-appset` as a dependency. For versions earlier than 2.35.3, use `'com.google.android.gms:play-services-appset:16.0.0-alpha1'`
    
        1dependencies {
    
    2implementation 'com.google.android.gms:play-services-appset:16.0.2'
    
    3}

  2. Enable to use app set ID as Device ID.

KotlinJava

    
        1amplitude = Amplitude(
    
    2  Configuration(
    
    3  apiKey = AMPLITUDE_API_KEY,
    
    4  context = applicationContext,
    
    5  useAppSetIdForDeviceId = true
    
    6  )
    
    7)
    
        1Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    2configuration.setUseAppSetIdForDeviceId(true);
    
    3 
    
    4Amplitude amplitude = new Amplitude(configuration);

### Device ID lifecycle

The SDK initializes the device ID in the following order, with the device ID
being set to the first valid value encountered:

  1. Device ID of the instance
  2. ADID if `useAdvertisingIdForDeviceId` is enabled and required module is installed. Learn more
  3. App Set ID with an `S` appended if `useAppSetIdForDeviceId` is enabled and required module is installed. Learn more
  4. A randomly generated UUID with an `R` appended

#### One user with multiple devices

A single user may have multiple devices, each having a different device ID. To
ensure coherence, set the user ID consistently across all these devices. Even
though the device IDs differ, Amplitude can still merge them into a single
Amplitude ID, thus identifying them as a unique user.

#### Transfer to a new device

It's possible for multiple devices to have the same device ID when a user
switches to a new device. When transitioning to a new device, users often
transfer their applications along with other relevant data. The specific
transferred content may vary depending on the application. In general, it
includes databases and file directories associated with the app. However, the
exact items included depend on the app's design and the choices made by the
developers. If databases or file directories have been backed up from one
device to another, the device ID stored within them may still be present. If
the SDK attempts to retrieve it during initialization, different devices might
end up using the same device ID.

#### Get device ID

Use the helper method `getDeviceId()` to get the value of the current
`deviceId`.

KotlinJava

    
    
    1val deviceId = amplitude.getDeviceId();
    
    
    1String deviceId = amplitude.getDeviceId();

To set the device, see to custom device ID.

### Location tracking

Amplitude converts the IP of a user event into a location (GeoIP lookup) by
default. This information may be overridden by an app's own tracking solution
or user data.

By default, Amplitude can use Android location service (if available) to add
the specific coordinates (longitude and latitude) for the location from which
an event is logged. Control this behavior by enable / disable location
listening during the initialization.

KotlinJava

    
    
    1amplitude = Amplitude(
    
    2  Configuration(
    
    3    apiKey = AMPLITUDE_API_KEY,
    
    4    context = applicationContext,
    
    5    locationListening = true
    
    6  )
    
    7)
    
    
    1Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    2configuration.setLocationListening(true);
    
    3 
    
    4Amplitude amplitude = new Amplitude(configuration);

## Proguard obfuscation

If you use ProGuard obfuscation, add the following exception to the file:
`-keep class com.google.android.gms.common.** { *; }`

### Opt users out of tracking

Users may wish to opt out of tracking entirely, which means Amplitude doesn't
track any of their events or browsing history. `OptOut` provides a way to
fulfill a user's requests for privacy.

KotlinJava

    
    
    1amplitude = Amplitude(
    
    2  Configuration(
    
    3    apiKey = AMPLITUDE_API_KEY,
    
    4    context = applicationContext,
    
    5    optOut = true
    
    6  )
    
    7)
    
    
    1Configuration configuration = new Configuration(AMPLITUDE_API_KEY, getApplicationContext());
    
    2configuration.setOptOut(true);
    
    3 
    
    4Amplitude amplitude = new Amplitude(configuration);

### Push notification events

Don't send push notification events client-side with the Android SDK. Because
a user must open the app to initialize the Amplitude SDK in order for the SDK
to send the event, events aren't sent to the Amplitude servers until the next
time the user opens the app. This can cause data delays.

KotlinJava

    
    
     1import com.amplitude.common.Logger
    
     2import com.amplitude.core.LoggerProvider
    
     3 
    
     4class sampleLogger : Logger {
    
     5override var logMode: Logger.LogMode
    
     6 get() = Logger.LogMode.DEBUG
    
     7 set(value) {}
    
     8 
    
     9 override fun debug(message: String) {
    
    10 TODO("Handle debug message here")
    
    11 }
    
    12 
    
    13 override fun error(message: String) {
    
    14 TODO("Handle error message here")
    
    15 }
    
    16 
    
    17 override fun info(message: String) {
    
    18 TODO("Handle info message here")
    
    19 }
    
    20 
    
    21 override fun warn(message: String) {
    
    22 TODO("Handle warn message here")
    
    23 }
    
    24}
    
    25 
    
    26class sampleLoggerProvider : LoggerProvider {
    
    27 override fun getLogger(amplitude: com.amplitude.core.Amplitude): Logger {
    
    28 return sampleLogger()
    
    29 }
    
    30}
    
    31 
    
    32amplitude = Amplitude(
    
    33 Configuration(
    
    34 apiKey = AMPLITUDE_API_KEY,
    
    35 context = applicationContext,
    
    36 loggerProvider = sampleLoggerProvider()
    
    37 )
    
    38)
    
    
     1import com.amplitude.common.Logger;
    
     2import com.amplitude.core.LoggerProvider;
    
     3 
    
     4class sampleLogger implements Logger {
    
     5 @NonNull
    
     6 @Override
    
     7 public LogMode getLogMode() {
    
     8 return LogMode.DEBUG;
    
     9 }
    
    10 
    
    11 @Override
    
    12 public void setLogMode(@NonNull LogMode logMode) {
    
    13 // TODO("Handle debug message here")
    
    14 }
    
    15 
    
    16 @Override
    
    17 public void debug(@NonNull String message) {
    
    18 // TODO("Handle debug message here")
    
    19 }
    
    20 
    
    21 @Override
    
    22 public void error(@NonNull String message) {
    
    23 // TODO("Handle error message here")
    
    24 }
    
    25 
    
    26 @Override
    
    27 public void info(@NonNull String message) {
    
    28 // TODO("Handle info message here")
    
    29 }
    
    30 
    
    31 @Override
    
    32 public void warn(@NonNull String message) {
    
    33 // TODO("Handle warn message here")
    
    34 }
    
    35}
    
    36 
    
    37class sampleLoggerProvider implements LoggerProvider {
    
    38 @NonNull
    
    39 @Override
    
    40 public Logger getLogger(@NonNull com.amplitude.core.Amplitude amplitude) {
    
    41 return new sampleLogger();
    
    42 }
    
    43}

### Multiple instances

You can create multiple instances of Amplitude. Instances with the same
`instanceName` share storage and identity. For isolated storage and identity
use a unique `instanceName` for each instance. For more details see
Configuration.

    
    
     1val amplitude1 = Amplitude(Configuration(
    
     2 instanceName = "one",
    
     3 apiKey = "api-key-1",
    
     4 context = applicationContext,
    
     5))
    
     6val amplitude2 = Amplitude(Configuration(
    
     7 instanceName = "two",
    
     8 apiKey = "api-key-2",
    
     9 context = applicationContext,
    
    10))

### Offline mode

Starting from version 1.13.0, the Amplitude Android Kotlin SDK supports
offline mode. The SDK checks network connectivity every time it tracks an
event. If the device is connected to network, the SDK schedules a flush. If
not, it saves the event to storage. The SDK also listens for changes in
network connectivity and flushes all stored events when the device reconnects.

To enable this feature, add the `ACCESS_NETWORK_STATE` permission to
`AndroidManifest.xml`. Otherwise, the SDK flushes the event based on
`flushIntervalMillis` and `flushQueueSize`.

    
    
    1<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

You can also implement you own offline logic:

  1. Set `config.offline` to `AndroidNetworkConnectivityCheckerPlugin.Disabled` to disable the default offline logic.
  2. Toggle `config.offline` by yourself

##### SDK Details

[![](https://img.shields.io/maven-central/v/com.amplitude/analytics-
android.svg?label=Maven%20Central)](https://mvnrepository.com/artifact/com.amplitude/analytics-
android)

[](https://github.com/amplitude/Amplitude-Kotlin)
[](https://github.com/amplitude/Amplitude-Kotlin/releases)

Was this page helpful?

Thanks for your feedback!

July 23rd, 2024

Need help? [Contact Support](https://help.amplitude.com/hc/en-us/requests/new)

Visit [Amplitude.com](https://www.amplitude.com)

Have a look at the Amplitude [Blog](https://amplitude.com/blog)

Learn more at [Amplitude Academy](https://academy.amplitude.com/)

[ ](https://www.linkedin.com/company/amplitude-analytics) [
](https://twitter.com/Amplitude_HQ) [ ](https://www.g2.com/products/amplitude-
analytics/reviews)

[Terms of Service](https://amplitude.com/terms) [Privacy
Notice](https://amplitude.com/privacy) [Acceptable Use
Policy](https://amplitude.com/aup) [Legal](https://amplitude.com/legal)

© 2024 Amplitude, Inc. All rights reserved. Amplitude is a registered
trademark of Amplitude, Inc.

