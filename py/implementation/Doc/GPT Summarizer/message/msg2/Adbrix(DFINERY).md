SDK name: Adbrix(DFINERY)
Documentation:
![](https://www.facebook.com/tr?id=473345380651706&ev=PageView&noscript=1)

[ ![Logo](/hc/theming_assets/01HZM7C4JZXXAAHFTPJWXR7EWW) HELP CENTER ](/hc/en-
us "Home")

[IGAWORKS BLOG](https://www.igaworksblog.com/) [Go to
Console](https://console.dfinery.io) [Contact
us](https://webforms.pipedrive.com/f/6rJIAsPlCWFDGOhm8dRJEIXGclaEjMkFVpHD4N6AEUQxdXjrxO48tGuJUOjvayCHfR)
[Open Ticket](/hc/en-us/requests/new)

  1. [DFINERY Help Center](/hc/en-us)
  2. [Developer Guide](/hc/en-us/categories/360000018393-Developer-Guide)
  3. [SDK Integrations](/hc/en-us/sections/360003363913-SDK-Integrations)

### Articles in this section

  * [Integrating DFINERY (Adbrix) [Android]](/hc/en-us/articles/360003279994-Integrating-DFINERY-Adbrix-Android)
  * [Integrating Definery (Adbrix) [iOS]](/hc/en-us/articles/900005450503-Integrating-Definery-Adbrix-iOS)
  * [Integrating DFINERY (Adbrix) [Web]](/hc/en-us/articles/900005110403-Integrating-DFINERY-Adbrix-Web)
  * [Integrate DFINERY (Adbrix) - Hybrid App](/hc/en-us/articles/360010205713-Integrate-DFINERY-Adbrix-Hybrid-App)
  * [Integrating DFINERY (Adbrix) [React Native]](/hc/en-us/articles/360033981253-Integrating-DFINERY-Adbrix-React-Native)
  * [Integrating DFINERY (Adbrix) [Flutter]](/hc/en-us/articles/900000507886-Integrating-DFINERY-Adbrix-Flutter)

#  Integrating DFINERY (Adbrix) [Android]

![Avatar](https://help.dfinery.io/system/photos/13327294565785/dfinery_symbol_rgb_color_1_.png)

DFINERY

  * August 24, 2024 03:02
  * Updated

[Follow](/hc/en-us/articles/360003279994-Integrating-DFINERY-Adbrix-
Android/subscription.html "Opens a sign-in dialog")

###  ** **Quick Start** **

We guide you through the minimum integration steps to use DFINERY (Adbrix).

If you follow the guide below and complete [ **Gradle Settings - > Proguard
Settings ** ],

  1. You can check basic indicators such as DAU in the DFINERY (Adbrix) console. 
  2. You can track app install advertisements through tracking links. 

[[인용​:보통:위험]]​  ** **System Requirements  
** ** Definery (Adbrix) Android SDK operates in the following environments.  
1\. Build environment: Android Studio  
2\. Android Min SDK version: 14 or higher

####  ** **Gradle settings** **

DFINERY (Adbrix) supports SDK download and installation through gradle.

It is more convenient to change the View to Android type for Gradle settings.

![mceclip0.png](/hc/article_attachments/360038443774)

Add the following content to the [ **build.gradle (Project: ProjectName)** ]
file.

[[Quote:Risk:Moderate]] 2021.05.03 Bintray service has been terminated.  
We are distributing the library using mavenCentral. Please modify the gradle
settings as follows. Please delete the existing jcenter() as it is no longer
used.

    
    
    **allprojects {**
        repositories {
            google()  
     jcenter() //delete this.
    mavenCentral()
    }
    }

Add dependency to the [ **build.gradle (Module: app)** ] file as follows.

    
    
    android {
        compileOptions {
            sourceCompatibility JavaVersion.VERSION_1_8
            targetCompatibility JavaVersion.VERSION_1_8
        }
    }
    dependencies {
        implementation 'com.google.android.gms:play-services-ads-identifier:18.0.1'
        implementation 'com.android.installreferrer:installreferrer:2.2'  
        implementation 'io.dfinery:android-sdk:2.5.1.2'
    }
    
    //If jetifier cannot be used
    
    android {
        compileOptions {
            sourceCompatibility JavaVersion.VERSION_1_8
            targetCompatibility JavaVersion.VERSION_1_8
        }
    }
    dependencies {
        implementation 'com.google.android.gms:play-services-ads-identifier:18.0.1'
        implementation 'com.android.installreferrer:installreferrer:2.2'
        implementation ( 'io.dfinery:android-sdk:2.5.1.2' ) {  
     exclude group : "com.android.installreferrer"  
     }
    }

[[Quote:Risk:Moderate]] * To prevent fraudulent traffic, be sure to add
**com.android.installreferrer:installreferrer** .  
* To obtain Google Advertising ID and media advertising, you must add **com.google.android.gms:play-services-ads-identifier** . 

# installreferrer If a Java class duplication error occurs, please set the
definition library as follows.

    
    
    implementation ( 'io.dfinery:android-sdk:2.5.1.2' ) {  
       exclude group : "com.android.installreferrer"  
     }

After writing all Gradle scripts, install the SDK through [File > Sync Project
with Gradle Files] in Android Studio.

![mceclip1.png](/hc/article_attachments/360038444194)

####  ** **Required permission settings** **

DFINERY (Adbrix) SDK requires the following permissions.

Set in [ **AndroidManifest.xml > manifest ** ] as follows.

    
    
    <manifest>
    ...
    **< uses-permission android:name="android.permission.INTERNET" />
        <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
        <uses-permission android:name="com.google.android.gms.permission.AD_ID" />**
    ...
    </manifest>

####  ** **SDK initialization** **

There are two ways to initialize the DFINERY (Adbrix) SDK.

Initialize the SDK according to the development environment.

  1. **Using DFINERY (Adbrix) application class**
  2. **Use your own application class**

** **1.Use Definery (Adbrix) application class** **

If you do not have a self-implemented application, you can quickly and easily
initialize the SDK using the application class provided by the DFINERY
(Adbrix) SDK.

Set in [ **AndroidManifest.xml > application ** ] as follows.

    
    
    <application
        android:name="com.igaworks.v2.core.application.AbxApplication"
        ...
        >
      
    <meta-data android:name="AdBrixRmAppKey" android:value="your_adbrix_remastered_app_key" />  
     <meta-data android:name="AdBrixRmSecretKey" android:value="your_adbrix_remastered_secret_key" />
    </application>

** **2.Use your own application class** **

If you have a self-implemented application class, set onCreate() of that class
as follows.

    
    
    <application
           android:name=".MyApplicationClass"
            ...
        >
    
    </application>

Java  Kotlin

    
    
    public class MyApplicationClass extends Application {
    
        @Override
        public void onCreate() {
            super.onCreate();
    
            AdBrixRm.init(this, "your_adbrix_remastered_app_key", "your_adbrix_remastered_secret_key");
      
        }
    }
    
    
    class MyApplicationClass : Application() {
    
        override fun onCreate() {
            super.onCreate()
    
            AdBrixRm.init(this, "your_adbrix_remastered_app_key", "your_adbrix_remastered_secret_key");
    
        }
    }
    

[[Quote:Guide:Normal]] ** Check App Key & Secret Key  **  
App key and secret key are identifiers used by Definery (Adbricks) to
distinguish apps.  
This is a value absolutely necessary for SDK integration. You can check it
after registering the app in the Definery (Adbrix) console.  
_ [ How to check app key and secret key
](https://help.dfinery.io/hc/ko/articles/360006735353)  
_ [ Go to Adbricks console ](https://console.adbrix.io/login)

[[Quote:Guide:Normal]] ** Congratulations!!!  **  
  
Basic integration to use DFINERY (Adbrix) has been completed.  
The available features are as follows:  
1\. Reporting to check indicators such as DAU, MAU, and daily retention  
2\. App introduction campaigns such as NCPI  
  
If you want to analyze events such as purchases that occur within the app, you
can continue linking by referring to the guide below.

* * *

###  
SDK obfuscation exception handling

To ensure that SDK operation and analysis proceed smoothly, we process
obfuscation exceptions as follows.

####  proguard

Please add the code below to app/proguard-rule.pro.

    
    
    -keep class com.google.android.gms.ads.identifier.AdvertisingIdClient {*;}
    -keep class com.google.android.gms.ads.identifier.AdvertisingIdClient$* {*;}
    -dontwarn com.android.installreferrer.**  
     -keep class com.igaworks.v2.** { *; }  
     -keep class abx.** { *; }  
     -keep class io.adbrix.sdk.** { *; }

####  Other obfuscation tools

When using an obfuscation tool other than proguard, please obfuscate the
packages below.

    
    
    com.igaworks.v2.**  
     abx.**  
     io.adbrix.sdk.**

* * *

###  ** Additional SDK settings  **

####  ** **Event upload cycle settings** **

DFINERY (Adbrix) provides two standards for when to upload events to the
DFINERY (Adbrix) server through SDK.

  1. Based on cumulative event count 
  2. based on time 

[[Quote:Information:Danger]] Of the two criteria, the upload will proceed
according to the criteria that is satisfied first. It must be called
immediately after AdBrixRm.init() in your application class.

** **1\. Based on cumulative number of events** **

Set to upload event information to the DFINERY (Adbrix) server when the set
number of events is accumulated.

Set using the values ​​below predefined in the DFINERY (Adbrix) SDK.

  * AdBrixRm.AdBrixEventUploadCountInterval.MIN: 10 
  * AdBrixRm.AdBrixEventUploadCountInterval.NORMAL: 30 
  * AdBrixRm.AdBrixEventUploadCountInterval.MAX: 60 cases 

Java  Kotlin

    
    
    public class LauncherActivity extends Activity {
    
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_launcher);
    
            // Event upload cycle setting: When the cumulative number of events is 10, events are uploaded to the AdBrix server.
            AdBrixRm.setEventUploadCountInterval(AdBrixRm.AdBrixEventUploadCountInterval.MIN);
    
        }
    }
    
    
    class LauncherActivity : Activity() {
    
        override fun onCreate() {
            super.onCreate()
            
            // Event upload cycle setting: When the cumulative number of events is 10, events are uploaded to the AdBrix server.
            AdBrixRm.setEventUploadCountInterval(AdBrixRm.AdBrixEventUploadCountInterval.MIN)
    
        }
    }
    

** ** 2\. Time standard  ** **

Set to upload event information to the DFINERY (Adbrix) server after a set
time.

Set using the values ​​below predefined in the DFINERY (Adbrix) SDK.

  * AdBrixRm.AdBrixEventUploadTimeInterval.MIN: 30 seconds 
  * AdBrixRm.AdBrixEventUploadTimeInterval.NORMAL: 60 seconds 
  * AdBrixRm.AdBrixEventUploadTimeInterval.MAX: 120 seconds 

Java  Kotlin

    
    
    public class LauncherActivity extends Activity {
    
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_launcher);
    
            // Event upload cycle setting: Event upload to AdBrix server every 120 seconds
            AdBrixRm.setEventUploadTimeInterval(AdBrixRm.AdBrixEventUploadTimeInterval.MAX);
        }
    }
    
    
    class LauncherActivity : Activity() {
    
        override fun onCreate() {
            super.onCreate()
    
            // Event upload cycle setting: Event upload to AdBrix server every 120 seconds
            AdBrixRm.setEventUploadTimeInterval(AdBrixRm.AdBrixEventUploadTimeInterval.MAX)
    
        }
    }
    

####  ** **GDPR settings** **

You can use the GDPR request event to no longer collect any personal data
associated with the data subject in response to a user request.

When this event is called, SDK operation is stopped and all event saving or
transmission is not possible.

This feature cannot be restored until the user deletes and reinstalls the app.

Java  Kotlin

    
    
    void gdprForgetMeEvent() {
        AdBrixRm.gdprForgetMe(getApplicationContext());
    }
    
    
    fun gdprForgetMeEvent() {
        AdBrixRm.gdprForgetMe(applicationContext);
    }

[[Quote:Danger:Moderate]]  **Danger!!!**  
Calling **the gdprForgetMe** API **will cause the SDK to stop immediately and
analysis of all events will be disabled** .  
This state will persist until the user reinstalls the app.

####  ** **Tracking settings** **

The Android SDK tracks Google's [ Advertising Identifier
](https://support.google.com/googleplay/android-
developer/answer/6048248?hl=ko) by default. This value must be used in
accordance with [ Advertising ID policy
](https://play.google.com/about/monetization-ads/ads/ad-id/) . If necessary,
you can limit tracking of advertising identifiers using the following APIs:

[[Quote:Guide:Normal]] Warning  
The corresponding API must be declared before calling the AdBrixRm.init()
method.

Java  Kotlin

    
    
    //The method must be called before AdBrixRm.init().
    AdBrixRm.setEnableAdIdTracking(false);
    
    
    //The method must be called before AdBrixRm.init().
    AdBrixRm.setEnableAdIdTracking(false);

* * *

###  ** **Deep link/deferred deep link event analysis** **

####  ** **Deep link analysis** **

Analyze the occurrence of deep link open events through tracking links.

Depending on the launchMode property of the activity opened with a deep link,
the linking method varies as follows.

  1. When in singleTask mode 
  2. When not in singleTask mode 

[[Quote:Guide:Normal]]  **How do I check launchMode???**  
Find the activity that will be opened by the deep link in the
AndroidManifest.xml file.  
Check the value of android:launchMode among the attributes that define the
activity.

**1\. When in singleTask mode**

When android:launchMode is singleTask, set as follows to analyze app open
events through deep linking.

Set the following settings for all activities opened through deep links.

Java  Kotlin

    
    
    public class DeeplinkOpenedActivity extends Activity {
    
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
       }
    
        @Override
        protected void onNewIntent(Intent intent) {
            super.onNewIntent(intent);
            // Do something with Deeplink Intent Data
            setIntent(intent);  
      
     // 1. Call the deep link event.
            AdBrixRm.deeplinkEvent(DeeplinkOpenedActivity.this);  
      
     // 2. If you have configured the activity life cycle to handle the onResume callback so that the onResume callback does not occur, remove the comment in the code below.  
     //AdBrixRm.onResume(DeeplinkOpenedActivity.this);
        }  
      
     @Override  
     protected void onResume(){  
     super.onResume();  
     }
    }
    
    
    class DeeplinkOpenedActivity : Activity() {
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.deeplink_activity)
        }
    
        override fun onNewIntent(intent: Intent) {
            super.onNewIntent(intent)
            setIntent(intent)  
      
     // 1. Call the deep link event.
            AdBrixRm.deeplinkEvent(this)  
      
     // 2. If you have configured the activity life cycle to handle the onResume callback so that the onResume callback does not occur, remove the comment in the code below.  
     //AdBrixRm.onResume(this)
        }  
      
     override fun onResume() {  
     super.onResume()  
     }
    }

[[인용​:보통:위험]]​ * Both setIntent() and deeplinkEvent() functions must be set in
the same order as the example above.

[[Quote:Warning]] **Handling the Android Activity Lifecycle?**  
The SDK handles deep link open events using the onResume callback of the
Android activity lifecycle.  
**If your app is terminating the activity before the onResume callback occurs,
you must call the AdBrixRm.onResume function and** pass the SDK onResume
callback.

In order to process app opening through deep linking, deep linking must be set
up in the app.

Set the deep link to the activity registered in [ **AndroidManifest.xml >
manifest > application ** ] as follows.

    
    
    <intent-filter>
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="your_scheme" android:host="your_host" />
    </intent-filter>

When using **Android AppLink,** set the activity registered in [
**AndroidManifest.xml > manifest > application ** ] as follows. Applink is an
optional feature, so please connect only if you use Applink.

    
    
    <intent-filter android:autoVerify="true">
        <action android:name="android.intent.action.VIEW" />
        <category android:name="android.intent.category.DEFAULT" />
        <category android:name="android.intent.category.BROWSABLE" />
        <data android:scheme="https" android:host="your_appkey.adtouch.adbrix.io" />
    </intent-filter>

[[Quote:Warning:Normal]] In the your_appkey field, you must enter the Appkey
you use when linking, and please enter it in lowercase.

[[Quote:Risk:Medium]] Please check before connecting Applink!  
1\. In order to use Applink, you must set the deep link path method to
"dynamic path" when creating a tracking link, and then enter the deep link
path to move to in the deeplink_custom_path value, a parameter attached to the
created tracking link, and pass it to Applink.  
2\. If you arbitrarily modify "is_used_abx_applink=true", which is
automatically added to the value passed as intent of the activity opened with
Applink, accurate advertising performance measurement will not be possible.  
3\. Applink is an optional feature. If you do not use Applink, this task is
not required.

**2\. When not in singleTask mode**

When android:launchMode is a mode other than singleTask, set as follows to
analyze app open events through deep linking.

Configure the deep link open activity provided by AdBrix SDK in the
AndroidManifest.xml file as follows.

    
    
    <activity  
     android:name="com.igaworks.v2.core.application.AbxDefaultDeeplinkActivity"  
     android:label="@string/app_name"  
     android:launchMode="singleTask"  
     android:noHistory="true">  
     <intent-filter android:label="@string/app_name">  
     <action android:name="android.intent.action.VIEW" />  
     <category android:name="android.intent.category.DEFAULT" />  
     <category android:name="android.intent.category.BROWSABLE" />  
     <!--Enter the deep link schema and host. -->  
     <data android:scheme="your_scheme" android:host="your_host" />  
     </intent-filter>  
     <!-- Set the path of the actual deep link activity to be opened by AbxDefaultDeeplinkActivity in android:value. -->  
     <meta-data android:name="AbxRedirectActivity" android:value="com.exampleunity.UnityPlayerActivity"/>  
     </activity>

####  ** **Deferred deep linking** **

A deferred deep link is responsible for delivering the relevant information
from the server so that it can land on a specific screen after installing the
app.

[[Quote:Guide:General]] The value transmitted from a deferred deep link is
transmitted as a string type as follows.  
yes; myscheme://host?key=value

**1\. When using Custom Application Class**

When using Custom Application Class in the app, it is integrated as follows.

Java  Kotlin

    
    
    public class MyApplication extends Application {
    
        @Override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            AdBrixRm.init(this,"your_appKey","your_secretKey");
            AdBrixRm.setOnDeferredDeeplinkListener(new AdBrixRm.onDeferredDeeplinkListener() {
                @Override
                public void onReceive(OnDeferredDeeplinkResult result) {
                    // AdbrixRm SDk returns deferred deeplink url as string.
                    // Use this string value and send your user to certin activity.
                    Log.d("abxrm", "Deferred Deeplink : "+ result.getDeeplink());
                }
            });
       }
    }
    
    
    class MyApplication:Application(){
    
        override fun onCreate() {
            super.onCreate()
            AdBrixRm.init(this, "your_appKey", "your_secretKey");
            AdBrixRm.setOnDeferredDeeplinkListener {
                // AdbrixRm SDk returns deferred deeplink url as string.
                // Use this string value and send your user to certin activity.
                Log.d("abxrm", "Deferred Deeplink : " + it.getDeeplink())
            }
        }
    }

**2\. When using AdbrixRM Application Class**

When using the Application Class provided by DFINERY (Adbrix), it is linked to
an activity that lands with a deep link.

Java  Kotlin

    
    
    public class MainActivity extends Activity{
    
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            
            // To get deferred deeplink url, set this listener.
            AdBrixRm.setOnDeferredDeeplinkListener(new AdBrixRm.onDeferredDeeplinkListener() {
                @Override
                public void onReceive(OnDeferredDeeplinkResult result) {
                    // AdbrixRm SDk returns deferred deeplink url as string.
                    // Use this string value and send your user to certin activity.
                    Log.d("abxrm", "Deferred Deeplink : "+ result.getDeeplink());
                }
            });
       }
    }
    
    
    class MainActivity: Activity(){
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContentView(R.layout.activity_main)
            
            // To get deferred deeplink url, set this listener.
            AdBrixRm.setOnDeferredDeeplinkListener {
                // AdbrixRm SDk returns deferred deeplink url as string.
                // Use this string value and send your user to certin activity.
                Log.d("abxrm", "Deferred Deeplink : " + it.getDeeplink())
            }
        }
    }

[[Quote:Warning:Normal]]  **Listener is not called!!!**  
If deferred deep link information is not delivered to the listener you
implemented, please check the following:  
1\. No conversion occurred through the tracking link.  
2\. Deep linking is not set up in the tracking link.

[[Quote:Warning:Normal]]  ** The app opens twice!!!  **  
When you install/run an app from Google Play through a tracking link with deep
linking set up,  
Deferred deep linking provided by Google Play Store works.  
We recommend that you handle exceptions through the listener you implement to
avoid duplicate processing.

[[Quote:Danger:Small]]  ** **An operation is not implemented: Not yet
implemented error is reported.** **  
Regardless of the SDK, this error may occur when using the TODO annotation
within a callback method.  
If there is a TODO in the callback method, please remove it.

[[Quote:Danger:Small]]  ** **fetchDeferredAppLinkData API from Facebook SDK is
not available** **  
Our DeferredDeeplink API takes over the role of fetchDeferredApplinkData used
in Facebook advertising, so it cannot be used repeatedly. If you are using it,
please delete it.

* * *

##  **Event Analysis**

By analyzing events that occur in the app, you can construct reports and send
postbacks.

To analyze an event, you must insert an event analysis code at the time an
event occurs and deliver appropriate event information.

DFINERY (Adbrix) provides four major types of event analysis.

  1. **User analysis**
    1. Login/logout events 
    2. User information~ 
  2. **Custom event analysis**
  3. **Common (general) event analysis**
    1. join the membership 
    2. app updates 
    3. user invitation 
    4. credit usage 
    5. purchase 
  4. **Commerce event analysis**   

    1. Enter the home (main) screen 
    2. Enter category (special exhibition) 
    3. View product details 
    4. Put in a shopping cart 
    5. Add product of interest 
    6. Confirm your order 
    7. Cancel order 
    8. Search for product 
    9. Share product 
    10. View product list 
    11. View shopping cart list 
    12. Payment information 
  5. **Game event analysis**
    1. Tutorial completed 
    2. character generation 
    3. Stage completed 
    4. Level achieved 

###  ** **User analysis** **

####  ** **Login/logout events** **

Analyze app users’ login/logout events.

When login is successful, the identification value (user ID) that identifies
the user is passed as follows.

[[인용​:보통:위험]]​  **Login Precautions**  
The user ID used for login is used for matching between users and devices when
using the growth action function. If login is called again without logging out
after logging in, correct matching may not occur.  
Please be careful not to include personal information in your user ID. If the
user ID includes personal information such as email or phone number, we
recommend encrypting it.

**API**

Java  Kotlin

    
    
    //When User Login
    AdBrixRm.login(String user_id);
        
    //When user logout
    AdBrixRm.logout();
    
    
    //When User Login
    AdBrixRm.login(String user_id)
    
    //When user logout
    AdBrixRm.logout();
    

**Sample Code**

Java  Kotlin

    
    
    void loginAndLogoutEvent() {
    
        if(isLogin){
            // Login success with user_id "user_1234"
            AdBrixRm.login("user_1234");
        }else{
            //When user logs out
            AdBrixRm.logout();
        }
    }
    
    
    fun loginAndLogoutEvent() {
    
        if(isLogin){
            // Login success with user_id "user_1234"
            AdBrixRm.login("user_1234")
        }else{
            //When user logs out
            AdBrixRm.logout()
        }  
    
    }

####  ** **User information** **

You can analyze the users age, gender, and other information.

[[인용​:보통:위험]]​  **Precautions when setting user information**  
Please use the login, setAge, and setGender APIs for user ID, age, and gender,
respectively.

**API**

Java  Kotlin

    
    
    //Set User Age
    AdBrixRm.setAge(int age);
    
    // Set User Gender
    AdBrixRm.setGender(AdBrixRm.AbxGender abxgender);
    
    //Set other User info
    // value types are only allowed with String, Long, Double, Boolean
    AdBrixRm.UserProperties userProperties = new AdBrixRm.UserProperties();
          userProperties.setAttrs(String key1, String value1)
            .setAttrs(String key2, long value2)
            .setAttrs(String key3, double value3)
             setAttrs(String key4, boolean value4);
     
    AdBrixRm.saveUserProperties(userProperties);
    
    
    
    //Set User Age
    AdBrixRm.setAge(int age)
    
    // Set User Gender
    AdBrixRm.setGender(AdBrixRm.AbxGender abxgender)
    
    //Set other User info
    // value types are only allowed with String, long, double, boolean
    val userProperties = AdBrixRm.UserProperties()
            .setAttrs(String key1, String value1)
            .setAttrs(String key2, long value2)
            .setAttrs(String key3, double value3)
             setAttrs(String key4, boolean value4)
     
    AdBrixRm.saveUserProperties(userProperties)
    

**Sample Code**

Java  Kotlin

    
    
    void userPropertyUpdate() {
    
        // set user age
        AdBrixRm.setAge(30);
    
        // set user gender
        AdBrixRm.setGender(AdBrixRm.AbxGender.MALE);
    
        //set other userinfo
        AdBrixRm.UserProperties userProperties = new AdBrixRm.UserProperties();
                userProperties.setAttrs("user_nick", "peterPark")
                .setAttrs("place","Seoul")
                .setAttrs("height",180)
                .setAttrs("married",false);
    
              
        AdBrixRm.saveUserProperties(userProperties);
    
    }
    
    
    fun userPropertyUpdate() {
    
        // set user age
        AdBrixRm.setAge(30);
    
        // set user gender
        AdBrixRm.setGender(AdBrixRm.AbxGender.MALE);
    
        //set other userinfo
       val userProperties = AdBrixRm.UserProperties()
                .setAttrs("user_nick", "peterPark")
                .setAttrs("place","Seoul")
                .setAttrs("height",180)
                .setAttrs("married",false);
       
        AdBrixRm.saveUserProperties(userProperties)
    
    }
    

[[Quote:Risk:Moderate]]  **Things to keep in mind when setting UserProperty
and AttrModel**  
1.100 or more pieces of information will not be processed.  
2\. The data type of the key value is string, cannot exceed 50 characters, and
cannot use any characters other than lowercase English letters and numbers.  
3\. The data length of the Value value cannot exceed 1024 bytes in byte. Also,
only Long, Double, Boolean, and String types can be used.  
4\. Null value cannot be used as Value value.

###  ** **Custom event analysis** **

Analyzes all common user events within the app. (excluding purchase-related
events)

You can freely analyze most actions within the app, such as button click,
character creation, tutorial completion, and level up.

**API**

Java  Kotlin

    
    
    // Custom event with AttrModel
    AdBrixRm.event(String eventName, AdBrixRm.AttrModel attrmodel);
    
    // Custom event without AttrModel
    AdBrixRm.event(String eventName);
    
    
    
    // Custom event with AttrModel
    AdBrixRm.event(String eventName, AdBrixRm.AttrModel attrmodel)
    
    // Custom event without AttrModel
    AdBrixRm.event(String eventName)
    

**Sample Code**

Java  Kotlin

    
    
    void userCustomEvent() {
    
        // Set additional event information
        AdBrixRm.AttrModel eventAttr = new AdBrixRm.AttrModel()
                .setAttrs("address","Dongan-gu, Anyang-si, Gyeonggi-do")
                .setAttrs("firsttime",true);
    
        // Click the “Invite Friends” button
        AdBrixRm.event("invite_button_click",eventAttr);
    
        // "Character Creation" completed
        AdBrixRm.event("create_character_complete",eventAttr);
    
        // "View Tutorial" completed
        AdBrixRm.event("tutorial_complete",eventAttr);
    
        // "Level 10 achieved" completed
        AdBrixRm.event("level_10",eventAttr);
    
    }
    
    
    fun locationUpdate() {
          
         // Set additional event information
         val eventAttr = AdBrixRm.AttrModel()
         	      .setAttrs("address", "Dongan-gu, Anyang-si, Gyeonggi-do")
                .setAttrs("firsttime", true)
    
        // Click the “Invite Friends” button
        AdBrixRm.event("invite_button_click",eventAttr)
    
        // "Character Creation" completed
        AdBrixRm.event("create_character_complete",eventAttr)
    
        // "View Tutorial" completed
        AdBrixRm.event("tutorial_complete",eventAttr)
    
        // "Level 10 achieved" completed
        AdBrixRm.event("level_10",eventAttr)
        
    }

[[Quote:Risk:Medium]] Custom events can only be set to a maximum of 100, in
the order they are called.

** **※ caution** **

As in the example below, do not set naturally increasing values ​​as event
names.

Too many events actually interfere with analysis.

    
    
    AdBrixRm.event("Level-301-Achieved-at-01:23:45.1234567");

Therefore, in this case, please set additional event information
(AdBrixRm.AttrModel) and set custom parameters to call the event.  

    
    
    // Set additional event information
    AdBrixRm.AttrModel eventAttr = new AdBrixRm.AttrModel()
                .setAttrs("level",37)
                .setAttrs("clear_time_mile", 39238);
    
    // Call custom event API with event parameters
    AdBrixRm.event("level_clear", eventAttr);        
    

* * *

###  ** **Common (general) event analysis** **

Among the events that occur in the app, we analyze the commonly occurring
event (payment).

Common event types provided by DFINERY (Adbrix) are as follows.

  * join the membership 
  * app updates 
  * user invitation 
  * credit usage 
  * Make payment 

* If you want to view sales by advertising channel in DFINERY (Adbrix), you must perform the ‘Payment’ link. 

####  ** **join the membership** **

Analyze membership registration events that occurred in the app.

**API**

Java  Kotlin

    
    
    // SignUp event with Additional signUp info
    AdBrixRm.Common.signUp(AdBrixRm.CommonSignUpChannel signUpChannel, AdBrixRm.CommonProperties.SignUp signUpInfo);
     
    // SignUp event without Additional signUp info
    AdBrixRm.Common.signUp(AdBrixRm.CommonSignUpChannel signUpChannel);
    
    
    
    // SignUp event with Additional signUp info
    AdBrixRm.Common.signUp(AdBrixRm.CommonSignUpChannel signUpChannel, AdBrixRm.CommonProperties.SignUp signUpInfo)
     
    // SignUp event without Additional signUp info
    AdBrixRm.Common.signUp(AdBrixRm.CommonSignUpChannel signUpChannel)

**Sample Code**

Java  Kotlin

    
    
    void userRegister() {
        try {
     // Set additional event information as membership registration event information.
            AdBrixRm.CommonProperties.SignUp signupUserInfo = new AdBrixRm.CommonProperties.SignUp();            
          
            //Membership registration API call
            AdBrixRm.Common.signUp(AdBrixRm.CommonSignUpChannel.Google,signupUserInfo);
    
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    
    
    void userRegister() {
        try {    
            // Set additional event information as membership registration event information.
             val signupUserInfo = AdBrixRm.CommonProperties.SignUp()
    
             //Membership registration API call
             AbxCommon.signUp(AdBrixRm.CommonSignUpChannel.Google, signupUserInfo)
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

####  ** **app updates** **

Analyze app update events that occurred in the app.

**API**

Java  Kotlin

    
    
    AdBrixRm.Common.appUpdate(AdBrixRm.CommonProperties.AppUpdate appUpdate); 
    
    
    
    AdBrixRm.Common.appUpdate(AdBrixRm.CommonProperties.AppUpdate appUpdate)

**Sample Code**

Java  Kotlin

    
    
    void appUpdate() {
        try {                
            AdBrixRm.CommonProperties.AppUpdate updateInfo = new AdBrixRm.CommonProperties.AppUpdate()
                            .setPrevVersion("1.0.0a")
                            .setCurrVersion("1.0.1a");
                            
            //Call app update API
            AdBrixRm.Common.appUpdate(updateInfo);
    
        } catch (JSONException e){
            e.printStackTrace();
        }
    }
    
    
    void appUpdate() {
          try {
            // Set app update event information.    
            val updateInfo = AdBrixRm.CommonProperties.AppUpdate()
                .setCurrVersion("1.2.0")
                .setPrevVersion("1.1.0")
                                                                      
            //Call app update API
            AbxCommon.appUpdate(updateInfo)
    
           } catch (e: Exception) {
                e.printStackTrace()
           }
    }

####  **_user invitation_ **

Analyze app invitation events that occurred in the app.

**API**

Java  Kotlin

    
    
    // UserInvite event with Additional event info
    AdBrixRm.Common.invite(AdBrixRm.CommonInviteChannel inviteChannel, AdBrixRm.CommonProperties.Invite inviteInfo);
     
    // UserInvite event without Additional event info
    AdBrixRm.Common.invite(AdBrixRm.CommonInviteChannel inviteChannel);
    
    
    
    // UserInvite event with Additional event info
    AdBrixRm.Common.invite(AdBrixRm.CommonInviteChannel inviteChannel, AdBrixRm.CommonProperties.Invite inviteInfo)
     
    // UserInvite event without Additional event info
    AdBrixRm.Common.invite(AdBrixRm.CommonInviteChannel inviteChannel)

**Sample Code**

Java  Kotlin

    
    
    void userInvite() {
        try {
            AdBrixRm.CommonProperties.Invite inviteInfo = new AdBrixRm.CommonProperties.Invite();
                                           
            //Call user invitation API
            AdBrixRm.Common.invite(AdBrixRm.CommonInviteChannel.Facebook,inviteInfo);
    
        } catch (JSONException e){
            e.printStackTrace();
        }
    }
    
    
    void userInvite() {
        try {
           val properties = AdBrixRm.CommonProperties.Invite();
           //Call user invitation API
           AbxCommon.invite(AdBrixRm.CommonInviteChannel.Facebook, properties)
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

####  **_credit usage_ **

Analyze events related to the use of cash currency within the app.

**API**

Java  Kotlin

    
    
    AdBrixRm.Common.useCredit(AdBrixRm.CommonProperties.UseCredit userCreditInfo);
    
    
    
    AdBrixRm.Common.useCredit(AdBrixRm.CommonProperties.UseCredit userCreditInfo)
    

**Sample Code**

Java  Kotlin

    
    
    void usingCredit() {
        try {
    
            // User cash currency usage information
            AdBrixRm.AttrModel commonAttr = new AdBrixRm.AttrModel()
                            .setAttrs("credit", 10000);
                            
            AdBrixRm.CommonProperties.UseCredit userCreditInfo = new AdBrixRm.CommonProperties.UseCredit()
                            .setAttrModel(commonAttr);
           
            //Call credit usage API
            AdBrixRm.Common.useCredit(userCreditInfo);
    
        } catch (JSONException e){
         e.printStackTrace();
        }
    }
    
    
    void usingCredit() {
          try {
    
              // Additional information on currency usage event
              val useCreaditAttr = AdBrixRm.AttrModel()
                  .setAttrs("money", 1000.00)              
    
              //Call credit usage API
              AbxCommon.useCredit(properties)
    
         } catch (e: Exception) {
            e.printStackTrace()
         }
    }

####  ** **Make payment** **

[[인용​:보통:위험]]​ Add total order amount parameter!!! (sdk ver: 1.1.2200)  
A parameter has been added to enter the total sales amount of the order. Just
enter the amount based on the order total amount calculation criteria.

**API**

Java  Kotlin

    
    
    AdBrixRm.Common.purchase(
          String orderId,
          List  productModelList,
          double orderSale, // Optional
          double discount,
          double deliveryCharge,
          AdBrixRm.CommercePaymentMethod paymentMethod;
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Common.purchase(
          String orderId,
          List  productModelList,
          double orderSale, //Optional
          double discount,
          double deliveryCharge,
          AdBrixRm.CommercePaymentMethod paymentMethod,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void purchaseEvent() {
    
        try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel purchaseAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
            
            AdBrixRm.CommonProperties.Purchase purchaseat = new AdBrixRm.CommonProperties.Purchase()
                .setAttrModel(purchaseAttr);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
            // Product payment - mobile payment
            AdBrixRm.Common.purchase("290192012", productModelArrayList, 22500.0,0.00, 3500.00, AdBrixRm.CommercePaymentMethod.MobilePayment,purchaseat);
    
        } catch (JSONException e) {
            e.printStackTrace();
        }
    
    }
    
    
    fun purchaseEvent() {
    
        try {
    
            // Set product category
            val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
            //Setting additional product information
            val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
            val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
            // event additional information
            val purchaseAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
            
            val purchaseat = AdBrixRm.CommonProperties.Purchase()
                .setAttrModel(purchaseAttr)
                
            //Product information
            val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
            val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
            // Set product information arrayList
            val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
            // call purchase event
            AbxCommon.purchase("orderid_1", proList,54000.00 0.00, 2500.00, AdBrixRm.CommercePaymentMethod.CreditCard, purchaseat)
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    
    }
    

* * *

###  ** **Commerce event analysis** **

We analyze purchase-related events (viewing product details, adding to
shopping cart, etc.) that occur in the app.

The types of commerce events provided by AdBrix are as follows.

  * Enter the home (main) screen 
  * Enter category (special exhibition) 
  * View product details 
  * Put in a shopping cart 
  * Add wishlist (product of interest) 
  * Confirm your order 
  * Cancel order 
  * Search for product 
  * Share product 
  * View product list 
  * View shopping cart 
  * Enter payment information 

####  ** **Enter the home (main) screen** **

Analyzes events in which the user enters the apps home (main) screen.

Java  Kotlin

    
    
    void viewHomeEvent(){
    
        // Home (main) screen entry event analysis
        AdBrixRm.Commerce.viewHome();
    
    }
    
    
    fun viewHomeEvent(){
    
        // Home (main) screen entry event analysis
        AbxCommerce.viewHome()
    
    }
    

####  ** **Enter category (special exhibition)** **

Analyze events in which users enter the category (special exhibition) screen.

The product information displayed when entering the category is delivered as
follows.

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.categoryView(
          AdBrixRm.CommerceCategoriesModel productCategory,
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.categoryView(
          AdBrixRm.CommerceCategoriesModel productCategory,
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void viewCategoryEvent(){
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
        // Analyze category view events
        AdBrixRm.Commerce.categoryView(productCategory, productModelArrayList,commmerceAttr);
    
    }
    
    
    fun viewCategoryEvent(){
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        // Analyze category view events
        AbxCommerce.categoryView(productCategory, proList, commerceAttr)
    
    }
    

####  ** **View product details** **

We analyze events where users view products in detail.

We convey information about the following products.

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.productView(
          AdBrixRm.CommerceProductModel productMode;
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.productView(
          AdBrixRm.CommerceProductModel productModel;
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void viewProductDetailEvent(){
    
            try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                                                            
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
                            
            // Product details view event analysis
            AdBrixRm.Commerce.productView(productModel_1,commmerceAttr);
    
            }catch (JSONException e){
                e.printStackTrace();;
            }
        }
    
    
    fun viewProductDetailEvent(){
    
        try {
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
    
        // event additional information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
            
        // Product details view event analysis
        AbxCommerce.productView(productModel1, commerceAttr)
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
    

####  ** **Put in a shopping cart** **

We analyze events in which users add products to their shopping carts.

We convey the following product information:

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.addToCart(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.addToCart(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void addToCartEvent(){
    
        try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
            // Analysis of add to cart event
            AdBrixRm.Commerce.addToCart(productModelArrayList,commmerceAttr);
    
        }catch (JSONException e){
            e.printStackTrace();
        }
    }
    
    
    fun addToCartEvent(){
    
        try {
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        // Analysis of add to cart event
        AbxCommerce.addToCart(proList, commerceAttr)
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
    

####  ** **Add product of interest (wish list)** **

Analyze events in which a user adds a product to a product of interest
(wishlist).

We convey the following product information:

**API (when applying individual ProductModel)  
**

Java  Kotlin

    
    
    AdBrixRm.Commerce.addToWishList(
          AdBrixRm.CommerceProductModel productModel;
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.addToWishList(
          AdBrixRm.CommerceProductModel productModel;
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void addToWishListEvent(){
        try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                                                            
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Analysis of product of interest (wish list) addition event
            AdBrixRm.Commerce.addToWishList(productModel_1,commmerceAttr);
    
        }catch (JSONException e){
            e.printStackTrace();
        }
    }
    
    
    fun addToWishListEvent(){
        try {
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        //call addToWishList api
        AbxCommerce.addToWishList(productModel1, commerceAttr)
    
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
    

**API (when applying multiple ProductModels)**

[[인용​:보통:위험]]​ This API applies from Android SDK 2.4.0.0.

Java  Kotlin

    
    
    AdBrixRm.Commerce.addToWishList(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.addToWishList(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void addToWishListEvent(){
        try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
            
            // Analysis of product of interest (wish list) addition event
            AdBrixRm.Commerce.addToWishList(productModelArrayList,commmerceAttr);
    
        }catch (JSONException e){
            e.printStackTrace();
        }
    }
    
    
    fun addToWishListEvent(){
        try {
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        //call addToWishList api
        AbxCommerce.addToWishList(proList, commerceAttr)
    
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
    

####  ** **Confirm your order** **

We analyze the final confirmation event that a user confirms before paying for
a product.

We convey the following order and product information:

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.reviewOrder(
          String orderId,
          List  productModelList,
          double discount,
          double deliveryCharge,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.reviewOrder(
          String orderId,
          List  productModelList,
          double discount,
          double deliveryCharge,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void reviewOrderEvent(){
        try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
            // Analyze order confirmation event
            AdBrixRm.Commerce.reviewOrder("290192012", productModelArrayList, 0.00, 3500.00,commmerceAttr);
    
        } catch (JSONException e) {
            e.printStackTrace();
        }
    
    }
    
    
    fun reviewOrderEvent(){
        try {
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        // Analyze order confirmation event
        AbxCommerce.reviewOrder("orderid_11", proList, 0.00, 2500.00, commerceAttr)
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    
    }
    

####  ** **Cancel order (refund)  
** **

Analyze events in which a user canceled an order or issued a refund.

We convey the following product and order information:

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.refund(
          String orderId,
          List <AdBrixRm.CommerceProductModel> productModelList,
          double penalty charge,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.refund(
          String orderId,
          List <AdBrixRm.CommerceProductModel> productModelList,
          double penalty charge, 
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void refundOrderEvent(){
        try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
    
            // Order cancellation (refund) event analysis
            AdBrixRm.Commerce.refund("290192012", productModelArrayList, 0.00,commmerceAttr);
    
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
    
    
    fun refundOrderEvent(){
        try {
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        // Order cancellation (refund) event analysis
        AbxCommerce.refund("orderid_22", proList, 19000.00, commerceAttr)
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
    

####  ** **Search for products** **

Analyze events in which users search for products.

We deliver product information included in the following search results.

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.search(
          String searchKeyword,
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.search(
          String searchKeyword,
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void searchProductEvent(){
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
        // Product search event analysis
        AdBrixRm.Commerce.search("Casual Pants", productModelArrayList,commmerceAttr);
    
    }
    
    
    fun searchProductEvent(){
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
            
        // Product search event analysis
        AbxCommerce.search("Search term", proList, commerceAttr)
    
    }
    

####  ** **Share product** **

Analyze events in which users share product information.

We communicate shared product information such as:

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.share(
          AdBrixRm.CommerceSharingChannel SharingChannel,
          AdBrixRm.CommerceProductModel productModel;
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.share(
          AdBrixRm.CommerceSharingChannel SharingChannel,
          AdBrixRm.CommerceProductModel productModel;
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void shareProductEvent(){
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                                                            
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
        // Analyze product information sharing event
        AdBrixRm.Commerce.share(AdBrixRm.CommerceSharingChannel.KakaoTalk, productModel_1, commmerceAttr);
    
    }
    
    
    fun shareProductEvent(){
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        // Analyze product information sharing event
        AbxCommerce.share(AdBrixRm.CommerceSharingChannel.KakaoStory, productModel1, commerceAttr)
    
    }
    

**API (when applying multiple ProductModels)**

[[인용​:보통:위험]]​ This API applies from Android SDK 2.4.0.0.

Java  Kotlin

    
    
    AdBrixRm.Commerce.share(
          AdBrixRm.CommerceSharingChannel SharingChannel,
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.share(
          AdBrixRm.CommerceSharingChannel SharingChannel,
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void addToWishListEvent(){
        try {
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
            
            // share event analysis
            AdBrixRm.Commerce.share(AdBrixRm.CommerceSharingChannel.KakaoTalk, productModelArrayList, commmerceAttr);
    
        }catch (JSONException e){
            e.printStackTrace();
        }
    }
    
    
    fun addToWishListEvent(){
        try {
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        //call share api
        AbxCommerce.share(AdBrixRm.CommerceSharingChannel.KakaoStory, proList, commerceAttr)
    
    
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }
    

####  ** **View product list** **

Analyze events in which users view product lists.

We deliver the following product information you have viewed.

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.listView(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.listView(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void listViewProductsEvent(){
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
        //Analysis of product list search event  
        AdBrixRm.Commerce.listView(productModelArrayList,commmerceAttr);
        
    }
    
    
    
    fun listViewProductsEvent(){
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        //Analysis of product list search event 
        AbxCommerce.listView(proList, commerceAttr)
        
    }
    

####  ** **View shopping cart** **

Analyze events in which users view their shopping carts.

We deliver the following product information you have viewed.

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.cartView(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel // Optional
          );
    
    
    
    AdBrixRm.Commerce.cartView(
          List <AdBrixRm.CommerceProductModel> productModelList,
          AdBrixRm.AttrModel attrModel //Optional
          )
    

**Sample Code**

Java  Kotlin

    
    
    void cartViewProductsEvent(){
    
            // Set product category
            AdBrixRm.CommerceCategoriesModel productCategory = new AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5");
    
            //Setting additional product information
            AdBrixRm.AttrModel productAttr1 = new AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false);
                
            AdBrixRm.AttrModel productAttr2 = new AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true);
    
            // Additional event information
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true);
                                    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_1 =
                    new AdBrixRm.CommerceProductModel().setProductID("5385487400")
                            .setProductName("Special price on 10 types of slacks")
                            .setPrice(10000.00)
                            .setQuantity(1)
                            .setDiscount(1000.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr1);
    
            // Create product information model
            AdBrixRm.CommerceProductModel productModel_2 =
                    new AdBrixRm.CommerceProductModel().setProductID("145099811")
                            .setProductName("[Carryover Special Price] Printed Sweatshirt")
                            .setPrice(15500.00)
                            .setQuantity(1)
                            .setDiscount(1200.00)
                            .setCurrency(AdBrixRm.Currency.KR_KRW)
                            .setCategory(productCategory)
                            .setAttrModel(productAttr2);
    
            // Create product information model ArrayList
            ArrayList productModelArrayList = new ArrayList<>();
            productModelArrayList.add(productModel_1);
            productModelArrayList.add(productModel_2);
    
        //Analysis of shopping cart view event  
        AdBrixRm.Commerce.cartView(productModelArrayList,commmerceAttr);
        
    }
    
    
    
    fun cartViewProductsEvent(){
    
       // Set product category
       val productCategory = AdBrixRm.CommerceCategoriesModel()
                .setCategory("Category 1")
                .setCategory("Category 2")
                .setCategory("Category 3")
                .setCategory("Category 4")
                .setCategory("Category 5")
    
        //Setting additional product information
        val productAttr1 = AdBrixRm.AttrModel()
                .setAttrs("size", 25)
                .setAttrs("color", "blue")
                .setAttrs("vip", false)
                
        val productAttr2 = AdBrixRm.AttrModel()
                .setAttrs("size", 33)
                .setAttrs("color", "black")
                .setAttrs("vip", true)
    
        // Additional event information
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("howmany_buy", 36)
                .setAttrs("discount", true)
                
        //Product information
        val productModel1 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_1")
                .setProductName("Product Name1")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(5000.00)
                .setAttrModel(productAttr1)
                .setPrice(50000.00)
                .setQuantity(1)
    
        val productModel2 = AdBrixRm.CommerceProductModel()
                .setProductID("productid_2")
                .setProductName("Product Name2")
                .setCategory(productCategory)
                .setCurrency(AdBrixRm.Currency.KR_KRW)
                .setDiscount(10000.00)
                .setAttrModel(productAttr2)
                .setPrice(100000.00)
                .setQuantity(1)
    
        // Set product information arrayList
        val proList = mutableListOf<AdBrixRm.CommerceProductModel>()
            proList.add(productModel1)
            proList.add(productModel2)
    
        //Analysis of shopping cart view event 
        AbxCommerce.cartView(proList, commerceAttr)
    
    }
    

####  ** **Enter payment information** **

Analyze events where users enter payment information.

**API**

Java  Kotlin

    
    
    AdBrixRm.Commerce.paymentInfoAdded(AdBrixRm.AttrModel attrModel);
    
    
    
    AdBrixRm.Commerce.paymentInfoAdded(AdBrixRm.AttrModel attrModel)
    

**Sample Code**

Java  Kotlin

    
    
    void paymentInfoAddedEvent(){
    
            AdBrixRm.AttrModel commmerceAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("card", "kbcard")
                .setAttrs("discount", true);
            
            //Payment information input event
            AdBrixRm.Commerce.paymentInfoAdded(commmerceAttr);
    
    }
    
    
    
    fun paymentInfoAddedEvent(){
          
        //Payment information input event
        val commerceAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("card","kcard")
                .setAttrs("discount", true)               
                 
        AbxCommerce.paymentInfoAdded(commerceAttr)
    
    }
    

* * *

###  ** **Game event analysis** **

Analyze game-related events (tutorials, stages, etc.) that occur in the app.

The types of game events provided by DFINERY (Adbrix) are as follows.

  * Tutorial completed 
  * character generation 
  * Stage completed 
  * Level achieved 

####  ** **Tutorial completed** **

Analyze tutorial completion events that occur in the app.

The following tutorial completion information is passed by configuring the
value of GameProperies.TutorialComplete.

**API**

Java  Kotlin

    
    
    AdBrixRm.Game.tutorialComplete(AdBrixRm.GameProperties.TutorialComplete gameProperties);
    
    
    
    AdBrixRm.Game.tutorialComplete(AdBrixRm.GameProperties.TutorialComplete gameProperties)
    

**Sample Code**

Java  Kotlin

    
    
    void tutorialCompleteEvent(){
    
            AdBrixRm.AttrModel gameAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true);
    
            AdBrixRm.GameProperties.TutorialComplete gameProperties
                      = new AdBrixRm.GameProperties.TutorialComplete()
                      .setIsSkip(true)
                      .setAttrModel(gameAttr);
    
            //Call tutorial completion event
            AdBrixRm.Game.tutorialComplete(gameProperties);
    }
    
    
    fun tutorialCompleteEvent(){
    
            val gameAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true)                            
    
            val tutorialProperties = AdBrixRm.GameProperties.TutorialComplete()
                .setIsSkip(false)
                .setAttrModel(gameAttr)
    
            //Call tutorial completion event
            AbxGame.tutorialComplete(tutorialProperties)
    
    }
    

####  ** **character generation** **

Analyze character creation events that occurred in the app.

The following character creation information is passed by configuring the
value of GameProperies.CharacterCreated.

**API**

Java  Kotlin

    
    
    AdBrixRm.Game.characterCreated(AdBrixRm.GameProperties.CharacterCreated gameProperties);
    
    
    
    AdBrixRm.Game.characterCreated(AdBrixRm.GameProperties.CharacterCreated gameProperties)
    

**Sample Code**

Java  Kotlin

    
    
    void characterCreatedEvent(){
    
            AdBrixRm.AttrModel gameAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true);
                
            AdBrixRm.GameProperties.CharacterCreated gameProperties
                      = new AdBrixRm.GameProperties.CharacterCreated()
                      .setAttrModel(gameAttr);
    
            //Call character creation event
            AdBrixRm.Game.characterCreated(gameProperties);
    }
    
    
    fun characterCreatedEvent(){
    
            val gameAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true)
    
            val characterProperties = AdBrixRm.GameProperties.CharacterCreated()
                .setAttrModel(gameAttr)
    
            //Call character creation event
            AbxGame.characterCreated(characterProperties)
            
    }
    

####  ** **Stage completed** **

Analyze stage completion events that occur in the app.

The following stage completion information is passed by configuring the value
of GameProperies.StageCleared.

**API**

Java  Kotlin

    
    
    AdBrixRm.Game.stageCleared(AdBrixRm.GameProperties.StageCleared gameProperties);
    
    
    
    AdBrixRm.Game.stageCleared(AdBrixRm.GameProperties.StageCleared gameProperties)
    

**Sample Code**

Java  Kotlin

    
    
    void stageClearedEvent(){
    
            AdBrixRm.AttrModel gameAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true);
    
            AdBrixRm.GameProperties.StageClearedgameProperties
                      = new AdBrixRm.GameProperties.StageCleared()
                      .setStageName("1-1")
                      .setAttrModel(gameAttr);
    
            //Call stage completion completion event
            AdBrixRm.Game.stageCleared(gameProperties);
    }
    
    
    fun stageClearedEvent(){
    
            val gameAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true)
                               
            val stageProperties = AdBrixRm.GameProperties.StageCleared()
                .setStageName("stage111")
                .setAttrModel(gameAttr)
    
            AbxGame.stageCleared(stageProperties)
            
    }
    

####  ** **Level achieved** **

Analyze level achievement events that occurred in the app.

The following level achievement information is passed by configuring the value
of GameProperies.LevelAchieved.

**API**

Java  Kotlin

    
    
    AdBrixRm.Game.levelAchieved(AdBrixRm.GameProperties.LevelAchieved gameProperties);
    
    
    
    AdBrixRm.Game.levelAchieved(AdBrixRm.GameProperties.LevelAchieved gameProperties)
    

**Sample Code**

Java  Kotlin

    
    
    void levelAchievedEvent(){
    
            AdBrixRm.AttrModel gameAttr = new AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true);
    
            AdBrixRm.GameProperties.LevelAchievedgameProperties
                      = new AdBrixRm.GameProperties.LevelAchieved()
                      .setLevel(1)
                      .setAttrModel(gameAttr);
    
            //Call level achievement event
            AdBrixRm.Game.levelAchieved(gameProperties);
    }
    
    
    fun levelAchievedEvent(){
    
            val gameAttr = AdBrixRm.AttrModel()
                .setAttrs("grade", "vip")
                .setAttrs("level", 36)
                .setAttrs("google_vip", true)
                
            val levelProperties = AdBrixRm.GameProperties.LevelAchieved()
                .setLevel(12)
                .setAttrModel(gameAttr)          
    
            //Call level achievement event
            AbxGame.levelAchieved(levelProperties)
            
    }
    

  * [Facebook](https://www.facebook.com/share.php?title=Integrating+DFINERY+%28Adbrix%29+%5BAndroid%5D&u=https%3A%2F%2Fhelp.dfinery.io%2Fhc%2Fen-us%2Farticles%2F360003279994-Integrating-DFINERY-Adbrix-Android)
  * [Twitter](https://twitter.com/share?lang=en&text=Integrating+DFINERY+%28Adbrix%29+%5BAndroid%5D&url=https%3A%2F%2Fhelp.dfinery.io%2Fhc%2Fen-us%2Farticles%2F360003279994-Integrating-DFINERY-Adbrix-Android)
  * [LinkedIn](https://www.linkedin.com/shareArticle?mini=true&source=DFINERY&title=Integrating+DFINERY+%28Adbrix%29+%5BAndroid%5D&url=https%3A%2F%2Fhelp.dfinery.io%2Fhc%2Fen-us%2Farticles%2F360003279994-Integrating-DFINERY-Adbrix-Android)

1

Was this article helpful?

[](/hc/en-us/signin?return_to=https%3A%2F%2Fhelp.dfinery.io%2Fhc%2Fen-
us%2Farticles%2F360003279994-Integrating-DFINERY-Adbrix-Android "Yes")
[](/hc/en-us/signin?return_to=https%3A%2F%2Fhelp.dfinery.io%2Fhc%2Fen-
us%2Farticles%2F360003279994-Integrating-DFINERY-Adbrix-Android "No")

1 out of 1 found this helpful

Have more questions? [Submit a request](/hc/en-us/requests/new)

Return to top

### Related articles

  * [Integrating Definery (Adbrix) [iOS]](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCAdTgYzRADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCHoc3tFTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJEL2hjL2VuLXVzL2FydGljbGVzLzkwMDAwNTQ1MDUwMy1JbnRlZ3JhdGluZy1EZWZpbmVyeS1BZGJyaXgtaU9TBjsIVDoJcmFua2kG--389ef909aede2f48c6063333e47e50177a5a1bf3)
  * [Deeplink: Distinguishing and understanding URI schemes, universal links, and app links](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCHm2CtRTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCHoc3tFTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJ4L2hjL2VuLXVzL2FydGljbGVzLzM2MDAzOTc1NzQzMy1EZWVwbGluay1EaXN0aW5ndWlzaGluZy1hbmQtdW5kZXJzdGFuZGluZy1VUkktc2NoZW1lcy11bml2ZXJzYWwtbGlua3MtYW5kLWFwcC1saW5rcwY7CFQ6CXJhbmtpBw%3D%3D--ab7758ee84385092e49f343245ee3476fc7d1c6c)
  * [Integrating DFINERY (Adbrix) [Web]](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCIMifIzRADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCHoc3tFTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJDL2hjL2VuLXVzL2FydGljbGVzLzkwMDAwNTExMDQwMy1JbnRlZ3JhdGluZy1ERklORVJZLUFkYnJpeC1XZWIGOwhUOglyYW5raQg%3D--9200972ca1d9ef948227d80b4ae08f12c93709df)
  * [Integrating DFINERY (Adbrix) [Flutter]](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCO7nNYzRADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCHoc3tFTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJHL2hjL2VuLXVzL2FydGljbGVzLzkwMDAwMDUwNzg4Ni1JbnRlZ3JhdGluZy1ERklORVJZLUFkYnJpeC1GbHV0dGVyBjsIVDoJcmFua2kJ--df17e45b2ee51a6a32c77e5ca1272674c2bf9ac6)
  * [Integrate Growth Action [Android]](/hc/en-us/related/click?data=BAh7CjobZGVzdGluYXRpb25fYXJ0aWNsZV9pZGwrCKYE4dNTADoYcmVmZXJyZXJfYXJ0aWNsZV9pZGwrCHoc3tFTADoLbG9jYWxlSSIKZW4tdXMGOgZFVDoIdXJsSSJEL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNzAyNDkzNC1JbnRlZ3JhdGUtR3Jvd3RoLUFjdGlvbi1BbmRyb2lkBjsIVDoJcmFua2kK--5444f90491a9b65d4d713c841655c178ecb48239)

### [클릭하여 고객지원팀에게 문의하기 답을 찾지 못하였나요? 걱정하지 마시고, 고객지원팀에게 문의주세요!  ](/requests/new)

INDEX

[ ![Logo](/hc/theming_assets/01HZM7C4RA7ZM48B9BNR10P8SF) ](/hc/en-us "Home")

English (US)  [ 한국어
](/hc/change_language/ko?return_to=%2Fhc%2Fko%2Farticles%2F360003279994-%25EB%2594%2594%25ED%258C%258C%25EC%259D%25B4%25EB%2584%2588%25EB%25A6%25AC-%25EC%2595%25A0%25EB%2593%259C%25EB%25B8%258C%25EB%25A6%25AD%25EC%258A%25A4-%25EC%2597%25B0%25EB%258F%2599%25ED%2595%2598%25EA%25B8%25B0-Android)

