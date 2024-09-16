SDK name: AppBrain SDK
Documentation:
____[ ![AppBrain Best Android Apps](https://www.appbrain.com/static/202408212147594/images/logo_48.png) AppBrain | Docs ](/ "AppBrain Best Android Apps")

__

  * [ Apps ](/apps/trending "Get the top trending Android Apps")
  * [ Statistics ](/stats "Android and Google Play Statistics")
  * [ Docs ](/info/help/index.html "Help Center")
  *   * [ Developers ](https://developers.appbrain.com/dev_dashboard "Access the AppBrain dashboard")
  * [ Get SDK ](https://github.com/swisscodemonkeys/appbrain-sdk/releases/latest "Download the AppBrain SDK")
  * [ Sign up ](https://www.appbrain.com/signup?li_cont=https%3A%2F%2Fwww.appbrain.com%2Finfo%2Fhelp%2Fsdk%2Fcoppa.html "Sign up")
  * [ Log in ](https://www.appbrain.com/login?li_cont=https%3A%2F%2Fwww.appbrain.com%2Finfo%2Fhelp%2Fsdk%2Fcoppa.html "Log in")

General

  * [Introduction](../index.html)
  * [Privacy policy](../privacy/index.html)
  * [About AppBrain](../about.html)
  * [HTML widgets](../html-widgets.html)
  * [Embeddable Android app widgets](../embeddable-app-widgets.html)

Publishers

  * [AppBrain SDK](index.html)
    * [Getting started](gettingstarted.html)
      * [SDK setup](setup.html)
      * [Manual setup](manualsetup.html)
      * COPPA compliance
    * [Ad unit overview](ad-units.html)
    * [Banners](banners.html)
    * [Interstitial](interstitial.html)
    * [ListView ads](listviews.html)
    * [Extra features](extra.html)
    * [Integration with other SDKs](othersdks.html)
    * [Integration policy](policy.html)
    * [Javadoc](javadoc/index.html)
  * [Resources](../publisher-resources/index.html)
  * [Terms of service](../publisher-tos.html)
  * [FAQ](../publisher-faq/index.html)

Advertisers

  * [Resources](../advertiser-resources/index.html)
  * [Terms of service](../advertiser-tos.html)
  * [FAQ](../advertiser-faq/index.html)

Intelligence

  * [Insights](../intelligence-resources/insights/index.html)
  * [Subscriptions](../intelligence-resources/subscriptions.html)
  * [SDK downloads](../intelligence-resources/sdk-downloads.html)
  * [Phone downloads](../intelligence-resources/phones-downloads.html)
  * [Terms of service](../intelligence-tos.html)

AppBrain API

  * [Using the AppBrain API](../api/appbrain-api.html)
  * [API specification](../api/specification.html)
  * [Pricing](../api/pricing.html)
  * [Promotion campaigns](../api/promotion-campaigns.html)
  * [Reporting](../api/reporting.html)
  * [AppLinks TOS](../app-links.html)

Search

# COPPA compliance

The Children’s Online Privacy Protection Rule (COPPA) requires that apps must
not collect any personal information from children under 13 without parental
consent. This also applies to included third party SDKs, such as the AppBrain
SDK. For more information on COPPA, and whether your app is affected by it,
please refer to the [COPPA FAQ](http://www.ftc.gov/tips-advice/business-
center/guidance/complying-coppa-frequently-asked-questions).

The AppBrain SDK provides a COPPA compliancy mode. If COPPA compliancy is
enabled, the AppBrain SDK removes any personal information from its requests.
Note that unique identifiers are still sent to our servers for the allowed
purposes of frequency capping and fraud analysis. All unique identifiers are
deleted within 10 days, are not used for behavioral targeting, and are never
passed on to third parties.

COPPA compliancy mode in the SDK can be enabled in one of the following ways:

## Android Manifest

You can indicate that your app is directed to children in your
`AndroidManifest.xml`. This enables COPPA compliancy for all SDK requests, and
is thus the preferred way to enable COPPA compliancy for child directed apps,
as they need to enforce the additional privacy constraints for all users,
regardless of their age.

Enable COPPA compliancy by adding the following line to your
AndroidManifest.xml **inside** the `<application>` tag:

    
    
    <meta-data
        android:name="appbrain.child_directed"
        android:value="true" />
    

## Programmatically enable COPPA compliance

You can programmatically enable child directed treatment if you know that a
certain installation or use of your app falls under the COPPA rule (e.g. if
you know that your app is installed on a child’s device), by calling
`AppBrain.getAds().tagForChildDirectedTreatment(true)`. Most likely you want
to call this in `Application.onCreate()`.

## Explicitly indicate the user’s age

By calling `AppBrain.getAds().setUserData()` you can explicitly inform the SDK
about your current user’s age. For users under 13 years, COPPA compliancy is
automatically enabled if either the SIM-card or the carrier-network is based
in the US. Note that this automatic detection might not be enough to make your
app COPPA compliant. We thus recommend to always explicitly enable COPPA
compliancy, as described above, when dealing with users that fall under the
COPPA rule.

**Relevant links**  
[COPPA FAQ](http://www.ftc.gov/tips-advice/business-center/guidance/complying-
coppa-frequently-asked-questions)

More apps

  * [Top Android apps being viewed](/browse/live)
  * [Kalyan Original Matka Play App](/app/kalyan-original-matka-play-app/com.kalyan.original.app)
  * [Viper Connect for Android](/app/viper-connect/com.directed.viperconnect)
  * [SalaryBox: Attendance, Payroll](/app/salarybox-attendance-payroll/in.product.salary)

Android Statistics

  * [Android statistics](/stats "See what's popular on Google Play, research your competitors, find technical statistics.")
  * [Google Play Developer stats](/stats/developers "Explore Android developer statistics")
  * [Trending Android Apps](/apps/trending)
  * [Top popular Apps](/apps/popular)

About AppBrain

  * [Contact](/info/about)
  * [Blog](https://medium.com/appbrain)
  * [Privacy](/info/help/privacy/index.html)
  * [Documentation](/info/help/index.html)
  * [Articles](/articles)
  * [How to improve the earnings of your ad units](/info/help/publisher-resources/improve-earnings-android-ad-units.html "Optimize the revenue that your ad units in your Android apps generate")

(C) 2010-2024 - AppBrain

