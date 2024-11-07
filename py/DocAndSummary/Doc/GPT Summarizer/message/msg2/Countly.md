SDK name: Countly
Documentation:
[ ![logo](/hc/theming_assets/01HZKRSF1QE2BNTTBS303AMZTW)
![logo](/hc/theming_assets/01HZKRSF6STFGDGTN3VRX54BZ4) ](/hc/en-us "Home")

Help Center

[Community](https://discord.gg/countly) [Submit a request](/hc/en-
us/requests/new) [Sign in](/hc/en-
us/signin?return_to=https%3A%2F%2Fsupport.countly.com%2Fhc%2Fen-
us%2Farticles%2F360037754031-Android&locale=en-us "Opens a dialog")

Hello. How can we help?

  1. [Countly](/hc/en-us)
  2. [Knowledge Base](/hc/en-us/categories/360002373332-Knowledge-Base)
  3. [SDK Integration](/hc/en-us/sections/360007310512-SDK-Integration)

#  Android

[Follow](/hc/en-us/articles/360037754031-Android/subscription.html "Opens a
sign-in dialog")

Last modified: August 14, 2024 13:21

This documentation is for the Countly Android SDK version 24.7.X. The SDK
source code repository can be found [here](https://github.com/Countly/countly-
sdk-android).

Click [here, ](https://support.count.ly/hc/en-
us/articles/360037236571-Downloading-and-Installing-
SDKs#h_01H9QCP8G73H5RWXFK9P9W6F7Q)to access the documentation for older SDK
versions.

The Countly Android SDK requires a minimum Android version of 5.0 (API Level
21).

To examine the example integrations please have a look here.

# Adding the SDK to the Project

You need to use the MavenCentral repository to download the SDK package. If it
is not included in your project, include it, with the following code:

    
    
    buildscript {
      repositories {
          mavenCentral()
      }
    }

Now, add the Countly SDK dependency (**use the latest SDK version currently
available from gradle, not specifically the one shown in the sample below**).

    
    
    dependencies {
      implementation 'ly.count.android:sdk:24.7.2'
    }

# SDK Integration

Before you can use any functionality, you have to initiate the SDK. That can
be done either in your `Application` subclass (preferred), or from your main
activity `onCreate` method.

## Minimal Setup

The shortest way to initiate the SDK is with this call:

    
    
    Countly.sharedInstance().init(new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL));

It is there that you provide the Android context, your appKey, and your
Countly server URL. Please check [here](https://support.count.ly/hc/en-
us/articles/900000908046-Getting-started-with-
SDKs#h_01HABSX9KX44C9SF48WRPQNCP3) for more information on how to acquire your
application key (APP_KEY) and server URL.

To configure the SDK during init, a config object called "CountlyConfig" is
used. Configuration is done by creating such an object and then calling it's
provided function calls to enable the functionality that you need. Afterwards,
the particular config object is provided to the "init" method.

If you are in doubt about the correctness of your Countly SDK integration you
can learn about the verification methods from
[here](https://support.count.ly/hc/en-us/articles/900000908046-Getting-
started-with-SDKs#h_01HABSX9KXE6YKVETHDWPP8J3K).

## Adding callbacks

After the `Countly.sharedInstance().init(...)`call, you'll need to add the
following calls to all your activities:

  * Call `Countly.sharedInstance().onStart(this)` in onStart, where `this` is a link to the current Activity.
  * Call `Countly.sharedInstance().onStop()` in onStop.
  * Call `Countly.sharedInstance().onConfigurationChanged(newConfig)` in onConfigurationChanged if you want to track the orientation changes.

If the "onStart" and "onStop" calls are not added, some functionalities will
not work, e.g. automatic sessions will not be tracked. The Countly "onStart"
has to be called in the activities "onStart" function, it cannot be called in
"onCreate" or in any other place, otherwise, the application will receive
exceptions.

![](https://archive.count.ly/images/guide/283f96f-activity_lifecycle.png)

## Required App Permissions

Additionally, ensure the  _INTERNET_ and  _ACCESS_NETWORK_STATE_ permissions
are set if there aren’t any, in your manifest file. Those calls should look
something like this:

    
    
    <uses-permission android:name="android.permission.INTERNET"/>  
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />

# SDK Logging

The first thing you should do while integrating our SDK is enable logging. If
logging is enabled, then our SDK will print out debug messages about its
internal state and encountered problems. Those messages may be screened in
logcat and may use Android's internal log calls.

Call `setLoggingEnabled` on the config class to enable logging:

    
    
    CountlyConfig config = (new CountlyConfig(appC, COUNTLY_APP_KEY, COUNTLY_SERVER_URL));  
    config.setLoggingEnabled(true);

For more information on where to find the SDK logs you can check the
documentation [here](https://support.count.ly/hc/en-
us/articles/900000908046-Getting-started-with-
SDKs#h_01HABSX9KXC5S8Q1NQWDZ33HXC).

# Crash Reporting

The Countly SDK for Android has the ability to collect [crash
reports](https://support.count.ly/hc/en-us/articles/4404213566105), which you
may examine and resolve later on the server.

In the SDK all crash-related functionality can be browsed from the returned
interface on:

    
    
    Countly.sharedInstance().crashes()

## Automatic Crash Handling

To enable automatic crash reporting, call the following function on the config
object. After init, this will enable crash reporting, which will automatically
catch uncaught Java exceptions. They will be sent to the dashboard once the
app is launched again and the SDK is initiated.

    
    
    config.enableCrashReporting();

## Automatic Crash Report Segmentation

You may add a key/value segment to crash reports. For example, you could set
which specific library or framework version you used in your app. You may then
figure out if there is any correlation between the specific library or another
segment and the crash reports.

Use the following function for this purpose:

    
    
    config.setCustomCrashSegment(Map<String, String> segments)

## Handled Exceptions

You might catch an exception or similar error during your app’s runtime.

You may also log these handled exceptions to monitor how and when they are
happening with the following command:

    
    
    Countly.sharedInstance().crashes().recordHandledException(Exception exception);

If you have handled an exception and it turns out to be fatal to your app, you
may use this call:

    
    
    Countly.sharedInstance().crashes().recordUnhandledException(Exception exception);

## Crash Breadcrumbs

Throughout your app you can leave crash breadcrumbs which would describe
previous steps that were taken in your app before the crash. After a crash
happens, they will be sent together with the crash report.

Following the command adds crash breadcrumb:

    
    
    Countly.sharedInstance().crashes().addCrashBreadcrumb(String record) 

## Crash Filtering

There might be cases where a crash could contain sensitive information. For
such situations, there is a crash filtering option that can discard or modify
a crash.

To filter a crash you should provide a callback to the config object using the
`crashes.setGlobalCrashFilterCallback` method during initialization. This
callback will be called every time a crash is recorded.

The callback receives a `CrashData` object, which contains all the information
about the crash that would be sent to the server:

    
    
    class CrashData {
      String stackTrace;
      Map<String, Object> crashSegmentation;
      List<String> breadcrumbs;
      boolean fatal;
      Map<String, Object> crashMetrics;
    }

\- **stackTrace** : Concatenated stack trace with new lines.

\- **crashSegmentation** : Combination of automatic crash report segmentation
and segmentation given while recording the crash.

\- **breadcrumbs** : List of recorded breadcrumbs.

\- **fatal** : Indicates whether or not a crash is unhandled.

\- **crashMetric** : Crash related [metrics](https://support.count.ly/hc/en-
us/articles/9290669873305-A-deeper-look-at-SDK-
concepts#h_01HJ5V4WX0XFP7FC8ETDC3B96M) recorded by the SDK.

You can modify or filter the crash using the getter and setter methods
provided by the CrashData. After modifying the crash, to send the crash to the
server, you should return 'false.' If the callback returns 'true' the crash
will be discarded:

    
    
    config.crashes.setGlobalCrashFilterCallback(new GlobalCrashFilterCallback() {
      @Override
      public boolean filterCrash(CrashData crash) {
        // You may want to omit a secret from the stack trace to protect it
        crash.setStackTrace(crash.getStackTrace().replace("secret", "*****"));
        // or if crash segmentation contains a secret key, it can me omitted
        if (crash.getCrashSegmentation().containsKey("secret")) {
          // You can change a crash is handled or not
          crash.setFatal(false);
          // The secret value could be overridden easily to protect it
          crash.getCrashSegmentation().put("secret", "*****");
        }
    
        // Maybe when reporting crashes, only a device  permitted to report the crashes for testing or debugging
        if (crash.getCrashMetrics().containsKey("_device")) {
          // if metrics has a device other than an Android, discard crash
          Object device = crash.getCrashMetrics().get("_device");
          if (device instanceof String) {
            return !device.equals("Android");
          } else {
            // if value not found or not a string, discard the crash
            return true;
          }
        }
        return false;
      }
    });

## Recording all threads

If you would like to record the state of all other threads during an uncaught
exception or during the recording of a handled exception, you can call this
during init:

    
    
    config.setRecordAllThreadsWithCrash();

## Native C++ Crash Reporting

Due to the limitations of the `dump_syms` binary, C++ symbol extraction and
automatic upoload of them is only supported on Linux devices.

Countly uses [Google's Breakpad open source
library](https://github.com/google/breakpad) to be able to report crashes that
occurred within the C++ components of your application, assuming there are
any. Breakpad provides:

  * a tool for creating symbol files from your object files (`dump_syms`)
  * the ability to detect and record crashes via compact minidump files (crash handler)
  * a tool for generating human readable stack traces by using symbol files and crash minidump files.

![](https://count.ly/images/guide/7cbb985-breakpad.png)

Countly provides the [sdk_native](https://github.com/Countly/countly-sdk-
android/tree/master/sdk-native) Android library to add crash handler to your
native code and create crash minidump files. The SDK will check for those
minidump files and send them automatically to your Countly server upon
application start. You would download `sdk_native` from the MavenCentral
repository and include it in your project, similar to how you included our SDK
(please change the `LATEST_VERSION` below by checking our Maven
[page](https://central.sonatype.com/artifact/ly.count.android/sdk/versions),
currently 23.8.3):

    
    
    // build gradle file
    repositories {
      mavenCentral()
    }
    
    dependencies {
      implementation 'ly.count.android:sdk-native:LATEST_VERSION'
    }

Then call our init method as early as possible in your application life cycle
to be able to catch crashes that occur during initialization:

    
    
    import ly.count.android.sdknative.CountlyNative;
    
    CountlyNative.initNative(getApplicationContext());

`getApplicationContext()` is needed to determine a storage place for minidump
files.

## Symbolication

You may create Breakpad symbol files yourself and upload them to your Countly
server using our UI. They will be needed to create stack traces from minidump
files. Countly also developed a Gradle plugin to automate this process. To use
the upload plugin in Studio, you first need to include it:

### Automatic symbol file upload

build.gradle build.gradle.kts

    
    
    plugins {
      id "ly.count.android.plugins.upload-symbols" version "24.7.2"
    }
    
    
    plugins {
      id("ly.count.android.plugins.upload-symbols") version "24.7.2"
    }

If you have root level gradle file and want to enable the plugin for sub-
projects, add `apply false` to the end of the lines. And in sub-projects add
it to `plugins` block without version part.

build.gradle build.gradle.kts

    
    
    // in root level gradle file
    plugins {
      id "ly.count.android.plugins.upload-symbols" version "24.7.2" apply false
    }
        
    // in sub-project gradle file
    plugins {
      id "ly.count.android.plugins.upload-symbols"
    }
    
    
    // in root level gradle file
    plugins {
      id("ly.count.android.plugins.upload-symbols") version "24.7.2" apply false
    }
        
    // in sub-project gradle file
    plugins {
      id("ly.count.android.plugins.upload-symbols")
    }

If you do not have `plugins` block in sub-projects, you can add them via:

build.gradle build.gradle.kts

    
    
    apply plugin: ly.count.android.plugins.UploadSymbolsPlugin
    
    
    
    apply(plugin = "ly.count.android.plugins.upload-symbols")
    

Then you will need to configure a Gradle Countly block for the plugin:

build.gradle build.gradle.kts

    
    
    countly {
      server "https://YOUR_SERVER"
      app_key "YOUR_APP_KEY"  
    }
    
    
    countly {
      server = "https://YOUR_SERVER"
      app_key = "YOUR_APP_KEY"  
    }

Next, you will have two new Gradle tasks available to you: `uploadJavaSymbols`
and `uploadNativeSymbols`. `uploadJavaSymbols` is for uploading the
`mapping.txt` file generated by Proguard. After building your project, you may
run these tasks through Studio's Gradle tool window (1). They will be
available under your app (2) and grouped as Countly tasks (3).

![](https://count.ly/images/guide/6ddc195-Selection_006.png)

Another option is to run them from the command line:

    
    
    ./gradlew uploadNativeSymbols
    
    // or if you have subprojects
    
    ./gradlew :project-name:uploadNativeSymbols

You may also configure your build so these tasks will run after every build
(leave out the task which is not required for you):

    
    
    tasks.whenTaskAdded { task ->
      if (task.name.startsWith('assemble')) {
        //this would upload your Java mapping file
        task.dependsOn('uploadJaveSymbols')
    
        //this would upload your native (c++) symbols
        task.dependsOn('uploadNativeSymbols')
      }
    }

In addition, you may also override some default values in the Countly block in
an effort to specify your server and app info.

build.gradle build.gradle.kts

    
    
    countly {
      // required by both tasks
      server "https://try.count.ly"
      app_key "XXXXXX"  // same app_key used for SDK integration
    
      // optional properties for uploadJavaSymbols. Shown are the default values.
    
      // location of mapping.txt file relative to project build directory
      mappingFile "outputs/mapping/release/mapping.txt"
    
      // note that will be saved with the upload and can be checked in the UI
      noteJava "sdk-plugin automatic upload of mapping.txt"
    
      // optional properties for uploadNativeSymbols. Shown are the default values.
    
      // directory of .so files relative to project build directory.
      // you can check the tar.gz file created under intermediates/countly
      // BUILD_TYPE could be debug or release
      nativeObjectFilesDir "intermediates/merged_native_libs/BUILD_TYPE"
      
      // path for breakpad tool dump_syms executable
      dumpSymsPath "/usr/bin/dump_syms" // note that will be saved with the upload and can be checked in the UI noteNative "sdk-plugin automatic upload of breakpad symbols" }
    }
    
    
    countly {
      // required by both tasks
      server = "https://try.count.ly"
      app_key = "XXXXXX"  // same app_key used for SDK integration
    
      // optional properties for uploadJavaSymbols. Shown are the default values.
    
      // location of mapping.txt file relative to project build directory
      mappingFile = "outputs/mapping/release/mapping.txt"
    
      // note that will be saved with the upload and can be checked in the UI
      noteJava = "sdk-plugin automatic upload of mapping.txt"
    
      // optional properties for uploadNativeSymbols. Shown are the default values.
    
      // directory of .so files relative to project build directory.
      // you can check the tar.gz file created under intermediates/countly
      // BUILD_TYPE could be debug or release
      nativeObjectFilesDir = "intermediates/merged_native_libs/BUILD_TYPE"
    
      // path for breakpad tool dump_syms executable
      dumpSymsPath = "/usr/bin/dump_syms" // note that will be saved with the upload and can be checked in the UI noteNative "sdk-plugin automatic upload of breakpad symbols" }
    }

It is possible that two of these properties will need to be configured
manually: `dumpSymsPath` and `nativeObjectFilesDir`. The plugin assumes you
will run the task after a release build. To test it for debug builds, please
change `nativeObjectFilesDir` to `"intermediates/cmake/debug/obj"` (or to
wherever your build process puts .so files under the build directory).

We created a [sample app](https://github.com/Countly/countly-sdk-
android/tree/master/app-native) in our github repo that demonstrates both how
to use SDK-native and our upload plugin.

# Events

An[ event](https://support.count.ly/hc/en-us/articles/4403721560857-Events) is
any type of action that you can send to a Countly instance, e.g. purchases,
changed settings, view enabled, and so on. This way it's possible to get much
more information from your application compared to what is sent from the
Android SDK to the Countly instance by default.

All data passed to the Countly server via the SDK or API should be in UTF-8.

In the SDK all event-related functionality can be browsed from the returned
interface on:

    
    
    Countly.sharedInstance().events()

When providing segmentation for events, the following primitive data types are
supported: "String," "Integer," "Double," and "Boolean." Additionally, arrays,
Lists, and JSONArrays composed of these primitive types are also supported.
Please note that no other data types will be recorded.

## Recording Events

We have provided an example of recording a **purchase** event below. Here is a
quick summary of the information with which each usage will provide us:

  * Usage 1: how many times the **purchase** event occurred.
  * Usage 2: how many times the **purchase** event occurred + the total amount of those purchases.
  * Usage 3: how many times the **purchase** event occurred + from which countries and application versions those purchases were made.
  * Usage 4: how many times the **purchase** event occurred + the total amount, both of which are also available, segmented into countries and application versions.
  * Usage 5: how many times the **purchase** event occurred + the total amount, both of which are also available, segmented into countries and application versions + the total duration of those events.

**1\. Event key and count**

    
    
    Countly.sharedInstance().events().recordEvent("purchase", 1);

**2\. Event key, count, and sum**

    
    
    Countly.sharedInstance().events().recordEvent("purchase", 1, 0.99);

**3\. Event key and count with segmentation(s)**

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    
    Countly.sharedInstance().events().recordEvent("purchase", segmentation, 1);

**4\. Event key, count, and sum with segmentation(s)**

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    
    Countly.sharedInstance().events().recordEvent("purchase", segmentation, 1, 0.99);

**5\. Event key, count, sum, and duration with segmentation(s)**

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    
    Countly.sharedInstance().events().recordEvent("purchase", segmentation, 1, 0.99, 60);

Those are only a few examples of what you can do with events. You may extend
those examples and use Country, app_version, game_level, time_of_day, and any
other segmentation that will provide you with valuable insights.

## Timed Events

It's possible to create timed events by defining a start and a stop moment.

    
    
    String eventName = "Some event";
    
    //start some event
    Countly.sharedInstance().events().startEvent(eventName);
    //wait some time
    
    //end the event
    Countly.sharedInstance().events().endEvent(eventName);

You may also provide additional information when ending an event. However, in
that case, you have to provide the segmentation, count, and sum. The default
values for those are "null", 1 and 0.

    
    
    String eventName = "Some event";
    
    //start some event
    Countly.sharedInstance().events().startEvent(eventName);
    //wait some time
    
    Map<String, String> segmentation = new HashMap<>();
    segmentation.put("wall", "orange");
    
    //end the event while also providing segmentation information, count and sum
    Countly.sharedInstance().events().endEvent(eventName, segmentation, 4, 34);
    

You may cancel the started timed event in case it is not relevant anymore:

    
    
    //start some event
    Countly.sharedInstance().events().startEvent(eventName);
    //wait some time
    
    //cancel the event
    Countly.sharedInstance().events().cancelEvent(eventName);

## Past Events

In the previous examples, the event creation time is recorded once the event
is created.

In some use cases, you might want to cache and store events by yourself and
then record them in the SDK with a past timestamp. The timestamp is a Unix
timestamp stored in milliseconds. For that you would use:

    
    
    Countly.sharedInstance().events().recordPastEvent(key, segmentation, count, sum, dur, timestamp)

# Sessions

## Automatic Sessions

Countly Android SDK comes with built in automatic session tracking
functionality. Only thing necessary for this functionality to work is to add
the proper calls to your activities after initializing the SDK. For more
information you can check [here](https://support.count.ly/hc/en-
us/articles/360037754031-Android#h_01HAVQDM5SXG0Q4MRTDYXJRA8H).

## Manual Sessions

Sometimes it might be preferable to control the session manually instead of
relying on the SDK.

It can be enabled during init with:

    
    
    config.enableManualSessionControl();

Afterwards it is up to the implementer to make calls to:

  * Begin session
  * Update session duration
  * End session (also updates duration)

The appropriate call to do that are:

    
    
    Countly.sharedInstance().sessions().beginSession();  
    Countly.sharedInstance().sessions().updateSession();  
    Countly.sharedInstance().sessions().endSession();

By default, you should do some session call every 60 seconds after beginning a
session so that it is not closed server side. If you would want to increase
that duration, you would have to increase the "Maximal Session Duration" in
your server API configuration.

### Hybrid Mode

You can modify the manual session control by giving the control of
`updateSession` calls to the SDK. This way you would only need to call
`beginSession` and `endSession` methods and SDK would handle the rest.

    
    
    // after enabling manual sessions
    config.enableManualSessionControlHybridMode();

# View Tracking

In the SDK all view related functionality can be browsed from the returned
interface on:

    
    
    Countly.sharedInstance().views()

## Automatic Views

View tracking is a way to report every screen view to the Countly dashboard.
In order to enable automatic view tracking, call:

    
    
    config.enableAutomaticViewTracking();

The tracked views will use the full activity names which include their package
name. It would look similar to "com.my.company.activityname".

It is possible to use short view names that make use of the simple activity
name. This would look like "activityname". To use this functionality, call
this before calling init:

    
    
    config.enableAutomaticViewShortNames();

If you want to add segmentation to all your automatic views, please have a
look here.

If you want to exclude certain activities from automatic view tracking, you
can let the SDK know during initialization by passing them in an array:

    
    
    config.setAutomaticViewTrackingExclusions(Class[] exclusions);

## Manual View Recording

The SDK provides various ways to track views. You can have a single view at a
given time or track multiple views according to your needs. Each view would
have its own unique view ID which could be used for manipulating the view
further.

### Auto Stopped Views

An easy way to track views is with using the auto stopped views. These views
would stop if another view starts. You can start an auto stopped view with or
without segmentation like this:

    
    
    // without segmentation
    Countly.sharedInstance().views().startAutoStoppedView("View Name");
      
    // Or with segmentation
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    
    Countly.sharedInstance().views().startAutoStoppedView("View Name", segmentation);

It would return a string view ID:

    
    
    String id = Countly.sharedInstance().views().startAutoStoppedView("View Name");

### Regular Views

Opposed to "auto stopped views", with regular views you can have multiple of
them started at the same time, and then you can control them independently.

You can start a view that would not close when another views starts like this:

    
    
    Countly.sharedInstance().views().startView("View Name");

While manually tracking views, you may add your custom segmentation to them
like this:

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
      
    Countly.sharedInstance().views().startView("View Name", segmentation);

These views would also return a string view ID when they are called.

### Stopping Views

You can stop a view with its name or its view ID. To stop it with its name:

    
    
    Countly.sharedInstance().views().stopViewWithName("View Name");

You can provide a segmentation while doing so:

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    
    Countly.sharedInstance().views().stopViewWithName("View Name", segmentation);

If there are multiple views with the same name (they would have different
identifiers) but if you try to stop one with that name the SDK would close one
of those randomly.

To stop a view with its view ID:

    
    
    Countly.sharedInstance().views().stopViewWithID("View ID");

You can provide a segmentation while doing so:

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    
    Countly.sharedInstance().views().stopViewWithID("View ID", segmentation);

You can also stop all running views at once with a segmentation:

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
      
    Countly.sharedInstance().views().stopAllViews(segmentation);

### Pausing and Resuming Views

If you are starting multiple views at the same time it might be necessary for
you to pause some views while others are still continuing. This can be
achieved by using the unique identifier you get while starting a view.

To pause a view with its ID:

    
    
    Countly.sharedInstance().views().pauseViewWithID("View ID");

To resume a view with its ID:

    
    
    Countly.sharedInstance().views().resumeViewWithID("View ID");

### Adding Segmentation to Started Views

You can add segmentation values to a view before it ends. This can be done as
many times as desired and the final segmentation that will be send to the
server would be the cumulative sum of all segmentations. However if a certain
segmentation value for a specific key has been updated, the latest value will
be used.

To add segmentation to a view using its view ID:

    
    
    String viewID = Countly.sharedInstance().views().startView("View Name");
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
      
    Countly.sharedInstance().views().addSegmentationToViewWithID(viewID, segmentation);

To add segmentation to a view using its name:

    
    
    String viewName = "View Name";
    Countly.sharedInstance().views().startView(viewName);
      
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
      
    Countly.sharedInstance().views().addSegmentationToViewWithName(viewName, segmentation);

## Global View Segmentation

You can set a global segmentation to be send with all views when it ends:

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    
    Countly.sharedInstance().views().setGlobalViewSegmentation(segmentation);  
    

You can update this segmentation any time you want:

    
    
    Map<String, Object> segmentation = new ConcurrentHashMap<>();
    segmentation.put("country", "Germany");
    segmentation.put("app_version", "1.0");
    segmentation.put("rating", 10);
    segmentation.put("precision", 324.54678d);
    segmentation.put("timestamp", 1234567890L);
    segmentation.put("clicked", false);
    segmentation.put("languages", new String[] { "en", "de", "fr" });
    segmentation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    segmentation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
      
    Countly.sharedInstance().views().updateGlobalViewSegmentation(segmentation);

To review the resulting data from view tracking, open the dashboard and go to
`Analytics > Views`. For more information on how to use view tracking data to
its fullest potential, click [here](http://resources.count.ly/docs/view-
analytics).

![001.png](/hc/article_attachments/9508351988121)

# Device ID Management

All tracked information is tied to a "device ID". A device ID is a unique
identifier for your users. When the SDK is initialized the first time and no
custom device ID is provided, a random one will be generated. For most use
cases that is enough as it provides a random identity to one of your apps
users.

One of the first things you'll need to decide is which device ID generation
strategy to use. There are several options defined below:

The easiest method is letting the Countly SDK seamlessly handle the device ID
on its own. You may then use the following calls. It will use the default
strategy, which currently is OpenUDID.

    
    
    CountlyConfig config = (new CountlyConfig(appC, COUNTLY_APP_KEY, COUNTLY_SERVER_URL));  
    Countly.sharedInstance().init(config);

You may specify the device ID by yourself if you have one (it has to be unique
for each device). It may be an email or some other internal ID used by your
other systems.

    
    
    CountlyConfig config = (new CountlyConfig(appC, COUNTLY_APP_KEY, COUNTLY_SERVER_URL));  
    config.setDeviceId("YOUR_DEVICE_ID");  
    Countly.sharedInstance().init(config);

## Changing Device ID

In case your application authenticates users, you might want to change the ID
to the one in your backend after he has logged in. This helps you identify a
specific user with a specific ID on a device he logs in, and the same scenario
can also be used in cases this user logs in using a different way (e.g another
tablet, another mobile phone, or web). In this case, any data stored in your
Countly server database associated with the current device ID will be
transferred (merged) into user profile with device id you specified in the
following method call:

**Performance risk.** Changing device id with server merging results in huge
load on server as it is rewriting all the user history. This should be done
only once per user.

    
    
    Countly.sharedInstance().deviceId().changeWithMerge("new device ID")

In other circumstances, you might want to track information about another
separate user that starts using your app (changing apps account), or your app
enters a state where you no longer can verify the identity of the current user
(user logs out). In that case, you can change the current device ID to a new
one without merging their data. You would call:

    
    
    Countly.sharedInstance().deviceId().changeWithoutMerge("new device ID")

Doing it this way, will not merge the previously acquired data with the new
id.

Do note that every time you change your deviceId without a merge, it will be
interpreted as a new user. Therefore implementing id management in a bad way
could inflate the users count by quite a lot.

The worst would be to not merge device id on login and generate a new random
ID on logout. This way, by repeatedly logging in and out one could generate an
infinite amount of users.

So the recommendation is (depending on your apps use case) either to keep the
same deviceId even if the user logs out or to have a predetermined deviceId
for when the users on the specific device logs out. The first method would not
inflate the user count, but not viable for single device, multiple users use
case. The second would create a "multi-user" id for every device and possibly
slightly inflate the user count.

## Temporary Device ID

In the previous ID management approaches, data is still sent to your server,
but it adds user inflation risk if badly managed. The use of a temporary ID
can help to mitigate such problems.

During app start or any time after init, you can enter a temporary device ID
mode. All requests will be stored internally and not sent to your server until
a new device ID is provided. In that case, all events created during this
temporary ID mode will be associated with the new device ID and sent to the
server.

To enable this mode during init, you would call this on your config object
before init:

    
    
    countlyConfig.enableTemporaryDeviceIdMode();

To enable temporary id after init, you would call:

    
    
    Countly.sharedInstance().deviceId().enableTemporaryIdMode();

To exit temporary id mode, you would call either "changeDeviceIdWithoutMerge"
or "changeDeviceIdWithMerge" or init the SDK with a developer supplied device
ID.

## Retrieving Current Device ID

You may want to see what device id Countly is assigning for the specific
device and what the source of that id is. For that, you may use the following
calls. The id type is an enum with the possible values of:
"DEVELOPER_SUPPLIED", "OPEN_UDID", "ADVERTISING_ID".

    
    
    String usedId = Countly.sharedInstance().deviceId().getID();
    Type idType = Countly.sharedInstance().deviceId().getType();

# Push Notifications

For Android 13 (API 33) and higher you have to declare push notification
permissions in you app's manifest file. For related documentation you can
check
[here](https://developer.android.com/develop/ui/views/notifications/notification-
permission#declare).

Also starting from Android 12 (API 31) notification trampoline is restricted.
For more information you can click
[here](https://developer.android.com/about/versions/12/behavior-
changes-12#notification-trampolines).

Countly supports FCM (Firebase Cloud Messaging) and Huawei Push Kit as push
notification service providers. The SDK doesn't have any direct dependencies
on FCM or HMS libraries and uses reflection instead, so **it's up to
application developers to ensure correct dependencies are present** (please
refer to our [Demo app build.gradle](https://github.com/Countly/countly-sdk-
android/blob/master/app/build.gradle) for reference).

By default Countly SDK uses FCM as push notification provider. If FCM is not
present in the system, Countly would try to get HMS token instead. It's
possible to alter this behaviour by supplying HMS as a preferred provider:

    
    
    CountlyConfigPush countlyConfigPush = new CountlyConfigPush(this).setProvider(Countly.CountlyMessagingProvider.HMS);
    CountlyPush.init(countlyConfigPush);

## Integration

To have the best experience with push notifications, the SDK should be
initialized in your Application subclass' "onCreate" method. Android O and
later models require the use of `NotificationChannel`s. Use
`CountlyPush.CHANNEL_ID` for Countly-displayed notifications:

    
    
    public class App extends Application {
    
      @Override
      public void onCreate() {
        super.onCreate();
    
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
    
          // Register the channel with the system; you can't change the importance
          // or other notification behaviors after this
          NotificationManager notificationManager = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
          if (notificationManager != null) {
            // Create the NotificationChannel
            NotificationChannel channel = new NotificationChannel(CountlyPush.CHANNEL_ID, getString(R.string.countly_hannel_name), NotificationManager.IMPORTANCE_DEFAULT);
            channel.setDescription(getString(R.string.countly_channel_description));
            notificationManager.createNotificationChannel(channel);
          }
        }
    
        CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL)
          .setLoggingEnabled(true);
        Countly.sharedInstance().init(config);
      
        CountlyConfigPush countlyConfigPush = new CountlyConfigPush(this);
        CountlyPush.init(countlyConfigPush);
        FirebaseInstanceId.getInstance().getInstanceId()
          .addOnCompleteListener(new OnCompleteListener<InstanceIdResult>() {
            @Override
            public void onComplete(@NonNull Task<InstanceIdResult> task) {
              if (!task.isSuccessful()) {
                Log.w(TAG, "getInstanceId failed", task.getException());
                return;
              }
      
              // Get new Instance ID token
              String token = task.getResult().getToken();
                CountlyPush.onTokenRefresh(token);
              }
          });
      }
    }

Please note that the second parameter in `CountlyConfigPush()` call defines
whether a particular device would be handled as a test setup or in production.
It's quite handy to separate test devices from production ones by changing
`CountlyMessagingMode`, so you could test your notifications before sending
them to all your users.

You should add this permission entry into your app manifest:  

    
    
    <uses-permission android:name="${applicationId}.CountlyPush.BROADCAST_PERMISSION" />

**Additional Intent Redirection checks**

Intent Redirection Vulnerability is an issue that lets your app allow
malicious apps to access private app components or files. Google removes apps
from Google Play that is susceptible to Intent Redirection Vulnerability. For
Push Notifications, we are also using Intent Redirection in our SDK, so for
that reason, we have also implemented additional Intent Redirection
protection.

You can set the additional intent redirection check to true for intent
redirect security.

    
    
    CountlyPush.useAdditionalIntentRedirectionChecks = true;

If these are enabled then the SDK will enforce additional security checks.
More info can be found
[here](https://support.google.com/faqs/answer/9267555?hl=en).

If, for some reason, the 'activity name' does not start with the 'application
package name' (for e.g if you are using Android Product/Build Flavors to
create multiple apps with the same code base), then you need to provide the
additional allowed class and package names for Intent Redirection manually.

You can set the allowed package and class names for Intent Redirection using
this call:

    
    
    List<String> allowedClassNames = new ArrayList<>();
    allowedClassNames.add("MainActivity");
    List<String> allowedPackageNames = new ArrayList<>();
    allowedPackageNames.add(getPackageName());
    
    CountlyConfigPush countlyConfigPush = new CountlyConfigPush(this)
      .setAllowedIntentClassNames(allowedClassNames)
      .setAllowedIntentPackageNames(allowedPackageNames);
    CountlyPush.init(countlyConfigPush);

Please follow provider-specific instructions for Firebase and / or Huawei Push
Kit below.

### Firebase

Before implementing FCM to your application you would need to get Push
Notification credentials from your Firebase Console and upload them to your
Countly server. (If you have not done that already you can follow this guide.)

#### Integrating FCM into Your App

Please review our [Demo app](https://github.com/Countly/countly-sdk-
android/tree/master/app) for a complete integration example.

Once you have followed the Google's guide for [Adding Firebase to your
project](https://firebase.google.com/docs/android/setup), setting up the
Countly FCM is quite easy.

**Adding dependencies**

Add the following dependency to your `build.gradle` (**use latest Firebase
version**):

    
    
    //latest firebase-messaging version that is available
    implementation 'com.google.firebase:firebase-messaging:23.1.2'

Now, we will need to add the `Service`. Add a service definition to your
`AndroidManifest.xml`:

    
    
    <service android:name=".DemoFirebaseMessagingService">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
    

... and add a class for it as well (for Flutter and React-Native project this
step is not needed as the SDK adds the service files implicitly):

    
    
    public class DemoFirebaseMessagingService extends FirebaseMessagingService {
      private static final String TAG = "DemoMessagingService";
    
      @Override
      public void onNewToken(@NotNull String token) {
        super.onNewToken(token);
    
        Log.d("DemoFirebaseService", "got new token: " + token);
        CountlyPush.onTokenRefresh(token);
      }
    
      @Override
      public void onMessageReceived(@NotNull RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);
    
        Log.d("DemoFirebaseService", "got new message: " + remoteMessage.getData());
    
        // decode message data and extract meaningful information from it: title, body, badge, etc.
        CountlyPush.Message message = CountlyPush.decodeMessage(remoteMessage.getData());
    
        if (message != null && message.has("typ")) {
          // custom handling only for messages with specific "typ" keys
          message.recordAction(getApplicationContext());
          return;
        }
    
        Intent notificationIntent = null;
        if (message.has("anotherActivity")) {
          notificationIntent = new Intent(getApplicationContext(), AnotherActivity.class);
        }
          
        Boolean result = CountlyPush.displayMessage(getApplicationContext(), message, R.drawable.ic_message, notificationIntent);
        if (result == null) {
          Log.i(TAG, "Message wasn't sent from Countly server, so it cannot be handled by Countly SDK");
        } else if (result) {
          Log.i(TAG, "Message was handled by Countly SDK");
        } else {
          Log.i(TAG, "Message wasn't handled by Countly SDK because API level is too low for Notification support or because currentActivity is null (not enough lifecycle method calls)");
        }
      }
    
      @Override
      public void onDeletedMessages() {
        super.onDeletedMessages();
      }
    }

This class is responsible for token changes and message handling logic.
Countly provides default UI for your notifications, which would display a
`Notification`, if your app is in the background, or `Dialog`, if your app is
active. It will also automatically report button clicks back to the server for
Actioned metric conversion tracking. However, it is completely up to you,
whether you would like to use this class or not. Let's have an overview of the
`onMessageReceived` method:

  1. It calls `CountlyPush.decodeMessage()` to decode a message from the Countly-specific format. In this way, you'll have a method of accessing standard fields, such as a badge, URL, or your custom data keys.
  2. Then it checks if the message has a `typ`custom data key, and if it does, it only records the Actioned metric. Let's assume your custom notification is to preload some data from a remote server. Our demo app has a more in-depth scenario for this case.
  3. In case the message also has `anotherActivity` custom data key, it creates a `notificationIntent` to launch the activity, named `AnotherActivity`. This intent is only used as default content intent for the user tap on a `Notification`. It is not used for`Dialog`.
  4. Then the service calls `CountlyPush.displayMessage()`to perform a standard Countly notification displaying logic - `Notification`, assuming your app is in the background or not running, and the `Dialog` is in the foreground. Note that this method takes an `int` resource parameter. It must be compatible with the corresponding version of the Android notification small icon.

Apart from that which is listed above, the SDK also exposes methods
`CountlyPush.displayNotification()` & `CountlyPush.displayDialog()` in case
you only need `Notification` and don't want `Dialog` or vice versa.

This is an example of a push notification payload sent from the Countly
server:

    
    
    {
      collapse_key: “collapse_key”, // if present
      time_to_live: 123,
      data: {
        message: “message string”, // if present
        title: “title string”, // if present
        sound: “sound string”, // if present
        badge: 123, // if present
        c.i: “message id string”,
        c.l: “http://message-wide-url”, // if present
        c.m: “http://rich.media.url.jpg”, // if present
        c.s: “true”, // if sound & message absent
        c.b: [ // if present
          {t: “Button 1 title”, l: “http://button.1.url”},
          {t: “Button 2 title”, l: “http://button.2.url”} // if present
        ],
        // any other data properties if present
      }
    }
    

### Huawei Push Kit

Before implementing HMS to your application you would need to get Push
Notification credentials for the Push Kit and upload them to your Countly
server. (If you have not done that already you can follow this guide.)

#### Integrating HMS into Your App

HMS implementation in Countly SDK looks very much like FCM: add dependencies,
add service definition and the service class. Please refer to our [Demo
app](https://github.com/Countly/countly-sdk-android/tree/master/app) for a
reference implementation. Assuming you've already integrated [HMS
Core](https://developer.huawei.com/consumer/en/doc/development/HMSCore-
Guides/android-integrating-sdk-0000001050040084) into your app, all you need
to do is add a dependency into build.gradle (**use latest dependency
version!**):

    
    
    implementation 'com.huawei.hms:push:4.0.3.301'  
    

... add service definition into AndroidManifest.xml:

    
    
    <service 
      android:name=".DemoHuaweiMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
      </intent-filter>
    </service>
    

... and the service itself:

    
    
    public class DemoHuaweiMessagingService extends HmsMessageService {
      private static final String TAG = "DemoHuaweiMessagingService";
    
      @Override
      public void onNewToken(String token) {
        super.onNewToken(token);
    
        CountlyPush.onTokenRefresh(token, Countly.CountlyMessagingProvider.HMS);
      }
    
      @SuppressLint("LongLogTag")
      @Override
      public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);
    
        Log.d(TAG, "got new message: " + remoteMessage.getDataOfMap());
    
        // decode message data and extract meaningful information from it: title, body, badge, etc.
        CountlyPush.Message message = CountlyPush.decodeMessage(remoteMessage.getDataOfMap());
        if (message == null) {
          Log.d(TAG, "Not a Countly message");
          return;
        }
    
        if (message.has("typ")) {
          // custom handling only for messages with specific "typ" keys
          if (message.data("typ").equals("download")) {
            message.recordAction(getApplicationContext());
            return;
          } else if (message.data("typ").equals("promo")) {
            return;
          }
        }
    
        Intent intent = null;
        if (message.has("another")) {
          intent = new Intent(getApplicationContext(), ActivityExampleOthers.class);
        }
        Boolean result = CountlyPush.displayMessage(getApplicationContext(), message, R.drawable.ic_message, intent);
        if (result == null) {
          Log.i(TAG, "Message doesn't have anything to display or wasn't sent from Countly server, so it cannot be handled by Countly SDK");
        } else if (result) {
          Log.i(TAG, "Message was handled by Countly SDK");
        } else {
          Log.i(TAG, "Message wasn't handled by Countly SDK because API level is too low for Notification support or because currentActivity is null (not enough lifecycle method calls)");
        }
      }
    }

... which is almost identical to the FCM demo service.

## Customizing Push Messages

### Custom Notification Sound

If you would like to use a custom sound in your push notifications, they must
be present on the device. They cannot be linked from the internet.

For you to use a custom notification sound, there are 2 things you will need
to do.

First, you will need to prepare the URI that will link to the resource on your
device. It would look something like this:

    
    
    String soundUri = ContentResolver.SCHEME_ANDROID_RESOURCE + "://"+ getApplicationContext().getPackageName() + "/" + R.raw.notif_sound;

You would then send this URI as part of the push notification, using the "Send
sound" field. This should cover devices with the Android SDK version less than
26.

For devices with the SDK version 26+, you will also need to provide this URI
during the notification channel setup. It would look something like this:

    
    
    AudioAttributes audioAttributes = new AudioAttributes.Builder()
      .setContentType(AudioAttributes.CONTENT_TYPE_SONIFICATION)
       .setUsage(AudioAttributes.USAGE_NOTIFICATION)
       .build();
    
    channel.setSound(soundUri, audioAttributes);

More info about that here:
<https://stackoverflow.com/questions/48986856/android-notification-setsound-
is-not-working>

### Automatic Message Handling

Countly handles most common message handling tasks for you. For example, it
generates and shows `Notification` or `Dialog` and tracks conversion rates
automatically. In most cases, it’s not necessary for you to know how it works,
but if you would like to customize the behavior or exchange it with your own
implementation, here is a more in-depth explanation of what it does.

First, the received notification payload is analyzed and, if it's a Countly
notification (if it has a `"c"` dictionary in the payload), it processes it.
Otherwise, or if the notification analysis says it is a `Data-only`
notification (you're the one responsible for message processing), it does
nothing.

Next, it automatically makes callbacks to the Countly Messaging server to
calculate the number of open push notifications which got open and the number
of notifications with positive reactions.

Here are the explanations of common usage scenarios that are handled
automatically:

  * It doesn't do anything, apart from conversion tracking if you specify it as a `Data-only` notification in the dashboard. This effectively sets a special flag in the message payload, so you may process it on your own. 
  * It displays a `Notification` whenever a message arrives, and your application is in the background. 
  * It displays `Dialog` when a new message arrives, and your application is in the foreground. 
  * It displays `Dialog` when a new message with an action arrives (open URL), and the user responds to it by swiping or tapping the notification.

A `Dialog` always has a message, but the set of displayed buttons depends on
the message type:

  * It displays a single ‘Cancel’ button for notifications without any actions (only a text message).
  * For notifications with a **URL** (for instance, you ask the user to open a link to some blog post), it displays both the ‘Cancel’ & ‘Open’ buttons.
  * It displays the corresponding buttons for notifications with custom buttons.

## Deep Links

When using Countly push notifications, you may benefit from Android deep links
in your application for the buttons you provide. Those are basically links for
specific activities of your application. A link may either be a generic ‘http’
link, such as `http://www.oneexample.com/survey`, or a link with a custom URI
(uniform resource indicator) scheme, such as `otherexample://things`.

In order for Android deep links to work, you will need to specify the intent
filters in your application's manifest for the specific groups of links you
would like to use.

A deeper guide on how to configure your application to use deep links may be
found [here](https://developer.android.com/training/app-links/deep-
linking.html).

## Handling Push Callbacks

When receiving a push notification, the user may click the notification
directly or they may click the button. When a user clicks anywhere on the push
notification, an intent is launched to open the provided link. This may be a
web page URL or a deep link. If you have configured your app, so that opening
this intent will open an activity of your app, it should be possible to track
which button was pressed.

There is also the option to add additional metadata to those intents. The
included meta information contains data, such as which button was pressed,
which link was given in the notification, the title, and the message of the
notification.

This functionality is disabled by default, and the additional metadata might
be added as extras to the intent.

In order to enable this functionality, you will need to call the following
function before initializing Countly messaging:

    
    
    countlyConfig.setPushIntentAddMetadata(true);

To access those extras from the intent, you should use these names:

    
    
    ProxyActivity.intentExtraButtonLink
    ProxyActivity.intentExtraMessageText
    ProxyActivity.intentExtraMessageTitle
    ProxyActivity.intentExtraWhichButton

To read the extra from the intent, you would use something similar to this:

    
    
    String buttonUrl = intent.getStringExtra(ProxyActivity.intentExtraButtonLink);

You've probably noticed that we used `Countly.CountlyMessagingMode.TEST` in
our example. That is because we are currently building the application only
for testing purposes. Countly separates users who run apps built for test and
for release. This way you'll be able to test messages before sending them to
all your users. When releasing your app, please use
`Countly.CountlyMessagingMode.PRODUCTION`.

## Setting up Credentials

To use Push Notifications in your application you would need to acquire
credentials from the PN service of your choice (Firebase or Huawei) and then
upload these credentials to your Countly server.

### Acquiring Credentials

#### Firebase

In order to be able to send notifications through FCM, Countly server needs a
FCM server key. In order to get one, open Project settings in [Firebase
console](https://console.firebase.google.com):

![](https://count.ly/images/guide/57c5e32-Screenshot_2018-04-21_17.20.16.png)

Select Cloud Messaging tab

![](https://count.ly/images/guide/fb244d1-Screenshot-2018-04-21-17.20.41-x.png)

#### Huawei

Assuming you have followed Huawei's guide of [setting up an
application](https://developer.huawei.com/consumer/en/doc/distribution/app/agc-
help-createapp-0000001146718717), next step would be to [enable
PushKit](https://developer.huawei.com/consumer/en/doc/distribution/app/agc-
enable_service#enable-service). Then [enable Receipt
status](https://developer.huawei.com/consumer/en/doc/development/HMS-
Guides/push-receipt):

  * enter `https://YOUR_COUNTLY_SERVER/i/pushes/huawei` into the callback address field, while replacing YOUR_COUNTLY_SERVER with actual server address;
  * and enter your certificate in PEM format (only your certificate, without the rest of the chain; usually first one in `openssl s_client -connect YOUR_COUNTLY_SERVER:443 -showcerts`).

![Screenshot_2020-08-25_at_15.52.49.png](/hc/article_attachments/900003139063)

Then you'd need to get your App ID & App secret from AppGallery Connect -> My
Apps:

![Screenshot_2020-08-25_at_15.49.12.png](/hc/article_attachments/900003139103)

### Setting up the Dashboard

#### Firebase

Copy & paste the FCM keys you get from your Firebase console into Management >
Applications > Push Notifications > Google FCM credentials upload form in your
Countly server and press “Save changes”:

![002.png](/hc/article_attachments/28254475243801)

#### Huawei

Copy your App ID & the secret you got from your Huawei app gallery and paste
it into Management > Applications > Push Notifications > Huawei Push Kit
upload form in your Countly server and press “Save changes”:

![003.png](/hc/article_attachments/28254475261721)

# User Location

While integrating this SDK into your application, you might want to track your
user location. You could use this information to better know your app’s user
base or to send them tailored push notifications based on their coordinates.
There are 4 fields that may be provided:

  * Country code in the two-letter, ISO standard
  * City name (must be set together with the country code)
  * Latitude and longitude values separated by a comma, e.g. "56.42345,123.45325"
  * Your user’s IP address

## Setting Location

During init you can set location info that will be sent during the start of
the user session:

    
    
    config.setLocation(countryCode, city, gpsCoordinates, ipAddress);

Note that the ipAddress will only be updated if set through the init process.

    
    
    //set user location
    String countryCode = "us";
    String city = "Houston";
    String latitude = "29.634933";
    String longitude = "-95.220255";
    String ipAddress = null;
    
    Countly.sharedInstance().setLocation(countryCode, city, latitude + "," + longitude, ipAddress);

When those values are set, a separate request will be created to send them
sent. Except for ip address, because Countly Server processes IP address only
when starting a session.

If you don't want to set specific fields, set them to null.

## Disabling Location

Also during init, you can disable location:

    
    
    config.setDisableLocation();

Users might want to opt-out of location tracking. To do so, call:

    
    
    //disable location
    Countly.sharedInstance().disableLocation();

This action will erase the cached location data from the device and the
server.

# Remote Config

Remote config allows you to modify how your app functions or looks by
requesting key-value pairs from your Countly server. The returned values may
be modified based on the user properties. For more details, please see the
[Remote Config documentation](https://support.count.ly/hc/en-
us/articles/9895605514009-Remote-Config).

Once downloaded, Remote config values will be saved persistently and available
on your device between app restarts unless they are erased.

The two ways of acquiring remote config data are enabling automatic download
triggers or manual requests.

If a full download of remote config values is performed, the previous list of
values is replaced with the new one. If a partial download is performed, only
the retrieved keys are updated, and values that are not part of that download
stay as they were. A previously valid key may return no value after a full
download.

## Downloading Values

### Automatic Remote Config Triggers

Automatic remote config triggers have been turned off by default; therefore,
no remote config values will be requested without developer intervention.

The automatic download triggers that would trigger a full value download are:

  * when the SDK has finished initializing
  * after the device ID is changed without merging
  * when user gets out of temp ID mode
  * when 'remote-config' consent is given after it had been removed before (if consents are enabled)

To enable the automatic triggers, you have to call
`enableRemoteConfigAutomaticTriggers` on the configuration object you will
provide during init.

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.enableRemoteConfigAutomaticTriggers(); // necessary to enable the feature
    Countly.sharedInstance().init(config);
    

Another thing you can do is to enable value caching with the
`enableRemoteConfigValueCaching` flag. If all values were not updated, you
would have metadata indicating if a value belongs to the old or current user.

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.enableRemoteConfigValueCaching();
    Countly.sharedInstance().init(config);

### Manual Calls

There are three ways to trigger remote config value download manually:

  * Manually downloading all keys
  * Manually downloading specific keys
  * Manually downloading, omitting (everything except) keys.

Each of these calls also has an optional parameter that you can provide a
RCDownloadCallback to, which would be triggered when the download attempt has
finished.

`dowloadAllKeys` is the same as the automatically triggered update - it
replaces all stored values with the ones from the server (all locally stored
values are deleted and replaced with new ones).

Or you might only want to update specific key values. To do so, you will need
to call `downloadSpecificKeys` to downloads new values for the wanted keys.
Those are provided with a String array.

Or you might want to update all the values except a few defined keys. To do
so, call `downloadOmittingKeys` would update all values except the provided
keys. The keys are provided with a String array.

All Keys Certain Keys Omit Keys

    
    
    Countly.sharedInstance().remoteConfig().downloadAllKeys(new RCDownloadCallback() {
      @Override
      public void callback(RequestResult rResult, String error, boolean fullValueUpdate, Map<String, RCData> downloadedValues) {
        if (rResult == RequestResult.Success) {
          // do sth
        } else {
          // do sth
        }
      }
    });
    
    
    Countly.sharedInstance().remoteConfig().downloadSpecificKeys(String[] keysToInclude, new RCDownloadCallback() {
      @Override
      public void callback(RequestResult rResult, String error, boolean fullValueUpdate, Map<String, RCData> downloadedValues) {
        if (rResult == RequestResult.Success) {
          // do sth
        } else {
          // do sth
        }
      }
    });
    
    
    Countly.sharedInstance().remoteConfig().downloadOmittingKeys(String[] keysToOmit, new RCDownloadCallback() {
      @Override
      public void callback(RequestResult rResult, String error, boolean fullValueUpdate, Map<String, RCData> downloadedValues) {
        if (rResult == RequestResult.Success) {
          // do sth
        } else {
          // do sth
        }
      }
    });

When making requests with an "inclusion" or "exclusion" array, if those arrays
are empty or null, they will function the same as a `dowloadAllKeys` request
and will update all the values. This means it will also erase all keys not
returned by the server.

## Accessing Values

To get a stored value, call `getValue` with the specified key. This returns an
RCData object that contains the value of the key and the metadata about that
value's owner. If value in RCData was `null` then no value was found or the
value was `null`.

    
    
    Object value_1 = Countly.sharedInstance().remoteConfig().getValue("key_1").value;
    Object value_2 = Countly.sharedInstance().remoteConfig().getValue("key_2").value;
    Object value_3 = Countly.sharedInstance().remoteConfig().getValue("key_3").value;
    Object value_4 = Countly.sharedInstance().remoteConfig().getValue("key_4").value;
    
    int int_value = (int) value_1;
    double double_value = (double) value_2;
    JSONArray jArray = (JSONArray) value_3;
    JSONObject jobj = (JSONObject) value_4;

If you want to get all values together you can use `getAllValues` which
returns a Map<String, RCData>. The SDK does not know the returned value type,
so, it will return the `Object`. The developer then needs to cast it to the
appropriate type. The returned values may also be `JSONArray`, `JSONObject`,
or just a simple value, such as `int`.

    
    
    Map<String, RCData> allValues = Countly.sharedInstance().remoteConfig().getAllValues();  
    
    int int_value = (int) allValues["key_1"].value ;
    double double_value = (double) allValues["key_2"].value;
    JSONArray jArray = (JSONArray) allValues["key_3"].value;
    JSONObject jobj = (JSONObject) allValues["key_4"].value;

RCData object has two keys: value (Object) and isCurrentUsersData (Boolean).
Value holds the data sent from the server for the key that the RCData object
belongs to. The isCurrentUsersData is only false when there was a device ID
change, but somehow (or intentionally) a remote config value was not updated.

    
    
    Class RCData {
      Object value;
      Boolean isCurrentUsersData;
    }

## Clearing Stored Values

At some point, you might like to erase all the values downloaded from the
server. You will need to call one function to do so.

    
    
    Countly.sharedInstance().remoteConfig().clearAll();

## Global Download Callbacks

Also, you may provide a global callback function to be informed when the
remote config download request is finished with
`remoteConfigRegisterGlobalCallback` during the SDK initialization:

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.remoteConfigRegisterGlobalCallback(RCDownloadCallback callback);
    Countly.sharedInstance().init(config);
    

RCDownloadCallback is called when the remote config download request is
finished, and it would have the following parameters:

  * `rResult`: RequestResult Enum (either Error, Success or NetworkIssue)
  * `error`: String (error message. "null" if there is no error)
  * `fullValueUpdate`: boolean ("true" - all values updated, "false" - a subset of values updated)
  * `downloadedValues`: Map<String, RCData> (the whole downloaded remote config values)

    
    
    RCDownloadCallback {
      void callback(RequestResult rResult, String error, boolean fullValueUpdate, Map<String, RCData> downloadedValues)
    }
    

`downloadedValues` would be the downloaded remote config data where the keys
are remote config keys, and their value is stored in RCData class with
metadata showing to which user data belongs. The data owner will always be the
current user.

You can also register (or remove) callbacks to do different things after the
SDK initialization. You can register these callbacks multiple times:

    
    
    // register a callback
    Countly.sharedInstance().remoteConfig().registerDownloadCallback(RCDownloadCallback callback);
    
    // remove a callback
    Countly.sharedInstance().remoteConfig().removeDownloadCallback(RCDownloadCallback callback);

## A/B Testing

Your users' participation in A/B tests can be coupled with or decoupled from
the Remote Config feature in multiple ways. Possible ways to enroll or remove
your users for A/B tests are listed below.

### Enrollment on Download

You can enroll to available experiments when downloading the Remote Config
values automatically. To do this you should call `enrollABOnRCDownload` method
on the CountlyConfig object you pass for the initialization:

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.enrollABOnRCDownload ();
    Countly.sharedInstance().init(config);

### Enrollment on Access

You can enroll to A/B tests while getting RC values from storage. You can use
`getValueAndEnroll` while getting a single value and `getAllValuesAndEnroll`
while getting all values to enroll to the keys that exist. If no value was
stored for those keys these functions would not enroll the user. Both of these
functions works the same way with their non-enrolling variants mentioned
above, namely; `getValue` and `getValues`.

### Enrollment on Action

To enroll a user into the A/B tests for the given keys you use the following
method:

    
    
    Countly.sharedInstance().remoteConfig().enrollIntoABTestsForKeys(String[] keys);

Here the keys array is the mandatory parameter for this method to work.

### Exiting A/B Tests

If you want to remove users from A/B tests of certain keys you can use the
following function:

    
    
    Countly.sharedInstance().remoteConfig().exitABTestsForKeys(String[] keys);

Here if no keys are provided it would remove the user from all A/B tests
instead.

# User Feedback

There are several ways to receive user feedback: the Star Rating Dialog and
the Feedback Widgets (Survey, NPS, Rating).

Star Rating Dialog allows users to give feedback by rating it from 1 to 5.
Feedback Widgets (Survey, NPS, Rating) allow for even more textual feedback
from users.

## Star Rating Dialog

Star-rating integration provides a dialog for receiving users’ feedback about
the application. It contains a title, a simple message explaining its uses, a
1-to-5-star meter for receiving users’ ratings, and a dismiss button in case
the user does not want to give a rating.

This star rating has nothing to do with the Google Play Store ratings and
reviews. It is just for getting brief feedback from users to be displayed on
the Countly dashboard. If the user dismisses the star-rating dialog without
providing a rating, the event will not be recorded.

The star-rating dialog's title, message, and dismiss button text may be
customized through the countly configuration.

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.setStarRatingSessionLimit(LIMIT);
    config.setStarRatingCallback(new StarRatingCallback() {
        @Override public void onRate(int rating) {
            Log.i(Countly.TAG, "Rating: " + rating);
        }
    
        @Override public void onDismiss() {
            Log.i(Countly.TAG, "Rating dialog was dismissed");
        }
    });
    config.setStarRatingTextTitle("Custom title");
    config.setStarRatingTextMessage("Custom message");
    config.setStarRatingTextDismiss("Custom dismiss button text");
    
    Countly.sharedInstance().init(config);
    

The star-rating dialog can be displayed in 2 ways:

  * Manually by the developer
  * Automatically, depending on the session count

In order to display the star-rating dialog manually, you must call the
`ShowStarRating` function. Optionally, you may provide the callback functions.
There is no limit on how many times the star-rating dialog may be displayed
manually.

    
    
    //show the star rating without a callback
    Countly.sharedInstance().ratings().showStarRating(activity, null);
    
    //show the star rating with a callback
    Countly.sharedInstance().ratings().showStarRating(activity, callback)

The star-rating dialog will be displayed automatically when an application's
session count reaches the specified limit, i.e. once for each new version of
the application. This session count limit may be specified upon initial
configuration or through the `SetAutomaticStarRatingSessionLimit` function.
The default limit is 5. Once the star-rating dialog has been displayed
automatically, it will not be displayed again, unless a new app version comes
along.

You will need to pass the activity context during init to show the automatic
star-rating dialog.

    
    
    //set the rating limit through the configuration
    int starRatingLimit = 5;
    config.setStarRatingSessionLimit(starRatingLimit);

If you would like to enable the automatic star-rating function, use the
`SetIfStarRatingShownAutomatically` function, it is disabled by default.

    
    
    //enable automatic star rating
    config.setIfStarRatingShownAutomatically(true);
    
    //disable automatic star rating
    config.setIfStarRatingShownAutomatically(false);

If you would like to have the star rating shown only once per app's lifetime
and not for each new version, use the
`SetStarRatingDisableAskingForEachAppVersion` function.

    
    
    //disable star rating for each new version
    config.setStarRatingDisableAskingForEachAppVersion(true);
    
    //enable star rating for each new version
    config.setStarRatingDisableAskingForEachAppVersion(false);

The star-rating callback provides functions for two events. `OnRate` is called
when the user chooses a rating. `OnDismiss` is called when the user clicks the
back button, clicks outside the dialog, or clicks the "Dismiss" button. The
callback provided in the init function is only used when displaying the
automatic star rating. Only the provided callback will be used for the manual
star rating.

    
    
    StarRatingCallback callback = new StarRatingCallback() {
      @Override
      public void onRate(int rating) {
        //the user rated the app
      }
    
      @Override
      public void onDismiss() {
        //the star rating dialog was dismissed
      }
    };

## Feedback Widget

Feedback Widgets is an [Countly Enterprise](https://countly.com/enterprise)
plugin.

It is possible to display 3 kinds of feedback widgets:
[nps](https://support.count.ly/hc/en-us/articles/4652903481753-Feedback-
Surveys-NPS-and-Ratings-#h_01HAY62C2QB9K7CRDJ90DSDM0D),
[survey](https://support.count.ly/hc/en-us/articles/4652903481753-Feedback-
Surveys-NPS-and-Ratings-#h_01HAY62C2Q965ZDAK31TJ6QDRY) and
[rating](https://support.count.ly/hc/en-us/articles/4652903481753-Feedback-
Surveys-NPS-and-Ratings-#h_01HAY62C2R4S05V7WJC5DEVM0N). All widgets are shown
as webviews and should be approached using the same methods.

Before any feedback widget can be shown, you need to create them in your
countly dashboard.

After you have created widgets at your dashboard you can reach their related
information as a list, corresponding to the current user's device ID, by
providing a callback to the getAvailableFeedbackWidgets method, which returns
the list as the first parameter and error as the second:

    
    
    Countly.sharedInstance().feedback().getAvailableFeedbackWidgets(new RetrieveFeedbackWidgets() {
      @Override 
      public void onFinished(List retrievedWidgets, String error) {
        // error handling here
    
        // do something with the returned list here like pick a widget and then show that widget etc...
    
      }
    });

The objects in the returned list would look like this:

    
    
    class CountlyFeedbackWidget {
      public String widgetId;
      public FeedbackWidgetType type;
      public String name;
      public String[] tags; 
    }

Here all the values are same with the values that can be seen at your Countly
server like the widget ID, widget type, widget name and the tags you have
passed while creating the widget. Tags can contain information that you would
like to have in order to keep track of the widget you have created. Its usage
is totally left to the developer.

Potential 'type' values are:

    
    
    FeedbackWidgetType {survey, nps, rating}

After you have decided which widget you want to display, you would provide
that object to the following function as the first parameter. Second parameter
is app context, third is the close button text (if null no close button would
be shown) and third is a callback incase an error happens:

    
    
    Countly.sharedInstance().feedback().presentFeedbackWidget(chosenWidget, context, "Close", new FeedbackCallback() {
      // maybe show a toast when the widget is closed
      @Override 
      public void onFinished(String error) {
        // error handling here
      }
    });
    

### Manual Reporting

There might be some cases where you might want to use the native UI or a
custom UI you have created instead of our webview solution. At those times you
would want to request all the information related to that widget and then
report the result manually.

For a sample integration, have a look at our [sample
app](https://github.com/Countly/countly-sdk-
android/blob/master/app/src/main/java/ly/count/android/demo/ActivityExampleFeedback.java#L232)
at our github repo.

Initial steps for manually reporing your widget results are same with the
steps you take to display a rating widget. First you would need to retrieve
the available widget list with the previously mentioned
`getAvailableFeedbackWidgets` method. After that you would have a list of
possible `CountlyFeedbackWidget` objects. You would pick the widget you want
to display and pass that widget object to the function below as the first
parameter. Secong paramater is a callback that would return the widget data as
first parameter and the error as second:

    
    
    Countly.sharedInstance().feedback().getFeedbackWidgetData(chosenWidget, new RetrieveFeedbackWidgetData() {
      @Override 
      public void onFinished(JSONObject retrievedWidgetData, String error) {
    
      }
    }

Here the retrievedWidgetData would yield to a JSON Object with all of the
information you would need to present the widget by yourself.

For how this retrievedWidgetData would look like and in depth information on
this topic please check our detailed article
[here](https://support.count.ly/hc/en-us/articles/9290669873305-A-deeper-look-
at-SDK-concepts#h_01HABT18WT0D08H8DR2BAD77T2).

After you have collected the required information from your users with the
help of the `retrievedWidgetData` you have recieved, you would then package
the responses into a Map<String, Object>, and then pass it (reportedResult)
together with the widget object you picked from the retrieved widget list
(widgetToReport) and the `retrievedWidgetData` to report the feedback result
with the following call:

    
    
    //this contains the reported results
    Map<String, Object> reportedResult = new HashMap<>();
    
    //
    // You would fill out the results here. That step is not displayed in this sample check the detailed documentation linked above
    //
    
    //report the results to the SDK
    Countly.sharedInstance().feedback().reportFeedbackWidgetManually(widgetToReport, retrievedWidgetData, reportedResult);

If the user has closed the widget, you would report that by passing a "null"
as the reported result.

## Consent

If consents are enabled, to use Feedback Widgets, you have to provide the
'feedback' and to use Star Rating Dialog you have to provide the 'starRating'
consent for these features to work.

# User Profiles

User Profiles is a [Countly Enterprise](https://countly.com/enterprise) plugin
and built-in [Flex](https://countly.com/flex).

User Profiles is a tool for identifying users, their devices, event timelines,
and application crash information. It may contain any information you collect
or that is collected automatically by the Countly SDK.

You may send user-related information to Countly and let the Countly Dashboard
show and segment this data. You may also send a notification to a group of
users. For more information about User Profiles, review [this
documentation](https://support.count.ly/hc/en-us/articles/4403281285913-User-
Profiles)

## Setting User Properties

In the SDK, the typical workflow involves using the following methods to
provide information about the current user:

    
    
    // Provide multiple properties at once within a map
    Countly.sharedInstance().userProfile().setProperties(Map<String, Object> userProperties);
    
    // Provide single user property as key and value
    Countly.sharedInstance().userProfile().setProperties(String key, Object value);

These methods allow you to set predefined fields or any custom fields you wish
to include. While saving User Profile data by calling
`Countly.sharedInstance().userProfile().save()` is not mandatory; if required,
manually saving User Profile data by that call can still be applied. Recorded
User Profile data is automatically sent when:

  * An event is recorded
  * A session update occurs
  * The device ID changes

The keys for predefined user data fields are as follows:

Key | Type | Description  
---|---|---  
name | String | User's full name  
username | String | User's nickname  
email | String | User's email address  
organization | String | User's organization name  
phone | String | User's phone number  
picture | String | URL to avatar or profile picture of the user  
picturePath | String | Local path to the user's avatar or profile picture  
gender | String | User's gender as M for male and F for female  
byear | int | User's year of birth as integer  
  
Using "" for strings or a negative number for 'byear' will effectively delete
that property.

When providing properties, the following primitive data types are supported:
"String," "Integer," "Double," and "Boolean." Additionally, arrays, Lists, and
JSONArrays composed of these primitive types are also supported. Please note
that no other data types will be recorded.

    
    
    // Update the user profile with multiple values
    Map<String, Object> userInformation = new HashMap<>();
    userInformation.put("byear", 2024);
    userInformation.put("name", "Beduk");
    userInformation.put("level", 56);
    userInformation.put("languages", new String[] { "en", "de", "fr" });
    userInformation.put("sub_names", Arrays.asList("John", "Doe", "Jane"));
    userInformation.put("tags", new JSONArray(Arrays.asList("tag1", "tag2", "tag3")));
    // Set user information
    // ...
    
    Countly.sharedInstance().userProfile().setProperties(userInformation);
    Countly.sharedInstance().userProfile().save();

**You may use any key values to be stored and displayed on your Countly
backend for custom user properties. Note: keys with . or $ symbols will have
those symbols removed.**

## Modifying Data

Additionally, you may perform different manipulations on your custom data
values, such as incrementing the current value on a server or storing an array
of values under the same property.

You will find the list of available methods below:

    
    
    //set one custom properties
    Countly.sharedInstance().userProfile().setProperty("test", "test");
    //increment used value by 1
    Countly.sharedInstance().userProfile().increment("used");
    //increment used value by provided value
    Countly.sharedInstance().userProfile().incrementBy("used", 2);
    //multiply value by provided value
    Countly.sharedInstance().userProfile().multiply("used", 3);
    //save maximal value
    Countly.sharedInstance().userProfile().saveMax("highscore", 300);
    //save minimal value
    Countly.sharedInstance().userProfile().saveMin("best_time",60);
    //set value if it does not exist
    Countly.sharedInstance().userProfile().setOnce("tag", "test");
    //insert value to array of unique values
    Countly.sharedInstance().userProfile().pushUnique("type", "morning");
    //insert value to array which can have duplicates
    Countly.sharedInstance().userProfile().push("type", "morning");
    //remove value from array
    Countly.sharedInstance().userProfile().pull("type", "morning");
    
    //send provided values to server
    Countly.sharedInstance().userProfile().save();

## Orientation Tracking

Tracking of orientation changes is enabled by default. To stop recording your
application's orientation changes, you need to disable it on your init object
like:

    
    
    config.setTrackOrientationChanges(false);

You need to add this to all of your activities where you want to track
orientation:

    
    
    android:configChanges="orientation|screenSize"

Inside of your manifest, it would look something like this:

    
    
    <activity
      android:name=".ActivityExample"
      android:label="@string/activity_name"
      android:configChanges="orientation|screenSize">
    </activity>

To finish your setup for orientation tracking, you need to provide an
application class to the config object via "setApplication." This will
automatically catch orientation changes for all activities connected to the
given application class.

Otherwise, you must set up the Android callback to "onConfigurationChanged."
In those, you would have to call
"Countly.sharedInstance().onConfigurationChanged(newConfig)". You may set it
up similarly to this:

    
    
    @Override
    public void onConfigurationChanged (Configuration newConfig){
      super.onConfigurationChanged(newConfig);
      Countly.sharedInstance().onConfigurationChanged(newConfig);
    }
    

# Application Performance Monitoring

This SDK provides a few mechanisms for APM. To browse some of the provided
functionality, check the returned interface from here:

    
    
    Countly.sharedInstance().apm()

While using APM calls, you have the ability to provide trace keys by which you
can track those parameters in your dashboard. Those keys have to abide by the
following regex:

    
    
    /^[a-zA-Z][a-zA-Z0-9_]*$/

In short, only Latin letters, numbers, and underscores can be used. The key
can not start with an underscore or number. The key also has to be shorter
than 32 characters.

## Custom Traces

Currently, you can use custom traces to record the duration of application
processes. At the end of them, you can also provide any additionally gathered
data.

The trace key uniquely identifies the thing you are tracking and the same name
will be shown in the dashboard. The SDK does not support tracking multiple
events with the same key.

To start a custom trace, use:

    
    
    Countly.sharedInstance().apm().startTrace(String traceKey);

To end a custom trace, use:

    
    
    Map<String, Integer> customMetric = new HashMap();
    customMetric.put("ABC", 1233);
    customMetric.put("C44C", 1337);
    
    Countly.sharedInstance().apm().endTrace(String traceKey, customMetric);

The provided Map of integer values that will be added to that trace in the
dashboard.

## Network Traces

You can use the APM to track your requests.

Call this just before making your network request:

    
    
    Countly.sharedInstance().apm().startNetworkRequest(String networkTraceKey, String uniqueId);

`NetworkTraceKey` would be a unique identifier of the API endpoint you are
targeting. `UniqueId` is an identifier for requests for a specific traceKey.
In case you have overlapping network requests, you would have a unique id for
each of the requests. `NetworkTraceKey` and `UniqueId` are used as a pair to
uniquely identify the request you are making.

Call this after your network request is done:

    
    
    Countly.sharedInstance().apm().endNetworkRequest(String networkTraceKey, String uniqueId, int responseCode, int requestPayloadSize, int responsePayloadSize);

You would provide the same `NetworkTraceKey` and `UniqueId` as starting the
request and then also provided the received response code, sent payload size
in bytes, and received payload size in bytes.

## Automatic Device Traces

Currently, the Android SDK provides 3 automatic traces:

  * App start time
  * App time in the background
  * App time in foreground

To record app start time you need to implement 3 things.

First, you must enable this feature in config on init:

    
    
    config.apm.enableAppStartTimeTracking()

Second, you must call `Countly.applicationOnCreate();` right after your
application classes `onCreate` like:

    
    
    public class App extends Application {
      @Override
      public void onCreate() {
        super.onCreate();
        Countly.applicationOnCreate();
        ...
      }
    }

Third, you must initialize countly in your apps Application onStart callback.

If you do this, you will get the correct on start times.

## App Time in Background / Foreground

Countly will record the time your users spend in the foreground and
background. For this to work, your users need to be given any consent and
enable foreground/background tracking. You also need to provide your
Application class to your config object with "setApplication" during init.
Enable this feature on init:

    
    
    config.apm.enableForegroundBackgroundTracking()

# User Consent

In an effort to comply with GDPR Countly provides ways to toggle different
Countly features on/off depending on the given consent.

More information about GDPR can be found
[here](https://medium.com/countly/countly-the-gdpr-how-worlds-leading-mobile-
and-web-analytics-platform-can-help-organizations-5015042fab27).

## Setup During Init

The requirement for consent is disabled by default. To enable it, you will
have to call `setRequiresConsent` with `true` before initializing Countly.

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);  
    config.setRequiresConsent(true);  
    Countly.sharedInstance().init(config);

By default, no consent is given. That means that if no consent is enabled,
Countly will not work and no network requests related to its features will be
sent. When the consent status of a feature is changed, that change will be
sent to the Countly server.

For all features, except `push`, consent is not persistent and will have to be
set each time before Countly init. Therefore, the storage and persistence of
the given consent falls on the SDK integrator.

Consent for features may be given and revoked at any time, but if it is given
after Countly init, some features may only work in part.

If consent is removed, but the appropriate function can't be called before the
app closes, it should be done upon the next app start, so that any relevant
server-side features may be disabled (such as the reverse geo IP for
location).

Feature names in the Android SDK are stored as static fields in the class
called `CountlyFeatureNames`.

The current features are:

* `sessions` \- tracking when, how often and how long users use your app.

*`events` \- allow sending events to the server.

* `views` \- allow the tracking of which views user visits.

*`location` \- allow the sending of location information.

* `crashes` \- allow the tracking of crashes, exceptions, and errors.

*`attribution` \- allow tracking of which campaign did the user come from.

* `users` \- allow the collecting/providing of user information, including custom properties.

*`push` \- allow push notifications.

* `starRating` \- allow their rating and feedback to be sent.

*`apm` \- allow usage of APM features and collection of APM related. data

* `feedback` \- allow to show the survey and nps feedback widgets.

* `remoteConfig` \- allow to download remote config values from your server.

## Changing Consent

There are 3 ways of changing feature consent:

  * `giveConsent`/`removeConsent` \- gives or removes consent to a specific feature.

    
    
    // give consent to "sessions" feature
    Countly.sharedInstance().giveConsent(new String[]{Countly.CountlyFeatureNames.sessions});
    
    // remove consent from "sessions" feature
    Countly.sharedInstance().removeConsent(new String[]{Countly.CountlyFeatureNames.sessions});

  * `setConsent` \- set consent to a specific (true/false) value

    
    
    // give consent to "sessions" feature
    Countly.sharedInstance().setConsent(new String[]{Countly.CountlyFeatureNames.sessions}, true);
    
    // remove consent from "sessions" feature
    Countly.sharedInstance().setConsent(new String[]{Countly.CountlyFeatureNames.sessions}, false);

  * `setConsentFeatureGroup` \- set consent for a feature group to a specific (true/false) value

    
    
    // prepare features that should be added to the group
    String[] groupFeatures = new String[]{ Countly.CountlyFeatureNames.sessions, Countly.CountlyFeatureNames.location };
    
    String groupName = "featureGroup1";
    
    // give consent to "sessions" and "location" feature with a single consent group call
    Countly.sharedInstance().setConsentFeatureGroup(groupName, true);
    
    // remove consent from "sessions" and "location" feature with a single consent group call
    Countly.sharedInstance().setConsentFeatureGroup(groupName, false);

## Feature Groups

Features may be put into groups. By doing this, you may give/remove consent to
multiple features in the same call. They may be created using
`createFeatureGroup`. Those groups are not persistent and must be created on
every restart.

    
    
    // prepare features that should be added to the group
    String[] groupFeatures = new String[]{ Countly.CountlyFeatureNames.sessions, Countly.CountlyFeatureNames.location };
    
    // create the feature group
    Countly.sharedInstance().createFeatureGroup("groupName", groupFeatures);

# Security and Privacy

## Parameter Tamper Protection

You may set the optional `salt` to be used for calculating the checksum of
requested data which will be sent with each request, using the `&checksum`
field. You will need to set exactly the same `salt` on the Countly server. If
the `salt` on the Countly server is set, all requests would be checked for the
validity of the `&checksum` field before being processed.

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);  
    config.setParameterTamperingProtectionSalt("salt");  
    Countly.sharedInstance().init(config);

## SSL Certificate Pinning

Public key and certificate pinning are techniques that improve communication
security by eliminating the threat of [man-in-the-middle attack
(MiM)](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) in SSL
connections.

When you supply a list of acceptable SSL certificates to Countly SDK with
either `countlyConfig.enablePublicKeyPinning()` or
`countlyConfig.enableCertificatePinning()`, it will ensure that connection is
made with one of the public keys specified or one of the certificates
specified respectively. Using whole certificate pinning is somewhat safer, but
using public key pinning is preferred since certificates can be rotated and do
expire while public keys don't (assuming you don't change your CA).

Pinning is done during init through the CountlyConfig object.

For more information on how to acquire the public key or the certificate, have
a look [here](https://support.count.ly/hc/en-
us/articles/9290669873305-A-deeper-look-at-SDK-
concepts#h_01HDNHXZ2Y30VG0D1TKCYPHJXT).

Here is an example of public key pinning for a example server.

    
    
    //sample certificate for the countly try server
    String[] certificates = new String[] {
      "MIIGnjCCBYagAwIBAgIRAN73cVA7Y1nD+S8rToAqBpQwDQYJKoZIhvcNAQELBQAwgY8xCzAJ"
        + "BgNVBAYTAkdCMRswGQYDVQQIExJHcmVhdGVyIE1hbmNoZXN0ZXIxEDAOBgNVBAcTB1"
        + "NhbGZvcmQxGDAWBgNVBAoTD1NlY3RpZ28gTGltaXRlZDE3MDUGA1UEAxMuU2VjdGln"
        + "byBSU0EgRG9tYWluIFZhbGlkYXRpb24gU2VjdXJlIFNlcnZlciBDQTAeFw0yMDA2MD"
        + "EwMDAwMDBaFw0yMjA5MDMwMDAwMDBaMBUxEzARBgNVBAMMCiouY291bnQubHkwggEi"
        + "MA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCl9zmATVRwrGRtRQJcmBmA+zc/ZL"
        + "io3YfkwXO2w8u9lnw60J4JpPNn9OnGcxdM+sqbXKU3jTdjY4j3yaA6NlWibq2jU2x6"
        + "HT2sS+I5gFFE/6tO53WqjoMk48i3FkyoJDittwtQrVaRGcP8RjJH0pfXaP+JLrLAgg"
        + "HuW3tCFqYzkWi3uLGVjQbSIRNiXsM3FI0UMEa/x1I3U4hLjMjH28KagZbZLWnHOvks"
        + "AvGLg3xQkS+GSQ+6ARZ2/bGh5O9q4hCCCk0/PpwAXmrOnWtwrNuwHcCDOvuB22JxLd"
        + "t8jQDYrjwtJIvq4Yut8FQPv/75SKoETWWHyxe0x5NsB34UwA/BAgMBAAGjggNsMIID"
        + "aDAfBgNVHSMEGDAWgBSNjF7EVK2K4Xfpm/mbBeG4AY1h4TAdBgNVHQ4EFgQU8uf/ND"
        + "Rt8cu+AwARVIGXPMfxGbQwDgYDVR0PAQH/BAQDAgWgMAwGA1UdEwEB/wQCMAAwHQYD"
        + "VR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMEkGA1UdIARCMEAwNAYLKwYBBAGyMQ"
        + "ECAgcwJTAjBggrBgEFBQcCARYXaHR0cHM6Ly9zZWN0aWdvLmNvbS9DUFMwCAYGZ4EM"
        + "AQIBMIGEBggrBgEFBQcBAQR4MHYwTwYIKwYBBQUHMAKGQ2h0dHA6Ly9jcnQuc2VjdG"
        + "lnby5jb20vU2VjdGlnb1JTQURvbWFpblZhbGlkYXRpb25TZWN1cmVTZXJ2ZXJDQS5j"
        + "cnQwIwYIKwYBBQUHMAGGF2h0dHA6Ly9vY3NwLnNlY3RpZ28uY29tMB8GA1UdEQQYMB"
        + "aCCiouY291bnQubHmCCGNvdW50Lmx5MIIB9AYKKwYBBAHWeQIEAgSCAeQEggHgAd4A"
        + "dQBGpVXrdfqRIDC1oolp9PN9ESxBdL79SbiFq/L8cP5tRwAAAXJwTJ0kAAAEAwBGME"
        + "QCIEErTN/aGJ8LV9brGklKeGAXMg1EN/FUxXDu13kNfXhcAiBrKMYe+W4flPyuLNm5"
        + "jp6FJwtUTZPNpZ+TmM40dRdwjQB0AN+lXqtogk8fbK3uuF9OPlrqzaISpGpejjsSwC"
        + "BEXCpzAAABcnBMncsAAAQDAEUwQwIfEYSpsSDtKpmj9ZmRWsx73G622N74v09JDjzP"
        + "bkg9RQIgUelIqSwqu69JanH7losrqTTsjwNv+3QJBNJ6GxJKkh0AdgBvU3asMfAxGd"
        + "iZAKRRFf93FRwR2QLBACkGjbIImjfZEwAAAXJwTJ0YAAAEAwBHMEUCIQCMBaaQAoua"
        + "97R+z2zONMUq1XsDP5aoAiutZG4XxuQ6wAIgW1p6XS3az4CCqjwbDKxL9qEnw8fWd+"
        + "yLx2skviSsTS0AdwApeb7wnjk5IfBWc59jpXflvld9nGAK+PlNXSZcJV3HhAAAAXJw"
        + "TJ1PAAAEAwBIMEYCIQDg1YFbJPPKDIyrFZJ9rtrUklkh2k/wpgwjDuIp7tPtOgIhAL"
        + "dZl9s/qISsFm2E64ruYbdE4HKR1ZJ0zbIXOZcds7XXMA0GCSqGSIb3DQEBCwUAA4IB"
        + "AQB2Ar1h2X/S4qsVlw0gEbXO//6Rj8mTB4BFW6c5r84n0vTwvA78h003eX00y0ymxO"
        + "i5hkqB8gd1IUSWP1R1ijYtBVPdFi+SsMjUsB5NKquQNlWpo0GlFjRlcXnDC6R6toN2"
        + "QixJb47VM40Vmn2g0ZuMGfy1XoQKvIyRosT92jGm1YcF+nLEHBDr+89apZ8sUpFfWo"
        + "AnCom+8sBGwje6zP10eBbprHyzM8snvdwo/QNLAzLcvVNKP+Sr4H7HKzec3g1+THI0"
        + "M72TzoguJcOZQEI6Pd+FIP5Xad53rq4jCtRGwYrsieH49a3orBnkkJvUKni+mtkxMb"
        + "PTJ7eeMmX9g/0h"
    };
    
    CountlyConfig countlyConfig = new CountlyConfig(getApplicationContext(), COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    countlyConfig.enablePublicKeyPinning(certificates);
    Countly.sharedInstance().init(countlyConfig);

In case you get a `CertificateException` with `"Public keys didn't pass
checks"` that means the certificate or public key for the reached server did
not match to any one of the provided ones. Usually, it means that your
provided certificate is wrong.

In case you still have issues, have a look
[here](https://support.count.ly/hc/en-us/articles/9290669873305-A-deeper-look-
at-SDK-concepts#h_01HDNJK8PAE5GEQWRFDS4KD6S6).

## Using Proguard

The Countly Android SDK does not require specific proguard exclusions and can
be fully obfuscated.

If you are using the Huawei Push Kit for Push Notifications, make sure to add
these recommended proguard rules

    
    
    -ignorewarnings
    -keepattributes *Annotation*
    -keepattributes Exceptions
    -keepattributes InnerClasses
    -keepattributes Signature
    -keepattributes SourceFile,LineNumberTable
    -keep class com.huawei.hianalytics.**{*;}
    -keep class com.huawei.updatesdk.**{*;}
    -keep class com.huawei.hms.**{*;}

For the most up-to-date Huawei Push Kit proguard rules recommendations, have a
look [here](https://developer.huawei.com/consumer/en/doc/HMSCore-
Guides/android-config-obfuscation-scripts-0000001050176973).

More info about proguard, obfuscation, and code shrinking can be found
[here](https://developer.android.com/studio/build/shrink-code#keep-code).

# Other Features and Notes

## SDK Config Parameters Explained

These are the methods that lets you set values in your Countly config object:

  * **setContext(Context context)** \- Mandatory. Sets Android context.
  * **setServerURL(String serverURL)** \- Mandatory. Sets the URL of the Countly server to submit data to.
  * **setAppKey(String appKey)** \- Mandatory. Sets the app key for the application being tracked.
  * **setDeviceId(String deviceID)** \- Sets the unique ID for the device the app is running on. Null means that Countly will use the OpenUDID generation method.
  * **setStarRatingSessionLimit(int starRatingLimit)** \- Sets the limit after how many sessions the automatic star rating dialog is shown.
  * **setStarRatingCallback(StarRatingCallback starRatingCallback)** \- Sets the callback function that will be called from the automatic star rating dialog.
  * **setStarRatingTextTitle(String starRatingTextTitle)** \- Sets the title text for the star rating dialogs.
  * **setStarRatingTextMessage(String starRatingTextMessage)** \- Sets the message text for the star rating dialogs.
  * **setStarRatingTextDismiss(String starRatingTextDismiss)** \- Sets the dismiss button text for the star rating dialogs.
  * **setLoggingEnabled(boolean enabled)** \- Enables or disables internal debugging logs.
  * **enableCrashReporting()** \- Enables uncaught crash reporting.
  * **setViewTracking(boolean enable)** \- Enables or disables automatic view tracking.
  * **setAutoTrackingUseShortName(boolean enable)** \- Enables or disables the use of short names for automatic activity tracking.
  * **setAutomaticViewSegmentation(Map <String, Object> segmentation)** \- Sets the automatic view segmentation.
  * **setAutoTrackingExceptions(Class[] exceptions)** \- Sets activities to be excluded from automatic view tracking.
  * **addCustomNetworkRequestHeaders(Map <String, String> customHeaderValues)** \- Adds custom header key/value pairs to each request.
  * **setPushIntentAddMetadata(boolean enable)** \- Enables or disables adding metadata to push intents.
  * **setRemoteConfigAutomaticDownload(boolean enabled, RemoteConfigCallback callback)** \- If enabled, automatically downloads the newest remote config values.
  * **setRequiresConsent(boolean shouldRequireConsent)** \- Set if consent should be required.
  * **setConsentEnabled(String[] featureNames)** \- Sets which features are enabled in case consent is required.
  * **setHttpPostForced(boolean isForced)** \- Set the override for forcing to use HTTP POST for all connections to the server.
  * **enableTemporaryDeviceIdMode()** \- Enable temporary device ID mode.
  * **setCrashFilterCallback(CrashFilterCallback callback)** \- Set crash filter callback.
  * **setParameterTamperingProtectionSalt(String salt)** \- Set parameter tampering protection salt.
  * **setTrackOrientationChanges(boolean shouldTrackOrientation)** \- Set track orientation changes.
  * **setRecordAllThreadsWithCrash()** \- Set record all threads with crash.
  * **setEnableAttribution()** \- Enables or disables attribution.
  * **enablePublicKeyPinning()** \- Allows public key pinning by providing a list of SSL certificates.
  * **enableCertificatePinning()** \- Allows certificate pinning by providing a list of SSL certificates.
  * **setShouldIgnoreAppCrawlers()** \- Specifies if the Countly SDK should ignore app crawlers.
  * **setAppCrawlerNames()** \- Specifies the names of app crawlers to be ignored.
  * **setEventQueueSizeToSend()** \- Sets the threshold for event grouping.
  * **enableManualSessionControl()** \- Enables manual session control.
  * **setCustomCrashSegment()** \- Sets custom crash segmentation information to be added to all recorded crashes.
  * **setRecordAllThreadsWithCrash()** \- Sets record all threads with crash.
  * **checkForNativeCrashDumps(boolean checkForDumps)** \- Set the check for native crash dumps.
  * **setUpdateSessionTimerDelay(int delay)** \- Sets the interval for the automatic session update calls (min value 1 sec, max value 10 min).
  * **setCountlyStore(CountlyStore store)** \- Sets the Countly store for use during testing.
  * **setDisableUpdateSessionRequests(boolean disable)** \- Disables periodic session time updates.
  * **setIfStarRatingDialogIsCancellable(boolean isCancellable)** \- Sets if the star rating dialog is cancellable.
  * **setIfStarRatingShownAutomatically(boolean isShownAutomatically)** \- Sets if the star rating should be shown automatically.
  * **setStarRatingDisableAskingForEachAppVersion(boolean disableAsking)** \- Sets if the star rating is shown only once per app lifetime.
  * **setApplication(Application application)** \- Sets the link to the application class.
  * **apm.enableAppStartTimeTracking()** \- Enables the recording of the app start time.
  * **setDisableLocation()** \- Disables location tracking.
  * **setLocation(String country_code, String city, String gpsCoordinates, String ipAddress)** \- Sets location parameters.
  * **setMetricOverride(Map <String, String> providedMetricOverride)** \- Sets the metrics you want to override or additional custom metrics you want to provide. For more information on this, check here.
  * **apm.setAppStartTimestampOverride(long appStartTimestampOverride)** \- Overrides the app start timestamp.
  * **apm.enableManualAppLoadedTrigger()** \- Enables manual trigger of the moment when the app has finished loading.
  * **apm.enableForegroundBackgroundTracking()** \- Enables automatic control of triggers.
  * **setLogListener(ModuleLog.LogCallback logCallback)** \- Adds a log callback that duplicates all logs done by the SDK.
  * **setMaxRequestQueueSize(int newMaxSize)** \- Sets the new maximum size for the request queue.
  * **setDirectAttribution(String campaignType, String campaignData)** \- Reports direct user attribution.
  * **setIndirectAttribution(Map <String, String> attributionValues)** \- Reports indirect user attribution.
  * **setUserProperties(Map <String, Object> userProperties)** \- Provides user properties that would be sent as soon as possible.
  * **enableExplicitStorageMode()** \- If this mode is enabled then the SDK not write the request and event queues to disk until the explicit write signal is given.

## Example Integrations

[app](https://github.com/Countly/countly-sdk-android/tree/master/app) module
is an example integration that is written in Java. It covers most of the
functionalities.

[app-kotlin](https://github.com/Countly/countly-sdk-android/tree/master/app-
kotlin) module is an example integration that is written in Kotlin.

[app-native](https://github.com/Countly/countly-sdk-android/tree/master/app-
native) module is an example demonstration of native crash reporting in Java.

## Setting Event Queue Threshold

Events get grouped together and are sent either every minute or after the
unsent event count reaches a threshold. By default it is 10. If you would like
to change this, call:

    
    
    config.setEventQueueSizeToSend(6);

## Setting Maximum Request Queue Size

When you initialize Countly, you can specify a value for the
setMaxRequestQueueSize flag. This flag limits the number of requests that can
be stored in the request queue when the Countly server is unavailable or
experiencing connection problems.

If the server is down, requests sent to it will be queued on the device. If
the number of queued requests becomes excessive, it can cause problems with
delivering the requests to the server, and can also take up valuable storage
space on the device. To prevent this from happening, the
setMaxRequestQueueSize flag limits the number of requests that can be stored
in the queue.

If the number of requests in the queue reaches the setMaxRequestQueueSize
limit, the oldest requests in the queue will be dropped, and the newest
requests will take their place. This ensures that the queue doesn't become too
large, and that the most recent requests are prioritized for delivery.

If you do not specify a value for the setMaxRequestQueueSize flag, the default
setting of 1,000 will be used.

    
    
    config.setMaxRequestQueueSize(5000);

## Checking If the SDK Has Been Initialized

In case you would like to check if init has been called, you may use the
following function:

    
    
    Countly.sharedInstance().isInitialized();

## SDK Internal Limits

Countly SDKs have internal limits to prevent users from unintentionally
sending large amounts of data to the server. If these limits are exceeded, the
data will be truncated to keep it within the limit. You can check the exact
parameters these limits affect from [here](https://support.count.ly/hc/en-
us/articles/9290669873305-A-Deeper-Look-at-SDK-concepts#sdk_internal_limits).

### Key Length

Limits the maximum size of all user set keys (default: 128 chars):

    
    
    CountlyConfig config = new CountlyConfig(getApplicationContext(), COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.sdkInternalLimits.setMaxKeyLength(32);

### Value Size

Limits the size of all user-set string segmentation (or their equivalent)
values (default: 256 chars):

    
    
    CountlyConfig config = new CountlyConfig(getApplicationContext(), COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.sdkInternalLimits.setMaxValueSize(128);

### Segmentation Values

Limits the amount of user-set segmentation key-value pairs (default: 100
entries):

    
    
    CountlyConfig config = new CountlyConfig(getApplicationContext(), COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.sdkInternalLimits.setMaxSegmentationValues(50);

### Breadcrumb Count

Limits the amount of user-set breadcrumbs that can be recorded (default: 100
entries, exceeding this deletes the oldest one):

    
    
    CountlyConfig config = new CountlyConfig(getApplicationContext(), COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.sdkInternalLimits.setMaxBreadcrumbCount(50);

### Stack Trace Lines Per Thread

Limits the stack trace lines that would be recorded per thread (default: 30
lines):

    
    
    CountlyConfig config = new CountlyConfig(getApplicationContext(), COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.sdkInternalLimits.setMaxStackTraceLinesPerThread(10);

### Stack Trace Line Length

Limits the characters that are allowed per stack trace line (default: 200
chars):

    
    
    CountlyConfig config = new CountlyConfig(getApplicationContext(), COUNTLY_APP_KEY, COUNTLY_SERVER_URL);
    config.sdkInternalLimits.setMaxStackTraceLineLength(100);

## Attribution

This feature is available for the [Countly
Enterprise](https://countly.com/enterprise), but currently server side support
for this is limited.

**To report install attribution, you would perform the following request:**

    
    
    Countly.sharedInstance().attribution().recordDirectAttribution("countly", "{'cid':'campaign_id', 'cuid':'campaign_user_id'}");

**In the place of "campaign_id" you would put your retrieved campaign ID
value, and in place of " campaign_user_id" you would put your campaign user
ID.**

**For information on how to get these install attribution values, we recommend
looking
into["InstallReferrerClient".](https://developer.android.com/reference/com/android/installreferrer/api/InstallReferrerClient)**

**If you would want to record the advertising ID of the user, you would
execute the following code with the retrieved value:**

    
    
    Map<String, String> attributionValues = new HashMap<>();  
    attributionValues.put(AttributionIndirectKey.AdvertisingID, "valid_advertising_id_value");  
    Countly.sharedInstance().attribution().recordIndirectAttribution(attributionValues);

## Forcing HTTP POST

If the data sent to the server is short enough, the SDK will use HTTP GET
requests. To override that behavior so that HTTP POST requests are used in all
cases, you will need to set "setHttpPostForced" flag as true in your init
config.

    
    
    // enable it at your init config
    CountlyConfig config = (new CountlyConfig(appC, COUNTLY_APP_KEY, COUNTLY_SERVER_URL));
    config.setHttpPostForced(true);
    
    // or set it to false
    config.setHttpPostForced(false);
    

## Custom HTTP Header Values

In case you would like to add custom header key/value pairs to each request
sent to the Countly server, you may make the following call:

    
    
    HashMap<String, String> customHeaderValues = new HashMap<>();
    customHeaderValues.put("foo", "bar");
    
    config.addCustomNetworkRequestHeaders(customHeaderValues);

The provided values will override any previously stored value pairs. In case
you would like to erase any previously stored pairs, provide `null`.

## Custom Metrics

During some specific circumstances, like beginning a session or requesting
remote config, the SDK is sending device metrics.

It is possible for you to either override the sent metrics (like the
application version for some specific variant) or provide either your own
custom metrics. If you are providing your own custom metrics, you would need
your own custom plugin server-side which would interpret it appropriately. If
there is no plugin to handle those custom values, they will be ignored. You
can set these custom metrics while initializing the Countly SDK.

    
    
    //provide custom metric values
    CountlyConfig config = ... // configuration related to implementation
    
    Map<String, String> metricOverride = new HashMap<>();
    metricOverride.put("SomeKey", "123");
    metricOverride.put("_app_version", "custom_version-123");
    
    config.setMetricOverride(metricOverride);

For more information on the specific metric keys used by Countly, check
[here](https://support.count.ly/hc/en-
us/articles/9290669873305#h_01HABT18WWYQ2QYPZY3GHZBA9B).

## Log Listener

Android SDK lets you handle its internal logs by allowing you to provide a
callback to listen to its log output. This callback must be put inside the
Countly config object with the help of the `setLogListener()` method. This
callback should return two parameters: first, the String log message, and
second, the log level enum. Using these two pieces of information, you should
be able to do anything you see fit with these logs.

An example usage:

    
    
     CountlyConfig config = (new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL))
      .setLoggingEnabled(true)
      .setLogListener(new ModuleLog.LogCallback() {
        @Override public void LogHappened(String logMessage, ModuleLog.LogLevel logLevel) {
          // do something according to the log level
          switch (logLevel) {
            case Verbose:
              // do something
              break;
            case Debug:
              // do something
              break;
            case Info:
              // do something
              break;
            case Warning:
              // do something
              break;
            case Error:
              // do something
              break;
          }
        }
      });
    

## Receiving and Showing Badge Numbers from Push Notifications

While showing badges isn't supported natively for versions before Android O,
there are some devices and launchers that support it. Therefore, you may want
to implement such a feature in your app. However, not all devices will support
badges.

While creating a new message in the messaging overview and preparing its
content, there is an optional prompt called "Add iOS badge". You may use this
prompt to also send badges to Android devices.

![](https://count.ly/images/guide/5fbc4a2-Ekran_Resmi_2017-01-27_07.15.34.png)

In order to receive this badge number in your application, you must subscribe
to the broadcasts about received messages. There you will be informed about
all received push notifications using Message and the bundle. The badge number
is sent with the key "badge". You may use it to extract the badge number from
the bundle received and then use it to display badge numbers with your
implementation of choice.

In the example below, we use a badge library called
[ShortcutBadger](https://github.com/leolin310148/ShortcutBadger), which is
used for showing badge notifications on Android devices. You can reach
instructions on how to implement it into your Android project
[here](https://github.com/leolin310148/ShortcutBadger#usage).

    
    
    /** Register for broadcast action if you need to be notified when Countly message received */
    messageReceiver = new BroadcastReceiver() {
      @Override
      public void onReceive(Context context, Intent intent) {
        Message message = intent.getParcelableExtra(CountlyMessaging.BROADCAST_RECEIVER_ACTION_MESSAGE);
        Log.i("CountlyActivity", "Got a message with data: " + message.getData());
    
        //Badge related things
        Bundle data = message.getData();
        String badgeString = data.getString("badge");
        try {
          int badgeCount = Integer.parseInt(badgeString);
    
          boolean succeded = ShortcutBadger.applyCount(getApplicationContext(), badgeCount);
          if(!succeded) {
            Toast.makeText(getApplicationContext(), "Unable to put badge", Toast.LENGTH_SHORT).show();
          }
        } catch (NumberFormatException exception) {
          Toast.makeText(getApplicationContext(), "Unable to parse given badge number", Toast.LENGTH_SHORT).show();
        }
      }
    };
    IntentFilter filter = new IntentFilter();
    filter.addAction(CountlyMessaging.getBroadcastAction(getApplicationContext()));
    registerReceiver(messageReceiver, filter);

## Ignoring App Crawlers

Sometimes server data might be polluted with app crawlers which are not real
users, and you would like to ignore them. Starting from the 17.05 release,
it's possible to ignore app crawlers by filtering on the app level. The
current version does that, using device names. Internally, the Countly SDK has
a list of crawler device names. If a device name matches one from that list,
no information is sent to the server.

At the moment, that list has only one entry: "Calypso AppCrawler". In the
future we might add more crawler device names if such are reported. If you
have encountered a crawler that is not on that list, and you would like to
ignore it, you may add it to your SDK list yourself by calling
`addAppCrawlerName`.

Currently, the SDK ignores crawlers by default. If you would like to change
this setting, use `ifShouldIgnoreCrawlers`. If you would like to check if the
current device was detected as a crawler, use `isDeviceAppCrawler`. Detection
is done in the init function, meaning you would have to add the crawler names
before that and perform the check after.

    
    
    CountlyConfig config = new CountlyConfig(this, COUNTLY_APP_KEY, COUNTLY_SERVER_URL);  
      
    //set that the sdk should ignore app crawlers
    config.setShouldIgnoreAppCrawlers(true);
    
    //set that the sdk should not ignore app crawlers
    config.setShouldIgnoreAppCrawlers(false);
    
    //add app crawler device names to ignore
    config.setAppCrawlerNames(new String[] { "App Crawler" });
    
    //returns true if this device is detected as a app crawler and false otherwise
    Countly.sharedInstance().requestQueue().isDeviceAppCrawler();

## Interacting with the Internal Request Queue

When recording events or activities, the requests don't always get sent
immediately. Events get grouped together and sometimes there is no connection
to the server and the requests can't be sent.

There are two ways how to interact with this request queue at the moment.

You can force the SDK to try to send the requests immediately:

    
    
    //Doing internally stored requests  
    Countly.sharedInstance().requestQueue().attemptToSendStoredRequests();

This way the SDK will not wait for its internal triggers and it will try to
empty the queue on demand.

There are some circumstances where you would want to delete all stored
requests. Then you would call:

    
    
    //Delete all stored requests in queue  
    Countly.sharedInstance().requestQueue().flushQueues();

## Direct Request

This feature allows you to create custom functionality or implement features
that the SDK might be lacking at that moment.

This feature should not be used lightly as improper usage can lead to
problems.

This exposes a call where you can provide custom key/value pairs with
`Map<String, String>`. These will be added to a base request created by the
SDK. The base parameters will have things like time-related fields, device ID,
app key, checksums, etc. These base parameters are protected fields and can't
be overridden.

If consent would be required then the SDK will make sure that any consent has
been given. The SDK will not perform any additional consent checks. It is up
to the developer to make sure that they have the right consent to record the
information they are trying to record.

These key/value pairs should be of simple string or stringified JSON. The
simplest way to pass a stringified JSON is to create a JSONObject/JSONArray
and call the toString() function on it to convert it to a stringified JSON.  

    
    
    Map<String, String> requestMap = new HashMap<>();
    requestMap.put("city", "Istanbul");
    requestMap.put("country_code", "TR");
    requestMap.put("ip_address", "41.0082,28.9784");
    
    try {
      JSONObject event = new JSONObject();
      event.putOpt("key", "test");
      event.putOpt("count", "5");
      event.putOpt("sum", "2");
      event.putOpt("dur", "2000");
    
      JSONObject ffJson = new JSONObject();
      ffJson.putOpt("type", "FF");
      ffJson.putOpt("start_time", 123456789);
      ffJson.putOpt("end_time", 123456789);
    
      JSONObject skipJson = new JSONObject();
      skipJson.putOpt("type", "skip");
      skipJson.putOpt("start_time", 123456789);
      skipJson.putOpt("end_time", 123456789);
    
      JSONObject resumeJson = new JSONObject();
      resumeJson.putOpt("type", "resume_play");
      resumeJson.putOpt("start_time", 123456789);
      resumeJson.putOpt("end_time", 123456789);
    
      JSONArray trickPlay = new JSONArray();
      trickPlay.put(ffJson);
      trickPlay.put(skipJson);
      trickPlay.put(resumeJson);
    
      JSONObject segmentation = new JSONObject();
      segmentation.putOpt("trickplay", trickPlay);
      event.putOpt("segmentation", segmentation);
    
      JSONArray events = new JSONArray();
      events.put(event);
      requestMap.put("events",events.toString());
    } catch (JSONException e) {
      e.printStackTrace();
    }
    Countly.sharedInstance().requestQueue().addDirectRequest(requestMap);

## Explicit Storage Mode

The Explicit Storage Mode is a feature that allows you to control the
frequency of writes to your device's storage.

With this mode enabled, the Countly SDK's request and event queues will be
stored only in memory and will not be automatically persisted to storage when
changes occur. Instead, the host app must explicitly signal when the queues
should be persisted to storage.

Please note that using this mode increases the risk of data loss and data
duplication if persistence synchronization is not implemented correctly.

To enable Explicit Storage Mode during initialization, use the following
configuration option:

    
    
    config.enableExplicitStorageMode();

To write the memory queues to storage, use the following method:

    
    
    Countly.sharedInstance().requestQueue().esWriteCachesToPersistence();

If you want know if any writes were performed, you can also use the following
variant. It allows you to set a callback that would inform you if anything was
written to storage. If your memory cache state would be the same as your
perisent storage state, no writes would be performed.

    
    
    Countly.sharedInstance().requestQueue().esWriteCachesToPersistence(new ExplicitStorageCallback() {
      @Override public void WriteToStorageFinished(boolean writeWasPerformed) {
        if (writeWasPerformed) {
          Log.d(Countly.TAG, "Memory cache ouf of sync with persistent storage. New state was written to storage.");
        } else {
          Log.d(Countly.TAG, "Memory cache matches persistent storage. No writes were performed.");
        }
      }
    });

Like mentioned before, inpropper usage can lead to data loss or data
duplication.

Data loss can occur when you have recorded new data and there is no or slow
connection to your server. If your app would crash or exit before the SDK is
able to send that data or before you had the ability to call
`esWriteCacheToStorage` , that information would be lost.

Data duplication can occur when you have recorded data and have called
`esWriteCacheToStorage` before it is sent to your server. This would then
persist the "full" queues to storage. After this point the data would have
been successfully sent to your server, but then no call would be made to
`esWriteCacheToStorage` before the app crashes or exits. During the next init
of the SDK it would then load the persistent state from storage to memory and
try sending those requests. When that would happen, the SDK would attempt to
send requests that were already successfully sent to the server.

We recommend using Explicit Storage Mode only in scenarios where reducing the
frequency of writes to storage is critical to the performance of your app. In
other scenarios, we recommend using the default storage behavior provided by
the Countly SDK.

## Server Configuration

This is an experimental feature!

You can make your SDK fetch some configurations you have set in your Countly
server by setting `enableServerConfiguration` during init:

    
    
    config.enableServerConfiguration()

## A/B Testing Variant Information

You can access all the A/B test variants for your Countly application within
your mobile app. This information can be useful while testing your app with
different variants. There are four calls you can use for downloading,
accessing, and enrolling for your variants.

### Downloading Test Variants

You can download a map of all A/B testing parameters (keys) and variants
associated with it:

    
    
    Countly.sharedInstance().remoteConfig().testingDownloadVariantInformation(RCVariantCallback completionCallback)

You can provide an RCVariantCallback (which is optional) to be called when the
fetching process ends. Depending on the situation, this would return a
RequestResponse Enum (Success, NetworkIssue, or Error) as the first parameter
and a String error as the second parameter if there was an error ("null"
otherwise). A sample usage would be like this:

    
    
    Countly.sharedInstance().remoteConfig().TestingDownloadVariantInformation(new RCVariantCallback() {
      @Override
      public void callback(RequestResponse result, String error) {
        if (result == RequestResponse.Success) {
          // do sth after the success
        } else {
          // do sth after failure
        }
      }
    });
    

### Accessing Fetched Test Variants

When test variants are downloaded, they are saved to the memory. If the memory
is erased, you must download the variants again. So a common flow is to use
the fetched values right after fetching them. To access all fetched values,
you can use:

    
    
    Countly.sharedInstance().remoteConfig().testingGetAllVariants()

This would return a Map<String, String[]> where a test's parameter is
associated with all variants under that parameter. The parameter would be the
key, and its value would be a String Array of variants. For example:

    
    
    {
      "key_1" : ["variant_1", "variant_2"],
      "key_2" : ["variant_3"]
    }
    

Or instead you can get the variants of a specific key:

    
    
    Countly.sharedInstance().remoteConfig().testingGetVariantsForKey(String valueKey)

This would only return a String Array (String[]) of variants for that specific
key. If no variants were present for a key, it would return an empty array. A
typical result would look like this:

    
    
    ["variant_1", "variant_2"]
    

### Enrolling For a Variant

After fetching A/B testing parameters and variants from your server, next you
would like to enroll the user to a specific variant. To do this, you can use
the following method:

    
    
    Countly.sharedInstance().remoteConfig().testingEnrollIntoVariant(String keyName, String variantName, RCVariantCallback completionCallback)

Here the 'valueKey' would be the parameter of your A/B test, and 'variantName'
is the variant you have fetched and selected to enroll for. The
RCVariantCallback callback function is optional and works the same way as
explained above in the Downloading Test Variants section.

## Drop Old Requests

If you are concerned about your app being used sparsely over a long time
frame, old requests inside the request queue might not be important. If, for
any reason, you don't want to get data older than a certain timeframe, you can
configure the SDK to drop old requests:

    
    
    config.setRequestDropAgeHours(10)

By using the `setRequestDropAgeHours` method while configuring the SDK
initialization options, you can set a timeframe (in hours) after which the
requests would be removed from the request queue. For example, by setting this
option to 10, the SDK would ensure that no request older than 10 hours would
be sent to the server.

# FAQ

## What Information is Collected by the SDK

The following description mentions data that is collected by SDK's to perform
their functions and implement the required features. Before any of it is sent
to the server, it is stored locally. For further information please have a
look to the [collected informations](https://support.count.ly/hc/en-
us/articles/9290669873305-A-deeper-look-at-SDK-
concepts#h_01HJ5MD0WB97PA9Z04NG2G0AKC) for all SDKs.

## How can I build the Android SDK?

If you need to customize our Android SDK to fit your needs, you may find it
[here](https://github.com/Countly/countly-sdk-android) among our Countly
Github repositories as an Android Studio project. Modules included in the
project are:

Module Name | Description  
---|---  
`sdk` | Countly Android SDK.  
`app` | Sample app to test `sdk`  
`sdk-native` | Module needed for [Native C++ crash reporting](https://support.count.ly/hc/en-us/articles/360037754031-Android-SDK#h_01HAVQDM5TFKEHBN5G8J9VSP37)  
`app-native` | Sample app to test `sdk-native`  
  
Recently, Android Studio versions have a
[bug](https://github.com/Countly/countly-sdk-
android/issues/96#issuecomment-492327285) which you may encounter when
building your project in Studio. If you see a build error such as `SIMPLE:
Error configuring`, please check your text view for the build Gradle output.
If you see this error `CMake was unable to find a build program corresponding
to "Ninja". CMAKE_MAKE_PROGRAM is not set`, then you need to make `ninja`
available in your PATH. If you are using `cmake` embedded in Studio, `ninja`
may be found in the `<sdk_location>/cmake/<cmake_version>/bin` directory.

There is a build step for the `sdk-native` module which takes place outside of
Studio. You may find the related code and build scripts in `sdk-
native/src/cpp_precompilation`. We are working on building a breakpad library
with an appropriate ndk version to integrate this step into your Studio build.
Meanwhile, it seems OK to use the library files in `sdk-
native/src/main/jniLibs/` that are externally built.

## Which Operating Systems are Supported?

Our Android SDK should be able support Android based operating systems without
issues. It should also work without any major issues on devices that don't
have Google services, for example, on Huawei devices which have the HarmonyOS
operating system.

## Is it Possible to Use Android SDK with Another Crash SDK?

It should be fine to use Countly together with another crash SDK. If you would
like to track caught exception, you would just pass them to both SDKs. When
catching uncaught exceptions with both, there are some uncertainties. Although
in Android there can be only one uncaught exception handler, you can save the
previous handler and when receiving an uncaught exception, pass it also to the
saved one. We can't be certain how other SDKs are implemented or if the OS
would give enough time to propagate the exception through all handlers.
Therefore, if you want to use Countly with another crash SDK, we advise to
initialize Countly as the last one.

## How Can I Tell Which Countly Android SDK Version I am Using?

The Countly class has a public static string called
`COUNTLY_SDK_VERSION_STRING` that contains the current SDK version. You can
access it by calling `Countly.COUNTLY_SDK_VERSION_STRING`. It would return
something similar to "20.11.10".

## Looking for help?

[ Countly Enterprise Support Login using your company email to create a
support ticket as a Countly Enterprise Customer
__](https://support.count.ly/hc/en-us/signin)

[ Countly Enterprise Support Create a ticket for any support request you might
have as a Countly Enterprise Customer __](https://support.count.ly/hc/en-
us/requests/new)

[ Countly Community Join us on Discord to engage in discussions, share your
feature ideas, and learn from fellow Countly users
__](https://discord.gg/countly)

![](/hc/theming_assets/01HZKRSA6VPV8TKNTGD6Q71QER)

We are on a mission to liberate and secure your analytics data

We are committed to giving you control of your analytics data. 100% data
ownership, 100% control.

An analytics platform as it should be.

[__](https://www.youtube.com/user/GoCountly/videos)[__](https://twitter.com/gocountly)[__](https://www.linkedin.com/company/countly)[__](https://www.facebook.com/Countly/)[__](https://discord.gg/countly)

Product

[Privacy by Design](https://count.ly/privacy-by-design)
[Overview](https://count.ly/product) [Plugins](https://count.ly/plugins)
[Mobile Analytics](https://count.ly/mobile-analytics) [Web
Analytics](https://count.ly/web-analytics) [Desktop
Analytics](https://count.ly/desktop-analytics) [IoT
Analytics](https://count.ly/internet-of-things-analytics)
[Pricing](https://count.ly/pricing)

Company

[About](https://count.ly/about) [Customers](https://count.ly/customers)
[Partners](https://count.ly/partners) [Jobs](https://angel.co/countly/jobs)
[Blog](https://blog.count.ly/) [Brand Assets](https://count.ly/brand-assets)
[Open Source](https://github.com/Countly)

Featured Plugins

[User Profiles](https://count.ly/plugins/user-profiles) [Advanced
Segmentation](https://count.ly/plugins/drill-segmentation) [Behavioral
Cohorts](https://count.ly/plugins/behavioral-cohorts) [Push
Notifications](https://count.ly/plugins/rich-push-notifications) [Automated
Push](https://count.ly/plugins/automated-push-notifications) [Remote
Configuration](https://count.ly/plugins/remote-config) [A/B
Testing](https://count.ly/plugins/ab-testing) [Crash
Analytics](https://count.ly/plugins/crash-analytics)

