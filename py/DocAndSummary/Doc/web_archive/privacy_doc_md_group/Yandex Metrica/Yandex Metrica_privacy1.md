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

  * General information
  * Quick guide

  1. User privacy and policy compliance
  2. COPPA

# COPPA

  * General information
  * Quick guide

## General informationGeneral information

On April 21, 2000, the Children's Online Privacy Protection Act
([COPPA](https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-312))
became effective. The act governs the collection of personal information from
children under the age of 13 by individuals or entities within US
jurisdiction. Pursuant to the Act, the application operator shall include in
their privacy policy the methods for obtaining parental or caretaker's
consent, as well as the operator's commitment to protecting the privacy and
safety of children on the internet, including marketing restrictions.

Data about the user's age must be transmitted to the SDK every time the
application starts.

Starting in version 5.4.0, the Yandex Mobile Ads SDK will enable you to
restrict the collection of information from children under the age of 13.

## Quick guideQuick guide

Data about the user's age must be transmitted to the SDK every time the
application starts.

  1. Follow the [instructions](quick-start) for connecting the Mobile Ads SDK.

  2. Show a window where the user can accept the user agreement for personal data processing (for more information, see the [example](https://github.com/yandexmobile/yandex-ads-sdk-android/tree/master/YandexMobileAdsExample/app/src/main/java/com/yandex/ads/sample)).

  3. Use the `setAgeRestrictedUser` method to pass the received value to the Mobile Ads SDK. By default, it is assumed that the user isn't a child under the age of 13.

### Was the article helpful?

YesNo

Previous

[GDPR](/helpcenter/en/dev/android/gdpr)

Next

[Accounting contextual data](/helpcenter/en/dev/android/context-data)

![](https://mc.yandex.ru/watch/60763294)

