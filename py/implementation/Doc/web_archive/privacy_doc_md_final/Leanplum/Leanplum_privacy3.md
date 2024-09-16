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
In](/login?redirect_uri=/reference/events)[![Leanplum's user guides and
developer documentation.](https://files.readme.io/c88e191-small-
Leanplum_Logo_White.png)](https://www.leanplum.com)

 __Developer Guide

[Log In](/login?redirect_uri=/reference/events)

Tracking User Behavior

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

# Tracking User Behavior

The Leanplum SDK will automatically log session and other limited amounts of
user data for you. This includes when a user starts or ends a session and such
data like their location or device.

Leanplum is also able to track more detailed data points you collect on a
user. This may include points such as ad revenue, user preferences or how long
it takes a users to play each level of your game. Each of these custom
behavior you capture can be sent as an event or state.

Events can be used to target users for certain messages, tests, or other
content changes. Below you will find more details on the the type of behavior
you are wanting to track in Leanplum.

##

Tracking an Event

An **event** is anything that can occur in your app. Events include actions
like clicking a link, sharing an update, purchasing a subscription or other
in-app asset, killing enemies etc. All events are timestamped according to
when they occur. Thus, it is not advisable to log too many events, as each one
will have to be sent to our server.

Add the following lines of code to track an event. You can place the `Leanplum
track` call anywhere as long as it executes after `start` (examples below):

SwiftObjective-CJavaUnity (C#)JavaScriptReact Native

    
    
    // This example tracks the event "Launch" 
    import UIKit
    import Foundation
    
    @UIApplicationMain
    class AppDelegate: UIResponder, UIApplicationDelegate {
    
        var window: UIWindow?
    
        func application(application: UIApplication!, didFinishLaunchingWithOptions launchOptions: NSDictionary!) -> Bool {
            ...
            Leanplum.onVariablesChanged({
                Leanplum.track(event: "Launch")
            })
            ...
            return true
        }
    ...
    
    
    
    // This example tracks the event "Launch" after defining the variable "welcomeMessage". 
    #import <Leanplum/Leanplum.h>
    
    @implementation AppDelegate
    
    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
    { ...
      [Leanplum onVariablesChanged:^{
        NSLog(@"%@", welcomeMessage.stringValue);
        [Leanplum track:@"Launch"];
      }];
      return YES;
    }
    ...
    @end
    
    
    
    // This example tracks the event "Launch" after defining the variable "welcomeMessage".
    import com.leanplum.annotations.Variable;
    import com.leanplum.annotations.Parser;
    
    public class ApplicationClass extends Application {
    
      @Variable public static String welcomeMessage = "Welcome to Leanplum!";
    
      @Override
      public void onCreate() {
        ...
        Parser.parseVariables(this);
    
        Leanplum.addVariablesChangedHandler(new VariablesChangedCallback() {
          @Override
          public void variablesChanged() {
            Log.i("Test", welcomeMessage);
            Leanplum.track("Launch");
          }
        });
        ...
    
        Leanplum.start();
      }
    }
    
    
    
    // This example tracks the event "Launch".
    using LeanplumSDK;
    
    public class LeanplumWrapper : MonoBehaviour
    {   ...
        void Start()
        {   ...
          Leanplum.Track("Launch");
        }
    }
    
    
    
    // Tracks view cart event for a user.
    Leanplum.track("View Cart");
    
    
    
    // Tracks view cart event for a user.
    Leanplum.track("View Cart");
    

SwiftObjective-CJavaUnity (C#)JavaScriptReact Native

    
    
    // User killed an enemy.
    Leanplum.track(event: "Kills")
    
    // User completed a challenge.
    Leanplum.track(event: "Score", value: 1)
    Leanplum.track(event: "Challenges")
    
    // User liked a post.
    Leanplum.track(event: "Likes", info: post.id)
    
    // Or, you can supply a dictionary with up to 200 numerical or string parameters.
    Leanplum.track(event: "Likes", params:["post":post.id])
    
    
    
    // User killed an enemy.
    [Leanplum track:@"Kills"];
    
    // User completed a challenge.
    [Leanplum track:@"Score" withValue:@1];
    [Leanplum track:@"Challenges"];
    
    // User liked a post.
    [Leanplum track:@"Likes" withInfo:@"Post Info"];
    
    // Or, you can supply a dictionary with up to 200 numerical or string parameters.
    [Leanplum track:@"Likes" withParameters:@{@"post":post.id}];
    
    
    
    // User killed an enemy.
    Leanplum.track("Kills");
    
    // User completed a challenge.
    Leanplum.track("Score", challengeValue);
    Leanplum.track("Challenges");
    
    // User liked a post.
    Leanplum.track("Likes", post.id());
    
    // Or, you can supply a dictionary with up to 200 numerical or string parameters.
    Map<String, Object> params = new HashMap<String, Object>();
    params.put("post", post.id());
    Leanplum.track("Likes", params);
    
    
    
    // User killed an enemy.
    Leanplum.Track("Kills");
    
    // User completed a challenge.
    Leanplum.Track("Score", challengeValue);
    Leanplum.Track("Challenges");
    
    // User liked a post.
    Leanplum.Track("Likes", post.id());
    
    // Or, you can supply a dictionary with up to 200 numerical or string parameters.
    Dictionary<string, object> params = new Dictionary<string, object>();
    params.Add("post", post.id());
    Leanplum.Track("Likes", params);
    
    // You can also pass a value and parameters.
    // User made a purchase. Use Leanplum.PURCHASE_EVENT_NAME to indicate a purchase.
    Dictionary<string, object> item = new Dictionary<string, object>();
    params.Add("itemCategory", "Apparel");
    Leanplum.Track(Leanplum.PURCHASE_EVENT_NAME, 19.99, item);
    
    
    
    // Tracks view cart event for a user.
    Leanplum.track("View Cart");
    
    // Tracks view cart event with numeric event parameter, itemsInCart.
    Leanplum.track("View Cart", {itemsInCart: 4});
    
    // Tracks an event with a value and two event parameters.
    Leanplum.track("Purchase", 4.99, {itemCategory: 'Apparel', itemName: 'Shoes'});
    
    
    
    // Tracks view cart event for a user.
    Leanplum.track('View Cart');
    
    // Tracks view cart event with numeric event parameter, itemsInCart.
    Leanplum.track('View Cart', {itemsInCart: 4});
    
    // Tracks an event with a value and two event parameters.
    Leanplum.track('Purchase', {itemCategory: 'Apparel', itemName: 'Shoes'});
    

> ## 🚧
>
> 500 event limit and event naming limits
>
> Note that there is a limit of 500 events per app in Leanplum. Since events
> are not unlimited, it's best to track more general events, and use
> parameters to track specific information associated with the event.
>
> For example, you should use a simple name for a purchase event, such as
> `LP_PURCHASE_EVENT` and pass a purchase ID or item ID as a **parameter**.
> Review our [Naming rules for events, states, and
> parameters](/reference#section-naming-events-states-user-attributes-and-
> parameters) for a full list of limitations.

##

Advancing to a State

A **state** is a time-based event in Leanplum that allows you to track . For
example, some states can include being in a particular level, watching a
video, or browsing an in-app store.

All states have a time and a duration. The duration is set automatically —
when one state begins, the previous one ends.

This example is called when the user advances to the next level.

SwiftObjective-CJavaUnity (C#)JavaScript (HTML5)React Native

    
    
    //Example state call
    Leanplum.advance(state: "Level", info: level.name)
    
    
    //The pause state function is useful if you need to pause in the middle of use. 
    //EX: Game with 'pause' mode.  We automatically handle this when the app is backgrounded
    Leanplum.pauseState()
    Leanplum.resumeState()
    
    
    //They will cause the user to leave current state and not enter another one
    Leanplum.advance(state:nil)
    
    
    
    //Example state call
    [Leanplum advanceTo:@"Level" withInfo:level.name];
    
    //The pause state function is useful if you need to pause in the middle of use. 
    //EX: Game with 'pause' mode.  We automatically handle this when the app is backgrounded
    [Leanplum pauseState];
    [Leanplum resumeState];
    
    //They will cause the user to leave current state and not enter another one
    [Leanplum advanceTo:nil];
    
    
    
    //Example state call
    Leanplum.advanceTo("Level", level.name());
    
    //The pause state function is useful if you need to pause in the middle of use. 
    //Ex with 'pause' mode.  We automatically handle this when the app is backgrounded
    Leanplum.pauseState();
    Leanplum.resumeState();
    
    //They will cause the user to leave current state and not enter another one
    Leanplum.advanceTo(null);
    
    
    
    //Example state call
    Leanplum.AdvanceTo("Level", level.Name);
    
    //The pause state function is useful if you need to pause in the middle of use. 
    //EX: Game with 'pause' mode.  We automatically handle this when the app is backgrounded
    Leanplum.PauseState();
    Leanplum.ResumeState();
    
    //They will cause the user to leave current state and not enter another one
    Leanplum.AdvanceTo(null);
    
    
    
    // example state call
    Leanplum.advanceTo("Cart", {numItems: 2});
    
    //The pause state function is useful if you need to pause in the middle of use. 
    //EX: Game with 'pause' mode.  We automatically handle this when the app is backgrounded
    Leanplum.pauseState();
    Leanplum.resumeState();
    
    //They will cause the user to leave current state and not enter another one
    Leanplum.advanceTo(null);
    
    
    
    // example state call
    Leanplum.advanceTo("Cart", "info", {numItems: 2});
    
    //The pause state function is useful if you need to pause in the middle of use. 
    //EX: Game with 'pause' mode.  We automatically handle this when the app is backgrounded
    Leanplum.pauseState();
    Leanplum.resumeState();
    
    //They will cause the user to leave current state and not enter another one
    Leanplum.advanceTo(null);
    

##

Parameter

A **parameter** is a piece of data associated with an event or state. You can
supply parameters as a dictionary along with events and states. Here are some
reports you can run with parameters:

  * Filter reports by event parameter values
  * Group metrics by distinct event parameter values (creates a bar graph + table). Example: Show me my top purchased items.
  * Group metrics by ranges of event parameter values (creates a histogram + table). Example: Show me the distribution of purchase prices. Example: Show me the distribution of points scored.
  * Create custom metrics for numeric parameter values, like totals and averages. Example: For a purchase event, track the average revenue and the amount of currency bought per user.

> ## 📘
>
> Parameter limitations
>
> Parameters and Event Values are not available in Developer activity
> analytics, but you can verify your parameters are being tracked correctly in
> the Debugger console.
>
> Also, with the out-of-box Leanplum SDK, parameters cannot be used as a
> criteria to target users. For example, if you have an event
> "Favorite_Color_Selected" with parameters for each color, you would not be
> able to target users who completed the **Favorite color select** event and
> chose the color _blue_.

Events and states accumulate over time, and we send events in batches
periodically to minimize network usage and maximize battery life.

  * __Table of Contents
  *     * Tracking an Event
    * Advancing to a State
    * Parameter

