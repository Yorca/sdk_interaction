SDK name: Visual Studio App Center
Documentation:
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
docs/blob/live/docs/sdk/other-apis/android.md "Edit This Document")

Table of contents Read in English Save Add to Plan [ Edit
](https://github.com/MicrosoftDocs/appcenter-docs/blob/live/docs/sdk/other-
apis/android.md "Edit This Document")

* * *

#### Share via

Facebook x.com LinkedIn Email

* * *

Print

Table of contents

# Other Android APIs

  * Article
  * 11/28/2022
  * 12 contributors

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
  * [MAUI/Xamarin](xamarin)
  * [UWP](uwp)
  * [WPF/WinForms](wpf-winforms)
  * [Unity](unity)
  * [macOS](macos)
  * [tvOS](tvos)
  * [Cordova](cordova)

## Adjust the log level

You can control the amount of log messages by App Center that show up in
LogCat. Use the `AppCenter.setLogLevel()` API to enable additional logging
while debugging. The log levels correspond to the ones defined in
`android.util.Log`. By default, it's set it to `ASSERT` for non-debuggable
applications and `WARN` for debuggable applications. You can set the log level
at any time you want.

To have as many log messages as possible, use `Log.Verbose`.

    
    
    AppCenter.setLogLevel(Log.VERBOSE);
    
    
    
    AppCenter.setLogLevel(Log.VERBOSE)
    

## Identify installations

The App Center SDK creates a UUID for each device once the app is installed.
This identifier remains the same for a device when the app is updated and a
new one is generated only when the app is re-installed or the user manually
deletes all app data. The following API is useful for debugging purposes.

    
    
    AppCenter.getInstallId();
    
    
    
    AppCenter.getInstallId()
    

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](android) guide.

Note

This method must only be used after `AppCenter` has been started, it will
always return `null` before start.

## Identify users

The App Center SDK supports setting a **user ID** that's used to augment crash
reports. To use this capability:

  1. Configure the App Center SDK by calling `AppCenter.start(...)` as described in the [App Center SDK Getting started guide](../getting-started/android).
  2. Set a `userID` in the SDK using the following code:

    
    
    AppCenter.setUserId("your-user-id");
    
    
    
    AppCenter.setUserId("your-user-id")
    

After setting a user ID, you can use App Center's search feature to search for
specific crash reports for the ID. Learn more in App Center's [search
documentation](../../diagnostics/search).

Note

The value for the user ID is limited to 256 characters. It will be shown with
your crash reports but not used for aggregation or counts of affected users.
In case you set user ID multiple times, only the last user ID will be used.
You need to set the user ID yourself before each application launch, because
this value isn't stored by the SDK between launches.

## Disable all services at runtime

If you want to disable all App Center services at once, use the `setEnabled()`
API. When disabled, the SDK won't forward any information to App Center.

    
    
    AppCenter.setEnabled(false);
    
    
    
    AppCenter.setEnabled(false)
    

To enable all services at once again, use the same API but pass `true` as a
parameter.

    
    
    AppCenter.setEnabled(true);
    
    
    
    AppCenter.setEnabled(true)
    

The state is persisted in the device's storage across application launches.

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](android) guide.

Note

This method must only be used after `AppCenter` has been started.

## Disallow network requests

In the App Center SDK, network requests are allowed by default. If you want to
send data that the App Center SDK collects by the user concern you can
disallow automatic sending data.

    
    
    AppCenter.setNetworkRequestsAllowed(false);
    
    
    
    AppCenter.setNetworkRequestsAllowed(false)
    

In this case, the App Center SDK continues to collect data but it will be sent
only when the network requests will be allowed.

    
    
    AppCenter.setNetworkRequestsAllowed(true);
    
    
    
    AppCenter.setNetworkRequestsAllowed(true)
    

Note

This value is retained between starts.

At any time, you can check whether sending data in the App Center SDK is
allowed or not.

    
    
    AppCenter.isNetworkRequestsAllowed();
    
    
    
    AppCenter.isNetworkRequestsAllowed()
    

Note

The value saved previously in `SharedPreferences` is ignored until `AppCenter`
is started. It will return the last value set using
`setNetworkRequestsAllowed` or `true` if the value wasn't changed before
AppCenter start.

## Change state of service in runtime

Enable or disable the services at the runtime with following code:

    
    
    Analytics.setEnabled(false);
    
    
    
    Analytics.setEnabled(false)
    

Note

This method must only be used after `Analytics` has been started.

## Check if App Center is enabled

You can also check if App Center is enabled or not.

    
    
    AppCenter.isEnabled();
    
    
    
    AppCenter.isEnabled()
    

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](android) guide.

Note

This method must only be used after `AppCenter` has been started, it will
always return `false` before start.

## Check App Center SDK version at runtime

You can get the version of App Center SDK that you're currently using.

    
    
    AppCenter.getSdkVersion();
    
    
    
    AppCenter.getSdkVersion()
    

## Storage size

When using the App Center SDK, logs are stored locally on the device. Large
logs can take up a lot of space, so you may choose to limit the size of the
local database. It's also useful in conjunction with the `pause` and `resume`
APIs. If you expect to be paused for a long time, you can use a larger
database size to store more events.

You can use the `setMaxStorageSize` API to set the size of the local DB. The
API is asynchronous, and the callback is called when you start App Center
services. For this reason, `setMaxStorageSize` must be called before your call
to `AppCenter.start(...)`. You may only call the API once.

    
    
    // Use 20 MB for storage.
    AppCenter.setMaxStorageSize(20 * 1024 * 1024L).thenAccept(new AppCenterConsumer<Boolean>() {
    
        @Override
        public void accept(Boolean success) {
            // The success parameter is false when the size can't be honored.
        }
    });
    AppCenter.start("{Your App Secret}", Analytics.class);
    
    
    
    // Use 20 MB for storage.
    AppCenter.setMaxStorageSize(20 * 1024 * 1024).thenAccept {
        // The success parameter (it) is false when the size can't be honored.
    }
    
    AppCenter.start(application, "{Your App Secret}", Analytics::class.java)
    

If you don't set the max storage size, the SDK uses a default max size of 10
MB. The minimum size you're allowed to set is 20 KB.

Note

The actual max storage size may be higher than the value you've chosen. SQLite
rounds the size up to the next multiple of the page size. The App Center SDK
uses a page size of 4 KB.

Note

The logs older than 25 days will be discarded.

## Add distribution stores

By default in-app updates work for apps installed from the defined list of
stores. If you want to distribute your application via stores that are not
included in the predefined list of stores, then you can add the needed package
installer using the API below before App Center start:

    
    
        Set<String> stores = new HashSet<String>();
        stores.add("com.store1.packageinstaller");
        stores.add("com.store2.packageinstaller");
        Distribute.addStores(stores);
    

Note

Don't add stores like Google Play to avoid any restrictions.

### Unsuccessful API calls

There are many reasons the callback may fail.

  * The specified size is an invalid value (less than 20KB or greater than 140TB).
  * The current database size is larger than the specified maximum size.
  * The API has already been called. You may configure it only once per process.
  * The API has been called after `AppCenter.start(...)`.

You can check warnings and errors in the console using the `AppCenter` log tag
to troubleshoot configuration issues.

## Asynchronous APIs in the Android SDK

Asynchronous APIs return a `AppCenterFuture` object instead of returning the
result directly.

You can either call `get()` on the future object to synchronously wait for the
result or provide a callback like this, filling in the respective return types
when calling the API:

    
    
    AppCenterFuture<{ReturnType}> future = {AnyAsyncApi}();
    future.thenAccept(new AppCenterConsumer<{ReturnType}>() {
    
        @Override
        public void accept({ReturnType} result) {
    
            // do something with result, this is called back in UI thread.
        }
    });
    
    
    
    val future = {AnyAsyncApi}()
    future.thenAccept(object : AppCenterConsumer<{ReturnType}> {
        override fun accept(t: {ReturnType}?) {
            // do something with result, this is called back in UI thread.
        }
    })
    

To avoid blocking UI thread that causes slowing down your application,
consider using `thenAccept` with the callback all the time.

On a worker thread you can call `{AnyAsyncApi}().get()`.

Callback example:

    
    
    AppCenter.isEnabled().thenAccept(new AppCenterConsumer<Boolean>() {
    
        @Override
        public void accept(Boolean enabled) {
            Log.d("MyApp", "AppCenter.isEnabled=" + enabled);
        }
    });
    
    
    
    AppCenter.isEnabled().thenAccept { enabled -> 
        Log.d("MyApp", "AppCenter.isEnabled=$enabled")
    }
    

Synchronous example:

    
    
    boolean enabled = AppCenter.isEnabled().get();
    
    
    
    val enabled = AppCenter.isEnabled().get()
    

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
docs/blob/live/docs/sdk/crashes/android.md "Edit This Document")

Table of contents Read in English Save Add to Plan [ Edit
](https://github.com/MicrosoftDocs/appcenter-
docs/blob/live/docs/sdk/crashes/android.md "Edit This Document")

* * *

#### Share via

Facebook x.com LinkedIn Email

* * *

Print

Table of contents

# App Center Crashes (Android)

  * Article
  * 11/28/2022
  * 19 contributors

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
  * [MAUI/Xamarin](xamarin)
  * [UWP](uwp)
  * [WPF/WinForms](wpf-winforms)
  * [Unity](unity)
  * [macOS](macos)
  * [tvOS](tvos)
  * [Cordova](cordova)

App Center Crashes will automatically generate a crash log every time your app
crashes. The log is first written to the device's storage and when the user
starts the app again, the crash report will be sent to App Center. Collecting
crashes works for both beta and live apps, i.e. those submitted to Google
Play. Crash logs contain valuable information for you to help fix the crash.

Follow the [Getting Started](../getting-started/android) section if you
haven't set up the SDK in your application yet.

## Generate a test crash

App Center Crashes provides you with an API to generate a test crash for easy
testing of the SDK. This API can only be used in debug builds and won't do
anything in release builds.

    
    
    Crashes.generateTestCrash();
    
    
    
    Crashes.generateTestCrash()
    

## Get more information about a previous crash

App Center Crashes has two APIs that give you more information in case your
app has crashed.

### Did the app receive a low memory warning in the previous session?

At any time after starting the SDK, you can check if the app received a memory
warning in the previous session:

    
    
    Crashes.hasReceivedMemoryWarningInLastSession();
    
    
    
    Crashes.hasReceivedMemoryWarningInLastSession()
    

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](../other-apis/android) guide.

Note

This method must only be used after `Crashes` has been started, it will always
return `false` before start.

Note

In some cases, a device with low memory can't send events.

### Did the app crash in the previous session?

At any time after starting the SDK, you can check if the app crashed in the
previous launch:

    
    
    Crashes.hasCrashedInLastSession();
    
    
    
    Crashes.hasCrashedInLastSession()
    

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](../other-apis/android) guide.

This comes in handy in case you want to adjust the behavior or UI of your app
after a crash has occurred. Some developers chose to show additional UI to
apologize to their users, or want way to get in touch after a crash has
occurred.

Note

This method must only be used after `Crashes` has been started, it will always
return `false` before start.

### Details about the last crash

If your app crashed previously, you can get details about the last crash.

    
    
    Crashes.getLastSessionCrashReport();
    
    
    
    Crashes.getLastSessionCrashReport()
    

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](../other-apis/android) guide.

There are numerous use cases for this API, the most common one is people who
call this API and implement their custom CrashesListener.

Note

This method must only be used after `Crashes` has been started, it will always
return `null` before start.

## Customize your usage of App Center Crashes

App Center Crashes provides callbacks for developers to perform additional
actions before and when sending crash logs to App Center.

To handle the callbacks, either implement all methods in the `CrashesListener`
interface, or override the `AbstractCrashesListener` class and pick only the
ones you're interested in.

### Use your own CrashesListener

Create your own CrashesListener and assign it like this:

    
    
    CrashesListener customListener = new CrashesListener() {
        // Implement all callbacks here.
    };
    Crashes.setListener(customListener);
    
    
    
    val customListener = object : CrashesListener {
        // Implement all callbacks here.
    }
    Crashes.setListener(customListener)
    

In case you're only interested in customizing some of the callbacks, use the
`AbstractCrashesListener` instead:

    
    
    AbstractCrashesListener customListener = new AbstractCrashesListener() {
        // Implement any callback here as required.
    };
    Crashes.setListener(customListener);
    
    
    
    val customListener = object : AbstractCrashesListener() {
        // Implement any callback here as required.
    }
    Crashes.setListener(customListener)
    

Note

Set the listener _before_ calling `AppCenter.start()`, since App Center starts
processing crashes immediately after the start.

### Should the crash be processed?

Implement this callback if you want to decide if a particular crash needs to
be processed or not. For example, there could be a system level crash that
you'd want to ignore and that you don't want to send to App Center.

    
    
    @Override
    public boolean shouldProcess(ErrorReport report) {
        return true; // return true if the crash report should be processed, otherwise false.
    }
    
    
    
    override fun shouldProcess(report: ErrorReport?): Boolean {
        return true
    }
    

### Ask for the user's consent to send a crash log

If user privacy is important to you, you might want to get user confirmation
before sending a crash report to App Center. The SDK exposes a callback that
tells App Center Crashes to await user confirmation before sending any crash
reports.

If you chose to do so, you're responsible for obtaining the user's
confirmation, e.g. through a dialog prompt with one of the following options:
**Always Send** , **Send** , and **Don't send**. Based on the input, you'll
tell App Center Crashes what to do and the crash will then be handled
accordingly.

Note

The SDK doesn't display a dialog for this, the app must provide its own UI to
ask for user consent.

The following callback shows how to tell the SDK to wait for user confirmation
before sending crashes:

    
    
    @Override
    public boolean shouldAwaitUserConfirmation() {
    
        // Build your own UI to ask for user consent here. SDK doesn't provide one by default.
    
        // Return true if you built a UI for user consent and are waiting for user input on that custom UI, otherwise false.
        return true;
    }
    
    
    
    override fun shouldAwaitUserConfirmation(): Boolean {
        return true
    }
    

If you return `true`, your app must obtain (using your own code) the user's
permission and message the SDK with the result using the following API:

    
    
    // Depending on the user's choice, call Crashes.notifyUserConfirmation() with the right value.
    Crashes.notifyUserConfirmation(Crashes.DONT_SEND);
    Crashes.notifyUserConfirmation(Crashes.SEND);
    Crashes.notifyUserConfirmation(Crashes.ALWAYS_SEND);
    
    
    
    Crashes.notifyUserConfirmation(Crashes.DONT_SEND)
    Crashes.notifyUserConfirmation(Crashes.SEND)
    Crashes.notifyUserConfirmation(Crashes.ALWAYS_SEND)
    

As an example you can refer to [our custom dialog
example](https://aka.ms/custom-dialog-android).

### Get information about the sending status for a crash log

At times, you want to know the status of your app crash. A common use case is
that you might want to show UI that tells the users that your app is
submitting a crash report, or, in case your app is crashing quickly after the
launch, you want to adjust the behavior of the app to make sure the crash logs
can be submitted. App Center Crashes has three different callbacks that you
can use in your app to be notified of what's going on:

#### The following callback will be invoked before the SDK sends a crash log

    
    
    @Override
    public void onBeforeSending(ErrorReport errorReport) {
        // Your code, e.g. to present a custom UI.
    }
    
    
    
    override fun onBeforeSending(report: ErrorReport?) {
        // Your code, e.g. to present a custom UI.
    }
    

In case we have network issues or an outage on the endpoint, and you restart
the app, `onBeforeSending` is triggered again after process restart.

#### The following callback will be invoked after the SDK sent a crash log
successfully

    
    
    @Override
    public void onSendingSucceeded(ErrorReport report) {
        // Your code, e.g. to hide the custom UI.
    }
    
    
    
    override fun onSendingSucceeded(report: ErrorReport?) {
        // Your code, e.g. to hide the custom UI.
    }
    

#### The following callback will be invoked if the SDK failed to send a crash
log

    
    
    @Override
    public void onSendingFailed(ErrorReport report, Exception e) {
        // Your code goes here.
    }
    
    
    
    override fun onSendingFailed(report: ErrorReport?, e: Exception?) {
        // Your code goes here.
    }
    

Receiving `onSendingFailed` means a non-recoverable error such as a **4xx**
code occurred. For example, **401** means the `appSecret` is wrong.

This callback isn't triggered if it's a network issue. In this case, the SDK
keeps retrying (and also pauses retries while the network connection is down).

### Add attachments to a crash report

You can add binary and text attachments to a crash report. The SDK will send
them along with the crash so that you can see them in App Center portal. The
following callback will be invoked right before sending the stored crash from
previous application launches. It won't be invoked when the crash happens. Be
sure the attachment file **isn't** named `minidump.dmp` as that name is
reserved for minidump files. Here's an example of how to attach text and an
image to a crash:

    
    
    @Override
    public Iterable<ErrorAttachmentLog> getErrorAttachments(ErrorReport report) {
    
        // Attach some text.
        ErrorAttachmentLog textLog = ErrorAttachmentLog.attachmentWithText("This is a text attachment.", "text.txt");
    
        // Attach binary data.
        byte[] binaryData = getYourBinary();
        ErrorAttachmentLog binaryLog = ErrorAttachmentLog.attachmentWithBinary(binaryData, "your_filename.jpeg", "image/jpeg");
    
        // Return attachments as list.
        return Arrays.asList(textLog, binaryLog);
    }
    
    
    
    override fun getErrorAttachments(report: ErrorReport?): MutableIterable<ErrorAttachmentLog> {
    
        // Attach some text.
        val textLog = ErrorAttachmentLog.attachmentWithText("This is a text attachment.", "text.txt")
    
        // Attach binary data.
        val binaryData = getYourBinary()
        val binaryLog = ErrorAttachmentLog.attachmentWithBinary(binaryData, "your_filename.jpeg", "image/jpeg")
    
        // Return attachments as list.
        return listOf(textLog, binaryLog)
    }
    

Note

The size limit is currently 7 MB. Attempting to send a larger attachment will
trigger an error.

## Enable or disable App Center Crashes at runtime

You can enable and disable App Center Crashes at runtime. If you disable it,
the SDK won't do any crash reporting for the app.

    
    
    Crashes.setEnabled(false);
    
    
    
    Crashes.setEnabled(false)
    

To enable App Center Crashes again, use the same API but pass `true` as a
parameter.

    
    
    Crashes.setEnabled(true);
    
    
    
    Crashes.setEnabled(true)
    

The state is persisted in the device's storage across application launches.

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](../other-apis/android) guide.

Note

This method must only be used after `Crashes` has been started.

## Check if App Center Crashes is enabled

You can also check if App Center Crashes is enabled or not:

    
    
    Crashes.isEnabled();
    
    
    
    Crashes.isEnabled()
    

This API is asynchronous, you can read more about that in our [App Center
Asynchronous APIs](../other-apis/android) guide.

Note

This method must only be used after `Crashes` has been started, it will always
return `false` before start.

## Handled Errors

App Center also allows you to track errors by using handled exceptions. To do
so, use the `trackError` method:

    
    
    try {
        // your code goes here.
    } catch (Exception exception) {
        Crashes.trackError(exception);
    }
    
    
    
    try {
        // your code goes here.
    } catch (exception: Exception) {
        Crashes.trackError(exception)
    }
    

An app can optionally attach properties to a handled error report to provide
further context. Pass the properties as a map of key/value pairs (strings
only) as shown in the example below.

    
    
    try {
        // your code goes here.
    } catch (Exception exception) {
        Map<String, String> properties = new HashMap<String, String>() {{
            put("Category", "Music");
            put("Wifi", "On");
        }};
        Crashes.trackError(exception, properties, null);
    }
    
    
    
    try {
        // your code goes here.
    } catch (exception: Exception) {
        val properties = mapOf("Category" to "Music", "Wifi" to "On")
        Crashes.trackError(exception, properties, null)
    }
    

You can also optionally add binary and text attachments to a handled error
report. Pass the attachments as an `Iterable` as shown in the example below.

    
    
    try {
        // your code goes here.
    } catch (Exception exception) {
    
        // Attach some text.
        ErrorAttachmentLog textLog = ErrorAttachmentLog.attachmentWithText("This is a text attachment.", "text.txt");
    
        // Attach binary data.
        byte[] binaryData = getYourBinary();
        ErrorAttachmentLog binaryLog = ErrorAttachmentLog.attachmentWithBinary(binaryData, "your_filename.jpeg", "image/jpeg");
    
        // Track an exception with attachments.
        Crashes.trackError(exception, null, Arrays.asList(textLog, binaryLog));
    }
    
    
    
    try {
        // your code goes here.
    } catch (exception: Exception) {
    
        // Attach some text.
        val textLog = ErrorAttachmentLog.attachmentWithText("This is a text attachment.", "text.txt")
    
        // Attach binary data.
        val binaryData = getYourBinary()
        val binaryLog = ErrorAttachmentLog.attachmentWithBinary(binaryData, "your_filename.jpeg", "image/jpeg")
    
        // Track an exception with attachments.
        Crashes.trackError(exception, null, listOf(textLog, binaryLog))
    }
    

## Reporting NDK crashes

### Reporting crashes

To receive proper crash reports in App Center, first make sure you have the
App Center Crashes SDK set up by following the instructions listed above.

#### Building the breakpad library

Next, include and compile Google Breakpad by following the instructions listed
in the official [Google Breakpad for Android
README](https://github.com/google/breakpad/blob/master/README.ANDROID).

Note

The App Center SDK doesn't bundle Google Breakpad by default.

#### Attaching the exception handler

Once you have Google Breakpad included, attach the NDK Crash Handler after
`AppCenter.start`:

    
    
    // Attach NDK Crash Handler after SDK is initialized.
    Crashes.getMinidumpDirectory().thenAccept(new AppCenterConsumer<String>() {
        @Override
        public void accept(String path) {
    
            // Path is null when Crashes is disabled.
            if (path != null) {
                setupNativeCrashesListener(path);
            }
        }
    });
    

The method `setupNativeCrashesListener` is a native method that you must
implement in C/C++:

    
    
    #include "google-breakpad/src/client/linux/handler/exception_handler.h"
    #include "google-breakpad/src/client/linux/handler/minidump_descriptor.h"
    
    void Java_com_microsoft_your_package_YourActivity_setupNativeCrashesListener(
            JNIEnv *env, jobject, jstring path) {
        const char *dumpPath = (char *) env->GetStringUTFChars(path, NULL);
        google_breakpad::MinidumpDescriptor descriptor(dumpPath);
        new google_breakpad::ExceptionHandler(descriptor, NULL, dumpCallback, NULL, true, -1);
        env->ReleaseStringUTFChars(path, dumpPath);
    }
    

Where `dumpCallback` is used for troubleshooting:

    
    
    /*
     * Triggered automatically after an attempt to write a minidump file to the breakpad folder.
     */
    bool dumpCallback(const google_breakpad::MinidumpDescriptor &descriptor,
                      void *context,
                      bool succeeded) {
    
        // Allow system to log the native stack trace.
        __android_log_print(ANDROID_LOG_INFO, "YourLogTag",
                            "Wrote breakpad minidump at %s succeeded=%d\n", descriptor.path(),
                            succeeded);
        return false;
    }
    

Once these methods are properly set up, the app sends the minidump to App
Center automatically upon restart. To troubleshoot, you can use verbose logs
(`AppCenter.setLogLevel(Log.VERBOSE)` before `AppCenter.start`) to check if
minidumps are sent after the app is restarted.

Note

App Center uses the reserved name `minidump.dmp` for minidump attachments.
Make sure to give your attachment a different name unless it's a minidump file
so we can handle it properly.

Note

There's a known bug in breakpad which makes it impossible to capture crashes
on x86 emulators.

### Symbolication

See the [Diagnostics documentation](../../diagnostics/android-ndk) for more
information regarding the processing of crashes.

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

