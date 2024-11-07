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

