![](https://resource.helplook.net/docker_production/wa7y4l/icon/icon.png?rand=2028897097)

[![](https://resource.helplook.net/docker_production/wa7y4l/nav_logo/site_logo?rand=1966047563)](/)

Search...

[SDK
Download](https://portal.toponad.com/m/sdk/download)[TopOn](https://www.toponad.com/en)

Menu

# Google UMP SDK Gudelines



## 1\. Background



> Starting January 16, 2024, publishers and developers using Google AdSense,
> Ad Manager, or AdMob when serving ads to users in the European Economic Area
> or the United Kingdom must use Google-certified transparency and user input
> that has been approved by the [IAB Consultation Management Platform (CMP)
> integrated with the Consultation Framework
> (TCF)](https://iabeurope.eu/transparency-consent-framework/)

Starting from 6.2.87, TopOn SDK provides a compatible Google UMP SDK method to
configure the GDPR level. TopOn SDK internally sets the GDPR reporting level
of the third-party advertising platform based on this level.



## 2\. How to Setup UMP

### 2.1 Enabling Google UMP on AdMob Dashboard

You first must create and publish the Google GDPR message on the AdMob
dashboard. To do so:

1\. Sign in to your AdMob account at
[apps.admob.com](https://apps.admob.com/).

  *     * [Add your apps to the AdMob dashboard](https://support.google.com/admob/answer/9989980?sjid=7572347865551051335-NA), if you have not done so already.

2\. Click **Privacy & messaging**.

3\. Click **GDPR.**

4\. Click **Create message**. The **GDPR message**  page opens.

5\. Select the apps that you want to display your message:

  1.  Click **Select apps**.
  2.  Select the desired apps.
  3.  Click **Save**.

6\. Select the languages in which you want to display your message.

7\. In the **User consent options**  section, select **Consent or Manage
options.**

     **Note** : Do not check the **Close (do not consent)**** ** option.

8\. In the **Targeting**** ** section, select **Countries subject to GDPR (EEA
and UK)**.

9\. Click **Continue**. The **Edit message**  page opens.

10\. In the **Message name**  field, enter a descriptive message name to help
you identify the message later. This name appears only on the **Privacy &
messaging** page and is not visible to users.

11\. Select the **Styling**** ** tab.

  1. Under the **Global** section, set the **Secondary color** to white (#ffffff).
  2. Under the **Buttons** section, set the **Secondary color** to gray (#6e6e6e).

12\. Click **Publish**.



### 2.2 Customize Ad Partners List

**Note** : By default, Google might not show all of your ad partners in your
GDPR message. If you fail to include these networks, this could adversely
affect your ad revenue. Follow the steps in this section to ensure all of your
ad partners appear in the GDPR message.

To Customize which ad partners show in the GDPR message:

1\. Open the [GDPR
settings](https://apps.admob.com/v2/privacymessaging/gdpr/settings)
page.![](https://cdn-customer.helplook.net/_hl/load-img.85451f72.png)

2\. Click the edit icon (![✎](https://cdn-customer.helplook.net/_hl/load-
img.85451f72.png)) under the **Review your ad partners**  section.

3\. Select the **Custom ad partners**  toggle and then select all of the
networks you integrated in your app.

Google Name |  TopOn SDK Network  
---|---  
Facebook | 
    
    
    Meta  
  
AppLovin Corp | 
    
    
    Applovin  
      
    
    Chartboost

|

    
    
    Chartboost  
  
ironSource Mobile | 
    
    
    IronSource  
  
InMobi Choice | InMobi  
BIGOAds | 
    
    
    Bigo  
  
Chartboost | Chartboost  
      
    
    UnityAds

| Unity Ads  
Ogury Ltd | Ogury  
      
    
    AdColony

|

    
    
    AdColony  
  
Google | 
    
    
    Admob  
      
    
    StartApp

|

    
    
    Start.io【StartApp】  
  
Verve Group | 
    
    
    PubNative【Verve】  
      
    
    Tapjoy

|

    
    
    Tapjoy  
  
Liftoff | 
    
    
    Vungle  
      
    
    F@N communications

| Nend  
Fyber |  Fyber  
      
    
    Kidoz

|

    
    
    Kidoz  
  
Mobvista/Mintegral | 
    
    
    Mintegral  
  
Note: Other advertising platforms that are not in this table, such as**Pangle,
Huawei, Maio, Appnext, MyTarget, Yandex,** etc., are not in the Admob GDPR
advertising partner list. TopOn will use pop-up consent results internally to
set the GDPR reporting level of these ad Network platforms.



**4.** Click **Confirm**.

5\. Click **Save**** ** at the bottom of the **GDPR settings**  page.



### **2.3 Enabling Google UMP**

1\. Start by adding the dependency for the Google User Messaging Platform SDK
to your module's app-level Gradle file (usually app/build.gradle)

    
    
    dependencies {
        implementation("com.google.android.ump:user-messaging-platform:2.1.0")
    }

2\. Add**gms.ads.APPLICATION_ID** in **AndroidManifest.xml** The value value
needs to be configured with the ID of the App  created in the Admob.

    
    
    <manifest>
        <application>
            <meta-data
                android:name="com.google.android.gms.ads.APPLICATION_ID"
                android:value="ca-app-pub-xxxxxxxxxxxxxxxx~yyyyyyyyyy"/>
        </application>
    </manifest>

3\. Call the ATSDK.showGDPRConsentDialog API and perform SDK initialization
within the onDismiss callback. ATSDK.showGDPRConsentDialog will internally
determine whether the UMP SDK is integrated. If it is integrated, it will use
the UMP SDK Api to pop up a GDPR information pop-up window. If there is no
integration, it will use the TopOn GDPR information pop-up window in the
European Union to let the user select the GDPR level.**Note** : You need to
initiate an ad request after the SDK is initialized.

    
    
    ATSDK.showGDPRConsentDialog(activity, new ATGDPRConsentDismissListener() {
        @Override
        public void onDismiss(ConsentDismissInfo consentDismissInfo) {
            //Note: The SDK needs to be initialized in this callback and the ad will be loaded after initialization.
            ATSDK.init(activity, appId, appKey);
        }
    });

4\. During the trial phase, you can use the sample code below to simulate the
UMP GDPR pop-up window popping up in the EU.

    
    
    /**
     * This test code needs to be removed before going online
     * deviceId can be filtered in logcat by calling ATSDK.showGDPRConsentDialog
     * "Use new ConsentDebugSettings.Builder().addTestDeviceHashedId"
     */
    ATSDK.setDebuggerConfig(this, "", new ATDebuggerConfig.Builder().setUMPTestDeviceId("deviceid").build());

### **2.4** Add a consent revocation link to your app

> **Note:** Consent revocation is the process by which users in the EEA
> (European Economic Area), the UK, and Switzerland who consented to
> personalized ads can revoke that consent. You must provide a link in your
> app's menu that allows users who want to revoke consent to do so, then
> present the consent message to those users again.

Learn more by visiting
[here](https://support.google.com/admob/answer/10113915?hl=en&ref_topic=10113206&sjid=8371632926513349913-AP).

Please refer to [the Google AdMob Ads SDK
Documentation](https://developers.google.com/admob/android/privacy#privacy_options)
for privacy options.

## 3.  FAQ

### 3.1 UMP SDK has been integrated into the project. How to update TopOn to
version 6.2.87 or above?

Since TopOnSDK will first read the GDPR related settings set by UMP SDK when
initializing to set the GDPR reporting level of the third-party advertising
platform, developers need to ensure that the "**ad partners** " list in the
Admob background GDPR settings must include all the advertising partners
integrated in your application. Ad platforms (except Pangle, Huawei, Maio,
Appnext, MyTarget, and Yandex platforms), please refer to the[Customize Ad
Partners List](https://rgdusb.helplook.com/docs/Google-UMP-SDK-
Gudelines#1e4a70d2f11803fb6fafbf458b5ca0c3) above for configuration.

In addition, it is recommended to use ATSDK.showGDPRConsentDialog to replace
the original UMP SDK Api calling code. Refer to the sample code above to
initialize the SDK in the onDismiss callback. If you want to retain the
original UMP SDK Api calling logic in the project, you need to refer to the
example in the [Admob UMP Usage
Guide](https://developers.google.com/admob/android/privacy?hl=zh-cn#request-
ads) and initialize the TopOn SDK after the
OnConsentFormDismissedListener#onConsentFormDismissed() callback or determine
that consensusInformation.canRequestAds is true.

Last modified: 2024-07-12[Powered by![](https://cdn-
customer.helplook.net/_hl/logo.098f3ac5.svg)](https://www.helplook.com/?source=support_wa7y4l)

  * [Getting Started](/docs/lMKM4P) __

    * [Introduction](/docs/mSI16D)
    * [ Get Started with TopOn](/docs/hdNNBR)
    * [Introduction to Basic Terms and Data Indicators](/docs/5Hd0ij)
    * [Topon Account Management](/docs/MfO9IZ)
  * [Platform Guide](/docs/5R9YAn) __

    * [Performance](/docs/Performance)
    * [ Application](/docs/Application)
    * [Mediation Management](/docs/xTb1HE) __

      * [Ad Source](/docs/Ad-Source)
      * [ Segment](/docs/Segment)
      * [Header bidding](/docs/Header-bidding)
      * [Advanced Setting](/docs/Advanced-Setting)
      * [Mediation data](/docs/Mediation-data)
    * [Network Setting](/docs/Network-Setting)
    * [Report](/docs/jztUzL) __

      * [Full Report](/docs/Full-Report)
      * [ Cohorts Report](/docs/Cohorts-Report)
      * [Funnel Report](/docs/Funnel-Report)
      * [User Engagement report](/docs/User-Engagement-report)
      * [Hourly Report](/docs/Hourly-Report)
      * [Cross Promotion Report](/docs/Cross-Promotion-Report)
      * [ROI Report](/docs/ROI-Report)
      * [Monitoring And Alarm](/docs/Monitoring-And-Alarm)
      * [Direct Offers Report](/docs/Direct-Offers-Report)
    * [Advanced](/docs/iGt0u3) __

      * [A/B Test](/docs/J8GsJv)
      * [ Log Analysis](/docs/kan3NQ)
      * [Sub-account Management](/docs/xxzaI9)
      * [Upload Network Report Data](/docs/Upload-Network-Report-Data)
      * [Cross Promotion](/docs/qXyFRq)
      * [Direct Offer](/docs/hdScTL)
      * [Test Mode](/docs/Test-Mode)
    * [Advertising Optimization & Data Troubleshooting](/docs/UVeVr4) __

      * [Waterfall and optimization tips](/docs/l6kH9E)
      * [ Data gap troubleshooting](/docs/VfpUl4)
      * [Data Fluctuation Troubleshooting](/docs/bvXyae)
      * [Other Data Issues](/docs/1PIRvy)
    * [Privacy policy](/docs/3ajolA) __

      * [Privacy Policy](/docs/Privacy-Policy)
  * [ Mediation Network Guide](/docs/2sOZw7) __

    * [Mediation Overview](/docs/Mediation-Overview)
    * [ Ad Format Mapping](/docs/Ad-Format-Mapping)
    * [CSJ](/docs/CSJ-integration-instructions)
    * [Tencent](/docs/Tencent-Ads-integration-instructions)
    * [Baidu Union Ads](/docs/Baidu-Union-Ads-integration-instructions)
    * [Kuaishou Ads](/docs/Kuaishou-Ads-integration-instructions)
    * [Huawei Ads](/docs/Huawei-Ads-integration-instructions)
    * [Meta](/docs/Meta-Audience-Network-integration-instructions)
    * [Admob](/docs/Admob-integration-instructions)
    * [Mintegral](/docs/Mintegral-integration-instructions)
    * [Liftoff(Vungle)](/docs/Vungle-integration-instructions)
    * [Pangle](/docs/Pangle-integration-instructions)
    * [UnityAds](/docs/UnityAds-integration-instructions)
    * [Applovin](/docs/Applovin-integration-instructions)
    * [Inmobi](/docs/Inmobi-integration-instructions)
    * [ironSource](/docs/ironSource-integration-instructions)
    * [Chartboost](/docs/Chartboost-integration-instructions)
    * [Helium](/docs/Helium-integration-instructions)
    * [ReklamUp](/docs/ReklamUp-integration-instructions)
    * [A4G(Admob)](/docs/A4G-Admob-integration-instructions)
    * [Google Ad Manager](/docs/Google-Ad-Manager)
    * [Digital Turbine(Fyber)](/docs/Fyber-integration-instructions)
    * [Adcolony](/docs/Adcolony-integration-instructions)
    * [TopOn ADX](/docs/TopOn-ADX) __

      * [(Unity) Integrate TopOn via ironSource custom network adapter](/docs/Unity-Integrate-TopOn-via-ironSource-custom-network-adapter)
      * [(Unity) Integrate TopOn via Max custom network adapter](/docs/Unity-Integrate-TopOn-via-Max-custom-network-adapter)
      * [Sellers.json and Ads.txt](/docs/Sellers-json-and-Ads-txt)
      * [TopOn Adx Client Bidding Integration](/docs/TopOn-Adx-Client-Bidding-Integration)
      * [(Android) Integrate TopOn Adx with IronSource Mediation](/docs/Integrate-TopOn-Adx-with-IronSource-Mediation)
      * [(Android) Integrate TopOn Adx with Max Mediation](/docs/Integrate-TopOn-Adx-with-Max-Mediation)
    * [Bigo Ads](/docs/Bigo-Ads-integration-instructions)
    * [Yandex](/docs/Yandex-integration-instructions)
    * [myTarget](/docs/myTarget-integration-instructions)
    * [Tapjoy](/docs/Tapjoy-integration-instructions)
    * [Maio](/docs/Maio-integration-instructions)
    * [Nend](/docs/Nend)
    * [Ogury](/docs/Ogury-integration-instructions)
    * [Kidoz](/docs/Kidoz-integration-instructions)
    * [Start.io](/docs/Start-io)
    * [Verve Group](/docs/Verve-Group-integration-instructions)
    * [TapTap](/docs/TapTap)
    * [Mi Uion](/docs/Mi-Uion)
    * [Klevin](/docs/Klevin)
    * [JAD](/docs/JAD)
    * [Sigmob](/docs/Sigmob-integration-instructions)
    * [appnext](/docs/appnext-integration-instructions)
    * [Custom Network](/docs/Custom-Network-integration-instructions)
    * [Network API Time Zone](/docs/Network-API-Time-Zone)
  * [SDK Integration Guides](/docs/cUkkAX) __

    * [Android](/docs/vxp6Qy) __

      * [Integrated](/docs/integration)
      * [ AD Formats](/docs/6uTCVc) __

        * [Rewarded video Ad](/docs/Rewarded-video-Ad)
        * [ Interstitial Ad](/docs/Interstitial-Ad-CQuK) __

          * [Custom interstitial ads](/docs/Custom-interstitial-ads-ai4T)
        * [ Splash Ad](/docs/Splash-Ad-wwJ3) __

          * [Best practices for Splash Ads](/docs/Best-Practices-for-Open-Screen-Ads-GRUR)
          * [ Customized splash screen ads](/docs/Customized-splash-screen-ads-iPyO)
        * [Banner Ad](/docs/Banner-Ad-I8kI) __

          * [Custom banner ads](/docs/Custom-banner-ads-zY3m)
        * [ Native Ad](/docs/Native-Ad-koMu) __

          * [(Caution) Notes for Native Advertising Platforms](/docs/Caution-Notes-for-Native-Advertising-Platforms)
      * [ Callback information description](/docs/Callback-information-description)
      * [Advanced](/docs/t6Xeoq) __

        * [Custom Network](/docs/Custom-advertising-platform) __

          * [Basic process](/docs/Basic-process)
          * [ Rewarded Video Ad](/docs/Rewarded-Video-Ad-I0s7)
          * [Interstitial Ad](/docs/Interstitial-Ad)
          * [Banner Ad](/docs/Banner-Ad-r4ki)
          * [Native Ad](/docs/Native-Ad)
          * [Splash Ad](/docs/Splash-Ad)
          * [Custom Client Bidding Network](/docs/Custom-Client-Bidding-Network)
        * [Admob content mapping function](/docs/Admob-content-mapping-function)
        * [WeChat mini program support](/docs/WeChat-mini-program-support)
        * [Custom parameters](/docs/Set-custom-parameters)
        * [Fully automatic loading](/docs/Fully-automatic-loading-F6tB) __

          * [rewarded video ads are fully loaded automatically](/docs/rewarded-video-ads-are-fully-loaded-automatically)
          * [ Interstitial ads are automatically loaded](/docs/Interstitial-ads-are-automatically-loaded)
      * [Policy compliance](/docs/mqm8R6) __

        * [Domestic privacy configuration](/docs/Domestic-privacy-configuration)
        * [ GDPR configuration](/docs/Overseas-privacy-configuration)
        * [Google Data Security Guidelines](/docs/Google-Data-Security-Guidelines)
        * [Google UMP SDK Gudelines](/docs/Google-UMP-SDK-Gudelines-oThF)
      * [Testing Networks](/docs/aAjULO) __

        * [How to test ads](/docs/How-to-test-ads)
        * [ Error code description](/docs/Error-code-description-ua8l)
        * [Test Tool](/docs/Test-Tool-Beta)
      * [Q&A](/docs/mfntvD) __

        * [FAQ](/docs/FAQ) __

          * [Compilation problems](/docs/Compilation-problems)
          * [ Ads no fill issue](/docs/Ads-no-fill-issue)
          * [Native advertising exception](/docs/Native-advertising-exception)
          * [Banner ad exception](/docs/Banner-ad-exception)
          * [Abnormal opening screen advertisement](/docs/Abnormal-opening-screen-advertisement)
          * [Interstitial screen and incentive anomalies](/docs/Interstitial-screen-and-incentive-anomalies)
          * [Game abnormality](/docs/Game-abnormality)
        * [Android SDK access FAQs](/docs/Android-SDK-access-FAQs)
    * [iOS Guide](/docs/UC0qle) __

      * [integrated](/docs/integrated)
      * [ AD Formats](/docs/GRlOmB) __

        * [Rewarded video ad](/docs/Rewarded-video-ads)
        * [ Interstitial Ad](/docs/Interstitial-Ads-srKk) __

          * [Custom interstitial ads](/docs/Custom-interstitial-ads)
        * [ Splash ad](/docs/Splash-screen-ads) __

          * [Best practices for splash Ads](/docs/Best-Practices-for-Open-Screen-Ads)
          * [ Customized splash ads](/docs/Customized-splash-screen-ads)
        * [Banner Ad](/docs/Banner-Ads-A93Q) __

          * [Custom banner ads](/docs/Custom-banner-ads)
        * [ Native Ad](/docs/Native-Advertising)
      * [Advanced](/docs/bR8N2L) __

        * [Fully automatic loading](/docs/Fully-automatic-loading-m9JA) __

          * [Rewarded video ads](/docs/Rewarded-video-ads-lUrB)
          * [ Interstitial Video](/docs/Interstitial-Video)
        * [Custom parameters](/docs/Custom-parameters)
        * [Custom advertising platform](/docs/Custom-advertising-platform-Y6CD) __

          * [Basic process](/docs/Basic-process-l8Ih)
          * [ Rewarded video](/docs/Rewarded-video)
          * [Interstitials](/docs/Interstitials)
          * [Splash ads](/docs/Splash-ads-Rowx)
          * [Banner ads](/docs/Banner-ads-qxqY)
          * [native advertising](/docs/native-advertising-SJow)
          * [Custom advanced configuration](/docs/Custom-advanced-configuration)
        * [WeChat mini program support](/docs/WeChat-mini-program-support-gkLU)
      * [Policy compliance](/docs/ONYGJY) __

        * [Privacy Information Statement](/docs/Privacy-Information-Statement)
        * [ GDPR configuration](/docs/GDPR-configuration-TnKK)
        * [Google UMP Adaptation Usage Guide](/docs/Google-UMP-Adaptation-Usage-Guide)
      * [Test](/docs/3MffkL) __

        * [How to test ads](/docs/How-to-test-ads-pzHY)
        * [ Testing tools (Beta)](/docs/Testing-tools-Beta)
        * [Test ID](/docs/Test-ID)
        * [Callback description](/docs/oMfi2W) __

          * [SDK >=6.3.61 callback description](/docs/SDK-6-3-61-callback-description)
          * [SDK<6.3.61 callback description](/docs/SDK-6-3-61-callback-description-kJWG)
        * [Error code](/docs/Error-code)
      * [Q&A](/docs/ytBV5B) __

        * [FAQ troubleshooting guide](/docs/FAQ-troubleshooting-guide) __

          * [Compilation and listing issues](/docs/Compilation-and-listing-issues)
          * [ Not filling or loading failure](/docs/Not-filling-or-loading-failure)
          * [Native AD exception](/docs/Native-AD-exception)
          * [Banner AD exception](/docs/Banner-AD-exception)
          * [Splash AD exception](/docs/Splash-AD-exception)
          * [Rewarded AD and Interstitial exception](/docs/Rewarded-AD-and-Interstitial-exception)
        * [iOS SDK access FAQs](/docs/iOS-SDK-access-FAQs)
      * [iOS14.5+ support](/docs/qIRbte)
    * [Unity Guide](/docs/B5HRHG) __

      * [Integrated Basic Description](/docs/xsG93u) __

        * [SDK import instructions](/docs/SDK-import-instructions) __

          * [TopOn Unity3D Plugin (2.0.0+) import instructions](/docs/TopOn-Unity3D-plugin-2-import-instructions)
        * [ Unity SDK initialization](/docs/Unity-SDK-initialization)
        * [Rewarded Video Ad](/docs/Rewarded-video-ad-integration-instructions) __

          * [Fully automatic loading of incentive videos](/docs/Fully-automatic-loading-of-incentive-videos)
        * [ Interstitial ad](/docs/Interstitial-Ad-Integration-Instructions) __

          * [Fully automatic loading of interstitial ads](/docs/Fully-automatic-loading-of-interstitial-ads)
        * [ Banner Ad](/docs/Banner-advertising-integration-instructions)
        * [Native](/docs/Native-Ads-Integration-Instructions)
        * [Splash ad](/docs/Open-screen-advertising-access)
        * [Callback information description](/docs/Callback-information-description-dOjB)
        * [Error codes and FAQ](/docs/Error-codes-and-FAQ)
      * [Policy compliance](/docs/CQlUHh) __

        * [Google UMP SDK Gudelines](/docs/Google-UMP-SDK-Gudelines-0XZF)
        * [ Privacy Compliance Guide](/docs/Privacy-Compliance-Guide)
        * [Set up GDPR](/docs/Set-up-GDPR)
      * [Integration Testing](/docs/jNARvK) __

        * [Testing Guide](/docs/Testing-Guide)
        * [ Testing tools](/docs/Testing-tools-Beta-lXhy)
    * [Flutter Guide](/docs/OMbKDO) __

      * [Import and configure](/docs/3JCx7n)
      * [ Initialization instructions](/docs/Initialization-instructions-3iXm)
      * [Splash ads](/docs/Splash-ads-iRKG)
      * [Rewarded video](/docs/Rewarded-video-ehFo)
      * [Interstitials ads](/docs/Interstitials-ads-CwqH)
      * [banner ads](/docs/banner-ads-VMiL)
      * [native ads](/docs/native-ads)
      * [Callback information](/docs/Callback-information-eZOu)
      * [FAQ and error codes](/docs/FAQ-and-error-codes)
      * [Download Flutter files](/docs/Download-Flutter-files)
    * [Cocos Creator Guide](/docs/9Xhkol) __

      * [Import and configure](/docs/Import-and-configure-QIpl)
      * [ Initialization instructions](/docs/Initialization-instructions-8nXi)
      * [Rewarded video](/docs/motivational-video-WfKm) __

        * [Fully automatic loading](/docs/Fully-automatic-loading-oq9N)
      * [ Interstitials ads](/docs/interstitials-fm0O)
      * [Banner ads](/docs/banner-ads-RBzN)
      * [Native ads](/docs/native-advertising-EmBO)
      * [Callback information](/docs/Monitoring-callback-information-description-MHzn)
      * [FAQ and error codes](/docs/FAQ-and-error-codes-q757)
    * [React Native Guide](/docs/KEMyy4) __

      * [Import and configure](/docs/Import-and-configure-i8P2)
      * [ Initialization instructions](/docs/Initialization-instructions-VWug)
      * [Rewarded video](/docs/motivational-video-EL2B)
      * [Interstitials ads](/docs/interstitials-ipu2)
      * [Banner ads](/docs/banner-ads-tJNc)
      * [Callback information](/docs/Monitoring-callback-information-description-gER9)
      * [FAQ and error codes](/docs/FAQ-and-error-codes-y516)
    * [Advanced features](/docs/aHxwBl) __

      * [Scenario AD scene](/docs/Scenario-advertising-scene)
      * [ Segment](/docs/Segment-cAgO)
      * [cold start strategy](/docs/cold-start-strategy)
      * [SDK preset strategy](/docs/SDK-preset-strategy)
      * [Server-side rewarded](/docs/Serverside-incentives)
  * [Open API Guide](/docs/h8XHF8) __

    * [Demo](/docs/Demo)
    * [ Authentication](/docs/Authentication)
    * [Error Code](/docs/Error-Code)
    * [Management API](/docs/Management-API) __

      * [App API](/docs/App-API)
      * [ Placement API](/docs/Placement-API)
      * [Segment API](/docs/Segment-API)
      * [Waterfall API](/docs/Waterfall-API)
      * [Network API](/docs/Network-API)
      * [Adsource API](/docs/Adsource-API)
      * [A/B Test](/docs/A-B-Test)
    * [Reporting API](/docs/Reporting-API) __

      * [Full report](/docs/Full-report)
      * [ Ltv 1-60 days report](/docs/Ltv-160-days-report)
      * [Retention 2-60 day report](/docs/Retention-260-day-report)
    * [Device Reporting API](/docs/Device-Reporting-API) __

      * [Impression And Click Device report](/docs/Impression-And-Click-Device-report)
    * [ Upload revenue report](/docs/Upload-revenue-report)
    * [Appendix](/docs/Appendix) __

      * [APP category and sub category enum](/docs/APP-category-and-sub-category-enum)
      * [ Segment rule enum](/docs/Segment-rule-enum)
      * [Detailed parameters of network](/docs/Detailed-parameters-of-network)
  * [H5 SDK Access Guide](/docs/OibqXn) __

    * [Platform Guide](/docs/H5lTag) __

      * [Configuration Instructions](/docs/Configuration-Instructions)
    * [ Network Guide](/docs/3UebRt) __

      * [AdSense](/docs/AdSense)

[ Powered by![](https://cdn-
customer.helplook.net/_hl/logo.098f3ac5.svg)](https://www.helplook.com/?source=support_wa7y4l)

