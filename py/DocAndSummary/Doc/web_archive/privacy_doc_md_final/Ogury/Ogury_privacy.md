[![Logo](https://ogury-
ltd.gitbook.io/~gitbook/image?url=https%3A%2F%2F3481785215-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
x-
prod.appspot.com%2Fo%2Fspaces%252F-LwmnMrU_Opf4plVgohC%252Flogo%252FOtYgqbt4P2FNWQPpLxjY%252FOgury_White_Green_RGB.png%3Falt%3Dmedia%26token%3Da63d6bb2-1d85-482c-82f8-bdea2145ac79&width=192&dpr=4&quality=100&sign=951ecbe2&sv=1)![Logo](https://ogury-
ltd.gitbook.io/~gitbook/image?url=https%3A%2F%2F3481785215-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-
x-
prod.appspot.com%2Fo%2Fspaces%252F-LwmnMrU_Opf4plVgohC%252Flogo%252FOtYgqbt4P2FNWQPpLxjY%252FOgury_White_Green_RGB.png%3Falt%3Dmedia%26token%3Da63d6bb2-1d85-482c-82f8-bdea2145ac79&width=192&dpr=4&quality=100&sign=951ecbe2&sv=1)](/android)

More

SearchCtrl \+ K

  * [Getting started](/android)

  * [Test your implementation](/android/test-your-implementation)

  * [Release notes](https://docs.ogury.co/release-notes/android/ogury-sdk)
  * Ad Formats

    * [Interstitial Ad](/android/ad-formats/interstitial-ad)

    * [Opt-in Video Ad](/android/ad-formats/opt-in-video-ad)

    * [Banner Ad](/android/ad-formats/banner-ad)

    * [Thumbnail Ad](/android/ad-formats/thumbnail-ad)

  * Ogury Choice Manager

    * [Collect the user consent](/android/ogury-choice-manager/collect-the-user-consent)

    * [Third-party consent manager](/android/ogury-choice-manager/third-party-consent-manager)

    * [Advanced usages](https://docs.ogury.co/choice-manager-android/advanced-usages)
  * Help

    * [Migration guide](/android/help/migration-guide)

    * [FAQ](/android/help/faq)

    * [Help center](https://ogury-ltd.gitbook.io/help-center-for-publishers/)

[Powered by
GitBook](https://www.gitbook.com/?utm_source=content&utm_medium=trademark&utm_campaign=-LwmnMrU_Opf4plVgohC-1994518377)

# Collect the user consent

As of November 13, 2023, **Ogury Choice Manager is deprecated** , meaning it
will no longer be supported or updated.

Consequently, no new consent notices will be delivered through Ogury Choice
Manager's APIs. Therefore, it is strongly advised against using Ogury Choice
Manager in new versions of applications. In case you have migrated to a new
Consent Management Platform (CMP), ensure that Ogury and its partners are
included as vendors.

For earlier versions of applications still using Ogury Choice Manager, the API
will maintain its functionality, continuing to return consent for users who
have previously responded to a consent notice. This will remain in effect
until their consent expires.

Ogury Choice Manager handles user consent collection and storage for all your
[vendors](/android/help/faq#q-what-is-a-vendor), with a simple integration,
ensuring compliance with the GDPR regulation. Your users are shown a single
consent notice giving them the choice of the data they want to share, if any.

As an [IAB Transparency and Consent Framework
(TCF)](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-
Consent-Framework/blob/master/TCFv2/IAB%20Tech%20Lab%20-%20CMP%20API%20v2.md)
approved solution, Ogury Choice Manager not only meets the letter of the law,
but is also aligned with all relevant best practice standards.

Also, Ogury Choice Manager facilitates CCPA compliance by [IAB California
Consumer Privacy Act
(CCPA)](https://github.com/InteractiveAdvertisingBureau/USPrivacy) framework.

But where other solutions draw the line here, Ogury Choice Manager goes one
step further by incorporating vendors that fall outside of IAB jurisdiction,
including Facebook and Google. The net result is a definitive, one-stop
consent notice that covers most vendors available on the market today.

##

Requirements

Your application must be registered on your Ogury dashboard and the SDK must
be started. If not, please refer to the [Getting
started](/android#step-1-register-your-application) section before the next
steps.

##

Step 1: Get the user consent

To collect the user consent for the [all registered vendors](https://consent-
form.ogury.co/unifiedVendors-tcf-v2/latest/unifiedVendors.json), call the
`ask` method in the `onCreate` method of your `Activity`.

This method is designed to ask the server for the current user's last answer.
If the server is unable to retrieve an answer or if the user falls in a case
where a notice needs to be displayed, this method will trigger the surfacing
of the notice. Otherwise the `ask` method synchronizes the consent signal and
makes it available through the SDK methods.

You can call the `ask` method as follows:

Copy

    
    
    OguryChoiceManager.ask(activity, oguryConsentListener);

The `ask` method takes the following parameters:

  * the current `Activity`.

  * a [`OguryConsentListener`](/android/ogury-choice-manager/collect-the-user-consent#listener) interface to listen to changes of the consent signal.

The`ask` method must be called **at each launch of your application** to be
sure to have an up-to-date consent status.

**The Ogury Choice Manager and the Ogury ad formats are synchronized**. So you
can start loading the ads while requesting user consent. You do not need to
wait for the user response. Indeed, the ad will be loaded once the user's
consent is obtained. Just pay attention to call `ask `method before loading
ads.

###

**Integration example**

Copy

    
    
    public class MyActivity extends Activity {
    
        @Override protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            
            OguryConfiguration.Builder oguryConfigurationBuilder = new OguryConfiguration.Builder(this, "OGY-XXXXXXXXXXXX");
            Ogury.start(oguryConfigurationBuilder.build());
            
            OguryChoiceManager.ask(this, oguryConsentListener);
            
            // ... and load Ogury ad formats
        }
        
        private final OguryConsentListener oguryConsentListener = new OguryConsentListener() {
            @Override public void onComplete(OguryChoiceManager.Answer answer) {
                // transmit consent to other vendors' SDKs
            }
            @Override public void onError(OguryError error) {
                // handle error
            }
        };
        
    }

##

Step 2: Allow users to edit their consent

As per the GDPR regulation, publishers need to ensure the users can access and
edit their consent choices through their application at any time.

The `edit` method behaves the same way as the `ask` method but enforces the
display. If an error occurred, nothing is displayed to the user. In this case,
you need to [handle the error](/android/ogury-choice-manager/collect-the-user-
consent#error-handling) to inform the user.

Copy

    
    
    OguryChoiceManager.edit(activity, oguryConsentListener);

The `edit` method takes the following parameters:

  * the current `Activity`.

  * a [`OguryConsentListener`](/android/ogury-choice-manager/collect-the-user-consent#listener) interface to listen to changes of the consent signal.

We recommend to expose a button to edit the consent in the application
settings.

##

Step 3: Finish your integration

Congratulations! Ogury Choice Manager is now implemented.

The user consent is automatically synchronized across all Ogury products, so
you don't need to transmit it to them. You can now go back to the [Getting
started](/android#step-4-collect-the-user-consent) section to implement ad
formats and finish your integration.

However, should you have other vendors' SDKs processing user data, you can
learn how to transmit them the consent signal in the [Advanced
usages](https://docs.ogury.co/choice-manager-android/advanced-usages) section
of the [Ogury Choice Manager documentation](https://docs.ogury.co/choice-
manager-android).

##

Advanced Topics

###

**Check the availability of the edit method**

The edit option might not be available and then calling the `edit` method will
return an error in the following cases:

  * if the user is not located in the EU, i.e. not in a country where the GDPR applies;

  * as a result of a specific configuration on the Ogury Dashboard;

Before displaying the edit button, you should check this option with the
following method:

Copy

    
    
    OguryChoiceManager.isEditAvailable();

Calling this method make sense only once the synchronization triggered by `ask
`method has completed. Otherwise this method returns `true` by default.

###

Listener

The Ogury SDK provides the `OguryConsentListener` interface to listen to
consent signal changes.

The `OguryConsentListener` exposes the following methods:

Methods| Definition  
---|---  
`onComplete`| A consent notice has been displayed to the user or the consent
status has been synchronized. This method provides an
[`Answer`](/android/ogury-choice-manager/collect-the-user-consent#answer).
Learn more about how to handle the user consent if you have other vendors'
SDKs processing user data on [Ogury Choice Manager
documentation](https://docs.ogury.co/choice-manager-android/advanced-topics).  
`onError`| An error occurred. In this case, nothing is displayed to the user
and the consent status is not synchronized. This method provides an
[`OguryError`](/android/ogury-choice-manager/collect-the-user-consent#error-
handling) that contains the reason of the failure.  
  
###

Answer

In the `onComplete` method of the `OguryConsentListener` interface, you can
get the answer of the user through the`Answer` object. The `Answer` has one of
the following values:

Answer values| Definition  
---|---  
`FULL_APPROVAL`| The user has approved all vendors and all purposes displayed
in the consent notice.  
`PARTIAL_APPROVAL`| The user has approved some vendors and/or some purposes
displayed in the consent notice.  
`REFUSAL`| The user has refused all vendors and all purposes displayed in the
consent notice.  
`NO_ANSWER`| The user has not responded.  
  
###

Error handling

If Ogury Choice Manager fails to get the consent signal for any reason during
an `ask` or an `edit`, the `onError` method of the `OguryConsentListener` is
called. This method provides an `OguryError` object that contains an error
code and an error message.

To get the error code, you can call the `getErrorCode`. You can retrieve a
more explicit message by calling the `getMessage` method.

You can find predefined values for each error code in
`OguryChoiceManagerErrorCode` object. For example, you can check if error
occurred because there is no Internet connection by
using`NO_INTERNET_CONNECTION` error code as following:

Copy

    
    
    if (error.getErrorCode() == OguryChoiceManagerErrorCode.NO_INTERNET_CONNECTION) {
        // ...
    }

Here is the list of all error codes in `OguryChoiceManagerErrorCode` object:

Name| Value| Definition  
---|---|---  
`NO_INTERNET_CONNECTION`| `0`| **No Internet connection** The device has no
Internet connection. Try again once the device is connected to the Internet.  
`ASSET_KEY_UNKNOWN`| `1`| **Asset Key unknown** The Asset Key passed in the
method is unknown. Make sure to copy the exact Asset Key from the [Ogury
Dashboard](https://publishers.ogury.co/) (see the [Getting
started](/android#step-1-register-your-application) section for more
information). It may also occur while new configuration are propagating
immediately following the creation of the application.  
`BUNDLE_NOT_MATCHING`| `2`| **Bundle not matching** The bundle registered on
the [Ogury Dashboard](https://publishers.ogury.co/) does not match the Android
package of the running application. Check that you have copied the Asset Key
corresponding to the current application from the [Ogury
Dashboard](https://publishers.ogury.co/) (see the [Getting
started](/android#step-1-register-your-application) section for more
information).  
`SERVER_NOT_RESPONDING`| `3`| **Server not responding** The server has failed
to respond because of an internal error. Please try again.  
`SYSTEM_ERROR`| `4`| **System error** The SDK has encountered an internal
error. Please try again.  
`REGION_RESTRICTED`| `1000`| **Region restricted** The user is in the
restricted region.  
`TIMEOUT_ERROR`| `1002`| **Timeout error** Timeout error happened while
waiting for the response. See the error message for more details.  
`FORM_ERROR`| `1003`| **Form error** The error occurs when trying to show
Consent notice. See the error message for more details.  
`PARSING_ERROR`| `1004`| **Parsing error** The error occurs when parsing data.
Probably some field in JSON is missing or is invalid. See the error message
for more details.  
`EDIT_DISABLED_DEVICE_ID_RESTRICTED`| `1007`| **Edit function is disabled
because device id is restricted** See the error message for more details.  
`EDIT_DISABLED_GEORESTRICTED_USER`| `1008`| **Edit function is disabled
because of the users ' geolocation** See the error message for more details.  
  
Last updated 9 months ago

On this page

  * Requirements
  * Step 1: Get the user consent
  * Integration example
  * Step 2: Allow users to edit their consent
  * Step 3: Finish your integration
  * Advanced Topics
  * Check the availability of the edit method
  * Listener
  * Answer
  * Error handling

Was this helpful?

