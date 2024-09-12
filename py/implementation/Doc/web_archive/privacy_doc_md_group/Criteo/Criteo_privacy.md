![](../../../app/img/criteo-logo.svg)

## App Developer Portal

  * [![](../../../app/images/apple.png)](../../../app/ios/get-started)
  * [![](../../../app/images/android.png)](../../../app/android/get-started)

NAV ![](../../../app/img/navbar.png)

  * ### [Get Started](../../../app/android/get-started)

  * [Testing](../../../app/android/testing)
  *  
  * ### App Bidding

  * [Overview](../../../app/android/app-bidding)
  * [Google Ad Manager](../../../app/android/app-bidding/google-ad-manager)
    * [Native Styles](../../../app/android/app-bidding/google-ad-manager/native-styles)
    * [Video](../../../app/android/app-bidding/google-ad-manager/video)
  * [MAX Applovin](../../../app/android/app-bidding/max)
  * [Other Ad Servers](../../../app/android/app-bidding/other-ad-servers)
  * [In-House Bidding](../../../app/android/app-bidding/inhouse)
    * [Advanced Native](../../../app/android/app-bidding/inhouse/advanced-native)
  * [Standalone](../../../app/android/standalone)
    * [Advanced Native](../../../app/android/standalone/advanced-native)
  *  
  * ### Mediation

  * [Admob](../../../app/android/mediation/admob)
  *  
  * ### Advanced

  * [Data Passing](../../../app/android/data-passing)
  * [Privacy Guidelines](../../../app/android/privacy)
  * [Release Notes](../../../app/android/release-notes)
  * [Migrating to v4.0](../../../app/android/migration/4.0)

# Privacy Guidelines

## General Data Protection Regulation (GDPR)

Under EU laws, app developers are required to collect user's consent to users
in European Economic Area (EEA) prior to serving any ads. Read more on
[Privacy Guidelines for Publishers](https://www.criteo.com/criteo-privacy-
guidelines-for-clients-and-publisher-partners/).

Criteo Publisher SDK uses [iAB GDPR Consent
Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-
and-Consent-Framework/blob/master/Mobile%20In-
App%20Consent%20APIs%20v1.0%20Final.md) in order to read user's consent. The
following keys are read by Criteo SDK and would need to be readily available
on `SharedPreferences` for applicable users:

  * TCF v1.1: `IABConsent_ConsentString` , `IABConsent_SubjectToGDPR`
  * TCF v2.0: `IABTCF_TCString`, `IABTCF_gdprApplies`

If you have a custom Consent Management Provider (CMP) to handle user's
consent, please make sure that your CMP conforms to iAB CMP framework.

## California Consumer Privacy Act (CCPA)

In order to help App developers ensure CCPA compliance, starting from version
3.3.0, Criteo Publisher SDK accepts two different methods to indicate user's
consent in the California state:

### iAB CCPA Compliance Framework

According to [iAB CCPA Compliance
Framework](https://www.iab.com/guidelines/ccpa-framework/), App developers
would need to ensure that the US privacy string with key `IABUSPrivacy_String`
is readily available on `SharedPreferences` for applicable users. Read more on
[this document](https://iabtechlab.com/wp-content/uploads/2019/11/US-Privacy-
USER-SIGNAL-API-SPEC-v1.0.pdf) under "In-app Support" section for more
information.

If you have a custom Consent Management Provider (CMP) to handle user's
consent, please make sure that your CMP conforms to iAB CCPA framework.

### CCPA Binary API

Alternatively, Criteo Publisher SDK provides a public API for app developers
who would prefer to pass explicit opt out value to Criteo.

This value must be passed to Criteo as soon as your app receives consent, or
otherwise, from applicable users. Criteo SDK v3.3.0 introduced a new Builder
class in order to initialize Criteo SDK that allows you to pass the opt out
value:

`usPrivacyOptOut` value | Description  
---|---  
`false` | User have not opted out  
`true` | User opted out  
      
    
    try {
        new Criteo.Builder(this, criteoPublisherId)
                .usPrivacyOptOut(false)
                .adUnits(adUnits)
                .debugLogsEnabled(true)
                .init();
    } catch (CriteoInitException e) {
    
    }
    
    
    
    try {
        Criteo.Builder(this, criteoPublisherId)
            .usPrivacyOptOut(false)
            .adUnits(adUnits)
            .debugLogsEnabled(true)
            .init()
    } catch (e: CriteoInitException) {
    
    }
    

In a case where user consent changes anytime after you initialize Criteo SDK,
your app must update Criteo SDK with `setUsPrivacyOptOut()` method:

    
    
    Criteo.getInstance().setUsPrivacyOptOut(false);
    
    
    
    Criteo.getInstance().setUsPrivacyOptOut(false)
    

## COPPA Compliance

The United States Federal Trade Commission has changed the compliance rules
for the Childrenâs Online Privacy Protection Act (âCOPPAâ), effective
July 1, 2013. The proposal effects websites, and associated services), that
have been identified as: (1) directed to users under 13 years of age; or (2)
collecting information from users actually known to be under 13 (collectively
âChildrenâs Sitesâ).

As of SDK v4.7.0, Criteo supports reading a COPPA boolean flag.

    
    
    Criteo.getInstance().setTagForChildDirectedTreatment(true);
    
    
    
    Criteo.getInstance().setTagForChildDirectedTreatment(true);
    

