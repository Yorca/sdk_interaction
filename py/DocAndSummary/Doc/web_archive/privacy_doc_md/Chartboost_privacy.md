[ ![](/assets/images/svg/cb_logo_2023.svg) ](/en/)

  * [Monetization](/en/monetization/)
  * [Mediation](/en/mediation/)
  * [Advertising](/en/advertising/)
  * [Partners](/en/partners/)
  * [FAQs](/en/faq/)

  * [Log in](https://platform.chartboost.com/login)
  * [Contact Support](/en/support/contact-us/)

🇺🇸 English

    * [🇺🇲 English](/en/)
    * [🇨🇳 Chinese (中国)](/zh/)

  1. [Documentation](/en/)
  2. [Monetization](/en/monetization)
  3. Android SDK

Search

##### Monetization

  * [Get Started](/en/monetization/get-started/)
  * [How To Make Money](/en/monetization/how-to-make-money/)
  * [Managing Your Account](/en/monetization/managing-your-account/)
  * Payments

    * [Setup Payment](/en/monetization/payments/setup-payment/)
    * [Payment Terms & Dates](/en/monetization/payments/payment-terms-dates/)
    * [Adjusting Your Payout Threshold](/en/monetization/payments/adjusting-your-payout-threshold/)

  * [Using Your Dashboard](/en/monetization/using-your-dashboard/)
  * [Viewing Analytics](/en/monetization/viewing-analytics/)
  * [Test Mode](/en/monetization/test-mode/)
  * [Charles Web Proxy](/en/monetization/charles-web-proxy/)
  * Publishing
  * [Adding Your First App & Campaign](/en/monetization/publishing/adding-your-first-app-and-campaign/)
  * [Publisher App Review](/en/monetization/publishing/publisher-app-review/)
  * [Ad Locations](/en/monetization/publishing/ad-locations/)
  * [List Management](/en/monetization/publishing/list-management/)
  * [Monetization Settings](/en/monetization/publishing/monetization-settings/)
  * [App Privacy Settings](/en/monetization/publishing/app-privacy-settings/)
  * [app-ads.txt](/en/monetization/publishing/app-ads-txt/)
  * [Optimization Tips & Best Practices](/en/monetization/publishing/optimization-tips-and-best-practices/)
  * Mediation
  * [Partner Overview](/en/monetization/mediation/mediation-partner-overview/)
  * [Tips & Best Practices](/en/monetization/mediation/mediation-tips-and-best-practices/)
  * Partners

    * [AdMob](/en/monetization/mediation/admob/)
    * [Chartboost](/en/monetization/mediation/chartboost/)
    * [DT FairBid](/en/monetization/mediation/dt-fairbid/)
    * [MAX](/en/monetization/mediation/max/)
    * [Unity LevelPlay](/en/monetization/mediation/unity-levelplay/)

  * SDK Integration
  * Android SDK

    * [Get Started](/en/monetization/integrate/android/get-started/)
    * [Banners](/en/monetization/integrate/android/banners/)
    * [Delegate Methods](/en/monetization/integrate/android/delegate-methods/)
    * [Named Locations](/en/monetization/integrate/android/named-locations/)
    * [SDK Privacy Methods](/en/monetization/integrate/android/sdk-privacy-methods/)
    * [Chartboost Videos](/en/monetization/integrate/android/chartboost-videos/)
    * [Error Codes](/en/monetization/integrate/android/error-codes/)
    * [Data Safety Details](/en/monetization/integrate/android/data-safety-details/)
    * [Changelog](/en/monetization/integrate/android/changelog/)
    * [SDK Deprecation Policy](/en/monetization/integrate/android/sdk-deprecation-policy/)

  * iOS SDK

    * [Get Started](/en/monetization/integrate/ios/get-started/)
    * [Banners](/en/monetization/integrate/ios/banners/)
    * [Delegate Methods](/en/monetization/integrate/ios/delegate-methods/)
    * [Named Locations](/en/monetization/integrate/ios/named-locations/)
    * [Upgrading the SDK for iOS 14+](/en/monetization/integrate/ios/upgrading-the-sdk/)
    * [SDK Privacy Methods](/en/monetization/integrate/ios/sdk-privacy-methods/)
    * [Chartboost Videos](/en/monetization/integrate/ios/chartboost-videos/)
    * [Error Codes](/en/monetization/integrate/ios/error-codes/)
    * [Privacy Manifest](/en/monetization/integrate/ios/privacy-manifest/)
    * [Changelog](/en/monetization/integrate/ios/changelog/)
    * [SDK Deprecation Policy](/en/monetization/integrate/ios/sdk-deprecation-policy/)

  * API Reference
  * [API Access & Overview](/en/monetization/reference/api-access-authentication/)
  * [App Management API](/en/monetization/reference/app-management-api/)
  * [Ad Locations API](/en/monetization/reference/ad-locations-api/)
  * [Analytics API](/en/monetization/reference/analytics-api/)
  * [List Management API](/en/monetization/reference/list-management-api/)
  * [↗ iOS SDK API Reference](https://reference.chartboost.com/monetization/ios/)

# Search Chartboost Docs

[ Search by ](https://www.algolia.com/ref/docsearch/)

# SDK Privacy Methods

Chartboost requires publishers to obtain consent from their users in order to
process personal data and provide relevant ads. Apps under the **Google Play
Designed for Families** policy **MUST** set the COPPA privacy flag to `true`.
Review our [COPPA FAQs](/en/faq/coppa/) for more information on behavior
targeting.

The `addDataUseConsent` is the new public API usage to set consent values.
This new API provides user consent data for privacy laws currently in
existence or future laws. Replaces `CBPIDataUseConsent` method.

##  GDPR 🔗

  * Kotlin 
  * Java 

  *     /** 
    * GDPR support settings: 
    * NON_BEHAVIORAL(0) means the user does not consent to targeting (Contextual ads) 
    * BEHAVIORAL(1) means the user consents (Behavioral and Contextual Ads) 
    */ 
    val dataUseConsent = GDPR(GDPR.GDPR_CONSENT.BEHAVIORAL)
    Chartboost.addDataUseConsent(context, dataUseConsent)
    

  *     /**
    * GDPR support settings:
    * NON_BEHAVIORAL(0) means the user does not consent to targeting (Contextual ads)
    * BEHAVIORAL(1) means the user consents (Behavioral and Contextual Ads)
    */
    DataUseConsent dataUseConsent = new GDPR(GDPR.GDPR_CONSENT.BEHAVIORAL);
    Chartboost.addDataUseConsent(context, dataUseConsent);
    

##  CCPA 🔗

  * Kotlin 
  * Java 

  *     /** 
    * CCPA support settings: 
    * OPT_IN_SALE(1YN-) means the user consents (Behavioral and Contextual Ads) 
    * OPT_OUT_SALE(1NY-) means the user does not consent to targeting (Contextual ads) 
    */ 
    val dataUseConsent = CCPA(CCPA.CCPA_CONSENT.OPT_IN_SALE) Chartboost.addDataUseConsent(context, dataUseConsent)
    

  *     /**
    * CCPA support settings:
    * OPT_IN_SALE(1YN-) means the user consents (Behavioral and Contextual Ads)
    * OPT_OUT_SALE(1NY-) means the user does not consent to targeting (Contextual ads)
    */
    DataUseConsent dataUseConsent = new CCPA(CCPA.CCPA_CONSENT.OPT_IN_SALE);
    Chartboost.addDataUseConsent(context, dataUseConsent);
    
    

##  COPPA 🔗

If an app is child-directed, a value of true or false must be set to define
proper behavior.

  * Kotlin 
  * Java 

  *     /** 
    * COPPA: 
    * true means that COPPA restrictions apply and the android advertising identifier is not transmitted. (Contextual ads) 
    * false means that COPPA restrictions do not apply. (Behavioral and Contextual Ads) 
    */ 
    val dataUseConsent = COPPA(true) Chartboost.addDataUseConsent(context, dataUseConsent)
    

  *     /**
    * COPPA:
    * true means that COPPA restrictions apply and the android advertising identifier is not transmitted. (Contextual ads)
    * false means that COPPA restrictions do not apply. (Behavioral and Contextual Ads)
    */
    DataUseConsent dataUseConsent = new COPPA(true);
    Chartboost.addDataUseConsent(context, dataUseConsent);
    

Apps under the **Google Play Designed for Families** policy **MUST** set the
COPPA privacy flag to `true` in order to restrict transmitting the android
advertising identifier.

##  Custom Consent 🔗

Chartboost allows publishers to provide custom consent information, besides
the predefined GDPR and CCPA values. Currently, the only custom consent values
allowed are valid [IAB’s U.S. Privacy
String](https://iabtechlab.com/standards/ccpa/) for the CCPA standard.

For example:

  * Kotlin 
  * Java 

  *     val dataUseConsent = Custom("name", "value")
    Chartboost.addDataUseConsent(context, dataUseConsent)
    

  *     DataUseConsent dataUseConsent = new Custom("name", "value");
    Chartboost.addDataUseConsent(context, dataUseConsent);
    

##  Clear Data Use Consent 🔗

To clear any of the privacy data use consent, use the following method:

  * Kotlin 
  * Java 

  *     Chartboost.clearDataUseConsent(context, dataUseConsent.privacyStandard)
    

  *     Chartboost.clearDataUseConsent(context, dataUseConsent.getPrivacyStandard());
    

  * GDPR
  * CCPA
  * COPPA
  * Custom Consent
  * Clear Data Use Consent

  * (C) 2024 Chartboost, Inc. 
  * [Chartboost.com](https://chartboost.com)
  * [Legal](/en/legal/)
  * Cookie Settings

