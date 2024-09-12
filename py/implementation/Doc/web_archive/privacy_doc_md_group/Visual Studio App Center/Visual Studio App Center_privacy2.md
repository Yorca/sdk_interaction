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

