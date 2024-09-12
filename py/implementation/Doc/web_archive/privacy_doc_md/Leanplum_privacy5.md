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
In](/login?redirect_uri=/reference/gdpr-overview)[![Leanplum's user guides and
developer documentation.](https://files.readme.io/c88e191-small-
Leanplum_Logo_White.png)](https://www.leanplum.com)

 __Developer Guide

[Log In](/login?redirect_uri=/reference/gdpr-overview)

GDPR & CCPA overview

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

# GDPR & CCPA overview

##

GDPR

GDPR (General Data Protection Regulation) took effect May 25, 2018, and its
regulations apply to any company, person, or group that collects, processes,
or otherwise handles the personal data of EU and UK residents.

GDPR defines two different types of organizations who have to follow the new
regulations: data controllers and data processors.

  * **Data controllers:** determine why and how personal data is processed. As a Leanplum customer, your organization is considered a data controller.
  * **Data processors:** process user data on behalf of the controller. Leanplum processes user data on your behalf, which makes us a data processor.

As a processor, Leanplum provides the technical capabilities and
organizational processes that will allow you and our customers to maintain the
rights of your EU and UK users while using our product.

##

CCPA

Inspired by GDPR, California enacted its own consumer data protection
regulations called California Consumer Protection Act (CCPA). Effective
January 1, 2020 this act works to create new consumer rights for personal data
collected from California residents.

Under CCPA, Leanplum is a Service Provider to our customers and businesses.
Consumer rights to erasure, objection, access & portability are fulfilled via
the same APIs created for GDPR. However, th right to rectification is
currently absent from CCPA.

See below for some common tasks to help you remain GDPR and CCPA compliant
while using Leanplum.

##

Informing your end users

As a data controller, you have to inform your end-users about the personal
data you collect from them and their rights surrounding this data. GDPR & CCPA
lay out several requirements for what you must inform your end-users, and it’s
up to you to provide the information in a transparent, accessible way.

For more details on how Leanplum handles and protects your users’ data, refer
to the security information in your contract’s data processing addendum.

##

User consent for data collection

Under GDPR & CCPA, users must explicitly opt-in to data collection before you
start tracking with Leanplum. The GDPR has some stringent requirements for how
and when to give users the option to consent for data collection, so make sure
you are aware of these regulations.

To prevent data collection through Leanplum, do not call leanplum.start()
until after the user opts-in for data collection. You can also offer separate
opt-out prompts for different messaging channels in Leanplum. Giving users
more options to control their app experience might encourage them to consent
(opt-in) to data collection.

For example, if a user opts-in to data collection in general, but not to email
or push, your app should call leanplum.start and the opt-out methods for the
push and email channels. See the unsubscribe params in
**[setUserAttributes](/reference/post_api-action-setuserattributes)** for more
info.

##

Block data collection and processing

If a user objects to data processing, you can prevent Leanplum from collecting
and processing data for that user with the `block` API request.

`block` will stop Leanplum from collecting data for that user moving forward.
In order to ensure that Leanplum does not process this user’s old data, we
will delete all of their data from our systems.

See **[block](/reference/post_api-action-block)** for more details.

##

Erasing user data

Under GDPR & CCPA, data subjects have the right to request the deletion or
removal of personal data.

To delete a user’s data from Leanplum, you can use the deleteUser request,
which will delete all attributes for that user. You can also use this call to
delete a user's sessions data.

See **[deleteUser](/reference/post_api-action-deleteuser)** for more
information.

> ## ❗️
>
> Data Exported to AWS S3 Bucket
>
> If you export Leanplum data into an AWS S3 bucket or other backup locations,
> you will be responsible to handle the GDPR & CCPA requests on that data.

##

Data access and portability

Users also have the right to request a copy of their personal data in a human
or machine-readable format. Both GDPR and CCPA specify that data subjects can
obtain and reuse their personal data for their own purposes (for example, to
create an account with a competing service).

To receive a copy of a user’s data, you can use the
**[exportUser](/reference/get_api-action-exportuser)** request. This will
return all user attributes.

More coming soon on requesting your users’ data from Leanplum.

##

Rectify user data

As a data controller, GDPR requires you to give users the ability to correct
personal data if they feel it is inaccurate or incomplete. In Leanplum, this
includes user location, user attributes, and device attributes.

Use the **[setUserAttributes](/reference/post_api-action-setuserattributes)**
API request to change a user's attributes or location data in Leanplum. You
can also change device-specific attributes using
**[setDeviceAttributes](/reference/post_api-action-setdeviceattributes)**.

##

Additional support

If you are unsure of how to use some of the methods or processes above,
contact [[email protected]](/cdn-cgi/l/email-
protection#f784828787988583b79b929699879b829ad994989a) for assistance. We are
happy to answer any questions on how to use our platform. One note, we do not
provide any legal advice and are not qualified lawyers. For any legal
questions about GDPR or CCPA, we urge you to consult with your lawyer.

You can also find some general guidelines for using the **[Leanplum API
here](/reference/api-introduction)**.

  * __Table of Contents
  *     * GDPR
    * CCPA
    * Informing your end users
    * User consent for data collection
    * Block data collection and processing
    * Erasing user data
    * Data access and portability
    * Rectify user data
    * Additional support

