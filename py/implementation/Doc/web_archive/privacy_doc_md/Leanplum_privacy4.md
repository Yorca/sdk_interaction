Jump to Content

[![Leanplum's user guides and developer
documentation.](https://files.readme.io/c88e191-small-
Leanplum_Logo_White.png)](https://www.leanplum.com)[Home](/)[User
Guide](/docs)[Developer Guide](/reference)[Changelog](/changelog)

[ __Home](/)[ __User Guide](/docs)[ __Developer Guide](/reference)[
__Changelog](/changelog)

* * *

[Home](/)[User Guide](/docs)[Developer
Guide](/reference)[Changelog](/changelog)[Log
In](/login?redirect_uri=/reference/android-location-services)[![Leanplum's
user guides and developer
documentation.](https://files.readme.io/c88e191-small-
Leanplum_Logo_White.png)](https://www.leanplum.com)

 __Developer Guide

[Log In](/login?redirect_uri=/reference/android-location-services)

Android location services

Search

JUMP TO

## Quick Start Guides

  * [Overview](/reference/overview)
  * [iOS](/reference/ios-setup)
  * [Android](/reference/android-setup)
  * [Unity](/reference/unity-setup)
  * [JavaScript](/reference/javascript-setup)
  * [React Native](/reference/react-native-setup)
  * [Unreal](/reference/unreal)

## SDK Documentation

  * [ __How the Leanplum SDK Works](/reference/how-the-leanplum-sdk-works)
    * [ Tracking Sessions](/reference/sessions)
    * [Syncing with Leanplum mid-session](/reference/syncing-with-leanplum-mid-session)
    * [Callbacks](/reference/callbacks)
    * [iOS Binary Size](/reference/ios-binary-size)
  * [ __Tracking User Information](/reference/user-and-device-tracking)
    * [ User IDs](/reference/user-ids)
    * [Device IDs](/reference/device-ids)
    * [User attributes](/reference/user-attributes)
    * [Handle same User login on different devices](/reference/handle-same-user-login-on-different-devices)
  * [ __Tracking User Behavior](/reference/events)
    * [ Tracking Monetization Events](/reference/tracking-monetization-events)
  * [ __In-app messaging](/reference/in-app-messaging)
    * [ Unity In-App messages](/reference/unity-in-app-messages)
    * [Web In-App messages](/reference/web-in-app-messages)
    * [IAM Handlers](/reference/iam-handlers)
    * [Custom Templates](/reference/customizing-in-app-message-templates)
    * [Custom Delivery Deferral](/reference/custom-delivery-deferral)
    * [Android: Add dialog customizer](/reference/android-add-dialog-customizer)
  * [ __Push notifications](/reference/push-notifications)
    * [ iOS push notifications](/reference/ios-push-notifications)
    * [Android push notifications](/reference/android-push-notifications)
    * [Unity push notifications](/reference/unity-push-notifications)
    * [JavaScript push notifications](/reference/javascript-push-notifications)
    * [ReactNative push notifications](/reference/reactnative-push-notifications)
    * [Xiaomi MiPush integration](/reference/xiaomi-mipush-integration)
    * [Huawei Push Kit integration](/reference/huawei-push-kit-integration)
  * [App inbox](/reference/app-inbox)
  * [ __Variables](/reference/defining-variables)
    * [ Variable Implementation](/reference/variable-types)
    * [Modeling structured data](/reference/modeling-structured-data)
    * [Secure Variables](/reference/secure-variables)
  * [ __Geofencing and location-based messaging](/reference/geofencing-and-location-based-messaging)
    * [ iOS location services](/reference/ios-location-services)
    * [Android location services](/reference/android-location-services)
    * [React Native location services](/reference/react-native-location-services)
  * [How to integrate external Attribution services (App setup)](/reference/how-to-integrate-external-attribution-services-app-setup)

## API

  * [ __API Introduction](/reference/api-introduction)
    * [ Making requests](/reference/making-requests)
    * [Authentication](/reference/authentication)
    * [Selecting a user](/reference/selecting-a-user)
    * [Responses](/reference/responses)
    * [Billing](/reference/billing)
    * [Batching requests with multi](/reference/batching-requests)
    * [Reduce billable requests](/reference/reduce-billable-requests)
    * [Debugging](/reference/debugging)
  * [API methods](/reference/api-methods)
  * [ __User Behavior](/reference/user-behavior)
    * [ advancepost](/reference/post_api-action-advance)
    * [pauseStatepost](/reference/post_api-action-pausestate)
    * [resumeStatepost](/reference/post_api-action-resumestate)
    * [pauseSessionpost](/reference/post_api-action-pausesession)
    * [resumeSessionpost](/reference/post_api-action-resumesession)
    * [heartbeatpost](/reference/post_api-action-heartbeat)
    * [startpost](/reference/post_api-action-start)
    * [stoppost](/reference/post_api-action-stop)
    * [trackpost](/reference/post_api-action-track)
  * [ __User Information](/reference/user-information)
    * [ setUserAttributespost](/reference/post_api-action-setuserattributes)
    * [setDeviceAttributespost](/reference/post_api-action-setdeviceattributes)
    * [setTrafficSourceInfopost](/reference/post_api-action-settrafficsourceinfo)
    * [registerDevicepost](/reference/post_api-action-registerdevice)
    * [deleteUserpost](/reference/post_api-action-deleteuser)
    * [blockpost](/reference/post_api-action-block)
    * [unblockpost](/reference/post_api-action-unblock)
  * [ __Messages](/reference/messages)
    * [ getMessageget](/reference/get_api-action-getmessage)
    * [getMessagesget](/reference/get_api-action-getmessages)
    * [getUnsubscribeCategoriesget](/reference/get_api-action-getunsubscribecategories)
    * [sendMessagepost](/reference/post_api-action-sendmessage)
    * [addAndroidNotificationChannelpost](/reference/post_api-action-addandroidnotificationchannel)
    * [getAndroidNotificationChannelsget](/reference/get_api-action-getandroidnotificationchannels)
    * [deleteAndroidNotificationChannelpost](/reference/post_api-action-deleteandroidnotificationchannel)
  * [ __A/B Tests](/reference/ab-tests)
    * [ getAbTestget](/reference/get_api-action-getabtest)
    * [getAbTestsget](/reference/get_api-action-getabtests)
    * [getVariantget](/reference/get_api-action-getvariant)
  * [ __Files and Variables](/reference/files-and-variables)
    * [ getVarsget](/reference/get_api-action-getvars)
    * [setVarspost](/reference/post_api-action-setvars)
    * [deleteVarspost](/reference/post_api-action-deletevars)
    * [downloadFileget](/reference/get_api-action-downloadfile)
    * [uploadFilepost](/reference/post_api-action-uploadfile)
  * [ __Export Data](/reference/export-data)
    * [ addPostbackpost](/reference/post_api-action-addpostback)
    * [listPostbacksget](/reference/get_api-action-listpostbacks)
    * [deletePostbackpost](/reference/post_api-action-deletepostback)
    * [exportDataget](/reference/get_api-action-exportdata)
    * [exportData schema (csv, S3 bucket)](/reference/exportdata-schema-csv-s3-bucket)
    * [exportReportget](/reference/get_api-action-exportreport)
    * [exportData schema (JSON)](/reference/exportdata-schema-json)
    * [exportUserget](/reference/get_api-action-exportuser)
    * [exportUsersget](/reference/get_api-action-exportusers)
    * [getExportResultsget](/reference/get_api-action-getexportresults)
  * [ __Import Data](/reference/import-data)
    * [ multi (CSV)post](/reference/post_api-action-multi)
    * [multi (JSON)](/reference/multi-json)
    * [getMultiResultsget](/reference/get_api-action-getmultiresults)
  * [ __Campaigns](/reference/post_api-action-startcampaign)
    * [ startCampaignpost](/reference/post_api-action-startcampaign)
  * [API Limits](/reference/api-limits)
  * [ __API guides](/reference/creating-new-users-with-our-api)
    * [ Creating new users with our API](/reference/creating-new-users-with-our-api)
    * [Sending messages manually via the API](/reference/sending-messages-manually-via-the-api)
    * [Setting attribution source data via the API](/reference/setting-attribution-source-data-via-the-api)
    * [Exporting bookmarked reports](/reference/exporting-bookmarked-reports)
    * [Exporting Leanplum in-app message events to other analytics providers](/reference/exporting-leanplum-in-app-message-events-to-other-analytics-providers)
    * [Exporting Leanplum A/B test info to other analytics providers](/reference/exporting-leanplum-ab-test-info-to-other-analytics-providers)
    * [Export Raw Data via Python Scripts [Sample: API]](/reference/export-raw-data-via-python-scripts-sample-api)
    * [Accessing content via the API](/reference/accessing-content-via-the-api)
    * [Tracking analytics data via API](/reference/tracking-analytics-data-via-api)
    * [Interpreting metrics in raw data export files](/reference/interpreting-metrics-in-raw-data-export-files)
    * [Calculate DAU with the raw data via Python](/reference/calculate-dau-with-the-raw-data-via-python)
  * [GDPR & CCPA overview](/reference/gdpr-overview)

JUMP TO

## Quick Start Guides

  * [Overview](/reference/overview)
  * [iOS](/reference/ios-setup)
  * [Android](/reference/android-setup)
  * [Unity](/reference/unity-setup)
  * [JavaScript](/reference/javascript-setup)
  * [React Native](/reference/react-native-setup)
  * [Unreal](/reference/unreal)

## SDK Documentation

  * [ __How the Leanplum SDK Works](/reference/how-the-leanplum-sdk-works)
    * [ Tracking Sessions](/reference/sessions)
    * [Syncing with Leanplum mid-session](/reference/syncing-with-leanplum-mid-session)
    * [Callbacks](/reference/callbacks)
    * [iOS Binary Size](/reference/ios-binary-size)
  * [ __Tracking User Information](/reference/user-and-device-tracking)
    * [ User IDs](/reference/user-ids)
    * [Device IDs](/reference/device-ids)
    * [User attributes](/reference/user-attributes)
    * [Handle same User login on different devices](/reference/handle-same-user-login-on-different-devices)
  * [ __Tracking User Behavior](/reference/events)
    * [ Tracking Monetization Events](/reference/tracking-monetization-events)
  * [ __In-app messaging](/reference/in-app-messaging)
    * [ Unity In-App messages](/reference/unity-in-app-messages)
    * [Web In-App messages](/reference/web-in-app-messages)
    * [IAM Handlers](/reference/iam-handlers)
    * [Custom Templates](/reference/customizing-in-app-message-templates)
    * [Custom Delivery Deferral](/reference/custom-delivery-deferral)
    * [Android: Add dialog customizer](/reference/android-add-dialog-customizer)
  * [ __Push notifications](/reference/push-notifications)
    * [ iOS push notifications](/reference/ios-push-notifications)
    * [Android push notifications](/reference/android-push-notifications)
    * [Unity push notifications](/reference/unity-push-notifications)
    * [JavaScript push notifications](/reference/javascript-push-notifications)
    * [ReactNative push notifications](/reference/reactnative-push-notifications)
    * [Xiaomi MiPush integration](/reference/xiaomi-mipush-integration)
    * [Huawei Push Kit integration](/reference/huawei-push-kit-integration)
  * [App inbox](/reference/app-inbox)
  * [ __Variables](/reference/defining-variables)
    * [ Variable Implementation](/reference/variable-types)
    * [Modeling structured data](/reference/modeling-structured-data)
    * [Secure Variables](/reference/secure-variables)
  * [ __Geofencing and location-based messaging](/reference/geofencing-and-location-based-messaging)
    * [ iOS location services](/reference/ios-location-services)
    * [Android location services](/reference/android-location-services)
    * [React Native location services](/reference/react-native-location-services)
  * [How to integrate external Attribution services (App setup)](/reference/how-to-integrate-external-attribution-services-app-setup)

## API

  * [ __API Introduction](/reference/api-introduction)
    * [ Making requests](/reference/making-requests)
    * [Authentication](/reference/authentication)
    * [Selecting a user](/reference/selecting-a-user)
    * [Responses](/reference/responses)
    * [Billing](/reference/billing)
    * [Batching requests with multi](/reference/batching-requests)
    * [Reduce billable requests](/reference/reduce-billable-requests)
    * [Debugging](/reference/debugging)
  * [API methods](/reference/api-methods)
  * [ __User Behavior](/reference/user-behavior)
    * [ advancepost](/reference/post_api-action-advance)
    * [pauseStatepost](/reference/post_api-action-pausestate)
    * [resumeStatepost](/reference/post_api-action-resumestate)
    * [pauseSessionpost](/reference/post_api-action-pausesession)
    * [resumeSessionpost](/reference/post_api-action-resumesession)
    * [heartbeatpost](/reference/post_api-action-heartbeat)
    * [startpost](/reference/post_api-action-start)
    * [stoppost](/reference/post_api-action-stop)
    * [trackpost](/reference/post_api-action-track)
  * [ __User Information](/reference/user-information)
    * [ setUserAttributespost](/reference/post_api-action-setuserattributes)
    * [setDeviceAttributespost](/reference/post_api-action-setdeviceattributes)
    * [setTrafficSourceInfopost](/reference/post_api-action-settrafficsourceinfo)
    * [registerDevicepost](/reference/post_api-action-registerdevice)
    * [deleteUserpost](/reference/post_api-action-deleteuser)
    * [blockpost](/reference/post_api-action-block)
    * [unblockpost](/reference/post_api-action-unblock)
  * [ __Messages](/reference/messages)
    * [ getMessageget](/reference/get_api-action-getmessage)
    * [getMessagesget](/reference/get_api-action-getmessages)
    * [getUnsubscribeCategoriesget](/reference/get_api-action-getunsubscribecategories)
    * [sendMessagepost](/reference/post_api-action-sendmessage)
    * [addAndroidNotificationChannelpost](/reference/post_api-action-addandroidnotificationchannel)
    * [getAndroidNotificationChannelsget](/reference/get_api-action-getandroidnotificationchannels)
    * [deleteAndroidNotificationChannelpost](/reference/post_api-action-deleteandroidnotificationchannel)
  * [ __A/B Tests](/reference/ab-tests)
    * [ getAbTestget](/reference/get_api-action-getabtest)
    * [getAbTestsget](/reference/get_api-action-getabtests)
    * [getVariantget](/reference/get_api-action-getvariant)
  * [ __Files and Variables](/reference/files-and-variables)
    * [ getVarsget](/reference/get_api-action-getvars)
    * [setVarspost](/reference/post_api-action-setvars)
    * [deleteVarspost](/reference/post_api-action-deletevars)
    * [downloadFileget](/reference/get_api-action-downloadfile)
    * [uploadFilepost](/reference/post_api-action-uploadfile)
  * [ __Export Data](/reference/export-data)
    * [ addPostbackpost](/reference/post_api-action-addpostback)
    * [listPostbacksget](/reference/get_api-action-listpostbacks)
    * [deletePostbackpost](/reference/post_api-action-deletepostback)
    * [exportDataget](/reference/get_api-action-exportdata)
    * [exportData schema (csv, S3 bucket)](/reference/exportdata-schema-csv-s3-bucket)
    * [exportReportget](/reference/get_api-action-exportreport)
    * [exportData schema (JSON)](/reference/exportdata-schema-json)
    * [exportUserget](/reference/get_api-action-exportuser)
    * [exportUsersget](/reference/get_api-action-exportusers)
    * [getExportResultsget](/reference/get_api-action-getexportresults)
  * [ __Import Data](/reference/import-data)
    * [ multi (CSV)post](/reference/post_api-action-multi)
    * [multi (JSON)](/reference/multi-json)
    * [getMultiResultsget](/reference/get_api-action-getmultiresults)
  * [ __Campaigns](/reference/post_api-action-startcampaign)
    * [ startCampaignpost](/reference/post_api-action-startcampaign)
  * [API Limits](/reference/api-limits)
  * [ __API guides](/reference/creating-new-users-with-our-api)
    * [ Creating new users with our API](/reference/creating-new-users-with-our-api)
    * [Sending messages manually via the API](/reference/sending-messages-manually-via-the-api)
    * [Setting attribution source data via the API](/reference/setting-attribution-source-data-via-the-api)
    * [Exporting bookmarked reports](/reference/exporting-bookmarked-reports)
    * [Exporting Leanplum in-app message events to other analytics providers](/reference/exporting-leanplum-in-app-message-events-to-other-analytics-providers)
    * [Exporting Leanplum A/B test info to other analytics providers](/reference/exporting-leanplum-ab-test-info-to-other-analytics-providers)
    * [Export Raw Data via Python Scripts [Sample: API]](/reference/export-raw-data-via-python-scripts-sample-api)
    * [Accessing content via the API](/reference/accessing-content-via-the-api)
    * [Tracking analytics data via API](/reference/tracking-analytics-data-via-api)
    * [Interpreting metrics in raw data export files](/reference/interpreting-metrics-in-raw-data-export-files)
    * [Calculate DAU with the raw data via Python](/reference/calculate-dau-with-the-raw-data-via-python)
  * [GDPR & CCPA overview](/reference/gdpr-overview)

# Android location services

Setting up geolocation regions and location-based messaging in Leanplum

In our Android SDK, we will automatically track the GPS/cell-based location if
its available to your app.

##

Set up location-based messaging

To use geofence regions to trigger messages and push notifications in your
app, you must add a few keys in your `AndroidManifest.xml` file as shown
below:

  1. Add the permission `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>` (Required for geofencing)
  2. Link the Google Play services library to your project and add the metadata in the application tag. `<meta-data android:name="com.google.android.gms.version" android:value="@integer/google_play_services_version" />` (Required for geofencing)

##

Other Use Cases of Leanplum Location

###

Disable location collection

If you do not want to send GPS/Cell location to Leanplum, you can call
`disableLocationCollection` before` start`.

`Leanplum.disableLocationCollection();`

###

Manually set user location

Our SDK allows you to manually set the user location by calling
`setDeviceLocation` with two arguments (see below) after calling `start`. If
you manually set the location, you will also need to call
`disableLocationCollection` before setting the location.

Java

    
    
    setDeviceLocation(location, type);
    

Argument| Type| Description  
---|---|---  
location| android.location.Location| The location object representing the
user's current location.  
type| LeanplumLocationAccuracyType| The type of geolocation. Either CELL
(default) or GPS (more precise).  
  
> ## 📘
>
> Due to a limitation with Android, you can only have 100 regions active for
> your app at any given time. Leanplum optimizes usage by not monitoring
> regions for messaging campaigns that don't target particular users.

  * __Table of Contents
  *     * Set up location-based messaging
    * Other Use Cases of Leanplum Location
      * Disable location collection
      * Manually set user location

