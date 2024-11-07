SDK name: Vpon
Documentation:
Skip to main content

[

  * Android](/android/) [
  * iOS](/ios/) [
  * Web](/web/) [
  * Flutter](/flutter/) [
  * English ](/android/custom-request-params/) [
  * 繁體中文 ](/zh-tw/android/custom-request-params/) [
  * 简体中文 ](/zh-cn/android/custom-request-params/)

[ ![](/assets/img/vpon-logo-new.png) ](/)

  * [Android](/android/)
  * [iOS](/ios/)
  * [Web](/web/)
  * [Flutter](/flutter/)
  * Language 
    * [English](/android/custom-request-params/)
    * [繁體中文](/zh-tw/android/custom-request-params/)
    * [简体中文](/zh-cn/android/custom-request-params/)

# Android - Custom Request Params

Optimizing your ads performance from advanced skills here.

Android Integration

  * [Getting Started](/android)
  * [Registration](/android/registration)
  * [Integration Guide](/android/integration-guide)
Ad Type Choices

  * [Banner Ad](/android/banner)
  * [Interstitial Ad](/android/interstitial)
  * [Native Ad](/android/native)
Advanced Setting

  * [Mediation](/android/mediation)
  * [Custom Request Params](/android/custom-request-params)
MISC

  * [Latest News](/android/latest-news)
  * [Change Log](/android/changelog)
  * [App Privacy Details](/android/app-privacy-details)
  * [FAQ](/android/faq)

Android Integration

* [Getting Started](/android)
* [Registration](/android/registration)
* [Integration Guide](/android/integration-guide)

Ad Type Choices

* [Banner Ad](/android/banner)
* [Interstitial Ad](/android/interstitial)
* [Native Ad](/android/native)

Advanced Setting

* [Mediation](/android/mediation)
* [Custom Request Params](/android/custom-request-params)

MISC

* [Latest News](/android/latest-news)
* [Change Log](/android/changelog)
* [App Privacy Details](/android/app-privacy-details)
* [FAQ](/android/faq)

# Custom Ad Request Parameters

* * *

Add the optional parameters below when setting up VpadnAdRequest to make Vpon
deliver more ads precisely.

    
    
    VponAdRequest.Builder builder = new VponAdRequest.Builder();
    
    builder.setAutoRefresh(boolean);
    // Only available for Banner Ad, will auto refresh ad if set true
    builder.addTestDevice(String);
    // Set your test device's GAID here if you're trying to get Vpon test ad
    
    builder.setGender(VponAdRequest.Gender.UNSPECIFIED);
    // Set user's gender if available
    builder.setBirthday(Date);
    // Set user's birthday if available
    builder.setLocation(Location);
    // Set user's location if available
    
    builder.setMaxAdContentRating(String);
    // To set up the maximum content rating filter
    builder.setTagForUnderAgeOfConsent(-1);
    // To set up if the ads will be displayed only to the specific ages of audience
    builder.tagForChildDirectedTreatment(-1);
    // To set up if the ads will be displayed to childern specific
    
    builder.addKeyword(String);
    builder.addKeywords(Set<String>);
    

# How To Send Content Data To Vpon

* * *

You can use `setContentUrl` and `setContentData` to send content information
to Vpon via SDK.

> **Note:** `setContentUrl` and `setContentData` only available in Vpon SDK
> v5.1.1 and above.
    
    
    VponAdRequest.Builder builder = new VponAdRequest.Builder();
    
    HashMap<String, Object> contentData = new HashMap<>();
    contentData.put("key1", "Vpon");
    contentData.put("key2", 1.2);
    contentData.put("key3", true);
    
    builder.setContentData(contentData);
    builder.setContentUrl("https://www.vpon.com/zh-hant/");
    

  
  

  * Document framework powered by [Bt-docs](http://bt-docs.liaohuqiu.net)
  * *
  * Hosted by [Github Pages](https://pages.github.com)

We would like to use third party cookies and scripts to improve the
functionality of this website.Approve[More
info](https://www.vpon.com/en/privacy-policy/)

