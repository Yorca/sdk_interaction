[____](https://www.pollfish.com/)

[Sign Up Free](https://www.pollfish.com/signup)[
Login](https://www.pollfish.com/login)

  * [ __](https://www.pollfish.com/docs/android-v7#)

  * ### [SDK& Documentation](https://www.pollfish.com/docs/android-v7#)

 __

[Researcher's Area __](https://www.pollfish.com/)[Publisher's Area
__](https://www.pollfish.com/publisher)

[How It Works](https://www.pollfish.com/how-it-
works)[Pricing](https://www.pollfish.com/#pricing)[Blog](https://www.pollfish.com/blog)[Resources](https://www.pollfish.com/pf)[Contact](https://www.pollfish.com/contact)

[Company](https://www.pollfish.com/docs/android-v7#)

[Media Kit](https://www.pollfish.com/company/mediakit)

[Researcher](https://www.pollfish.com/docs/android-v7#)

[Example
Results](https://www.pollfish.com/dashboard/results/253227526/618845688)[Case
Studies](http://blog.pollfish.com/category/market-research)

[Publisher](https://www.pollfish.com/docs/android-v7#)

[Referral](https://www.pollfish.com/publisher/referral)[Case
Studies](https://pollfish.com/case-studies/)[Demo
Apps](https://www.pollfish.com/publisher/demo)[Testimonials](https://www.pollfish.com/publisher/testimonials)

[SDK & Documentation](https://www.pollfish.com/docs/android-v7#)

[Android](https://www.pollfish.com/docs/android-v7#)

[Google Play Edition](https://www.pollfish.com/docs/android/google-
play)[Universal Edition](https://www.pollfish.com/docs/android/universal)

[Android v7
(Beta)](https://www.pollfish.com/docs/android-v7)[iOS](https://www.pollfish.com/docs/ios)[WebPlugin](https://www.pollfish.com/docs/webplugin)

[Other Plugins](https://www.pollfish.com/docs/android-v7#)

[Unity](https://www.pollfish.com/docs/unity)[Cordova](https://www.pollfish.com/docs/cordova)[Flutter](https://www.pollfish.com/docs/flutter)[React
Native](https://www.pollfish.com/docs/react-native)[AdMob Android
Adapter](https://www.pollfish.com/docs/android-admob-adapter)[AdMob iOS
Adapter](https://www.pollfish.com/docs/ios-admob-adapter)[AppLovin Max Android
Adapter](https://www.pollfish.com/docs/android-max-adapter)[AppLovin Max iOS
Adapter](https://www.pollfish.com/docs/ios-max-adapter)[IronSource Android
Adapter](https://www.pollfish.com/docs/android-ironsource-adapter)[IronSource
iOS Adapter](https://www.pollfish.com/docs/ios-ironsource-adapter)

[Rewarded Surveys](https://www.pollfish.com/docs/rewarded-
surveys)[Offerwall](https://www.pollfish.com/docs/offerwall)[Pay on
Screenouts](https://www.pollfish.com/docs/pay-on-screenouts)[Demographic
Surveys](https://www.pollfish.com/docs/demographic-surveys)[Mediation
Platform](https://www.pollfish.com/docs/mediation)[API
Documentation](https://www.pollfish.com/docs/api-documentation)[Dashboard
API](https://www.pollfish.com/docs/dashboard-api)[Server-to-Server
Callbacks](https://www.pollfish.com/docs/s2s)

[Respondent](https://www.pollfish.com/docs/android-v7#)

[Opt Out](https://www.pollfish.com/respondent/opt-out)

[Terms of Service](https://www.pollfish.com/docs/android-v7#)

[Researcher](https://www.pollfish.com/terms/researcher)[Subscription
Plans](https://www.pollfish.com/terms/subscriptions)[Researcher - Distribution
Link](https://www.pollfish.com/terms/researcher-
link)[Publisher](https://www.pollfish.com/terms/publisher)[Respondent](https://www.pollfish.com/terms/respondent)[Respondent
- Distribution Link](https://www.pollfish.com/terms/respondent-link)[Cookie
Policy](https://www.pollfish.com/terms/cookie-policy)[Google Play Data Safety
Questionnaire](https://www.pollfish.com/terms/google-play-data-safety-
questionnaire)

# Pollfish Android SDK v7 (Beta)

[Download SDK
v7.0.0-beta07](https://storage.googleapis.com/pollfish_production/sdk/Android/Prodege%20Android%20SDK-7.0.0-beta07.zip)See
what's new in this version

[Sample Project ](https://github.com/pollfish/android-sdk-pollfish/)

7.0.0-beta07

  * Fixing internal issues causing occasional crashes

7.0.0-beta06

  * Fixing internal issues causing ANRs

7.0.0-beta05

  * Fixing issue with blank end card after app returning to foreground

7.0.0-beta04

  * Internal fixes

7.0.0-beta03

  * Fixing issues with Adnroid 8

7.0.0-beta02

  * Fixing internal issues

7.0.0-beta01

  * new SDK with support for placements and rewarded ads

# Prerequisites

  * [Prodege Publisher Account](https://www.pollfish.com/dashboard/dev/)
  * Android API 21 or later
  * Java 1.8
  * Kotlin 1.9.0

  

# Quick Guide

  1. Obtain a [Publisher Account](https://www.pollfish.com/signup/publisher)
  2. Create a new App and copy the given API key
  3. Create a new placement and copy the given placement id
  4. Add Prodege SDK in your project
  5. Initialize Prodge SDK
  6. Load a Placement
  7. Show the placement
  8. Update you privacy policy and publish your app
  9. Request your account to get verified

  

> **Note:** Apps designed for [Children and Families
> program](https://play.google.com/about/families/ads-monetization/) should
> not be using Prodege SDK, since Prodege does not collect responses from
> users less than 16 years old.

  

> **Note:** Prodege SDK requires minSdk 21. If your app supports a lower
> minSdk you can still build your app please refer to section 7.

# Analytical steps

## 1\. Obtain a Publisher Account

Register as a Publisher at
[www.pollfish.com](https://www.pollfish.com/signup/publisher)

  

## 2\. Create a new App and copy the given API key

Login at
[www.pollfish.com](https://www.pollfish.com/docs/www.pollfish.com/login/publisher)
and click "Add a new app" on the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/). Copy then the given API
key for this app in order to use later on, when initializing Prodege SDK
within your code.

  

## 3\. Create a new placement and copy the given placement id

Navigate in your [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/) under App Settings -
Placements and choose "Create a Placement". You can select a Rewarded Ad or an
Offerwall approach based on your placement needs with any of the available Ad
Formats(it can change later through placement settings). Hit "Create
Placement" and copy the generated Placement id in order to use later on.

  

## 4\. Add Prodege SDK in your project

### **4.1. Retrieve Prodege Android SDK through maven**

Retrieve Prodege SDK through **maven()** with gradle by adding the following
line in your app's module **build.gradle** file:

    
    
    dependencies {
        implementation 'com.prodege:prodege:7.0.0-beta07'
    }
    

  

### **4.2. Manual installation**

> **Note:** If you are using Android Studio, right click on your project and
> select New Module. Then select Import .JAR or .aar Package option and from
> the file browser locate the `.aar` file. Right click again on your project
> and in the Module Dependencies tab choose to add the module that you
> recently added, as a dependency.

### 4.2.1 Download Prodege Android SDK `.aar` file and import it into your
project's libraries

Click
[here](https://storage.googleapis.com/pollfish_production/sdk/Android/Prodege%20Android%20SDK-7.0.0-beta07.zip)
to download the latest version of Prodege SDK.

**For Java based projects** you will have to include the Kotlin runtime
library in your module dependencies and set the java to version 1.8.

    
    
    android {
        // ...
        
        compileOptions {
            sourceCompatibility JavaVersion.VERSION_1_8
            targetCompatibility JavaVersion.VERSION_1_8
        }
    }
    
    dependencies {
        // ...
        
        implemetation 'org.jetbrains.kotlin:kotlin-stdlib:1.9.0'
    }
    

> **Note:** Skipping this step will result to runtime exception during the SDK
> initialization.

  

### 4.2.2 Add Google Play Advertising Identifier library to your project
(Optional)

Applications that integrate Prodege SDK may use Google Play Services library
in order to give access to the Advertising ID of a device to the SDK. Further
details regarding integration with the Google Play services library can be
found [here](https://developers.google.com/android/guides/setup). By skipping
this step you have to provide a userId during initialization. Refer to section
6 for more details.

    
    
    dependencies {
        implementation 'com.google.android.gms:play-services-ads-identifier:18.0.1'
    }
    

  

### **4.3. Add Advertising Id permission for Android 12+ (Optional if manual
installation without Google Play Advertising Identifier library integration)**

Apps updating their target API level to 31 (Android 12) or higher will need to
declare a Google Play services normal permission in the AndroidManifest.xml
file.

    
    
    <uses-permission android:name="com.google.android.gms.permission.AD_ID" />
    

You can read more about Google Advertising ID changes
[here](https://support.google.com/googleplay/android-
developer/answer/6048248).

  

### **4.4. Add support for cleartext http traffic (Optional)**

If you are looking to use Prodege Mediation surveys from all the providers, in
order to avoid any faulty behaviour on new Android devices we would advice
that you allow cleartext http traffic for the following domains. To achieve
that you need to:

  1. Donwload [ this file ](https://raw.githubusercontent.com/pollfish/android-sdk-pollfish/b94e812c8b61ad1ac72c16cd63892168c892a04c/resources/domain_whitelist.xml) and place it under **`res/xml`** directory.

  2. In your AndroidManifest.xml file add **`android:networkSecurityConfig`** tag as below:

    
    
     <application
        ...
        android:networkSecurityConfig="@xml/domain_whitelist">
    

  

## 5\. Initialize Prodege SDK

In order to initialize Prodege SDK, you will need a `Context` and the api key
as provided by the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/) in step 2. We advise to
call `Prodge.initialize` as soon as possible within your application's
lifecycle, for example in the `onCreate()` mehod of your `Application` or
`Activity` class. This will initialize Prodege SDK with default configuration.
Read further for additional configuration options and notfications on the
initialization result.

Kotlin:

    
    
    Prodege.initialize(context, "API_KEY")
    

Java:

    
    
    Prodege.initialize(context, "API_KEY", null, null);
    

  

### **5.1. Configure Prodege SDK initialization (Optional)**

You can use any of the additional configuration options to control the
behaviour of the Prodege SDK by creating an `InitOptions.Builder` instance and
build upon it.

Kotlin:

    
    
    import com.prodege.builder.InitOptions
    
    val optionsBuilder = InitOptions.Builder()
    

Java:

    
    
    import com.prodege.builder.InitOptions;
    
    InitOptions.Builder optionsBuilder = new InitOptions.Builder();
    

Below you can see all the available options.

No| Option  
---|---  
5.1.1| **`.userId(String)`**  
A unique identifier used to identify a user.  
5.1.2| **`.testMode(Boolean)`**  
Toggle Prodege SDK test mode.  
5.1.3| **`.userProperties(UserProperties)`**  
Provides user attributes upfront during initialization (only relevant with
surveys).  
5.1.4| **`.advertisingOptOut(Boolean)`**  
Opts out from the use of the device's advertising identifier.  
  
  

### 5.1.1. `.userId(String)`

A unique identifier used to identify a user.

Setting the `userId` will override the default behaviour and use that instead
of the Advertising Id in order to identify a user.

> **Note:** You can pass the id of a user as identified on your system.
> Prodege will use this id to identify the user across sessions instead of an
> ad id/idfa as advised by the stores. You are solely responsible for aligning
> with store regulations by providing this id and getting relevant consent by
> the user when necessary. Prodege takes no responsibility for the usage of
> this id. In any request from your users on resetting/deleting this id and/or
> profile created, you should be solely liable for those requests.

Kotlin:

    
    
    optionsBuilder.userId("USER_ID")
    

Java:

    
    
    optionsBuilder.userId("USER_ID");
    

> **Note:** Failing to provide a user identifier and missing Google Play
> Advertising Identifier library will result to a failed initialization,
> unless you explicitly request for advertising opt out (section 5.1.4).

  

### 5.1.2. `.testMode(Boolean)`

Toggles the Prodege SDK Test mode.

  * **`true`** is used to show to the developer how Prodege ads will be shown through an app (useful during development and testing).
  * **`false`** is the mode to be used for a released app in any app store (start receiving paid surveys).

> **Note:** You should not be testing in live mode since your account can get
> banned automatically from the system.

Prodege SDK runs by default in live mode. If you would like to test with test
ads:

Kotlin:

    
    
    optionsBuilder.testMode(true)
    

Java:

    
    
    optionsBuilder.testMode(true);
    

  

### 5.1.3. `.userProperties(UserProperties)` (only relevant with surveys)

Provides user attributes upfront during initialization in order to skip or
shorten Demographic surveys.

If you know upfront some user attributes like gender, age, education and
others you can pass them during initialization in order to shorten or skip
entirely Pollfish Demographic surveys and archieve better fill rate and higher
priced surveys.

> **Note:** You need to contact live support on our website to request your
> account to be eligible for submitting demographic info through your app,
> otherwise values submitted will be ignored by default.

> **Note:** You can read more on demographic surveys along with a list with
> all the available options [here](https://www.pollfish.com/docs/demographic-
> surveys).

An example of how you can create and pass a `UserProperties` object during
initialization can be seen below:

  

Kotlin:

    
    
    import com.prodege.builder.UserProperties
    
    val userProperties = UserProperties.Builder()
        .parentalStatus(UserProperties.ParentalStatus.TWO)
        .organizationRole(UserProperties.OrganizationRole.ADVERTISING)
        .numberOfEmployees(UserProperties.NumberOfEmployees.FIFTY_ONE_TO_HUNDREND)
        .educationLevel(UserProperties.EducationLevel.POST_GRADUATE)
        .career(UserProperties.Career.ADVERTISING)
        .income(UserProperties.Income.HIGH_I)
        .maritalStatus(UserProperties.MaritalStatus.SINGLE)
        .gender(UserProperties.Gender.MALE)
        .yearOfBirth(1926)
        .addSpokenLanguage(UserProperties.SpokenLanguage.GREEK)
        .addSpokenLanguage(UserProperties.SpokenLanguage.ENGLISH)
        .customAttribute("key", "value")
        .build()
    
    optionsBuilder.userProperties(userProperties)
    

Java:

    
    
    import com.prodege.builder.UserProperties;
    
    UserProperties userProperties = new UserProperties.Builder()
        .parentalStatus(UserProperties.ParentalStatus.TWO)
        .organizationRole(UserProperties.OrganizationRole.ADVERTISING)
        .numberOfEmployees(UserProperties.NumberOfEmployees.FIFTY_ONE_TO_HUNDREND)
        .educationLevel(UserProperties.EducationLevel.POST_GRADUATE)
        .career(UserProperties.Career.ADVERTISING)
        .income(UserProperties.Income.HIGH_I)
        .maritalStatus(UserProperties.MaritalStatus.SINGLE)
        .gender(UserProperties.Gender.MALE)
        .yearOfBirth(1926)
        .addSpokenLanguage(UserProperties.SpokenLanguage.GREEK)
        .addSpokenLanguage(UserProperties.SpokenLanguage.ENGLISH)
        .customAttribute("key", "value")
        .build();
    
    optionsBuilder.userProperties(userProperties);
    

  

### 5.1.4 `.advertisingOptOut(Boolean)`

Opts out from the use of the device's advertising identifier.

You can explicitly request to opt out from the use of the device's advertising
Id. This will configure Prodege SDK to use a unique session identifier for
each session. In case you skipped the Google Play Advertising Identifier
installation, you should set this option to `true` to avoid initialization
failure.

Providing a user identifier (section 5.1.1) will ignore the dependency on the
device advertising identifier and use that instead of a session identifier.

Prodege SDK runs by default in opt-in mode. If you would like to opt out:

Kotlin:

    
    
    optionsBuilder.advertisingOptOut(true)
    

Java:

    
    
    optionsBuilder.advertisingOptOut(true);
    

  

After configuring the `InitOptions.Builder` instance you can proceed with the
build of the `InitOptions` object and Prodege SDK initialization.

Kotlin:

    
    
    import com.prodege.Prodege
    
    val initOptions = optionsBuilder.build()
    
    Prodege.initialize(context, "API_KEY", listener, initOptions)
    

Java:

    
    
    import com.prodege.Prodege;
    
    InitOptions initOptions = optionsBuilder.build();
    
    Prodege.initialize(context, "API_KEY", listener, initOptions);
    

  

### **5.2. Listen for Prodege SDK initialization result (Optional)**

In order to get notified for the Prodege SDK initialization result you will
have to pass a `ProdegeInitListener` interface implementation:

Kotlin:

    
    
    import com.prodege.Prodege
    import com.prodege.listener.ProdegeException
    import com.prodege.listener.ProdegeInitListener
    
    class YourClass : ProdegeInitListener {
        // ...
    
        private fun initalizeProdegeSdk() {
            // ...
            
            Prodege.initialize(context, "API_KEY", this, initOptions)
        }
    
        override fun onSuccess() {
            // Initialization succeeded
        }
    
        override fun onError(exception: ProdegeException) {
            // Initialization failed
            Log.e(TAG, exception.message)
        }
    }
    

Java:

    
    
    import com.prodege.Prodege;
    import com.prodege.listener.ProdegeException;
    import com.prodege.listener.ProdegeInitListener;
    
    class YourClass implements ProdegeInitListener {
        // ...
        
        private void initializeProdegeSdk() {
            // ...
    
            Prodege.initialize(context, "API_KEY", this, initOptions);
        }
    
        @Override
        public void onSuccess() {
            // Initialization success
        }
    
        public void onError(ProdegeException exception) {
            // Initialization failed
        }
    }
    

  

## 6\. Load a placement

In order to load a Prodege Ad Unit placement, you will just need the placement
id as provided by the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/) in step 3. This will load
a placement with default configuration. Read further for additional
configuration options and notfications on the loading result.

Depending on the AdUnit type you should use the corresponding method to load
your placement.

### **6.1. Load a Rewarded Ad Unit placement**

Kotlin:

    
    
    Prodege.loadRewardedAd("PLACEMENT_ID")
    

Java:

    
    
    Prodege.loadRewardedAd("PLACEMENT_ID", null, null);
    

  

### 6.1.1. Listen for the placement loading result (Optional)

In order to get notified for the placement loading result you will have to
pass a `ProdegeRewardedLoadListener` interface implementation:

Kotlin:

    
    
    import com.prodege.Prodege
    import com.prodege.listener.ProdegeRewardedInfo
    import com.prodege.listener.ProdegeRewardedLoadListener
    import com.prodege.listener.ProdegeException
    
    class YourClass : ProdegeRewardedLoadListener {
        // ...
    
        private fun loadRewardedAd() {
            Prodege.loadRewardedAd("PLACEMENT_ID", this)
        }
    
        override fun onRewardedLoaded(placementId: String, info: ProdegeRewardedInfo) {
            // Rewarded Ad loaded
        }
    
        override fun onRewardedLoadFailed(placementId: String, exception: ProdegeException) {
            // Rewarded Ad failed to load
        }
    }
    

Java:

    
    
    import com.prodege.Prodege;
    import com.prodege.listener.ProdegeRewardedInfo;
    import com.prodege.listener.ProdegeRewardedLoadListener;
    import com.prodege.listener.ProdegeException;
    
    class YourClass implements ProdegeRewardedLoadListener {
        // ...
        
        private void loadRewardedAd() {
            Prodege.loadRewardedAd("PLACEMENT_ID", this, null);
        }
    
        @Override
        public void onRewardedLoaded(@NonNull String placementId, @NonNull ProdegeRewardedInfo prodegeRewardedInfo) {
            // Rewarded Ad loaded
        }
    
        @Override
        public void onRewardedLoadFailed(@NonNull String placementId, @NonNull ProdegeException e) {
            // Rewarded Ad failed to load
        }
    }
    

  

**`ProdegeRewardedInfo`**

This object contains information about the received Rewarded Ad.

The `ProdegeRewardedInfo` interface has two implementation depending on the
received Ad format, containing additional information on each sub-type.

    
    
    interface ProdegeRewardedInfo {
        val points: Int
        val currency: String
        val placement: String
    }
    

Field| Description  
---|---  
**`points`**|  The virtual reward value as calculated via a given exchange
rate on the [Publisher Dashboard](https://www.pollfish.com/dashboard/dev/).  
**`currency`**|  The virtual reward name as specified on [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/).  
**`placement`**|  The placement id of the received ad.  
  
  

**`ProdegeRewardedAdInfo`**

    
    
    data class ProdegeRewardedAdInfo(
        override val points: Int,
        override val currency: String,
        override val placement: String,
        val type: ProdegeRewardedAdType,
        val skippable: Boolean
    ) : ProdegeRewardedInfo
    

  

Field| Description  
---|---  
**`type`**|  The type of the received ad. Can be
`ProdegeRewardedAdType.SURVEY` or `ProdegeRewardedAdType.VIDEO`  
**`skippable`**|  Flag indicating whether the ad is sippable or not.  
  
  

**`ProdegeRewardedSurveyInfo`**

    
    
    data class ProdegeRewardedSurveyInfo(
        override val points: Int,
        override val currency: String,
        override val cpa: Int,
        override val placement: String,
        override val surveyClass: String?,
        override val remainingCompletes: Int?,
        override val incidenceRate: Int?,
        override val lengthOfInterview: Int?
    ) : ProdegeRewardedInfo, SurveyStats
    

  

Field| Description  
---|---  
**`cpa`**|  Money to be earned from the survey received in US dollar cents
(estimated based on daily exchange currency).  
**`surveyClass`**|  Information about the survey network and type.  
**`remainingCompletes`**|  The number of remaining completes for the survey.  
**`incidenceRate`**|  The current estimation for the survey incidence rate as
an integer number in the range 0-100. This param is optional and will have as
default the value -1 if it was not set and the IR was not computed reliably.  
**`lengthOfInterview`**|  The expected time in minutes that it takes to
complete the survey. This param is optional and will have as default the value
-1 if it was not set and the LOI was not computed reliably.  
  
  

The syntax for survey_class values is:

    
    
    survey_class: provider["/"type]
    provider: "Pollfish" | "Toluna" | "Cint" | "InnovateMR" | "SaySo" | "Dynata" | "Yuno" | "PureSpectrum" | "Opinionetwork" | "SchlesingerGroup" | "YunoRouter" | "IpsosMediation" | "ProdegeMR" | "MR" | "Samplicious" | "IRB" | "PollfishSwarm"
    type: "Basic" | "Playful" | "ThirdParty" | "Demographics" | "Internal"
    

which is the network name followed by an optional slash and survey type.

The provider is the network that provides the survey. The syntax rule has all
the networks currently supported by Prodege.

The type is that of the survey as described in the network's documentation.
The exception is the type "Demographics" which is always used to identify
surveys whose purpose is to collect demographic data for the users.

The whole set of values currently supported are:

Value| Description  
---|---  
**`Pollfish`**|  Pollfish Basic survey  
**`Pollfish/Basic`**|  Pollfish Basic survey (another name)  
**`Pollfish/Playful`**|  Pollfish Playful survey  
**`Pollfish/ThirdParty`**|  Pollfish 3rd party survey  
**`Pollfish/Demographics`**|  Pollfish Demographic survey  
**`Pollfish/Internal`**|  Pollfish internal survey created by the publisher  
**`Toluna`**|  Toluna survey  
**`Cint`**|  Cint survey  
**`InnovateMR`**|  InnovateMR survey  
**`SaySo`**|  SaySo survey  
**`Dynata`**|  Dynata survey  
**`Yuno`**|  Yuno survey  
**`PureSpectrum`**|  PureSpectrum survey  
**`Opinionetwork`**|  Opinionetwork survey  
**`SchlesingerGroup`**|  SchlesingerGroup survey  
**`YunoRouter`**|  YunoRouter survey  
**`IpsosMediation`**|  IpsosMediation survey  
**`ProdegeMR`**|  ProdegeMR survey  
**`MR`**|  MR survey  
**`Samplicious`**|  Samplicious survey  
**`IRB`**|  IRB survey  
**`PollfishSwarm`**|  PollfishSwarm survey  
  
  

> **Note:** When a new mediation network enters the Prodege network the
> appropriate values will be added.

  

### **6.2. Load an Offerwall Ad Unit placement**

Kotlin:

    
    
    Prodege.loadOfferwall("PLACEMENT_ID")
    

Java:

    
    
    Prodege.loadOfferwall("PLACEMENT_ID", null, null)
    

  

### 6.2.1. Listen for the offerwall loading result (Optional)

In order to get notified for the placement loading result you will have to
pass a `ProdegeOfferwallLoadListener` interface implementation:

Kotlin:

    
    
    import com.prodege.Prodege
    import com.prodege.listener.ProdegeOfferwallLoadListener
    import com.prodege.listener.ProdegeException
    
    class YourClass : ProdegeOfferwallLoadListener {
        // ...
    
        private fun loadOfferwall() {
            Prodege.loadOfferwall("PLACEMENT_ID", this)
        }
    
        override fun onOfferwallLoaded(placementId: String) {
            // Offerwall loaded
        }
    
        override fun onRewardedLoadFailed(placementId: String, exception: ProdegeException) {
            // Offerwall failed to load
        }
    }
    

Java:

    
    
    import com.prodege.Prodege;
    import com.prodege.listener.ProdegeOfferwallLoadListener;
    import com.prodege.listener.ProdegeException;
    
    class YourClass implements ProdegeOfferwallLoadListener {
        // ...
        
        private void loadOfferwall() {
            Prodege.loadOfferwall("PLACEMENT_ID", this, null);
        }
    
        @Override
        public void onOfferwallLoaded(@NonNull String placementId) {
            // Offerwall loaded
        }
    
        @Override
        public void onRewardedLoadFailed(@NonNull String placementId, @NonNull ProdegeException e) {
            // Offerwall failed to load
        }
    }
    

  

### **6.3. Configure your Placement Ad request (Optional)**

You can use any of the additional configuration options to configure your
placement load request by creating an `AdRequest.Builder` instance and build
upon it.

Kotlin:

    
    
    import com.prodege.builder.AdRequest
    
    val adRequestBuilder = AdRequest.Builder()
    

Java:

    
    
    import com.prodege.builder.AdRequest;
    
    AdRequest.Builder adRequestBuilder = new AdRequest.Builder();
    

Below you can see all the available options.

No| Option  
---|---  
6.3.1| **`.clickId(String)`**  
A pass through param that will be passed back through server-to-server
callback.  
6.3.2| **`.requestUuid(Boolean)`**  
Sets a pass-through param to be receive via the server-to-server callbacks.  
6.3.3| **`.rewardInfo(RewardInfo)`**  
An object holding information regarding the survey completion reward.  
  
  

### 6.3.1. `.clickId(String)`

A pass through parameter that will be returned back to the publisher through
server-to-server callbacks as specified
[here](https://www.pollfish.com/docs/s2s).

  

Kotlin:

    
    
    adRequestBuilder.clickId("CLICK_ID")
    

Java:

    
    
    adRequestBuilder.clickId("CLICK_ID");
    

  

### 6.3.2. `.requestUuid(String)`

A pass-through parameter that will be returned back to the publisher through
server-to-server callbacks as specified
[here](https://www.pollfish.com/docs/s2s).

  

Below you can see an example on how you can pass a requestUUID during
initialization:

  

Kotlin:

    
    
    adRequestBuilder.requestUuid("REQUEST_UUID")
    

Java:

    
    
    adRequestBuilder.requestUuid("REQUEST_UUID");
    

  

### 6.3.3. `.rewardInfo(RewardInfo)`

An object passing information regarding the reward settings, overriding the
values as speciefied on the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/).

We strogly advise that you should use the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/) to provide Reward Info if
your use case does not require a dynamic value.

    
    
    data class RewardInfo(
        val points: String,
        val conversionRate: Double,
        val signature: String
    )
    

  

Field| Description  
---|---  
**`rewardName`**|  Overrides the reward name as specified in the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/).  
**`rewardConversion`**|  Overrides the reward conversion as specified on the
[Publisher Dashboard](https://www.pollfish.com/dashboard/dev/). Conversion is
expecting a number matching this function (`1 USD = X Points`) where `X` is a
`Double` number.  
**`signature`**|  A parameter used to secure the `rewardName` and
`rewardConversion`.  
  
  

`signature` parameter is used to prevent tampering around reward conversion.
The platform supports url validation by requiring a hash of the
`rewardConversion`, `rewardName`, and `clickId`. Failure to pass validation
will result in no ads.

In order to generate the `signature` field you should sign the combination of
`${rewardConversion}${rewardName}${clickId}` parameters using the HMAC-SHA1
algorithm and your account's secret_key that can be retrieved from the Account
Information section on your [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/).

  

> **Note:** Although `rewardConversion` and `rewardName` are mandatory for the
> hashing to work, `clickId` parameter is optional and you should add them for
> extra security.

  

> **Note:** Please keep in mind if your `rewardConversion` is a whole number,
> you have to calculate the signature useing the floating point value with 1
> decimal point.

  

Sample code to generate valid signatures

Kotlin:

    
    
    import java.util.*
    import javax.crypto.Mac
    import javax.crypto.spec.SecretKeySpec
    
    val rewardConversion = 2.0
    val rewardName = "Dollars"
    val clickId = "CLICK_ID"
    val secretKey = "ACCOUNT_SECRET_KEY"
    
    val valueToSign = "$rewardConversion$rewardName$clickId"
    
    val signingKey = SecretKeySpec(secretKey.toByteArray(Charsets.UTF_8), "HmacSHA1")
    val mac = Mac.getInstance("HmacSHA1")
    mac.init(secretKey)
    
    val signature = Base64.getEncoder().encodeToString(mac.doFinal(valueToSign.toByteArray(Charsets.UTF_8)))
    

Java:

    
    
    import java.util.*;
    import javax.crypto.Mac;
    import javax.crypto.spec.SecretKeySpec;
    import java.nio.charset.StandardCharsets;
    
    double rewardConversion = 2.0;
    String rewardName = "Dollars";
    String clickId = "CLICK_ID";
    String secretKey = "ACCOUNT_SECRET_KEY";
    
    String valueToSign = "" + rewardConversion + rewardName + clickId;
    
    SecretKeySpec signingKey = new SecretKeySpec(secretKey.getBytes(StandardCharsets.UTF_8), "HmacSHA1");
    Mac mac = Mac.getInstance("HmacSHA1");
    mac.init(signingKey);
    
    String signature = Base64.getEncoder().encodeToString(mac.doFinal(valueToSign.getBytes(StandardCharsets.UTF_8)));
    

  

Kotlin:

    
    
    import com.prodege.builder.RewardInfo
    
    val rewardInfo = RewardInfo("Diamonds", 1.1, "SIGNATURE")
    
    adRequestBuilder.rewardInfo(rewardInfo)
    

Java:

    
    
    import com.prodege.builder.RewardInfo;
    
    val rewardInfo = new RewardInfo("Diamonds", 1.1, "SIGNATURE");
    
    adRequestBuilder.rewardInfo(rewardInfo);
    

  

After configuring the `AdRequest.Builder` instance you can proceed with the
build of the `AdRequest` object and Placement loading.

Kotlin:

    
    
    import com.prodege.Prodege
    
    val adRequest = adRequestBuilder.build()
    
    Prodege.loadRewardedAd("PLACEMENT_ID", listener, adRequest)
    // OR
    Prodege.loadOfferwall("PLACEMENT_ID", listener, adRequest)
    

Java:

    
    
    import com.prodege.Prodege;
    
    AdRequest adRequest = adRequestBuilder.build();
    
    Prodege.loadRewardedAd("PLACEMENT_ID", listener, adRequest);
    // OR
    Prodege.loadOfferwall("PLACEMENT_ID", listener, adRequest);
    

  

## 7\. Show the placement

After the successful load of a placement you can call `Prodege.showPlacement`
to show a placement.

Kotlin:

    
    
    Prodege.showPlacement("PLACEMENT_ID")
    

Java:

    
    
    Prodege.showPlacement("PLACEMENT_ID", null, null);
    

  

### **7.1. Listen for ad visibility updates (Optional)**

You can get notified when an ad has opened, closed or failed to present.
Publishers usually use this notification to pause a game until the ad is
closed again.

Kotlin:

    
    
    import com.pordege.Prodege
    import com.prodege.listener.ProdegeShowListener
    import com.prodege.listener.ProdegeException
    
    class YourClass : ProdegeShowListener {
        // ...
    
        private fun showPlacement() {
            Prodege.showPlacement("PLACEMENT_ID", this)
        }
    
        override fun onClosed(placement: String) {
            // Placement closed
        }
    
        override fun onOpened(placement: String) {
            // Placement opened
        }
        override fun onShowFailed(placement: String, exception: ProdegeException) {
            // Placement failed to show
        }
    }
    

Java:

    
    
    import com.pordege.Prodege;
    import com.prodege.listener.ProdegeShowListener;
    import com.prodege.listener.ProdegeException;
    
    public class YourClass implements ProdegeShowListener {
        // ...
    
        private void showPlacement() {
            Prodege.showPlacement("PLACEMENT_ID", this, null);
        }
    
        @Override
        public void onClosed(@NonNull String placementId) {
            // Placement closed
        }
    
        @Override
        public void onOpened(@NonNull String placementId) {
            // Placement opened
        }
    
        @Override
        public void onShowFailed(@NonNull String placementId, @NonNull ProdegeException e) {
             // Placement failed to show
        }
    
    }
    

  

### **7.2. Configure the placement presentation**

You can use any of the additional configuration options to configure your
placement's presentation by creating an `AdOptions.Builder` instance and build
upon it.

Kotlin:

    
    
    import com.prodege.builder.AdOptions
    
    val adOptionsBuilder = AdOptions.Builder()
    

Java:

    
    
    import com.prodege.builder.AdOptions;
    
    AdOptions.Builder adOptionsBuilder = new AdOptions.Builder();
    

Below you can see all the available options.

No| Option  
---|---  
7.2.1| **`.muted(Boolean)`**  
Sets Prodege video ads mute state.  
  
  

### 7.2.1. `.muted(Boolean)`

Sets Prodege video ads mute state.

  

Kotlin:

    
    
    adOptionsBuilder.muted(true)
    

Java:

    
    
    adOptionsBuilder.clickId(true);
    

  

After configuring the `AdRequest.Builder` instance you can proceed with the
build of the `AdRequest` object and Placement loading.

Kotlin:

    
    
    import com.prodege.Prodege
    
    val adOptions = adOptionsBuilder.build()
    
    Prodege.showPlacement("PLACEMENT_ID", listener, adOptions)
    // OR
    Prodege.showPlacement("PLACEMENT_ID", listener, adOptions)
    

Java:

    
    
    import com.prodege.Prodege;
    
    AdOptions adOptions = adOptionsBuilder.build();
    
    Prodege.showPlacement("PLACEMENT_ID", listener, adOptions);
    // OR
    Prodege.showPlacement("PLACEMENT_ID", listener, adOptions);
    

  

## 8\. Update your privacy policy and publish your app

Add the following paragraph to your app's privacy policy:

  

_Offer Serving Technology_

_This app uses Prodege SDK. Prodege is an on-line offer platform, through
which, app users are exposed to market research surveys and/or third-party ads
(âOffersâ). Prodege collaborates with publishers of applications for
smartphones in order to have access to users of such applications and address
Offers to them. When a user connects to this app, a specific set of user's
device data (including Advertising ID, Device ID, if and where the app-user
has enabled access to his/her Advertising and/or Device ID, either through his
system's settings or via a consent-prompt shown to him) and further response
meta-data is automatically sent, via our app, to Prodege servers in order for
Prodege to be able to serve Offers through our app. Prodege collects and
processes your data in accordance with all applicable law requirements. For a
full list of data received by Prodege through this app, and for further
information on how Prodege processes such data please read carefully Prodege
Privacy Policy for Users of Apps collaborating with Prodege available at
https://www.pollfish.com/terms/respondent. Your data may be transferred by
Prodege to non-EEA countries in accordance with all applicable law
requirements, including use of EU Commission Standard Contractual Clauses.
Prodege may share such data with third parties, clients and business partners,
for commercial purposes. By downloading the application, you accept this
privacy policy document and you hereby give your consent for the processing by
Prodege of the aforementioned data. Furthermore, you are informed that you may
disable Prodege operation at any time by visiting the following link
https://www.pollfish.com/respondent/opt-out. We once more invite you to check
the Prodege Privacy Policy, if you wish to have more detailed view of the way
Prodege works and with whom Prodege may further share your data._

  

> **Note:** It's important that you include this disclosure both in the
> privacy policy posted on Google Play but also in the privacy policy included
> in your app, as described in [Google's Developer Privacy
> Policy](https://play.google.com/about/privacy-security/personal-sensitive/)

**At this point you are ready to go live! Sign your app with a release key,
make sure you are not in test mode publish to any Android app store**

> **Note (for publishers using surveys):** Please bear in mind that the first
> time a user is introduced to the platform, when no paid surveys are
> available, a Standalone Demographic survey will be shown, as a way to
> increase the user's exposure in our clients' survey inventory. This survey
> returns no payment to app publishers, since it is part of the process that
> users need to go through, in order to join the platform. Our aim is to
> provide advanced targeting solutions to our customers and to do that we need
> to have this information. Targeting by marital status or education etc. are
> highly popular options in the survey world and we need to keep up with the
> market research. A vast majority of our clients are looking for this option
> when using the platform. Based on previous data, over 80% of the surveys
> designed on the platform require this type of targeting. Demographic surveys
> fire s2s callbacks with CPA=0. Publishers can provide rewards for users to
> incentivize them in completing the demographic surveys to get access to
> actual surveys.

In our efforts to include publishers and be as transparent as possible we
provide full control over the process. We let publishers decide if their users
are served these standalone surveys or not, in 2 different ways. Firstly by
monitoring the process in code and excluding any users by listening to the
relevant noitifications and checking the Cost Per Action (CPA) field which
will be 0 USD cents and also Survey Type which will be
`Pollfish/Demographics`. Secondly, publishers can disable the Standalone
Demographic surveys through the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/) in the Settings area of an
app. You can read more on demographic surveys
[here](https://www.pollfish.com/docs/demographic-surveys).

If you know attributes about a user like gender, age and others, you can
provide them during initialization as described in section 5.3.1.8 and skip or
shorten this way, Pollfish Demographic surveys.

  

### **8.1. Complete the Google Play Data Safety questionnaire**

When you publish your app your will be asked to complete the Google Play Data
Safety questionnaire. For any info relevant to data collected and used from
the Prodege SDK please advice the following
[link](https://www.pollfish.com/terms/google-play-data-safety-questionnaire).
For Prodege SDK the only questions that should be answered is under the **Data
types** step, **Device or other IDs** section. Please select the checkbox:

  

![](https://storage.googleapis.com/pollfish_production/doc_images/google-play-
data-safety.png)

  

After selecting the above checkbox, you will be prompted to answer a
questionnaire regarding the **Device or other IDs** on the **Data usage and
handling** step. Please answer the questionnaire with the following suggested
answers:

â¤ **Questionnaire Answers** (Click to expand)

Question| Answer  
---|---  
**Is this data collected, shared, or both?**  
Collected| YES  
Shared| YES  
**Is this data processed ephemerally?**|  NO  
**Is this data required for your app, or can users choose whether it's
collected?**|  Users can choose whether this data is collected  
**Why is this user data collected?**|  
Advertising or marketing| YES  
**Why is this user data shared?**|  
Advertising or marketing| YES  
  
  

## 9\. Request your account to get verified

After your app is published on an app store you should request your account to
get verified from the [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/).

![](https://storage.googleapis.com/pollfish_production/doc_images/verify_account.png)  

When your account is verified you will be able to start receiving paid surveys
from Prodege clients.

> **Note:** Review process can take from a few minutes to a few hours
> depending on the 24/7 Review Team availability.

  

# Optional section

## 10\. Receive event notifications

You can register and receive callback notification for various events during
the lifecycle of an ad by providing a `ProdegeEventListener` interface
implementation.

Kotlin:

    
    
    import com.prodege.Prodege
    import com.prodege.listener.ProdegeEventListener
    
    class YourClass : ProdegeEventListener {
        
        // See method overrides below
    
        private fun initializeProdegeSDK() {
            // ...
            
            Prodege.setEventListener(this)
        }
    }
    

Java:

    
    
    import com.prodege.Prodege;
    import com.prodege.listener.ProdegeEventListener;
    
    public class YourClass implements ProdegeEventListener {
        // See method overrides below
    
        private void initializeProdegeSDK() {
            // ...
            
            Prodege.setEventListener(this);
        }
    }
    

  

### **10.1.`fun onStart(placement: String)`**

Override `onStart` method to receive a notification when a video ad starts
playing.

Kotlin:

    
    
    override fun onStart(placement: String) {
        // Video ad started
    }
    

Java:

    
    
    @Override
    public void onStart(@NonNull String placementId) {
       // Video ad started
    }
    

  

### **10.2.`fun onComplete(placement: String)`**

Override `onComplete` method to receive a notification when an ad is
completed.

Kotlin:

    
    
    override fun onComplete(placement: String) {
        // Placement completed
    }
    

Java:

    
    
    @Override
    public void onComplete(@NonNull String placementId) {
         // Placement completed
    }
    

  

### **10.3.`fun onUserReject(placement: String)`**

Override `onUserReject` method to receive a notfication when a user rejects an
ad.

Kotlin:

    
    
    override fun onUserReject(placement: String) {
        // User rejected placement
    }
    

Java:

    
    
    @Override
    public void onUserReject(@NonNull String placementId) {
        // User rejected placement
    }
    

  

### **10.4.`fun onUserNotEligible(placement: String)`**

Override `onUserNotEligible` method to receive a notification when a user is
not eligible for an ad.

In market research monetization users can get screened out while completing a
survey because they are not relevant with audience that the market researcher
was looking for. In that case the user not eligible notification will fire and
the publisher will make no money from that survey. User not eligible
notification will fire after survey received when user starts completing the
survey.

Kotlin:

    
    
    override fun onUserReject(placement: String) {
        // User not eligible
    }
    

Java:

    
    
    @Override
    public void onUserNotEligible(@NonNull String placementId) {
        // User not eligible
    }
    

  

### **10.5.`fun onClick(placement: String)`**

Override `onClick` method to receive a notification when a user clicks through
an ad.

Kotlin:

    
    
    override fun onClick(placement: String) {
        // User clicked
    }
    

Java:

    
    
    @Override
    public void onClick(@NonNull String placementId) {
        // User clicked
    }
    

  

## 11\. Receive reward notifications

You can register and receive notifications when a user receives a reward by
providing a `ProdegeRewardListenerImplementation`.

Kotlin:

    
    
    import com.prodege.Prodege
    import com.prodege.listener.ProdegeRewardListener
    import com.prodege.listener.ProdegeReward
    
    class YourClass : ProdegeRewardListener {
        
        override fun onRewardReceived(reward: ProdegeReward) {
            // Reward received
        }
    
        private fun initializeProdegeSDK() {
            // ...
            
            Prodege.setRewardListener(this)
        }
    }
    

Java:

    
    
    import com.prodege.Prodege;
    import com.prodege.listener.ProdegeRewardListener;
    import com.prodege.listener.ProdegeReward;
    
    public class YourClass implements ProdegeRewardListener {
    
        @Override
        public void onRewardReceived(@NonNull ProdegeReward prodegeReward) {
            // Reward received
        }
    
        private void initializeProdegeSDK() {
            // ...
            
            Prodege.setRewardListener(this);
        }
    }
    

**`ProdegeReward`**

This object contains information about the received reward.

The `ProdegeReward` interface has two implementation depending on the received
Ad format, containing additional information on each sub-type.

    
    
    interface ProdegeReward {
        val points: Int
        val currency: String
        val placement: String
    }
    

Field| Description  
---|---  
**`points`**|  The virtual reward value as calculated via a given exchange
rate on the [Publisher Dashboard](https://www.pollfish.com/dashboard/dev/).  
**`currency`**|  The virtual reward name as specified on [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/).  
**`placement`**|  The placement id of the received ad.  
  
  

**`ProdegeAdReward`** is just an implementation of the `ProdegeReward`
interface, which does not include any additional information.

    
    
    data class ProdegeAdReward(
        override val points: Int,
        override val currency: String,
        override val placement: String
    ) : ProdegeReward
    

  

**`ProdegeSurveyReward`** contains some additional information around the
completed survey.

    
    
    data class ProdegeSurveyReward(
        override val points: Int,
        override val currency: String,
        override val cpa: Int,
        override val placement: String,
        override val surveyClass: String?,
        override val remainingCompletes: Int?,
        override val incidenceRate: Int?,
        override val lengthOfInterview: Int?
    ) : ProdegeReward, SurveyStats
    

  

## 12\. Additional Prodege SDK helper methods

### **12.1. Check if Prodege SDK is initialized**

You can check at any time whether the SDK is initialized by calling the
following method:

Kotlin:

    
    
    Prodege.isInitialized()
    

Java:

    
    
    Prodege.isInitialized();
    

  

### **12.2. Check if a placement is loaded**

You can check at any time whether a placement is loaded by calling the
following method:

Kotlin:

    
    
    Prodege.isPlacementLoaded("PLACEMENT_ID")
    

Java:

    
    
    Prodege.isPlacementLoaded("PLACEMENT_ID");
    

  

### **12.3. Check if a placement is visible**

You can check at any time whether a placement is visible to the user by
calling the following method:

Kotlin:

    
    
    Prodege.isPlacementVisible("PLACEMENT_ID")
    

Java:

    
    
    Prodege.isPlacementVisible("PLACEMENT_ID");
    

  

### **12.4. Get the user identifier**

You can check at any time which is the currect identifier and its type, that
the SDK is using to identify a user.

This will return an object of type `IdentifierInfo` containing various info
such as the identifier the type and the opt-out setting.

The type can be `ADVERTISING`, `SESSION` or `USER_ID`.

    
    
    data class IdentifierInfo(
        val userId: String,
        val type: IdentifierType,
        val optOut: Boolean
    )
    

  

### **12.5. Hide a placement**

You can manually hide a placement by calling:

Kotlin:

    
    
    Prodege.hide("PLACEMENT_ID")
    

Java:

    
    
    Prodege.hide("PLACEMENT_ID");
    

or you can manually hide all placements by calling:

Kotlin:

    
    
    Prodege.hideAll()
    

Java:

    
    
    Prodege.hideAll();
    

  

## 13\. Proguard

If you use proguard with your app, please insert the following lines in your
proguard configuration file:

    
    
    -dontwarn com.prodege.**
    -keep class com.prodege.** { *; }
    

  

## 14\. Minimum SDK version

Prodege SDK requires at minimum Android API 21 in order to work. You can still
build your app if your app minimum target is lower than 21.

**AndroidManifest.xml**

    
    
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
        xmlns:tools="http://schemas.android.com/tools">
    
        <uses-sdk tools:overrideLibrary="com.prodege" />
    
        <!-- ... -->
    

**app/build.gradle**

    
    
    defaultConfig {
        // ...
    
        multiDexEnabled true
    }
    
    dependencies {
        // ...
    
        implementation 'androidx.multidex:multidex:2.0.1'
    }
    

  

## 15\. Server-to-server callbacks upon conversion

If you want to reward your users for completing a ad it is common practice to
verify this through server to server callbacks in order to introduce an
enhanced security layer to your system. You can easily add your postback url
on your app's page on [Publisher
Dashboard](https://www.pollfish.com/dashboard/dev/). You can read more on how
to set server to server callbacks [here](https://www.pollfish.com/docs/s2s).

  

## 16\. Payouts on Screenouts

In Market Research monetization users can get screened out within the survey
since the Researcher might be looking a different user based on the provided
answers. Screenouts do not deliver any revenue for the publisher nor any
reward for the users. If you would like to activate payouts on screenouts too
please follow the steps as described [here](https://www.pollfish.com/docs/pay-
on-screenouts).

We are proud of the professional experience that we have gained over the years
by working for small and high-profile clients. Our experience expands to some
of the most beloved and well-known brands on the planet.

About

Researcher

Publisher

Respondent

  * [Contact](https://www.pollfish.com/contact)
  * [Company](https://www.pollfish.com/team)
  * [Pollfish & Prodege](https://www.pollfish.com/pollfish-and-prodege/)
  * [Careers](https://prodege.hrmdirect.com/employment/job-openings.php?search=true&city=Athina&state=-1&office=-1)
  * [Blog](http://www.pollfish.com/blog)
  * [Media Kit](https://www.pollfish.com/company/mediakit)

  * [FAQ](https://help.pollfish.com/faq-researchers)
  * [Case studies](https://resources.pollfish.com/case-studies/)

  * [Android documentation](https://www.pollfish.com/docs/android/google-play)
  * [Android v7 (Beta) documentation](https://www.pollfish.com/docs/android-v7)
  * [iOS documentation](https://www.pollfish.com/docs/ios)
  * [Web Plugin documentation](https://www.pollfish.com/docs/webplugin)
  * [Other Plugins](https://www.pollfish.com/docs/unity)
  * [Server-to-Server Callbacks](https://www.pollfish.com/docs/s2s)
  * [Rewarded Surveys](https://www.pollfish.com/docs/rewarded-surveys)
  * [Offerwall](https://www.pollfish.com/docs/offerwall)
  * [Pay on Screenouts](https://www.pollfish.com/docs/pay-on-screenouts)
  * [Demographic Surveys](https://www.pollfish.com/docs/demographic-surveys)
  * [Mediation Platform](https://www.pollfish.com/docs/mediation)
  * [API Documentation](https://www.pollfish.com/docs/api-documentation)
  * [Dashboard API](https://www.pollfish.com/docs/dashboard-api)
  * [Referral](https://www.pollfish.com/publisher/referral)
  * [Case studies](https://pollfish.com/case-studies/)
  * [Demo Apps](https://www.pollfish.com/publisher/demo)
  * [FAQ](https://help.pollfish.com/faq-publishers)

  * [Opt out](https://www.pollfish.com/respondent/opt-out)

[Contact â](https://www.pollfish.com/contact)

[
__](https://www.facebook.com/pollfish)[__](https://www.twitter.com/pollfish)[__](https://www.linkedin.com/company/pollfish)

Terms of Service:[Researcher](https://www.pollfish.com/terms/researcher) | [Publisher](https://www.pollfish.com/terms/publisher) | [Respondent](https://www.pollfish.com/terms/respondent)

Â© 2024 Pollfish. All Rights Reserved

