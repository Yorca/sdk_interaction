[![Logo](https://ogury-
ltd.gitbook.io/~gitbook/image?url=https%3A%2F%2F3481785215-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
x-
prod.appspot.com%2Fo%2Fspaces%252F-LwmnMrU_Opf4plVgohC%252Flogo%252FOtYgqbt4P2FNWQPpLxjY%252FOgury_White_Green_RGB.png%3Falt%3Dmedia%26token%3Da63d6bb2-1d85-482c-82f8-bdea2145ac79&width=192&dpr=4&quality=100&sign=951ecbe2&sv=1)![Logo](https://ogury-
ltd.gitbook.io/~gitbook/image?url=https%3A%2F%2F3481785215-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
x-
prod.appspot.com%2Fo%2Fspaces%252F-LwmnMrU_Opf4plVgohC%252Flogo%252FOtYgqbt4P2FNWQPpLxjY%252FOgury_White_Green_RGB.png%3Falt%3Dmedia%26token%3Da63d6bb2-1d85-482c-82f8-bdea2145ac79&width=192&dpr=4&quality=100&sign=951ecbe2&sv=1)](/android)

More

SearchCtrl \+ K

  * [Getting started](/android)

  * [Test your implementation](/android/test-your-implementation)

  * [Release notes](https://docs.ogury.co/release-notes/android/ogury-sdk)
  * Ad Formats

    * [Interstitial Ad](/android/ad-formats/interstitial-ad)

    * [Opt-in Video Ad](/android/ad-formats/opt-in-video-ad)

    * [Banner Ad](/android/ad-formats/banner-ad)

    * [Thumbnail Ad](/android/ad-formats/thumbnail-ad)

  * Ogury Choice Manager

    * [Collect the user consent](/android/ogury-choice-manager/collect-the-user-consent)

    * [Third-party consent manager](/android/ogury-choice-manager/third-party-consent-manager)

    * [Advanced usages](https://docs.ogury.co/choice-manager-android/advanced-usages)
  * Help

    * [Migration guide](/android/help/migration-guide)

    * [FAQ](/android/help/faq)

    * [Help center](https://ogury-ltd.gitbook.io/help-center-for-publishers/)

[Powered by
GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=-LwmnMrU_Opf4plVgohC-1994518377)

# Getting started

This documentation will go through all the steps required to display Ogury ads
on Android platform.

From October 2020, Ogury released a new API specially refactored to improve
the onboarding experience. If you have already integrated the Ogury SDK and
want to update your integration with the latest API, you can read the
[Migration guide](/android/help/migration-guide). It explains the main points
to easily switch from the old API to the new one.

##

Step 1: Register your application

  * [Log into your Ogury's publisher platform](https://ogury-ltd.gitbook.io/help-center-for-publishers/set-up-ogury-global-demand/setup-your-accounts).

  * [Register your application](https://ogury-ltd.gitbook.io/help-center-for-publishers/set-up-ogury-global-demand/how-to-create-an-asset#register-your-asset) and [save your **Asset Key**](https://ogury-ltd.gitbook.io/help-center-for-publishers/set-up-ogury-global-demand/how-to-create-an-asset#save-your-asset-key)**.**

The **Asset Key** follows the pattern**:**`OGY-XXXXXXXXXXXX`, where `X` is an
uppercase letter or digit. In all the following code samples, we will refer to
this **Asset Key** by using the string `OGY-XXXXXXXXXXXX`.

##

Step 2: Import the Ogury SDK

To import the latest version of the Ogury SDK into your project:

  * Open the `build.gradle` of your application.

  * Add the following lines:

Copy

    
    
    repositories {
        maven {
            url 'https://maven.ogury.co'
        }
    }
    dependencies {
        implementation 'co.ogury:ogury-sdk:5.+'
    }

To know more about the latest release of the Ogury SDK, you can check the
[release notes](https://docs.ogury.co/release-notes/android/ogury-sdk).

##

Step 3: Initialize the Ogury SDK

After you have registered your app and imported the Ogury SDK, you must call
`Ogury.start()` before you use any Ogury's functionalities.

Copy

    
    
    OguryConfiguration.Builder oguryConfigurationBuilder = new OguryConfiguration.Builder(this, "OGY-XXXXXXXXXXXX");
    Ogury.start(oguryConfigurationBuilder.build());

The `start` method takes an `OguryConfiguration` object as parameters. The
`OguryConfiguration` is built from its `Builder` which takes the following
parameters:

  * the [`Application`](https://developer.android.com/reference/android/app/Application) context.

  * the **Asset Key** of your application. If you do not have one yet, you can refer to the [first step](/android#step-1-register-your-application) to create it.

The paragraph below is addressed to mediation SDK partners. If you are a
publisher, you can directly go to step 4.

As a mediation SDK partner, please make sure add an extra line of code in your
adapter in order to pass Ogury the name & the version of your SDK. Here is how
it would look like:

Copy

    
    
    Configuration.Builder oguryConfigurationBuilder = new OguryConfiguration.Builder(this, "OGY-XXXXXXXXXXXX");
    oguryConfigurationBuilder.putMonitoringInfo("xxxxx_mediation_version", getMediationVersion());
    Ogury.start(oguryConfigurationBuilder.build());

The `putMonitoringInfo` method takes a key-value parameters:

  * the key is `"xxxxx_mediation_version"` with `xxxxx` being the **name of the mediation** (in lower snack case) , e.g. Google AdMob will use the key "`google_admob_mediation_version"`.

  * the value is the **version of the mediation SDK** , e.g. `"8.13.0"`.

##

Step 4: Collect the user consent

As of November 13, 2023, both **Ogury Choice Manager** and the **End User
License Agreement (EULA) are deprecated**.

Consequently, the EULA will cease to be presented, and the Choice Manager will
no longer display consent notices. As a result, it is strongly advised to
discontinue the use of Ogury Choice Manager in any new versions of
applications. Developers are encouraged to explore alternative solutions in
light of this deprecation.

The European GDPR regulation requires obtaining the users' consent in order to
display them personalized ads, (i) when the company processing personal data
is based in the EU, or (ii) when the users are EU citizens.

As a company based in the EU, Ogury accordingly requires an explicit consent
from the users to collect their personal data and display them personalized
ads. The consent collection can be operated:

  * by the [Ogury Choice Manager](/android/ogury-choice-manager/collect-the-user-consent).

  * by a [Third-party consent manager](/android/ogury-choice-manager/third-party-consent-manager).

Note that the Ogury SDK meets privacy requirements by design. Shall it not
receive a valid consent status from the Ogury Choice Manager or from a third-
party consent solution, it will display an [End User License Agreement
(EULA)](/android/help/faq#q-what-is-an-end-user-license-agreement-eula) before
serving the first ad. Another way to put it: no targeted ad will be displayed
to the users if they didn't give their consent first.

##

Step 5: Apply children's privacy treatment

This section is specifically for apps that are declared as mixed audience apps
in the Ogury dashboard. Note that the children's privacy treatment is always
applied on family audiences apps and does not apply on mature audiences apps.

The Ogury SDK provides a method to indicate that the current user is a child
and therefore the [US Children's Online Privacy and Protection Act
(COPPA)](https://www.ftc.gov/tips-advice/business-center/privacy-and-
security/children's-privacy) and the EU [General Data Protection Regulation
(GDPR)](https://gdpr.eu/) should be applied.

Copy

    
    
    Ogury.applyChildPrivacy(OguryChildPrivacyTreatment.UNSPECIFIED);

The `applyChildPrivacy` method can be called at any time. It takes effect from
the next Ogury ad requests and until the user closes the app. It takes one of
the integers of the `OguryChildPrivacyTreatment` class as parameters:

  * `UNSPECIFIED`: Default value. It was not specified that the the current user should receive treatment for users under COPPA or under the age of GDPR consent.

  * `CHILD_UNDER_COPPA_TREATMENT_FALSE`: Specifies that the current user should not receive treatment for users under COPPA and the GDPR laws is not applicable (users out the European Economic Area).

  * `CHILD_UNDER_COPPA_TREATMENT_TRUE`: Specifies that the current user should receive treatment for users under COPPA.

  * `UNDER_AGE_OF GDPR_CONSENT_TREATMENT_FALSE`: Specifies that the user should not receive treatment for users under the age of GDPR consent and the COPPA is not applicable.

  * `UNDER_AGE_OF GDPR_CONSENT_TREATMENT_TRUE`: Specifies that the user should receive treatment for users under the age of GDPR consent.

Additionally, the Ogury SDK provide a method to apply an ad content filtering
on the Ogury ad requests:

Copy

    
    
    OguryAdRequests.setAdContentThreshold(OguryAdRequests.AD_CONTENT_THRESHOLD_G);

The `setAdContentThreshold` method can be called at any time. It takes effect
on all Ogury formats, from the next ad requests and until the user closes the
app. It takes one of the string of the `OguryAdRequests` class as parameters:

  * `AD_CONTENT_THRESHOLD_UNSPECIFIED`: No content threshold to apply.

  * `AD_CONTENT_THRESHOLD_G`: Requires content suitable for general audiences, including families.

  * `AD_CONTENT_THRESHOLD_PG`: Requires content suitable for most audiences with parental guidance.

  * `AD_CONTENT_THRESHOLD_T`: Requires content suitable for teen and older audiences.

  * `AD_CONTENT_THRESHOLD_MA`: Requires content suitable only for mature audiences.

##

Step 6: Integrate Ogury ad formats

Ogury provides four different ad formats, (i) Interstitial Ads, (ii) Opt-in
Video Ads, (iii) Banner Ads, and (iv) Thumbnail Ads. You can refer to the
following sections to proceed with the integration:

  * [Interstitial Ad](/android/ad-formats/interstitial-ad)

  * [Opt-in Video Ad](/android/ad-formats/opt-in-video-ad)

  * [Banner Ad](/android/ad-formats/banner-ad)

  * [Thumbnail Ad](/android/ad-formats/thumbnail-ad)

##

Before going live

Ogury is part of the IAB [Authorized Sellers for
Apps](https://iabtechlab.com/wp-content/uploads/2019/03/app-
ads.txt-v1.0-final-.pdf) initiative to fight inventory fraud for applications.
It is recommended to [update your `app-ads.txt`](https://ogury-
ltd.gitbook.io/help-center-for-publishers/set-up-ogury-global-demand/update-
your-app-ads.txt) to include Ogury.

Last updated 2 months ago

On this page

  * Step 1: Register your application
  * Step 2: Import the Ogury SDK
  * Step 3: Initialize the Ogury SDK
  * Step 4: Collect the user consent
  * Step 5: Apply children's privacy treatment
  * Step 6: Integrate Ogury ad formats
  * Before going live

Was this helpful?

