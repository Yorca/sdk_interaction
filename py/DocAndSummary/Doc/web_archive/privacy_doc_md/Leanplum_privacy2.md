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
In](/login?redirect_uri=/reference/user-attributes)[![Leanplum's user guides
and developer documentation.](https://files.readme.io/c88e191-small-
Leanplum_Logo_White.png)](https://www.leanplum.com)

 __Developer Guide

[Log In](/login?redirect_uri=/reference/user-attributes)

User attributes

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

# User attributes

A user attribute is any piece of data you would use to characterize on that
user as you build their profile in Leanplum. User attributes, since they set
to characterize your user will carry over from session to session. This is
different from event parameters, which may take on different values per event
and from session to session.

##

Uses In Leanplum

User Attributes on the Leanplum platform have many uses and are really
powerful in creating meaningful engagements with your users. The main uses
include:

  * **Personalizing content:** You are able to insert user attribute values in Leanplum variables, messages, resources, and interfaces. Allowing you to personalize and reach different types of users in personal and meaningful ways.
  * **Segmentation Targeting:** With user attributes you are also able to build audiences and different segment of users you can use in A/B testing, Messages and Campaigns
  * **Filtering and Grouping reports:** Group and filter analytics reports by different user attributes and values. This allows you to create a histogram of average session length by number of friends or look at user data for "whales" (targeting your largest spender)

###

Examples:

Standard examples of User Attributes that have been tracked in the past are
below. Additionally, you can see how you can set user attributes from a client
level with our SDKs

  * Gender
  * Age
  * Number of friends
  * User interests
  * Email ( which is a required field if you are running [email campaigns](/docs/email-setup))

SwiftObjective-CJavaUnity (C#)JavaScript (HTML5)React Native

    
    
    // Passing attributes at session start allows us to target content based on the attributes.
    Leanplum.start(attributes: ["gender":"Female", "age": 29])
    
    // You can also pass them later on in the session, but you won't be able to
    // target variables or messages at these for that session.
    Leanplum.setUserAttributes(["gender":"Female", "age": 29])
    
    // Clear an attribute.
    Leanplum.start(userAttributes: ["gender":NSNull()])
    
    // To allow targeting the user in email campaigns, set the "email" attribute
    Leanplum.setUserAttributes(["email":"[[email protected]](/cdn-cgi/l/email-protection)"])
    
    
    
    // Passing attributes at session start allows us to target content based on the attributes.
    [Leanplum startWithUserAttributes:@{@"gender": @"Female", @"age": @29}];
    
    // You can also pass them later on in the session, but you won't be able to
    // target variables or messages at these for that session.
    [Leanplum setUserAttributes:@{@"gender": @"Female", @"age": @29}];
      
    // Clear an attribute.
    [Leanplum startWithUserAttributes:@{@"gender": [NSNull null]}];
    
    // To allow targeting the user in email campaigns, set the "email" attribute
    [Leanplum setUserAttributes:@{@"email": @"[[email protected]](/cdn-cgi/l/email-protection)"}];
    
    
    
    // Passing attributes at session start allows us to target content based on the attributes.
    Map<String, Object> attributes = new HashMap<String, Object>();
    attributes.put("gender", "Female");
    attributes.put("age", 29);
    Leanplum.start(this, attributes);
    
    // You can also pass them later on in the session, but you won't be able to
    // target variables or messages at these for that session.
    Leanplum.setUserAttributes(attributes);
    
    // Clear the attributes.
    attributes.put("gender", null);
    attributes.put("age", null);
    Leanplum.setUserAttributes(attributes);
    
    // To allow targeting the user in email campaigns, set the "email" attribute
    attributes.put("email", "[[email protected]](/cdn-cgi/l/email-protection)");
    Leanplum.setUserAttributes(attributes);
    
    
    
    // Passing attributes at session start allows us to target content based on the attributes.
    Dictionary<string, object> attributes = new Dictionary<string, object>();
    attributes.Add("gender", "Female");
    attributes.Add("age", 29);
    Leanplum.Start(attributes);
    
    // You can also pass them later on in the session, but you won't be able to
    // target variables or messages at these for that session.
    Leanplum.SetUserAttributes(attributes);
    
    // Clear the attributes.
    attributes.Add("gender", null);
    attributes.Add("age", null);
    Leanplum.SetUserAttributes(attributes);
    
    // To allow targeting the user in email campaigns, set the "email" attribute
    attributes.Add("email", "[[email protected]](/cdn-cgi/l/email-protection)");
    Leanplum.SetUserAttributes(attributes);
    
    
    
    // Passing attributes at session start allows us to target content based on the attributes.
    var attributes = {'gender': 'Female', 'age': 29};
    Leanplum.start(attributes);
    
    // You can also pass them later on in the session, but you won't be able to
    // target variables or messages at these for that session.
    Leanplum.setUserAttributes(attributes);
    
    // Clear the attributes.
    Leanplum.setUserAttributes({'gender': null, 'age': null});
    
    // To allow targeting the user in email campaigns, set the "email" attribute
    Leanplum.setUserAttributes({'email': '[[email protected]](/cdn-cgi/l/email-protection)'})
    
    
    
    Leanplum.setUserAttributes({'gender': 'Female'});
    
    // Examples
    var attributes = {'gender': 'Female', 'age': 29};
    Leanplum.setUserAttributes(attributes);
    
    // Clear the attributes
    Leanplum.setUserAttributes({'gender': 'Male', 'age': 30});
    
    // To allow targeting the user in email campaigns, set "email" attribute
    Leanplum.setUserAttributes({'email': '[[email protected]](/cdn-cgi/l/email-protection)'})
    

###

Constraints:

While user attributes are a powerful tool for creating meaningful engagement,
there is are constraints around numbers and types you can send. See those
below:

  * Up to 200 unique attributes can be defined per Leanplum app.
  * Attribute names must be strings, and values must be strings or numbers.
  * Attribute values will be the same across all events and states in a particular session. 

###

Additional Notes

> ## 📘
>
> User attribute as list
>
> Since user attribute values can only be strings or numbers, saving an
> array/list will need to be converted to a string first. This will allow you
> to:
>
>   * Add/remove elements through our
> _[setUserAttributes](/reference#post_api-action-setuserattributes)_ API,
> using userAttributeValuesToAdd and userAttributeValuesToRemove
>   * Loop through or use specific array elements with our _[Templating
> Language](/docs/message-templating-)_
>

> ## 📘
>
> User attribute as timestamp
>
> Leanplum supports date time segmentation on user attributes. Supported
> formats can be found [here](/docs/datetime-user-attribute#getting-started) .
>
> To schedule campaigns based on a user attribute timestamp, please see _[this
> article](/docs/sending-a-push-before-or-after-a-time-based-event-
> parameter)_.

> ## 📘
>
> User attributes and case sensitivity
>
> Please be aware that user attributes names are case-sensitive, while the
> values are not. For example the user attribute "language" and "Language" are
> considered different, while their values - "english", "English", "ENGLISH"
> are considered the same.

  * __Table of Contents
  *     * Uses In Leanplum
      * Examples:
      * Constraints:
      * Additional Notes

