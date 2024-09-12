[![logo](assets/img/logo-white.svg)](http://admost.github.io)

  * [Documentation](index.html)
  * [Privacy Compliance](https://admost.github.io/privacy.html)
  * [Release Notes](release-notes.html)
  * [FAQ](faq.html)
  * [ __   Demo Project](https://github.com/admost/amrandroid/tree/master/)

# __   Android Integration Guide

##### This is the easiest way to integrate Admost Android SDK and ad networks
to your current Android Mobile App.

  * Overview
  * Prerequisites
    * Android Version
    * IDE
    * App ID & Zone ID
    * Permissions
  * Setup
    * Ad-Networks
    * Required Files
    * Edit Files
    * Proguard
    * Shrink Resources
  * Usage
    * Initialization
      * GDPR
      * CCPA
    * Banner Ads
      * Custom Native Design
    * Interstitial Ads
    * App Open Ads
    * Rewarded Ads
    * Offerwall Ads
      * Spending Virtual Currencies
  * Extras
    * Google AdManager Integration
    * Test Suite
    * Huawei AppGallery Applications
    * In App Purchase Tracking
    * Amazon Store In App Purchase Tracking
    * Huawei AppGallery In App Purchase Tracking
    * Setting Application User Id
    * Adjust Integration
    * Server to Server Callbacks
    * Privacy Consent Check
    * Campaign Tracking
    * Remote Config
    * A/B Test
    * CMP Integration NEW
    * Third Party A/B test NEW

## Overview

The following document detaily shows that how to integrate Admost Android SDK
and desired networks via gradle build setup. There are too many ad networks
you may desire to add your current app. Integrating those ad networks to your
application can achievable via gradle. Most of the ad Integrating those ad
networks to your application can achievable via gradle. Most of the ad
networks are can be integrated by 1 line of code addition to your project's
`/app/src/build.gradle` file and `/build.gradle` file. However some of them
are requires more aditions to `/app/src/main/AndroidManifest.xml` and
`/app/src/proguard-rules.pro` file.

## Prerequisites

### Android Version

  * Android 4.0 (Ice Cream Sandwich - API Version 14) or later.
  * Enable AndroidX in your project. [For more information.](https://developer.android.com/jetpack/androidx/migrate)

### IDE

You have to use Latest Android Studio build. You can download the latest
Android Studio from [here. ](https://developer.android.com/studio/index.html)

`/app/src/main/AndroidManifest.xml`, `/app/src/build.gradle`,
`/app/src/proguard-rules.pro` and `/build.gradle` files may be required in the
next parts. You can see where to find those files in project view structure.

Android Studio _~ Project view_

  * .gradle 
  * .idea 
  * app 
    * build 
    * src 
      * main 
        * java
        * res
        * `AndroidManifest.xml`
      * `build.gradle` _app's gradle file_
      * `proguard-rules.pro`
    * build 
    * .gradle 
    * `build.gradle` _project's gradle file_

Folder/File | Purpose  
---|---  
`/app/src/main/AndroidManifest.xml` | This is your app's AndroidManifest.xml. We will just update inside of **application** tags.   
`/app/src/build.gradle` | This is your app's build.gradle file. We will just update inside of **dependencies** bracelets.   
`/app/src/proguard-rules.pro` | The proguard-rules.pro file is where you can add custom ProGuard rules.   
`/build.gradle` | This is project's build.gradle file. We will just update inside of **repositories** bracelets.   
  
### App ID & Zone ID

Application Id provided in Admost Mediation Dashboard. Zone Id(s) provided in
[Admost Mediation Dashboard](http://dashboard.admost.com/).

### Permissions

Some of the Ad networks requires additional permissions. You have to consider
this while adding those ad networks in to your application. We handled those
permissions in our SDK, you do not have to do anything but we are saying this
to keep in mind.

Those permissions are listed below;

    
    
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
                    

## Setup

### Ad-Networks

Please click `+` icon to add to list and `-` to remove from list. After finish
selecting ad networks, continue with next step

### Required Files

With your selections you are going to work with following files;

  * `/build.gradle`
  * `/app/src/build.gradle`
  * `gradle.properties`

If you are using proguard you have to edit `/app/src/proguard-rules.pro` too.

### Edit Files

Add the following lines inside  android{} bracelets in
`/app/src/build.gradle`file

    
    
     
                        compileOptions {
            sourceCompatibility JavaVersion.VERSION_1_8
            targetCompatibility JavaVersion.VERSION_1_8
        }

It is highly recommended to enable AndroidX in your project. Editing
`gradle.properties` file and adding the lines below(if they are not present)
is required for most ad-network sdks.**

__

Copy

    
    
    
    android.useAndroidX=true
    android.enableJetifier=true
    
    

If you are using Admob SDK (com.google.android.gms:play-services-ads) with
version **17.0.0 and higher** , you must add your **AdMob App ID** to your
Android Manifest file.

__

Copy

    
    
    <manifest>
        <application>
            <!-- Sample AdMob App ID: ca-app-pub-0000000000000000~0000000000 -->
            <meta-data
            android:name="com.google.android.gms.ads.APPLICATION_ID"
            android:value="[ADMOB_APP_ID]"/>
        </application>
    </manifest>
    				

#### Appsamurai Ad-Network Usage Warning

**Skip this subsection if you don't use Appsamurai ad-network.**

You need to enable Kotlin for your project , if you want to use Appsamurai.

Please visit: [**https://developer.android.com/kotlin/add-
kotlin**](https://developer.android.com/kotlin/add-kotlin)

#### Nend Ad-Network Usage Warning

**Skip this subsection if you don't use Nend ad-network.**

If you use Nend network and enable shrinkResources in your app, in addition to
minifyEnabled (in build gradle file: android > buildTypes > **shrinkResources
true**), you should have a file named **keep.xml** under res > raw folder with
the following content:  

    
    
    
    <?xml version="1.0" encoding="utf-8"?>
        <resources xmlns:tools="http://schemas.android.com/tools"
        tools:keep="@drawable/*_thumb,@drawable/*nend*"
        tools:shrinkMode="strict" />
    
    

#### AdGem Ad-Network Usage Warning

**Skip this subsection if you don't use AdGem ad-network.**

    
    
    
    // Step 1: You must use Java 8 if you want to use AdGem ad-network. 
    // Add the lines inside of app's build.gradle file > 'android' tag.
    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    
    // Step 2: Create a new XML resource file called adgem_config.xml within the res/xml directory.
    // If the xml directory does not exist, please create it.
    <adgem-configuration applicationId="ADGEM_APP_ID" 
    standardVideoAdsEnabled="false" 
    rewardedVideoAdsEnabled="false" 
    offerWallEnabled="true" /> 
    
    // Step 3: Add following lines to AndroidManifest.xml file.
    <meta-data android:name="com.adgem.Config" 
    android:resource="@xml/adgem_config"/> 
    
            

#### Kidoz Ad-Network Usage Warning

**Skip this subsection if you don't use Kidoz ad-network.**

Add following lines to AndroidManifest.xml file under application tag.

    
    
     <receiver android:name="com.kidoz.sdk.api.receivers.SdkReceiver" android:enabled="true" >
                <intent-filter>
                    <action android:name="android.intent.action.PACKAGE_ADDED"/>
                    <data android:scheme="package"/>
                </intent-filter>
            </receiver>

### Proguard

Copy & paste following code snippet in to your `/app/src/proguard-rules.pro`
file

    
    
    
    # ADMOST
    -keepattributes Exceptions, InnerClasses
    -dontwarn admost.sdk.**
    -keep class admost.sdk.** {*;}
    -dontwarn com.amr.unity.**
    -keep class com.amr.unity.** {*;}
    -dontwarn admost.adserver.**
    -keep class com.adjust.sdk.** {*;}
    -dontwarn com.adjust.sdk.**
    -keep class com.appsflyer.** {*;}
    -dontwarn com.appsflyer.**
    -keep class admost.adserver.** { *; }
    -dontwarn com.google.android.exoplayer2.**
    -keep class com.google.android.exoplayer2.**{ *;}
    -keep class android.support.v4.app.DialogFragment { *; }
    -keep class android.support.v4.util.LruCache { *; }
                            
    
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    
    # ADCOLONY
    -dontwarn com.adcolony.**
    -keep class com.adcolony.** { *; }
    -keepclassmembers class * { @android.webkit.JavascriptInterface <methods>; }
    -keepclassmembers class com.adcolony.sdk.ADCNative** { *; }
    
    # ADGEM
    -keep class com.adgem.** { *; }
    -dontwarn com.adgem.**
    
    # ADMOB / ADX / GOOGLE
    -keep class com.android.vending.billing.**
    -keep public class com.google.android.gms.ads.** { public *; }
    -keep public class com.google.ads.** { public *; }
    -keep class com.google.android.gms.** { *; }
    -dontwarn com.google.android.gms.**
    -keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable { public static final *** NULL; }
    -keepnames class * implements android.os.Parcelable
    -keepclassmembers class * implements android.os.Parcelable { public static final *** CREATOR; }
    -keep @interface android.support.annotation.Keep
    -keep @android.support.annotation.Keep class *
    -keepclasseswithmembers class * { @android.support.annotation.Keep <fields>; }
    -keepclasseswithmembers class * { @android.support.annotation.Keep <methods>; }
    -keep @interface com.google.android.gms.common.annotation.KeepName
    -keepnames @com.google.android.gms.common.annotation.KeepName class *
    -keepclassmembernames class * { @com.google.android.gms.common.annotation.KeepName *; }
    -keep @interface com.google.android.gms.common.util.DynamiteApi
    -keep public @com.google.android.gms.common.util.DynamiteApi class * { public <fields>; public <methods>; }
    -keep public @com.google.android.gms.common.util.DynamiteApi class * { *; }
    -keep class com.google.android.apps.common.proguard.UsedBy*
    -keep @com.google.android.apps.common.proguard.UsedBy* class *
    -keepclassmembers class * { @com.google.android.apps.common.proguard.UsedBy* *; }
    -dontwarn android.security.NetworkSecurityPolicy
    -dontwarn android.app.Notification
    
    #ADTIMING
    -dontwarn com.aiming.mdt.**.*
    -dontoptimize
    -dontskipnonpubliclibraryclasses
    -keepattributes *Annotation*
    #adt
    -keep class com.aiming.mdt.**{ *; }
    -keepattributes *Annotation*,InnerClasses
    -keepnames class * implements android.os.Parcelable {
    public static final ** CREATOR;
    }
    #R
    -keepclassmembers class **.R$* {
    public static <fields>;
    }
    
    #AFA
    -dontwarn com.admost.**
    -keep class com.admost.** {*;}
    
    # AMAZON
    -dontwarn com.amazon.**
    -keep class com.amazon.** { *; }
    -dontwarn org.apache.http.**
    -keepattributes *Annotation*
    
    # APPLOVIN
    -dontwarn com.applovin.**
    -keep class com.applovin.** { *; }
    
    # APPNEXT
    -keep class com.appnext.** { *; }
    -dontwarn com.appnext.**
    
    # CHARTBOOST
    -dontwarn org.apache.http.**
    -dontwarn com.chartboost.sdk.impl.**
    -keep class com.chartboost.sdk.** { *; }
    -keepattributes *Annotation*
    
    # CRITEO
    -dontwarn com.criteo.**
    -keep class com.criteo.** { *; }
    
    # DISPLAYIO
    -keep class io.display.sdk.** { *; }
    -dontwarn io.display.sdk.**
    -keep class com.brandio.ads.** { *;}
    -dontwarn com.brandio.ads.**
    
    # FACEBOOK
    -dontwarn com.facebook.ads.**
    -dontnote com.facebook.ads.**
    -keep class com.facebook.** { *; }
    -keepattributes Signature
    -keep class com.google.android.exoplayer2.** {*;}
    -dontwarn com.google.android.exoplayer2.**
    
    # FLURRY
    -keep class com.flurry.** { *; }
    -dontwarn com.flurry.**
    -keepattributes *Annotation*,EnclosingMethod,Signature
    -keepclasseswithmembers class * { public <init>(android.content.Context, android.util.AttributeSet, int); }
    -keep class * extends java.util.ListResourceBundle { protected Object[][] getContents(); }
    -keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable { public static final *** NULL; }
    -keepnames @com.google.android.gms.common.annotation.KeepName class *
    -keepclassmembernames class * { @com.google.android.gms.common.annotation.KeepName *; }
    -keepnames class * implements android.os.Parcelable { public static final ** CREATOR; }
    
    # FREECORP
    -keep class com.fly.** { *; }
    -dontwarn com.fly.**
    
    # FYBER
    -keep class com.fyber.** { *; }
    -dontwarn com.fyber.**
    -keep class com.fyber.mediation.MediationConfigProvider { public static *; }
    -keep class com.fyber.mediation.MediationAdapterStarter { public static *; }
    -keepclassmembers class com.fyber.ads.videos.mediation.** { void setValue(java.lang.String); }
    
    # HUAWEI-ADS
    -keep class com.huawei.openalliance.ad.** { *; }
    -keep class com.huawei.hms.ads.** { *; }
    
    # INMOBI
    -keepattributes SourceFile,LineNumberTable
    -keep class com.inmobi.** {*;}
    -dontwarn com.inmobi.**
    -keep public class com.google.android.gms.**
    -dontwarn com.google.android.gms.**
    -dontwarn com.squareup.picasso.**
    -keep class com.google.android.gms.ads.identifier.AdvertisingIdClient{public *;}
    -keep class com.google.android.gms.ads.identifier.AdvertisingIdClient$Info{public *;}
    -keep class com.squareup.picasso.** {*;}
    -dontwarn com.squareup.picasso.**
    -dontwarn com.squareup.okhttp.**
    -keep class com.moat.** {*;}
    -dontwarn com.moat.**
    -keep class com.integralads.avid.library.* {*;}
    
    
    # INNERACTIVE
    -dontwarn com.fyber.**
    -keep class com.fyber.** {*;}
    -dontwarn com.inneractive.api.ads.**
    -keep class com.inneractive.api.ads.** {*;}
    -keepclassmembers class com.inneractive.api.ads.** {*;}
    -keepclassmembers class com.inneractive.api.ads.sdk.nativead.** {*;}
    -keepattributes Signature
    -keepattributes *Annotation*
    -keep class sun.misc.Unsafe { *; }
    -keep class com.google.gson.stream.** { *; }
    -keep class com.google.gson.examples.android.model.** { *; }
    -keep class com.google.gson.Gson { *; }
    -keep class com.google.gson.GsonBuilder { *; }
    -keep class com.google.gson.FieldNamingStrategy { *; }
    
    # IRONSOURCE
    -dontwarn com.ironsource.**
    -keep class com.ironsource.** { *; }
    -keepclassmembers class * implements android.os.Parcelable { public static final android.os.Parcelable$Creator *; }
    -keep public class com.google.android.gms.ads.** { public *; }
    -keep class com.ironsource.adapters.** { *; }
    -dontwarn com.moat.**
    -keep class com.moat.** { public protected private *; }
    
    # LOOPME
    -dontwarn com.loopme.**
    -keep class com.loopme.** { *; }
    
    # MEDIABRIX
    -keep class com.mediabrix.** { *; }
    -keep class com.moat.** { *; }
    -keep class mdos.** { *; }
    -dontwarn com.mediabrix.**
    -dontwarn com.moat.**
    -dontwarn mdos.**
    
    # MILLENNIAL & NEXAGE
    -keep class com.millennialmedia.** { *; }
    -dontwarn com.millennialmedia.**
    
    # MINTEGRAL
    -keepattributes Signature
    -keepattributes *Annotation*
    -keep class com.mbridge.** {*; }
    -keep interface com.mbridge.** {*; }
    -dontwarn com.mbridge.**
    -keepclassmembers class **.R$* { public static final int mbridge*; }
    
    -keep public class com.mbridge.* extends androidx.** { *; }
    -keep public class androidx.viewpager.widget.PagerAdapter{*;}
    -keep public class androidx.viewpager.widget.ViewPager.OnPageChangeListener{*;}
    -keep interface androidx.annotation.IntDef{*;}
    -keep interface androidx.annotation.Nullable{*;}
    -keep interface androidx.annotation.CheckResult{*;}
    -keep interface androidx.annotation.NonNull{*;}
    -keep public class androidx.fragment.app.Fragment{*;}
    -keep public class androidx.core.content.FileProvider{*;}
    -keep public class androidx.core.app.NotificationCompat{*;}
    -keep public class androidx.appcompat.widget.AppCompatImageView {*;}
    -keep public class androidx.recyclerview.*{*;}
    -keep class com.mbridge.msdk.foundation.tools.FastKV{*;}
    -keep class com.mbridge.msdk.foundation.tools.FastKV$Builder{*;}
    
    # MOBFOX
    -dontwarn com.mobfox.**
    -keep class com.mobfox.** { *; }
    -keep class com.mobfox.adapter.** { *; }
    -keep class com.mobfox.sdk.** { *; }
    
    # MYTARGET
    -keep class com.my.target.** {*;} 
    
    # NEND
    -keep class net.nend.android.** { *; }
    -dontwarn net.nend.android.**
    
    # NATIVEX
    -dontwarn com.nativex.**
    -keep class com.nativex.** { *; }
    
    # OGURY
    -dontwarn com.ogury.**
    -keep class com.ogury.** { *; }
    
    # OUTBID
    -dontwarn outbid.com.outbidsdk.**
    -keep class outbid.com.outbidsdk.** { *; }
    
    # QUMPARA
    -dontwarn com.qumpara.analytics.**
    -keep class com.qumpara.analytics.** { *; }
    -dontwarn com.qumpara.offerwall.sdk.**
    -keep class com.qumpara.offerwall.sdk.** { *; }
    
    #POLLFISH
    -dontwarn com.pollfish.** 
    -keep class com.pollfish.** { *; }
    
    # PUBNATIVE
    -keepattributes Signature
    -keep class net.pubnative.** { *; }
    -dontwarn net.pubnative.**
    -keep class com.squareup.picasso.** { *; }
    -dontwarn com.squareup.picasso.**
    
    # REVMOB
    -dontwarn rm.com.android.sdk.**
    -keep class rm.com.android.sdk.** { public *; }
    
    # RETROFIT
    -dontwarn retrofit2.**
    -keep class retrofit2.** { *; }
    -keepattributes Signature
    -keepattributes Exceptions
    -keepclasseswithmembers class * {
        @retrofit2.http.* <methods>;
    }
    
    # SMAATO
    -dontwarn com.smaato.**
    -keep class com.smaato.** { public *; }
    -assumenosideeffects class android.util.Log {
        public static *** d(...);
        public static *** v(...);
        public static *** i(...);
    }
    -keep public class com.smaato.soma.internal.connector.OrmmaBridge { public *; }
    -keepattributes *Annotation*
    -dontwarn com.smaato.soma.SomaUnityPlugin*
    -dontwarn com.millennialmedia**
    -dontwarn com.facebook.**
    
    # SMARTAD
    -keep class com.smartadserver.** { *; }
    -dontwarn com.smartadserver.**
    
    
    # STARTAPP
    -keepattributes Exceptions, InnerClasses, Signature, Deprecated, SourceFile, LineNumberTable, *Annotation*, EnclosingMethod
    -dontwarn android.webkit.JavascriptInterface
    -keep class com.startapp.** { *; }
    -dontwarn com.startapp.**
    
    # TAPJOY
    -keep class com.tapjoy.** {*;}
    -keep class com.moat.** {*;}
    -keepattributes JavascriptInterface
    -keepattributes *Annotation*
    -keep class * extends java.util.ListResourceBundle {protected Object[][] getContents();}
    -keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable {public static final *** NULL;}
    -keepnames @com.google.android.gms.common.annotation.KeepName class *
    -keepclassmembernames class * {@com.google.android.gms.common.annotation.KeepName *;}
    -keepnames class * implements android.os.Parcelable {public static final ** CREATOR;}
    -keep class com.google.android.gms.ads.identifier.** {*;}
    -dontwarn com.tapjoy.**
    
    # TAPPX
    -keepattributes *Annotation*
    -keepclassmembers class com.google.**.R$* { public static <fields>; }
    -keep public class com.google.ads.** {*;}
    -keep public class com.google.android.gms.** {*;}
    -keep public class com.tappx.** { *; }
    -dontwarn com.tappx.**
    
    #PANGLE
    -dontwarn com.bytedance.**
    -keep class com.bytedance.** {*;}
    
    # UNITY
    -dontwarn com.unity3d.**
    -keep class com.unity3d.ads.** { *; }
    
    # Vungle
    -dontwarn com.vungle.**
    -dontnote com.vungle.**
    -keep class com.vungle.** { *; }
    -dontwarn com.vungle.warren.error.VungleError$ErrorCode
    -keep class com.moat.** { *; }
    -dontwarn com.moat.**
    -dontwarn org.codehaus.mojo.animal_sniffer.IgnoreJRERequirement
    -dontwarn okio.**
    -dontwarn retrofit2.Platform$Java8
    -keepattributes Signature
    -keepattributes InnerClasses
    -keepattributes *Annotation*
    -dontwarn sun.misc.**
    -keep class com.google.gson.examples.android.model.** { *; }
    -keep class * implements com.google.gson.TypeAdapterFactory
    -keep class * implements com.google.gson.JsonSerializer
    -keep class * implements com.google.gson.JsonDeserializer
    -keep class com.google.android.gms.internal.** { *; }
    -dontwarn com.google.android.gms.ads.identifier.**
    
    -keepclassmembers enum com.vungle.warren.** { *; }
    -dontwarn kotlin.Unit
    -dontwarn retrofit2.-KotlinExtensions
    -keepclassmembers,allowshrinking,allowobfuscation interface * {
        @retrofit2.http.* <methods>;
    }
    -dontwarn okhttp3.**
    -dontwarn javax.annotation.**
    -dontwarn org.conscrypt.**
    -keepnames class okhttp3.internal.publicsuffix.PublicSuffixDatabase
    -keepclassmembers class * extends com.vungle.warren.persistence.Memorable {
       public <init>(byte[]);
    }
    
    -dontwarn com.google.protobuf.**
    -keepclassmembers class com.google.protobuf.** {
     *;
    }
    -keep class * extends com.google.protobuf.GeneratedMessageLite { *; }
    
    
    #YANDEX
    -dontwarn com.yandex.**
    -keep class com.yandex.** { *; }                        
    
    # YOUAPPI
    -keep class com.google.gson.**{ *;}
    -keep class com.google.android.gms.**{*;}
    -keep class com.youappi.sdk.**{*;}
    -keep interface com.youappi.sdk.**{*;}
    -keep enum com.youappi.sdk.**{*;}
    -keepclassmembers class * {
       @android.webkit.JavascriptInterface <methods>;
    }
    
    # VERIZON
    -keepclassmembers class com.verizon.ads** {
    public *;
    }
    -keep class com.verizon.ads**
        
    
    
    
        
            # ADMOST
            -keepattributes Exceptions, InnerClasses
            -dontwarn admost.sdk.**
            -keep class admost.sdk.** {*;}
            -dontwarn com.amr.unity.**
            -keep class com.amr.unity.** {*;}
            -dontwarn admost.adserver.**
            -keep class com.adjust.sdk.** {*;}
            -dontwarn com.adjust.sdk.**
            -keep class com.appsflyer.** {*;}
            -dontwarn com.appsflyer.**
            -keep class admost.adserver.** { *; }
            -dontwarn com.google.android.exoplayer2.**
            -keep class com.google.android.exoplayer2.**{ *;}
            -keep class android.support.v4.app.DialogFragment { *; }
            -keep class android.support.v4.util.LruCache { *; }
            
            # ADMOB / ADX / GOOGLE
            -keep class com.android.vending.billing.**
            -keep public class com.google.android.gms.ads.** { public *; }
            -keep public class com.google.ads.** { public *; }
            -keep class com.google.android.gms.** { *; }
            -dontwarn com.google.android.gms.**
            -keep public class com.google.android.gms.common.internal.safeparcel.SafeParcelable { public static final *** NULL; }
            -keepnames class * implements android.os.Parcelable
            -keepclassmembers class * implements android.os.Parcelable { public static final *** CREATOR; }
            -keep @interface android.support.annotation.Keep
            -keep @android.support.annotation.Keep class *
            -keepclasseswithmembers class * { @android.support.annotation.Keep <fields>; }
            -keepclasseswithmembers class * { @android.support.annotation.Keep <methods>; }
            -keep @interface com.google.android.gms.common.annotation.KeepName
            -keepnames @com.google.android.gms.common.annotation.KeepName class *
            -keepclassmembernames class * { @com.google.android.gms.common.annotation.KeepName *; }
            -keep @interface com.google.android.gms.common.util.DynamiteApi
            -keep public @com.google.android.gms.common.util.DynamiteApi class * { public <fields>; public <methods>; }
            -keep public @com.google.android.gms.common.util.DynamiteApi class * { *; }
            -keep class com.google.android.apps.common.proguard.UsedBy*
            -keep @com.google.android.apps.common.proguard.UsedBy* class *
            -keepclassmembers class * { @com.google.android.apps.common.proguard.UsedBy* *; }
            -dontwarn android.security.NetworkSecurityPolicy
            -dontwarn android.app.Notification
            
            # FACEBOOK
            -dontwarn com.facebook.ads.**
            -dontnote com.facebook.ads.**
            -keep class com.facebook.** { *; }
            -keepattributes Signature
            -keep class com.google.android.exoplayer2.** {*;}
            -dontwarn com.google.android.exoplayer2.**
            
            # MINTEGRAL
            -keepattributes Signature
            -keepattributes *Annotation*
            -keep class com.mbridge.** {*; }
            -keep interface com.mbridge.** {*; }
            -keep interface androidx.** { *; }
            -keep class androidx.** { *; }
            -keep public class * extends androidx.** { *; }
            -dontwarn com.mbridge.**
            
            #PANGLE
            -dontwarn com.bytedance.**
            -keep class com.bytedance.** {*;}
            -keep class **.R$* { public static final int mbridge*; }
        
    

### Shrink Resources

If you are using `shrinkResources true`, please add the lines below to your
`/app/src/res/raw/keep.xml` file

    
    
                        <?xml version="1.0" encoding="utf-8"?> <resources xmlns:tools="http://schemas.android.com/tools"     tools:keep="@layout/tt_activity_full_video,@layout/tt_*,@drawable/mbridge*,@drawable-hdpi-v4/mbridge*,@drawable-hdpi/mbridge*,@layout/mbridge*,@values/mbridge*,@anim/mbridge*" />
                        
                        

## Usage

Admost Mediation library is a lean yet complete library that allows you to
request and show ads. Basic integration steps are:

### Initialization

Initialize the Admost Mediation SDK in your application’s launcher Activity.
This starts pre-caching and prepares the SDK to display ads.

    
    
    AdMostConfiguration.Builder configuration = new AdMostConfiguration.Builder(this, < ADMOST_APP_ID >);
    					

For GDPR compliance, please read the GDPR section of this documentation. The
following configuration parameters are added for GDPR compliance.

    
    
    configuration.setSubjectToGDPR(false);
    configuration.setUserConsent(true);
    

For CCPA compliance, please read the CCPA section of this documentation. The
following configuration parameter is added for CCPA compliance. You can use
the **setUserConsent** parameter for passing consent to the SDK as in GDPR.

    
    
    configuration.setSubjectToCCPA(false);
    

According to [Google Play Services
policy](https://support.google.com/googleplay/android-
developer/answer/9285070), if your app's target age group include children
under the age of 18, ads shown to children must be served from a [Google Play
certified ad network](https://support.google.com/googleplay/android-
developer/answer/9283445). A neutral age screen must be implemented so that
any ads not suitable for children are only shown to older audiences.

For this purpose, we added the following configuration parameter and it is
needed to be set for the users considered as children.

    
    
    // Only set true if you know the user is child. 
    configuration.setUserChild(true);
    

OPTIONAL: In order to see the logs (TAG: ADMOST) and integration
errors/warnings for your debuggable builds, you may optionally enable ADMOST
logs + warning Toast messages.  
Important Note: Use your **applications's own BuildConfig file's DEBUG** field
(check BuildConfig package name when importing this java class) as a parameter
rather than setting true or false directly. It is critical.

    
    
    configuration.showUIWarningsForDebuggableBuild(BuildConfig.DEBUG);
    

After specifying related parameters, you have to call the following init
method with configuration and listener parameters.

    
    
    
    AdMost.getInstance().init(configuration.build(), new AdMostInitListener() {
    	@Override
    	public void onInitCompleted() {
    
    	}
    
    	@Override
    	public void onInitFailed(int err) {
    
    	}
    });
    

#### GDPR

Once you have collected the user’s consent, you can pass it onto the SDK using
the init configuration parameters shown above.

`setUserConsent` has a boolean parameter. If you have the user’s consent, set
it true. If you do not have the user's consent, set it false.

`setSubjectToGDPR` has a boolean parameter. If you know the user is subject to
GDPR, set it true. If you know the user is not subject to GDPR, set it false.

If you don’t pass the user’s consent or subjectToGDPR to the SDK, the default
rules of Admost SDK will be applied.

We strongly recommend you to read the following articles before continue;

  * [Admost GDPR rules](https://admost.github.io/privacy.html#gdprrules)
  * [Google consent management requirements for serving ads in the EEA and UK](tcf-cmp.html) NEW

  

#### CCPA

Once you have collected the user’s consent, you can pass it onto the SDK using
the init configuration parameters shown above.

`setUserConsent` has a boolean parameter. If you have the user’s consent, set
it true. If you do not have the user's consent, set it false.

`setSubjectToCCPA` has a boolean parameter. If you know the user is subject to
CCPA, set it true. If you know the user is not subject to CCPA, set it false.

If you don’t pass the user’s consent or subjectToCCPA to the SDK, the default
rules of Admost SDK will be applied.

**IMPORTANT NOTE:** We strongly recommend you to read our **[CCPA
section](https://admost.github.io/privacy.html#ccparules)**.

### Banner Ads

    
    
    /*
    ZONE_ID : Your ZONE_ID defined on admost mediation panels.
    BINDER  : You can use your own layout design for banners, if you leave BINDER value null, default design will be applied.
    */
    
    BANNER = new AdMostView(ACTIVITY, < ZONE_ID >, new AdMostBannerCallBack() {
        @Override
        public void onReady(String network, int ecpm, View adView){
            // Ad is loaded and ready to be shown.
            // adView is the loaded banner's view and you need to attach it in your layout.
            // Sample usage ( https://github.com/admost/amrandroid/tree/master/sample/AMRSample )
        }
    
        @Override
        public void onFail(int errorCode) {
            // Ad is not loaded and can not be shown.
    		// Warning: Attempting to load a new ad from the onFail() methods is strongly discouraged.
    		// If you must load an ad from onFail() ensure to limit ad load retries to avoid continuous
    		// failed ad requests in situations such as limited network connectivity.
        }
    
        @Override
        public void onClick(String network) {
            //Ad clicked
        }
        @Override
        public void onAdRevenuePaid(AdMostImpressionData impressionData) {
            // It indicates that the impression is counted
        }
    
    }, < BINDER >);
    // Add the following line to load an ad.
    BANNER.load();
    
                    

You can use tag functionality for banner zones. Tags will let you monitor the
performance of the ads across different dimensions for the same zone. You can
switch ads on and off for any specified tag whenever you want. Example usage
is as follows;

    
    
    // TAG can be any string value meaningful for you. You don't need to define it on AdMost dashboard before using.
    // Just start using, it will be automatically detected
    BANNER.load(TAG);
    				

You have to call destroy(), pause() and resume() methods in the activity.

    
    
    @Override
    public void onResume() {
        super.onResume();
        BANNER.resume();
    }
    
    @Override
    public void onPause() {
        super.onPause();
        BANNER.pause();
    }
    
    
    @Override
    public void onDestroy() {
        super.onDestroy();
        BANNER.destroy();
    }
    

#### Custom Native Design

If you want to create your own design for native ads, you have to create a
binder object and pass it to AdMostView constructor as BINDER value. Example
integration for binder creation is as follows;

    
    
    int layout = layout.design_for_your_banner;
    AdMostViewBinder BINDER = new AdMostViewBinder.Builder(layout)
    	.titleId(R.id.ad_headline)
    	.textId(R.id.ad_body)
    	.callToActionId(R.id.ad_call_to_action)
    	.iconImageId(R.id.ad_app_icon)
    	.mainImageId(R.id.ad_image)
    	.backImageId(R.id.ad_back)
    	.attributionId(R.id.ad_attribution)
    	.privacyIconId(R.id.ad_privacy) // it is only required for INMOBI native ads
    	.isRoundedMode(false)
    	.isFixed(false)
    	.isCloseable(false)
    	.build();

For privacy icon placement, you have to add the following ImageView to your
custom layout with **visibility GONE**. It is suggested to add it to the right
top corner of your layout with minimum width of 25dp;

    
    
    <ImageView
            android:id="@+id/ad_privacy"
            android:layout_width="26dp"
            android:layout_height="26dp"
            android:paddingTop="2dp"
            android:paddingBottom="10dp"
            android:paddingLeft="10dp"
            android:paddingRight="2dp"
            android:src="@drawable/ad_privacy"
            android:layout_alignParentRight="true"
            android:visibility="gone" />

### Interstitial

    
    
    AdMostInterstitial INTERSTITIAL = new AdMostInterstitial(ACTIVITY, < ZONE_ID >, new AdMostFullScreenCallBack() {
        @Override
        public void onDismiss(String message) {
            // It indicates that the interstitial ad is closed by clicking cross button/back button
        }
        @Override
        public void onFail(int errorCode) {
            // It indicates that the interstitial ad received no-fill response from all of its placements.
            // Therefore, the ad can not be shown.
            // Warning: Attempting to load a new ad from the onFail() methods is strongly discouraged.
            // If you must load an ad from onFail() ensure to limit ad load retries to avoid continuous
            // failed ad requests in situations such as limited network connectivity.
    
        }
        @Override
         public void onReady(String network, int ecpm) {
           // It indicates that the interstitial ad is loaded and ready to show.
        }
        @Override
        public void onShown(String network) {
            // It indicates that the loaded interstitial ad is shown to the user.
        }
        @Override
        public void onClicked(String s) {
            // It indicates that the interstitial ad is clicked.
        }
        @Override
        public void onComplete(String s) {
            // If you are using interstitial, this callback will not be triggered.
        }
        @Override
        public void onStatusChanged(int statusCode) {
            // This callback will be triggered only when frequency cap ended.
            // status code
            // 1 - AdMost.AD_STATUS_CHANGE_FREQ_CAP_ENDED
        }
        @Override
        public void onAdRevenuePaid(AdMostImpressionData impressionData) {
            // It indicates that the impression is counted
        }
    
    });
    
    

You can use the following statement to load interstitial.

    
    
    INTERSTITIAL.refreshAd(AUTO_SHOW);

AUTO_SHOW (boolean) : Set true, if you want to show the fullscreen ad as soon
as it is ready. Otherwise, you need to call show() method manually.

    
    
    INTERSTITIAL.show();

You can use tag functionality for interstitial zones. Tags will let you
monitor the performance of the ads across different dimensions for the same
zone. You can switch ads on and off for any specified tag whenever you want.
Example usage is as follows;

    
    
    // TAG can be any string value meaningful for you. You don't need to define it on AdMost dashboard before using.
    // Just start using, it will be automatically detected
    INTERSTITIAL.show(TAG);
    				

You have to call destroy method when you are done with the interstitial.

    
    
    INTERSTITIAL.destroy();

### App Open

App open ad is a special ad format intended for publishers wishing to monetize
their app load screens. App open ads can be closed at any time, and are
designed to be shown when your users bring your app to the foreground.

On Admost, app open ads are kind of Interstitial ads and you can use all
interstitial functionality for this ad type. Only difference is, app open ads
has to be shown when your users bring your app to the foreground but
Interstitial ads should be displayed during natural pauses in the flow of an
app. To have a better understanding, you may take a look at the Google Open
Ads implementation details from the following guide  
[AdMob App Open Ads
Documentation](https://developers.google.com/admob/android/app-open)

If you prefer to show ads in the same way with the Admob App Open Ads
documentation, you have to use Admost initialize method instead of Admob
initialize and AdmostInterstitial load and show methods instead of Admob
AppOpenAd methods.

You may need to initialize Admost on application class before having an
activity. In this situation, you can call init method as shown in the
following example with null activity.

    
    
    AdMostConfiguration.Builder configuration = new AdMostConfiguration.Builder(null, ADMOST_APP_ID);
    configuration.setApplicationContext(getApplicationContext());
    AdMost.getInstance().init(configuration.build());
                        

After initializing the sdk, if you still don't have an activity reference you
can call app open load method with null activity and listen to ad callbacks.

If you initialize the sdk without an activity reference, you have to set
latest activity with the following command before showing ad. Because app open
ads need an activity reference to be shown.

    
    
    AdMost.getInstance().setLauncherActivity(ACTIVITY);
                        

### Rewarded

    
    
    AdMostInterstitial VIDEO = new AdMostInterstitial(ACTIVITY, < ZONE_ID >, new AdMostFullScreenCallBack() {
            @Override
             public void onReady(String network, int ecpm) {
                // It indicates that the rewarded video ad is loaded and ready to show.
            }
            @Override
            public void onFail(int errorCode) {
              // It indicates that the rewarded video ad received no-fill response from all of its placements.
              // Therefore, the ad can not be shown.
              // Warning: Attempting to load a new ad from the onFail() methods is strongly discouraged.
              // If you must load an ad from onFail() ensure to limit ad load retries to avoid continuous
              // failed ad requests in situations such as limited network connectivity.
    
            }
            @Override
            public void onDismiss(String message) {
              // It indicates that the rewarded video ad is closed by clicking cross button/back button.
              // It does not mean that the user deserves to receive a reward. You need to check whether onComplete(String network) callback is called or not
            }
            @Override
            public void onComplete(String network) {
              // It indicates that the user deserves to receive a reward. You may need to store this information in a variable and give a reward
              // to the user after onDismiss(String message) callback is called by showing some animations for instance.
              // Note: If onComplete(String network) callback is called for the ad, it is always called before onDismiss(String message) callback.
            }
            @Override
            public void onShown(String network) {
              // It indicates that the loaded rewarded video ad is shown to the user.(Note: It does not mean that the user deserves a reward)
              // It is immediately called after the loaded ad is shown to the user using VIDEO.show()
            }
            @Override
            public void onClicked(String s) {
                // It indicates that the video ad is clicked.
            }
            @Override
            public void onStatusChanged(int statusCode) {
                // This callback will be triggered only when frequency cap ended.
                // status code
                // 1 - AdMost.AD_STATUS_CHANGE_FREQ_CAP_ENDED
            }
            @Override
            public void onAdRevenuePaid(AdMostImpressionData impressionData) {
                // It indicates that the impression is counted
            }
    		
        });
                    

You can use the following statement to load rewarded video.

    
    
    VIDEO.refreshAd(AUTO_SHOW);

AUTO_SHOW (boolean) : Set true, if you want to show the rewarded video ad as
soon as it is ready. Otherwise, you need to call show() method manually.

    
    
    VIDEO.show();

You can use tag functionality for rewarded video zones. Tags will let you
monitor the performance of the ads across different dimensions for the same
zone. You can switch ads on and off for any specified tag whenever you want.
Example usage is as follows;

    
    
    // TAG can be any string value meaningful for you. You don't need to define it on AdMost dashboard before using.
    // Just start using, it will be automatically detected
    VIDEO.show(TAG);
    				

You have to call destroy method when you are done with the rewarded video.

    
    
    VIDEO.destroy();

### Offerwalls

    
    
    OFFERWALL = new AdMostInterstitial(ACTIVITY, < ZONE_ID >, new AdMostFullScreenCallBack() {
            @Override
            public void onReady(String network) {
                // Ad Loaded
            }
            @Override
            public void onFail(int errorCode) {
                // Ad Failed
            }
            @Override
            public void onDismiss(String message) {
                // Ad Dismiss
            }
            @Override
            public void onComplete(String network) {
                // Video Ad Completed
            }
            @Override
            public void onShown(String network) {
                //Ad Shown
            }
            @Override
            public void onClicked(String s) {
                //Ad Clicked
            }
            @Override
            public void onStatusChanged(int statusCode) {
                // This callback will be triggered only when frequency cap ended.
                // status code
                // 1 - AdMost.AD_STATUS_CHANGE_FREQ_CAP_ENDED
            }
    });

You can use the following statement to load offerwall ad.

    
    
    OFFERWALL.refreshAd(AUTO_SHOW);

AUTO_SHOW (boolean) : Set true, if you want to show the offerwall ad as soon
as it is ready. Otherwise, you need to call show() method manually.

    
    
    OFFERWALL.show();

You can use tag functionality for offerwall zones. Tags will let you monitor
the performance of the ads across different dimensions for the same zone. You
can switch ads on and off for any specified tag whenever you want. Example
usage is as follows;

    
    
    // TAG can be any string value meaningful for you. You don't need to define it on AdMost dashboard before using.
    // Just start using, it will be automatically detected
    OFFERWALL.show(TAG);
    				

You have to call destroy method when you are done with the offerwall ad.

    
    
    OFFERWALL.destroy();

  

####  Spending Virtual Currencies

    
    
    AdMost.getInstance().spendVirtualCurrency(new AdMostVirtualCurrencyListener() {
        @Override
        public void onSuccess(String adNetwork, String currencyName, double value) {
            // User rewarded (This method can be triggered multiple times depends on Offerwall Zone)
        }
    
        @Override
        public void onError(String adNetwork, String error) {
            // Error
        }
    });
                    
        

## Extras

### Google AdManager Integration

The Admost AdManager Adapters lets publishers to integrate Admost ads into
applications with minimum development effort. In order to show Admost ads
through AdManager, you should only follow setup and init phases of this
documentation. You don't need to implement usage section of this
documentation. The rest of the integration is about defining Admost adapters
and zone id's for all ad types in AdManager dashboard.

#### AdManager Dashboard

You sould follow the following steps to target an AdManager ad unit with
AdMost ad.

1\. Create a new Yield Group for the ad format you want and target your ad
unit  
2\. Add Yield partner for the created yield group  
3\. Fill the class names and parameter values of Yield partner details with
the following values  

##### Class Name

Banner : `admost.sdk.dfp.AmrDfpCustomEventBanner`

Interstitial : `admost.sdk.dfp.AmrDfpCustomEventInt`

Rewarded : `admost.sdk.dfp.AmrDfpCustomEventRewarded`

##### Parameter

Zone Id of related zone created on AdMost Dashboard

  

**Yield GROUP**

![shadowed image](assets/img/YieldGroup.png)  

**Yield PARTNER**

![shadowed image](assets/img/YieldPartner.png)

Now you can show Admost banner, interstitial and rewarded ads through Google
AdManager.

You can check AdManager banner and interstitial example in demo project;
[AdManagerIntegration](https://github.com/admost/amrandroid/blob/master/sample/AMRSample/app/src/main/java/com/kokteyl/amrunity/DFPIntegrationSampleActivity.java).

### Test Suite

You can use Test Suite to test your defined ad networks, you have to be a
tester to use this function. To be a tester, you should add your GAID to
Admost Dashboard Mediation > Manage Testers > New Tester. Tester activation
takes 15 minutes. Use the following code to open test suite activity;

    
    
    AdMost.getInstance().startTestSuite();
                    

If you set user consent false, then you should add Admost generated id. You
can find the id from log by searching 'admost'.  
Example log:  
/ADMOST: To enable AMR tester mode use this id : <201903210418A57D7ZBJSRTPY>
on AMR dashboard Manage Testers page!

__

### Screen Shot

![android-test-suite screenshot](assets/img/android_testsuite.png?v=1)

### Huawei AppGallery Applications

For Huawei AppGallery applications, it is recommended to create a new Admost
applcation on the dashboard and use new placements from ad networks to track
performance separately. For Huawei AppGallery applications, we are using
OAID(Open Advertiser ID) instead of GAID(Google Advertising ID) for
attribution purposes, so we need to know if the application is Huawei
AppGallery application. To set the application as Huawei app, you can use the
following method during initialization, otherwise AdMost sdk will try to get
GAID and fail.

    
    
    AdMostConfiguration.Builder configuration = new AdMostConfiguration.Builder(this, [APPLICATION_ID]);
    configuration.setAsHuaweiApp();
    AdMost.getInstance().init(configuration.build());
                    

### In App Purchase Tracking

The following call is used to track purchases:

    
    
    
    AdMost.getInstance().trackIAP(purchaseData, signature, priceAmountMicros, currency, tags, isDebug);
    

Explanation and code samples of parameters:

  * **purchaseData (String)** – a String in JSON format that contains details about the purchase order. It is returned by the operating system after you make the purchase call. 
  * **signature (String)** – String containing the signature of the purchase data that the developer signed with their private key. It is returned by the operating system after you make the purchase call. 
  * **priceAmountMicros (Double)** – Price in micro-units, where 1,000,000 micro-units equal one unit of the currency.
  * **currency (String)** – ISO 4217 currency code for price and original price.
  * **tags (String[])** \- You can add tags to the purchase to track it on Admost dashboard. If you don't want to use this parameter, leave it null. 
  * **isDebug (boolean)** \- Set true for test purchases. 

    
    
    @Override
    public void onPurchasesUpdated(BillingResult billingResult, @Nullable List purchases) {
        if (billingResult.getResponseCode() == BillingClient.BillingResponseCode.OK
                && purchases != null
                && purchaseItem != null) {
            for (Purchase purchase : purchases) {
                if (purchase.getSkus().size() > 0 && purchase.getSkus().get(0).equals(skuToSend) && purchase.getPurchaseState() == Purchase.PurchaseState.PURCHASED) {
                        AdMost.getInstance().trackIAP(purchase.getOriginalJson(), purchase.getSignature(), priceAmountMicros, currency, new String[] {"tag1","tag2"}, false );
                        break;
                }
            }
        }
    }   
                    

After your integration complete, enter your app's public key on Admost
Mediation dashboard. (Mediation > My Apps > Edit App)

To find the public key portion of this key pair, open your application's
details in the Play Console, click **Left Panel > Monitize > Monetization
Setup** , and get the key( Base64-encoded RSA public key ) that is shown under
**Licensing**.

For detailed information follow this
[link](https://developer.android.com/google/play/billing/integrate).

On subscription tracking, there is no difference in terms of client
integration. However, for inquiry of application's periodic earnings, you have
to create a service account on your Google api console project which is linked
to your application and give financial data permission to this account on your
google play developer console. While creating service account, you have to
choose JSON as key type and send this JSON file to AdMost account manager.

### Amazon Store In App Purchase Tracking

The following call is used to track amazon purchases with receipt validation:

    
    
    AdMostIAPListener iabListener = new AdMostIAPListener() {
    	//Successful Purchase
    	@Override
    	public void onValidationSuccess(String admostIapID) {}
    
    	//Invalid purchase data..!
    	@Override
    	public void onValidationFail(String admostIapID, AdMostServerException e) {}
    
    	//Exception occurred, will be tried again automatically..!
    	@Override
    	public void onException(String admostIapID) {}
    };
    
    String admostIapID = AdMost.getInstance().trackPurchaseAmazon(receiptJSON, purchaseResponseJSON, productJSON, iabListener, isDebug);
                    

Explanation and code samples of parameters:

  * **receiptJSON (JSONObject)** – a JSON object. Retrieve that value from com.amazon.device.iap.model.PurchaseResponse OR com.amazon.device.iap.model.PurchaseUpdatesResponse like this:  

    * purchaseResponse.getReceipt().toJSON() 
    * purchaseUpdatesResponse.getReceipts().get(indexOfRelatedReceipt).toJSON() 
  * **purchaseResponseJSON (JSONObject)** – a JSON object. Retrieve that value from com.amazon.device.iap.model.PurchaseResponse OR com.amazon.device.iap.model.PurchaseUpdatesResponse object like this:  

    * purchaseResponse.toJSON() 
    * purchaseUpdatesResponse.toJSON() 
  * **productJSON (JSONObject)** – a JSON object. Retrieve that value from com.amazon.device.iap.model.Product object like this:  

    * product.toJSON() 
  * **iabCallback (AdMostIAPCallback)** \- You can add this callback to be informed about the result of your purchase request. null value is 
  * **isDebug (boolean)** \- Set true for test purchases. 

### Huawei AppGallery In App Purchase Tracking

The following call is used to track Huawei purchases:

    
    
    
    AdMost.getInstance().trackIAPForHuawei(purchaseData, signature, tags, isDebug);
                    

You can find the sample code below.

    
    
    //Handles an activity result that's part of the purchase flow in in-app billing
    void onActivityResult(int requestCode, int resultCode, Intent data) {
    
        super.onActivityResult(requestCode, resultCode, data);
    
        if (requestCode == REQ_CODE_BUY) {
            if (data == null) {
                Toast.makeText(this, "error", Toast.LENGTH_SHORT).show();
                return;
            }
    
            PurchaseResultInfo purchaseResultInfo = Iap.getIapClient(this).parsePurchaseResultInfoFromIntent(data);
            AdMost.getInstance().trackIAPForHuawei(purchaseResultInfo.getInAppPurchaseData(), purchaseResultInfo.getInAppDataSignature(), new String[]{"tags you want","another tag"}, false);
        }
    }
                    

### Setting Application User Id

You can use the following method to set application specific user id in Admost
Analytics for enhanced tracking of your users. This information is also
required for server to server callbacks. It is added to the callback URL to
distinguish rewarded user.

    
    
    AdMost.getInstance().setUserId("APPLICATION_USER_ID");
    
                    

### Adjust Integration

In order to enhance Admost data with the Adjust campaign tracking
functionality, first you have to integrate Adjust sdk into your application as
described in the Adjust documentation. Admost sdk will match the Adjust and
Admost user definitions with the id provided by the Adjust sdk automatically.
Please note that, in order to correctly attribute an app install to its
source, Adjust needs information about the install referrer. So, implementing
Google install referrer solution is important for Adjust. You can find the
instructions from the following link.  
[adjust-install-referrer](https://github.com/adjust/android_sdk#install-
referrer)

### Server to Server Callbacks

For rewarded video ads, you can use Server to Server Callbacks for rewarding
users after successful completion of video ads. Please consult your business
contact person for enabling it and setting required parameters like callback
URL, request verification token and method.  
To use this feature, only requirement on application side is setting your
application user id as described here. You may also add new custom parameters
to the callback URL by setting custom data to the rewarded video
object(AdMostInterstitial) as shown in the sample code below. This method has
to be called before showing ad.

    
    
    Hashtable customData = new Hashtable<>();
    customData.put("os", Build.VERSION.SDK_INT);
    customData.put("ip", "172.12.1.23");
    REWARDED.setSSVCustomData(customData);
                    

### Privacy Consent Check

You can use the following method to check if the user is in a country which is
subject to GDPR or CCPA.

    
    
    AdMost.getInstance().setPrivacyConsentListener(this, new AdMost.PrivacyConsentListener() {
    	@Override
    	public void isPrivacyConsentRequired(string consentType) {
    		// Possible consentType values : "CCPA" , "GDPR" , "None"
    
    	}
    });
                    

### Remote Config

Admost Remote config is a feature for defining and updating server side
parameters from the Admost dashboard. You can define the parameters in long,
double, boolean and string types. To define parameters on Admost dashboard,
click on settings icon on My Apps page and select Remote Config item from the
list. The following page will pop up. You can define your parameters in this
page in JSON format.

  
![android-test-suite screenshot](assets/img/remote_config.png?v=1)  

To read the parameter values in your app, you can use the following methods of
the sdk. It is suggested to use these methods after admost initialization
completed, otherwise default values you set will be returned for new users.
For existing users, the data stored in shared preferences will be used before
initialization.

    
    
    AdMostRemoteConfig.getInstance().getLong("closePopupInSeconds",0L);
    AdMostRemoteConfig.getInstance().getString("version","1.0.0");
    AdMostRemoteConfig.getInstance().getDouble("price",3.1);
    AdMostRemoteConfig.getInstance().getBoolean("isDebug",false);
                    

You can also run A/B tests for remote config parameters bundling with other
mediation related test parameters. You do not have to do anything to run or
join these tests on client side, random percentile targeting feature of the
sdk will handle it itself. You can define these tests and target your
audiences from the dashboard's A/B test menu.

### A/B Test

AdMost A/B test feature is available on the sdk since version 2.0.0 have been
released, but until the relase of remote config feature it was only used for
the monetisation parameters tests. Now it is capable of doing in-game feature
tests with remote config parameters as well.

For using A/B test feature, you don't need to do anything on client side. All
settings can be done over the Dashboard.

Click here to see the documentation about the capabilities of Admost A/B test.

### CMP(Consent Management Platform) Integration

Starting January 16, 2024 Publishers and developers using Google AdSense, Ad
Manager, or AdMob will be required to use a Consent Management Platform (CMP)
that has been certified by Google and has integrated with the IAB's
Transparency and Consent Framework (TCF) when serving ads to users in the
European Economic Area or the UK.

As Admost, we have integration with Google’s CMP tool User Messaging Platform
(UMP). As a publisher, if you chose to continue with the UMP, you have to be
sure about the following steps;

  * Add UMP SDK into your app and complete the integration according to the UMP integration documentation.
  * Create a proper GDPR message for your app on the UMP dashboard.
  * Select all active ad networks and "Admost" as Vendor on the UMP dashboard.
  * Check Auto UMP Detection checkbox on Admost dashboard application edit popup.
  * Inform Admost SDK about the result of the Consent flow with the following lines 

Before Initialization;

    
                                        configuration.canRequestAds(consentInformation.canRequestAds);
                                    

After Initialization

    
                                        AdMost.getInstance().setCanRequestAds(consentInformation.canRequestAds);
                                    

If you are using CMP tool other than UMP, after completing the integration
with the CMP tool you have to inform Admost SDK about the consent result of
Custom Vendors including ADMOST before Admost initialization. Custom vendors
can be any ad network used for monetization which are created manually and are
not registered with IAB. Even if you don't have any extra custom vendors in
your application, you have to add ADMOST as a custom vendor. You can use the
following code snippet;

    
    
    HashMap vendorMap = new HashMap<>();
    vendorMap.put(AdMostAdNetwork.ADMOST, CONSENT_RESULT_BOOLEAN);
    vendorMap.put(AdMostAdNetwork.APPLOVIN, CONSENT_RESULT_BOOLEAN);
    AdMost.getInstance().setCustomVendors(vendorMap);   
                            

### Third Party A/B Test

If you are running an A/B test on another platform and want to track A/B test
users on Admost cohort analysis page, you have to follow the following steps;

  * Create an A/B test on Admost dashboard and connect your external A/B test with the new one
  * Call the following method as soon as you get the proper A/B test and group id from the external platform 

Call this method after Admost initialization

    
                                        AdMost.getInstance().setThirdPartyExperiment("firebase-test-id","group_A");
                                    

If the A/B test doesn't match with the id given on Admost dashboard, A/B test
will not be followed on dashboard.  
Group Id is free text field, it can have any value like "A", "B", "Group A"
etc.

Click here to see the documentation about the capabilities of Admost A/B test.

### Campaign Tracking

For tracking an ad campaign's performance, it is recommended to add Admost
install referrer receiver into application tag of your AndroidManifest.xml for
better tracking. If you are using other receiver libraries in your application
like Google Analytics campaign tracking receiver, you can use the
**admost.install.referrer.[1-5]** meta-data like below.

    
    
    <manifest>
    	<application>
    		<receiver
    			android:name="admost.sdk.base.InstallReferrerReceiver"
    			android:exported="true">
    			<intent-filter>
    				<action android:name="com.android.vending.INSTALL_REFERRER" />
    			</intent-filter>
    			<meta-data android:name="admost.install.referrer.1" android:value="com.google.android.gms.analytics.CampaignTrackingReceiver" />
    		</receiver>
    	</application>
    </manifest>
    
                    

The Install Referrer API is exposed by the Google Play Store app on a device.
Devices with a Google Play app version of 8.3.73 or later automatically have
access to the API. Admost is using this functionality if available for better
tracking. It is required to add the following dependency to your app gradle to
enable this functionality.

    
    
    dependencies {
        implementation 'com.android.installreferrer:installreferrer:1.0'
    }
                    

__

Copyright (C) 2017\. All right reserved

  * [iOS Integration](http://admost.github.io/amrios)
  * [Unity Integration](http://admost.github.io/amrunity)
  * [Contact us](mailto:android@kokteyl.com)

