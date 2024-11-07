SDK name: Yandex Metrica
Documentation:
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
  2. GDPR

# GDPR

  * General information
  * Quick guide

## General informationGeneral information

The General Data Protection Regulation (GDPR) came into effect in the spring
of 2018. GDPR regulates how information about citizens of the European
Economic Area and Switzerland can be collected and processed. Its intention is
to protect the privacy of confidential data and to ensure the transparency of
all processes related to the collection, storage and processing of information
on the internet.

The GDPR has an extraterritorial scope that applies to all companies that
process the personal data of citizens of the European Economic Area and
Switzerland, regardless of where the company is located.

## Quick guideQuick guide

The user's consent for processing personal data must be sent to the SDK each
time the application is launched.

  1. Follow the [instructions](quick-start) for connecting the Mobile Ads SDK.

  2. Show a window where the user can accept the user agreement for personal data processing (for more information, see the [example](https://github.com/yandexmobile/yandex-ads-sdk-android/tree/master/YandexMobileAdsExample/app/src/main/java/com/yandex/ads/sample)).

This code is a sample, not a step-by-step guide to follow.

Kotlin

Java

    
        class GdprDialogFragment : DialogFragment() {
        // ...
        // Example of creating a dialog window.
        override fun onCreateDialog(savedInstanceState: Bundle?): Dialog {
            val context = requireContext()
            val builder: AlertDialog.Builder = AlertDialog.Builder(context)
            builder.setTitle(R.string.gdpr_dialog_title)
                .setMessage(R.string.gdpr_dialog_message)
                .setPositiveButton(R.string.accept) { _, _ -> onButtonClicked(context, true) }
                .setNeutralButton(R.string.about) { _, _ -> openPrivacyPolicy() }
                .setNegativeButton(R.string.decline) { _, _ -> onButtonClicked(context, false) }
            return builder.create()
        }
    
        private fun openPrivacyPolicy() {
            val url = getString(R.string.privacy_policy_url)
            val intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
            startActivity(intent)
        }
    
        private fun onButtonClicked(context: Context, userConsent: Boolean) {
            val preferences: SharedPreferences = PreferenceManager.getDefaultSharedPreferences(context)
            preferences.edit()
                .putBoolean(SettingsFragment.USER_CONSENT_KEY, userConsent)
                .putBoolean(SettingsFragment.DIALOG_SHOWN_KEY, true)
                .apply()
            noticeDialogListener.onDialogClick()
        }
    }
    
    
        // ...
    public class GdprDialogFragment extends DialogFragment {
        // ...
        // Example of creating a dialog window.
        public Dialog onCreateDialog(Bundle savedInstanceState) {
            final Context context = getContext();
    
            AlertDialog.Builder builder = new AlertDialog.Builder(context);
            builder.setTitle(R.string.gdpr_dialog_title)
                    .setMessage(R.string.gdpr_dialog_message)
                    .setPositiveButton(R.string.accept, (dialog, id) ->
                            onButtonClicked(context, true))
                    .setNeutralButton(R.string.about, (dialog, which) ->
                            openPrivacyPolicy())
                    .setNegativeButton(R.string.decline, (dialog, id) ->
                            onButtonClicked(context, false));
            return builder.create();
        }
    
        private void openPrivacyPolicy() {
            final String url = getString(R.string.privacy_policy_url);
            final Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
            startActivity(intent);
        }
    
        private void onButtonClicked(final Context context,
                                     final boolean userConsent) {
            final SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(context);
            preferences.edit()
                    .putBoolean(SettingsFragment.USER_CONSENT_KEY, userConsent)
                    .putBoolean(SettingsFragment.DIALOG_SHOWN_KEY, true)
                    .apply();
    
            mNoticeDialogListener.onDialogClick();
        }
    }
    

  3. Use the `setUserConsent` method to pass the received value to the Mobile Ads SDK. Data of users located in the GDPR region will be processed only if the user consents to data processing.

### Was the article helpful?

YesNo

Previous

[Ad targeting](/helpcenter/en/dev/android/target)

Next

[COPPA](/helpcenter/en/dev/android/coppa)

![](https://mc.yandex.ru/watch/60763294)

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

