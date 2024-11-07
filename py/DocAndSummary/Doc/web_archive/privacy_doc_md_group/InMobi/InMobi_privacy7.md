

# Opt-out Mechanism

## SDK Integrations

### Do Not Sell Flag

Suppose you directly integrate using the InMobi SDK. In that case, you can
indicate to InMobi and their ad tech partners when a resident from the United
States opts out of the sale of their personal data by using the do-not-sell
flag at the request level.

You must handle the indication of user opt-out through the do-not-sell flag by
setting its value to true or false:

  * If you want to opt out of interest-based advertising, set the `do-not-sell` flag to `true`.
  * If you don't wish to opt out of interest-based advertising, set the `do-not-sell` flag to `false`. If you don't set the value, it picks up `false` by default.

You can set this flag at a request level as follows:

### iOS

#### Objective-C

    
    
    [IMPrivacyCompliance setDoNotSell:YES];
    

#### Swift

    
    
    IMPrivacyCompliance.setDoNotSell(true)
    

### Android

#### Kotlin

    
    
    InMobiPrivacyCompliance.setDoNotSell(true) 
    

#### Java

    
    
    InMobiPrivacyCompliance.setDoNotSell(true)
    

#### Note

The minimum supported InMobi SDK versions for Do Not Sell API are 10.5.6 for
iOS and 10.5.7 for Android.

### US Privacy String

Alternatively, InMobi SDK supports the IAB (Interactive Advertising Bureau)
U.S. Privacy String.

The IAB developed the U.S. Privacy String in response to the California
Consumer Privacy Act (CCPA) rollout in 2020. Like the IAB TCF (Transparency
Consent Framework) in Europe, the U.S. privacy string is a cookie that stores
information about disclosures made and choices selected by website visitors
regarding their consumer rights. Publishers and advertisers then use this
cookie to pass information to their downstream framework participants or
technology partners. This ensures the website visitor doesn't have to opt out
multiple times and creates a limited-service provider contract when consumers
visit the digital property.

The U.S. Privacy String contains:

  * **General Metadata** : Information about whether or not the U.S. Privacy Regulations apply to the consumer.
  * **Explicit Notice** : If an "explicit notice" legal disclosure has been established, the U.S. Privacy String will note this.
  * **Opt-Out** : Details if the consumer has opted out of selling their personal information.

To notify InMobi when a U.S. resident opts out of the sale of their personal
data by using the `IABUSPrivacy_String`, follow the below guidelines:

### iOS

#### Objective-C

    
    
    [IMPrivacyCompliance setUSPrivacyString@""];
    

#### Swift

    
    
    IMPrivacyCompliance.setUSPrivacyString("")
    

### Android

#### Java

    
    
    InMobiPrivacyCompliance.setUSPrivacyString("")
    

#### Kotlin

    
    
    InMobiPrivacyCompliance.setUSPrivacyString("") 
    

#### Note

  * The minimum supported InMobi SDK versions for Do Not Sell API are 10.5.6 for iOS and 10.5.7 for Android.
  * Ensure that the string value you pass complies with the [IAB specification](https://iabtechlab.com/wp-content/uploads/2019/11/Technical-Specifications-FAQ-US-Privacy-IAB-Tech-Lab.pdf).

## oRTB Integrations

If you monetize with InMobi using an oRTB connection, follow the [oRTB
specification](https://github.com/InteractiveAdvertisingBureau/USPrivacy/blob/master/CCPA/OpenRTB%20Extension%20for%20USPrivacy.md#extension-
object-us_privacy-attribute) to pass the US Privacy string consent to InMobi
in the Extension Object.

#### On This Page

Last Updated on: 13 Jul, 2023

✕

## You are almost there...

By installing this SDK update, you agree that your Children Privacy Compliance
setting remains accurate or that you will update that setting, whenever there
is a change in your app's audience. You may update the app's Children Privacy
Compliance settings at <https://publisher.inmobi.com/my-inventory/app-and-
placements>.

I AGREE

(C) 2024 InMobi

![InMobi Support
Center](https://web.inmobicdn.net/website/website/6.0.1/v4/img/logo.png)

