SDK name: Digital Turbine FairBid
Documentation:
AdColony SDK is no longer in operation. For inquiries or to register for DTX,
please contact
[monetization@digitalturbine.com](mailto:monetization@digitalturbine.com)

[ ![Logo](/hc/theming_assets/01J0TNPZH5HNC0B4JYVY4P382B) ](/hc/en-us "Home")

[Sign in](/hc/en-
us/signin?return_to=https%3A%2F%2Fdeveloper.digitalturbine.com%2Fhc%2Fen-
us%2Farticles%2F360010251818-GDPR&locale=en-us "Opens a dialog")

#  How can we help you?

  1. [Digital Turbine](/hc/en-us)
  2. [DT FairBid](/hc/en-us/categories/360001778457-DT-FairBid)
  3. [SDK Configurations](/hc/en-us/sections/9947507543196-SDK-Configurations)
  4. [Android SDK Configuration](/hc/en-us/sections/360002898457-Android-SDK-Configuration)
  5. [Advanced Settings](/hc/en-us/sections/360002954658-Advanced-Settings)

December 06, 2023 08:49

[Follow](/hc/en-us/articles/360010251818-GDPR/subscription.html "Opens a sign-
in dialog")

#  GDPR

The**General Data Protection Regulation** requires you to scope your user's
consent. A user is within the **GDPR** scope for your app when one more of the
following apply:

  * The user is currently located in the EU
  * The user has registered with the app as an EU resident
  * The app is specifically targeted to EU users

#### Important

**User Consent Not Passed**  
If you do not pass the user’s consent to the DT FairBid SDK, only contextual
ads will be shown to that user and your revenue might be negatively affected.

We recommend that the first time you gather a user’s consent, you pass it onto
the DT FairBid SDK before initializing it. The SDK will then take the user’s
consent into consideration when initializing. In the following sessions for
that user, you will only need to call the API in the event that the user
updates his or her consent (the SDK caches the consent).

Once you have collected the user’s consent, you can pass it to the SDK using
the following API:

## User Consent Given

    
    
    UserInfo.setGdprConsent(true, context); // true or YES if you have the user’s consent

## User Consent NOT Given

    
    
    UserInfo.setGdprConsent(false, context); // false or NOT if you have the user’s consent

## [Optional] Additional User Consent String

    
    
    String consentString = "BOEFEAyOEFEAyAHABDENAI4AAAB9vABAASA";
    UserInfo.setGdprConsentString(consentString, this);

You can read more about GDPR
[here](https://developer.digitalturbine.com/hc/en-
us/articles/360009980898-GDPR).

Back to Top ⇧

(C) Digital Turbine

AdColony SDK is no longer in operation. For inquiries or to register for DTX,
please contact
[monetization@digitalturbine.com](mailto:monetization@digitalturbine.com)

[ ![Logo](/hc/theming_assets/01J0TNPZH5HNC0B4JYVY4P382B) ](/hc/en-us "Home")

[Sign in](/hc/en-
us/signin?return_to=https%3A%2F%2Fdeveloper.digitalturbine.com%2Fhc%2Fen-
us%2Farticles%2F360010251878-CCPA-Privacy-String&locale=en-us "Opens a
dialog")

#  How can we help you?

  1. [Digital Turbine](/hc/en-us)
  2. [DT FairBid](/hc/en-us/categories/360001778457-DT-FairBid)
  3. [SDK Configurations](/hc/en-us/sections/9947507543196-SDK-Configurations)
  4. [Android SDK Configuration](/hc/en-us/sections/360002898457-Android-SDK-Configuration)
  5. [Advanced Settings](/hc/en-us/sections/360002954658-Advanced-Settings)

February 23, 2023 15:27

[Follow](/hc/en-us/articles/360010251878-CCPA-Privacy-String/subscription.html
"Opens a sign-in dialog")

#  CCPA - Privacy String

The intention of the California Consumer Privacy Act of 2018 (CCPA) is to
protect the personal information of California residents. CCPA applies to all
companies doing business in California. If a California resident uses an app
developer’s mobile app, CCPA applies to the developer and every company that
processes the personal information of the app’s users. CCPA came into effect
on 1 January 2020.

For more information on DT and CCPA, refer to DT's [Resource
Page](https://www.digitalturbine.com/ccpa-resource-page/).  
For more information about CCPA, refer to the [IAB CCPA Compliance
Framework](https://iabtechlab.com/standards/ccpa/).

# Setting the IAB US Privacy String

We recommend that the first time you gather a user opt out (aka 'consent'),
you pass it onto the SDK before initializing it. The SDK takes the user’s opt
out into consideration when initializing.

Once you have collected the user’s opt out, you can pass it onto the SDK and
set the IAB US privacy string using the following API:

    
    
    String privacyString = "1YNN";
    UserInfo.setIabUsPrivacyString(privacyString, context);

To determine what value to use for the US Privacy String, refer to the IAB
document
[here](https://github.com/InteractiveAdvertisingBureau/USPrivacy/blob/master/CCPA/US%20Privacy%20String.md).
Example values:

  * When CCPA does not apply (for example if the user is not a resident of California) you can either skip this API or use **1---**
  * If the user choses NOT to opt out, and is ok with advertising as usual, you can use **1YNN**
  * If the user chooses to restrict advertising and opt out, you can use **1YYN**

# Clearing Privacy Opt-Out

To clear the privacy string, use the following API:

    
    
    UserInfo.clearIabUsPrivacyString(context);

Back to Top ⇧

(C) Digital Turbine

AdColony SDK is no longer in operation. For inquiries or to register for DTX,
please contact
[monetization@digitalturbine.com](mailto:monetization@digitalturbine.com)

[ ![Logo](/hc/theming_assets/01J0TNPZH5HNC0B4JYVY4P382B) ](/hc/en-us "Home")

[Sign in](/hc/en-
us/signin?return_to=https%3A%2F%2Fdeveloper.digitalturbine.com%2Fhc%2Fen-
us%2Farticles%2F7019733520913-LGPD&locale=en-us "Opens a dialog")

#  How can we help you?

  1. [Digital Turbine](/hc/en-us)
  2. [DT FairBid](/hc/en-us/categories/360001778457-DT-FairBid)
  3. [SDK Configurations](/hc/en-us/sections/9947507543196-SDK-Configurations)
  4. [Android SDK Configuration](/hc/en-us/sections/360002898457-Android-SDK-Configuration)
  5. [Advanced Settings](/hc/en-us/sections/360002954658-Advanced-Settings)

February 23, 2023 15:27

[Follow](/hc/en-us/articles/7019733520913-LGPD/subscription.html "Opens a
sign-in dialog")

#  LGPD

**LGPD (Lei Geral de Proteção de Dados Pessoais)**  requires you to scope your
user's consent. A user is within the **LGPD** scope for your app when one more
of the following apply:

  * The user is currently located in Brazil
  * The user has registered with the app as a Brazilian resident
  * The app is specifically targeted to Brazilian users

#### Alert

**User Consent Not Passed**  
If you do not pass the user’s consent to the DT FairBid SDK, only contextual
ads will be shown to that user and your revenue might be negatively affected.

We recommend that the first time you gather a user’s consent, you pass it onto
the DT FairBid SDK before initializing it. The SDK will then take the user’s
consent into consideration when initializing. In the following sessions for
that user, you will only need to call the API in the event that the user
updates his or her consent (the SDK caches the consent).

Once you have collected the user’s consent, you can pass it onto the SDK using
the following API:

**User Consent Given**

    
    
    UserInfo.setLgpdConsent(true, context); // true if you have the user’s consent

**User Consent NOT Given**

    
    
    UserInfo.setLgpdConsent(false, context); // false if you have the user’s consent

You can read more about LGPD [here](https://developer.fyber.com/hc/en-
us/articles/7018487827345-LGPD).

Back to Top ⇧

(C) Digital Turbine

