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

# Third-party consent manager

Ogury requires an explicit consent from the user to use their personal data.
In addition to our [Ogury Choice Manager](/android/ogury-choice-
manager/collect-the-user-consent), the Ogury SDK can collect the consent
**automatically** from third-party consent manager (see [case
A](/android/ogury-choice-manager/third-party-consent-manager#case-a-your-cmp-
generates-a-tcfv2-consent-string-and-is-compatible-with-the-iab-gdpr-consent-
framework) for more details). Additionally we provide APIs to transmit the
consent from third-party consent manager to the Ogury SDK in case it is not
compatible with the automatic way (see [case B](/android/ogury-choice-
manager/third-party-consent-manager#case-b-your-cmp-generates-a-tcfv2-consent-
string-and-is-not-leveraging-the-iab-gdpr-consent-framework) and [case
C](/android/ogury-choice-manager/third-party-consent-manager#case-c-your-cmp-
is-not-compatible-with-tcfv2) for more details).

##

Requirements

Your application must be registered on your Ogury dashboard and the SDK must
be started. If not, you can refer to the [Getting started](/android).

To use automatic TCFV2 string retrieval ([case A](/android/ogury-choice-
manager/third-party-consent-manager#case-a-your-cmp-generates-a-tcfv2-consent-
string-and-is-compatible-with-the-iab-gdpr-consent-framewo)), make sure you
have the SDK version 5.0.7 or latest.

##

Case A: Your CMP generates a TCFv2 consent string and is compatible with the
[IAB GDPR Consent
Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-
and-Consent-
Framework/blob/master/TCFv2/IAB%20Tech%20Lab%20-%20CMP%20API%20v2.md#in-app-
details)​

The Ogury SDK (from version 5.0.7) will automatically synchronize the user's
consent before each ad request.

The user's consent is read from the Shared preferences as specified in [IAB
GDPR Consent Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-
Transparency-and-Consent-
Framework/blob/master/TCFv2/IAB%20Tech%20Lab%20-%20CMP%20API%20v2.md#in-app-
details) and synchronized every time the user changes its choices. Your CMP
must be initialized before doing any ad request in order for the consent to be
retrieved.

**Compatible third-party consent managers** :

  * ​[Quantcast Choice](https://www.quantcast.com/products/choice-consent-management-platform/)​

  * ​[Didomi](https://www.didomi.io/)​

  * etc.

If you are using an Ogury SDK version prior to 5.0.7, you must update your
Ogury SDK or use the method in [case B](/android/ogury-choice-manager/third-
party-consent-manager#case-b-your-cmp-generates-a-tcfv2-consent-string-and-is-
not-leveraging-the-iab-gdpr-consent-framewor).

##

Case B: Your CMP generates a TCFv2 consent string and is NOT leveraging the
IAB GDPR Consent Framework

If your consent notice is registered in the [IAB CMP
list](https://cmplist.consensu.org/v2/cmp-list.json) and produces [IAB-
specified consent
string](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-
Consent-
Framework/blob/master/TCFv2/IAB%20Tech%20Lab%20-%20Consent%20string%20and%20vendor%20list%20formats%20v2.md),
but is not leveraging the [IAB GDPR Consent
Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-
and-Consent-
Framework/blob/master/TCFv2/IAB%20Tech%20Lab%20-%20CMP%20API%20v2.md#in-app-
details) you can pass the consent to Ogury SDK.

Call the following method once the consent has been collected after [having
initialized the Ogury SDK](/android#step-3-initialize-the-ogury-sdk):

Copy

    
    
    OguryChoiceManagerExternal.TcfV2.setConsent(iabString, new Integer[0]);

The `setConsent` method takes the following parameter:

  * the [IAB-specified Consent String](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework/blob/master/TCFv2/IAB%20Tech%20Lab%20-%20Consent%20string%20and%20vendor%20list%20formats%20v2.md) generated by third-party CMP to transmit the consent of the vendors that are registered inside the [IAB Global Vendor List](https://vendor-list.consensu.org/v2/vendor-list.json).

The [IAB-specified Consent
String](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-
Consent-
Framework/blob/master/TCFv2/IAB%20Tech%20Lab%20-%20Consent%20string%20and%20vendor%20list%20formats%20v2.md)
must be valid and be generated by a whitelisted CMP. Otherwise the call to the
`setConsent` method will be **ignored**.

If, at any point, user consent is changed, call this method again with updated
values.

###

Integration example

Copy

    
    
    public class MyActivity extends Activity {
    
        @Override protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            
            OguryConfiguration.Builder oguryConfigurationBuilder = new OguryConfiguration.Builder(this, "OGY-XXXXXXXXXXXX");
            Ogury.start(oguryConfigurationBuilder.build());
            
            YourCmp.getConsent(this, yourCmpConsentListener);
        }
        
        private final YourCmpConsentListener yourCmpConsentListener = new YourCmpConsentListener() {
            @Override public void onComplete(OguryChoiceManager.Answer answer) {
                // Transmit the user consent to Ogury
                OguryChoiceManagerExternal.TcfV2.setConsent(YourCmp.getIabString(), new Integer[0]);
                
                // and start GAM and other vendor SDKs    
            }
            @Override public void onError(OguryError error) {
                // handle error
                // and start GAM and other vendor SDKs
            }
        };
        
    }

##

Case C: Your CMP is not compatible with TCFv2

As of November 13, 2023, **this functionality is deprecated** , and Ogury no
longer provides support for this consent type. Please use a Consent Management
Platform (CMP) that is compatible with TCFv2 to manage and generate user
consents.

This feature is submitted to a whitelist. Please contact your account manager
before starting using this method.

We provide an alternative programmatic way to provide a `true`/`false` user's
consent to the Ogury SDK in case of any of the previous methods did not work.

Before using this method, to be compliant with last GDPR requirements, you
must include a link to [Ogury's Privacy Policy](https://ogury.com/privacy-
policy/) in your own privacy policy.

If you have not done it before, you must [initialize the Ogury
SDK](/android#step-3-initialize-the-ogury-sdk) before calling this method.

Copy

    
    
    OguryChoiceManagerExternal.setConsent(consentBoolean, consentManagerName);

The `setConsent` method take the following parameter:

  * a boolean indicating whether the user has consented or not.

  * the name of the consent manager provider collecting the consent. The value must formatted in snake case

    * If you are using a third-party solution, enter the name of this solution in SCREAMING_SNAKE_CASE (all capital letters, space replaced by an underscore).

    * If you are using an in-house solution, use `"CUSTOM"`.

If, at any point, user consent is changed, call this method again with updated
values.

###

Integration example

Copy

    
    
    OguryConfiguration.Builder oguryConfigurationBuilder = new OguryConfiguration.Builder(this, "OGY-XXXXXXXXXXXX");
    Ogury.start(oguryConfigurationBuilder.build());
    // [...]
    OguryChoiceManagerExternal.setConsent(consentBoolean, "CUSTOM");

##

Finish your integration

You can go back to the [Getting started](/android#step-4-collect-the-user-
consent) to implement ad formats and finish your integration.

Last updated 9 months ago

On this page

  * Requirements
  * Case A: Your CMP generates a TCFv2 consent string and is compatible with the IAB GDPR Consent Framework​
  * Case B: Your CMP generates a TCFv2 consent string and is NOT leveraging the IAB GDPR Consent Framework
  * Integration example
  * Case C: Your CMP is not compatible with TCFv2
  * Integration example
  * Finish your integration

Was this helpful?

