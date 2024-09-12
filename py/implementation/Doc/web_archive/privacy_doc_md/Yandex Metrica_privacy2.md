[![Logo icon](https://yastatic.net/s3/doc-binary/src/support/mobile-
ads/en/logo/rsya.svg)](/)

  * [Quick start](/helpcenter/en/quick-start "Quick start")
  * [Monetization](/helpcenter/en/monetization "Monetization")
  * SDK

    * [Android](/helpcenter/en/dev/android "Android")
    * [iOS](/helpcenter/en/dev/ios "iOS")
    * [Unity](/helpcenter/en/dev/unity "Unity")
    * [Flutter](/helpcenter/en/dev/flutter "Flutter")

  * [Documents and payments](/helpcenter/en/docs-and-payments "Documents and payments")
  * [Support](/helpcenter/en/support "Support")

  * 

  * Android
  * [SDK integration](/helpcenter/en/dev/android/quick-start)
  * [Guide on migrating to version 6](/helpcenter/en/dev/android/release/6-0-0-migration)
  * [Guide on migrating to version 7](/helpcenter/en/dev/android/release/7-0-0-migration)
  * [Ad formats](/helpcenter/en/dev/android/formats)
  * [Ad targeting](/helpcenter/en/dev/android/target)
  * User privacy and policy compliance
    * [GDPR](/helpcenter/en/dev/android/gdpr)
    * [COPPA](/helpcenter/en/dev/android/coppa)
    * [Accounting contextual data](/helpcenter/en/dev/android/context-data)
    * [TCF v2.0 Consent](/helpcenter/en/dev/android/tcf-2-0)
    * [Using advertising IDs](/helpcenter/en/dev/android/ad-id)
    * [Data safety in Google Play](/helpcenter/en/dev/android/app-privacy-android)
  * Yandex Mediation
  * Advanced settings
    * [Impression Level revenue data (ILRD)](/helpcenter/en/dev/android/impression-level)
    * [Settings for Adfox](/helpcenter/en/dev/android/adfox-parameters)
  * [Changelog](/helpcenter/en/dev/android/changelog-android)
  * [Integration example](/helpcenter/en/dev/android/example-android)
  * Testing tools
  * [Third-party mediation platforms](/helpcenter/en/dev/android/third-mediation)

## In this article:

  * Requirements for using the function
  * How to enable contextual data accounting
  * How to disable contextual data accounting

  1. User privacy and policy compliance
  2. Accounting contextual data

# Accounting contextual data

  * Requirements for using the function
  * How to enable contextual data accounting
  * How to disable contextual data accounting

Note

To make the Mobile Ads SDK take the app context into account, [enable the
AppMetrica SDK](https://appmetrica.yandex.com/docs/mobile-sdk-
dg/android/about/android-initialize.html) version 3.14.3 and higher.

Contextual data tracking was made available on August 20, 2020.

To make monetization more effective, the Mobile Ads SDK automatically takes
into account the app context: interface texts, their topics, and how the user
interacts with content. This results in selecting more relevant ads.

At the same time:

  * You can restrict contextual data tracking, for example, in places where users enter confidential information: on payment screens or in personal correspondence.

  * You can completely disable contextual data accounting.

  * The SDK only takes into account depersonalized data and corresponds to the [ISO standard](https://appmetrica.yandex.ru/docs/data-security/iso-27001.html).

## Requirements for using the functionRequirements for using the function

  1. The function is only available for Android.
  2. The minimum supported version of the AppMetrica SDK is 3.14.3 and higher.
  3. The minimum supported version of the Mobile Ads SDK is Android 2.160 and higher.

## How to enable contextual data accountingHow to enable contextual data
accounting

To enable automatic tracking of contextual app data, initialize version 3.14.3
or later of the [AppMetrica SDK](https://appmetrica.yandex.com/docs/mobile-
sdk-dg/android/about/android-initialize.html#init2) library.

## How to disable contextual data accountingHow to disable contextual data
accounting

You can disable automatic accounting for different entities: Application,
Activity, or View:

Application

Activity

View

To disable automatic accounting of contextual data for the entire app, in the
AndroidManifest.xml file at the application level, add the following code:

    
    
      <meta-data
          android:name="@string/yandex_ads_context"
          android:value="@string/yandex_ads_context_do_not_parse"/>
    

Code example:

    
    
      <application
          android:name="com.yandex.appmetrica.autotests.agent.AgentApplication"
          ...>
          <meta-data
              android:name="@string/yandex_ads_context"
              android:value="@string/yandex_ads_context_do_not_parse"/>
      </application>
    

To disable automatic accounting of contextual data for a specific activity, in
the AndroidManifest.xml file at the activity level, add the following code:

    
    
    <meta-data
        android:name="@string/yandex_ads_context"
        android:value="@string/yandex_ads_context_do_not_parse"/>
    

**Code example:**

    
    
      <activity
          android:name=".NoContextActivity"
          ...>
          <meta-data
              android:name="@string/yandex_ads_context"
              android:value="@string/yandex_ads_context_do_not_parse"/>
      </activity>
    

There are two ways to disable automatic accounting of contextual data for a
particular view:

**In the Android resources of a project**

    
    
      <TextView ...>
          <tag android:id="@id/yandex_ads_context"
             android:value="@string/yandex_ads_context_do_not_parse"/>
      </TextView>
    

**Programmatically**

    
    
      view.setTag(R.id.yandex_ads_context, getString(R.string.yandex_ads_context_do_not_parse))
    

### Was the article helpful?

YesNo

Previous

[COPPA](/helpcenter/en/dev/android/coppa)

Next

[TCF v2.0 Consent](/helpcenter/en/dev/android/tcf-2-0)

![](https://mc.yandex.ru/watch/60763294)

