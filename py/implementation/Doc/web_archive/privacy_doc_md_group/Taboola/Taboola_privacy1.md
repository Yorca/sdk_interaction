Jump to Content

[![Taboola Mobile SDK](https://files.readme.io/d68bfa3-small-7839e39-small-
dev-center-
logo.png)](https://developers.taboola.com/)[Android](https://developers.taboola.com/taboolasdk/v3/docs/android-
sdk-3x-classic-first-
steps)[iOS](https://developers.taboola.com/taboolasdk/v3/docs/ios-
sdk-3x-classic-first-
steps)[Announcements](https://sdk.taboola.com/taboolasdk/blog)[Support
Forum](https://sdk.taboola.com/taboolasdk/discuss)

[ __SDK Documentation](/taboolasdk/v2/docs)[
__Recipes](/taboolasdk/v2/recipes)[ __Announcements](/taboolasdk/v2/changelog)
Taboola Backstage APITaboola Mobile SDKTaboola Recommendations APITaboola Web
Integrationsv2v3v4

* * *

[Android](https://developers.taboola.com/taboolasdk/v3/docs/android-
sdk-3x-classic-first-
steps)[iOS](https://developers.taboola.com/taboolasdk/v3/docs/ios-
sdk-3x-classic-first-
steps)[Announcements](https://sdk.taboola.com/taboolasdk/blog)[Support
Forum](https://sdk.taboola.com/taboolasdk/discuss)[![Taboola Mobile
SDK](https://files.readme.io/d68bfa3-small-7839e39-small-dev-center-
logo.png)](https://developers.taboola.com/)

 __SDK Documentation

Taboola Mobile SDK

v2 __

CCPA CCPA

Search

## Android SDK

  * [Getting Started with the Android SDK](/taboolasdk/v2/docs/taboola-android-sdk-install)
  * [ __Taboola Widget](/taboolasdk/v2/docs/taboola-widget-android-sdk)
    * [ Widget via Native](/taboolasdk/v2/docs/taboola-android-sdk-widget-via-native)
    * [Widget via JS](/taboolasdk/v2/docs/taboola-android-sdk-widget-via-js)
  * [ __Taboola Feed](/taboolasdk/v2/docs/taboola-feed-android-sdk)
    * [ Feed via Native](/taboolasdk/v2/docs/taboola-android-sdk-feed-via-native)
    * [Feed via JS](/taboolasdk/v2/docs/taboola-android-sdk-feed-via-js)
  * [Integration Verifier (debug mode)](/taboolasdk/v2/docs/android-sdk-integration-verifier)
  * [SDK Reference](/taboolasdk/v2/docs/taboola-android-sdk-reference)
  * [GDPR](/taboolasdk/v2/docs/android-sdk-gdpr)
  * [CCPA](/taboolasdk/v2/docs/taboola-android-sdk-ccpa)
  * [app-ads.txt](/taboolasdk/v2/docs/app-adstxt-android)
  * [Troubleshooting](/taboolasdk/v2/docs/android-troubleshooting)
  * [Changelog](/taboolasdk/v2/docs/taboola-android-sdk-changelog)
  * [License](/taboolasdk/v2/docs/taboola-android-sdk-license)
  * [Taboola Android SDK Plus 2.0 (Notifications)](/taboolasdk/v2/docs/taboola-android-sdk-plus-20-notifications)

## IOS SDK

  * [Getting Started with the iOS SDK](/taboolasdk/v2/docs/taboola-ios-sdk-install)
  * [ __Taboola Widget](/taboolasdk/v2/docs/taboola-widget-ios-sdk)
    * [ Widget via Native](/taboolasdk/v2/docs/taboola-ios-sdk-widget-via-native)
    * [Widget via JS](/taboolasdk/v2/docs/taboola-ios-sdk-widget-via-js)
  * [ __Taboola Feed](/taboolasdk/v2/docs/taboola-feed-ios-sdk)
    * [ Feed via Native](/taboolasdk/v2/docs/taboola-ios-sdk-feed-via-native)
    * [Feed via JS](/taboolasdk/v2/docs/taboola-ios-sdk-feed-via-js)
  * [SDK Reference](/taboolasdk/v2/docs/taboola-ios-sdk-reference)
  * [GDPR](/taboolasdk/v2/docs/ios-sdk-gdpr)
  * [CCPA](/taboolasdk/v2/docs/taboola-ios-sdk-ccpa)
  * [app-ads.txt](/taboolasdk/v2/docs/app-adstxt-ios)
  * [Changelog](/taboolasdk/v2/docs/taboola-ios-sdk-changelog)
  * [License](/taboolasdk/v2/docs/taboola-ios-sdk-license)

## Plugins

  * [ __React native](/taboolasdk/v2/docs/taboola-react-native-plugin)
    * [ app-ads.txt](/taboolasdk/v2/docs/taboola-react-native-app-adstxt)
    * [Changelog](/taboolasdk/v2/docs/taboola-react-native-changelog)
    * [License](/taboolasdk/v2/docs/taboola-react-native-license)
  * [Flutter (Beta)__](https://developers.taboola.com/taboolasdk/docs/sdk-3x-flutter)

# CCPA

Taboola Android SDK and the CCPA

[ __Suggest Edits](/taboolasdk/v2/edit/taboola-android-sdk-ccpa)

On January 1st, 2020, the CCPA (California Consumer Privacy Act) will come
into effect. The CCPA introduces a six months compliance grace period for
publishers, making forcible from July 1st, 2020. Taboola takes considerable
efforts to ensure that its SDK complies with the CCPA privacy practices, CCPA
data protection instructions, and the industry's best practices to support it.

##

Working with the IAB CCPA Framework

Taboola added support for the IAB CCPA Framework ("IABUSPrivacy_String") in
Android SDK version 2.4.0. Please make sure you are using this SDK version or
above.

##

Passing CCPA status directly to Taboola SDK

It is possible to forward the CCPA "Do Not Sell" (dns) status to Taboola SDK
on each time the widget/feed is initialized using a dedicated flag - `cdns`
The value (in string format) should be passed on each SDK session.

  * `true` \- CCPA applies, and the end-user didn't provide agreement to use the personal data per CCPA regulations (Do not sell is true)
  * `false` \- CCPA applies, and the end-user provide agreement to use the personal data per CCPA regulations (Do not sell is false)
  * `none` \- CCPA does not apply (the default status)

By default, the value of this flag is set to none - the end-user is not CCPA
subject, allowing Taboola to use the user's data. It is recommended to place
these lines alongside the other settings, such as publisher name, etc

Feed/Widget via Native (SDK Standard)

    
    
    //Setting taboolaWidget object
    taboolaWidget.setPublisher("<publisher-as-supplied-by-taboola>")
      .setMode("<mode-as-supplied-by-taboola>")
      .setPlacement("<placement-as-supplied-by-taboola>")
      .setPageUrl("<public-web-url-which-reflects-the-current-content>")
      .setPageType("<my-page-type>")
      .taboolaWidget.setTargetType("<my-target-type>");
     
    HashMap<String, String> extraProperties = new HashMap<>();
    extraProperties.put("cdns","false");
    taboolaWidget.setExtraProperties(extraProperties);
    

Feed/Widget via JS (SDK JS)

    
    
    <!-- in the body tag add user_opt_out to the JS tag -->
    <div id="container-id"></div>
    <script type="text/javascript">
       window._taboola = window._taboola || [];
       _taboola.push({mode: "mode-name",
       	container: "container-id",
       	placement: "Placement Name",
            cdns: "false", 
       	target_type: 'mix'});
       _taboola["mobile"] = window._taboola["mobile"] || [];
       _taboola["mobile"].push({
       publisher:"publisher-id-goes-here"
       });
    </script>
    

__Updated over 4 years ago

* * *

  * __Table of Contents
  *     * Working with the IAB CCPA Framework
    * Passing CCPA status directly to Taboola SDK

