![](https://resource.helplook.net/docker_production/wa7y4l/icon/icon.png?rand=2028897097)

[![](https://resource.helplook.net/docker_production/wa7y4l/nav_logo/site_logo?rand=1966047563)](/)

Search...

[SDK
Download](https://portal.toponad.com/m/sdk/download)[TopOn](https://www.toponad.com/en)

Menu

# GDPR configuration

## 1\. General Data Protection Regulation GDPR

Effective May 25, 2018, the European Union's General Data Protection
Regulation will officially come into effect. To protect the interests and
privacy of our developers and your users, we have updated our ["TopOn privacy
Policy" ](https://www.toponad.com/privacy-policy). At the same time, we have
added privacy permission settings to the SDK. Please check the following
configuration and complete the SDK integration.

  

## 2\. TopOn SDK configuration GDPR

### 2.1 Set TopOn GDPR level through TopOn SDK API

**(After setting, the third-party advertising platform GDPR reporting level
will be set internally based on this level)** :

    
    
    int level= { //level has the following options
      ATSDK.PERSONALIZED //Device data reporting is allowed
      ATSDK.NONPERSONALIZED //Device data is not allowed to be reported
      ATSDK.UNKNOWN //Unknown level, which can only be obtained through the getGDPRDataLevel method and cannot be set using the setGDPRUploadDataLevel method.
    }
    ATSDK.setGDPRUploadDataLevel(context, level);

###

### 2.2 Set the TopOn GDPR level through the authorized page provided by TopOn

**(The authorization page will set the reporting level according to the user's
choice)** :

    
    
    ATSDK.showGdprAuth(activity, new ATGDPRAuthCallback() {
        @Override
        public void onAuthResult(int level) {
            //The value of level is ATSDK.PERSONALIZED or ATSDK.NONPERSONALIZED
            ATSDK.setGDPRUploadDataLevel(context, level);   
            ATSDK.init(activity, appId, appKey);           
        }
    });

### 2.3 Set GDPR level through Ogury SDK

When you integrate Ogury, please use the following code to set up GDPR.
**Because Ogury does not provide an API to set the GDPR level, it can only be
set through their pop-up window.**

    
    
    ConsentManager.ask(context, "YourAssetKey", new ConsentListener() {
        @Override
        public void onComplete(final ConsentManager.Answer answer) {
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    if(ConsentManager.gdprApplies()) {
                        ATSDK.setGDPRUploadDataLevel(context, ATSDK.PERSONALIZED);
                    } else {
                        ATSDK.setGDPRUploadDataLevel(context, ATSDK.NONPERSONALIZED);
                    }
      ATSDK.init(applicationContext, appid, appkey);
    
                }
            });
        }
    
        @Override
        public void onError(final ConsentException e) {
            ATSDK.init(applicationContext, appid, appkey);
    
        }
    });
    
    

## 3\. GDPR configuration process recommendations in the EU

TopOn SDK > V5 .4.0 version, it is recommended to add the following GDPR
setting process. If the developer does not set the GDPR method when the user
is in the EU, TopOn SDK will adopt the GDPR default settings of the
advertising platform

### 3.1 Do not use the EU judgment API provided by TopOn SDK

**Process Description**

1\. After the APP is launched, the developer determines whether the user is in
the EU (the developer implements the method of determining whether the user is
in the EU by himself)

  * **Not in the EU** , skip to step 4
  * < span style="color: rgb(44, 62, 80);">**In the EU** , next step

2\. Determine whether the **Dataconsent** of TopOn SDK is **Unknown**

  * **is Unknown** (the GDPR level has not been set), next step
  * **Not Unknown** (GDPR level has been set), skip to step 4

3\. Call TopOn SDk's **showGdprAuth** Method (GDPR level set by user)  
4\. Initialize SDK

**Sample code**

    
    
    public void initTopOnSDK() {
        if (App. isEU() )  //App. isEU() is a method for determining the EU region implemented by developers themselves.
     { 
            if (ATSDK.getGDPRDataLevel(applicationContext) == ATSDK.UNKNOWN) {
                ATSDK.showGdprAuth(activity, new ATGDPRAuthCallback() {
                    @Override
                    public void onAuthResult(int level) {
                        ATSDK.setGDPRUploadDataLevel(applicationContext, level);
        ATSDK.init(applicationContext, appid, appkey);
                    }
                });
            }
          return;
        }
         ATSDK.init(applicationContext, appid, appkey);
    }
    

### 3.2 Use the EU judgment API provided by TopOn SDK

1\. After the App is started, execute the ATSDK.checkIsEuTraffic method to
dynamically obtain the current EU information, and at the same time initialize
ATSDK  

2\. Receive the detection results After the callback:

    * **True** , then proceed to the next step
    * **False****, it will no longer be processed**

**3\. Determine the TopOn SDK's Dataconsent is Unknown**

    * **Unknown (GDPR level has not been set), next step**
    * **No If it is Unknown (the GDPR level has been set), it will no longer be processed**

**4\. Call TopOn SDk showGdprAuth method (GDPR level set by user)**

**Sample code**

    
    
    ATSDK.checkIsEuTraffic(this, new NetTrafficeCallback() {
    
                @Override
                public void onResultCallback(boolean isEU) {
                    if (isEU && ATSDK.getGDPRDataLevel(DemoApplicaion.this) == ATSDK.UNKNOWN) {
                        ATSDK.showGdprAuth(DemoApplicaion.this);
                    }
    
                }
    
                @Override
                public void onErrorCallback(String errorMsg) {
                    Log.i("Demoapplication", "onErrorCallback:" + errorMsg);
                }
            });
    
            ATSDK.init(DemoApplicaion.this, appid, appKey);
    

**As shown in the picture:**

`****`![](https://cdn-customer.helplook.net/_hl/load-img.85451f72.png)

Last modified: 2024-02-06[Powered by![](https://cdn-
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

