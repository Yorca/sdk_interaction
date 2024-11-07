AdColony SDK is no longer in operation. For inquiries or to register for DTX,
please contact
[monetization@digitalturbine.com](mailto:monetization@digitalturbine.com)

[ ![Logo](/hc/theming_assets/01J0TNPZH5HNC0B4JYVY4P382B) ](/hc/en-us "Home")

[Sign in](/hc/en-
us/signin?return_to=https%3A%2F%2Fdeveloper.digitalturbine.com%2Fhc%2Fen-
us%2Farticles%2F360010822437-Integrating-the-Android-SDK&locale=en-us "Opens a
dialog")

#  How can we help you?

  1. [Digital Turbine](/hc/en-us)
  2. [DT Exchange](/hc/en-us/categories/360001778477-DT-Exchange)
  3. [Publishers Entrance](/hc/en-us/sections/360003125397-Publishers-Entrance)
  4. [SDK Configuration ](/hc/en-us/sections/10512451544220-SDK-Configuration)
  5. [Android SDK Configuration](/hc/en-us/sections/360003162198-Android-SDK-Configuration)

July 08, 2024 12:54

[Follow](/hc/en-us/articles/360010822437-Integrating-the-Android-
SDK/subscription.html "Opens a sign-in dialog")

#  Integrating the Android SDK

# Step 1: Integrating the SDK in your App

DT supports both Maven Central dependencies or manual download to integrate
our SDK.  
**Select which option you want to use to integrate the SDK** :

**Maven Central**

Add DT's maven repository and dependencies to your gradle build script:

  1. Add the following to your app’s project level build.gradle file inside the repositories section:

In project level build.gradle there are usually two `repositories` sections -
one for buildscript and one for allprojects. Add the entry in **allprojects**.

    
    
    allprojects {
      repositories {
        // add this
        mavenCentral()
      }
      // ...
    }

  2. Save your file
  3. Add the following to your app’s app level build.gradle file inside the dependencies section,

Starting with version 8.0.0, include the following:

    
    
    def fyberMarketplaceVersion = '8.2.7'
    
    dependencies {
        // ...
        implementation "com.fyber:marketplace-sdk:${fyberMarketplaceVersion}"
        // ...
    }
    

  4. Save the file.

**Manual Download**

## Android Download Button

  1. If you do not have an account, create one [here](https://revenuedesk.inner-active.com/login).
  2. Copy the following files from the **InneractiveAdSDK** folder into your `project libs` folder.  
Starting with 8.0.0 -  

fyber-marketplace-8.0.0.aar

Starting with 8.1.0 - for Open Measurement support

omsdk-android-1.3.25-release.aar

  3. Add the following to your project's build.gradle file:

    
    
    repositories { 
        // ... 
        // Add a flat dir repository 
        flatDir { 
           dirs 'libs' 
        } 
    }
    
    def fyberMarketplaceVersion = "8.2.7" // 
    dependencies { 
       // Add the fyber marketplace AAR libraries
       // 8.0.0 and above
       implementation (name:"fyber-marketplace-${fyberMarketplaceVersion}", ext:'aar')
       // add open measurement sdk - fyber marketplace 8.1.0 and above
       implementation (name:"omsdk-android-1.3.25-release", ext:'aar')
    }
    

# Step 2: Integrating Google Play Services

We recommend using the Google Play Services, otherwise we are unable to access
your Google Advertising ID. This leads to limited ad inventory, as an
increasing number of advertising campaigns require the identifier. This ID is
also essential for tracking daily active users (DAU) on your app.

  1. Add the following to your `build.gradle` dependencies section for Google Play Services:

Adding Dependencies

    
    
    dependencies  {
        implementation ('com.google.android.gms:play-services-base:Version#')
        // use only the ads identifier library
        implementation ('com.google.android.gms:play-services-ads-identifier:x.y.z') // or implementation ('com.google.android.gms:play-services-ads:x.y.z')
    }
    

  2. Apps that update their target API level to 31 (Android 12) must declare a Google Play Services permission in the manifest file as follows, unless the app uses a recent version of Google Mobile Ads SDK:

    
    
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>

Click the box below, for important information.

**New Google Advertising ID Restrictions**

Google Advertising ID (GAID) is a unique string identifier, which identifies a
device anonymously for advertising purposes.

This Advertising ID is provided by Google Play Services and enables users to
opt-out of personalized ads in apps, or reset their identifier. When a user
resets their identifier, it is not allowed to be connected to a previous
identifier.

### **Opt-Out Behavior Change**

Until late 2021, even when a user opted-out, the advertising ID was still
available for developers. The restriction meant that an opt-out ID could not
be used for creating user profiles for advertising purposes, or for targeting
users. The allowed activities for opted-out users were contextual advertising,
frequency capping, reporting and fraud detection.

Google announced that starting in late 2021, when a user opts-out of
personalized ads, the Advertising ID will not be available anymore. Instead, a
string of zeros is received.

This update will rollout with apps running on Android 12 phones, and is
expected to expand to all apps running on devices that support Google Play in
early 2022.

**Android 12** | **Android 11**  
---|---  
![image1.png](/hc/article_attachments/4417201161873) | ![image3.png](/hc/article_attachments/4417195765265)  
  
### **Android 12 Permission Change**

Google also announced [here](https://support.google.com/googleplay/android-
developer/answer/6048248), a behavior change for apps targeting Android 12
(API 31).

For developers to be able to receive the Advertising ID, a new permission must
be added to the manifest file, unless the app uses a recent version of Google
Mobile Ads SDK (see details below):

    
    
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>

The permission is included in recent versions of Google Mobile Ads SDK (play-
services-ads v20.4.0 and higher, or play-services-ads-identifier v17.1.0 and
higher). If the app uses these SDKs as dependencies, then the AD_ID permission
from the SDK’s library manifest is merged with your app’s main manifest by
default, and the advertising ID will be available.

Google will enforce the AD_ID permission for all devices, starting from early
2022.

For more information about Google Play Services, click
[here](https://developers.google.com/android/guides/setup).

# Step 3: Adding Mandatory Permissions - Android Manifest File

  1. Add the following mandatory permissions into your application's AndroidManifest.xml:

Adding Mandatory Permissions

    
    
    <uses-permission android:name="android.permission.INTERNET"/>  
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    

ACCESS_NETWORK_STATE permission is used to differentiate Wifi from a cellular
network.

  2. Add the following permissions to enable your app to get richer and broader demand

Recommended permissions for better targeting

    
    
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>  
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>  
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>

# Step 4: Initializing the SDK

Follow these steps to initialize the SDK

## Google Play Families Ads API

This optional API indicates to the FMP SDK that the user is a child, enabling
participation in the Google Play Families Ads program.

**Using the API**

    
    
    InneractiveAdManager.currentAudienceIsAChild();

The API is called once per app session and before the SDK is initialized.

By default, if the app doesn’t use the API, the user is not a child user.

Once you have added all your Android Manifest information and are ready to
start requesting ads, you must initialize the Inneractive Ads SDK :

  1. Call `InneractiveAdManager.initialize(context, <"appID">)`, and pass on your Activity or application context:

Pass Your Activity Context

    
    
    public class MainActivity extends Activity {
     
       @Override
       protected void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          setContentView(R.layout.activity_main);
          InneractiveAdManager.initialize(this, "Enter_Your_Fyber_AppID"); 
       }
     
       @Override
       protected void onDestroy() {
          if (isFinishing()) {
               //Optionally destroy the SDK after the activity has been destroyed  
               InneractiveAdManager.destroy();
          }
       } 
    }

Optionally, when you're finished using the library and do not intend to
display more ads, call `InneractiveAdManager.destroy()` to release any
resources being used by the SDK.

If you intend to destroy the library from within your activity's `onDestroy`
method, check to ensure that the activity has really finished.

#### Best Practice Check

You can change the library logging level. For more details, click
[here](https://developer.fyber.com/hc/en-us/articles/360010834097-Fyber-
Logging-Android).

### Locating the App ID

Follow the steps below to locate your App ID:

  1. Click **Apps** on the left menu

![Screen_Shot_2022-08-02_at_11_54_10.png](/hc/article_attachments/8085656912401)

  2. The App Management window opens. Next to each app, appears the corresponding App ID.

![Screen_Shot_2022-08-02_at_11_57_11.png](/hc/article_attachments/8085715869585)

## Initialization Callback

Starting from DT Exchange SDK version 7.5.4, it is possible to add an
initialization callback which notifies you about the initialization status of
the SDK.

The callback can be optionally passed to the `InneractiveAdManager` in the
following manner:

    
    
    InneractiveAdManager.initialize(context, appId, new OnFyberMarketplaceInitializedListener() {
               @Override
               public void onFyberMarketplaceInitialized(FyberInitStatus status) {
                   // ...
               }
    });

Where the Status being returned in the initialized callback is:

  * SUCCESSFULLY - when the SDK has been successfully initialized.
  * FAILED_NO_KITS_DETECTED - when only the “core” DT Exchange library has been detected. When this is the status, check your dependencies and add the “video-kit”, “mraid-kit” to it. 
  * FAILED - When the SDK has failed to communicate with our servers and could not be initialized at this time.
  * INVALID_APP_ID -the appId being passed to the `initialize` is incorrect. Please check your configuration or contact us for assistance. 

#### Important: Regarding the "Failed" Status

DT currently recommends using the SDK and performing ad requests when the
FyberInitStatus is “FAILED”, as the SDK, internally, attempts to re-initialize
itself when an AdRequest is executed. The above callback is not invoked in
such cases.

## Passing a User ID to the SDK (from v.7.7.0)

The following code snippet demonstrates how to set a User ID for this SDK
session.

The initial method of the SDK must be called in advance and there is no need
to wait for the onFyberMarketplaceInitialized callback

    
    
    String userId = ...;
    //Without reflection, using an import of the InneractiveAdManager class -
    InneractiveAdManager.setUserId(userId);
    
    //Optionally, using reflection as an example -
    Class FyberInneractiveAdManagerClass =   
    Class.forName("com.fyber.inneractive.sdk.external.InneractiveAdManager");
    Method setUserIdStaticMethod =   
    FyberInneractiveAdManagerClass.getDeclaredMethod("setUserId", String.class);
    setUserIdStaticMethod.invoke(null, userId);
    

You have completed the basic integration of the Android SDK! Now it's time to
integrate other ad types. For details of Android Ad Formats, click
[here](https://developer.fyber.com/hc/en-us/articles/360019744297-Android-Ad-
Formats).

Review the below GDPR related instructions (available starting Android v7.1.5
SDK and legacy version v6.5.6)

# Step 5: Adding User Consent

## GDPR

The General Data Protection Regulation of the European Union requires you to
scope your user's consent. A user could be within the GDPR scope for your app
when one or all of the following apply:

  * The user is currently located in the EU
  * The user has registered with the app as an EU resident
  * The app is specifically targeted to EU users

When you set a GDPR consent value for a user, DT concludes that you have
decided that the user is subject to GDPR rules, even if the user is outside
Europe. If, based on your legal position, your non-EU users are not subject to
GDPR, do not pass any consent value for them.

We recommend that you consult with a legal advisor to determine the best
approach for your business. It is also highly recommended to collect user
consent with a certified Consent Management Platform (CMP).

For a full list of CMPs, click [here](https://iabeurope.eu/cmp-list/).

Once you have collected the user’s consent, you can pass it onto the SDK using
the following API:

    
    
    /**
         * Set the general data protection regulation user consent status
         * @param wasConsentGiven
         */
        public static void setGdprConsent(boolean wasConsentGiven) {…}
        
        // Calling the consent method
        
        InneractiveAdManager.setGdprConsent(true);
    
        /**
        * Set the general data protection regulation consent string
        * @param gdprConsent the consent string
        */
        public static void setGdprConsentString(String gdprConsent) {…}
    
        // Calling the consent method
    
        InneractiveAdManager.setGdprConsentString("consentString");

`GdprConsent` is a boolean. It is **true** if you have the user’s consent. If
you do not have the user's consent, it is **false**.  
`GdprConsentString` is a string.

If you don’t pass the user’s consent to the SDK, only contextual ads are shown
to that user.

To clear the consent flag and consent data, the following API, use the
following API:

    
    
    InneractiveAdManager.clearGdprConsentData();

**It is highly recommended to use the 2nd option of passing a consent string
per the IAB's Transparent & Consent Framework by using a valid CMP (Consent
Management Platform). This is the most common form of consent communication
worldwide and is crucial in order to enjoy ad monetization in the EU. **

We recommend that the first time you gather the user’s consent, you pass it
onto the SDK  _after starting the SDK but before requesting an ad._ The SDK
then takes the user’s consent into consideration when initializing. In the
following sessions, you need only call the API if the user updates their
consent.

More information on GDPR can be found under the [GDPR Resource Page and
FAQs](https://developer.fyber.com/hc/en-us/articles/360010915398-GDPR).

## CCPA

The intention of the California Consumer Privacy Act of 2018 (CCPA) is to
protect the personal information of California residents. CCPA applies to all
companies doing business in California. If a California resident uses an app
developer’s mobile app, CCPA applies to the developer and every company that
processes the personal information of the app’s users.  
CCPA came into effect on 1 January 2020.

For more information on DT and CCPA, refer to DT's [Resource
Page](http://www.fyber.com/ccpa).  
For more information about CCPA, refer to the [IAB CCPA Compliance
Framework](https://iabtechlab.com/standards/ccpa/).

If you choose to allow users to 'opt-out of the sale of their personal
information' then you may use the following:

Once you have obtained a user response to an opt-out option, you can pass it
to the SDK using the following API:

CCPA API

    
    
    /*** Setting the US privacy setting string     
    * @param consentString a non empty String     
    */
    public static void setUSPrivacyString(String consentString) {…}
    
    // Calling the consent method  		     
    InneractiveAdManager.setUSPrivacyString("1YNN");   
    // This is an example value when the user chooses NOT to 'opt-out'

To determine what value to use for the US Privacy String, refer to the IAB
document
[here](https://github.com/InteractiveAdvertisingBureau/USPrivacy/blob/master/CCPA/US%20Privacy%20String.md).  
Example values:

  * When CCPA does not apply (for example if the user is not a resident of California) you can either skip this API or use the following value **1---**
  * If the user choses **NOT** to opt out, and is ok with advertising as usual, you can use **1YNN**
  * If the user chooses to restrict advertising and opt out, you can use 1YYN

To clear the privacy setting flag and opt-out data use the following API:

CCPA Clear Privacy Settings

    
    
    InneractiveAdManager.clearUSPrivacyString();

## LGPD

The Brazilian General Data Protection Law, the **Lei Geral de Proteção de
Dados Pessoais** (LGPD) requires that you only process personal data for
legitimate, specific, explicit and clearly communicated purposes.

Use the following API to enable publishers to set the LGPD consent value:

    
    
    InneractiveAdManager.setLgpdConsent(boolean wasConsentGiven)

The accepted values are:

**true** =consent was given, **false** =no consent.

If the consent value is not set, the default setting is no consent.

## COPPA

The Children's Online Privacy Protection Act of 1998 (COPPA) is a federal law
that imposes specific requirements on operators of websites and online
services to protect the privacy of children under 13.

### COPPA API for Flagging Specific Users

Android SDK 8.2.3+ supports the COPPA API which allows publishers to flag
specific end users as children as required under COPPA. It is the publisher's
responsibility to decide whether to use the COPPA API or to treat all users as
children. For instructions on flagging all users as children, click
[here](https://developer.digitalturbine.com/hc/en-
us/articles/9577916674333-COPPA).

#### Important

  * **Calling the COPPA API must be performed after a successful initialization of the DT SDK**
  * You must pass the COPPA state after every successful init of the SDK

Use the following API to confirm that the target audience of the application
applies to COPPA:

    
    
    InneractiveAdManager.currentAudienceAppliesToCoppa();

# Step 6: Configure Parameters

Use the following API to add gender and age parameters:

    
    
    // For gender values, see: InneractiveUserConfig.Gender
    InneractiveAdManager.setUserParams(new InneractiveUserConfig()
            .setGender(InneractiveUserConfig.Gender.FEMALE)
            .setAge(35));
    

# Step 7: app-ads.txt

The simple app-ads.txt standard helps prevent the unauthorized selling of in-
app inventory and app domain spoofing.

For details of listing your Developer Website URL in the Google Play Store,
click [here](/hc/en-us/articles/360010915438-app-ads-txt).

# Step 8: Optional - Using the DT Exchange SDK in Secure Only Mode (since
version 7.2.1)

    
    
    InneractiveAdManager.useSecureConnections(boolean useSecureConnnections)

This API described above allows you to control how should the SDK perform any
and all network connections.

By invoking this setter with a value of `true` all outgoing network
connections from the DT Exchange SDK will be using ssl/https.  _The default
behaviour is not to use secure connections_.

#### Secure Demand Notice

By requesting secure only content, you potentially decrease the amount of
demand which can be rendered by the SDK.

The Android application level secure API (`network-security-config
cleartextTrafficPermitted`) takes precedence over this value - i.e. if you set
`cleartextTrafficPermitted` to `false` and invoke the `useSecureConnections`
setter with a value of `false`, the SDK behaves as if you requested secure
only connections.

Back to Top ⇧

(C) Digital Turbine

