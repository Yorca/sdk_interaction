[![](https://documentation.hyprmx.com/~gitbook/image?url=https%3A%2F%2F4081935952-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
x-
prod.appspot.com%2Fo%2Fspaces%252F-MboAEhW7FGFK_brych0%252Ficon%252Fe66eLcEOp77OOnhkTbI3%252Fhypr_logo.jpeg%3Falt%3Dmedia%26token%3Dc88b9ed0-f2b8-4bc2-ae0b-457e5d68d244&width=32&dpr=4&quality=100&sign=72b95a08&sv=1)![](https://documentation.hyprmx.com/~gitbook/image?url=https%3A%2F%2F4081935952-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
x-
prod.appspot.com%2Fo%2Fspaces%252F-MboAEhW7FGFK_brych0%252Ficon%252Fe66eLcEOp77OOnhkTbI3%252Fhypr_logo.jpeg%3Falt%3Dmedia%26token%3Dc88b9ed0-f2b8-4bc2-ae0b-457e5d68d244&width=32&dpr=4&quality=100&sign=72b95a08&sv=1)Android
/ Amazon HyprMX SDK](/android-sdk)

[ SDK Documentation](https://documentation.hyprmx.com/sdk/)

More

[SDK Documentation](https://documentation.hyprmx.com/sdk/)

SearchCtrl \+ K

  * Getting Started

    * [Android / Amazon Setup Guide](/android-sdk)

    * [Privacy](/android-sdk/getting-started/privacy)

    * [Google's Data Safety Questionnaire](/android-sdk/getting-started/googles-data-safety-questionnaire)

    * [Migrate to Version 6.4+](/android-sdk/getting-started/migrate-to-version-6.4+)

  * Ad Formats

    * [Rewarded Ads](/android-sdk/ad-formats/rewarded-ads)

    * [Interstitial Ads](/android-sdk/ad-formats/interstitial-ads)

    * [Banner/MREC Ads](/android-sdk/ad-formats/banner-ads)

  * 3rd Party Mediation

    * [3rd Party Mediation](/android-sdk/3rd-party-mediation/3rd-party-mediation)

      * [AdMob Mediation](/android-sdk/3rd-party-mediation/3rd-party-mediation/hyprmx-mobile-sdk-admob-adapter-overview)

      * [AppLovin MAX](/android-sdk/3rd-party-mediation/3rd-party-mediation/applovin-max)

      * [Chartboost Mediation](/android-sdk/3rd-party-mediation/3rd-party-mediation/chartboost-mediation)

      * [Digital Turbine FairBid](/android-sdk/3rd-party-mediation/3rd-party-mediation/digital-turbine-fairbid)

      * [Unity LevelPlay](/android-sdk/3rd-party-mediation/3rd-party-mediation/unity-levelplay)

      * [X3M XMediator](/android-sdk/3rd-party-mediation/3rd-party-mediation/x3m-xmediator)

  * Downloads/Change Log

    * [Downloads](/android-sdk/downloads-change-log/downloads)

    * [Change Log](/android-sdk/downloads-change-log/change-log)

      * [Android SDK Change Log](/android-sdk/downloads-change-log/change-log/android-sdk-change-log)

      * [Android AdMob Adapter Change Log](/android-sdk/downloads-change-log/change-log/android-admob-adapter-change-log)

[Powered by
GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=-MboAEhW7FGFK_brych0)

# Privacy

Publishers are responsible for maintaining compliance with applicable privacy
laws and regulations. The HyprMX SDK provides a number of flags publishers can
use to pass the appropriate value to HyprMX to protect and maintain user's
data and privacy.

These flags support compliance with the General Data Protection Regulation
(GDPR), US privacy laws (CPRA, CPA, VCDPA, etc.), Children's Online Privacy
Protection Act (COPPA), and other regional privacy laws. However, consent and
privacy requirements may extend beyond these circumstances and should be
applied accordingly.

##

**Consent Flag**

HyprMX provides an API with a consentStatus parameter with the below values
for jurisdictions that require passing consent that takes a `ConsentStatus`
value depending on the user consent collected by your app. This flag will be
used to indicate a user’s opt-in or opt-out consent for the collection and use
of personal data under applicable laws and jurisdictions (GDPR, CPRA, etc.).

If a user provided consent in jurisdictions that require opt-in consent or did
not opt out of collection or usage of personal data in jurisdictions that
require opt-out consent, set a user’s consent status as below in the setter:

JavaKotlin

Copy

    
    
    HyprMX.INSTANCE.setConsentStatus(ConsentStatus.CONSENT_GIVEN); // If user provided consent, set this to CONSENT_GIVEN

Copy

    
    
    HyprMX.setConsentStatus(ConsentStatus.CONSENT_GIVEN) // If user provided consent, set this to CONSENT_GIVEN

If a user did not provide consent in jurisdictions that require opt-in consent
or opted out of collection or usage of personal data in jurisdictions that
require opt-out consent, set a user’s consent status as below in the setter:

JavaKotlin

Copy

    
    
    HyprMX.INSTANCE.setConsentStatus(ConsentStatus.CONSENT_DECLINED); // If user declined consent, set this to CONSENT_DECLINED

Copy

    
    
    HyprMX.setConsentStatus(ConsentStatus.CONSENT_DECLINED) // If user declined consent, set this to CONSENT_DECLINED

If you do not know the user’s consent status set it as unknown in the setter:

JavaKotlin

Copy

    
    
    HyprMX.INSTANCE.setConsentStatus(ConsentStatus.CONSENT_STATUS_UNKNOWN); // If you don't have consent status for the user, set this to CONSENT_STATUS_UNKNOWN

Copy

    
    
    HyprMX.setConsentStatus(ConsentStatus.CONSENT_STATUS_UNKNOWN) // If you don't have consent status for the user, set this to CONSENT_STATUS_UNKNOWN

##

**Age-restricted User Flag**

To adhere to the strictest laws and policies, HyprMX treats users under 16 as
children. HyprMX SDK provides an API to assist publishers with child-directed
treatment of users to support compliance with applicable regional laws and
regulations such as COPPA, GDPR, and Google Play Store policies. The publisher
is responsible for determining when to flag the end user as age-restricted
user and adhering to applicable laws and policies that require child-directed
treatment.

If the user requires a child-directed treatment, set the `ageRestrictedUser`
parameter to `true`.

JavaKotlin

Copy

    
    
    HyprMX.INSTANCE.setAgeRestrictedUser(true); // Set this to true if the user is under 16 or requires child-directed treatment

Copy

    
    
    HyprMX.setAgeRestrictedUser(true)

If the user doesn't require a child-directed treatment, set the
`ageRestrictedUser` parameter to `false`.

JavaKotlin

Copy

    
    
    HyprMX.INSTANCE.setAgeRestrictedUser(false); // Set this to false if the user is not under 16 or if you don't know whether the user is age restricted

Copy

    
    
    HyprMX.setAgeRestrictedUser(false)

##

**Google Play Families policy**

Google sets forth guidelines and requirements for publishers to follow if
their target audience includes children. It is the responsibility of the app
developer to ensure compliance with[ Google Play's Families
Program](https://play.google.com/console/about/programs/families/), including,
but not limited to,[ Google Play Families
Policies](https://support.google.com/googleplay/android-
developer/answer/9893335).

If your app is primarily directed at children, you **must** indicate to your
HyprMX Account Manager so the app can be designated as a child-directed app in
the backend. Additionally, you may use the Age-restricted User Flag to prevent
access to the AAID for end-users flagged as children.

If your app is directed at a mixed audience, including children, you **must**
use the Age-restricted User Flag to appropriately flag any user who is
considered a child under applicable jurisdiction as age-restricted user to
prevent access to the AAID for end-users flagged as children.

[PreviousAndroid / Amazon Setup Guide](/android-sdk)[NextGoogle's Data Safety
Questionnaire](/android-sdk/getting-started/googles-data-safety-questionnaire)

Last updated 4 months ago

On this page

  * Consent Flag
  * Age-restricted User Flag
  * Google Play Families policy

