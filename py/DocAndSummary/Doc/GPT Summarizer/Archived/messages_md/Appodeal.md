SDK name: Appodeal
Documentation:
Skip to main content

[![Appodeal logo](/img/logo.svg)![Appodeal logo](/img/logo.svg)**Help
Center**](/)

SDK Guides

  * [Android SDK](/android/get-started)
  * [iOS SDK](/ios/get-started)
  * [Unity Plugin](/unity/get-started)

* * *

  * [React-Native Plugin](https://github.com/appodeal/react-native-appodeal)
  * [Flutter Plugin](https://github.com/appodeal/Appodeal-Flutter-Plugin)

* * *

  * [SDK Deprecation Policy](/advanced/sdk-deprecation-policy)

General

  * [Network Setup](/networks-setup/introduction)
  * [FAQ & Troubleshooting](/faq-and-troubleshooting/faq/generate-the-json-file-in-google-cloud)
  * [Reporting](/reporting/reporting-api)
  * [Advanced](/advanced/ad-revenue-attribution)
  * [Accelerator Soft Launch](/accelerator/introduction)

[DashboardArrow Forward](https://app.appodeal.com/analytics/overview)

Search

English

  * [English](/android/data-protection/coppa)
  * [Русский](/ru/android/data-protection/coppa)

[Sign in](https://app.appodeal.com/signin)

#### Android SDK

[3.3.2](/android/get-started)

  * [3.3.2](/android/data-protection/coppa)
  * Archived versions
  * [3.2.1](https://0e7e302e.appodeal-sdk-docs-prod.pages.dev/android/get-started)
  * [3.1.3](https://c3798d39.appodeal-sdk-docs-prod.pages.dev/android/3.1.3/get-started)

  * [Get Started](/android/get-started)
  * [Ad Types](/android/ad-types/interstitial)

    * [Interstitial](/android/ad-types/interstitial)
    * [Rewarded Video](/android/ad-types/rewarded-video)
    * [Banner](/android/ad-types/banner)
    * [MREC](/android/ad-types/mrec)
    * [Native](/android/ad-types/native)
  * [Services](/android/services/adjust)

    * [Adjust](/android/services/adjust)
    * [AppsFlyer](/android/services/appsflyer)
    * [Firebase](/android/services/firebase)
    * [Meta](/android/services/meta)
  * [Data Protection](/android/data-protection/gdpr-and-ccpa)

    * [GDPR and CCPA](/android/data-protection/gdpr-and-ccpa)
    * [App Privacy Details on the Google Play](/android/data-protection/app-privacy-details)
    * [COPPA](/android/data-protection/coppa)
  * [Advanced](/android/advanced/configure-mediated-networks)

    * [Configure Mediated Networks](/android/advanced/configure-mediated-networks)
    * [Segments and Placements](/android/advanced/segments-placements)
    * [User Data](/android/advanced/user-data)
    * [Testing](/android/advanced/testing)
    * [Ad Revenue Callbacks](/android/advanced/ad-revenue-callback)
    * [Ad Revenue Forwarding to MMP/BI](/android/advanced/ad-revenue-forwarding)
    * [Event Tracking](/android/advanced/event-tracking)
    * [In-App purchases](/android/advanced/in-app-purchases)
    * [Launching a tROAS campaign in Google Ads](/android/advanced/launching-troas)
  * [Changelog](/android/changelog)
  * [Upgrade guide](/android/upgrade-guide)
  * [SDK Deprecation Policy](/android/sdk-deprecation-policy)

  * [](/)
  * Data Protection
  * COPPA

Version: 3.3.2

# COPPA

For purposes of the [Children's Online Privacy Protection Act
(COPPA)](https://business.ftc.gov/privacy-and-security/children%27s-privacy)
there is a setting called childDirectedTreatment. If your app is designed for
kids you can disable sending user data to ad networks by calling the method
below.

Should be called before the SDK initialization.

  * Kotlin
  * Java

    
    
    Appodeal.setChildDirectedTreatment(value: Boolean?)  
    
    
    
    Appodeal.setChildDirectedTreatment(@Nullable Boolean value);  
    

info

Call `setChildDirectedTreatment` with `true` to indicate that you want your
content treated as child-directed for purposes of COPPA.

Call `setChildDirectedTreatment` with `false` to indicate that you don't want
your content treated as child-directed for purposes of COPPA.

Call `setChildDirectedTreatment` with `null` to indicate that you want to use
the COPPA parameter from your application's settings on the
[appodeal.com](http://appodeal.com/).

* * *

[PreviousApp Privacy Details on the Google Play](/android/data-protection/app-
privacy-details)[NextConfigure Mediated Networks](/android/advanced/configure-
mediated-networks)

![Appodeal logo](/img/logo.svg)![Appodeal logo](/img/logo.svg)

Copyright © 2023 Appodeal, Inc.

  * [Terms of service](https://www.appodeal.com/home/terms-of-service/)
  * [Privacy Policy](https://appodeal.com/privacy-policy)
  * [SDK License Agreement](https://appodeal.com/sdk-license-agreement)

Skip to main content

[![Appodeal logo](/img/logo.svg)![Appodeal logo](/img/logo.svg)**Help
Center**](/)

SDK Guides

  * [Android SDK](/android/get-started)
  * [iOS SDK](/ios/get-started)
  * [Unity Plugin](/unity/get-started)

* * *

  * [React-Native Plugin](https://github.com/appodeal/react-native-appodeal)
  * [Flutter Plugin](https://github.com/appodeal/Appodeal-Flutter-Plugin)

* * *

  * [SDK Deprecation Policy](/advanced/sdk-deprecation-policy)

General

  * [Network Setup](/networks-setup/introduction)
  * [FAQ & Troubleshooting](/faq-and-troubleshooting/faq/generate-the-json-file-in-google-cloud)
  * [Reporting](/reporting/reporting-api)
  * [Advanced](/advanced/ad-revenue-attribution)
  * [Accelerator Soft Launch](/accelerator/introduction)

[DashboardArrow Forward](https://app.appodeal.com/analytics/overview)

Search

English

  * [English](/android/data-protection/gdpr-and-ccpa)
  * [Русский](/ru/android/data-protection/gdpr-and-ccpa)

[Sign in](https://app.appodeal.com/signin)

#### Android SDK

[3.3.2](/android/get-started)

  * [3.3.2](/android/data-protection/gdpr-and-ccpa)
  * Archived versions
  * [3.2.1](https://0e7e302e.appodeal-sdk-docs-prod.pages.dev/android/get-started)
  * [3.1.3](https://c3798d39.appodeal-sdk-docs-prod.pages.dev/android/3.1.3/get-started)

  * [Get Started](/android/get-started)
  * [Ad Types](/android/ad-types/interstitial)

    * [Interstitial](/android/ad-types/interstitial)
    * [Rewarded Video](/android/ad-types/rewarded-video)
    * [Banner](/android/ad-types/banner)
    * [MREC](/android/ad-types/mrec)
    * [Native](/android/ad-types/native)
  * [Services](/android/services/adjust)

    * [Adjust](/android/services/adjust)
    * [AppsFlyer](/android/services/appsflyer)
    * [Firebase](/android/services/firebase)
    * [Meta](/android/services/meta)
  * [Data Protection](/android/data-protection/gdpr-and-ccpa)

    * [GDPR and CCPA](/android/data-protection/gdpr-and-ccpa)
    * [App Privacy Details on the Google Play](/android/data-protection/app-privacy-details)
    * [COPPA](/android/data-protection/coppa)
  * [Advanced](/android/advanced/configure-mediated-networks)

    * [Configure Mediated Networks](/android/advanced/configure-mediated-networks)
    * [Segments and Placements](/android/advanced/segments-placements)
    * [User Data](/android/advanced/user-data)
    * [Testing](/android/advanced/testing)
    * [Ad Revenue Callbacks](/android/advanced/ad-revenue-callback)
    * [Ad Revenue Forwarding to MMP/BI](/android/advanced/ad-revenue-forwarding)
    * [Event Tracking](/android/advanced/event-tracking)
    * [In-App purchases](/android/advanced/in-app-purchases)
    * [Launching a tROAS campaign in Google Ads](/android/advanced/launching-troas)
  * [Changelog](/android/changelog)
  * [Upgrade guide](/android/upgrade-guide)
  * [SDK Deprecation Policy](/android/sdk-deprecation-policy)

  * [](/)
  * Data Protection
  * GDPR and CCPA

Version: 3.3.2

On this page

# GDPR and CCPA

info

Keep in mind that it’s best to contact qualified legal professionals, if you
haven’t done so already, to get more information and be well-prepared for
compliance.

[The General Data Protection Regulation](https://gdpr-info.eu/), better known
as GDPR, took effect on May 25, 2018. It's a set of rules designed to give EU
citizens more control over their personal data. Any _businesses established in
the EU or with users based in Europe are required to comply with GDPR or risk
facing heavy fines_. The California Consumer Privacy Act (CCPA) went into
effect on January 1, 2020. **We have put together some guidelines to help
publishers understand better the steps they need to take to be GDPR
compliant.**

You can learn more about GDPR and CCPA and their differences
[here](https://iapp.org/resources/article/ccpa-and-gdpr-comparison-chart/).

* * *

## Step 1. Update Privacy Policy​

### Include Additional Information To Your Privacy Policy​

Don’t forget to add information about IP address and advertising ID
collection, as well as [the link to Appodeal’s privacy
policy](https://www.appodeal.com/privacy-policy) to your app’s privacy policy
on the App Store.

To speed up the process, you could use [privacy policy
generators](https://app-privacy-policy-generator.firebaseapp.com/) \- just
insert advertising ID, IP address, and location (if you collect users’
location) in the **Personally Identifiable Information you collect** field (in
line with other information about your app) and [the link to Appodeal’s
privacy policy](https://www.appodeal.com/privacy-policy) in the **Link to the
privacy policy of third party service providers used by the app** field.

### Add A Privacy Policy To Your Mobile App​

You must add your explicit privacy policies in two places: on your app’s Store
Listing page and within your app.

You can find detailed instructions on adding your privacy policy to your app
on legal service websites. For example, Iubenda, the solution tailored to
legal compliance, provides [a comprehensive
guide](https://www.iubenda.com/en/help/401-privacy-policy-for-ios-and-macos-
apps) on including a privacy policy in your app.

Make sure that your privacy policy website has an SSL certificate—this point
might seem obvious, but it’s still essential.

Here are two useful resources that you can utilize while working on your app
compliance:

  * [Privacy, Security and Deception regulations (by Google Play)](https://play.google.com/intl/en-GB_ALL/about/privacy-security-deception/user-data)
  * [Recommendations on Developing a Meaningful Privacy Policy (by Attorney General California Department of Justice)](https://oag.ca.gov/sites/all/files/agweb/pdfs/cybersecurity/making_your_privacy_practices_public.pdf)

note

Please note that although we’re always eager to back you up with valuable
information, we’re not authorized to provide any legal advice. It’s important
to address your questions to lawyers who specialize in this area.

* * *

## Step 2. Configure Stack Consent Manager with TCF v2 Support​

info

Since `Appodeal SDK 3.2.1` it is fully compatible with Google UMP and supports
IAB TCF v2.

In order for Appodeal and our ad providers to deliver ads that are more
relevant to your users, as a mobile app publisher, you need to collect
explicit user consent in the regions covered by GDPR.

To get consent for collecting personal data of your users, we suggest you use
a ready-made solution - Stack Consent Manager based on **Google User Messaging
Platform (UMP)**.

Configure Google UMP

Before you start, you need to configure Google UMP. Follow [this
instruction](/advanced/google-cmp-and-tcfv2-support) to setup a consent form.

## Step 3. Integrate Stack Consent Manager​

Stack Consent Manager comes with a pre-made consent window that you can easily
present to your users. That means you no longer need to create your own
consent window.

Starting from Appodeal SDK 3.0, Stack Consent Manager is included by default.

**Consent will be requested automatically on SDK initialization** , and
consent form will be shown if it is necessary without any additional calls.

Please keep in mind that Consent will be shown only in the **EU** region, you
can use VPN for testing.

This means that Appodeal SDK integration code remains the same:

  * Kotlin
  * Java

    
    
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        Appodeal.initialize(activity, appKey, adTypes, object : ApdInitializationCallback {  
            override fun onInitializationFinished(list: List<ApdInitializationError>?) {  
                //Appodeal initialization finished  
            }  
        })  
    }  
    
    
    
    @Override  
    protected void onCreate(Bundle savedInstanceState) {  
        super.onCreate(savedInstanceState);  
        Appodeal.initialize(activity, appKey, adTypes, new ApdInitializationCallback() {  
            @Override public void onInitializationFinished(List<? extends ApdInitializationError> list) {  
                //Appodeal initialization finished  
            }  
        });  
    }  
    

## Advanced​

Stack Consent Manager is included in Appodeal SDK by default. **Consent will
be requested automatically on SDK initialization** , and consent form will be
shown if it is necessary without any additional calls.

You can still use your own Consent Manager or customize ours by following the
steps below.

If you wish, you can manage and update consent manually using Stack Consent
Manager calls.

### Update Consent Status​

To update the consent, call the method:

  * Kotlin
  * Java

    
    
    override fun onCreate(savedInstanceState: Bundle?) {  
        ConsentManager.requestConsentInfoUpdate(  
            parameters = ConsentUpdateRequestParameters(  
                activity = YourActivity@ this,  
                key = YOUR_APP_KEY,  
                tagForUnderAgeOfConsent = false,  
                sdk = "Appodeal",  
                sdkVersion = Appodeal.getVersion()  
            ),  
            callback = object : ConsentInfoUpdateCallback {  
                override fun onUpdated() {  
                    // User's consent status successfully updated.  
                }  
                  
                override fun onFailed(error: ConsentManagerError) {  
                    // Initialize the Appodeal SDK with default params.  
                }  
            }  
        )  
    }  
    
    
    
    @Override  
    protected void onCreate(Bundle savedInstanceState) {  
            ConsentManager.requestConsentInfoUpdate(  
                new ConsentUpdateRequestParameters(  
                    YourActivity.this,  
                    YOUR_APP_KEY,  
                    false,  
                    "Appodeal",  
                    Appodeal.getVersion()),  
                new ConsentInfoUpdateCallback() {  
                    @Override  
                    public void onUpdated() {  
                        // User's consent status successfully updated.  
                    }  
                      
                    @Override  
                    public void onFailed(ConsentManagerError error) {  
                        // Initialize the Appodeal SDK with default params.  
                    }  
                      
                     
                }  
            );  
    }  
    

tip

`requestConsentInfoUpdate` can be requested at any moment of the application
lifecycle. We recommend call request it at the application launch. Multiple
request calls are allowed.

note

Required parameters: `YOUR_APP_KEY` \- Appodeal app key, you can get it [in
your personal account](https://app.appodeal.com/apps);

`ConsentUpdateRequestParameters` \- Data class representing the parameters for
a consent update request in the Appodeal Consent Manager. Use this class to
encapsulate the necessary information for updating consent preferences.
Params:

  * `activity` \- Activity The activity in which the consent update is requested.
  * `key` \- The key associated with the user for whom the consent is being updated.
  * `tagForUnderAgeOfConsent` \- Optional. Indicates whether the user is tagged for under the age of consent. Set to true if the user is under the age of consent, otherwise set to false or null.
  * `sdk` \- Optional. The identifier for the SDK making the consent update request.
  * `sdkVersion` \- Optional. The version of the SDK making the consent update request.

`ConsentInfoUpdateCallback` \- listener for result request.

### Current consent status​

After consent info was updated you may check the current consent status:

  * Kotlin
  * Java

    
    
    val status: ConsentStatus = ConsentManager.status  
    
    
    
    ConsentStatus status = ConsentManager.getStatus  
    

info

Enum class representing the possible consent statuses in the Appodeal Consent
Manager.

  * `Unknown` \- Represents an unknown consent status;
  * `Required` \- Represents a required consent status;
  * `NotRequired` \- Represents a not required consent status;
  * `Obtained` \- Represents an obtained consent status.

### Can show personalized ads​

You may check whether personalized ads can be shown based on the current
consent status using:

  * Kotlin
  * Java

    
    
    ConsentManager.canShowAds()  
    
    
    
    ConsentManager.canShowAds();  
    

note

Returns `true` if personalized ads can be shown, `false` otherwise.

### Load Consent Form​

You may load and receive `ConsentForm` using following code:

  * Kotlin
  * Java

    
    
    ConsentManager.load(  
        context = YourActivity@this,  
        successListener = object : OnConsentFormLoadSuccessListener {  
            override fun onConsentFormLoadSuccess(consentForm: ConsentForm) {  
             // Consent form was loaded. Now you can display consent form as dialog  
            }  
        },  
        failureListener = object : OnConsentFormLoadFailureListener {  
            override fun onConsentFormLoadFailure(error: ConsentManagerError) {  
             // Consent form loading or showing failed. More info can be found in 'error' object  
             // Initialize the Appodeal SDK with default params.  
            }  
        }  
    )  
    
    
    
    ConsentManager.load(  
            YourActivity.this,  
            new OnConsentFormLoadSuccessListener() {  
                @Override  
                public void onConsentFormLoadSuccess(ConsentForm consentForm) {  
                    // Consent form was loaded. Now you can display consent form as dialog  
                }  
            },  
            new OnConsentFormLoadFailureListener() {  
                @Override  
                public void onConsentFormLoadFailure(ConsentManagerError error) {  
                    // Consent form loading or showing failed. More info can be found in 'error' object  
                    // Initialize the Appodeal SDK with default params.  
                }  
            }  
    );  
      
    

### Show consent form​

After the consent window Is ready you can show it.

  * Kotlin
  * Java

    
    
      
    consentForm.show(  
        activity = InterstitialActivity@this,  
        listener = object : OnConsentFormDismissedListener {  
            override fun onConsentFormDismissed(error: ConsentManagerError?) {  
                // Consent form loading or showing failed, or it does not required.   
                // More info can be found in 'error' object  
            }  
        }  
    )  
      
    
    
    
    consentForm.show(  
            InterstitialActivity.this,   
            new OnConsentFormDismissedListener() {  
                    @Override  
                public void onConsentFormDismissed(ConsentManagerError error) {  
                   // Consent form loading or showing failed, or it does not required.   
                   // More info can be found in 'error' object  
                }  
            }  
    );  
    

### Load and show if required​

You may also load the form and immediately show it if required

  * Kotlin
  * Java

    
    
    ConsentManager.loadAndShowConsentFormIfRequired(  
        activity = YourActivity@this,  
        dismissedListener = object : OnConsentFormDismissedListener {  
            override fun onConsentFormDismissed(error: ConsentManagerError?) {  
             // Consent form loading or showing failed, or it does not required. More info can be found in 'error' object  
            }  
        }  
    )  
    
    
    
    ConsentManager.loadAndShowConsentFormIfRequired(  
            YourActivity.this,  
            new OnConsentFormDismissedListener() {  
                    @Override  
                public void onConsentFormDismissed(ConsentManagerError error) {  
                    // Consent form loading or showing failed, or it does not required. More info can be found in 'error' object  
                }  
            }  
    );  
    

### Revokes consent​

You may reset the consent status to `unknown`, using method:

  * Kotlin
  * Java

    
    
    ConsentManager.revoke(context = YourActivity@this)  
    
    
    
    ConsentManager.revoke(YourActivity.this)  
    

info

Params: `context` \- The context in which consent is revoked.

[PreviousMeta](/android/services/meta)[NextApp Privacy Details on the Google
Play](/android/data-protection/app-privacy-details)

  * Step 1. Update Privacy Policy
    * Include Additional Information To Your Privacy Policy
    * Add A Privacy Policy To Your Mobile App
  * Step 2. Configure Stack Consent Manager with TCF v2 Support
  * Step 3. Integrate Stack Consent Manager
  * Advanced
    * Update Consent Status
    * Current consent status
    * Can show personalized ads
    * Load Consent Form
    * Show consent form
    * Load and show if required
    * Revokes consent

![Appodeal logo](/img/logo.svg)![Appodeal logo](/img/logo.svg)

Copyright © 2023 Appodeal, Inc.

  * [Terms of service](https://www.appodeal.com/home/terms-of-service/)
  * [Privacy Policy](https://appodeal.com/privacy-policy)
  * [SDK License Agreement](https://appodeal.com/sdk-license-agreement)

