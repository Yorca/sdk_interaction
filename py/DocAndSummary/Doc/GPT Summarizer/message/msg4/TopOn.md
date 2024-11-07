SDK name: TopOn
Documentation:
![](https://resource.helplook.net/docker_production/wa7y4l/icon/icon.png?rand=2028897097)

[![](https://resource.helplook.net/docker_production/wa7y4l/nav_logo/site_logo?rand=1966047563)](/)

Search...

[SDK
Download](https://portal.toponad.com/m/sdk/download)[TopOn](https://www.toponad.com/en)

Menu

# Domestic privacy configuration

For more information, please refer to the [Privacy Compliance
Guide](https://newdocs.toponad.com/docs/ByIf1V)

## 1\. Domestic personalized recommendation advertising switch  

## 2\. Set the privacy information control switch

  * In order to ensure that your App successfully passes the test and combined with the current regulatory focus, we can turn TopOn The initialization of the SDK is placed after the user agrees to the privacy policy. 
  * If you have higher demand, you can use the following methods to control it. Restricting user device data reporting may affect ad filling, so please consider using it. 

  

### 1\. TopOn

（1）TopOn SDK will collect the following user data by default:

​

  * public collection data：**System version name, system version number, application package name, application version name, application version number, device manufacturer, device model, screen resolution, mobile network code, mobile country code, language, time zone, User Agent, screen orientation, network Type, app installation source, acceleration sensor**
  * China SDK collects additional data：**MAC address, International Mobile Equipment Identity (IMEI), OAID, CPU model information, system startup identification, system update identification, whether the device is rooted, whether the device uses a proxy, the SSID of the device connected to the WIFI, Android ID,IMSI**
  * Non-China SDK collects additional data：**Google Ad ID, Android ID (versions below v6.1.80 collect Android ID by default, and will no longer collect it starting from v6.1.80)**

（2）TopOn SDK provides APIs for developers to limit the reporting of these
private data. When developers limit the reported device data, it may affect
the normal use of TopOn functions, such as traffic grouping, cross-promotion,
TopOn Adx and other functions. Developers are requested to Set with caution.

    
    
    //Call this code before initializing the SDK to limit the reporting of device privacy data. Incoming information will be restricted from reporting.
    ATSDK.deniedUploadDeviceInfo(
        DeviceDataInfo.DEVICE_SCREEN_SIZE //Screen Resolution
        , DeviceDataInfo.ANDROID_ID //Android ID
        , DeviceDataInfo.APP_PACKAGE_NAME //Application package name
        , DeviceDataInfo.APP_VERSION_CODE //Application version number
        , DeviceDataInfo.APP_VERSION_NAME //Application version name
         , DeviceDataInfo.BRAND //Device manufacturer
        , DeviceDataInfo.GAID //Google Ad ID
        , DeviceDataInfo.LANGUAGE //language
        , DeviceDataInfo.MCC //mobile web code
        , DeviceDataInfo.MNC //Mobile country code
        , DeviceDataInfo.MODEL //Device model
        , DeviceDataInfo.ORIENTATION //screen orientation
        , DeviceDataInfo.OS_VERSION_CODE //System version number
        , DeviceDataInfo.OS_VERSION_NAME //System version name
        , DeviceDataInfo.TIMEZONE //Time zone
        , DeviceDataInfo.USER_AGENT //User Agent
        , DeviceDataInfo.NETWORK_TYPE //Network Type
        , DeviceDataInfo.INSTALLER //App installation source
        , ChinaDeviceDataInfo.MAC //MAC address
        , ChinaDeviceDataInfo.IMEI //International Mobile Equipment Identity Number
        , ChinaDeviceDataInfo.OAID //OAID
        , ChinaDeviceDataInfo.SSID//SSID
        , ChinaDeviceDataInfo.IMSI//IMSI
    );

  

**(3)(new in v6.1.10)TopOn SDK Provides API to pass existing device ID to
TopOn SDK, example:**

    
    
    ATSDK.setATPrivacyConfig(new ATPrivacyConfig() {
                    /**
                     *
                     * @return Google Ad ID
                     */
                    @Override
                    public String getDevGaid() {
                        return null;
                    }
    
                    /**
                     *
                     * @return IMEI information
                     */
                    @Override
                    public String getDevImei() {
                        return null;
                    }
    
                    /**
                     *
                     * @return OAID information
                     */
                    @Override
                    public String getDevOaid() {
                        return null;
                    }
    });

  

### **2\. Pangolin**

    
    
    TTATInitManager.getInstance().setTtCustomController(new TTCustomController() {
        /**
         * Whether to allow Pangolin SDK to actively use geolocation information
    ​
         *
         * @returnTrue can be obtained, false is prohibited from obtaining. Default is true
         */
        @Override
        public boolean isCanUseLocation() {
            return super.isCanUseLocation();
        }
        /**
         * When isCanUseLocation=false, the geographical location information can be passed in, and Pangolin SDK uses the geographical location information you pass in.
         *
         * @return Geolocation parameters
         */
        @Override
        public LocationProvider getTTLocation() {
            return super.getTTLocation();
        }
    
        /**
         * Whether to allow Pangolin SDK to actively obtain the collection permission of the application installation list on the device
         *
         * @returntrue can be used, false is prohibited. Default is true
         */
        @Override
        public boolean alist() {
            return super.alist();
        }
    
        /**
         * Whether to allow Pangolin SDK to actively use mobile phone hardware parameters, such as: imei
         *
         * @return true Can be used, false is prohibited. Default is true
         */
        @Override
        public boolean isCanUsePhoneState() {
            return super.isCanUsePhoneState();
        }
    
        /**
         * When isCanUsePhoneState=false, imei information can be passed in, and Pangolin SDK uses the imei information you pass in.
         *
         * @return imei information
         */
        @Override
        public String getDevImei() {
            return super.getDevImei();
        }
    
        /**
         * Whether to allow Pangolin SDK to actively use the ACCESS_WIFI_STATE permission
    ​
         *
         * @return true Can be used, false is prohibited. Default is true
         */
        @Override
        public boolean isCanUseWifiState() {
            return super.isCanUseWifiState();
        }
    
        /**
         * Mac information can be passed in. Pangolin sdk uses the Mac information you pass in.
    ​
         *
         * @return Mac information
         */
        @Override
        public String getMacAddress() {
            return super.getMacAddress();
        }
    
        /**
         * Whether to allow Pangolin SDK to actively use the WRITE_EXTERNAL_STORAGE permission
         *
         * @return true can be used, false is prohibited. Default is true
         */
        @Override
        public boolean isCanUseWriteExternal() {
            return super.isCanUseWriteExternal();
        }
    
        /**
         *Developers can pass in oaid
          * Related collection of OAID from the Academy of Information and Communications Technology - How to obtain OAID:
          1. Mobile Security Alliance official website http://www.msa-alliance.cn/
          2. Download CAICT Unified SDK http://msa-alliance.cn/col.jsp?id=120
         * @return oaid
         */
        @Override
        public String getDevOaid() {
            return super.getDevOaid();
        }
    });

**  
**

### **3\. Youlianghui**

    
    
    GDTATInitManager.getInstance().setGDTATCustomController(new GDTATCustomController() {
        /*
        *Whether the user agrees to the privacy policy, the default is true
    ​
        * */
        @Override
        public boolean getAgreePrivacyStrategy() {
            return super.getAgreePrivacyStrategy();
        }
    });
    /* * Pass in geographic location information or WeChat OpenID information through this method * */ 
    GlobalSetting.setExtraUserData(Map<String, String> extraUserData);
     /* * Use this method to block the Youlianghui SDK and obtain the list of application installations on the device * */ 
    GlobalSetting.setEnableCollectAppInstallStatus(false)；

  

### **4\. Kuaishou**

    
    
    KSATInitManager.getInstance().setKSATCustomController(new KSATCustomController() {
        /*
        * Whether to allow Kuaishou SDK to actively use ICCID, default true
        * */
        @Override
        public boolean getCanReadICCID() {
            return super.getCanReadICCID();
        }
    
        /*
         * Whether to allow Kuaishou SDK to actively use the Mac address, the default is true
         * */
        @Override
        public boolean getCanReadMacAddress() {
            return super.getCanReadMacAddress();
        }
        /*
         * Whether to allow Kuaishou SDK to actively use the nearby wifi list, the default is true
         * */
        @Override
        public boolean getCanReadNearbyWifiList() {
            return super.getCanReadNearbyWifiList();
        }
        /*
        *More private data revealed
         * Reference document: https://p1-web.adkwai.com/udata/pkg/KS-Android-KSAdSDk/doc/4701b963d40a77bc0f45fd71d30b57da352.pdf
         * Description of "3.5 Privacy Information Control Switch" under
        * */
        @Override
        public KsCustomController getKsCustomeController() {
            return super.getKsCustomeController();
        }
    });

**  
**

### **5\. Baidu**

    
    
    BaiduATInitManager.getInstance().setBaiduATCustomController(new BaiduATCustomController() {
        /*
         * Allow Baidu SDK to obtain device id, such as imei
         * */
        @Override
        public boolean getPermissionReadDeviceID() {
            return super.getPermissionReadDeviceID();
        }
    
        /*
         * Allow Baidu SDK to use positioning permissions
         * */
        @Override
        public boolean getPermissionLocation() {
            return super.getPermissionLocation();
        }
        /*
         *Allow Baidu SDK to use storage space
         * */
        @Override
        public boolean getPermissionStorage() {
            return super.getPermissionStorage();
        }
    
        /*
         * Allow Baidu SDK to use the permission to obtain the application installation list
    ​
         * */
        @Override
        public boolean getPermissionAppList() {
            return super.getPermissionAppList();
        }
    
        /*
         * Allow Baidu SDK to use OAID
         * */
        @Override
        public boolean getPermissionOAID() {
            return super.getPermissionOAID();
        }
    
        /*
         * Allow Baidu SDK to use device information
         * */
        @Override
        public boolean getPermissionDeviceInfo() {
            return super.getPermissionDeviceInfo();
        }
    
        /*
         * Set whether Baidu SDK allows obtaining APP update permissions
         * */
        @Override
        public boolean getPermissionAppUpdate() {
            return super.getPermissionAppUpdate();
        }
    
        /*
         *Set whether Baidu SDK allows access to running APP permissions
         * */
        @Override
        public boolean getPermissionRunningApp() {
            return super.getPermissionRunningApp();
        }
    });

  

### **6\. You Keying**

    
    
    KlevinATInitManager.getInstance().setKlevinCustomController(new KlevinCustomController() {
        /**
         * Whether to allow the SDK to collect geographical location information
         * @return true: SDK collects location information, false: SDK does not obtain location information. Default is true
         */
        public boolean isCanUseLocation() {
            return true;
        }
        /**
         * When isCanUseLocation is false, the APP can pass in the geographical location information, and the Youkeyin SDK uses the geographical location information you pass in.
    ​
         * @return Geolocation parameters
         */
        public Location getLocation() {
            return null;
        }
        /**
         * Whether to allow the SDK to collect mobile phone hardware parameters, such as: IMEI
         * @return true: SDK collects IMEI, false: SDK does not collect IMEI. Default is true
         */
        public boolean isCanUsePhoneState() {
            return true;
        }
        /**
         *When isCanUsePhoneState is false, developers can pass in the IMEI information, and Youkeying SDK will use the IMEI information you pass in, and the SDK will not collect it internally.
         * @return IMEI information
         */
        public String getDevImei() {
            return null;
        }
        /**
         *Whether to allow the SDK to actively use the ACCESS_WIFI_STATE permission
          * @return true: can be used, false: prohibited. Default is true
         */
        public boolean isCanUseWifiState() {
            return true;
        }
        /**
        * Developers can pass in oaid
          * Related collection of OAID from the Academy of Information and Communications Technology - How to obtain OAID:
          1. Mobile Security Alliance official website http://www.msa-alliance.cn/
          2. Download CAICT Unified SDK http://msa-alliance.cn/col.jsp?id=120
         * @return oaid
         */
        public String getDevOaid() {
            return null;
        }
    });

### **7\. TapTap**

    
    
    TapATInitManager.getInstance().setTapAdCustomController(new TapAdCustomController() {
                // Whether to allow the SDK to actively use geolocation information
    ​
                @Override
                public boolean isCanUseLocation() {
                    return true;
                }
    
                // When isCanUseLocation=false, geographical location information can be passed in, and TapAd will use the geographical location information you pass in.
                @Override
                public TapAdLocation getTapAdLocation() {
                    return null;
                }
    
                // Whether to allow the SDK to actively use mobile phone hardware parameters, such as imei
                @Override
                public boolean isCanUsePhoneState() {
                    return true;
                }
    
                // When isCanUsePhoneState=false, imei information can be passed in, and TapAd uses the imei information you pass in.
    ​
                @Override
                public String getDevImei() {
                    return null;
                }
    
                //Whether to allow the SDK to actively use the ACCESS_WIFI_STATE permission
                @Override
                public boolean isCanUseWifiState() {
                    return true;
                }
    
                // Whether to allow the SDK to actively use the WRITE_EXTERNAL_STORAGE permission
                @Override
                public boolean isCanUseWriteExternal() {
                    return true;
                }
    
               // Developers can pass in oaid
                 //Related collection of OAID from the Academy of Information and Communications Technology—how to obtain OAID:
                 // 1. Mobile Security Alliance official website http://www.msa-alliance.cn/
                 // 2. Download CAICT unified SDK http://msa-alliance.cn/col.jsp?id=120
    ​
                @Override
                public String getDevOaid() {
                    return null;
                }
    
                // Whether to allow the SDK to actively obtain the collection permission of the application installation list on the device
                @Override
                public boolean alist() {
                    return true;
                }
    
                // Whether to allow the SDK to actively obtain ANDROID_ID
                @Override
                public boolean isCanUseAndroidId() {
                    return true;
                }
    
                @Override
                public CustomUser provideCustomUser() {
                    return null;
                }
            });

## **3\. Domestic download ads Second pop-up window confirmation**

  

In compliance scenarios, download ads need to prompt the user before
downloading, and the download can only start after the user confirms.

During ad playback, when a click triggers an ad download, the developer needs
to obtain the application name, version and other relevant information and
display a pop-up window prompting the user to confirm the download.

Applicable ad types: All ad types

**Applicable advertising platforms include** ：Youlianghui, Pangolin, Kuaishou
(you need to contact Kuaishou to activate the function), Mintegral Domestic
(you need to contact Mintegral to activate the function), Sigmob (you need to
contact Sigmob to activate the function), You Keying (download ads will
automatically pop up, if you want to turn off the function , need to contact
the third party to close)

### **3.1 Youlianghui**

**You can contact Youlianghui to apply (recommendation), or set it yourself
through code**

#### **3.1.1 Code settings for secondary pop-up window confirmation**

  * **If the developer applies for the secondary pop-up window permission and confirms it successfully, no code setting is required.**
  * Using code settings requires the developer to draw a pop-up window and prompt the user to confirm the download.
  * **After turning it on, you must process the onDownloadConfirm logic in ATSplashExListener, otherwise the click will not respond.**

**Take open-screen advertising as an example, the sample code is as follows:**

    
    
    ATSplashAd splashAd = new ATSplashAd(this, placementId, atMediationRequestInfo, new ATSplashExListener() {
                @Override
                public void onDownloadConfirm(Context context, ATAdInfo adInfo, ATNetworkConfirmInfo networkConfirmInfo) {
    
                        if (networkConfirmInfo instanceof GDTDownloadFirmInfo) {
                         //Secondary pop-up window processing, DownloadApkConfirmDialogWebView is a class for drawing secondary confirmation pop-up windows, which requires developers to render it themselves.
                        new DownloadApkConfirmDialogWebView(context, ((GDTDownloadFirmInfo) networkConfirmInfo).appInfoUrl, ((GDTDownloadFirmInfo) networkConfirmInfo).confirmCallBack).show();
                        }
                }
               ....
          }, 5000);
    Map<String, Object> localMap = new HashMap<>();
    localMap.put(ATAdConst.KEY.AD_WIDTH, layoutParams.width);
    localMap.put(ATAdConst.KEY.AD_HEIGHT, layoutParams.height);
    
    // After clicking on the application advertisement, a second pop-up window will pop up to confirm the download (closed when set to false)
    ​
    localMap.put(ATAdConst.KEY.AD_CLICK_CONFIRM_STATUS, true); 
    
    splashAd.setLocalExtra(localMap);

**GDTDownloadFirmInfo API description:**

Variable| Description  
---|---  
scenes| Download the scenes where it happened , Scene constants defined by
ApkDownloadComplianceInterface: SCENES_AD_OR_NATIVE_LANDING_PAGE (indicating
that the downloading scenario is clicking on the advertisement itself, or the
native landing page), SCENES_WEB_LANDING_PAGE (indicating that the downloading
scenario is clicking on the landing page)  
appInfoUrl| URL address of the application information to be downloaded  
confirmCallBack| Developer via This callBack notifies the sdk whether to
continue downloading or cancel downloading. onConfirm: Confirm download;
onCancel: Cancel download  
  
  

  

Last modified: 2024-07-24[Powered by![](https://cdn-
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

![](https://resource.helplook.net/docker_production/wa7y4l/icon/icon.png?rand=2028897097)

[![](https://resource.helplook.net/docker_production/wa7y4l/nav_logo/site_logo?rand=1966047563)](/)

Search...

[SDK
Download](https://portal.toponad.com/m/sdk/download)[TopOn](https://www.toponad.com/en)

Menu

# Google Data Security Guidelines

[According to Google's data security
requirements](https://support.google.com/googleplay/android-
developer/answer/10787469?hl=zh-Hans), developers need to disclose what data
is collected by their apps and all SDKs integrated into their apps.

TopOn lists that the data collected by the TopOn SDK can be used to answer
Google's data security questionnaire.

Tips:

1\. This information is only used to answer Google's data security
questionnaire , for specific TopOn Privacy Compliance Guidelines, please read
"[TopOn Privacy Compliance Guidelines](/docs/Privacy-Compliance-Guide)"

**Data Collection and Security:**

Does the SDK collect or share any required user data types? | Whether all data collected by the SDK is encrypted during transmission ? | Does the SDK provide a way for users to request deletion of their data?   
---|---|---  
Yes| Yes| Yes  
  
  

**Data type:**

Data type| Scope| Collect| Sharing| Purpose of collection and sharing  
---|---|---|---|---  
Position| N/A| No| No| N/A  
Personal information| N/A| No| No| N/A  
Financial information| N/A| No| No|  N/A  
Health Information| N/A| No| No| N/A  
Information| N/A| No| No| N/A  
Photos or videos| N/A| No| No| N/A  
Sound file| N/A| No| No| N/A  
Files and documents| N/A| No| No| N/A  
Calendar| N/A| No| No| N/A  
Interaction| N/A| No| No| N/A  
Apply activities| Default| Yes - app interaction; other actions (interaction
with ads)| Yes - app interaction; other actions (with ads) Advertising
interactions)| App interactions: analytics; other actions: analytics, fraud
prevention, security and compliance; advertising or marketing.  
Web browsing| N/A| No| No| N/A  
Application information and performance| N/A| No| No| N/A  
Device ID and other IDs| Optional| Yes| Yes| Analysis, Fraud prevention,
security and compliance; advertising or marketing.  
  
  

Last modified: 2024-07-25[Powered by![](https://cdn-
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

