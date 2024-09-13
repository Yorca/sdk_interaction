
# Children's Privacy Compliance

## Introduction

The Children's Online Privacy Protection Act (COPPA) is a law created to
protect the privacy of children under the age of 13. The Act was passed by the
U.S. Congress in 1998 and took effect in April 2000. COPPA is managed by the
Federal Trade Commission (FTC).

To reflect other regional law requirements and App Stores' policies regarding
data processing for children, InMobi treats children's privacy compliance
holistically in the Publisher Dashboard.

When a publisher adds their app or mobile website to the InMobi Publisher
Dashboard, or at any time when using the platform, the publisher is
responsible for indicating to InMobi when their inventory is directed to
children and ensuring they comply with the applicable law and App Stores
developer policies.

## Complying with COPPA & Children's Privacy

Children's privacy compliance is handled at the app level in the InMobi
Publisher Dashboard. By turning the toggle on, you are confirming that your
app is directed at children under the age of 16 or to a general audience which
may include children under the age of 16. In addition, you are confirming that
it complies with the Children's Online Privacy Protection Act and other
applicable regulations, which include terms on children's privacy.

## Children Privacy Compliance Settings under Inventory Tab

### Declare the App's Audience

With InMobi, you can now define your app's audience accurately. If your app is
directed to both children and adults, you can declare the app as a **Mixed
Audience App** in two simple steps:

  1. **Define Your App Audience** : Select the desired setting on the InMobi **Publisher Dashboard**. To find this prompt and declare an accurate audience for your app, navigate to **Inventory Settings &gt;&gt; Add Inventory** for new apps and **App Details &gt;&gt; Edit App Settings** for existing apps.![](https://i.l-new.inmobicdn.net/website/support/6.0.1/uploads/child_privacy.png)

#### Note

     * Apps declared as **Mixed Audience** are expected to know the user's age or have an age-gating mechanism within the app.
     * If you are declaring an app as a child-directed or a mixed audience app, you need to enable the settings on both your iOS and Android apps separately for parity. Our system has been developed to treat apps with the most conservative settings across Play Stores. Hence, if you are declaring an app as child-directed on iOS, the app will be treated as child-directed on Android too.

  2. **Pass the Age Restriction signals to InMobi** : If you have integrated via **SDK** and **API** , pass the age restriction information of users to InMobi and determine the definition of age restriction depending on the user's geographic data location.

#### SDK

If you have integrated via InMobi SDK, you should call the
`InMobiSdk.setIsAgeRestricted` API. If you pass the value as **True** , your
request will be treated as child-directed. The default value is **False**.

_**Android**_ :

#### Kotlin

    
    
    InMobiSdk.setIsAgeRestricted(false) // possible value are true, false
    

#### Java

    
    
    InMobiSdk.setIsAgeRestricted(false) // possible value are true, false;
    
    
    
    
    
    
    _**iOS**_ :
    
    
    
    
    
    
    
    
    #### Objective-C
    
    
    
    
    
    
    [IMSdk setIsAgeRestricted: false]; // possible value are true, false
    

#### Swift

    
    
    IMSdk. setIsAgeRestricted(false) // possible value are true, false
    

#### API

If you have integrated via API, you should pass the **OBJECT: Regs** to
InMobi.

Parameter | Scope | Type | Description  
---|---|---|---  
coppa | Optional | integer | Flag indicating if this request is subject to the COPPA regulations established by the USA FTC, where 0 = no, 1 = yes.  
ext | Optional | object | Placeholder for exchange-specific extensions to OpenRTB.  
ext.gdpr | Optional | integer | Indicates whether the request is subject to GDPR, where 0 = No, 1 = Yes.  
  
#### Note

You should complete both steps to support a mixed audience monetization setup.

You can read more about InMobi's COPPA compliance
[here](https://www.inmobi.com/coppa-terms). For any queries or concerns, you
can contact your **InMobi Account Manager** or write us at
[privacy@inmobi.com](mailto:privacy@inmobi.com).

#### On This Page

Last Updated on: 25 Sep, 2023

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

