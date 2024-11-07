SDK name: YouAppi
Documentation:
_Menu_[![](https://support.youappi.com/wp-
content/uploads/2017/11/YouAPPi_Logo-
Black-479x105.png)![](https://support.youappi.com/wp-
content/uploads/2017/11/YA-Logo-
White-300x60-1.png)](https://support.youappi.com/)

  * [SDK](https://support.youappi.com/kb/partners/sdk/)
  * [Partners](https://support.youappi.com/kb/partners/)
    * [Direct Campaign API](https://support.youappi.com/kb/partners/direct-campaign-api/)
    * [Ad Recommendation API](https://support.youappi.com/kb/partners/ad-recommendation-api/)
    * [SDK](https://support.youappi.com/kb/partners/sdk/)
    * [Postback](https://support.youappi.com/kb/partners/postback/)
  * [Advertisers](https://support.youappi.com/kb/advertisers/)
    * [Re-engagement / Prog-UA](https://support.youappi.com/kb/advertisers/re-engagement/)
    * [User Acquisition](https://support.youappi.com/kb/advertisers/user-acquisition/)
  * [Contact](https://support.youappi.com/?page_id=1324)

  * [SDK](https://support.youappi.com/kb/partners/sdk/)
  * [Partners](https://support.youappi.com/kb/partners/)
    * [Direct Campaign API](https://support.youappi.com/kb/partners/direct-campaign-api/)
    * [Ad Recommendation API](https://support.youappi.com/kb/partners/ad-recommendation-api/)
    * [SDK](https://support.youappi.com/kb/partners/sdk/)
    * [Postback](https://support.youappi.com/kb/partners/postback/)
  * [Advertisers](https://support.youappi.com/kb/advertisers/)
    * [Re-engagement / Prog-UA](https://support.youappi.com/kb/advertisers/re-engagement/)
    * [User Acquisition](https://support.youappi.com/kb/advertisers/user-acquisition/)
  * [Contact](https://support.youappi.com/?page_id=1324)

# Android

[home](https://support.youappi.com)/[Knowledge
Base](https://support.youappi.com)/[Partners](https://support.youappi.com/kb/partners/)/[SDK](https://support.youappi.com/kb/partners/sdk/)/[Android](https://support.youappi.com/kb/partners/sdk/android/)

__

##  Android SDK

__ 7113 views  __ 2019-11-04 __ Ofer Garnett __ 0

Table of Contents

Toggle

  * Getting Started
  * Integration
    * Integrate using AAR file
    * Integrate using repository
  * Using the SDK
    * Custom parameters and server-to-server callback (optional)
      * Dynamic User Id
    * Age and Gender support (optional)
    * Implementation example for Rewarded Video
    * Android App Bundle
    * Device Orientation
  * GDPR User's Consent
  * Logging and troubleshooting
  * Load and Show best practices
  * Demo App

# Getting Started

Latest Android version: 5.0.1  
---  
Release date: 16-Mar 2020  
  
This document details the process of integrating YouAppi's SDK with your
Android app.

If you have any questions, please, feel free to email us:
[support@youappi.com](mailto:support@youappi.com)

The basic steps of integration are:

  * Add our SDK AAR and dependencies to your project.
  * Init the SDK.
  * Load an ad.
  * Show an ad.

_**Requirements:**_

Minimum API level: 16, Android 4.1

**Please, note that SDK can access some of user 's private information, so,
make sure you have read [this
part](https://support.youappi.com/knowledgebase/android-
sdk/#Users_Private_Information) carefully. **

# Integration

## Integrate using AAR file

Our latest SDK version can be downloaded as a ZIP file from the following URL:

[YouAppi Android SDK](http://sdkui.youappi.com/download/latest/sdk/android)

The ZIP file contains:

  * SDK AAR file - **youappi-sdk-android-moat.aar** - YouAppi's SDK
  * SDK AAR file - **youappi-sdk-android-admob.aar** - YouAppi's AdMob adapter
  * SDK AAR file - **youappi-sdk-android-mopub.aar** - YouAppi'd MoPub adapter

  * Copy **youappi-sdk-android-moat.aar** file to the **apps\libs** folder of your project.
  * Add the following to the **project** build.gradle file inside the **repositories** section: 
    
        repositories {
        flatDir {
            dirs 'libs'
        }
    }

  * Add to your **app** build.gradle file the following under **dependencies** section: 
    
        dependencies {
        implementation name:'youappi-sdk-android-moat', ext:'aar'
        implementation 'com.google.code.gson:gson:2.6'
        implementation 'com.google.android.gms:play-services-ads-identifier:16.0.0'
    }

Please make sure to add the play-services-ads-identifier dependency so we will
be able to access the Android Advertising ID (AAID).

Note: If Manifest Merger is disabled, the following items need to be added to
the **AndroidManifest.xml** file:

  * Add **AdActivity** activity to **< application>** tag : 
    
        <activity android:name="com.youappi.sdk.AdActivity"
       android:configChanges="screenSize|orientation"/>

  * These permissions should be added if your app is running on older devices: 
    
        <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>

## Integrate using repository

  * Add the following to the **project** build.gradle file inside the **repositories** section: 
    
        maven { url "http://repository.youappi.com/repository/release" }
    

  * Add to your **app** build.gradle file the following under **dependencies** section: 
    
        dependencies {
         implementation "com.youappi.sdk:youappi-sdk-android-moat:4.4.6"
         implementation "com.google.android.gms:play-services-ads-identifier:16.0.0"
    }
    

Please make sure to add the play-services-ads-identifier dependency so we will
be able to access the Android Advertising ID (AAID).

# Using the SDK

  * Initialize YouAppi SDK as soon as your app loads with the app token, provided by YouAppi, user consent and GDPR. USER_CONSENT is the user’s response to a dialog presented to the user asking for permission. If your user is NOT subject to the GDPR rules (e.g.: a EU residence), please, make sure DOES_GDPR_APPLY value is 'false' in order to get relevant ads: 
    
        YouAPPi.init(context, "<YOUR_APP_TOKEN>", USER_CONSENT, DOES_GDPR_APPLY);

  * **Please note:** it is strongly recommended to initialize YouAppi SDK in the **onCreate** method of the **Application** object of your app. It will ensure YouAppi SDK instance is always properly initialized. Here is an example: 
    
        import android.app.Application;
    import com.youappi.sdk.YouAPPi;
                
    public class YouAppApplication extends Application {
                    
          private static final String DEMO_TOKEN = "<YOUR_APP_TOKEN>;
          private static final boolean USER_CONSENT = true;
          private static final boolean DOES_GDPR_APPLY = false;
     
          @Override
          public void onCreate() {
                super.onCreate();
                YouAPPi.init(this, DEMO_TOKEN, USER_CONSENT, DOES_GDPR_APPLY);
          }
    }
    

  * Also, update the corresponding **manifest.xml** with the **Application class name** : 
    
        <?xml version="1.0" encoding="utf-8"?>
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        package="com.youappi.sdk.demo">
    
        <application
            android:name = ".YouAppApplication"
            android:allowBackup="true"
            android:icon="@mipmap/ic_launcher"
            android:label="@string/app_name"
            ...
            ...
        </application>
    </manifest>

  * Create an ad instance for one of YouAppi's products: 
    * Rewarded Video
    * Interstitial Ad (Note: Interstitial Ad can be a static or a video depending on the creative type)
    
        YARewardedVideoAd rewardedVideoAd = YouAPPi.getInstance().rewardedVideoAd("test_rewarded_video_ad");
    YAInterstitialAd interstitialAd = YouAPPi.getInstance().interstitialAd("test_interstitial_ad");

  * **Please note:** YouAppi ad unit id is created and controlled by the app developer. The ad unit id later appears in reports and helps to analyze performance for each ad unit. Any arbitrary value can be selected for ad unit id as long as it is constructed from: 
    * letters (lowercase, uppercase)
    * numbers
    * underscores.

  * Load an ad (for example, a rewarded video ad):
    
        rewardedVideoAd.load();

  * Show an ad:
    
        rewardedVideoAd.show();

  * **Please note:** Interstitial Ad can be static or video based on the creative type set in an ad request. For static: 
    *         YAAdRequest adRequest = new YAAdRequest()
        	.setCreativeType(YAAdRequest.CreativeType.Static)

## Custom parameters and server-to-server callback (optional)

YouAppi SDK supports customer parameters and server-to-server callback. Custom
parameters could be passed during the ad request and received upon user’s
completion event as a part of the callback string (server-to-server completion
callback).

Parameter Name| Description| Value Type| Provided by  
---|---|---|---  
user_id| A unique identifier of the user to be rewarded.| String| Publisher  
reward_type| A name of the virtual item to be rewarded.| String| Publisher  
reward_value| A number of credit units to be rewarded to the user.| String|
Publisher  
reward_id| A unique identifier of the commission event.| String| YouAppi  
dynamicUserId| A unique parameter to verify transaction that could be changed
throughout the session.| String| Publisher  
  
Callback URL example:  
http://www.app.com?appUserId={user_id}&RewardValue={reward_value}&RewardType={reward_type}&RewardId={reward_id}&DynamicUserId={dynamicUserId}

You can use YAAdRequest object to add custom parameters as <key, value> to
your ad request before loading an ad:

    
    
    YaAdRequest adRequest = new YAAdRequest();
    adRequest.addCustomParam("param_key", "param_value");
    rewardedVideoAd.setAdRequest(adRequest);

### Dynamic User Id

This optional parameter could be changed throughout the session and used to
verify Rewarded Video transactions. To receive this parameter through the
server-to-server completion callback, setDynamicUserId() method should be
called before calling show(). This parameter will be received with the other
custom parameters upon user's completion event as a part of the server-to-
server callback string.

    
    
    YouAPPi.getInstance().setDynamicUserId("best_user_ever");

## Age and Gender support (optional)

In order to get better supply that allocated specifically to the user, user's
age and gender could be forwarded to our server throughout YouAppi SDK. You
can use YAAdRequest object and setGender() / setAge() methods accordingly
before loading ads.

    
    
    YAAdRequest adRequest = new YAAdRequest()
            .setGender(YAAdRequest.Gender.Female)
            .setAge("40");

## Implementation example for **Rewarded Video**

Please note: this example is for rewarded video. Other products work in a
similar way.

  * Create a rewarded video instance: 
    
        YARewardedVideoAd rewardedVideoAd = YouAPPi.getInstance().rewardedVideoAd("test_rewarded_video_ad");

  * Add rewarded video event listener:
    
        rewardedVideoAd.setRewardedVideoAdListener(new YARewardedVideoAd.RewardedVideoAdListener() {
                @Override
                public void onRewarded(String s) {
                    
                }
     
                @Override
                public void onVideoStart(String s) {
     
                }
     
                @Override
                public void onVideoEnd(String s) {
     
                }
     
                @Override
                public void onVideoSkipped(String s, int i) {
     
                }
     
                @Override
                public void onCardShow(String s) {
     
                }
     
                @Override
                public void onCardClose(String s) {
     
                }
     
                @Override
                public void onCardClick(String s) {
     
                }
     
                @Override
                public void onLoadSuccess(String s) {
     
                }
     
                @Override
                public void onLoadFailure(String s, YAErrorCode yaErrorCode, Exception e) {
     
                }
     
                @Override
                public void onShowFailure(String s, YAErrorCode yaErrorCode, Exception e) {
     
                }
     
                @Override
                public void onAdStarted(String s) {
     
                }
     
                @Override
                public void onAdEnded(String s) {
     
                }
            });

  * Add custom parameters / age / gender (if needed) and load rewarded video ad: 
    
        YAAdRequest adRequest = new YAAdRequest()
             .addCustomParam("user_id", "user100")
             .addCustomParam("reward_value", "25")
             .addCustomParam("reward_type", "coins")
             .setGender(YAAdRequest.Gender.Female)
             .setAge("40");
    rewardedVideo.setAdRequest(adRequest);
    rewardedVideoAd.load();

  * Once ad is loaded, the event **onLoadSuccess** is called, set dynamic usr id (if needed) and show ads:
    
        YouAPPi.getInstance().setDynamicUserId("best_user_ever");
    rewardedVideoAd.show();

  * Ad availability can also be checked by calling:
    
        rewardedVideoAd.isAvailable();

If you're using **proguard** in your application the following entries should
be added to your proguard file:

    
        -keep class com.google.gson.**{ *;}
    -keep class com.google.android.gms.**{*;}
    -keep class com.youappi.sdk.**{*;}
    -keep interface com.youappi.sdk.**{*;}
    -keep enum com.youappi.sdk.**{*;}
    -keepclassmembers class * {
       @android.webkit.JavascriptInterface <methods>;
    }

## Android App Bundle

In order to upload your app's compiled code and resources to Google Play using
[Android App Bundle](https://developer.android.com/guide/app-bundle/) without
generating APK, exclude Android Manifest from the package options of your
build.gradle:

    
    
    packagingOptions {
        exclude 'AndroidManifest.xml'
    }

## Device Orientation

If the app developer fixes the app orientation to a specific orientation
(portrait or landscape), then the specific orientation needs to be added to
the **AndroidManifest.xml** file:

    
    
    <activity android:name="com.youappi.sdk.AdActivity"
        android:screenOrientation="landscape"/>
    

# GDPR User's Consent

The USER_CONSENT value should be determined by the app developer according to
the User’s response to a Consent Request. The DOES_GDPR_APPLY value should be
set according to the user being subject to the GDPR rules (e.g.: an EU
residence). The DOES_GDPR_APPLY flag value signals to YouAppi the permission
to process and store the user’s Personal Information (e.g.: Advertising ID and
IP address). In case that the flag value is false, YouAppi may decide not to
respond to the ad request, since the user cannot be detected and his actions
cannot be attributed to the user and hence also to YouAppi and to the app
developer.

GDPR user consent can be passed in the following ways:

  * It is mandatory to pass user consent in SDK init:

    
    
    YouAPPi.init(context, "<YOUR_APP_TOKEN>", USER_CONSENT, DOES_GDPR_APPLY);

  * USER_CONSENT can be set by using:

    
    
    YouAPPi.getInstance().setUserConsent(true);
    

  * DOES_GDPR_APPLY can be set by using:

    
    
    YouAPPi.getInstance().setgdpr(false);

  * If the user is known to be in an age restricted class (e.g.: under the age of 16 in some countries or under the age of 13 in other countries ) then the age restricted indication should be passed:

    
    
    YouAPPi.getInstance().setAgeRestrictedUser(true);

# Logging and troubleshooting

After initializing the SDK you can set LogListener to get detailed log events
from YouAppi's SDK:

    
    
    YouAPPi.getInstance().setLogListener(new Logger.LogListener()
       {
           @Override
           public void log(String tag, String message)
           {
               // This will be called each time YouAppi SDK generates a log message.
           }
       });

# Load and Show best practices

  * Make sure to init the SDK as soon as the app starts. It might take few seconds to complete the init process.
  * Make sure to load the ad about 30 seconds before you want to show it since it takes time for the ad and assets to be prepared.
  * Make sure to show an ad as close as possible to its load, in order to have a better fill rate and relevant ads.
  * Make sure not to wait too long before showing an ad, since the ad will be expired 5 hours after being called for. In other words, “show” must be performed no more than 5 hours after the “load”.
  * Use ad event listeners in order to be notified when an ad is ready to be shown.
  * Use ad event listeners to handle load and show.
  * Loading an ad too many times without showing it might cause YouAppi servers to block the SDK from requests.

# Demo App

A demo app showing a simple usage of the SDK can be found in the following
Github repository:

<https://github.com/YouAppi/youappi-sdk-android-demo>

The demo app contains 4 modules:

  * **app-demo** - Shows how to use YouAppi's SDK
  * **app-demo-admob** - Shows how to use YouAppi's SDK with AdMob adapter
  * **app-demo-mopub** - Shows how to use YouAppi's SDK with MoPub adapter
  * **app-demo-nativeads** – Shows how to use YouAppi’s SDK Native Ads

Please make sure to read the README.md file for further instructions.

__Tags:[android](https://support.youappi.com/kb-
tag/android/)[sdk](https://support.youappi.com/kb-tag/sdk/)

[__](https://twitter.com/home?status=https://support.youappi.com/knowledgebase/android-
sdk/)[__](https://www.facebook.com/sharer/sharer.php?u=https://support.youappi.com/knowledgebase/android-
sdk/
"facebook")[__](https://pinterest.com/pin/create/button/?url=https://support.youappi.com/knowledgebase/android-
sdk/&media=&description=)[__](https://plus.google.com/share?url=https://support.youappi.com/knowledgebase/android-
sdk/)[__](http://www.linkedin.com/shareArticle?mini=true&url=https://support.youappi.com/knowledgebase/android-
sdk/)

##### Related Articles

  * [Android SDK Native Ads Video](https://support.youappi.com/knowledgebase/android-sdk-native-video/)
  * [Android SDK Native Ads Static](https://support.youappi.com/knowledgebase/android-sdk-native-ads/)

  

  * [__](https://twitter.com/YouAppi "Twitter")
  * [__](https://www.facebook.com/youAPPi/ "Facebook")
  * [__](https://plus.google.com/u/0/+Youappi/posts "Google+")
  * [__](https://www.linkedin.com/company/2461032 "Linkedin")
  * [__](https://www.pinterest.com/youappi2015/ "Pinterest")

  * [Privacy Policy](https://youappi.com/privacy-policy/)
  * [Terms of Use](https://youappi.com/terms-of-use/)
  * [EULA](https://support.youappi.com/eula/)

  * © 2017 [YouAppi](http://youappi.com). All Rights Reserved.

