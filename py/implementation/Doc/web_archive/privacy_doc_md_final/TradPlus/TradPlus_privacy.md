Skip to main content

Menu

[![TradPlus](/en/img/logo.png)![TradPlus](/en/img/logo.png)](/en/)[Android
Access
Guide](/en/docs/tradplussdk_android_doc_v6/quick_start/interstitial)[iOS
Access
Guide](/en/docs/integration_ios/fast_integration_ios/fast_interstitial)[Unity3D
Access Guide](/en/docs/doc_u3d/u3d_integration/setting_plugin)[API
Document](/en/docs/api_cn/api_report_v2_0)

English

  * [中文](/)
  * [English](/en/)

SDK Download

  * Android SDK Download
  * iOS SDK Download
  * Unity Plugin Download

[![TradPlus](/en/img/logo.png)![TradPlus](/en/img/logo.png)](/en/)

  * Languages
    * [中文](/)
    * [English](/en/)
  * [Android Access Guide](/en/docs/tradplussdk_android_doc_v6/quick_start/interstitial)
  * [iOS Access Guide](/en/docs/integration_ios/fast_integration_ios/fast_interstitial)
  * [Unity3D Access Guide](/en/docs/doc_u3d/u3d_integration/setting_plugin)
  * [API Document](/en/docs/api_cn/api_report_v2_0)

Menu

  * Quick Start
    * [Interstitials](/en/docs/tradplussdk_android_doc_v6/quick_start/interstitial)
    * [Rewarded Ads](/en/docs/tradplussdk_android_doc_v6/quick_start/rewardvideo)
    * [Splash](/en/docs/tradplussdk_android_doc_v6/quick_start/quick_splash)
    * [Native Ads](/en/docs/tradplussdk_android_doc_v6/quick_start/quick_native)
    * [Banners](/en/docs/tradplussdk_android_doc_v6/quick_start/quick_banner)
    * [In-stream Video Ad](/en/docs/tradplussdk_android_doc_v6/quick_start/mediavideo)
  * Advanced Features
    * [Segement](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/android_access_doc)
    * ROI
      * [User level impression revenue](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/impression_revenue)
      * [Firebase integration](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/firebase_measure_ad_revenue)
      * [AppsFlyer integration](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/appsflyer)
      * [Adjust integration](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/adjust)
      * [ThinkingData integration](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/thinkingdata_docs)
      * [Singluar integration](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/singluar_docs)
      * [tenjin integration](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/tenjin_an)
      * [solar-engine integration](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/roi/solar_engine_an)
    * [Loading Ad In Different Scenarios](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/adscenario_info)
    * [Server Reward Verification](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/rewardedvideo_s2s_doc-2)
    * [Callback Information](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/callback_info)
    * [Error Code](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/errormsg)
    * [Google Content Mapping Feature](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/google_content_mapping)
    * [App-ads.txt](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/app-ads)
    * [TTD：UID2 user guide](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/ttd_uid2_android)
    * Other
      * [Other function introduction](/en/docs/tradplussdk_android_doc_v6/tradplus_sdk_overview/others/other_api)
  * Privacy PoLicy
    * [Privacy Regulations](/en/docs/tradplussdk_android_doc_v6/privacy_policy/os_privacy_policy)
  * Test Your Integration
    * [Test Mode](/en/docs/tradplussdk_android_doc_v6/sdk_test_android/testmode)
  * [Android FAQ](/en/docs/tradplussdk_android_doc_v6/android_faq)
  * [Change Log](/en/docs/tradplussdk_android_doc_v6/change_log)

# Privacy Regulations

> **In order to protect the interests and privacy of our developers and your
> users, and conduct business in compliance with relevant laws, regulations,
> policies and standards。**

* * *

## Step 1 、Check the current region#

  * Android V8.4.0.1 began to support
  * Call this method before initializing the SDK

TradPlusSdk.checkCurrentArea(this,new
TPPrivacyManager.OnPrivacyRegionListener() {

@Override

public void onSuccess(boolean isEu, boolean isCn, boolean isCalifornia) {

// After obtaining the relevant regional configuration, set the relevant
privacy API, and then initialize the SDK

if(isEu) {

// Indicates that it is the European region, set GDPR

}

if(isCalifornia){

// Indicates that it is the California region of the United States, set CCPA

}

}

@Override

public void onFailed() {

// Generally, the query fails due to network problems. Developers need to
judge the region by themselves, and then set the privacy

}

});

Copy

## Step 2、CCPA#

It mainly introduces how to set CCPA in the Android project: ：

> The California Consumer Privacy Act (CCPA) is the first comprehensive
> privacy law in the United States. Signed into law in late June 2018, it
> provides California consumers with a variety of privacy rights. Businesses
> subject to the CCPA will have several obligations to these consumers,
> including disclosure of information, consumer rights similar to the European
> Union's General Data Protection Regulation (GDPR), the right to "opt out" of
> certain data transfers, and the right to "opt-in" not The Rights of Adults.

* * *

#### When to set#

  * Developers below V8.4.0.1 have to judge the region by themselves，If they are in the California region of the United States, they need to set CCPA and then initialize the SDK.
  * V8.4.0.1 and above, you can call the `checkCurrentArea()` method to determine the region（see above to view the current area introduction), set CCPA when the monitor callback isCalifornia returns true, and then initialize the SDK.

#### TP API#

Platform| Method| Note  
---|---|---  
Android| `TradPlusSdk.setCCPADoNotSell(context, boolean);`| `false` California
users do not report data ；`true` accept reported data  
Unity3dAndroid| `TradPlus.setCCPADoNotSell(boolean); `| `false` California
users do not report data ；`true` accept reported data  
  
#### Meta Settings CCPA#

  * Starting from V6.9.4 API, according to the requirements of Meta (Facebook), developers need to set CCPA by themselves.

  * If you need to integrate Meta, make sure to comply with Meta CCPA regulations 。
  * Please refer to [data-processing-options](https://developers.facebook.com/docs/marketing-apis/data-processing-options#audience-network-sdk)

  * Please note that you need to set Facebook's Limited Data Use flag before initializing the TradPlus SDK.

Sample code :

import com.facebook.ads.AdSettings;

...

// If you do not want to enable Limited Data Use (LDU) mode, pass
SetDataProcessingOptions() an empty string array:

AdSettings.setDataProcessingOptions( new String[] {} );

// To enable LDU for users and specify user geography, call
SetDataProcessingOptions() in a form like this:

AdSettings.setDataProcessingOptions( new String[] {"LDU"}, 1, 1000 );

Copy

## Step 3、COPPA#

It mainly introduces how to set COPPA in the Android project:

> The Children's Online Privacy Protection Act mainly targets the online
> collection of personal information of children under the age of 13.

> The protection law stipulates that website administrators should abide by
> privacy rules, must explain when to ask for consent from children's parents
> and provide verifiable methods, and website administrators must protect
> children's online privacy and safety, including restricting sales to
> children under the age of 13.

* * *

  * Must be called before initializing TradPlus SDK
  * If the application is for adults, you can upload it directly false

#### API#

Platform| Method| Note  
---|---|---  
Android| `TradPlusSdk.setCOPPAIsAgeRestrictedUser(context, boolean);`| `false`
show that it is not a child ；`true` show that it is a child  
Unity3dAndroid| ` TradPlus.setCOPPAIsAgeRestrictedUser(boolean);`| `false`
show that it is not a child ；`true` show that it is a child  
  
#### Start.io#

  * TPV9.3.0.1 and above versions support Start.io to configure Coppa in the AndroidManifest.xml file

  * The app is aimed at a mixed audience (that is, for everyone, including children and families), is a mixed user profile `true`, is not a mixed user profile `false`

<meta-data

android:name="com.startapp.sdk.MIXED_AUDIENCE"

android:value="true"/>

Copy

  * Indicates whether a particular end user is a child, is a child user pass `true`, is not a child user pass `false`

<meta-data

android:name="com.startapp.sdk.CHILD_DIRECTED"

android:value="true"/>

Copy

## Step 4、GDPR#

It mainly introduces how to set GDPR in the Android project:

> The General Data Protection Regulation (GDPR) is a regulation of data
> protection and privacy law for all citizens of the European Union (EU) and
> European Economic Area (EEA). We have added a privacy permission setting in
> the SDK. Please check the configuration below and complete the SDK
> integration.

> On May 25, 2018, after the GDPR came into effect, Twitter, WhatsApp and
> other social apps updated their user terms, saying that they would prohibit
> teenagers under the age of 16 from using these apps. This is because there
> are strict regulations on the protection of children's personal information
> in the GDPR.

### Android platform settings GDPR#

#### 1、Use the TradPlus authorization page to set up GDPR#

  * Called before initializing the TradPlus SDK
  * Below V8.4.0.1, you need to call the TradPlusSdk.isEUTraffic(context) method to determine whether you are in the EU region， and only call showUploadDataNotifyDialog to set GDPR if you are in the EU region.
  * For V8.4.0.1 and above, you can call the checkCurrentArea() method to determine the area(see above to view the current area introduction), and set GDPR when the monitoring callback isEu returns true.

Sample code (V6.X ~ V8.4.0.1)

// Determine whether the user has already selected, return true to indicate
that the selection has been made, and there is no need to pop up the window
again

if(!TradPlusSdk.isFirstShowGDPR(this)) {

// Set GDPR listener

TradPlusSdk.setGDPRListener(new TradPlusSdk.TPGDPRListener() {

@Override

public void success(String msg) {

// get the country successfully

// Determine whether it is an EU country, if it is not an EU country, ignore
it directly

if(TradPlusSdk.isEUTraffic(context)) {

// It is an EU country, call the TradPlus authorization page, pop up a pop-up
window, let the user set the GDPR level by himself

TradPlusSdk.showUploadDataNotifyDialog(this, new
TradPlusSdk.TPGDPRAuthListener() {

@Override

public void onAuthResult(int level) {

// Get the setting result and make a record, true indicates that the user has
made a selection

TradPlusSdk.setIsFirstShowGDPR(context,true);

}

}, Const.URL.GDPR_URL); // Const.URL.GDPR_URL is the authorization page
defined by TradPlus

}

}

@Override

public void failed(String errormsg) {

// Unknown country, call the TradPlus authorization page, pop up a pop-up
window, let the user set the GDPR level by himself

TradPlusSdk.showUploadDataNotifyDialog(this, new
TradPlusSdk.TPGDPRAuthListener() {

@Override

public void onAuthResult(int level) {

// Get the setting result and make a record, true indicates that the user has
made a selection

TradPlusSdk.setIsFirstShowGDPR(context,true);

}

}, Const.URL.GDPR_URL);

}

});

}

Copy

#### 2、Customize the pop-up window to set GDPR#

In addition to using the TradPlus authorization page to set the GDPR level,
developers can also set the GDPR through a custom pop-up window. You need to
refer to the above API settings. The steps are as follows：

  * 1、Before initializing TradPlus SDK, call to set GDPR monitoring；
  * 2、 Set the GDPR monitoring `success` callback to determine whether you are in the EU region; if you are in the EU region, call your customized pop-up window and record the user's choice;；
  * 3、Set the GDPR monitoring `failed` callback to call your custom pop-up window and record the user's choice；

#### 3、API Introduction#

##### (1)Set up GDPR Listener#

TradPlusSdk.setGDPRListener(new TradPlusSdk.TPGDPRListener() {

@Override

public void success(String msg) {

//Successfully get the country

}

@Override

public void failed(String errormsg) {

//unknown country

}

});

Copy

##### (3)Other APIs#

Note| method| Remark  
---|---|---  
Are you in the EU| `TradPlusSdk.isEUTraffic(context);`| Need to be called in
setting GDPR Listener `success` callback  
Set GDPR level| `TradPlusSdk.setGDPRDataCollection(context,level);`| Parameter
two: PERSONALIZED device data is allowed to be reported; NONPERSONALIZED
device data is not allowed to be reported  
Get the GDPR rating| `TradPlusSdk.getGDPRDataCollection(context);`| Return
value 0 means agree, 1 means disagree  
Is it the first time the user selects|
`TradPlusSdk.isFirstShowGDPR(context);`| By default, `false` no selection has
been made; `true` indicates that the user has selected  
Record the user's choice| `TradPlusSdk.setIsFirstShowGDPR(context,true);`|
`true` Indicates that the user has made a choice and needs to `onAuthResult`
be called in the callback for setting the GDPR level on the authorization page  
Set up GDPR children| `TradPlusSdk.setGDPRChild(context,boolean);`| `true`
Indicates that the user is a child  
  
### Unity3DAndroid platform settings GDPR#

#### 1、Use the TradPlus authorization page to set up GDPR#

  * Called before initializing the TradPlus SDK
  * Below V8.4.0.1, you need to call the TradPlusSdk.isEUTraffic(context) method to determine whether you are in the EU region， and only call showUploadDataNotifyDialog to set GDPR if you are in the EU region.
  * For V8.4.0.1 and above, you can call the checkCurrentArea() method to determine the area(see above to view the current area introduction), and set GDPR when the monitoring callback isEu returns true.

Sample code (V6.X ~ V8.4.0.1)

//Set up GDPR Listener

TradPlus.setGDPRListener();

public void GDPRSuccess(string appId) {

// get the country successfully

bool isEUTraffic = TradPlus.isEUTraffic();

bool isFirstShow = TradPlus.isFirstShow();

// Determine if you are in the EU and the user has not selected

if (isEUTraffic && !isFirstShow) {

// It is an EU country, call the TradPlus authorization page, pop up a pop-up
window, let the user set the GDPR level by himself

// The method has helped the developer to record the user's choice

TradPlus.showUploadDataNotifyDialog();

}

}

public void GDPRFailed(string appId) {

// Unknown country, call the TradPlus authorization page, pop up a pop-up
window, let the user set the GDPR level by himself

// The method has helped the developer to record the user's choice

TradPlus.showUploadDataNotifyDialog();

}

Copy

#### 2、Customize the pop-up window to set GDPR#

In addition to using the TradPlus authorization page to set the GDPR level,
developers can also set the GDPR through a custom pop-up window. You need to
refer to the above API settings. The steps are as follows：

  * 1、Before initializing TradPlus SDK, call to set GDPR listener;；
  * 2、Set the GDPR monitoring `success` callback to determine whether you are in the EU region; if you are in the EU region, call your customized pop-up window and record the user's choice；
  * 3、Set the GDPR monitoring `failed` callback to call your custom pop-up window and record the user's choice;；

#### 3、API Introduction#

##### (1) Set up GDPR Listener#

/*

* Called before initializing TradPlus SDK

* In OnGDPRSuccessEvent, determine whether it is an EU country

*/

TradPlus.setGDPRListener();

TradPlusManager.OnGDPRSuccessEvent += OnGDPRSuccessEvent; //Get the country
successfully

TradPlusManager.OnGDPRFailedEvent += OnGDPRFailedEvent; //unknown country

Copy

##### (2)Call the authorization page to set GDPR#

TradPlus.showUploadDataNotifyDialog();//Use the URL provided by TradPlus

Copy

##### (3)Other APIs#

  * Other version API

Note| Method| Remark  
---|---|---  
Are you in the EU| `TradPlus.isEUTraffic();| Need to be called in setting GDPR
Listener success callback  
Set GDPR level| `TradPlus.setGDPRDataCollection(int);`| 0 The device data is
allowed to be reported; 1 The device data is not allowed to be reported  
Get the GDPR rating| `TradPlus.getGDPRDataCollection();`| Return value 0 means
agree, 1 means disagree  
Is it the first time the user selects| `TradPlus.isFirstShow();`| By default,
`false` no selection has been made; `true` indicates that the user has
selected  
Record the user's choice| `TradPlus.setFirstShow(true);`| `true` Indicates
that the user has made a choice, and the method provided by TradPlus
`TradPlus.showUploadDataNotifyDialog()` has been called by the developer  
Set up GDPR children| `TradPlus.setGDPRChild(boolean);`| `true` Indicates that
the user is a child, only supported by Admob's Support  
  
## Step 5、How to set up DFF#

ｐ

  * If the application needs to comply with the Google Play family policy requirements, the following code needs to be set. For more information, please refer to the [Google Designed For Families (DFF)](https://support.google.com/googleplay/android-developer/answer/9893335?hl=en&ref_topic=9877766)policy
  * Set the location where the earliest ad request is initiated, or both can be set (for example: access to IronSource incentives and interstitial screens, the type of loadAd request that is initiated first is set first)

TradPlus version| advertising platform  
---|---  
V8.7.0.1| Inmobi、ChartBoost、AdColony、IronSource、TapJoy  
  
Map<String, Object> mLocalExtras = new HashMap<>();

mLocalExtras.put("families_policy", true);

rewardAd.setCustomParams(mLocalExtras);

rewardAd.loadAd();

Copy

## Step 6、How to set LGPD#

> Lei Geral de Proteção de Dados (LGPD) is a comprehensive Brazilian data
> protection law, effective September 18, 2020, that provides individuals with
> broader data rights and increases compliance responsibilities for
> organizations. At its core, the LGPD is about giving Brazilian residents
> greater control over their personal data and giving national regulators new
> powers to impose hefty fines on organizations that violate the law, with
> rights and protections similar to those afforded to European residents by
> the GDPR.

  * Must be called before initializing TradPlus SDK
  * Only need to call in Brazil, do not set in non-Brazilian regions

Note| Method| Remark  
---|---|---  
Set LGPD level| `TradPlusSdk.setLGPDConsent(Context context, int consent)`|
Parameter 2: 0, device data is allowed to be reported; 1, device data is not
allowed to be reported  
Get LGPD rating| `TradPlusSdk.getLGPDConsent(Context context)`| Return value 0
means agree, 1 means disagree  
  
## Step 7、Google Content Rating#

  * V9.4.0.1 began to support
  * Called before requesting an ad, taking a rewarded video as an example:

//digital content tags all audiences

private String mAdContentRating =
RequestConfiguration.MAX_AD_CONTENT_RATING_G;

...

Map<String, Object> mLocalExtras = new HashMap<>();

mLocalExtras.put("max_ad_content_rating", mAdContentRating);

rewardAd.setCustomParams(mLocalExtras);

// Called before requesting an ad

rewardAd.loadAd();

Copy

  * digital content label

digital content label| illustrate  
---|---  
RequestConfiguration.MAX_AD_CONTENT_RATING_G| all audiences  
RequestConfiguration.MAX_AD_CONTENT_RATING_T| teenager  
RequestConfiguration.MAX_AD_CONTENT_RATING_MA| aldult  
RequestConfiguration.MAX_AD_CONTENT_RATING_PG| Need to be accompanied by
parents to watch  
  
  * Step 1 、Check the current region
  * Step 2、CCPA
  * Step 3、COPPA
  * Step 4、GDPR
    * Android platform settings GDPR
    * Unity3DAndroid platform settings GDPR
  * Step 5、How to set up DFF
  * Step 6、How to set LGPD
  * Step 7、Google Content Rating

