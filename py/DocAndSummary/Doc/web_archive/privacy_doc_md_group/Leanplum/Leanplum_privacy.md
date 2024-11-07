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
In](/login?redirect_uri=/reference/user-ids)[![Leanplum's user guides and
developer documentation.](https://files.readme.io/c88e191-small-
Leanplum_Logo_White.png)](https://www.leanplum.com)

 __Developer Guide

[Log In](/login?redirect_uri=/reference/user-ids)

User IDs

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

# User IDs

When Leanplum start is called for the first time on a device, a new user
profile is created and Leanplum starts tracking activity and sessions for the
user. If no custom User ID is sent with the `start` call, an anonymous user id
will be assigned based on the [Device ID](/reference/device-ids).

However, you can set your own user id by passing a user id. This way, you can
store multiple devices under a singular user id.

Below are the situations when we would recommend setting the User ID

##

On User Login

While you are able to pass in a user id on the `Leanplum.start()` call, to
track user activity early on it is best to set the user ID in Leanplum upon
the user logging in.

Once you set the user ID for the **first time** on a device, the existing
profile in Leanplum will updated with that user ID and all previously tracked
data remains.

After the initial call, each time you set a different User Id on login, you
will end the current User session, and create a new session on the new User.
If the new User ID doesn't exist, a new User Profile will be created in
Leanplum.

SwiftObjective-CJavaUnity (C#)JavaScript (HTML5)React Native

    
    
    Leanplum.setUserId("user1234")
    
    
    
    [Leanplum setUserId:@"user1234"];
    
    
    
    Leanplum.setUserId("user1234");
    
    
    
    Leanplum.SetUserId("user1234");
    
    
    
    Leanplum.setUserId("user1234");
    
    
    
    Leanplum.setUserId("user1234");
    

Here's how setting the user ID with `setUserId` works with typical
registration and login scenarios:

  * **Register** : If a user ID has not been set on this device yet and the supplied user ID does not exist, Leanplum will update the current user profile (created on `start`) with the supplied user ID (replacing the device ID).
  * **Login** : If a user ID has not been set on this device yet and the supplied user ID does exist, the current and existing user profiles will be merged. This ensures that users with multiple devices are tracked as one user. If the same user logs back in on this device, no changes will be made to their profile since their user ID is already set.
  * **Switch user** : If a user ID has been set on this device and the supplied user ID is different, the current session will be ended and a new session will be started for the supplied user ID. A user with the supplied user ID will be created if one does not already exist.

##

Logouts

Leanplum will not end the session after a user logs out and does not include
any methods to do so. All user activity is tracked and attributed to the last
logged-in user (set by the `setUserId` call). This allows you to track
activity in your app even while the user is logged out.

If you want to keep track of which users are logged in and which are logged
out, set a user attribute (e.g. logged_in).

> ## ❗️
>
> Handling User ID on Logout
>
> You do not need to set a different user ID when handling logouts. If you do
> this, you will create a new user profile in Leanplum and start a new session
> on that user, which in turn will skew your analytics.

  * __Table of Contents
  *     * On User Login
    * Logouts

