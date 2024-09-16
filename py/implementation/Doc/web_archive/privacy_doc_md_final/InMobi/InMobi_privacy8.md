


# Getting Started with Android SDK Integration

Integrating and monetizing with InMobi SDK is easy. InMobi supports both
[manual download](https://dl.inmobi.com/inmobi-sdk/IM/InMobi-Android-
SDK-10.7.6.zip) and
[mavenCentral](https://mvnrepository.com/artifact/com.inmobi.monetization/inmobi-
ads-kotlin) to integrate the Android SDK.

#### Note

  * InMobi Android SDK repository is moved to [mavenCentral](https://mvnrepository.com/artifact/com.inmobi.monetization/inmobi-ads) since JCenter is deprecated and retired by Jfrog. For more information, see [this blog](https://jfrog.com/blog/into-the-sunset-bintray-jcenter-gocenter-and-chartcenter/).
  * If you are on InMobi Android SDK versions 10.1.4 or below via a direct integration and not mediation, follow the instructions on [Migrating to SDK 10.7.X](https://support.inmobi.com/monetize/sdk-documentation/android-guidelines/migrating-to-android-sdk-10xx).
  * From September 2023, InMobi has released new monetization and addressability features only on the Kotlin SDK (versions 10.5.0 and above). We highly recommend migrating to the latest InMobi Kotlin SDK version available [here](https://support.inmobi.com/monetize/sdk-documentation/download-sdk).

## Add the InMobi SDK

### Option 1: Pulling the Latest SDK via mavenCentral

If you are using Gradle to build your Android applications, you can pull the
latest version of the SDK from mavenCentral as described below:

  1. Include mavenCentral in your top-level **`build.gradle`** file:
    
        allprojects {
        repositories {
            mavenCentral()
        }
    }
    

  2. Add the following line to the dependencies element in your application module's `build.gradle`.
    
        implementation 'com.inmobi.monetization:inmobi-ads:10.1.3'
    

  3. Sync your Gradle project to ensure the dependency is downloaded by the build system.

###  
Option 2: Adding the SDK Library to your Application Project

Alternatively, you can download the latest version of InMobi's SDK
[here](http://www.inmobi.com/sdk) and copy the library to your application
module's **`libs/`** directory.

To add the library to your project's dependencies, add this line to the
**dependencies** element in your module's `build.gradle:`

    
    
    implementation fileTree(dir: 'libs', include: ['*.aar'])
    

#### **Note**

The latest version of InMobi SDK supports Android 4.1 (API level 16) or
higher.

## Add & Verify Dependencies

To monetize with the InMobi SDK, you must add the following dependencies to
your application module `build.gradle`:

### **Google Play Services**

The InMobi SDK for Android needs the Google Play Services library to enable
better ad targeting via the Google Play Advertising ID. Additionally, the SDK
also uses the Google Play Services for getting a location fix, should the user
consent to collecting their location.  
  
To add the Google Play Services client library to your application:

  1. Add the following line to the application module's dependency element.
    
        implementation 'com.google.android.gms:play-services-ads-identifier:18.0.1' 
    implementation 'com.google.android.gms:play-services-location:21.0.1'//optional dependency for better targeting
    	
    
    	
      2. 
    	
    
    Sync your Gradle project to ensure that the dependencies are included.
    
    
    	
    
    
    
    
    
    
    ###   
    
    **Chrome Custom Tab**
    
    
    
    
    
    This is required to redirect the users to URLs outside InMobi WebView. To add the Chrome Custom library to your application:
    
    
    
    
    
    
    	
      1. 
    	
    
    Add the following line to the application module's dependency element in the Gradle build script:
    
    
    
    	
    
        implementation 'androidx.browser:browser:1.4.0'
    

  2. Sync your Gradle project to ensure dependencies are included.

#### Caution

Failure to include Chrome Custom Tab dependency in your application gradle
scripts will cause ad requests to fail, thus affecting the monetization of
your app with the InMobi SDK.

### **Picasso Library**

The InMobi SDK for Android uses the popular Picasso library for loading ad
assets. To add the Picasso library to your application:

  1. Add the following line to the application module's dependency element in the Gradle build script:
    
        implementation 'com.squareup.picasso:picasso:2.8'
    

  2. Sync your Gradle project to ensure that the dependencies are included.

#### Caution

Failure to include Picasso dependency in your application gradle scripts will
cause interstitial ad requests to fail, thus affecting the monetization of
your app with the InMobi SDK.

### **Support Library  **

For supporting paged scroll of a deck of images or ads, you must use
`support-v4` library

To add the Support Library to your application, add the following line to the
application module's dependency element in the Gradle build script.

    
    
    implementation 'androidx.viewpager:viewpager:1.0.0'
    

### **RecyclerView**

For supporting free scroll of a deck of images or ads, you must use
RecyclerView.

To add the RecyclerView library to your application, add the following line to
the application module's dependency element in the Gradle build script.

    
    
    implementation 'androidx.recyclerview:recyclerview:1.2.1'
    

#### Caution

Failure to include RecyclerView dependency in your application gradle scripts
will cause interstitial ad requests to fail, thus affecting the monetization
of your app with the InMobi SDK.

### **AppSetId;**

[AppSet](https://developer.android.com/training/articles/app-set-id) ID helps
to track users uniquely per device and per publisher. To support retrieving of
AppSet ID in your application.

  1. Add the following line to the application module's dependency element in the Gradle build script:
    
        implementation 'com.google.android.gms:play-services-appset:16.0.2' //optional dependency for better targeting
    implementation 'com.google.android.gms:play-services-tasks:18.0.2' //optional dependency for better targeting 
    	
    
    	
      2. Sync your Gradle project to ensure dependencies are included.
    
    
    
    
    
    
    ### **Miscellaneous  **
    
    
    
    
    
    At times, including the InMobi SDK may cause the 64K limit on methods that can be packaged in an Android dex file to be breached. This can happen if, for example, your app packs a lot of features for your users and includes substantive code to realize this. 
    
    
    
    
    
    If this happens, you can use the multidex support library to enable building your app correctly. To do this: 
    
    
    
    
    
    
    	
      1. 
    	
    
    Modify the **defaultConfig** to mark your application as multidex enabled: 
    
    
    
    	
    
        defaultConfig {
        ... 
        multiDexEnabled true // add this to enable multi-dex 
    } 
    	
    
    	
      2. 
    	
    
    Add the following line to the dependencies element in your application module's build script. 
    
    
    
    	
    
        implementation 'androidx.multidex:multidex:2.0.1'
    

  
Now that you have added the dependencies, your app's build.gradle at this
point will look like as shown below:

    
    
    dependencies {
        implementation 'com.google.android.gms:play-services-ads-identifier:18.0.1' 
        implementation 'com.google.android.gms:play-services-location:21.0.1'//optional dependency for better targeting
        implementation 'androidx.browser:browser:1.4.0'
        implementation 'com.squareup.picasso:picasso:2.8'
        implementation 'androidx.recyclerview:recyclerview:1.2.1'
        implementation 'com.google.android.gms:play-services-appset:16.0.2' //optional dependency for better targeting
        implementation 'com.google.android.gms:play-services-tasks:18.0.2' //optional dependency for better targeting
    } 
    

## Additional Configurations

### **Granting Permissions**

It is highly recommended that you include `ACCESS_FINE_LOCATION` to enable
better ad targeting. This is not mandatory permission; however, including it
will enable accurate ad targeting.

    
    
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    

For further improved targeting, you can add the `ACCESS_WIFI_STATE` and
`CHANGE_WIFI_STATE` permissions to the manifest.

    
    
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    

Google now requires app developers that use the Android Advertising ID (AAID)
to declare the `AD_ID` permission when their apps target Android 13 or above.
You can declare the AD_ID permission to the manifest as follow:

    
    
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>
    

### **Hardware Acceleration**

Hardware acceleration allows you to display HTML5 video ads. To do this, add
`hardwareAccelerated:true` element to the `application` tag.

    
    
    <application 
        ... 
        android:hardwareAccelerated="true" 
        ... 
    >
    

### **Proguard Configuration**

Proguarding helps to remove unused symbols and reduce the final application
footprint. The following proguard directives should be added to your
application's proguard configuration file:

    
    
    -keepattributes SourceFile,LineNumberTable
    -keep class com.inmobi.** { *; }
    -keep public class com.google.android.gms.**
    -dontwarn com.google.android.gms.**
    -dontwarn com.squareup.picasso.**
    -keep class com.google.android.gms.ads.identifier.AdvertisingIdClient{
         public *;
    }
    -keep class com.google.android.gms.ads.identifier.AdvertisingIdClient$Info{
         public *;
    }
    # skip the Picasso library classes
    -keep class com.squareup.picasso.** {*;}
    -dontwarn com.squareup.okhttp.**
    # skip Moat classes
    -keep class com.moat.** {*;}
    -dontwarn com.moat.**
    # skip IAB classes
    -keep class com.iab.** {*;}
    -dontwarn com.iab.**
    

## Important Prerequisites

Let's pause for some checks before we begin initializing the SDK:

#### **Checkpoint: Preparing Your App for AndroidX**

InMobi SDK is compatible with AndroidX (JetPack) library. In case your app
uses the AndroidX library, InMobi SDK 9.1.7 or later is compliant with
AndroidX.  Enabling the jetifier is not required for InMobi SDK. Check for any
other dependencies requiring the enablement of the Jetifier before removing
it. However, if you are using any version below 9.1.7, follow the standard
guidelines by [Google](https://developer.android.com/jetpack/androidx/migrate)
for migration by adding both the flags in build file.

    
    
    android.useAndroidX=true
    android.enableJetifier=true
    

It is highly **recommended** to upgrade Android Gradle plugin version to 4.1
or greater to avoid known issues in the jetifier which is fixed in the latest
Gradle plugin version. To upgrade Android gradle plugin version please refer
to [Android developer
documentation](https://developer.android.com/studio/releases/gradle-plugin).

## Initializing the SDK

Initialize the SDK using the init API by passing the context, InMobi account
ID and the SdkInitialization listener in your launcher activity. Publishers
can now check whether the init is successful or not with the completion
callback. On completion of Init, any integration of ads should be taken care
of. In case the listener is null, the SDK will start working with default
settings and eventually gets updated settings later in the lifecycle of the
app.

#### Remember

You must call this method on the UI thread. Not doing so will cause the
initialization to fail and affect your application's ability to monetize with
InMobi.

#### Java

    
    
    JSONObject consentObject = new JSONObject();
    try {
        // Provide correct consent value to sdk which is obtained by User 
        consentObject.put(InMobiSdk.IM_GDPR_CONSENT_AVAILABLE, true);
        // Provide 0 if GDPR is not applicable and 1 if applicable  
        consentObject.put("gdpr", "0");
        // Provide user consent in IAB format 
        consentObject.put(InMobiSdk.IM_GDPR_CONSENT_IAB, " << consent in IAB format >> ");
    } catch (JSONException e) {
        e.printStackTrace();
    }
    InMobiSdk.init(this, "Insert InMobi Account ID here", consentObject, new SdkInitializationListener() {
        @Override
        public void onInitializationComplete(@Nullable Error error) {
            if (null != error) {
                Log.e(TAG, "InMobi Init failed -" + error.getMessage());
            } else {
                Log.d(TAG, "InMobi Init Successful");
            }
        }
    });
    

#### Kotlin

    
    
    val consentObject = JSONObject() 
    try { 
       // Provide correct consent value to sdk which is obtained by User 
       consentObject.put(InMobiSdk.IM_GDPR_CONSENT_AVAILABLE, true) 
       // Provide 0 if GDPR is not applicable and 1 if applicable 
       consentObject.put("gdpr", "0") 
       // Provide user consent in IAB format 
       consentObject.put(InMobiSdk.IM_GDPR_CONSENT_IAB, " << consent in IAB format >> ") 
    } catch (e:JSONException) { 
       e.printStackTrace() 
    } 
    InMobiSdk.init(this, "Insert InMobi Account ID here", consentObject,  SdkInitializationListener() { 
       @Override 
       fun onInitializationComplete(error : Error?) { 
           if (null != error) { 
               Log.e(TAG, "InMobi Init failed -" + error.getMessage()) 
           } else { 
               Log.d(TAG, "InMobi Init Successful") 
           } 
       } 
    }) 
    

Let's understand a few things here before you proceed to the next step:  
  
**What is a consentObject?** A consentObject is a JSONObject representation of
all kind of consent provided by the publisher to the SDK. The key is mandatory
if you wish to monetize traffic from European Economic Area; InMobi relies on
publishers to obtain user consent to comply with the regulations. You can read
further on GDPR regulations [here](https://gdpr.eu/faq/).

**Key** | **Type** | **Inference**  
---|---|---  
gdpr_consent | String | A consent string is a series of numbers, which identifies the consent status of an Ad tech Vendor. The string must follow the IAB contracts as mentioned [here](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework/blob/master/Consent%20string%20and%20vendor%20list%20formats%20v1.1%20Final.md). The key, gdpr_consent can be accessed via string constant IM_GDPR_CONSENT_IAB.  
gdpr_consent_available | boolean |  **true:** Publisher has provided consent to collect and use user's data. **false:** \- Publisher has not provided consent to collect and use user's data. **Any value other than "true" and "false" is invalid and will be treated as value not provided by publisher, i.e. empty value.** The key gdpr_consent_available can be accessed via string constant IM_GDPR_CONSENT_AVAILABLE.  
gdpr | String | Whether or not the request is subjected to GDPR regulations, deviation from the set values (0 = No, 1 = Yes ), indicate an unknown entity.  
  
#### Note

  1. You need to provide **`consentObject`** in every session. The SDK does not persist consent, it only keeps the **`consentObject`** in memory. If the app is relaunched or crashes - SDK will lose the **`consentObject`**.
  2. Within a session, you can update the consent this way:

#### Java

    
        InMobiSdk.updateGDPRConsent(JSONObject consentObject)	
    

#### Kotlin

    
        InMobiSdk.updateGDPRConsent(consentObject:JSONObject)
    	
    
    
    	
    
    	
      3. As part of the General Data Protection Regulation ("GDPR") publishers who collect data on their apps, are required to have a legal basis for collecting and processing the personal data of users in the European Economic Area ("EEA"). Please ensure that you obtain appropriate consent from the user before making ad requests to InMobi for Europe and indicate the same by following our recommended SDK implementation. Please do not pass any demographics information of a user, if you do not have user consent from such user in Europe.
    
    
    
    
    
    
    
    
    
    ## Optimization
    
    
    
    
    
    ### **A. Pass location signals to allow better ad targeting**
    
    
    
    
    
    
    
    
    #### Recommended
    
    
    
    
    
    If your app collects location from the user, we recommend passing it up, as impressions with location signal have higher revenue potential. InMobi SDK will automatically pass the location signals if available in the app. If you use location in your app but would like to disable passing location signals to InMobi, then **TURN OFF** the "**Location Automation** " for your property on the InMobi dashboard.
    
    
    
    
    
    
    
    
    ![](https://cdn2.hubspot.net/hubfs/2714195/SUPPORT%20PORTAL%20images/ANDROID/Android%20Main/Step%203.2.png)
    
    
    
    
    
    Otherwise, you can pass the location signals as follows:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiSdk.setLocation(locationObj);
    

#### Kotlin

    
    
    InMobiSdk.setLocation(locationObj)
    
    
    
    
    
    
    Alternatively, you can set the city, state, and country as well:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiSdk.setLocationWithCityStateCountry("city","state","country");
    

#### Kotlin

    
    
    InMobiSdk.setLocationWithCityStateCountry("city","state","country")
    
    
    
    
    
    
    ### **B. Pass demographic signals to allow better ad targeting**
    
    
    
    
    
    InMobi relies on the publishers to obtain explicit consent from users for continuing business activities in the EU as per GDPR. You can supply the InMobi SDK with the gender and age as follows:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiSdk.setGender(InMobiSdk.Gender.MALE); // or InMobiSdk.Gender.FEMALE
    InMobiSdk.setAge(age);
    InMobiSdk.setAgeGroup(InMobiSdk.AgeGroup.BELOW_18);
       // other enums: BETWEEN_18_AND_20, BETWEEN_21_AND_24, BETWEEN_25_AND_34
       // BETWEEN_35_AND_5, ABOVE_55
    

#### Kotlin

    
    
    InMobiSdk.setGender(InMobiSdk.Gender.MALE)  // or InMobiSdk.Gender.FEMALE 
    InMobiSdk.setAge(age) 
    InMobiSdk.setAgeGroup(InMobiSdk.AgeGroup.BELOW_18) 
    
    
    
    
    
    
    
    
    
    #### Recommended
    
    
    
    
    
    Passing location signals helps better ad targeting and ensures the ads served on your app are contextual and highly relevant to your users.
    
    
    
    
    
    
    
    
    
    
    
    ### **C. Children Privacy and Family Apps**
    
    
    
    
    
    We recommended using age restriction information as well to comply with policies such as the data practices for Google's Family Apps. You must determine the definition of age restriction depending on the user's geographic data location. If the value is passed as True, the InMobi SDK will not transmit device identifiers such as ("AAID" in Android & "IDFA" in iOS). Note that the default value will be False.
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiSdk.setIsAgeRestricted(false) // possible value are true, false;
    

#### Kotlin

    
    
    InMobiSdk.setIsAgeRestricted(false) // possible value are true, false
    
    
    
    
    
    
    ### **D. AD_ID Permission (Android Advertising ID)**
    
    
    
    
    
    For app developers using the Android Advertising ID, you must declare AD_ID permission when your apps target Android 13 or above, as per Google's announcement. If the AD_ID permission is not declared, the system shows a string of zeros.
    
    
    
    
    
    The InMobi SDK supports the AD_ID permission starting from version 10.0.5. For targeting Android 13 and above, you can declare the AD_ID permission in the manifest file as follows:
    
    
    
    
    
    
    <uses-permission android:name="com.google.android.gms.permission.AD_ID"/>
    

You are all set now! Now let's look at how you can set up different ad formats
and begin monetizing. Ready?

  * [Banner Ads](https://support.inmobi.com/monetize/android-guidelines/banner-ads-for-android/)
  * [Interstitial Ads](https://support.inmobi.com/monetize/android-guidelines/interstitial-ads-for-android/)
  * [In-Stream Video Ads](https://support.inmobi.com/monetize/sdk-documentation/android-guidelines/in-stream-video-ads-android)
  * [Rewarded Video Ads](https://support.inmobi.com/monetize/android-guidelines/rewarded-video-ads-for-android/)
  * [Native Ads](https://support.inmobi.com/monetize/android-guidelines/native-ads-for-android/)

#### On This Page

Last Updated on: 29 Aug, 2024

  * [Support Center](/)
  * [InMobi Publisher Platform](/monetize)
  * [SDK Documentation](/monetize/sdk-documentation/download-sdk)
  * [Android Guidelines](/monetize/sdk-documentation/android-guidelines/overview-android-guidelines)
  * Migrating to SDK 10.7.X

# Migrating to SDK 10.7.X

## Direct Integration

### Integration via Gradle

  1. Include mavenCentral in your top-level build.gradle file:
    
        allprojects { 
        repositories { 
            mavenCentral() 
        } 
    }
    

  2. Add the following line to the dependencies element in your application module's build.gradle.
    
         implementation 'com.inmobi.monetization:inmobi-ads-kotlin:10.7.6'
    	
    
    
    
    
    
    
    ### Manual Integration
    
    
    
    
    
    Alternatively, you can download the latest version of [InMobi's Kotlin SDK](https://dl.inmobi.com/inmobi-sdk/IM/InMobi-Android-SDK-10.7.4.zip) and copy the library to your application module's libs/directory.
    
    
    
    
    
    
    	
      1. 
    	
    
    Please add the following dependencies to your modules 'build.gradle' for integrating inmobi-ads-kotlin in addition to the dependencies mentioned in the support portal.
    
    
    
    	
    
        implementation "androidx.core:core-ktx:1.5.0" 
    implementation "com.inmobi.omsdk:inmobi-omsdk:1.4.12.0"
    

  2. Follow the next steps from [Add & Verify Dependencies](https://support.inmobi.com/monetize/android-guidelines/#add-&-verify-dependencies).

#### On This Page

Last Updated on: 29 Aug, 2024

  * [Support Center](/)
  * [InMobi Publisher Platform](/monetize)
  * [SDK Documentation](/monetize/sdk-documentation/download-sdk)
  * [Android Guidelines](/monetize/sdk-documentation/android-guidelines/overview-android-guidelines)
  * Banner Ads

# Banner Ads

## Set up a Banner Ad

  1. From the left navigation, select **Inventory Inventory Settings**.
  2. Search for the app or website you would like to create a placement for and click **\+ Add a placement**.
  3. Click **Select Ad Unit** and select **Banner**.
  4. Click **Add a placement** to start setting up your banner settings. After you create the banner placement, you can see the placement ID.

**![](/ui/uploads/banner_placement.png)**

## Add the Banner Ad to your App

### **Creating a Banner Ad**

### **Option 1: Adding a Banner in XML layout resource files**

You can add a banner ad in your layout resource file in XML and reference it
in your code as you would in a regular view.

The following snippet shows how to add a banner ad in XML. Note the InMobi ads
namespace that you need to add to the top-level layout element to add the
banner.

    
    
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" 
        xmlns:ads="http://schemas.android.com/apk/lib/com.inmobi.ads" 
        xmlns:tools="http://schemas.android.com/tools"  
        android:layout_width="match_parent" 
        android:layout_height="match_parent" 
       ...  
       > 
      
        <com.inmobi.ads.InMobiBanner 
            android:layout_width="320dp" 
            android:layout_height="50dp" 
            android:id="@+id/banner" 
            ads:placementId="plid-1431977751489005" 
            ads:refreshInterval="60" 
        /> 
    </LinearLayout>
    

For banner XML integration, publishers using Android SDK 720 and onwards needs
to append "plid-" to `placementId` TAG as following:` `

    
    
    ads:placementId="plid-1431977751489005"
    
    

Now, you can reference the banner in your code:

#### Java

    
    
    InMobiBanner bannerAd = (InMobiBanner)findViewById(R.id.banner);
    

#### Kotlin

    
    
    val bannerAd:InMobiBanner = findViewById(R.id.banner)
    
    
    
    
    
    
    Once you have the banner instance, you can request for ads to be loaded as shown in the following sections.
    
    
    
    
    
    Before you do that, call the InMobiSdk.init(Context, String) method in your main activity or the activity where you are displaying banner ad to initialize the InMobi SDK.
    
    
    
    
    
    ### **Option 2: Adding a Banner in code**
    
    
    
    
    
    To add a banner ad in Android code, create an instance of InMobiBanner:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiBanner bannerAd = new InMobiBanner(BannerAdsActivity.this, 1468078426600L); 
    

#### Kotlin

    
    
    val bannerAd = InMobiBanner(this@BannerAdsActivity, 1468078426600L)
    
    
    
    
    
    
    
    
    
    #### Note
    
    
    
    
    
    
    	
      * The InMobiBanner class is not thread-safe. A banner instance must be created on the UI thread.
    
    	
      * Similarly, all methods on this instance must be called on the UI thread. Not doing so will lead to unpredictable behavior and may affect your ability to monetize with InMobi.
    
    	
      * Creating an InMobiBanner object before SDK initialization will throw an exception.
    
    
    
    
    
    
    
    
    
    Once you have created a banner ad, you can add it to the view hierarchy:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    RelativeLayout adContainer = (RelativeLayout) findViewById(R.id.ad_container);
    RelativeLayout.LayoutParams bannerLp = new RelativeLayout.LayoutParams( < WIDTH_IN_PIXEL > , < HEIGHT_IN_PIXEL > );
    bannerLp.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM);
    bannerLp.addRule(RelativeLayout.CENTER_HORIZONTAL);
    adContainer.addView(bannerAd, bannerLayoutParams);
    

#### Kotlin

    
    
    val adContainer:RelativeLayout = findViewById(R.id.ad_container) 
    val bannerLp:RelativeLayout.LayoutParams = RelativeLayout.LayoutParams( < WIDTH_IN_PIXEL > , < HEIGHT_IN_PIXEL > ) 
    bannerLp.addRule(RelativeLayout.ALIGN_PARENT_BOTTOM) 
    bannerLp.addRule(RelativeLayout.CENTER_HORIZONTAL) 
    adContainer.addView(bannerAd, bannerLayoutParams)
    
    
    
    
    
    
    
    
    
    #### Note
    
    
    
    
    
    
    	
      * You should specify the banner view dimensions in pixel units when setting the layout parameters for the banner ad.
    
    	
      * Also, it is a programming error to supply WRAP_CONTENT as the layout parameters for a banner ad. This constraint applies whether you create a banner in your XML layout resource file or in code.
    
    	
      * If you are building for both phones and tablets, you can supply MATCH_PARENT as the layout parameters for the banner. The InMobi SDK will correctly compute the banner view dimensions and use them to fetch an ad from the InMobi Network.
    
    
    
    
    
    
    
    
    
    ## Loading a Banner Ad
    
    
    
    
    
    Loading a banner ad requires you to add the banner ad view to your view hierarchy before requesting for an ad on the **InMobiBanner** instance. Adding the view to the view hierarchy enables the InMobi SDK to correctly compute the banner view dimensions and to request for the best ad matching those dimensions from the network.
    
    
    
    
    
    Once you have added **InMobiBanner** to the view hierarchy, you can call the **load()** method on the instance you just created to request for an ad.
    
    
    
    
    
    ## Optimization
    
    
    
    
    
    #### **Setting up Auto-refresh for your Banner Ad**
    
    
    
    
    
    The banner ads refresh automatically after the first time you requested for an ad by calling load() on an **InMobiBanner** instance. You can set up auto-refresh either while creating a banner in XML layout resource file, or later in code, by calling the **setRefreshInterval(int)** method on a banner ad.
    
    
    
    
    
    The sample below shows how to do this in XML:
    
    
    
    
    
    
    <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" 
        xmlns:ads="http://schemas.android.com/apk/lib/com.inmobi.ads" 
        xmlns:tools="http://schemas.android.com/tools"  
    android:layout_width="match_parent" 
        android:layout_height="match_parent"  
       ...
       >  
         
        <com.inmobi.ads.InMobiBanner 
            android:layout_width="320dp" 
            android:layout_height="50dp" 
            android:id="@+id/banner" 
            ads:placementId="plid-1431977751489005" 
    ads:refreshInterval="60" 
        /> 
    </LinearLayout>
    

#### **Animating Banner Ad Refreshes**

You can choose an animation style that takes effect when a banner is
refreshed. You can also choose to turn OFF any animation for banner refreshes.

To do so, you can call the `setAnimationType(InMobiBanner.AnimationType)`
method after obtaining a banner instance.

#### Note

The default animation is set to `AnimationType.ROTATE_HORIZONTAL_AXIS`. If you
want to turn this off, call the `setAnimationType` method with the
`AnimationType.ANIMATION_OFF` parameter.

#### **Listening for Banner Ad Lifecycle Events**

If you want to listen for key events in the banner lifecycle, you should
implement the `BannerAdListener` interface. You can then set this listener
using the `setListener(BannerAdListener)` method on the `InMobiBanner`
instance. A brief description of each event is as follows.

#### Java

    
    
    /**
    * A listener for receiving notifications during the lifecycle of a banner ad.
    */
    public abstract class BannerAdEventListener {
        /**  
         * Called to notify that an ad was received successfully but is not ready to be displayed yet.  
         *  
         * @param ad   Represents the ad which was loaded or preloaded  
         * @param info Represents the ad meta information  
         */ 
        public void onAdFetchSuccessful(@NonNull InMobiBanner ad, @NonNull AdMetaInfo info) {} 
        /**  
         * Called to notify that an ad was successfully loaded.  
         * @param ad Represents the {@link InMobiBanner} ad which was loaded  
         * @param info Represents the ad meta information  
         */ 
        public void onAdLoadSucceeded(@NonNull InMobiBanner ad, @NonNull AdMetaInfo info) {} 
        /**  
         * Called to notify that a request to load an ad failed.  
         * @param ad Represents the {@link InMobiBanner} ad which failed to load  
         * @param status Represents the {@link InMobiAdRequestStatus} status containing error reason
         */ 
        public void onAdLoadFailed(@NonNull InMobiBanner ad, @NonNull InMobiAdRequestStatus status) {} 
        /**  
         * Called to notify that the user interacted with the ad.  
         * @param ad Represents the {@link InMobiBanner} ad on which user clicked  
         * @param params Represents the click parameters  
         */ 
        public void onAdClicked(@NonNull InMobiBanner ad, Map < Object, Object > params) {} 
        /**  
         * Called to notify that the banner ad was displayed  
         * @param ad Represents the {@link InMobiBanner} ad which was displayed  
         */ 
        public void onAdDisplayed(@NonNull InMobiBanner ad) {} 
        /**  
         * Called to notify that the User is about to return to the application after closing the ad.  
         * @param ad Represents the {@link InMobiBanner} ad which was closed  
         */ 
        public void onAdDismissed(@NonNull InMobiBanner ad) {} 
        /**  
         * Called to notify that the user is about to leave the application as a result of interacting with the ad.  
         * @param ad Represents the {@link InMobiBanner} ad  
         */ 
        public void onUserLeftApplication(@NonNull InMobiBanner ad) {} 
        /**  
         * Called to notify that a reward was unlocked.  
         * @param ad Represents the {@link InMobiBanner} ad for which rewards was unlocked  
         * @param rewards Represents the rewards unlocked  
         */ 
        public void onRewardsUnlocked(@NonNull InMobiBanner ad, Map < Object, Object > rewards) {} 
        /** 
         * Called to notify that inmobi has logged an impression for the ad 
         * @param ad     Represents the ad which was impressed 
         */ 
        public void onAdImpression(@NonNull InMobiBanner ad) { 
        } 
    }
    

#### Kotlin

    
    
    /**
    * A listener for receiving notifications during the lifecycle of a banner ad.
    */
    abstract class BannerAdEventListener : AdEventListener<inmobibanner>() {
    /**
        * Called to notify that an ad preload has failed.  
        *  
        ***Note** This notification is given only when you use `preload()` in  
        * [InMobiBanner.preloadManager]  
        *  
        * @param ad     Represents the [InMobiBanner] ad which was preloaded  
        * @param status Represents the [InMobiAdRequestStatus] status containing error reason 
        */  
    open fun onAdFetchFailed(ad: InMobiBanner, status: InMobiAdRequestStatus) {}
    /**
        * Called to notify that the banner ad has expanded  
        *  
        * @param ad Represents the [InMobiBanner] ad which was expanded  
        */  
    open fun onAdDisplayed(ad: InMobiBanner) {}
    /**
        * Called to notify that the User is about to return to the application after closing the ad.  
        *  
        * @param ad Represents the [InMobiBanner] ad which was closed  
        */  
    open fun onAdDismissed(ad: InMobiBanner) {}
    /**
        * Called to notify that the user is about to leave the application as a result of interacting with the ad.  
        *  
        * @param ad Represents the [InMobiBanner] ad  
        */  
    open fun onUserLeftApplication(ad: InMobiBanner) {}
    /**
        * Called to notify that a reward was unlocked.  
        *  
        * @param ad      Represents the [InMobiBanner] ad for which rewards was unlocked  
        * @param rewards Represents the rewards unlocked  
        */  
    open fun onRewardsUnlocked(ad: InMobiBanner, rewards: Map<any, any="">) {}
        /** 
         * Called to notify that inmobi has logged an impression for the ad 
         * @param ad     Represents the ad which was impressed 
         */ 
    open fun onAdImpression(ad: InMobiBanner) {}
    }
    
    
    
    
    
    
    You can check the code samples for banner ad integrations on GitHub [here](https://github.com/InMobi/sdk-sample-code-android/tree/master/samples/bannerSample).
    
    
    
    
    
    #### **Deprecating Banner**
    
    
    
    
    
    If you're done with the Banner object, then simply call deprecate on the same to release the resources. This will do the following:
    
    
    
    
    
    
    	
      1. Remove the ad-view from the view hierarchy.
    
    	
      2. Cancel any ongoing refresh.
    
    	
      3. De-reference the listeners.
    
    	
      4. Other clean-ups.
    
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    bannerAd.destroy(); // bannerAd is an example instance.
    
    

#### Kotlin

    
    
    bannerAd.destroy() // bannerAd is an example instance.
    
    
    
    
    
        
            
    
    
            
            
    
    
            
    
    
        
    
    
        
    
    
            
    
    
                
    
    #### On This Page
    
    
            
    
    
        
    
    
        
    
    
            Last Updated on: 01 Aug, 2022
        
    
    
    
    
     
    
    
    
    
                    
                        
    
        
    
    
            
      * [Support Center](/)
    
            
            
      * [InMobi Publisher Platform](/monetize)
    
            
            
            
        
                    
                
                
                                
                  
                        
                
                        
                    
                                                    
            
      * [SDK Documentation](/monetize/sdk-documentation/download-sdk)
    
         
                                        
                    
                                        
                    
                    
                                        
                    
                    
                                        
                    
                                        
                
                      
                
                
                                
                
                       
                
                        
      * [Android Guidelines](/monetize/sdk-documentation/android-guidelines/overview-android-guidelines)
    
                      
         
                
            
      * Interstitial Ads
    
        
    
           
    
    
    
        
        
    
    
            
    
    
                
    
    # Interstitial Ads
    
    
            
    
    
            
    
    
                
    
    
    
    
    We support both static and video interstitial ads. Follow the instructions below to set up interstitial ads.
    
    
    
    
    
    ## Set up Interstitial Ad
    
    
    
    
    
    
    
    
    
    
    
    
    	
      1. From the left navigation, select **Inventory Inventory Settings.**
    
    	
      2. Search for the app or website you would like to create a placement for and click **+ Add a placement**.
    
    	
      3. Click **Select Ad Unit** and select **Interstitial**.
    
    	
      4. Click **Add a placement** to start setting up your Interstitial settings.
    
    	
      5. 
    	
    
    From there you can select your Ad Experience template. If you haven't created an Ad Experience template yet, you can select the default Interstitial ad template created by InMobi which can contain both static and video creatives. You can always create your own template from **Inventory Ad Experience Template**. For more information, see [Ad Experience Settings](/monetize/publisher-dashboard/inventory-tab/ad-experience-settings). After you create the Interstitial placement, you can see the placement ID. ![](/ui/uploads/interstitial_placement.png)
    
    
    	
    
    
    
    
    
    
    
    
    
    
    
    
    ## Add Interstitial Ad to your App
    
    
    
    
    
    
    
    
    
    
    
    ### **Creating Interstitial Ad**
    
    
    
    
    
    To create an interstitial ad, create an instance of an InMobiInterstitial:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiInterstitial interstitialAd = new InMobiInterstitial(InterstitialAdsActivity.this, 1471550843414L, 
    mInterstitialAdEventListener);
    

#### Kotlin

    
    
    val interstitialAd = InMobiInterstitial(this@InterstitialAdsActivity, 1471550843414L, mInterstitialAdEventListener )
    
    
    
    
    
    
    Here, mInterstitialAdEventListener is an implementation of the InterstitialAdEventListener Abstract class. It is mandatory to supply an implementation of this abstract class to create an interstitial ad.
    
    
    
    
    
    
    
    
    
    
    
    #### Warning
    
    
    
    
    
    
    	
      * The InMobiInterstitial class is not thread-safe. An interstitial instance must be created on the UI thread.
    
    	
      * Similarly, all methods on this instance must be called on the UI thread. Not doing so will lead to unpredictable behavior and may affect your ability to monetize with InMobi.
    
    	
      * Creating an InMobi Interstitial object without SDK Initialization will throw an exception.
    
    
    
    
    
    
    
    
    
    
    
    
    InterstitialAdEventListener abstract class allows you to listen to key lifecycle events for an interstitial ad. You should listen to these events to ensure that your application correctly handles the various lifecycle transitions.
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    /**
    * Listener for receiving notifications during the lifecycle of an interstitial.
    */
    public abstract class InterstitialAdEventListener {
        /**  
         * Called to indicate that an ad was loaded and it can now be shown. This will always be called  
         * after the {@link ##onAdFetchSuccessful(InMobiInterstitial, AdMetaInfo)} callback.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad which was loaded  
         * @param info Represents the ad meta information  
         */ 
        public void onAdLoadSucceeded(@NonNull InMobiInterstitial ad, @NonNull AdMetaInfo info) {} 
        /**  
         * Callback to signal that a request to fetch an ad (by calling  
         * {@link InMobiInterstitial##load()} failed. The status code indicating the reason for failure  
         * is available as a parameter. You should call {@link InMobiInterstitial##load()} again to  
         * request a fresh ad.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad which failed to load  
         * @param status Represents the {@link InMobiAdRequestStatus} status containing error reason  
         */ 
        public void onAdLoadFailed(@NonNull InMobiInterstitial ad, @NonNull InMobiAdRequestStatus status) {} 
        /**  
         * Called to indicate that an ad is available in response to a request for an ad (by calling  
         * {@link InMobiInterstitial##load()}. Note: This does not  
         * indicate that the ad can be shown yet. Your code should show an ad after the  
         * {@link ##onAdLoadSucceeded(InMobiInterstitial)} method is called. Alternately, if you do not  
         * want to handle this event, you must test if the ad is ready to be shown by checking the  
         * result of calling the {@link InMobiInterstitial##isReady()} method.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad for which ad content was received  
         * @param info Represents the ad meta information  
         */ 
        public void onAdFetchSuccessful(@NonNull InMobiInterstitial ad, @NonNull AdMetaInfo info) {} 
        /**  
         * Called to indicate that an ad interaction was observed.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad on which user clicked  
         * @param params Represents the click parameters  
         */ 
        public void onAdClicked(@NonNull InMobiInterstitial ad, Map < Object, Object > params) {} 
        /**  
         * Called to indicate that the ad will be launching a fullscreen overlay.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad which will display  
         */ 
        public void onAdWillDisplay(@NonNull InMobiInterstitial ad) {} 
        /**  
         * Called to indicate that the fullscreen overlay is now the topmost screen.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad which is displayed  
         * @param info Represents the ad meta information  
         */ 
        public void onAdDisplayed(@NonNull InMobiInterstitial ad, @NonNull AdMetaInfo info) {} 
        /**  
         * Called to indicate that a request to show an ad (by calling {@link InMobiInterstitial##show()}  
         * failed. You should call {@link InMobiInterstitial##load()} to request for a fresh ad.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad which failed to show  
         */ 
        public void onAdDisplayFailed(@NonNull InMobiInterstitial ad) {} 
        /**  
         * Called to indicate that the fullscreen overlay opened by the ad was closed.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad which was dismissed  
         */ 
        public void onAdDismissed(@NonNull InMobiInterstitial ad) {} 
        /**  
         * Called to indicate that the user may leave the application on account of interacting with the ad.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad  
         */ 
        public void onUserLeftApplication(@NonNull InMobiInterstitial ad) {} 
        /**  
         * Called to indicate that rewards have been unlocked.  
         *  
         * @param ad Represents the {@link InMobiInterstitial} ad for which rewards was unlocked  
         * @param rewards Represents the rewards unlocked  
         */ 
        public void onRewardsUnlocked(@NonNull InMobiInterstitial ad, Map < Object, Object > rewards) {} 
        /** 
         * Called to notify that inmobi has logged an impression for the ad 
         * @param ad     Represents the ad which was impressed 
         */ 
        public void onAdImpression(@NonNull InMobiInterstitial ad) { 
        } 
    }
    

#### Kotlin

    
    
    /**
    * Listener for receiving notifications during the lifecycle of an interstitial.
    */
    abstract class InterstitialAdEventListener : AdEventListener<inmobiinterstitial>() {
    /**
        * Called to notify that an ad preload has failed.  
        *  
        ***Note** This notification is given only when you use `preload()` in  
        * [InMobiInterstitial.preloadManager]  
        *  
        * @param ad     Represents the [InMobiInterstitial] ad which was preloaded  
        * @param status Represents the [InMobiAdRequestStatus] status containing error reason  
        */  
    open fun onAdFetchFailed(ad: InMobiInterstitial, status: InMobiAdRequestStatus) {}
    /**
        * Called to indicate that the ad will be launching a fullscreen overlay.  
        *  
        * @param ad Represents the [InMobiInterstitial] ad which will display  
        */  
    open fun onAdWillDisplay(ad: InMobiInterstitial) {}
    /**
        * Called to indicate that the fullscreen overlay is now the topmost screen.  
        *  
        * @param ad   Represents the [InMobiInterstitial] ad which is displayed  
        * @param info Represents the meta info for the ad displayed  
        */  
    open fun onAdDisplayed(ad: InMobiInterstitial, info: AdMetaInfo) {}
    /**
        * Called to indicate that a request to show an ad (by calling [InMobiInterstitial.show]  
        * failed. You should call [InMobiInterstitial.load] to request for a fresh ad.  
        *  
        * @param ad Represents the [InMobiInterstitial] ad which failed to show  
        */  
    open fun onAdDisplayFailed(ad: InMobiInterstitial) {}
    /**
        * Called to indicate that the fullscreen overlay opened by the ad was closed.  
        *  
        * @param ad Represents the [InMobiInterstitial] ad which was dismissed  
        */  
    open fun onAdDismissed(ad: InMobiInterstitial) {}
    /**
        * Called to indicate that the user may leave the application on account of interacting with the ad.  
        *  
        * @param ad Represents the [InMobiInterstitial] ad  
        */  
    open fun onUserLeftApplication(ad: InMobiInterstitial) {}
    /**
        * Called to indicate that rewards have been unlocked.  
        *  
        * @param ad      Represents the [InMobiInterstitial] ad for which rewards was unlocked  
        * @param rewards Represents the rewards unlocked  
        */  
    open fun onRewardsUnlocked(ad: InMobiInterstitial, rewards: Map<any, any="">) {}
    /**
         * Called to notify that inmobi has logged an impression for the ad 
         * @param ad     Represents the ad which was impressed 
         */ 
    open fun onAdImpression(ad: InMobiInterstitial) {}
    }
    
    
    
    
    
    
    ## Loading an Interstitial Ad
    
    
    
    
    
    To request for an interstitial ad, call the load() method on the InMobiInterstitial instance:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    interstitialAd.load();
    

#### Kotlin

    
    
    interstitialAd.load()
    
    
    
    
    
    
    InterstitialAdEventListener abstract class notifies the result of this method. If the ad request was successful, the onAdFetchSuccessful(InMobiInterstitial, AdMetaInfo) event is generated. This is followed by either the onAdLoadSucceeded or the onAdLoadFailed event.
    
    
    
    
    
    If the onAdLoadFailed event is generated, the reason is indicated by the InMobiAdRequestStatus object passed in this event.
    
    
    
    
    
    If the onAdLoadSucceeded event is generated, you can show the ad anytime after this by calling show() on the InMobiInterstitial instance.
    
    
    
    
    
    
    
    
    #### Note
    
    
    
    
    
    Calling load() on the same interstitial ad after the onAdLoadSucceeded event is generated by the SDK is not guaranteed to request a fresh ad from the network. A fresh ad will only be fetched if either the previous ad was discarded by the SDK, or if the ad expired or the user cleared application data and caches.
    
    
    
    
    
    
    
    
    ##   
    
    Showing an Interstitial Ad
    
    
    
    
    
    To show an interstitial ad, call show() on the InMobiInterstitial instance anytime after the onAdLoadSucceeded event has been generated by the SDK. The code fragment below illustrates the same.
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiInterstitial interstitialAd;
    InterstitialAdEventListener mInterstitialAdEventListener = new InterstitialAdEventListener() {
        // implementation for other events 
        // onAdFetchSuccessful, onAdLoadFailed, etc 
        @Override
        public void onAdLoadSucceeded(@NonNull InMobiInterstitial inMobiInterstitial, @NonNull AdMetaInfo info) {
            Log.d(TAG, "Ad can now be shown!");
            mCanShowAd = true;
        }
    };
    void init() {
        InMobiInterstitial interstitialAd = new InMobiInterstitial(GameActivity.this, 1471550843414 L, mInterstitialAdEventListener);
    }
    void prepareGameLevel() {
        interstitialAd.load();
    }
    void handleGameLevelCompleted() {
        If(mCanShowAd) interstitialAd.show();
    }
    

#### Kotlin

    
    
    val interstitialAd: InMobiInterstitial 
    val mInterstitialAdEventListener = InterstitialAdEventListener() { 
       // implementation for other events 
       // onAdFetchSuccessful, onAdLoadFailed, etc 
       override fun onAdLoadSucceeded(inMobiInterstitial: InMobiInterstitial, info: AdMetaInfo) { 
           Log.d(TAG, "Ad can now be shown!") 
           mCanShowAd = true 
       } 
    } 
    fun init() { 
       val interstitialAd = InMobiInterstitial(this@GameActivity, 1471550843414L, mInterstitialAdEventListener) 
    } 
    fun prepareGameLevel() { 
       interstitialAd.load() 
    } 
    fun handleGameLevelCompleted() { 
       if(mCanShowAd) interstitialAd.show() 
    } 
    
    
    
    
    
    
    Your application will be notified of the result of this request via the InterstitialAdEventListener abstract class.
    
    
    
    
    
    If the ad can be shown, the SDK will notify your code by calling on the onAdWillDisplay interface, followed by calling the onAdDisplayed method when the ad is actually presented on the screen.
    
    
    
    
    
    If the ad cannot be displayed, the onAdDisplayFailed event is generated by the SDK to let your application know that the ad could not be displayed. You can request for a fresh ad by calling load() again to handle this event.
    
    
    
    
    
    When an interstitial ad is dismissed, your application will be notified in the onAdDismissed callback.
    
    
    
    
    
    You can check the code samples for interstitial ad integrations on GitHub [here](https://github.com/InMobi/sdk-sample-code-android/tree/master/samples/interstitialSample).
    
    
    
    
        
            
    
    
            
            
    
    
            
    
    
        
    
    
        
    
    
            
    
    
                
    
    #### On This Page
    
    
            
    
    
        
    
    
        
    
    
            Last Updated on: 01 Aug, 2022
        
    
    
    
    
     
    
    
    
    
                    
                        
    
        
    
    
            
      * [Support Center](/)
    
            
            
      * [InMobi Publisher Platform](/monetize)
    
            
            
            
        
                    
                
                
                                
                  
                        
                
                        
                    
                                                    
            
      * [SDK Documentation](/monetize/sdk-documentation/download-sdk)
    
         
                                        
                    
                                        
                    
                    
                                        
                    
                    
                                        
                    
                                        
                
                      
                
                
                                
                
                       
                
                        
      * [Android Guidelines](/monetize/sdk-documentation/android-guidelines/overview-android-guidelines)
    
                      
         
                
            
      * Rewarded Video Ads
    
        
    
           
    
    
    
        
        
    
    
            
    
    
                
    
    # Rewarded Video Ads
    
    
            
    
    
            
    
    
                
    
    
    
    
    ## Set up a Rewarded Video Ad
    
    
    
    
    
    
    
    
    
    
    
    
    	
      1. From the left navigation select **Inventory Inventory Settings**.
    
    	
      2. Search for the app or website you would like to create a placement for and click **+ Add a placement**.
    
    	
      3. Click **Select Ad Unit** and select **Rewarded Video**.
    
    	
      4. Click **Add a placement** to start setting up your rewarded video settings. After you create the rewarded video placement, you can see the placement ID.![](/ui/uploads/rewarded_placement.png)
    
    
    
    
    
    
    
    
    
    
    
    
    #### Important
    
    
    
    
    
    InMobi SDK provides you the callback in any case, so you could choose not to fill in anything and handle the rewards completely at your end.
    
    
    
    
    
    
    
    
    
    
    
    ##   
    
    Add Rewarded Video Ad to your App
    
    
    
    
    
    #### **Creating a Rewarded Video Ad**
    
    
    
    
    
    To create a rewarded video ad, create an instance of an InMobiInterstitial:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiInterstitial interstitialAd = new InMobiInterstitial(InterstitialAdsActivity.this, 1471550843414L, 
    mInterstitialAdEventListener);
    

#### Kotlin

    
    
    val interstitialAd = InMobiInterstitial(this@InterstitialAdsActivity, 1471550843414L, 
    mInterstitialAdEventListener)
    
    
    
    
    
    
    Here, mInterstitialAdEventListener is an implementation of the InterstitialAdEventListener abstract class. It is mandatory to supply an implementation of this interface to create an interstitial ad.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #### Note
    
    
    
    
    
    
    	
      * The InMobiInterstitial class is not thread-safe. An interstitial instance must be created on the UI thread.
    
    	
      * Similarly, all methods on this instance must be called on the UI thread. Not doing so will lead to unpredictable behavior and may affect your ability to monetize with InMobi.
    
    	
      * Creating an InMobiInterstitial object without SDK Initialization will throw an exception.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    The InterstitialAdEventListener abstract class allows you to listen to key lifecycle events for an interstitial ad. You should listen to these events to ensure that your application correctly handles the various lifecycle transitions.
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    /** 
     * Listener for receiving notifications during the lifecycle of an interstitial. 
     */
    public abstract class InterstitialAdEventListener {
        /** 
         * Called to indicate that an ad was loaded and it can now be shown. This will always be called 
         * after the {@link #onAdFetchSuccessful(InMobiInterstitial, AdMetaInfo)} callback. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad which was loaded 
         * @param info Represents the ad meta information 
         */
        public void onAdLoadSucceeded(@NonNull InMobiInterstitial ad, @NonNull AdMetaInfo info) {}
        /** 
         * Callback to signal that a request to fetch an ad (by calling 
         * {@link InMobiInterstitial#load()} failed. The status code indicating the reason for failure 
         * is available as a parameter. You should call {@link InMobiInterstitial#load()} again to 
         * request a fresh ad. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad which failed to load 
         * @param status Represents the {@link InMobiAdRequestStatus} status containing error reason 
         */
        public void onAdLoadFailed(@NonNull InMobiInterstitial ad, InMobiAdRequestStatus status) {}
        /** 
         * Called to indicate that an ad is available in response to a request for an ad (by calling 
         * {@link InMobiInterstitial#load()}.Note: This does not 
         * indicate that the ad can be shown yet. Your code should show an ad after the 
         * {@link #onAdLoadSucceeded(InMobiInterstitial)} method is called. Alternately, if you do not 
         * want to handle this event, you must test if the ad is ready to be shown by checking the 
         * result of calling the {@link InMobiInterstitial#isReady()} method. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad for which ad content was received 
         * @param info Represents the ad meta information 
         */
        public void onAdFetchSuccessful(@NonNull InMobiInterstitial ad, @NonNull AdMetaInfo info) {}
        /** 
         * Called to indicate that an ad interaction was observed. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad on which user clicked 
         * @param params Represents the click parameters 
         */
        public void onAdClicked(@NonNull InMobiInterstitial ad, Map < Object, Object > params) {}
        /** 
         * Called to indicate that the ad will be launching a fullscreen overlay. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad which will display 
         */
        public void onAdWillDisplay(@NonNull InMobiInterstitial ad) {}
        /** 
         * Called to indicate that the fullscreen overlay is now the topmost screen. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad which is displayed 
         * @param info Represents the ad meta information 
         */
        public void onAdDisplayed(@NonNull InMobiInterstitial ad, @NonNull AdMetaInfo info) {}
        /** 
         * Called to indicate that a request to show an ad (by calling {@link InMobiInterstitial#show()} 
         * failed. You should call {@link InMobiInterstitial#load()} to request for a fresh ad. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad which failed to show 
         */
        public void onAdDisplayFailed(@NonNull InMobiInterstitial ad) {}
        /** 
         * Called to indicate that the fullscreen overlay opened by the ad was closed. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad which was dismissed 
         */
        public void onAdDismissed(@NonNull InMobiInterstitial ad) {}
        /** 
         * Called to indicate that the user may leave the application on account of interacting with the ad. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad 
         */
        public void onUserLeftApplication(@NonNull InMobiInterstitial ad) {}
        /** 
         * Called to indicate that rewards have been unlocked. 
         * 
         * @param ad Represents the {@link InMobiInterstitial} ad for which rewards was unlocked 
         * @param rewards Represents the rewards unlocked 
         */
        public void onRewardsUnlocked(@NonNull InMobiInterstitial ad, Map < Object, Object > rewards) {}
    }
    

#### Kotlin

    
    
    /** 
    * Listener for receiving notifications during the lifecycle of an interstitial. 
    */ 
    abstract class InterstitialAdEventListener : AdEventListener<inmobiinterstitial>() { 
       /** 
        * Called to notify that an ad preload has failed. 
        * 
        ***Note** This notification is given only when you use `preload()` in 
        * [InMobiInterstitial.preloadManager] 
        * 
        * @param ad     Represents the [InMobiInterstitial] ad which was preloaded 
        * @param status Represents the [InMobiAdRequestStatus] status containing error reason 
        */ 
       open fun onAdFetchFailed(ad: InMobiInterstitial, status: InMobiAdRequestStatus) {} 
       /** 
        * Called to indicate that the ad will be launching a fullscreen overlay. 
        * 
        * @param ad Represents the [InMobiInterstitial] ad which will display 
        */ 
       open fun onAdWillDisplay(ad: InMobiInterstitial) {} 
       /** 
        * Called to indicate that the fullscreen overlay is now the topmost screen. 
        * 
        * @param ad   Represents the [InMobiInterstitial] ad which is displayed 
        * @param info Represents the meta info for the ad displayed 
        */ 
       open fun onAdDisplayed(ad: InMobiInterstitial, info: AdMetaInfo) {} 
       /** 
        * Called to indicate that a request to show an ad (by calling [InMobiInterstitial.show] 
        * failed. You should call [InMobiInterstitial.load] to request for a fresh ad. 
        * 
        * @param ad Represents the [InMobiInterstitial] ad which failed to show 
        */ 
       open fun onAdDisplayFailed(ad: InMobiInterstitial) {} 
       /** 
        * Called to indicate that the fullscreen overlay opened by the ad was closed. 
        * 
        * @param ad Represents the [InMobiInterstitial] ad which was dismissed 
        */ 
       open fun onAdDismissed(ad: InMobiInterstitial) {} 
       /** 
        * Called to indicate that the user may leave the application on account of interacting with the ad. 
        * 
        * @param ad Represents the [InMobiInterstitial] ad 
        */ 
       open fun onUserLeftApplication(ad: InMobiInterstitial) {} 
       /** 
        * Called to indicate that rewards have been unlocked. 
        * 
        * @param ad      Represents the [InMobiInterstitial] ad for which rewards was unlocked 
        * @param rewards Represents the rewards unlocked 
        */ 
       open fun onRewardsUnlocked(ad: InMobiInterstitial, rewards: Map<any, any="">) {} 
    }
    
    
    
    
    
    
    ##   
    
    Loading a Rewarded Ad
    
    
    
    
    
    To request for a interstitial ad, call the load() method on the InMobiInterstitial instance:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    interstitialAd.load();
    

#### Kotlin

    
    
    interstitialAd.load()
    
    
    
    
    
    
    You will be notified of the result of this method via the InterstitialAdEventListener event interface. If the ad request was successful, the onAdFetchSuccessful(InMobiInterstitial, AdMetaInfo) event will be generated. This will be followed by either the onAdLoadSucceeded or the onAdLoadFailed event. If the onAdLoadFailed event is generated, the reason is indicated by the InMobiAdRequestStatus object passed in this event. If the onAdLoadSucceeded event is generated, you may now show the ad anytime after this by calling show() on the InMobiInterstitial instance.
    
    
    
    
    
    
    
    
    #### Note
    
    
    
    
    
    Calling load() on the same interstitial ad after the onAdLoadSucceeded event is generated by the SDK is not guaranteed to request a fresh ad from the network. A fresh ad will only be fetched if either the previous ad was discarded by the SDK, or if the ad expired or the user cleared application data and caches.
    
    
    
    
    
    
    
    
    ##   
    
    Showing a Rewarded Video Ad
    
    
    
    
    
    To show a rewarded video ad, just call show() on the InMobiInterstitial instance anytime after the onAdLoadSucceeded event has been generated by the SDK. The code fragment below illustrates this:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InMobiInterstitial interstitialAd;
    InterstitialAdEventListener mInterstitialAdEventListener = new InterstitialAdEventListener() {
        // implementation for other events 
        // onAdFetchSuccessful, onAdLoaFailed, etc 
        @Override
        public void onAdLoadSucceeded(@NonNull InMobiInterstitial inMobiInterstitial, @NonNull AdMetaInfo info) {
            Log.d(TAG, "Ad can now be shown!");
            mCanShowAd = true;
        }
    };
    void init() {
        interstitialAd = new InMobiInterstitial(GameActivity.this, 1471550843414 L, mInterstitialAdEventListener);
    }
    void prepareGameLevel() {
        interstitialAd.load();
    }
    void handleGameLevelCompleted() {
        If(mCanShowAd) interstitialAd.show();
    }
    

#### Kotlin

    
    
    val interstitialAd: InMobiInterstitial 
    val mInterstitialAdEventListener = InterstitialAdEventListener() { 
       // implementation for other events 
       // onAdFetchSuccessful, onAdLoadFailed, etc 
       override fun onAdLoadSucceeded(inMobiInterstitial: InMobiInterstitial, info: AdMetaInfo) { 
           Log.d(TAG, "Ad can now be shown!") 
           mCanShowAd = true 
       } 
    } 
    fun init() { 
       val interstitialAd = InMobiInterstitial(this@GameActivity, 1471550843414L, mInterstitialAdEventListener) 
    } 
    fun prepareGameLevel() { 
       interstitialAd.load() 
    } 
    fun handleGameLevelCompleted() { 
       if(mCanShowAd) interstitialAd.show() 
    } 
    
    
    
    
    
    
    Your application will be notified of the result of this request via the InterstitialAdEventListener's callbacks. If the ad can be shown, then the SDK will notify your code by calling on the onAdWillDisplay interface, followed by calling the onAdDisplayed method when the ad is actually presented on the screen. If the ad cannot be displayed, the onAdDisplayFailed event is generated by the SDK to let your application know that the ad could not be displayed. You can request for a fresh ad by calling load() again to handle this event.
    
    
    
    
    
    When an interstitial ad is dismissed, your application will be notified in the onAdDismissed callback.
    
    
    
    
    
    
    
    
    
    
    
    ##   
    
    Implementing Callback for Rewards
    
    
    
    
    
    For rewarded video ads, the SDK will generate the onAdRewardActionCompleted event.
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    InterstitialAdEventListener mInterstitialAdEventListener = new InterstitialAdEventListener() { 
        // implementation for other events  
        // onAdLoadSucceeded, onAdDisplayed, etc  
        @Override 
        public void onRewardsUnlocked(@NonNull InMobiInterstitial inMobiInterstitial, Map < Object, Object > map) { 
            Log.d(TAG, "Ad rewards unlocked!"); 
            for (Object key: map.keySet()) { 
                Object value = map.get(key); 
                Log.v(TAG, "Unlocked " + value + " " + key); 
            } 
        } 
    };
    

#### Kotlin

    
    
    val mInterstitialAdEventListener: InterstitialAdEventListener = 
       object : InterstitialAdEventListener() { 
           // implementation for other events 
           // onAdLoadSucceeded, onAdDisplayed, etc 
           override fun onRewardsUnlocked( inMobiInterstitial: InMobiInterstitial, 
               map: Map<any, any=""> 
           ) { 
               Log.d(TAG, "Ad rewards unlocked!") 
               for (key in map.keys) { 
                   val value = map[key] 
                   Log.v(TAG, "Unlocked $value $key") 
               } 
           } 
       }
    
    
    
    
    
    
    You can check the code samples for interstitial ad integrations on GitHub [here](https://github.com/InMobi/sdk-sample-code-android/tree/master/samples/interstitialSample).
    
    
    
    
        
            
    
    
            
            
    
    
            
    
    
        
    
    
        
    
    
            
    
    
                
    
    #### On This Page
    
    
            
    
    
        
    
    
        
    
    
            Last Updated on: 18 May, 2023
        
    
    
    
    
     
    
    
    
    
                    
                        
    
        
    
    
            
      * [Support Center](/)
    
            
            
      * [InMobi Publisher Platform](/monetize)
    
            
            
            
        
                    
                
                
                                
                  
                        
                
                        
                    
                                                    
            
      * [SDK Documentation](/monetize/sdk-documentation/download-sdk)
    
         
                                        
                    
                                        
                    
                    
                                        
                    
                    
                                        
                    
                                        
                
                      
                
                
                                
                
                       
                
                        
      * [Android Guidelines](/monetize/sdk-documentation/android-guidelines/overview-android-guidelines)
    
                      
         
                
            
      * Native Ads
    
        
    
           
    
    
    
        
        
    
    
            
    
    
                
    
    # Native Ads
    
    
            
    
    
            
    
    
                
    
    InMobi Native Ads support both static and video ads. You can opt for In-Feed, Splash, or Pre-Roll formats. The steps for creating a native ad placement are given below.
    
    
    
    
    
    ## Set up Native Ad
    
    
    
    
    
    InMobi Native Ads support both static and video ads. You can opt for In-Feed, Splash , or Pre-Roll formats. The steps for creating a native ad placement are given below.
    
    
    
    
    
    
    	
      1. From the left navigation, select **Inventory Inventory Settings**.
    
    	
      2. Search for the app or website you would like to create a placement and click **+ Add a placement**.
    
    	
      3. Click **Select Ad Unit** and select **Native**.
    
    	
      4. Click **Add a placement** to start setting up your Native settings.
    
    	
      5. From there, you can select your Ad Experience template. If you haven't created an Ad Experience template yet, you can select the default Interstitial ad template created by InMobi, which can contain both static and video creatives. The default setting is an in-Feed ad layout, with an aspect ratio ranging between 256:135 - 1200x627.![](/ui/uploads/ad_exp_temp.png)
    
    
    
    
    
    
    You can always create your own native template by going to **Inventory Ad Experience Template** and select your chosen ad layout. For more information on Ad Experience Templates, see [Ad Experience Settings](/monetize/publisher-dashboard/inventory-tab/ad-experience-settings).
    
    
    
    
    
    Once the native placement is created, you will be able to see the placement ID.
    
    
    
    
    
    ![](/ui/uploads/native_placement.png)
    
    
    
    
    
     
    
    
    
    
    
    
    
    
    ## Add Native Ad to your App
    
    
    
    
    
    #### **Creating a Native Ad**
    
    
    
    
    
    To create a native ad, create an InMobiNative instance:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    public class NativeAdsActivity extends Activity { 
        …………………… 
        private final List<InMobiNative> mNativeAds = new ArrayList<>(); 
        …………………… 
        InMobiNative nativeAd = new InMobiNative(NativeAdsActivity.this, YOUR_PLACEMENT_ID, nativeAdEventListener); 
        nativeAd.load(); 
        mNativeAds.add(nativeAd); 
        …………………… 
    }
    

#### Kotlin

    
    
    class NativeAdsActivity : Activity { 
       …………………… 
       private val mNativeAds : List<inmobinative> = ArrayList() 
       …………………… 
       val nativeAd = InMobiNative(this@NativeAdsActivity, YOUR_PLACEMENT_ID, nativeAdEventListener) 
       nativeAd.load() 
       mNativeAds.add(nativeAd) 
       …………………… 
    }
    
    
    
    
    
    
    Here nativeAdEventListener is an implementation of the NativeAdEventListener abstract class. It is mandatory to supply an implementation of this interface to create a native ad. Creating an InMobiNative object without SDK Initialization will throw an exception.
    
    
    
    
    
    
    
    
    #### Mandatory
    
    
    
    
    
    You must supply a Context implementation to the InMobiNative constructor. Please make sure your implementation holds a strong reference of InMobiNative otherwise, you will not be able to get any callback from SDK for this reference. This can be achieved by making it a member variable of a class or storing it in the collection, which lives through your application life cycle.
    
    
    
    
    
    
    	
      * inMobiNative should always be a strong reference otherwise, you may not receive any callback (load success, load failure, etc.) for this reference.
    
    	
      * If inMobiNative is referenced by any variable, ensure that it is a strong reference.
    
    	
      * Use the android profiler to ensure that inMobiNative is not removed due to garbage collection.
    
    
    
    
    
    
    
    
    
    NativeAdEventListener abstract class allows you to listen to key lifecycle events for a native ad.
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    /**
    * A listener for receiving notifications during the lifecycle of a Native ad.
    */
    public abstract class NativeAdEventListener {
        /**  
         * Called to indicate that an ad is available in response to a request for an ad (by calling  
         * {@link InMobiNative##load()}. Note: This does not  
         * indicate that the ad can be shown yet. Your code should show an ad after the  
         * {@link ##onAdLoadSucceeded(InMobiNative)} method is called. Alternately, if you do not  
         * want to handle this event, you must test if the ad is ready to be shown by checking the  
         * result of calling the {@link InMobiNative##isReady()} method. 
         *  
         * @param ad Represents the {@link InMobiNative} ad for which ad content was received  
         */ 
        public void onAdReceived(InMobiNative ad) {} 
        /**  
         * Called to indicate that an ad was loaded and it can now be shown. This will always be called  
         * after the {@link ##onAdReceived(InMobiNative)} callback.  
         *  
         * @param ad Represents the {@link InMobiNative} ad which was loaded  
         */ 
        public void onAdLoadSucceeded(InMobiNative ad) {} 
        /**  
         * Called to notify that a native ad failed to load.  
         *  
         * @param ad  Represents the {@link InMobiNative} ad which failed to load  
         * @param requestStatus Represents the {@link InMobiAdRequestStatus} status containing error reason  
         */ 
        public void onAdLoadFailed(InMobiNative ad, InMobiAdRequestStatus requestStatus) {} 
        /**  
         *  
         * @param ad  Represents the {@link InMobiNative} ad whose fullscreen was dismissed  
         */ 
        public void onAdFullScreenDismissed(InMobiNative ad) {} 
        /**  
         * Called to notify that the ad will open an overlay that covers the screen.  
         *  
         * @param ad Represents the {@link InMobiNative} ad which will go fullscreen  
         */ 
        public void onAdFullScreenWillDisplay(InMobiNative ad) {} 
        /**  
         * Called to notify that the ad opened an overlay that covers the screen.  
         *  
         * @param ad Represents the {@link InMobiNative} ad whose fullscreen will be displayed  
         */ 
        public void onAdFullScreenDisplayed(InMobiNative ad) {} 
        /**  
         * Called to notify that the user is about to leave the application as a result of interacting with it.  
         *  
         * @param ad Represents the {@link InMobiNative} ad  
         */ 
        public void onUserWillLeaveApplication(InMobiNative ad) {} 
        /**  
         * Called to notify ad was clicked. Note:Override this method to notify click to the Mediation Adapter.  
         *  
         * @param ad Represents the {@link InMobiNative} ad which was clicked  
         */ 
        public void onAdClicked(InMobiNative ad) {} 
        /**  
         * Called to notify that the ad status has changed.  
         *  
         * @param nativeAd Represents the {@link InMobiNative} ad  
         */ 
        public void onAdStatusChanged(InMobiNative nativeAd) {} 
        /** 
         * Called to notify that inmobi has logged an impression for the ad 
         * 
         * @param ad     Represents the ad which was impressed 
         */ 
        public void onAdImpression(@NonNull InMobiNative ad) {} 
    }
    

#### Kotlin

    
    
    /**
    * A listener for receiving notifications during the lifecycle of a Native ad.
    */
    abstract class NativeAdEventListener : AdEventListener<InMobiNative>() {
    /**
        * @param ad Represents the [InMobiNative] ad whose fullscreen was dismissed 
        */ 
    open fun onAdFullScreenDismissed(ad: InMobiNative) {}
    /**
        * Called to notify that the ad will open an overlay that covers the screen. 
        * 
        * @param ad Represents the [InMobiNative] ad which will go fullscreen 
        */ 
    open fun onAdFullScreenWillDisplay(ad: InMobiNative) {}
    /**
        * Called to notify that the ad opened an overlay that covers the screen. 
        * 
        * @param ad Represents the [InMobiNative] ad whose fullscreen will be displayed 
        */ 
    open fun onAdFullScreenDisplayed(ad: InMobiNative) {}
    /**
        * Called to notify that the user is about to leave the application as a result of interacting with it. 
        * 
        * @param ad Represents the [InMobiNative] ad 
        */ 
    open fun onUserWillLeaveApplication(ad: InMobiNative) {}
    /**
        * Called to notify ad was clicked. **Note:**Override this method to notify click to the Mediation Adapter. 
        * 
        * @param ad Represents the [InMobiNative] ad which was clicked 
        */ 
    open fun onAdClicked(ad: InMobiNative) {}
    /**
        * Called to notify that the ad status has changed. 
        * 
        * @param nativeAd Represents the [InMobiNative] ad 
        */ 
    open fun onAdStatusChanged(nativeAd: InMobiNative) {}
    /**
         * Called to notify that inmobi has logged an impression for the ad 
         * @param ad     Represents the ad which was impressed 
         */ 
    open fun onAdImpression(ad: InMobiNative) {}
    }
    
    
    
    
    
    
    VideoEventListener abstract class allows you to listen to video lifecycle events for a native ad.
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    /** 
     * A listener for receiving notifications during the lifecycle of a Native ad. 
     */
    public abstract class VideoEventListener {
        /** 
         * Called to notify that the video has finished playing. 
         * 
         * @param ad Represents the {@link InMobiNative} ad 
         */
        public void onVideoCompleted(InMobiNative ad) {}
        /** 
         * Called to notify that the user has skipped video play. 
         * 
         * @param ad Represents the {@link InMobiNative} ad 
         */
        public void onVideoSkipped(InMobiNative ad) {}
        /** 
         * Called to notify when media audio state changes. 
         * 
         * @param isMuted Represents whether media is muted or not. 
         */
        public void onAudioStateChanged(InMobiNative inMobiNative, boolean isMuted) {}
    }
    

#### Kotlin

    
    
    abstract class VideoEventListener { 
       /** 
        * Called to notify that the video has finished playing. 
        * 
        * @param ad Represents the [InMobiNative] ad 
        */ 
       open fun onVideoCompleted(ad: InMobiNative) {} 
       /** 
        * Called to notify that the user has skipped video play. 
        * 
        * @param ad Represents the [InMobiNative] ad 
        */ 
       open fun onVideoSkipped(ad: InMobiNative) {} 
       /** 
        * Called to notify when media audio state changes. 
        * 
        * @param isMuted Represents whether media is muted or not. 
        */ 
       open fun onAudioStateChanged(inMobiNative: InMobiNative, isMuted: Boolean) {} 
    }
    
    
    
    
    
    
    ## Loading Native Ad
    
    
    
    
    
    To request a native ad, call the load() method on the InMobiNative instance you created above:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    nativeAd.load(); 

#### Kotlin

    
    
    nativeAd.load()
    
    
    
    
    
    
    The NativeAdEventListener abstract class notifies the result of this method. If the ad request was successful, the onAdReceived(InMobiNative) event is generated. This is followed by either the onAdLoadSucceeded or the onAdLoadFailed event. If the onAdLoadFailed event is generated, the reason is indicated by the InMobiAdRequestStatus object passed in this event.
    
    
    
    
    
    ####   
    
    **Listening to video events**
    
    
    
    
    
    To receive video events register videoEventListener using method setVideoEventListener (VideoEventListener videoEventListener) on the InMobiNative instance you created above:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    nativeAd.setVideoEventListener (videoEventListener);
    

#### Kotlin

    
    
    nativeAd.setVideoEventListener (videoEventListener)
    
    
    
    
    
    
    The VideoEventListener abstract class notifies you about video events for native ads.
    
    
    
    
    
    #### **Native Ad APIs**
    
    
    
    
    
    Following are the important APIs in InMobiNative that will help to stitch the ads:
    
    
    
    
    
    
    	
      * View getPrimaryViewOfWidth(context, convertView, parent, width) - Returns a View of specified width (specified in actual pixels). This is the main ad content in your native ad. It will return a view of the same aspect ratio that you selected on the InMobi dashboard while creating the native placement. All impression render events are fired automatically when this primary view is displayed on the screen.
    
    	
    
    If you have selected Feed Layout while creating your placement, specify width = 25 while fetching your primaryView. It will just show the AdChoices icon and fire the ad render events.
    
    
    
    	
    
    getPrimaryViewOfWidth(..) takes in four parameters:
    
    
    
    	
        		
            * context - The context in which ad is going to be rendered.
        
        		
            * convertView - This is the complete view of a row of the ListView. You should not provide this as NULL because we use this parameter to recycle our ads effectively. This will allow for a smooth scroll performance.
        
        		
            * parentView - This is the parent view inside which you will place the primaryView (which is returned by getPrimaryViewOfWidth() function). We need it for determining the layout parameters of Primary View.
        
        		
            * adViewWidthInPixels - This is the width (in pixels) that you want the primaryView to take up.
        
        	
    	
    
    	
      * String getAdTitle() - returns the string title for the ad.
    
    	
      * String getAdDescription() - returns the string description for the ad.
    
    	
      * String getAdIconUrl() - returns icon Image String URL for the ad.
    
    	
      * String getAdCtaText() - returns Click to action string for the ad.
    
    	
      * String getAdRating() - returns rating for the ad (optional).
    
    	
      * String getAdLandingPageUrl() - returns landing URL for the ad.
    
    	
      * boolean isAppDownload - returns true when the featured ad is from an app install advertiser.
    
    	
      * boolean isReady() - True means the ad is ready to be displayed.
    
    	
      * Boolean isVideo() - returns a Boolean if the ad returned contains a video or not, returns null if it is called in a wrong state.
    
    	
      * void reportAdClickAndOpenLandingPage() - This function fires the click events and opens the landing page. You need not to open the landing page on your own while using this function.
    
    	
      * JSONObject getCustomAdContent() - This function returns the JSONObject. This json have additional information (description, image URL, etc.), which can be used to create custom UI around the primary view of the ad.
    
    
    
    
    
    
    ## Stitching a Native Ad
    
    
    
    
    
    A native ad can be stitched in your app in three formats:
    
    
    
    
    
    
    	
      * In-Feed ads
    
    	
      * Splash ads
    
    	
      * Pre-Roll ads
    
    
    
    
    
    
    ## In-Feed Ad Integration
    
    
    
    
    
    
    	
      1. Declare an ad position in your feed where you want to show ad.
    	
    
    For example, to show ad at 4th position:
    
    
    
    	
    
    
    	
    
    #### Java
    
    
    
    	
    
        private static final int AD_POSITION = 4; 

#### Kotlin

    
        private val AD_POSITION = 4
    	
    
    
    	
    
    	
      2. 
    	
    
    If the ad load is successful, you will get a callback onAdLoadSucceeded(InMobiNative).You should then add the InMobiNativeAd object to your data source within this listener. If your feed in the app is a ListView, a sample implementation for ListView is shown below:
    
    
    
    	
    
    
    	
    
    #### Java
    
    
    
    	
    
        @Override
    public void onAdLoadSucceeded(@NonNull InMobiNative nativeAd) {
        AdFeedItem nativeAdFeedItem = new AdFeedItem(nativeAd);
        mFeedItems.add(AD_POSITION, nativeAdFeedItem);
        mFeedAdapter.notifyDataSetChanged();
    }
    

#### Kotlin

    
        override fun onAdLoadSucceeded(nativeAd: InMobiNative) {
       val nativeAdFeedItem = AdFeedItem(nativeAd)
       mFeedItems.add(AD_POSITION, nativeAdFeedItem)
       mFeedAdapter.notifyDataSetChanged()
    }
    	
    
    
    	  
    
    	In the step above, AdFeedItem is an extension class of your FeedItem class, where FeedItem is the class which powers each row of your ListView. Also mItems is the ArrayList, which powers the Adapter of this ListView.
    
    	
      3. 
    	
    
    So far, we have loaded an ad and added it to your data source. Now, it's time to display the ad. The sample implementation for ListView is as follows:
    
    
    
    	
    
    
    	
    
    #### Java
    
    
    
    	
    
        @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        final int itemViewType = getItemViewType(position);
        if (itemViewType == VIEW_TYPE_CONTENT_FEED) {
            //Your app code 
        } else {
            //Since this content type is InMobi Ad, you need to get native Ad view 
            final InMobiNative nativeAd = ((AdFeedItem) feedItem).mNativeAd;
            View primaryView = nativeAd.getPrimaryViewOfWidth(context, convertView, parent, parent.getWidth());
            if (convertView == null) {
                convertView = mLayoutInflater.inflate(R.layout.ad_item, parent, false);
            }
            ((RelativeLayout) convertView.findViewById(R.id.primaryView)).addView(primaryView);
            ((TextView) convertView.findViewById(R.id.title)).setText(nativeAd.getTitle());
            ((TextView) convertView.findViewById(R.id.desc)).setText(nativeAd.getDescription());
            ((TextView) convertView.findViewById(R.id.cta)).setText(nativeAd.getCtaText());
            return convertView;
        }
    }
    

#### Kotlin

    
        override fun getView(position: Int, convertView: View?, parent: ViewGroup): View? {
       var convertView: View? = convertView
       val itemViewType: Int = getItemViewType(position)
       if (itemViewType == VIEW_TYPE_CONTENT_FEED) {
           //Your app code
       } else {
           //Since this content type is InMobi Ad, you need to get native Ad view
           val nativeAd: InMobiNative = (feedItem as AdFeedItem).mNativeAd
           val primaryView: View =
               nativeAd.getPrimaryViewOfWidth(context, convertView, parent, parent.getWidth())
           if (convertView == null) {
               convertView = mLayoutInflater.inflate(R.layout.ad_item, parent, false)
           }
           (convertView.findViewById(R.id.primaryView) as RelativeLayout).addView(primaryView)
           (convertView.findViewById(R.id.title) as TextView).setText(nativeAd.getTitle())
           (convertView.findViewById(R.id.desc) as TextView).setText(nativeAd.getDescription())
           (convertView.findViewById(R.id.cta) as TextView).setText(nativeAd.getCtaText())
           return convertView
       }
    }
    	
    
    
    
    	
    
    The function getItemViewType(position) checks whether the content type is FEED OR AD as given below:
    
    
    
    	
    
    
    	
    
    #### Java
    
    
    
    	
    
        @Override
    public int getItemViewType(int position) {
        FeedItem feedItem = getItem(position);
        if (feedItem instanceof AdFeedItem) {
            return VIEW_TYPE_INMOBI_STRAND;
        }
        return VIEW_TYPE_CONTENT_FEED;
    }
    

#### Kotlin

    
        override fun getItemViewType(position: Int): Int {
       val feedItem: FeedItem = getItem(position)
       return if (feedItem is AdFeedItem) {
           VIEW_TYPE_INMOBI_STRAND
       } else VIEW_TYPE_CONTENT_FEED
    }
    	
    
    
    	  
    
    	We have used some of the APIs described in the section above to show the title, description, and CTA text of the ad. Similarly, the other APIs can be used to show the corresponding parts of the ad.
    
    
    
    
    
    
    ##   
    
    Splash Integration
    
    
    
    
    
    Splash experience can be implemented using the same InMobiNative class. However, there are a few things to be noted:
    
    
    
    
    
    
    	
      * You should use InMobiNativeAd.isReady() function to determine if the ad is ready to be shown. Sometimes, your main thread may be occupied and hence you may not receive onAdLoadSucceeded in time. Hence, it is better to proactively check if the ad is ready just after your cut-off time has elapsed.
    
    	
      * **IMPORTANT:** You should NOT destroy or refresh the ad if the second screen of the ad is on the display. You can check this in the onAdFullScreenDisplayed and not dismiss the ad if this callback is fired.
    
    
    
    
    
    
    A sample implementation is as follows:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    @Override
    public void onAdFullScreenDisplayed(InMobiNative nativeAd) {
        isSecondScreenDisplayed = YES;
    }
    public void dismissAd() {
        if (isSecondScreenDisplayed) {
            Log.d(TAG, "DO NOT DISMISS THE AD WHILE THE SCREEN IS BEING DISPLAYED");
        } else {
            splashAdView.setVisibility(View.GONE);
            nativeAd.destroy();
        }
    }
    

#### Kotlin

    
    
    override fun onAdFullScreenDisplayed(nativeAd: InMobiNative?) {
       isSecondScreenDisplayed = YES
    }
     
    fun dismissAd() {
       if (isSecondScreenDisplayed) {
           Log.d(TAG, "DO NOT DISMISS THE AD WHILE THE SCREEN IS BEING DISPLAYED")
       } else {
           splashAdView.setVisibility(View.GONE)
           nativeAd.destroy()
       }
    }
    
    
    
    
    
    
    ## Pre-Roll Integration
    
    
    
    
    
    Pre-Roll Video experience can be implemented using the same InMobiNative Class. You need to register videoEventListener and need to dismiss the ad view in the following callback:
    
    
    
    
    
    
    
    
    #### Java
    
    
    
    
    
    
    @Override 
    public void onVideoCompleted(@NonNull InMobiNative nativeAd) { 
        Log.d (TAG, "Media playback complete " + mPosition); 
    }
    

#### Kotlin

    
    
    override fun onVideoCompleted(@NonNull nativeAd: InMobiNative?) {
       Log.d(TAG, "Media playback complete $mPosition")
    }
    

The Pre-Roll ad can be dismissed as follows:

#### Java

    
    
    public void dismissAd() { 
        plashAdView.setVisibility(View.GONE); 
        nativeAd.destroy(); 
    }
    

#### Kotlin

    
    
    fun dismissAd() {
       plashAdView.setVisibility(View.GONE)
       nativeAd.destroy()
    }
    

#### Java

    
    
    public void onAdLoadSucceeded(@NonNull <inmobi_ad_object> ad, @NonNull AdMetaInfo info) { Log.d(TAG, "Creative ID for ad : " + info.getCreativeID()); }
    

#### Kotlin

    
    
    fun onAdLoadSucceeded(ad:<inmobi_ad_object> , info:AdMetaInfo ) {
       Log.d(TAG, "Creative ID for ad : " + info.getCreativeID())
    }
    

#### **Refreshing Native Ad**

You will need to refresh the ad at various points to optimize ad exposure to
your users. To refresh the ad, you will need to call the following functions
in the exact order.

#### Note

It is important to remove the `adFeedItem` object from your data source and
destroying it before refreshing. You will then need to create a new object and
call load as shown in the following code:

#### Java

    
    
    private void refreshAd() {
        Iterator < FeedItems > feedItemIterator = mFeedItems.iterator();
        while (feedItemIterator.hasNext()) {
            final FeedItem feedItem = feedItemIterator.next();
            if (feedItem instanceof AdFeedItem) {
                feedItemIterator.remove();
            }
        }
    
        // refresh feed 
        mFeedAdapter.notifyDataSetChanged();
        // destroy InMobiNative object 
        inMobiNativeAd.destroy();
        // create InMobiNative object again 
        InMobiNative inMobiNativeAd = new InMobiNative( 
            << Activity Instance >> , 
            << Your Placement ID >> , 
            << InMobiNativeAdListener created in step 1 >> );
        inMobiNativeAd.load();
    }
    

#### Kotlin

    
    
    private fun refreshAd() {
       val feedItemIterator = mFeedItems.iterator()
       while (feedItemIterator.hasNext()) {
           val feedItem = feedItemIterator.next()
           if (feedItem instanceof AdFeedItem) {
               feedItemIterator.remove()
           }
       }
     
       // refresh feed
       mFeedAdapter.notifyDataSetChanged()
       // destroy InMobiNative object
       inMobiNativeAd.destroy()
       // create InMobiNative object again
       InMobiNative inMobiNativeAd = new InMobiNative(
           << Activity Instance >> ,
           << Your Placement ID >> ,
           << InMobiNativeAdListener created in step 1 >>
       );
       inMobiNativeAd.load()
    }
    

#### **Managing the InMobiNative Instances**

  1. Every instance of `InMobiNative` represents exactly one ad.
  2. If you want to place ad at multiple positions within a content feed, create as many instances of `InMobiNative` as the number of ad positions.
  3. You should create instances of `InMobiNative` in `onCreate()` callback of Activity or in `onActivityCreated()` callback of Fragment.
  4. You should destroy the `InMobiNative` instances in `onDestroy()` callback of Activity or in `OnDestroyView()` callback of Fragment.
  5. An `InMobiNativeAd` object must always be destroyed once you remove it from the data source. All user interactions with the ad view will not be honored after `InMobiNativeAd` is destroyed. So, you will have to definitely discard the ad view before destroying the `InMobiNativeAd`.
  6. All `InMobiNativeAd` instances must also be destroyed, when the component hosting them (your activity in this case) is getting destroyed using the destroy() API.

#### **Click Tracking on the Ad Views**

To have the InMobi SDK open the landing URL in addition to reporting a click,
call the `reportAdClickAndOpenLandingPage()` method on the native ad instance:

#### Java

    
    
    nativeAd.reportAdClickAndOpenLandingPage(); 

#### Kotlin

    
    
    nativeAd.reportAdClickAndOpenLandingPage()
    

## Implementing Backfill

InMobi's SDK can run both HTML and native units against your native placement.
You can run the following ad sizes depending on the real estate reserved for
your native placement.

  * 320x50 HTML Banner
  * 300x250 HTML Banner
  * 320x480 HTML Full screen Banner
  * 320x568 HTML Full screen Banner

To switch this on, you need to reach out to your respective partner manager
with the preferred backfill size. Also, you will need to handle this in your
code as follows:

#### Java

    
    
    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        final int itemViewType = getItemViewType(position);
        if (itemViewType == VIEW_TYPE_CONTENT_FEED) {
            //Your app code 
        } else {
            //Since this content type is InMobi Ad, you need to get native Ad view 
            final InMobiNative nativeAd = ((AdFeedItem) feedItem).mNativeAd;
            //Detect whether its a backfill response or normal native 
            JSONObject customContent = currentNativeAd.getCustomAdContent();
            boolean isBackFillBanner = false;
            try {
                isBackFillBanner = customContent.getBoolean("isHTMLResponse");
            } catch (JSONException e) {
                isBackFillBanner = false;
            }
            if (isBackFillBanner) {
                View primaryView = nativeAd.getPrimaryViewOfWidth(context, convertView, parent, Math.round(getResources().getDisplayMetrics().density * 250));
                if (convertView == null) {
                    convertView = mLayoutInflater.inflate(R.layout.ad_item, parent, false);
                }
                ((RelativeLayout) convertView.findViewById(R.id.primaryView)).addView(primaryView);
                return convertView;
            } else {
                View primaryView = nativeAd.getPrimaryViewOfWidth(context, convertView, parent, parent.getWidth());
                if (convertView == null) {
                    convertView = mLayoutInflater.inflate(R.layout.ad_item, parent, false);
                }
                ((RelativeLayout) convertView.findViewById(R.id.primaryView)).addView(primaryView);
                ((TextView) convertView.findViewById(R.id.title)).setText(nativeAd.getTitle());
                ((TextView) convertView.findViewById(R.id.desc)).setText(nativeAd.getDescription());
                ((TextView) convertView.findViewById(R.id.cta)).setText(nativeAd.getCtaText());
                return convertView;
            }
        }
    }
    

#### Kotlin

    
    
    override fun getView(position: Int, convertView: View?, parent: ViewGroup): View? {
       var convertView: View? = convertView
       val itemViewType: Int = getItemViewType(position)
       if (itemViewType == VIEW_TYPE_CONTENT_FEED) {
           //Your app code
       } else {
           //Since this content type is InMobi Ad, you need to get native Ad view
           val nativeAd: InMobiNative = (feedItem as AdFeedItem).mNativeAd
           //Detect whether its a backfill response or normal native
           val customContent: JSONObject = currentNativeAd.getCustomAdContent()
           var isBackFillBanner = false
           isBackFillBanner = try {
               customContent.getBoolean("isHTMLResponse")
           } catch (e: JSONException) {
               false
           }
           return if (isBackFillBanner) {
               val primaryView: View = nativeAd.getPrimaryViewOfWidth(
                   context,
                   convertView,
                   parent,
                   Math.round(getResources().getDisplayMetrics().density * 250)
               )
               if (convertView == null) {
                   convertView = mLayoutInflater.inflate(R.layout.ad_item, parent, false)
               }
               (convertView.findViewById(R.id.primaryView) as RelativeLayout).addView(primaryView)
               convertView
           } else {
               val primaryView: View =
                   nativeAd.getPrimaryViewOfWidth(context, convertView, parent, parent.getWidth())
               if (convertView == null) {
                   convertView = mLayoutInflater.inflate(R.layout.ad_item, parent, false)
               }
               (convertView.findViewById(R.id.primaryView) as RelativeLayout).addView(primaryView)
               (convertView.findViewById(R.id.title) as TextView).setText(nativeAd.getTitle())
               (convertView.findViewById(R.id.desc) as TextView).setText(nativeAd.getDescription())
               (convertView.findViewById(R.id.cta) as TextView).setText(nativeAd.getCtaText())
               convertView
           }
       }
    }
    

#### Note

  * To detect if the response is backfill, the customAdContent will contain the string `isHTMLResponse`.
  * Do **NOT** scale the width of the HTML banner response. For e.g. if you selected backfill of 300x250, make sure the provided width is hardcoded 250.
  * Do **NOT** add the CTA button in case of backfill response. The clicks will not be monetized in case you add this button alongside the ad.

#### On This Page

Last Updated on: 01 Aug, 2022

  * [Support Center](/)
  * [InMobi Publisher Platform](/monetize)
  * [SDK Documentation](/monetize/sdk-documentation/download-sdk)
  * [Android Guidelines](/monetize/sdk-documentation/android-guidelines/overview-android-guidelines)
  * Audio Ads

# Audio Ads

Enhance your app's monetization potential with InMobi's cutting-edge Audio Ads
feature. With InMobi's SDK support for Audio Ads, you can seamlessly integrate
high-quality, targeted audio advertisements into your app's audio content.
Engage your users with relevant and captivating audio messages that fit
seamlessly within their experience.

## Set up Audio Ad

  1. From the left navigation, select **Inventory Inventory Settings**.
  2. Search for the app or website you would like to create a placement for and click **\+ Add a placement**.
  3. Click **Select Ad Unit** and select **Audio Icon**.![](https://i.l-new.inmobicdn.net/website/support/6.0.1/uploads/audio-ads2.png)
  4. Click **Add a placement** to start setting up your Audio settings. After you create the audio placement, you can see the placement ID.

## Add Audio Ad to Your App

Ensure you have updated the InMobi Android SDK to version 10.5.7 or above.
Creating an `InMobiAudio` object before SDK initialization throws an error.

### Add An Audio Slot in Code

To add an Audio ad in the Android code, create an `InMobiAudio` instance:

    
    
    val inmobiAudioAd = InMobiAudio(this, AUDIO_PLACEMENT_ID);
    

You can create an audio container anywhere on the screen with a 70p x 70px
size, preferably, and add it to the view hierarchy:

    
    
    val adContainer = findViewById<RelativeLayout>(<ad-container-id>) 
    adContainer.removeAllViews() 
    adContainer.addView(inmobiAudioAd) 
    inmobiAudioAd.setAudioSize(70, 70)
    

## Load Audio Ad

To request an interstitial ad, call the `load()` method on the `InMobiAudio`
instance:

    
    
    inmobiAudioAd.load()
    

If the `onAdLoadSucceeded` event is generated, you can show the ad after this
by calling `show()` on the `InMobiAudio` instance.

#### Note

  * If new instances are created for every audio ad, ensure `load()` is called with every `InMobiAudio` instance.
  * Ensure the InMobi SDK is initialized successfully before calling `load()`.

## Show Audio Ad

To show an audio ad, call `show()` on the InMobiAudio instance after the
`onAdLoadSucceeded` the SDK has generated an event.

    
    
    inmobiAudioAd.setListener(object: AudioAdEventListener(){ 
        override fun onAdLoadSucceeded(p0: InMobiAudio?, p1: AdMetaInfo) { 
            super.onAdLoadSucceeded(p0, p1) 
            inmobiAudioAd.show(); 
        } 
    }
    

## Optimization

### Listen for Audio Ad Lifecycle Events

If you want to listen to key events in the audio ad lifecycle, you can
implement the AudioAdEventListener interface. A sample implementation is shown
below.

    
    
    val audioAdEventListener = object : AudioAdEventListener() {    
        /**  
         * Called to notify that an ad was received successfully but is not ready to be ayed yet.  
         *  
         * @param ad   Represents the ad which was loaded or preloaded  
         * @param info Represents the ad meta information  
         */  
        override fun onAdFetchSuccessful(ad: InMobiAudio, info: AdMetaInfo) {    
        }    
        /**  
         * Called to notify that an ad preload has failed.  
         *  
         * @param ad     Represents the [InMobiAudio] ad which was preloaded  
         * @param status Represents the [InMobiAdRequestStatus] status containing error reason  
         */  
        override fun onAdFetchFailed(ad: InMobiAudio, status: InMobiAdRequestStatus) {    
        }    
        /**  
         * Called to notify that an ad was successfully loaded and is ready to be displayed.  
         *  
         * @param ad   Represents the ad which was loaded  
         * @param info Represents the ad meta information  
         */  
        override fun onAdLoadSucceeded(ad: InMobiAudio, info: AdMetaInfo) {    
        }    
        /**  
         * Called to notify that a request to load an ad failed.  
         *  
         * @param ad     Represents the ad which failed to load  
         * @param status Represents the [InMobiAdRequestStatus] status containing error reason  
         */  
        override fun onAdLoadFailed(ad: InMobiAudio, status: InMobiAdRequestStatus) {    
        }    
        /**  
         * Called to notify that the banner ad has expanded  
         *  
         * @param ad Represents the [InMobiAudio] ad which was expanded  
         */  
        override fun onAdDisplayed(ad: InMobiAudio) {  
        }    
        /**  
         * Called to indicate that a request to show an ad (by calling [InMobiAudio.show]  
         * failed. You should call [InMobiAudio.load] to request for a fresh ad.  
         *  
         * @param ad Represents the [InMobiAudio] ad which failed to show  
         */  
        override fun onAdDisplayFailed(ad: InMobiAudio) {  
        }
        /**  
         * Called to notify that inmobi has logged an impression for the ad  
         *  
         * @param ad     Represents the ad which was impressed  
         */  
        override fun onAdImpression(ad: InMobiAudio) {  
        }    
        /**  
         * Called to notify that the Audio status has changed  
         *  
         * @param ad Represents the [InMobiAudio] ad  
         * @param audioStatus Represents the [AudioStatus] of the current playing ad  
         */  
        override fun onAudioStatusChanged(ad: InMobiAudio, audioStatus: AudioStatus) {    
        }    
        /**  
         * Called to notify that the user interacted with the ad.  
         *  
         * @param ad     Represents the ad on which user clicked  
         * @param params Represents the click parameters  
         */  
        override fun onAdClicked(ad: InMobiAudio, params: Map<Any, Any>) {    
        }    
        /**  
         * Called to notify that a reward was unlocked.  
         *  
         * @param ad      Represents the [InMobiAudio] ad for which rewards was unlocked  
         * @param rewards Represents the rewards unlocked  
         */  
        override fun onUserLeftApplication(ad: InMobiAudio) {    
        }    
        /**  
         * Called to notify that the User is about to return to the application after closing d.  
         *  
         * @param ad Represents the [InMobiAudio] ad which was closed  
         */  
        override fun onAdDismissed(ad: InMobiAudio) {    
        }  
    }  
     
    audioAd.setListener(audioAdEventListener)
    

#### Note

The bid value can be accessed from the `AdMetaInfo` object's bid field.

### Destroy Audio Object

You can release the resources after showing an audio ad by calling destroy.
You may call the function on receiving `AudioStatus`.Completed in
`onAudioStatusChanged` function callback in the listener.

  1. Remove the ad view from the view hierarchy
  2. De-reference the listeners
  3. Other clean-ups.

    
    
    inmobiAudioAd.destroy()
    

## Integrate Rewarded Audio Icons

### Set up Audio Ad

  1. From the left navigation select **Inventory Inventory Settings**.
  2. Search for the app or website you would like to create a placement for and click **\+ Add a placement**.
  3. Click **Select Ad Unit** and select **Rewarded Audio**.
  4. Click **Add a placement** to start setting up your rewarded video settings. After you create the rewarded video placement, you can see the placement ID.![](/ui/uploads/rewarded_placement.png)

### Add Rewarded Audio Ad to Your App

The implementation for Rewarded Audio Icon ads closely resembles that of Audio
Icons.

You are expected to present a prompt to users, seeking their opt-in prior to
displaying the rewarded audio icon ad. The InMobi SDK also offers the
`onRewardsUnlocked` event for Rewarded ads. However, you can retain the
flexibility to determine the timing of user rewards using various event
callbacks.

    
    
    inmobiAudioAd.setListener(object: AudioAdEventListener(){ 
        override fun onRewardsUnlocked(ad: InMobiAudio, rewards: Map<Any, Any>) { 
            super.onRewardsUnlocked(ad, rewards) 
            // pass rewards to the user 
        } 
    }
    

## Test Integration

Using sandbox ads, you can assess the placement and refine the user
experience. This involves configuring the placement in **Test Mode** , setting
it as '**Global** ' within the placement settings. It's important to ensure
that you set the device volume to a sufficient level to ensure ad playback.

For those employing manual SDK integration, it's imperative to initialize the
InMobi SDK within the mediation debugger to ensure seamless operation and
accurate evaluation.

#### On This Page

Last Updated on: 22 Aug, 2023

  * [Support Center](/)
  * [InMobi Publisher Platform](/monetize)
  * [SDK Documentation](/monetize/sdk-documentation/download-sdk)
  * [Android Guidelines](/monetize/sdk-documentation/android-guidelines/overview-android-guidelines)
  * Testing and Troubleshooting

# Testing and Troubleshooting

## Retrieve the CreativeID

It may happen that some advertisers escape ad quality checks and end up
compromising the user experience on the app by showcasing either an
irrelevant, distasteful, or disrupting creative to the user. To combat such
situations, you can retrieve the creativeID of the ad instance and report back
to your InMobi point of contact with the encrypted creativeID. CreativeID is a
property of IMBanner, IMInterstitial and IMNative object, which can be
retrieved as follow:

#### Java

    
    
    public void onAdLoadSucceeded(@NonNull <inmobi_ad_object> ad, @NonNull AdMetaInfo info) { Log.d(TAG, "Creative ID for ad : " + info.getCreativeID()); }
    

#### Kotlin

    
    
    fun onAdLoadSucceeded(ad:<inmobi_ad_object> , info:AdMetaInfo ) {
       Log.d(TAG, "Creative ID for ad : " + info.getCreativeID())
    }
    

## Test Your Integration

You can start testing your integration by navigating to the [Integration
Tab](/monetize/publisher-dashboard/integration-tab) on the InMobi Publisher
Dashboard.

If you have Java and Python installed in your local system, [click
here](https://www.dropbox.com/sh/ypa20foniunqn80/AAB2Jlt0vl_6pUzvWyWvZx-
ya?dl=0) and run the Library Detection Tool to ensure that all the mandatory
libraries are needed for InMobi SDK integration [InMobi SDK, Picasso, browser,
and RecyclerView] are available.

![](https://inmobiwebsitecdn.azureedge.net/support-
assets/web/ui/uploads/library_detection__tool.png)

To set up a test device, you will need the corresponding device ID. The device
id is the Google Play Advertising ID (GPID). To get the device ID, configure
the SDK to print debug logs to the console.

#### **Remember**

You**MUST** turn off the test mode before going live or else your app will
fail to monetize.

## Get the Device ID

The device id is the Google Play Advertising ID (GPID). To get the device ID,
configure the SDK to print debug logs to the console.

You can do so by adding the following line to your Activity where you are
integrating InMobi ads.

#### Java

    
    
    InMobiSdk.setLogLevel(LogLevel.DEBUG);
    
    

#### Kotlin

    
    
    InMobiSdk.setLogLevel(LogLevel.DEBUG)
    



  