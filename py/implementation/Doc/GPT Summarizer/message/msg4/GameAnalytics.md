SDK name: GameAnalytics
Documentation:
Skip to main content

[![GameAnalytics Logo](/img/ga-logo.png)![GameAnalytics Logo](/img/ga-
logo.png)](https://gameanalytics.com/)[Setup](/)[Integrations](/integrations)[Guides](/features)[API](/integrations/api/overview)[Data
Access](/datasuite)

[Resources](https://gameanalytics.com/resources)[Feedback](https://feedback.gameanalytics.com/)[Contact](https://gameanalytics.com/contact/)

  * [Getting Started](/)

    * [Platform Overview](/)
    * [Metrics & Dimensions](/metrics-dimensions)
    * [Event Types](/event-types)

    * [Advanced Tracking](/advanced-tracking/custom-dimensions)

    * [Data retention](/data-retention)
    * [Service Level Agreement](/service-level-agreement)
  * [Integrations](/integrations)

    * [SDKs](/integrations/sdk)

      * [Unity](/integrations/sdk/unity)

        * [Setup](/integrations/sdk/unity)
        * [Event Tracking](/integrations/sdk/unity/event-tracking)
        * [Game Ops](/integrations/sdk/unity/game-ops)
        * [SDK Features](/integrations/sdk/unity/sdk-features)
        * [Advanced Setup](/integrations/sdk/unity/advanced-setup)
      * [Unreal](/integrations/sdk/unreal)

      * [Roblox](/integrations/sdk/roblox)

      * [Godot](/integrations/sdk/godot)

      * [Cocos2D](/integrations/sdk/cocos2d)

      * [GameMaker](/integrations/sdk/gamemaker)

      * [Cordova](/integrations/sdk/cordova)

      * [Flutter](/integrations/sdk/flutter)

      * [Adobe Air](/integrations/sdk/adobe-air)

      * [Construct](/integrations/sdk/construct)

      * [Defold](/integrations/sdk/defold)

      * [Android](/integrations/sdk/android)

      * [iOS](/integrations/sdk/ios)

      * [Meta Quest 2](/integrations/sdk/meta-quest)

      * [tvOS](/integrations/sdk/tvos)

      * [Javascript](/integrations/sdk/javascript)

      * [C++](/integrations/sdk/cpp)

      * [C#](/integrations/sdk/c-sharp)

    * [Collection API](/integrations/api/overview)

    * [Attribution](/integrations/attribution)

    * [Advertising (ILRD)](/integrations/advertising)

    * [Monetization](/integrations/monetization)

  * [Features](/features)

    * [Dashboards](/features/dashboards)

    * [Explore Tool](/features/explore-tool)

    * [Funnels](/features/funnels)

    * [Engagement](/features/engagement/overview)

    * [Cohorts](/features/cohorts)

    * [Health](/features/health)

    * [Monetization](/features/monetization/overview)

    * [Remote Configs](/features/remote-configs)

    * [A/B Testing](/features/ab-testing)

    * [Portfolio overview](/features/portfolio-overview/overview)

    * [Filter value selection](/features/filter-value-selection/overview)

    * [Reporting](/features/reporting/overview)

    * [Account Management](/features/account-management)

    * [Game Data Sharing](/features/game-data-sharing/overview)

    * [Metrics API](/features/metrics-api/overview)

    * [Legacy Tool](/features/legacy-tool)

  * [DataSuite](/datasuite)

    * [Overview](/datasuite)
    * [Subscribe](/datasuite/subscribe)
    * [Data Warehouse](/datasuite/data-warehouse/overview)

    * [Data Export](/datasuite/data-export/overview)

  * [GameIntel](/gameintel)

    * [Overview](/gameintel)
    * [Store Intelligence](/gameintel/store-intelligence/overview)

    * [Benchmarks](/gameintel/benchmarks/overview)

    * [Purchasing and billing](/gameintel/purchasing-billing)
  * [Organization API](/organization-api)

    * [Overview](/organization-api)
    * [API notes](/organization-api/api-notes)
    * [API specification](/organization-api/api-specs)

  * [](/)
  * [Integrations](/integrations)
  * [SDKs](/integrations/sdk)
  * [Unity](/integrations/sdk/unity)
  * SDK Features

On this page

# SDK Features

## Control Event Submission[â](/integrations/sdk/unity/sdk-features#control-
event-submission "Direct link to Control Event Submission")

You can manually turn off/on event submission for GA events. This is useful if
you need, for GDPR purposes, to disable event submission.

    
    
    GameAnalytics.setEnabledEventSubmission(false);  
    

info

By default event submission is of course enabled. You will still receive
configs if you have set any for your game even after disabling event
submission.

## Custom Dimensions[â](/integrations/sdk/unity/sdk-features#custom-
dimensions "Direct link to Custom Dimensions")

GameAnalytics allows you to create up to 3 custom dimensions for your events.
You will first have to set these up in your **GA dashboard** in `Settings`
under the `Setup` tab.

caution

Any value which is not defined in the dashboard will be ignored!

    
    
    // set custom dimension number 1  
    GameAnalytics.SetCustomDimension01 (string customDimension);  
      
    // set custom dimension number 2  
    GameAnalytics.SetCustomDimension02 (string customDimension)  
      
    // set custom dimension number 3  
    GameAnalytics.SetCustomDimension03 (string customDimension)  
    

Field| Type| Required| Description  
---|---|---|---  
customDimension| string| yes| One of the available dimension values set in
Settings (Setup tab). Will persist cross session. Set to null to remove again.  
  
tip

Read more about custom dimensions [here](/advanced-tracking/custom-dimensions)

## Custom Event Fields[â](/integrations/sdk/unity/sdk-features#custom-event-
fields "Direct link to Custom Event Fields")

caution

Custom event fields **will not** be available in the GameAnalytics dashboards.

Read more about how to use Custom Event Fields [here](/advanced-
tracking/custom-event-fields).

During the game it is possible to set global custom event fields that can be
changed at any time. Custom event fields are a set of key-value pairs can be
added to any of your events.

It is also possible to overwrite the global custom event fields by using the
optional custom event fields parameter for when sending individual events,
please refer to the events documentation page for usage.

Setting global custom event fields:

    
    
    Dictionary<string, object> customFields = new Dictionary<string, object>();  
    customFields.Add("test", 1000);  
    customFields.Add("test_2", "global_hello_world");  
    GameAnalytics.SetGlobalCustomEventFields(customFields);  
    

Field| Type| Description| Example  
---|---|---|---  
customFields| dictionary| A set of key-value pairs. Values can be strings or
numbers| {  
"test": 1000,  
"tests": "hello_world"  
}  
  
tip

Read more about custom dimensions
[here](https://docs.gameanalytics.com/advanced-tracking/custom-dimensions).

## PlayMaker[â](/integrations/sdk/unity/sdk-features#playmaker "Direct link
to PlayMaker")

GameAnalytics is set up to work with PlayMaker to make it as easy as possible
for you to send events using the visual PlayMaker scripting tools.

### Activating the SDK for PlayMaker[â](/integrations/sdk/unity/sdk-
features#activating-the-sdk-for-playmaker "Direct link to Activating the SDK
for PlayMaker")

You need to tell our SDK that it will be used with PlayMaker. To do so you
need to toggle the SDK scripts by clicking `Window -> GameAnalytics ->
PlayMaker -> Toggle Scripts`.

![Unity
Playmaker](/assets/images/playmaker_0-469c4823c009a35b564bcd0dc0243a31.png)

caution

Make sure at this stage PlayMaker is already added to Unity!

### Using the GA SDK with PlayerMaker[â](/integrations/sdk/unity/sdk-
features#using-the-ga-sdk-with-playermaker "Direct link to Using the GA SDK
with PlayerMaker")

At this stage a new category for Actions named GameAnalytics should pop-up in
the PlayMaker Actions list used for when adding an action to a state.

![Unity
Playmaker](/assets/images/playmaker_1-5da0ee903dd4ce84a2c199736bb80364.png)

When using GameAnalytics actions you may notice that some of the parameters
are mandatory while others can be set to none. Follow closely our
documentation about each event type (Business, Design, Progression, Resource
and Error) before using the actions.

![Unity
Playmaker](/assets/images/playmaker_2-7107f042d3715fa40a953a1c42df08a0.png)

info

In order to better understand how to use GameAnalytics please read our
guidelines about the implementation process and how the tool reads custom
events.

## Disclaimers[â](/integrations/sdk/unity/sdk-features#disclaimers "Direct
link to Disclaimers")

caution

Known issue: On Unity 2019.2 there is an issue with importing
âAssets/GameAnalytics/Plugins/GameAnalytics.dllâ which makes the importing
of the GameAnalytics Unity SDK package freeze and does not complete. A quick
fix for this is to delete
âAssets/GameAnalytics/Plugins/GameAnalytics.dllâ. This of course means you
will not be able to build for desktop platforms (Windows, Mac or Linux). We
are sorry for the inconvenience and we trying to fix this issue as soon as
possible. Note: There is a fix now in v5.1.11

  

caution

FPS metrics change from v5.1.7: In v5.1.7 we fixed our FPS event script where
it will use Time.unscaledTime instead of Time.time to get a more accurate FPS
metrics if your game frequently changes the time scale in the game. So after
updating the SDK to v5.1.7 or a later version you might see a big change in
the FPS metrics if you frequently changing the time scale in your game.

caution

  

caution

Important Announcement From v3.11.0 and onwards you need to manually
initialize the SDK by calling GameAnalytics.Initialize() from your own
GameObject (with script execution order coming after GameAnalytics scriptâs
order if your object is in the same scene as the GameAnalytics object as some
code is called on Awake event which needs to be called before initializing the
sdk). Read more about it in the Initialization section [
here](https://gameanalytics.com/item/unity-sdk/#initialization).

## Session Handling[â](/integrations/sdk/unity/sdk-features#session-handling
"Direct link to Session Handling")

By default the SDK will handle session start/end automatically, but it is also
possible to manually control this yourself.

caution

Be aware that the initialization will always automatically start the first
session even with manual session handling.

### Automatic Session Handling[â](/integrations/sdk/unity/sdk-
features#automatic-session-handling "Direct link to Automatic Session
Handling")

The automatic session handling will track the focused time the user is
spending in your game â from game launch to the user leaving the game.

#### `session start`[â](/integrations/sdk/unity/sdk-features#session-start
"Direct link to session-start")

On Android a new session will start once the game is launched or when the app
is resuming if there is no current session.

#### `session end`[â](/integrations/sdk/unity/sdk-features#session-end
"Direct link to session-end")

A session will end once the game is going to home-screen (or is not visible
anymore).

It will end the session at once if the application received the onStop event
from the game activity. It can also end the session if onPause event was
received and 90 seconds have passed (sometimes only the onPause will trigger
even though the user left the app).

### Manual Session Handling[â](/integrations/sdk/unity/sdk-features#manual-
session-handling "Direct link to Manual Session Handling")

The automatic session handling only works if the game is contained in one
activity.

It will then handle session end and start based on the events on that single
activity. This behavior is common (having one activity) but some games define
multiple activities and this automatic session handling will not work in an
optimal way.

If your game does have multiple activities (or you just want to be in control
when to start and end sessions) you can enable/disable manual session handling
by calling this at any given time:

    
    
    GameAnalytics.setEnabledManualSessionHandling(true);  
    

You will then need to call `endSession` and `startSession` at the appropriate
times.

tip

With manual session handling it is recommended to also call endSession when
the game activity event onStop is fired. This will ensure a correct session
close when users click the home or on/off button.

#### `startSession()`[â](/integrations/sdk/unity/sdk-features#startsession
"Direct link to startsession")

This will start a new session if:

  * manual session handling is enabled
  * SDK is initialized (initialize will start a session automatically)

    
    
    GameAnalytics.startSession();  
    

#### `endSession()`[â](/integrations/sdk/unity/sdk-features#endsession
"Direct link to endsession")

This will end a session if:

  * manual session handling is enabled
  * a session is active
  * SDK is initialized (initialize will start a session automatically)

    
    
    GameAnalytics.endSession();  
    

caution

If a current session is active then it will **end the current session and
start a new one**.

### Behind the Scenes[â](/integrations/sdk/unity/sdk-features#behind-the-
scenes "Direct link to Behind the Scenes")

This is what happens when the session is starting or ending.

#### Session start[â](/integrations/sdk/unity/sdk-features#session-start-1
"Direct link to Session start")

  1. Generate new session.
  2. Add a `session_start` event (a âuserâ event).
  3. Start the periodic activation of submitting queued events.
  4. Next event submits will fix potential missing `session_end` from earlier sessions.

##### Session end[â](/integrations/sdk/unity/sdk-features#session-end-1
"Direct link to Session end")

  1. Stop the periodic activation of submitting queued events.
  2. Add a `session_end` event.
  3. Submit queued events.

* * *

[PreviousGame Ops](/integrations/sdk/unity/game-ops)[NextAdvanced
Setup](/integrations/sdk/unity/advanced-setup)

On this page

  * Control Event Submission
  * Custom Dimensions
  * Custom Event Fields
  * PlayMaker
    * Activating the SDK for PlayMaker
    * Using the GA SDK with PlayerMaker
  * Disclaimers
  * Session Handling
    * Automatic Session Handling
    * Manual Session Handling
    * Behind the Scenes

Copyright 2024 GameAnalytics \- [Terms](https://gameanalytics.com/terms/) | [Privacy](https://gameanalytics.com/privacy/) | [Cookies](https://gameanalytics.com/cookie-policy/)

[![](/assets/images/iso_white-2889ac0c54957549a3caadf3348fdd30.png)](https://www.aicpa.org/soc4so)[![](/assets/images/soc2-type2-c83b5a9c8172777ddaf9c7486cd63898.png)](https://www.iafcertsearch.org/certification/0ec9433f-1a3f-503b-a8fa-5586c625eb07)[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJYAAAA2CAYAAAAlHWAMAAAABGdBTUEAALGPC/xhBQAAADhlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAAqACAAQAAAABAAAAlqADAAQAAAABAAAANgAAAABEpPWMAAAgEUlEQVR4Ae3deaxnRZUH8NsLDTTN1iy2yvIaUFBQQBR3bVREcUEUMwH3FYOJJurEuCQyySQa9A81OmNGoxkwKu4iiuKGiqK44goqCAjIJtjQ0Kzdcz63+/uj+vbv9/o9+pHJZLqS21W36ux16tSpur8H87r7rizab7/9dlyzZs229cy/79hsoXxvLTB//vw1CxcuvPVPf/rTP4vGXfeWzji8eeM6N6fvwQ9+8AF33XXXYxcsWHD4vHnzHlbP/YvetvWs3Ry6W3Dn3ALmfvXatWuvqPq3d9999/lV//jiiy/+y1xwmivHmrf33nsfUM70+u222+7opUuXLj/ggAO6crJut91267baaqu5kHULjTm0QC347o477uiuvfba7sILL+wuuuii7sYbb7z41ltvPbvYvP+SSy750+aw22zHKsdZssMOO7yynOpfy5n2ePrTn949+clP7nbdddeutsBZy0bhCtGd2oOGp1bWjGjBSZkJTgsfvLaeCY0W/v9Sm27R7+9//3v3/e9/v/vBD37Q1dZ4ye233/7e1atXn3bNNdfccm90umcW7gX28uXL9y6H+vdly5Ydf+yxxy444ogjeiqrVq3qnWOnnXbqlixZMmMHM8m1jXb/+Mc/utDYcccdO3Q25QDGPZxSYbBNOeQQB3xoxOht3RPexD+hOR1YaE6CmQmNSbj60UdjNoXdFi1a1F133XXd17/+9e5LX/rSXddff/1/F6231/Z47WxogZ0d94Z6bXc71POf++yzzwmvec1ruic84Qndj3/84+6UU07pVq5c2VUU6x796Ed3L3nJS7rdd9+9qz28wR7frESyu+CCC7oPfehD3aWXXtqV03YPfehDu3e84x1d8ZpII0asUN797W9/6+68887uAQ94QFcO3xuYodvCiPpqVfZbwdVXX93ddNNN/TsZtt56635B4Hm/+92v22abbXpZ0OB80xV60n8SHPoWS2QYR+u2227rbrnlllE0GQczqQ998tKNHWZbOBf9f/WrX3Uf//jH11522WUfqMX+bzUf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)](https://www.kidsafeseal.com/certifiedproducts/game_analytics.html)[![](data:image/png;base64,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)](https://partners.amazonaws.com/partners/0010h00001kMkq4AAC/)

