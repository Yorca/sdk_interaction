SDK name: AD(X)
Documentation:
[![](https://docs.adxcorp.kr/~gitbook/image?url=https%3A%2F%2F941224284-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
legacy-
files%2Fo%2Fspaces%252F-MKnpTl0mjoA9ICYmXj-%252Favatar-1624947515118.png%3Fgeneration%3D1624947515254063%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=64480dc1&sv=1)![](https://docs.adxcorp.kr/~gitbook/image?url=https%3A%2F%2F941224284-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
legacy-
files%2Fo%2Fspaces%252F-MKnpTl0mjoA9ICYmXj-%252Favatar-1624947515118.png%3Fgeneration%3D1624947515254063%26alt%3Dmedia&width=32&dpr=4&quality=100&sign=64480dc1&sv=1)ADX
Library](/)

More

SearchCtrl \+ K

  * [ADXLibrary](/)

  * Android

    * [Integrate](/android/integrate)

    * [SDK Integration](/android/sdk-integration)

      * [Initialize](/android/sdk-integration/initialize)

      * [Ad Formats](/android/sdk-integration/ad-formats)

        * [Banner Ad](/android/sdk-integration/ad-formats/banner-ad)

        * [Interstitial Ad](/android/sdk-integration/ad-formats/interstitial-ad)

        * [Native Ad](/android/sdk-integration/ad-formats/native-ad)

        * [Rewarded Ad](/android/sdk-integration/ad-formats/rewarded-ad)

          * [AD(X)](/android/sdk-integration/ad-formats/rewarded-ad/ad-x)

          * [AdMob](/android/sdk-integration/ad-formats/rewarded-ad/admob)

      * [Ad Error](/android/sdk-integration/ad-error)

      * [Sample Application](/android/sdk-integration/sample-application)

    * [Targeting Android 12](/android/targeting-android-12)

    * [Change log](/android/android-changelog)

  * iOS

    * [Integrate](/ios/integrate)

    * [SDK Integration](/ios/sdk-integration)

      * [Initialize](/ios/sdk-integration/initialize)

      * [Ad Formats](/ios/sdk-integration/ad-formats)

        * [Banner Ad](/ios/sdk-integration/ad-formats/banner-ad)

        * [Interstitial Ad](/ios/sdk-integration/ad-formats/interstitial-ad)

        * [Native Ad](/ios/sdk-integration/ad-formats/native-ad)

        * [Rewarded Ad](/ios/sdk-integration/ad-formats/rewarded-ad)

          * [AD(X)](/ios/sdk-integration/ad-formats/rewarded-ad/ad-x)

          * [AdMob](/ios/sdk-integration/ad-formats/rewarded-ad/admob)

      * [Ad Error](/ios/sdk-integration/ad-error)

      * [Sample Application](/ios/sdk-integration/sample-application)

    * [Supporting iOS 14](/ios/supporting-ios-14)

      * [App Tracking Transparency](/ios/supporting-ios-14/app-tracking-transparency)

      * [SKAdNetwork ID List](/ios/supporting-ios-14/skadnetwork-id-list)

    * [Change log](/ios/ios-changelog)

  * Unity

    * [Integrate](/unity/integrate)

    * [SDK Integration](/unity/sdk-integration)

      * [Initialize](/unity/sdk-integration/initialize)

      * [Ad Formats](/unity/sdk-integration/ad-formats)

        * [Banner Ad](/unity/sdk-integration/ad-formats/banner-ad)

        * [Interstitial Ad](/unity/sdk-integration/ad-formats/interstitial-ad)

        * [Rewarded Ad](/unity/sdk-integration/ad-formats/rewarded-ad)

          * [AD(X)](/unity/sdk-integration/ad-formats/rewarded-ad/ad-x)

          * [AdMob (ADX v2.4.0 미만)](/unity/sdk-integration/ad-formats/rewarded-ad/admob-adx-v2.4.0)

          * [AdMob (ADX v2.4.0 이상)](/unity/sdk-integration/ad-formats/rewarded-ad/admob-adx-v2.4.0-1)

      * [Ad Error](/unity/sdk-integration/ad-error)

      * [Sample Application](/unity/sdk-integration/sample-application)

    * [Change log](/unity/change-log)

  * Flutter

    * [Integrate](/flutter/integrate)

    * [SDK Integration](/flutter/sdk-integration)

      * [Initialize](/flutter/sdk-integration/initialize)

      * [Ad Formats](/flutter/sdk-integration/ad-formats)

        * [Banner Ad](/flutter/sdk-integration/ad-formats/banner-ad)

        * [Interstitial Ad](/flutter/sdk-integration/ad-formats/interstitial-ad)

        * [Rewarded Ad](/flutter/sdk-integration/ad-formats/rewarded-ad)

      * [Sample Application](/flutter/sdk-integration/sample-application)

    * [Change log](/flutter/change-log)

  * Appendix

    * [SSV Callback (Server-Side Verification)](/appendix/ssv-callback-server-side-verification)

    * [UMP (User Messaging Platform)](/appendix/ump-user-messaging-platform)

[Powered by
GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=-MKnpTl0mjoA9ICYmXj-)

# Initialize

##

0\. GDPR (General Data Protection Regulation)

GDPR은 유럽연합(이하 'EU')의 개인정보 보호 법령으로 서비스 제공자는 EU 사용자의 개인정보 또는 그에 준하는 정보에 대한 수집 및
활용에 대해 사용자에게 동의 여부를 확인받아야 합니다. GDPR 규정 준수 및 규정에 따른 광고네트워크 동작에 필요한 절차입니다.

##

1\. Initialize & GDPR Content UI

초기화 시 EU 사용자의 GDPR 동의 여부를 받아 처리할 수 있는 관련 기능을 제공합니다. Main Activity의
`onCreate`에서 광고 관련 코드를 요청하기 전에 초기화 함수를 호출합니다.

Android ADX SDK에는 사용자로부터 **GDPR** 동의를 받을 수 있는 기능이 포함되어 있습니다.

* * *

**2024년 1월 16일** 부터 IAB 유럽의 인증과 플랫폼 사업자의 **인증을 받은 동의 플랫폼(CMP)를 통해 GDPR 동의 관리를
처리해야 됨에 따라** , **Android ADX SDK 버전 2.5.0 이상부터, SDK 내부에서 자체적으로 제공되던 GDPR 동의
화면은 더 이상 지원되지 않으니, 애드몹 UMP (User Messaging Platform)를 통하여 GDPR 동의를 처리해야합니다.**

* * *

유럽 경제 지역 (European Economic Area)에서 Android 애플리케이션을 서비스하고 있거나, 또는 서비스할 계획이 있다면
**Android ADX SDK 버전 2.5.0 이상을 설치하고, 이 문서의**[**UMP (User Messaging
Platfom)**](/appendix/ump-user-messaging-platform#1.-gdpr)**이동하여 기술된 내용에 따라
설정하여 주십시오.**

  * `"<ADX_APP_ID>"`에 ADX에서 발급받은 **ADX App ID** 를 사용합니다.

  * **SDK 초기화는 앱 실행 시 한 번만 호출** 하여 주시고, **광고 요청은 초기화가 완료된 후** 에 이뤄져야 합니다.

    * `onCompleted`가 호출 된 후, 광고를 요청해야 합니다.

  * GdprType은 아래 항목 중 하나를 선택하여 입력합니다.

**GDPR 타입**| **설명**  
---|---  
POPUP_LOCATION| 지역에 따라 동의 팝업 호출 (EU 지역)  
POPUP_DEBUG| 지역 상관없이 동의 팝업 호출 테스트 (DEBUG)  
DIRECT_NOT_REQUIRED| 동의 여부가 필요없는 지역 (EU 외 지역)  
DIRECT_DENIED| 사용자가 개인정보 활용 및 수집 거부  
DIRECT_CONFIRM| 사용자가 개인정보 활용 및 수집 동의  
  
###

Case 1. EEA 사용자의 GDPR 동의 화면 제공

유럽 경제 지역 (European Economic Area) 사용자에게 동의 여부를 선택할 수 있도록 동의 화면을 제공합니다.

유럽 경제 지역 (European Economic Area) 사용자에게 동의 여부를 선택할 수 있는 기능이 애드몹 UMP (User
Messaging Platform)에 의해서 처리되며, 애드몹 UMP 기능은 Android ADX SDK 버전 2.5.0 이상에 포함되어
있습니다.

  * `ADXConfiguration`에서 GdprType을 `POPUP_LOCATION`로 설정하시면, 사용자의 접속 국가에 따라 EU 사용자는 GDPR 동의 Consent UI를 통해 동의 여부를 결정할 수 있습니다.

  * GdprType을 `POPUP_DEBUG`로 설정 시 접속 국가와 상관없이 Consent UI를 확인하실 수 있습니다.

**(주의사항)** `POPUP_LOCATION` 또는`POPUP_DEBUG` 의 경우 `initiailize` 의 `Context` 값으로
`Activity` 를 넣어주셔야 합니다. 그렇지 않은 경우 정상적으로 초기화되지 않습니다.

JavaKotlin

Copy

    
    
    // ADX 초기화 관련 설정
    ADXConfiguration adxConfiguration = new ADXConfiguration.Builder()
                            .setAppId("<ADX_APP_ID>")
                            .setGdprType(ADXConfiguration.GdprType.POPUP_LOCATION)
                            .setTestDeviceIds(Arrays.asList("")) // UMP Test Device
                            .build();
    
    ADXSdk.getInstance().initialize((Activity) this, adxConfiguration, new ADXSdk.OnInitializedListener() {
            @Override
            public void onCompleted(boolean result, ADXGDPR.ADXConsentState adxConsentState) {
                    // 광고 초기화 완료
            }
    });

Copy

    
    
    // ADX 초기화 관련 설정
    val adxConfiguration = ADXConfiguration.Builder()
        .setAppId("<ADX_APP_ID>")
        .setGdprType(ADXConfiguration.GdprType.POPUP_LOCATION)
        .setTestDeviceIds(mutableListOf("")) // UMP Test Device
        .build()
    
    ADXSdk.getInstance().initialize(this as Activity, adxConfiguration) { result, adxConsentState ->
        // 광고 초기화 완료
    }

애드몹 UMP의 GDPR 동의 화면을 테스트 목적으로 확인하려면, **아래 두 가지 설정이 필요합니다.**

1) 애드몹 대쉬보드 (https://apps.admob.com)로 이동한 다음에 아래 GDPR 메시지 작성 가이드 내용을 따라서 메시지
작성과 게시를 완료하십시오.
[https://support.google.com/admob/answer/10113207?hl=ko](https://support.google.com/admob/answer/10113207?hl=ko)

* * *

2) 로그 출력에서 아래의 기기 ID를 확인합니다. 이 식별자 문자열을 **ADXConfiguration** 객체 생성 시 사용하는
**setTestDeviceIds** 파라미터에 입력하고, **setGdprType** 파라미터에는 **POPUP_DEBUG** 를 입력하여
주십시오. Use new
ConsentDebugSettings.Builder().addTestDeviceHashedId("**33BE2250B43518CCDA7DE426D04EE231**
") to set this as a debug device.

![](https://docs.adxcorp.kr/~gitbook/image?url=https%3A%2F%2F941224284-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
x-
prod.appspot.com%2Fo%2Fspaces%252F-MKnpTl0mjoA9ICYmXj-%252Fuploads%252FP3x1wC02V28PouygLG3S%252Fump_gdpr.png%3Falt%3Dmedia%26token%3Db7f611df-
af25-4593-a060-3e2b7abc60e5&width=768&dpr=4&quality=100&sign=a4e6e746&sv=1)

<UMP GDPR 동의 화면>

###

Case 2. 직접 동의 여부 설정

유럽 경제 지역 (European Economic Area) 사용자가 없거나 앱 내에 회원가입이나 GDPR에서 정하는 개인정보에 준하는
정보를 수집하고 있으시다면 **한국에서 푸시알림 동의, 개인정보처리방침에 대해 동의절차를 진행하는 것과 같이 따로 직접 동의절차를 진행 및
처리** 해주셔야합니다.

  * EU 외 지역으로 동의 여부가 필요 없는 경우, `ADXConfiguration`에서 GdprType을 `DIRECT_NOT_REQUIRED`로 설정해주세요.

  * EU 지역으로 직접 동의 절차를 진행하시는 경우, 동의절차 결과에 따라 GdprType을 설정해주세요 .

    * 사용자가 개인정보 활용 및 수집 동의한 상태: `DIRECT_CONFIRM`

    * 사용자가 개인정보 활용 및 수집 거부한 상태: `DIRECT_DENIED`

JavaKotlin

Copy

    
    
    // ADX 초기화 관련 설정
    ADXConfiguration adxConfiguration = new ADXConfiguration.Builder()
                            .setAppId("<ADX_APP_ID>")
                            .setGdprType(ADXConfiguration.GdprType.DIRECT_CONFIRM)
                            .build();
    
    ADXSdk.getInstance().initialize((Activity) this, adxConfiguration, new ADXSdk.OnInitializedListener() {
            @Override
            public void onCompleted(boolean result, ADXGDPR.ADXConsentState adxConsentState) {
                    // 광고 초기화 완료
            }
    });

Copy

    
    
    // ADX 초기화 관련 설정
    val adxConfiguration = ADXConfiguration.Builder()
        .setAppId("<ADX_APP_ID>")
        .setGdprType(ADXConfiguration.GdprType.DIRECT_CONFIRM)
        .build()
    
    ADXSdk.getInstance().initialize(this as Activity, adxConfiguration) { result, adxConsentState ->
        // 광고 초기화 완료
    }

##

2\. Native Ad 초기화

####

동일한 Activity에서 초기화 함수와 Native Ad 함수를 호출하는 경우

초기화 함수를 호출하기 전에 `AdxNativeAdFactory`의 `init()`과 `setAdxViewBinder()` 를 초기화
함수보다 먼저 호출해야합니다. 초기화 함수 호출 후 `OnInitializedListener`의 `onCompleted` 내에서
`AdxNativeAdFactory.preloadAd()`를 호출해야**** 합니다.

JavaKotlin

Copy

    
    
    AdxNativeAdFactory.init(this);
    
    AdxNativeAdFactory.setAdxViewBinder("<NATIVE_AD_UNIT_ID>", new AdxViewBinder.Builder(R.layout.layout_media_native_ad)
            .mediaViewContainerId(R.id.mediaContainerId)
            .iconImageId(R.id.adIconId)
            .titleId(R.id.titleId)
            .adChoiceContainerId(R.id.adChoicesContainerId)
            .callToActionId(R.id.callToActionId)
            .build());

Copy

    
    
    AdxNativeAdFactory.init(this)
    
    AdxNativeAdFactory.setAdxViewBinder("<NATIVE_AD_UNIT_ID>", AdxViewBinder.Builder(R.layout.layout_media_native_ad)
            .mediaViewContainerId(R.id.mediaContainerId)
            .iconImageId(R.id.adIconId)
            .titleId(R.id.titleId)
            .adChoiceContainerId(R.id.adChoicesContainerId)
            .callToActionId(R.id.callToActionId)
            .build()

Native Ad 구현 방법은 [해당 페이지](/android/sdk-integration/ad-formats/native-ad)를
참고해주세요.

##

3\. ConsentState

GDPR 동의 여부에 대해 4개의 상태값을 가집니다.

**상태**| **설명**  
---|---  
ADXConsentStateUnknown| 동의 여부가 존재하지 않는 사용자로 호출 상태로 개인화 광고가 노출되지 않습니다.  
ADXConsentStateNotRequired| 동의 여부가 필요없는 지역 (EU 외 지역)개인화 광고가 노출됩니다.  
ADXConsentStateDenied| 사용자가 개인정보 활용 및 수집을 거부한 상태 개인화 광고가 노출되지 않습니다.  
ADXConsentStateConfirm| 사용자가 개인정보 활용 및 수집을 동의한 상태개인화 광고가 노출됩니다.  
  
동의 여부를 확인/변경 하시는 경우 `ADXGdprManager`의 아래 함수를 사용하여 주시기 바랍니다.

JavaKotlin

Copy

    
    
    // ADXGdprManager에 설정된 사용자의 동의 정보를 확인하실 수 있습니다.
    ADXGdprManager.getResultGDPR(this);
    
    // 직접 동의 여부를 변경합니다.
    ADXGdprManager.saveResultGDPR(this, ADXConsentState);

Copy

    
    
    // ADXGdprManager에 설정된 사용자의 동의 정보를 확인하실 수 있습니다.
    ADXGdprManager.getResultGDPR(this)
    
    // 직접 동의 여부를 변경합니다.
    ADXGdprManager.saveResultGDPR(this, ADXConsentState)

##

4\. Privacy Policy

AD(x)의 Privacy Policy 문서 URL은 `ADXGDPR`의 `getPrivacyURL()`을 호출하여 사용하실 수 있습니다.

JavaKotlin

Copy

    
    
    ADXGdprManager.getPrivacyURL();

Copy

    
    
    ADXGdprManager.getPrivacyURL()

##

5\. 디버깅 로그 활성화

QA 진행 시 연동 및 미디에이션 정상 동작 확인을 위해 초기화 함수를 호출하기 전에 아래와 같이 추가되어야 합니다.

JavaKotlin

Copy

    
    
    ADXLogUtil.setLogEnable(true);

Copy

    
    
    ADXLogUtil.setLogEnable(true)

[PreviousSDK Integration](/android/sdk-integration)[NextAd
Formats](/android/sdk-integration/ad-formats)

Last updated 4 months ago

On this page

  * 0\. GDPR (General Data Protection Regulation)
  * 1\. Initialize & GDPR Content UI
  * Case 1. EEA 사용자의 GDPR 동의 화면 제공 
  * Case 2. 직접 동의 여부 설정 
  * 2\. Native Ad 초기화 
  * 3\. ConsentState
  * 4\. Privacy Policy
  * 5\. 디버깅 로그 활성화

Was this helpful?

