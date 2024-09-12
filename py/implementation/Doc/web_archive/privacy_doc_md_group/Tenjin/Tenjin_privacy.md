[
![Tenjin](//cdn.document360.io/logo/c76013a0-ead2-4f6f-b719-916d141054ef/967b0f50d722471b8c53fcedc0a548c6-knowledge
base_dark \(1\) \(1\).png) ](//www.tenjin.com/)

  * [Dashboard](//www.tenjin.com/dashboard)

  * [ __](/v1/en)
  * [__](/docs/en/whats-newx)
  * English

    * [ English ](/docs/en/android-sdk "en")
    * [ Chinese ](/docs/zh/android-sdk "zh")
    * [ Ja - 日本語 ](/docs/ja/android-sdk "ja")

Contents x

  * [ For Marketers  ]()
  * [ For Developers  ](ios-sdk)
  * [ General  ](account-creation)
  * [ The Tenjin Help Center Glossary  ](a)
  * [ FAQ Center  ](attribution-faq)

* * *

Android SDK

  *  __02 Aug 2024
  *  __ 15 Minutes to read 

Share this __

  * __ Print

  *  __ Share

  *  __ Dark

 __ Light

 __Contents

# Android SDK

  *  __Updated on 02 Aug 2024
  *  __ 15 Minutes to read 

  * __ Print

  *  __ Share

  *  __ Dark

 __ Light

* * *

Article summary

 __

Did you find this summary helpful? __ __ __ __

__

Thank you for your feedback

## [Get Started with the Android SDK](/docs/android-sdk#get-started-with-the-
android-sdk)

The Tenjin Android SDK allows users to track events and installs in their
Android apps. To learn more about Tenjin and our product offering, please
visit https://www.tenjin.com.

  * Please see our [Release Notes](//github.com/tenjin/tenjin-android-sdk/blob/master/RELEASE_NOTES.md) to see detailed version history of changes.
  * We recommend using the latest version of [Android Studio](//developer.android.com/studio/index.html).
  * For Unity integration, please visit https://github.com/tenjin/tenjin-unity-sdk.
  * For any issues or support, please contact: support@tenjin.com.

* * *

## [Table of contents](/docs/android-sdk#table-of-contents)

  * Basic Integration
    * Google Play or Amazon store
      * Permissions
      * Android Advertising ID (AAID)
      * App Store
      * App Initialization
    * Android other store
      * Permissions
      * Android Advertising ID (AAID)
      * OAID
        * MSA OAID
        * Huawei OAID
        * Huawei Install Referrer
      * App Store
      * App Initialization
    * Proguard settings
  * Additional Integration
    * GDPR
      * Opt in/Opt out using CMP consents
    * Purchase Events
    * Custom Events
    * Server-to-server integration
    * App Subversion
    * LiveOps Campaigns
    * Customer User ID
    * Analytics Installation ID
    * Retry/cache of events/IAP
    * Impression Level Ad Revenue Integration
    * Google DMA parameters
  * Testing

* * *

## [Basic Integration](/docs/android-sdk#basic-integration)

#### Manual Installation

Please use the steps listed below under the section 'Android Studio.'

#### Maven

If you use Maven, add implementation `com.tenjin:android-sdk:VERSION` to your
`Gradle` dependencies and add `mavenCentral()` to the source repositories if
it’s not there already.

### [Android Studio](/docs/android-sdk#android-studio)

  1. Download the latest Android SDK from [here.](//github.com/tenjin/tenjin-android-sdk/releases)

  2. Add the Tenjin SDK into your Android Studio project. Go to the Project Navigator in Android Studio. Select the option `Project` in the Project Navigator. You will find the `libs` folder under the `app` module of your Android Studio project.

  3. You need to add the file `tenjin.jar` or `tenjin.aar` to the `libs` folder.  
![AndroidStudio](//tenjin-instructions.s3.amazonaws.com/android_jar.png)

  4. In your Android Studio project under `app` module, select the `build.gradle` file, and add the following under the dependencies block:
    
        dependencies {
        implementation fileTree(dir: 'libs', include: ['*.jar', '*.aar'])
        implementation files('libs/tenjin.aar')
    }
    

> We have a demo project - [tenjin-android-sdk-
> demo](//github.com/tenjin/tenjin-android-sdk-demo) that demonstrates the
> integration of tenjin-android-sdk. You can this project as example to
> understand how to integrate the tenjin-android-sdk.

* * *

### [Google Play or Amazon store](/docs/android-sdk#google-play-or-amazon-
store)

If you distribute your apps on Google Play Store or Amazon store, implement
the following initial setups.

#### [Permission](/docs/android-sdk#permission)

The Tenjin SDK requires the following permissions:

    
    
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /> <!-- Required to get network connectivity (i.e. wifi vs. mobile) -->
    

Google Play Services requires all API level 32 (Android 13) apps using the
advertising_id(Android Advertising ID (AAID)) to declare the Google Play
Services AD_ID permission (shown below) in their manifest file. **Please add
this permission as soon as possible.** You are also required to update the
tenjin-android-sdk to version 1.12.8 in order to use the below permission.

    
    
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>
    

#### [Android Advertising ID (AAID) and Install Referrer](/docs/android-
sdk#android-advertising-id-aaid-and-install-referrer)

Add [Android Advertising ID
(AAID)](//developers.google.com/android/guides/setup#list-dependencies) and
[Install
Referrer](//developer.android.com/google/play/installreferrer/library)
libraries, add it to your build.gradle file.

    
    
    dependencies {
      implementation 'com.google.android.gms:play-services-ads-identifier:{version}'
      implementation 'com.android.installreferrer:installreferrer:{version}'
    }
    

To be able to collect [Meta's Install
Referrer,](//developers.facebook.com/docs/app-ads/meta-install-referrer/) add
these queries to your Android Manifest:

    
    
    <queries>
      <package android:name="com.facebook.katana" />
    </queries>
    
    <queries>
      <package android:name="com.instagram.android" />
    </queries>
    

If you haven't set up Facebook's SDK (Meta) yet, add the following to your
AndroidManifest.xml file:

    
    
    <meta-data android:name="com.facebook.sdk.ApplicationId" android:value="@string/facebook_app_id" />
    

Next, add this value to your strings.xml file:

    
    
    <string name="facebook_app_id" translatable="false">YOUR_APP_ID</string>
    

#### [App Store](/docs/android-sdk#app-store)

By default, **unspecified** is the default App Store. Update the app store
value to either **googleplay** or **amazon** , depending on your app.

  1. `AndroidManifest.xml`:

    
    
    <meta-data
        android:name="TENJIN_APP_STORE"
        android:value="googleplay" />
    

  2. `setAppStore()`:

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    
    instance.setAppStore(TenjinSDK.AppStoreType.googleplay);
    

#### App Store Options

    
    
      TenjinSDK.AppStoreType.googleplay // Google Play App Store
      TenjinSDK.AppStoreType.amazon     // Amazon AppStore
      TenjinSDK.AppStoreType.other      // Other
    

* * *

#### [App Initialization](/docs/android-sdk#app-initialization)

  1. Get your `SDK_KEY` from your app page. Note: `SDK_KEY` is unique for each of your app. You can create up to 3 keys for the same app.  
![app_api_key.png](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/app_api_key%281%29.png)

  2. In your Activity, import Tenjin: `import com.tenjin.android.TenjinSDK;`

  3. In the `onResume` method of your main `Activity` class, add the following line of code:

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    
    instance.connect();
    

**NOTE:** If your app has the logic to ask user's consent between `onCreate`
and `onResume`, use `onCreate` instead of `onResume` for Tenjin SDK
initialization because users who don't consent won't be tracked on `onResume`.

**NOTE:** Please ensure you implement this code on every `onResume`, not only
on the first app open of the app. If we notice that you don't follow our
recommendation, we can't give you proper support or your account might be
suspended.

* * *

### [Other Android store](/docs/android-sdk#other-android-store)

If you distribute your apps outside of Google Play Store or Amazon store(Other
Android store), implement the following initial setups.

#### [Permission](/docs/android-sdk#permission1)

    
    
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" /> <!-- Required to get network connectivity (i.e. wifi vs. mobile) -->
    

Later this year, Google Play Services will require all API level 32 (Android
13) apps using the advertising_id(Android Advertising ID (AAID)) to declare
the Google Play Services AD_ID permission (shown below) in their manifest
file. **Please add this permission as soon as possible.** You are also
required to update the tenjin-android-sdk to version 1.12.8 in order to use
the below permission.

    
    
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>
    

#### [Android Advertising ID (AAID) and Install Referrer](/docs/android-
sdk#android-advertising-id-aaid-and-install-referrer1)

Add [Android Advertising ID
(AAID)](//developers.google.com/android/guides/setup#list-dependencies) and
[Install
Referrer](//developer.android.com/google/play/installreferrer/library)
libraries, add it to your build.gradle file.

    
    
    dependencies {
      implementation 'com.google.android.gms:play-services-ads-identifier:{version}'
      implementation 'com.android.installreferrer:installreferrer:{version}'
    }
    

If you are using an [Ad Network](//tenjin.com/blog/best-ad-networks-to-
advertise-hybrid-hyper-casual-games-in-2024/) that targets the IMEI, you will
need to add the following permissions enabled. (If you are distributing your
apps in Google Play, please **DO NOT** add this permission.)

    
    
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    

#### [OAID](/docs/android-sdk#oaid)

Tenjin supports promoting your app on other Android App Stores using the
Android OAID. We have the following requirements for integrating OAID
libraries.

#### [MSA OAID](/docs/android-sdk#msa-oaid)

MSA OAID is an advertising ID for devices manufactured in China that the MSA
(Mobile Security Alliance) provides. For integration with the [MSA
library](http://www.msa-alliance.cn/col.jsp?id=120), download the following
[oaid_sdk_1.0.25.aar](//github.com/tenjin/tenjin-android-sdk/blob/master/msa-
oaid/oaid_sdk_1.0.25.aar) and
[supplierconfig.json](//github.com/tenjin/tenjin-android-sdk/blob/master/msa-
oaid/supplierconfig.json).

Add the following to your project gradle file:

    
    
    implementation files('libs/oaid_sdk_1.0.25.aar')
    

Be sure to copy the [supplierconfig.json](//github.com/tenjin/tenjin-android-
sdk/blob/master/msa-oaid/supplierconfig.json) file to the `assets` folder of
your project.

#### [Huawei OAID](/docs/android-sdk#huawei-oaid)

For outside of China, you can collect OAID using the library provided by
Huawei. For integration with the [Huawei OAID
library](//developer.huawei.com/consumer/en/codelab/HMSAdsOAID/index.html#3),
add the following to your project:

In your `build.gradle` file, add the Maven address for the Huawei SDKs:

    
    
    allprojects {
        repositories {
            google()
            maven { url 'https://developer.huawei.com/repo/' }
        }
    }
    
    
    
    dependencies {
        implementation 'com.huawei.hms:ads-identifier:{version}'
    }
    

#### [Huawei Install Referrer](/docs/android-sdk#huawei-install-referrer)

If you are marketing your app with [Huawei App
Gallery](//appgallery.huawei.com/), add both the `Huawei OAID` SDK from above
and the [Install
Referrer](//developer.huawei.com/consumer/en/codelab/HMSAdsTransformOAID/index.html#3)
library.

    
    
    dependencies {
    
        implementation 'com.huawei.hms:ads-identifier:{version}'
        implementation 'com.huawei.hms:ads-installreferrer:{version}'
    
    }
    

* * *

#### [App Store](/docs/android-sdk#app-store1)

By default, **unspecified** is the default App Store. Update the app store
value to **other**.

  1. `AndroidManifest.xml`:

    
    
    <meta-data
        android:name="TENJIN_APP_STORE"
        android:value="other" />
    

  2. `setAppStore()`:

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    
    instance.setAppStore(TenjinSDK.AppStoreType.other);
    

* * *

#### [App Initialization](/docs/android-sdk#app-initialization1)

  1. Get your `SDK_KEY` from your app page. Note: `SDK_KEY` is unique for each of your app. You can create up to 3 keys for the same app.  
![app_api_key.png](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/app_api_key%281%29.png)

  2. In your Activity, import Tenjin: `import com.tenjin.android.TenjinSDK;`

  3. In the `onCreate` method of your main `Activity` class, add the following line of code:

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    
    instance.connect();
    

**NOTE:** Please ensure you implement this code on every `onCreate`, not only
on the first app open of the app. If we notice that you don't follow our
recommendation, we can't give you proper support or your account might be
suspended.

* * *

### [Proguard Settings](/docs/android-sdk#proguard-settings)

    
    
    -keep class com.tenjin.** { *; }
    -keep public class com.google.android.gms.ads.identifier.** { *; }
    -keep public class com.google.android.gms.common.** { *; }
    -keep public class com.android.installreferrer.** { *; }
    -keep class * extends java.util.ListResourceBundle {
        protected java.lang.Object[][] getContents();
    }
    -keepattributes *Annotation*
    

Do not obfuscate oaid classes:

    
    
    -keep class XI.CA.XI.**{*;}
    -keep class XI.K0.XI.**{*;}
    -keep class XI.XI.K0.**{*;}
    -keep class XI.xo.XI.XI.**{*;}
    -keep class com.asus.msa.SupplementaryDID.**{*;}
    -keep class com.asus.msa.sdid.**{*;}
    -keep class com.bun.lib.**{*;}
    -keep class com.bun.miitmdid.**{*;}
    -keep class com.huawei.hms.ads.identifier.**{*;}
    -keep class com.samsung.android.deviceidservice.**{*;}
    -keep class com.zui.opendeviceidlibrary.**{*;}
    -keep class org.json.**{*;}
    -keep public class com.netease.nis.sdkwrapper.Utils {public <methods>;}
    

If you are using Huawei libraries, you can to use these setttings:

    
    
    -keep class com.huawei.hms.ads.** { *; }
    -keep interface com.huawei.hms.ads.** { *; }
    

* * *

## [Additional Integration](/docs/android-sdk#additional-integration)

### [GDPR](/docs/android-sdk#gdpr)

The General Data Protection Regulation (EU) (GDPR) is a regulation in EU law
on data protection and privacy in the European Union (EU) and the European
Economic Area (EEA).

You need to get user consent whether they allow tracking or not in first ap
open, then write the result into `checkOptInValue()` . After that, you can
follow the inetgration as below. If you do not need to be GDPR compliant in
your App, please just ignore this whole section.

As part of GDPR compliance, with Tenjin's SDK you can opt-in, opt-out
devices/users, or select which specific device-related params to opt-in or
opt-out. `optOut()` will not send any API requests to Tenjin, and we will not
process any events.

To opt-in/opt-out:

    
    
    import com.tenjin.android.TenjinSDK;
    
    public class TenjinDemo extends ActionBarActivity {
        @Override
        public void onResume() {
            //standard code
            super.onResume()
    
            //Integrate TenjinSDK connect call
            String apiKey = "<SDK_KEY>";
            TenjinSDK instance = TenjinSDK.getInstance(this, apiKey);
    
            boolean userOptIn = checkOptInValue();
    
            if (userOptIn) {
                instance.optIn();
            }
            else {
                instance.optOut();
            }
    
            instance.connect();
    
            //Your other code...
            //...
    
        }
    
        protected boolean checkOptInValue(){
            // check opt-in value
            // return true; // if user opted-in
            return false;
        }
    }
    

To opt-in/opt-out specific device-related parameters, you can use
`optInParams()` or `optOutParams()`.

  * `optInParams()` will only send device-related parameters that are specified. `optOutParams()` will send all device-related parameters except ones that are specified.

  * Kindly note that we require the following parameter to properly track devices in Tenjin's system. If the mandatory parameter is missing, the event will not be processed or recorded.

    * `advertising_id`
  * If you are targeting IMEI and/or OAID [Ad Networks](//tenjin.com/blog/best-ad-networks-to-advertise-hybrid-hyper-casual-games-in-2024/), these params are required:

    * `imei`
    * `oaid`
  * If you intend to use Google AdWords, these params are required:

    * `platform`
    * `os_version`
    * `app_version`
    * `locale`
    * `device_model`
    * `build_id`

If you want to only get specific device-related parameters, use
`optInParams()`. In example below, we will only these device-related
parameters: `ip_address`, `advertising_id`, `limit_ad_tracking`, and
`referrer`.

    
    
    String apiKey = "<SDK_KEY>";
    TenjinSDK instance = TenjinSDK.getInstance(this, apiKey);
    
    String[] optInParams = {"ip_address", "advertising_id", "limit_ad_tracking", "referrer"};
    instance.optInParams(optInParams);
    
    instance.connect();
    

If you want to send ALL parameters except specific device-related parameters,
use `optOutParams()`. In the example below, we will send ALL device-related
parameters except:

    
    
    String apiKey = "<SDK_KEY>";
    TenjinSDK instance = TenjinSDK.getInstance(this, apiKey);
    
    String[] optOutParams = {"locale", "timezone", "build_id"};
    instance.optOutParams(optOutParams);
    
    instance.connect();
    

## [Opt in/out using CMP ](/docs/android-sdk#opt-inout-using-cmp)

You can automatically opt in or opt out using your CMP consents (purpose 1)
which are already saved in the user's device. The method returns a boolean to
let you know if it's opted in or out.

`optInOutUsingCMP()`

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    optInOut = instance.optInOutUsingCMP(); 
    

* * *

### [Device-Related Parameters](/docs/android-sdk#devicerelated-parameters)

Param| Description| Reference  
---|---|---  
ip_address| IP Address|  
advertising_id| Device Advertising ID|
[Android](//developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient.html#getAdvertisingIdInfo\(android.content.Context\))  
limit_ad_tracking| limit ad tracking enabled|
[Android](//developers.google.com/android/reference/com/google/android/gms/ads/identifier/AdvertisingIdClient.Info.html#isLimitAdTrackingEnabled\(\))  
oaid| Open Advertising ID| [Android](http://www.msa-
alliance.cn/col.jsp?id=120)  
imei| Device IMEI|
[Android](//developer.android.com/reference/android/telephony/TelephonyManager#getImei\(\))  
platform| Platform| Android  
referrer| Google Play Install Referrer|
[Android](//developer.android.com/google/play/installreferrer/index.html)  
os_version| operating system version|
[Android](//developer.android.com/reference/android/os/Build.VERSION.html#SDK_INT)  
device| device name|
[Android](//developer.android.com/reference/android/os/Build.html#DEVICE)  
device_manufacturer| device manufacturer|
[Android](//developer.android.com/reference/android/os/Build.html#MANUFACTURER)  
device_model| device model|
[Android](//developer.android.com/reference/android/os/Build.html#MODEL)  
device_brand| device brand|
[Android](//developer.android.com/reference/android/os/Build.html#BRAND)  
device_product| device product|
[Android](//developer.android.com/reference/android/os/Build.html#PRODUCT)  
carrier| phone carrier|
[Android](//developer.android.com/reference/android/telephony/TelephonyManager.html#getSimOperatorName\(\))  
connection_type| cellular or wifi|
[Android](//developer.android.com/reference/android/net/ConnectivityManager.html#getActiveNetworkInfo\(\))  
screen_width| device screen width|
[Android](//developer.android.com/reference/android/util/DisplayMetrics.html#widthPixels)  
screen_height| device screen height|
[Android](//developer.android.com/reference/android/util/DisplayMetrics.html#heightPixels)  
os_version_release| operating system version|
[Android](//developer.android.com/reference/android/os/Build.VERSION.html#RELEASE)  
build_id| build ID|
[Android](//developer.android.com/reference/android/os/Build.html)  
locale| device locale|
[Android](//developer.android.com/reference/java/util/Locale.html#getDefault\(\))  
country| locale country|
[Android](//developer.android.com/reference/java/util/Locale.html#getDefault\(\))  
timezone| timezone|
[Android](//developer.android.com/reference/java/util/TimeZone.html)  
  
  

* * *

### [Purchase Events](/docs/android-sdk#purchase-events)

To understand user revenue and purchase behavior, developers can send
`transaction` events to Tenjin. Tenjin will validate `transaction` receipts
for you. Kindly note that we currently only support IAP transactions from
Google Play.

**IMPORTANT:** You will need to add your app's public key in the [Tenjin
dashboard](//www.tenjin.com/dashboard/apps) (under the app 'edit' page). You
can retrieve your Base64-encoded RSA public key from the [ Google Play
Developer Console](//play.google.com/apps/publish/) > Select your app >
Monetize > Monetization setup > Google Play Billing > Licensing:
Base64-encoded RSA public key. Please note that for Android, we currently only
support IAP transactions from Google Play.

  
  
![image.png](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/image%28404%29.png)

  
  
  
  
After entering your Public Key into the Tenjin dashboard for your app, you can
use the Tenjin SDK method below:

    
    
    public void transaction(String productId, String currencyCode, int quantity, double unitPrice, String purchaseData, String dataSignature)
    

Example:

    
    
    public void sendPurchaseEvent(Purchase purchase, Double price, String currencyCode) {
        String sku = purchase.getSku();
        String purchaseData = purchase.getOriginalJson();
        String dataSignature = purchase.getSignature();
    
        TenjinSDK instance = getTenjinInstance();
        instance.transaction(sku, currencyCode, 1, price, purchaseData, dataSignature);
    }
    
    

You can verify if the IAP validation is working through our [Live Test Device
Data Tool](//www.tenjin.com/dashboard/sdk_diagnostics). You should see a live
event come in:

  
  
![](//s3.amazonaws.com/tenjin-instructions/sdk_live_purchase_events_2.png)  
  

**Disclaimer:** If you are implementing purchase events on Tenjin for the
first time, make sure to verify the data with other tools you’re using before
you start scaling up your user acquisition campaigns using purchase data.

NOTE

Please ensure to 'acknowledge' the purchase event before sending it to Tenjin.
For more details, read
[here](//developer.android.com/google/play/billing/integrate#non-consumable-
products)

Flexible App Store Commission setup

Choose between 15% and 30% App Store’s revenue commission via our new setup.
The steps are -

  * Go to CONFIGURE --> Apps
  * Click on the app you want to change it for
  * Under the ‘App Store Commission’ section click ‘Edit’
  * Choose 30% or 15% as your desired app store commission.
  * Select the start date and end date (Or you can keep the end date blank if you dont want an end date)
  * Click Save (note: the 15% commission can be applied only to dates moving forward and not historical dates. So please set the start date from the date you make the change and forward)

**Amazon AppStore**

Amazon AppStore receipt validation requires `receiptId` and `userId`
parameters.

**IMPORTANT:** You will need to add your Amazon app's Shared Key in the
[Tenjin dashboard](//www.tenjin.io/dashboard/apps). The shared secret can be
found on the Shared Key in your developer account with the [Amazon Appstore
account](//developer.amazon.com/settings/console/sdk/shared-key/)

* * *

### [Custom Events](/docs/android-sdk#custom-events)

**NOTE:** The initialization event `connect()` must come before sending any
custom events.

You can use the Tenjin SDK to pass a custom event: `eventWithName(String
name)`.

The custom interactions with your app can be tied to level cost from each
acquisition source that you use through Tenjin's service. Here is an example
of usage:

    
    
    String apiKey = <SDK_KEY>;
    TenjinSDK instance = TenjinSDK.getInstance(this, apiKey);
    
    //Integrate a custom event with a distinct name - ie. swiping right on the screen
    instance.eventWithName("swipe_right");
    
    

* * *

### [Custom Events with values](/docs/android-sdk#custom-events-with-values)

You can use the Tenjin SDK to pass a custom event with an integer value:
`eventWithNameAndValue(String name, int value)`.

Passing an integer `value` with an event's `name` allows marketers to sum up
and track averages of the values passed for that metric in the Tenjin
dashboard. If you plan to use DataVault, these values can be used to derive
additional metrics that can be useful.

    
    
    String apiKey = <SDK_KEY>;
    TenjinSDK.instance = TenjinSDK.getInstance(this, apiKey);
    
    //Integrate a custom event with a distinct name and value - ie. paying 100 virtual coins for an item
    instance.eventWithNameAndValue("item", 100);
    

Using the example above, the Tenjin dashboard will sum and average the values
for all events with the name `item`.

Keep in mind that this event will not work if the value passed not an integer.

    
    
    //Integrate a custom event with a distinct name and value - ie. paying 100 virtual coins for an item
    instance.eventWithNameAndValue("item", "1");
    

* * *

### [Server-to-server integration](/docs/android-sdk#servertoserver-
integration)

Tenjin offers server-to-server integration. This allows you to send your
install and post-install events directly from your servers to Tenjin servers
without needing an SDK integration. If you want to access to the
documentation, please send email to support@tenjin.com.

* * *

### [App Subversion parameter for A/B Testing (requires
DataVault)](/v1/docs/android-sdk#app-subversion-parameter-for-ab-testing-
requires-datavault)

If you are running A/B tests and want to report the differences, we can append
a numeric value to your app version using the `appendAppSubversion()` method.
For example, if your app version `1.0.1`, and set `appendAppSubversion(8888)`,
it will report app version as `1.0.1.8888`.

This data will appear within DataVault, where you will be able to run reports
using the app subversion values.

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    instance.appendAppSubversion(8888);
    instance.connect();
    

* * *

### [LiveOps Campaigns](/docs/android-sdk#liveops-campaigns)

Tenjin supports retrieving of user attribution information, like sourcing [ad
network](//tenjin.com/blog/best-ad-networks-to-advertise-hybrid-hyper-casual-
games-in-2024/) and campaign, from the SDK. This will allow developers to
collect and analyze user-level attribution data in real-time. Here are the
possible use cases using Tenjin LiveOps Campaigns:

  * If you have your own data anlytics tool, custom callback will allow you to tie the attribution data to your in-game data per device level.
  * Show different app content depending on where the user comes from. For example, if user A is attributed to organic and user B is attributed to Facebook and user B is likely to be more engaged with your app, then you want to show a special in-game offer after the user installs the app. If you want to discuss more specific use cases, please write to support@tenjin.com.

NOTE: LiveOps Campaigns is a paid feature, so please contact your Tenjin
account manager if you would like to get access.

* * *

### [Customer User ID](/docs/android-sdk#customer-user-id)

You can set and get customer user id to send as a parameter on events.

`.setCustomerUserId(userId: "user_id")`

`.getCustomerUserId()`

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    instance.setCustomerUserId(userId: "user_id");
    userId = instance.getCustomerUserId(); 
    

## [Analytics Installation ID](/docs/android-sdk#analytics-installation-id)

You can get the analytics id which is generated randomly and saved in the
local storage of the device.  
`getAnalyticsInstallationId()`

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    analyticsId = instance.getAnalyticsInstallationId; 
    

* * *

## [Retry Cache](/docs/android-sdk#retry-cache)

You can enable/disable retrying and caching events and IAP when requests fail
or users don't have internet connection. These events will be sent after a new
event has been added to the queue and user has recovered connection.

`.setCacheEventSetting(setting: true)`

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    instance.setCacheEventSetting(setting: true);
    

* * *

### [Impression Level Ad Revenue Integration](/docs/android-sdk#impression-
level-ad-revenue-integration)

Tenjin supports the ability to integrate with the Impression Level Ad Revenue
(ILRD) feature from,

  * AppLovin
  * Unity LevelPlay
  * HyperBid
  * AdMob
  * TopOn
  * CAS
  * TradPlus

This feature allows you to receive events which correspond to your ad revenue
is affected by each advertisement show to a user. To enable this feature,
follow the below instructions.

NOTE: ILRD is a paid feature, so please contact your Tenjin account manager to
discuss the price before sending ILRD events.

* * *

### [Google DMA Parameters](/docs/android-sdk#google-dma-parameters)

**If you already have a CMP integrated, Google DMA parameters will be
automatically collected by the Tenjin SDK. There’s nothing to implement in the
Tenjin SDK if you have a CMP integrated**. If you want to override your CMP,
or simply want to build your own consent mechanisms, you can use the
following:

`setGoogleDMAParameters(boolean, boolean)`

    
    
    TenjinSDK instance = TenjinSDK.getInstance(this, "<SDK_KEY>");
    instance.setGoogleDMAParameters(adPersonalization, adUserData); 
    

To explicitly manage the collection of Google DMA parameters, you have the
flexibility to opt in or opt out at any time. While the default setting is to
opt in, you can easily adjust your preferences using the optInGoogleDMA or
optOutGoogleDMA methods, ensuring full control over your data privacy
settings:

    
    
    instance.optInGoogleDMA(); 
    instance.optOutGoogleDMA(); 
    

* * *

## [Testing](/docs/android-sdk#testing)

You can verify if the integration is working through our [Live Test Device
Data Tool](//www.tenjin.com/dashboard/sdk_diagnostics). Add your
`advertising_id` or `IDFA/GAID` to the list of test devices. You can find this
under Support -> [Test Devices](//www.tenjin.com/dashboard/debug_app_users).
Go to the [SDK Live page](//www.tenjin.com/dashboard/sdk_diagnostics) and send
the test events from your app. You should see live events come in:

![](//s3.amazonaws.com/tenjin-instructions/sdk_live_purchase_events_2.png)

* * *

* * *

Was this article helpful?

__Yes __No

 __

Thank you for your feedback! Our team will get back to you

How can we improve this article?

Your feedback

Need more information

Difficult to understand

Inaccurate or irrelevant content

Missing/broken link

Others

Comment

Comment (Optional)

Character limit : 500

Please enter your comment

Email (Optional)

Email

Notify me about change  

Please enter a valid email

Cancel

* * *

###### What's Next

  * [ Unity SDK ](/docs/unity-sdk) __

Table of contents

    * Get Started with the Android SDK 
    * Table of contents 
    * Basic Integration 
    * Additional Integration 
    * Opt in/out using CMP 
    * Analytics Installation ID 
    * Retry Cache 
    * Testing 

[ ![Tenjin
Logo](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/Tenjin%20logo.svg)
](//tenjin.com/)

[Homepage](//tenjin.com/)

[Blog](//tenjin.com/blog/)

[Pricing](//tenjin.com/pricing/)

[Terms](//tenjin.com/terms/)

[Privacy Policy](//tenjin.com/privacy/)

[Contact Us](//tenjin.com/contact-us/)

[
![LinkedIn](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/linked.svg)
](//www.linkedin.com/company/tenjin) [
![Twitter](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/twitter.svg)
](//x.com/tenjinIO) [
![YouTube](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/youtube.svg)
](//www.youtube.com/c/TenjinIO) [
![Facebook](//cdn.document360.io/c76013a0-ead2-4f6f-b719-916d141054ef/Images/Documentation/facebook.png)
](//www.facebook.com/tenjinio/)

**Cookie consent**

By entering and using this site, you consent to the use of only necessary
cookies to enhance your site experience and improve our services.

Accept

__

