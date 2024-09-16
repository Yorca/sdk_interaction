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

