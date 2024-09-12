JavaScript is disabled on your browser.

Skip navigation links

Flurry Android SDK 88.2.0

  * [Overview](../../../index.html)
  * [Package](package-summary.html)
  * Class
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Help](../../../help-doc.html#class)

  * Summary: 
  * Nested | 
  * Field | 
  * Constr | 
  * Method

  * Detail: 
  * Field | 
  * Constr | 
  * Method

SEARCH:

Package [com.flurry.android](package-summary.html)

# Class FlurryAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html
"class or interface in java.lang")

com.flurry.android.FlurryAgent

* * *

public final class FlurryAgent extends
[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html
"class or interface in java.lang")

The Flurry Android Analytics Agent allows you to track the usage and behavior
of your Android application on users' devices for viewing in the Flurry
Analytics system. Set of methods that allow developers to capture detailed,
aggregate information regarding the use of their app by end users.

See Also:

    

  * [Flurry Publisher Support Site](https://developer.yahoo.com/flurry/docs/)

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[FlurryAgent.Builder](FlurryAgent.Builder.html "class in
com.flurry.android")`

Builder Pattern class for FlurryAgent.

`static class `

`[FlurryAgent.UserProperties](FlurryAgent.UserProperties.html "class in
com.flurry.android")`

User Properties class for FlurryAgent.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")`

`VERSION_STRING`



  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static void`

`addOrigin([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originName,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originVersion)`

Add origin attribution.

`static void`

`addOrigin([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originName,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originVersion,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> originParameters)`

Add origin attribution with parameters.

`static void`

`addSessionProperty([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") name,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") value)`

This method allows you to associate parameters with an session.

`static void`

`deleteData()`

This api allows you to delete data collected by Flurry

`static void`

`endTimedEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId)`

End a timed event.

`static void`

`endTimedEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)`

End a timed event with the 2nd key.

`static void`

`endTimedEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters)`

End a timed event with parameters.

`static void`

`endTimedEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)`

End a timed event with parameters and the 2nd key.

`static
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html
"class or interface in java.util")<[FlurryModule](FlurryModule.html "interface
in com.flurry.android")>`

`getAddOnModules()`

Returns a list of the Flurry add-on modules

`static int`

`getAgentVersion()`

Get the version of the Flurry SDK.

`static [Consent](Consent.html "class in com.flurry.android")`

`getFlurryConsent()`

Return Flurry consent set by `updateFlurryConsent(Consent)` or
[`FlurryAgent.Builder.withConsent(Consent)`](FlurryAgent.Builder.html#withConsent\(com.flurry.android.Consent\))

`static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")`

`getInstantAppName()`

Return instant app name.

`static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")`

`getReleaseVersion()`

Get the release version of the Flurry SDK.

`static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")`

`getSessionId()`

Check to see if there is an active session.

`static boolean`

`isInitialized()`

Check to see if FlurryAgent is initialized or not.

`static boolean`

`isSessionActive()`

Check to see if there is an active session.

`static void`

`logBreadcrumb([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") crashBreadcrumb)`



`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logEvent([FlurryEvent](FlurryEvent.html "enum class in com.flurry.android")
event, [FlurryEvent.Params](FlurryEvent.Params.html "class in
com.flurry.android") parameters)`

Log a standard event with suggested parameters and user defined parameters.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId)`

Log an event.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, boolean timed)`

Log a timed event.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)`

Log a timed event with the 2nd key.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters)`

Log an event with parameters.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters, boolean timed)`

Log a timed event with parameters.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logEvent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)`

Log a timed event with parameters and the 2nd key.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logPayment(int responseCode,
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html
"class or interface in
java.util")<[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html
"class or interface in java.lang")> purchases,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters)`

Log a payment from Google.

`static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in
com.flurry.android")`

`logPayment([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") productName,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") productId, int quantity, double price,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") currency,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") transactionId,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters)`

Log a payment.

`static void`

`onEndSession(android.content.Context context)`

End a Flurry session for the given Context.

`static void`

`onError([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") errorId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") errorClass)`

Report errors that your app catches.

`static void`

`onError([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") errorId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") message,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") errorClass,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> errorParams)`

Report errors that your app catches.

`static void`

`onError([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") errorId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") message,
[Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html
"class or interface in java.lang") exception)`

Report errors that your app catches.

`static void`

`onError([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") errorId,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") message,
[Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html
"class or interface in java.lang") exception,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> errorParams)`

Report errors that your app catches.

`static void`

`onStartSession(android.content.Context context)`

Start or continue a Flurry session for the project on the given Context.

`static void`

`openPrivacyDashboard([FlurryPrivacySession.Request](FlurryPrivacySession.Request.html
"class in com.flurry.android") request)`

This api opens privacy dashboard in Chrome CustomTab (if its dependency's been
included in the gradle and device support it as well), otherwise will open it
in the external browser.

`static void`

`registerListener([FlurryAgentListener](FlurryAgentListener.html "interface in
com.flurry.android") listener)`

Registers the listener.

`static void`

`setAge(int age)`

Sets the age of the user at the time of this session.

`static void`

`setCaptureUncaughtExceptions(boolean captureExceptions)`

True to enable or false to disable the ability to catch all uncaught
exceptions and have them reported back to Flurry.

`static void`

`setContinueSessionMillis(long sessionMillis)`

Set the timeout for expiring a Flurry session.

`static void`

`setDataSaleOptOut(boolean isOptOut)`

This api allows you to set opt-out/opt-in for data sale

`static void`

`setGender(byte gender)`

Sets the gender of the user.

`static boolean`

`setGppConsent([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") gppString,
[Set](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Set.html
"class or interface in
java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html
"class or interface in java.lang")> gppSectionIds)`

Set Flurry Consent for the IAB Global Privacy Platform (GPP).

`static void`

`setIncludeBackgroundSessionsInMetrics(boolean
includeBackgroundSessionsInMetrics)`

True if this session should be added to total sessions/DAUs when
applicationstate is inactive or background.

`static void`

`setInstantAppName([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") instantAppName)`

Set instant app name if it's an instant app.

`static void`

`setLogEnabled(boolean enableLog)`

True to enable or false to disable the internal logging for the Flurry SDK.

`static void`

`setLogLevel(int logLevel)`

Set the log level of the internal Flurry SDK logging.

`static void`

`setReportLocation(boolean reportLocation)`

Set whether Flurry should record location via GPS.

`static void`

`setSessionOrigin([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originName,
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") deepLink)`

This method allows you to specify session origin and deep link for each
session.

`static void`

`setSslPinningEnabled(boolean sslPinningEnabled)`

True to enable or false to disable SSL Pinning for Flurry Analytics
connection.

`static void`

`setUserId([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") userId)`

Sets the Flurry userId for this session.

`static void`

`setVersionName([String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") versionName)`

Set the version name of the app.

`static void`

`unregisterListener([FlurryAgentListener](FlurryAgentListener.html "interface
in com.flurry.android") listener)`

Unregisters the listener.

`static boolean`

`updateFlurryConsent([Consent](Consent.html "class in com.flurry.android")
flurryConsent)`

Update Flurry consent.

### Methods inherited from class
java.lang.[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html
"class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#clone\(\)
"class or interface in java.lang"),
[equals](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\)
"class or interface in java.lang"),
[finalize](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#finalize\(\)
"class or interface in java.lang"),
[getClass](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#getClass\(\)
"class or interface in java.lang"),
[hashCode](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#hashCode\(\)
"class or interface in java.lang"),
[notify](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#notify\(\)
"class or interface in java.lang"),
[notifyAll](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#notifyAll\(\)
"class or interface in java.lang"),
[toString](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#toString\(\)
"class or interface in java.lang"),
[wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#wait\(\)
"class or interface in java.lang"),
[wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#wait\(long\)
"class or interface in java.lang"),
[wait](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html#wait\(long,int\)
"class or interface in java.lang")`

  * ## Field Details

    * ### VERSION_STRING

public static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") VERSION_STRING

  * ## Method Details

    * ### isInitialized

public static boolean isInitialized()

Check to see if FlurryAgent is initialized or not. Note: Before FlurryAgent
has been initialized, most of FlurryAgent calls will be ignored.

Returns:

    true if FlurryAgent is initialized, false if not.
    * ### getAgentVersion

public static int getAgentVersion()

Get the version of the Flurry SDK.

Returns:

    The version of the Flurry SDK.
    * ### getReleaseVersion

public static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") getReleaseVersion()

Get the release version of the Flurry SDK.

Returns:

    The release version GA/Beta of the Flurry SDK with prefix Flurry_Android.
    * ### getAddOnModules

@NonNull public static
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html
"class or interface in java.util")<[FlurryModule](FlurryModule.html "interface
in com.flurry.android")> getAddOnModules()

Returns a list of the Flurry add-on modules

Returns:

    the list of add-on modules
    * ### setVersionName

public static void setVersionName(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") versionName)

Set the version name of the app. Set the name of the this version of the app.
This name will appear in the http://dev.flurry.com as a filtering option by
version for many charts.

Parameters:

    `versionName` \- The version of the app.
    * ### setReportLocation

public static void setReportLocation(boolean reportLocation)

Set whether Flurry should record location via GPS. Defaults to true.

Parameters:

    `reportLocation` \- True to allow Flurry to record location via GPS, false otherwise
    * ### addOrigin

public static void addOrigin(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originName, @NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originVersion)

Add origin attribution. Only 10 unique originNames can be logged with the
Flurry service per project.

        
                 FlurryAgent.addOrigin("An Origin without Params", "Origin Version");
         

Parameters:

    `originName` \- The name/id of the origin you wish to attribute.
    `originVersion` \- The version of the origin you wish to attribute.
See Also:

    
      * `addOrigin(String, String, Map)`
    * ### addOrigin

public static void addOrigin(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originName, @NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") originVersion,
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> originParameters)

Add origin attribution with parameters. Only up to 10 parameters can be passed
in with the Map.

        
                 // Add an origin with params, where param1=value1 and param2=value2 Map<String, String>
         params = new HashMap<String, String>(); params.put("param1", "value1");
         params.put("param2", "value2"); FlurryAgent.addOrigin("An Origin with Params", "Origin Version",
         params);
         

Parameters:

    `originName` \- The name/id of the origin you wish to attribute.
    `originVersion` \- The version of the origin you wish to attribute.
    `originParameters` \- A `Map<String, String>` of the parameters which should be submitted with this origin attribution.
See Also:

    
      * `addOrigin(String, String)`
    * ### setInstantAppName

public static void setInstantAppName(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") instantAppName)

Set instant app name if it's an instant app. If it's an instant app, instant
app name will be shown in session properties under "instantapp.name".

Parameters:

    `instantAppName` \- The name for your instant app
    * ### getInstantAppName

public static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") getInstantAppName()

Return instant app name. If it's an instant app, instant app name will be
shown in session properties under "instantapp.name"

Returns:

    instant app name
    * ### getFlurryConsent

public static [Consent](Consent.html "class in com.flurry.android")
getFlurryConsent()

Return Flurry consent set by `updateFlurryConsent(Consent)` or
[`FlurryAgent.Builder.withConsent(Consent)`](FlurryAgent.Builder.html#withConsent\(com.flurry.android.Consent\))

Returns:

    Flurry consent
    * ### setGppConsent

public static boolean setGppConsent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") gppString, @NonNull
[Set](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Set.html
"class or interface in
java.util")<[Integer](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html
"class or interface in java.lang")> gppSectionIds)

Set Flurry Consent for the IAB Global Privacy Platform (GPP). To pass an IAB
string to Flurry, see [`Consent`](Consent.html "class in com.flurry.android")
and [`FlurryConsent`](FlurryConsent.html "class in com.flurry.android")

Parameters:

    `gppString` \- IAB GPP String.
    `gppSectionIds` \- Integer set of IAB GPP section ids that are applicable for this bid request.
Returns:

    true if consent is valid, false otherwise
    * ### updateFlurryConsent

public static boolean updateFlurryConsent(@NonNull [Consent](Consent.html
"class in com.flurry.android") flurryConsent)

Update Flurry consent. To pass an IAB string to Flurry, see
[`FlurryConsent`](FlurryConsent.html "class in com.flurry.android")

Parameters:

    `flurryConsent` \- Flurry consent
Returns:

    true if consent is valid, false otherwise
    * ### onStartSession

public static void onStartSession(@NonNull android.content.Context context)

Start or continue a Flurry session for the project on the given Context. You
MUST initialize the Flurry SDK via #FlurryAgent.Builder.build(Context, String)
before calling this method. Also, it is important to match any call to
#onStartSession(Context) in the Android onStart method with a call to
#onEndSession(Context) in the Android onEnd method.

        
                 // The Activity's onStart method
         protected void onStart() { // Start the Flurry session
         FlurryAgent.onStartSession(this); }
         

So long as there is any Context that has called #onStartSession(Context) but
not `onEndSession(Context)`, the session will be continued. Also, if a new
Context calls #onStartSession(Context) within 10 seconds (the default session
timeout length) of the last Context calling onEndSession, then the session
will be resumed, instead of a new session being created. Session length, usage
frequency, events and errors will continue to be tracked as part of the same
session. This ensures that as a user transitions from one Activity to another
in your application they will not have a separate session tracked for each
Activity, but will have a single session that spans many activities.
#onStartSession should be called from within the onStart method of the
activity in question. The first call to onStartSession will set up the
configuration for all later occurring calls to onStartSession. There is no
need to call this method unless you wish to track another type of Context.

Parameters:

    `context` \- A reference to a [android.content.Context](http://developer.android.com/reference/android/content/Context.html) object such as an [android.app.Activity](http://developer.android.com/reference/android/app/Activity.html) or an [android.app.Service](http://developer.android.com/reference/android/app/Service.html).
Since:

    1.0
    * ### onEndSession

public static void onEndSession(@NonNull android.content.Context context)

End a Flurry session for the given Context. The session implementation for the
Android SDK is implemented as a stack. It is important to match any call to
#onStartSession(Context, String) in the Android onStart method with a call to
#onEndSession(Context) in the Android onEnd method.

        
                 
         // The Activity's onStop method
         protected void onStop() {
          FlurryAgent.onEndSession(this);
          }
         
         

Pop a session off the stack for this Activity. If no sessions remain after the
call to onEndSession(Context) and no new calls to `onStartSession(Context)`
are made within the timeout specified (which defaults to 10 seconds) then the
session will truly end. Calls to #onEndSession should be made from the
Activity's onStop method in order to assure a complete analytics lifecycle for
the Activity. There is no need to call this method unless you wish to track
another type of Context.

Parameters:

    `context` \- A reference to a [android.content.Context](http://developer.android.com/reference/android/content/Context.html) object such as an [android.app.Activity](http://developer.android.com/reference/android/app/Activity.html) or an [android.app.Service](http://developer.android.com/reference/android/app/Service.html).
Since:

    1.0
    * ### isSessionActive

public static boolean isSessionActive()

Check to see if there is an active session. The session implementation for the
Android SDK is implemented as a stack. It is important to match any call to
`onStartSession(Context)` in the Android onStart method with a call to
`onEndSession(Context)` in the Android onEnd method. At any point, you can
call this method to find if there is an active running session.

Returns:

    true if a session is currently active, false if not.
Since:

    5.0.0
    * ### getSessionId

public static
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") getSessionId()

Check to see if there is an active session. The session implementation for the
Android SDK is implemented as a stack. It is important to match any call to
`onStartSession(Context)` in the Android onStart method with a call to
`onEndSession(Context)` in the Android onEnd method. At any point, you can
call this method to get the active session id.

Returns:

    The current session id, or null if no session is currently active.
Since:

    5.4.0
    * ### logEvent

@NonNull public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html
"enum class in com.flurry.android") logEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId)

Log an event. Only 300 unique eventIds can be logged with the Flurry service
per project.

        
                FlurryAgent.logEvent("An Event without Params");

Parameters:

    `eventId` \- The name/id of the event.
Returns:

    enum FlurryEventRecordStatus { kFlurryEventFailed, kFlurryEventRecorded, kFlurryEventUniqueCountExceeded, kFlurryEventParamsCountExceeded, kFlurryEventLogCountExceeded, kFlurryEventLoggingDelayed, kFlurryEventAnalyticsDisabled}
Since:

    Log an event with the Flurry service. The event is identified by the eventId, which is a String. Events will appear in the developer portal after they have been processed by the Flurry service.
See Also:

    
      * `logEvent(String, Map)`
      * `logEvent(String, Map, boolean)`
    * ### logEvent

@NonNull public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html
"enum class in com.flurry.android") logEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, @NonNull
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters)

Log an event with parameters. Only up to 10 parameters can be passed in with
the Map. If more than 10 parameters are passed, all parameters will be dropped
and the event will be logged as if it had no parameters.

        
                 // Log an event with params, where param1=value1 and param2=value2 Map<String, String>
         params = new HashMap<String, String>(); params.put("param1", "value1");
         params.put("param2", "value2"); FlurryAgent.logEvent("Event with params", params);
         
         

Log an event with parameters with the Flurry service. The event is identified
by the eventId, which is a String. A `Map<String, String>` of parameters can
be passed in where the key is the parameter name, and the value is the value.

Parameters:

    `eventId` \- The name/id of the event.
    `parameters` \- A `Map<String, String>` of the parameters which should be submitted with this event.
Returns:

    enum FlurryEventRecordStatus { kFlurryEventFailed, kFlurryEventRecorded, kFlurryEventUniqueCountExceeded, kFlurryEventParamsCountExceeded, kFlurryEventLogCountExceeded, kFlurryEventLoggingDelayed, kFlurryEventAnalyticsDisabled}
See Also:

    
      * `logEvent(String)`
      * `logEvent(String, Map, boolean)`
    * ### logEvent

@NonNull public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html
"enum class in com.flurry.android") logEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, boolean timed)

Log a timed event.

Parameters:

    `eventId` \- The name/id of the event.
    `timed` \- True if the event should be timed, false otherwise.
Returns:

    [`FlurryEventRecordStatus`](FlurryEventRecordStatus.html "enum class in com.flurry.android")
Since:

    1.0
See Also:

    
      * `endTimedEvent(String)`
      * `logEvent(String)`
    * ### logEvent

@NonNull public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html
"enum class in com.flurry.android") logEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, @NonNull
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters, boolean timed)

Log a timed event with parameters. Log a timed event with parameters with the
Flurry service. To end the timer, call #endTimedEvent(String) with this
eventId. Only up to 10 parameters can be passed in with the Map. If more than
10 parameters are passed, all parameters will be dropped and the event will be
logged as if it had no parameters.

Parameters:

    `eventId` \- The name/id of the event.
    `parameters` \- A `Map<String, String>` of parameters to log with this event.
    `timed` \- True if this event is timed, false otherwise.
Returns:

    enum FlurryEventRecordStatus { kFlurryEventFailed, kFlurryEventRecorded, kFlurryEventUniqueCountExceeded, kFlurryEventParamsCountExceeded, kFlurryEventLogCountExceeded, kFlurryEventLoggingDelayed, kFlurryEventAnalyticsDisabled}
See Also:

    
      * `logEvent(String, Map)`
    * ### logEvent

@NonNull public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html
"enum class in com.flurry.android") logEvent(@NonNull
[FlurryEvent](FlurryEvent.html "enum class in com.flurry.android") event,
@Nullable [FlurryEvent.Params](FlurryEvent.Params.html "class in
com.flurry.android") parameters)

Log a standard event with suggested parameters and user defined parameters.

        
                 // Log a standard event with suggested params and user defined params, where parameters = FlurryEvent.Params
         params = new FlurryEvent.Params();
         params.put(param1, "value1"); params.put(param2, "value2");
         FlurryAgent.logEvent(flurryEvent, params);
         
         

Log a standard event with suggested parameters and user defined parameters
with the Flurry service. The event is identified by the event, which is a
FlurryEvent Enum. A `FlurryEvent.Params` of parameters can be passed in where
the key is the event parameter enum or user defined string, and the value is
the value.

Parameters:

    `event` \- The enum type of the event.
    `parameters` \- A `Map<FlurryEvent.Param, String>` of the suggested parameters which should be submitted with this event.
Returns:

    enum FlurryEventRecordStatus { kFlurryEventFailed, kFlurryEventRecorded, kFlurryEventUniqueCountExceeded, kFlurryEventParamsCountExceeded, kFlurryEventLogCountExceeded, kFlurryEventLoggingDelayed, kFlurryEventAnalyticsDisabled}
    * ### logEvent

@NonNull public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html
"enum class in com.flurry.android") logEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, @NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)

Log a timed event with the 2nd key.

        
                 Example:
           // 0    1    2    3    4    5    6    sec.
           // ID1  ID2       ID3
           //      -    -    -    ID2: 3 sec.
           //                -    -    ID3: 2 sec.
           // -    -    -    -    -    -    ID1: 6 sec.
           try {
               FlurryAgent.logEvent("TimedEventName", "InstanceId1");
               Thread.sleep(1000);
               FlurryAgent.logEvent("TimedEventName", "InstanceId2");
               Thread.sleep(2000);
               FlurryAgent.logEvent("TimedEventName", "InstanceId3");
        
               Thread.sleep(1000);
               FlurryAgent.endTimedEvent("TimedEventName", "InstanceId2");  // ID2 duration: 3 sec.
               Thread.sleep(1000);
               FlurryAgent.endTimedEvent("TimedEventName", "InstanceId3");  // ID3 duration: 2 sec.
               Thread.sleep(1000);
               FlurryAgent.endTimedEvent("TimedEventName", "InstanceId1");  // ID1 duration: 6 sec.
           } catch (InterruptedException e) {
               // no-op
           }
         

Parameters:

    `eventId` \- The name/id of the event.
    `timedId` \- The 2nd key for timed event.
Returns:

    [`FlurryEventRecordStatus`](FlurryEventRecordStatus.html "enum class in com.flurry.android")
    * ### logEvent

@NonNull public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html
"enum class in com.flurry.android") logEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, @NonNull
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters, @NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)

Log a timed event with parameters and the 2nd key. Log a timed event with
parameters with the Flurry service. To end the timer, call
#endTimedEvent(String) with this eventId. Only up to 10 parameters can be
passed in with the Map. If more than 10 parameters are passed, all parameters
will be dropped and the event will be logged as if it had no parameters.

Parameters:

    `eventId` \- The name/id of the event.
    `parameters` \- A `Map<String, String>` of parameters to log with this event.
    `timedId` \- The 2nd key for timed event.
Returns:

    enum FlurryEventRecordStatus { kFlurryEventFailed, kFlurryEventRecorded, kFlurryEventUniqueCountExceeded, kFlurryEventParamsCountExceeded, kFlurryEventLogCountExceeded, kFlurryEventLoggingDelayed, kFlurryEventAnalyticsDisabled}
    * ### endTimedEvent

public static void endTimedEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId)

End a timed event.

Parameters:

    `eventId` \- The name/id of the event to end the timer on.
See Also:

    
      * `for more details.`
    * ### endTimedEvent

public static void endTimedEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, @NonNull
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters)

End a timed event with parameters. Only up to 10 unique parameters total can
be passed for an event, including those passed when the event was initiated.
If more than 10 unique parameters total are passed, all parameter updates
passed on this endTimedEvent call will be ignored.

Parameters:

    `eventId` \- The name/id of the event to end the timer on.
    `parameters` \- A `Map<String, String>` of parameters to log with this event.
See Also:

    
      * `logEvent(String, Map)`
    * ### endTimedEvent

public static void endTimedEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, @NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)

End a timed event with the 2nd key.

Parameters:

    `eventId` \- The name/id of the event to end the timer on.
    `timedId` \- The 2nd key for timed event.
    * ### endTimedEvent

public static void endTimedEvent(@NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") eventId, @NonNull
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters, @NonNull
[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang") timedId)

End a timed event with parameters and the 2nd key. Only up to 10 unique
parameters total can be passed for an event, including those passed when the
event was initiated. If more than 10 unique parameters total are passed, all
parameter updates passed on this endTimedEvent call will be ignored.

Parameters:

    `eventId` \- The name/id of the event to end the timer on.
    `parameters` \- A `Map<String, String>` of parameters to log with this event.
    `timedId` \- The 2nd key for timed event.
    * ### logPayment

public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum
class in com.flurry.android") logPayment(int responseCode, @Nullable
[List](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/List.html
"class or interface in
java.util")<[Object](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Object.html
"class or interface in java.lang")> purchases, @Nullable
[Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html
"class or interface in
java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in
java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html
"class or interface in java.lang")> parameters)

Log a payment from Google. This method is suppose to be called from
PurchasesUpdatedListener callback of BillingClient.

        
                 Example:
             public class BillingClientLifecycle implements PurchasesUpdatedListener {
        
        
        
        
        
        
        Parameters:
        
            responseCode - The BillingResult.getResponseCode received in PurchasesUpdatedListener callback.
        
            purchases - List of Purchase objects by user from google play received in PurchasesUpdatedListener callback.
        
            parameters - A Map<String, String> of the parameters which should be submitted
                             with this event.
        
        Returns:
        
            FlurryEventRecordStatus.
        
        See Also:
        
            
        
            
                  * logEvent(String, Map)
            
            
        
        
        
        
        
        
        
            * 
        
        
        
        ### logPayment
        
        
        
        
        @NonNull
        public static [FlurryEventRecordStatus](FlurryEventRecordStatus.html "enum class in com.flurry.android") logPayment(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") productName,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") productId,
         int quantity,
         double price,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") currency,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") transactionId,
         @Nullable
         [Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> parameters)
        
        
        
        
        Log a payment. This method is supposed to be called when you get an activity
         result back from a Google Play Purchase in your Activity.onActivityResult()
        
        
        
        
        
        Parameters:
        
            productName - The name of the product purchased.
        
            productId - The id of the product purchased.
        
            quantity - The number of products purchased.
        
            price - The price of the the products purchased in the given currency.
        
            currency - The currency for the price argument.
        
            transactionId - A unique identifier for the transaction used to make the purchase.
        
            parameters - A Map<String, String> of the parameters which should be submitted
                              with this event.
        
        Returns:
        
            FlurryEventRecordStatus.
        
        See Also:
        
            
        
            
                  * logEvent(String, Map)
            
            
        
        
        
        
        
        
        
            * 
        
        
        
        ### onError
        
        
        
        
        public static void onError(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorId,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorClass)
        
        
        
        
        Report errors that your app catches. Flurry will report the first 10 errors to occur in each
         session.
        
        
        
        
        
        Parameters:
        
            errorId - Unique ID for reported error.
        
            message - Message for the error reported.
        
            errorClass - Class in which the error is reported.
        
        
        
        
        
        
            * 
        
        
        
        ### onError
        
        
        
        
        public static void onError(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorId,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorClass,
         @Nullable
         [Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorParams)
        
        
        
        
        Report errors that your app catches. Flurry will report the first 10 errors to occur in each
         session.
        
        
        
        
        
        Parameters:
        
            errorId - Unique ID for reported error.
        
            message - Message for the error reported.
        
            errorClass - Class in which the error is reported.
        
            errorParams - Map of params to be logged with this error
        
        
        
        
        
        
            * 
        
        
        
        ### onError
        
        
        
        
        public static void onError(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorId,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,
         @NonNull
         [Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") exception)
        
        
        
        
        Report errors that your app catches. Flurry will report the first 10 errors to occur in each
         session.
        
        
        
        
        
        Parameters:
        
            errorId - Unique ID for reported error.
        
            message - Message for the error reported.
        
            exception - Thrown error to be reported.
        
        
        
        
        
        
            * 
        
        
        
        ### onError
        
        
        
        
        public static void onError(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") errorId,
         @NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") message,
         @NonNull
         [Throwable](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") exception,
         @Nullable
         [Map](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> errorParams)
        
        
        
        
        Report errors that your app catches. Flurry will report the first 10 errors to occur in each
         session.
        
        
        
        
        
        Parameters:
        
            errorId - Unique ID for reported error.
        
            message - Message for the error reported.
        
            exception - Thrown error to be reported.
        
            errorParams - Map of params to be logged with this error
        
        
        
        
        
        
            * 
        
        
        
        ### logBreadcrumb
        
        
        
        
        public static void logBreadcrumb(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") crashBreadcrumb)
        
        
        
        
        
        
            * 
        
        
        
        ### setAge
        
        
        
        
        public static void setAge(int age)
        
        
        
        
        Sets the age of the user at the time of this session.
        
        
        
        
        
        Parameters:
        
            age - valid values are 0-110
        
        
        
        
        
        
            * 
        
        
        
        ### setGender
        
        
        
        
        public static void setGender(byte gender)
        
        
        
        
        Sets the gender of the user.
        
        
        
        
        
        Parameters:
        
            gender - One of the values among [Constants.MALE](Constants.html#MALE),[Constants.FEMALE](Constants.html#FEMALE) and [Constants.UNKNOWN](Constants.html#UNKNOWN)
                       as defined in Constants.
        
        
        
        
        
        
            * 
        
        
        
        ### setUserId
        
        
        
        
        public static void setUserId(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)
        
        
        
        
        Sets the Flurry userId for this session. The Flurry userId can be used to tie a user
         back to your internal systems. This userId will travel along with any event reporting
         that the Flurry Dev Portal provides.
        
        
        
        
        
        Parameters:
        
            userId - Unique user id for session.
        
        
        
        
        
        
            * 
        
        
        
        ### setSessionOrigin
        
        
        
        
        public static void setSessionOrigin(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") originName,
         @Nullable
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") deepLink)
        
        
        
        
        This method allows you to specify session origin and deep link for each session. This is
         different than addOrigin which is used for third party wrappers after every session start.
        
        
        
        
        
        Parameters:
        
            originName - Name of the origin.
        
            deepLink - Url of the deep Link.
        
        
        
        
        
        
            * 
        
        
        
        ### addSessionProperty
        
        
        
        
        public static void addSessionProperty(@NonNull
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name,
         @Nullable
         [String](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/String.html "class or interface in java.lang") value)
        
        
        
        
        This method allows you to associate parameters with an session. Parameters are valuable as
         they allow you to store characteristics of an session.
         Only 10 unique keys are allowed for session property parameters per session.
         Exceeded key-values will be dropped.
        
        
        
        
        
        Parameters:
        
            name - Property name.
        
            value - Property value.
        
        
        
        
        
        
            * 
        
        
        
        ### openPrivacyDashboard
        
        
        
        
        public static void openPrivacyDashboard(@NonNull
         [FlurryPrivacySession.Request](FlurryPrivacySession.Request.html "class in com.flurry.android") request)
        
        
        
        
        This api opens privacy dashboard in Chrome CustomTab (if its dependency's been included in the gradle and device support it as well),
         otherwise will open it in the external browser.
        
         You can set [FlurryPrivacySession.Callback](FlurryPrivacySession.Callback.html "interface in com.flurry.android") in request class which notify you when opening dashboard failed or succeed.
         
        
        
        
         Note: Since this api is asynchronous, would recommend you to show spinner while we are loading Privacy Dashboard. you can dismiss it in callback.
        
        
        
        
        
        Parameters:
        
            request - object to request privacy dashboard uri
        
        
        
        
        
        
            * 
        
        
        
        ### setDataSaleOptOut
        
        
        
        
        public static void setDataSaleOptOut(boolean isOptOut)
        
        
        
        
        This api allows you to set opt-out/opt-in for data sale
        
        
        
        
        
        Parameters:
        
            isOptOut - true to opt-out data sale, false to opt-in
        
        
        
        
        
        
            * 
        
        
        
        ### deleteData
        
        
        
        
        public static void deleteData()
        
        
        
        
        This api allows you to delete data collected by Flurry
        
        
        
        
        
        
            * 
        
        
        
        ### setCaptureUncaughtExceptions
        
        
        
        
        public static void setCaptureUncaughtExceptions(boolean captureExceptions)
        
        
        
        
        True to enable or false to disable the ability to catch all uncaught exceptions
         and have them reported back to Flurry.
        
        
        
        
        
        Parameters:
        
            captureExceptions - true to enable, false to disable.
        
        
        
        
        
        
            * 
        
        
        
        ### setContinueSessionMillis
        
        
        
        
        public static void setContinueSessionMillis(long sessionMillis)
        
        
        
        
        Set the timeout for expiring a Flurry session.
         e.g., FlurryAgent.setContinueSessionMillis(60 * 1000); // Set session timeout to 60 seconds
        
        
        
        
        
        Parameters:
        
            sessionMillis - The time in milliseconds to set the session timeout to. Minimum value of 5000.
        
        Since:
        
            1.0 The default value for a session timeout is 10,000 milliseconds. The minimum
         timeout for a session is 5,000 milliseconds. Calling #onStartSession(Context, String)
         within the set time will cause the previous session to resume. Calling
         #onStartSession(Context, String) after the set amount of time has passed will result
         in a new session being created.
        
        
        
        
        
        
            * 
        
        
        
        ### setIncludeBackgroundSessionsInMetrics
        
        
        
        
        public static void setIncludeBackgroundSessionsInMetrics(boolean includeBackgroundSessionsInMetrics)
        
        
        
        
        True if this session should be added to total sessions/DAUs when applicationstate is inactive or background.
         Default is set to true.
        
        
        
        
        
        Parameters:
        
            includeBackgroundSessionsInMetrics - if background and inactive session should be counted toward dau
        
        
        
        
        
        
            * 
        
        
        
        ### registerListener
        
        
        
        
        public static void registerListener(@NonNull
         [FlurryAgentListener](FlurryAgentListener.html "interface in com.flurry.android") listener)
        
        
        
        
        Registers the listener. The listener is an interface which can be implemented to receive notification of
         various events associated with session.
        
        
        
        
        
        Parameters:
        
            listener - Your implementation of the Flurry agent listener.
        
        
        
        
        
        
            * 
        
        
        
        ### unregisterListener
        
        
        
        
        public static void unregisterListener(@NonNull
         [FlurryAgentListener](FlurryAgentListener.html "interface in com.flurry.android") listener)
        
        
        
        
        Unregisters the listener. The listener is an interface which can be implemented to receive notification of
         various events associated with session.
        
        
        
        
        
        Parameters:
        
            listener - Your implementation of the Flurry agent listener.
        
        
        
        
        
        
            * 
        
        
        
        ### setLogEnabled
        
        
        
        
        public static void setLogEnabled(boolean enableLog)
        
        
        
        
        True to enable or  false to disable the internal logging for the Flurry SDK.
        
        
        
        
        
        Parameters:
        
            enableLog - true to enable logging,  false to disable it.
        
        
        
        
        
        
            * 
        
        
        
        ### setLogLevel
        
        
        
        
        public static void setLogLevel(int logLevel)
        
        
        
        
        Set the log level of the internal Flurry SDK logging.
        
        
        
        
        
        Parameters:
        
            logLevel - The level to set it to.
        
        
        
        
        
        
            * 
        
        
        
        ### setSslPinningEnabled
        
        
        
        
        public static void setSslPinningEnabled(boolean sslPinningEnabled)
        
        
        
        
        True to enable or  false to disable SSL Pinning for Flurry Analytics connection. Defaults to false.
        
         Turn on to add SSL Pinning protection for the Flurry Analytics connections. Disable it
         if your app is using proxy or any services that are not compliant with SSL Pinning.
        
        
        
        
        
        Parameters:
        
            sslPinningEnabled - true to enable SSL Pinning for Flurry Analytics connection, false to disable it.
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    * * *
    
    
    
    
    Copyright (C) 2009-2024, Flurry, Inc. All Rights Reserved. [Flurry Publisher Support Site](https://developer.yahoo.com/flurry/docs/).
    
    
    
    
    
    
    
    
    
    
    
    

