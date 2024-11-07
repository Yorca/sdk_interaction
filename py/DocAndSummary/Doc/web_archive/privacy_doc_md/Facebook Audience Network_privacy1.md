![](https://facebook.com/security/hsts-pixel.gif?c=3.2.5)

[Meta App Events](/docs/app-events)

  * [Overview](/docs/app-events/overview)
  * [Getting Started](/docs/app-events/getting-started)
  * [Guides](/docs/app-events/guides)
  * [Best Practices](/docs/app-events/best-practices)
  * [Reference](/docs/app-events/reference)
  * [FAQ](/docs/app-events/faq)

# Data Processing Options for US Users

Starting June 1, 2023, Limited Data Use for people in Colorado and Connecticut
via Meta Business Tools and Meta Audience Network will be effective. Starting
June 1, 2023, Limited Data Use for people in California via customer list
custom audiences will also be effective. To give businesses time to prepare,
Limited Data Use’s expanded features are available to explore as of May 1,
2023, but won’t go into effect until June 1, 2023. Please note that any
Limited Data Use flag sent for these updated states and products prior to June
1, 2023, will not be implemented.

Limited Data Use is a data processing option that gives you more control over
how your data is used in Meta’s systems and better supports your compliance
efforts with various US state privacy regulations. To utilize this feature,
you must proactively enable Limited Data Use. When Meta receives data with
Limited Data Use enabled from people in the states where Limited Data Use
applies, we will process that data in accordance with our role as a service
provider or processor, as applicable, and limit the use of that data as
specified in our [State-Specific
Terms](https://www.facebook.com/legal/terms/state-specific).

For [Business Tools](https://www.facebook.com/help/331509497253087) and
Audience Network, Limited Data Use is available only for people in California,
Colorado or Connecticut. If a business enables Limited Data Use but does not
set the location parameters to US and California, Colorado or Connecticut, we
will determine if the event is from one of those states. If Limited Data Use
is enabled for an event in California, Colorado or Connecticut, we will
process data in accordance with our role as a service provider or processor
and limit the use of that data in accordance with our [State-Specific
Terms](https://www.facebook.com/legal/terms/state-specific).

Businesses may notice an impact to campaign performance and effectiveness, and
retargeting and measurement capabilities will be limited when Limited Data Use
is enabled.

## Implementation

### Graph API

To implement Data Processing Options using the Graph API, add
`data_processing_options`, `data_processing_options_country`, and
`data_processing_options_state` to your API call.

To explicitly not enable LDU, send an empty `data_processing_options` array:

    
    
    {
      "event": "CUSTOM_APP_EVENTS",
      "application_tracking_enabled": "1",
      "advertiser_tracking_enabled": "1",
      "custom_events": ["fb_mobile_purchase"],
      "data_processing_options": []
    }  

To enable LDU and have Meta perform geolocation, you can send an event with
the following code:

    
    
    {
      "event": "CUSTOM_APP_EVENTS",
      "application_tracking_enabled": "1",
      "advertiser_tracking_enabled": "1",
      "custom_events": ["fb_mobile_purchase"],
      "data_processing_options": ["LDU"],
      "data_processing_options_country": 0,
      "data_processing_options_state": 0
    }  

To enable LDU and manually specify the location, e.g., for California, you can
send an event with the following code:

    
    
      {
      "event": "CUSTOM_APP_EVENTS",
      "application_tracking_enabled": "1",
      "advertiser_tracking_enabled": "1",
      "custom_events": ["fb_mobile_purchase"],
      "data_processing_options": ["LDU"],
      "data_processing_options_country": 1,
      "data_processing_options_state": 1000
    }  

### Mobile SDKs

We recommend using our latest versions to ensure the functionality of Data
Processing Options. The below implementation instructions are accurate for the
following SDK versions:

  * iOS Facebook SDK v7.1.1 or higher
  * Android Facebook SDK v7.1.0 or higher
  * Unity SDK v7.21.0 or higher

Please update if you are using any versions below the ones listed above.

As of July 1, 2023, we are ending the Transition Period for older versions of
App Events via the Facebook SDK, whereby we applied Limited Data Use to all
personal information shared about people in California. The ability to enable
default Limited Data Use will no longer be available for any versions below
iOS Facebook SDK v7.1.1, Android Facebook SDK v7.1.0 and Unity SDK v7.21.0. If
you choose to use Limited Data Use for a person in California, Colorado,
Connecticut, Florida, Texas, or Oregon on or after July 1, 2023, you must
update your SDK and implement Data Processing Options as set forth in this
document.

Implementation| Adding Data Processing Options| Facebook SDK for iOS v7.1.1+ (Objective-C) | With Objective-C, use `FBSDKSettings setDataProcessingOptions`.   
To explicitly not enable Limited Data Use (LDU), use:

    
    
    [FBSDKSettings setDataProcessingOptions:@[]];

To enable LDU and have Meta perform geolocation, use:

    
    
    [FBSDKSettings setDataProcessingOptions:@[@"LDU"] country:0 state:0]; 

To enable LDU and manually specify the location, e.g., for California, use:

    
    
    [FBSDKSettings setDataProcessingOptions:@[@"LDU"] country:1 state:1000];     
  
---|---  
Facebook SDK for iOS v7.1.1+ (Swift) | With Swift, use `setDataProcessingOptions`.   
To explicitly not enable LDU, use:

    
    
    Settings.setDataProcessingOptions(modes: [])   

To enable LDU and have Meta perform geolocation, use:

    
    
    Settings.setDataProcessingOptions(modes: ["LDU"], country: 0, state: 0)

To enable LDU and manually specify the location, e.g., for California, use:

    
    
    Settings.setDataProcessingOptions(modes: ["LDU"], country: 1, state: 1000)    
  
Facebook SDK for Android v7.1.0+ | Use the `setDataProcessingOptions` method.   
To explicitly not enable LDU, use:

    
    
    FacebookSdk.setDataProcessingOptions(new String[] {});   

To enable LDU and have Meta perform geolocation, use:

    
    
    FacebookSdk.setDataProcessingOptions(new String[] {"LDU"}, 0, 0);   

To enable LDU and manually specify the location, e.g., for California, use:

    
    
    FacebookSdk.setDataProcessingOptions(new String[] {"LDU"}, 1, 1000);    
  
Unity SDK v7.21.1+ | To explicitly not enable LDU, send an event with:
    
    
    FB.Mobile.SetDataProcessingOptions(new string[] {});

To enable LDU and have Meta perform geolocation, send an event with:

    
    
    FB.Mobile.SetDataProcessingOptions(new string[] {"LDU"}, 0, 0); 

To enable LDU and manually specify the location, e.g., for California, send an
event with:

    
    
    FB.Mobile.SetDataProcessingOptions(new string[] {"LDU"}, 1, 1000);    
  
![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

``

``

``

