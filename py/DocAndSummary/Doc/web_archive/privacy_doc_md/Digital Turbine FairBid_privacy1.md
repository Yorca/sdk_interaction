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

