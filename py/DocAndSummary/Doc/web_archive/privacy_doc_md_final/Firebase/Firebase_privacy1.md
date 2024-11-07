

# FirebaseAnalytics

    
    
    @[DataCollectionPurpose](/docs/reference/android/com/google/privacy/one/psl/annotation/DataCollectionPurpose)(dataTypes = [SemanticType.ST_ANALYTICS_ID, SemanticType.ST_PAYMENTS_TRANSACTION_INFO, SemanticType.ST_HARDWARE_ID, SemanticType.ST_IDENTIFYING_ID, SemanticType.ST_COARSE_LOCATION], collectionPurposes = [CollectionPurpose.CP_ANALYTICS])  
    public final class [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics)

* * *

The top level Firebase Analytics singleton that provides methods for logging
events and setting user properties. See [the developer
guides](http://goo.gl/X2xCu3) for general information on using Firebase
Analytics in your apps.

Applications can get an instance of this class by calling
`[getInstance](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance\(android.content.Context\))`.
`[getInstance](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance\(android.content.Context\))`
is thread safe and can be called from any thread.

## Summary

### Nested types  
  
---  
`public enum
[FirebaseAnalytics.ConsentStatus](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus)`
The status value of the consent type.  
`public enum
[FirebaseAnalytics.ConsentType](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType)`
The type of consent to set.  
`public class
[FirebaseAnalytics.Event](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event)`
An Event is an important occurrence in your app that you want to measure.  
`public class
[FirebaseAnalytics.Param](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param)`
Params supply information that contextualize Events.  
`public class
[FirebaseAnalytics.UserProperty](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.UserProperty)`
A UserProperty is an attribute that describes the app-user.  
  
### Public methods  
  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)<@[Nullable](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html) [String](https://developer.android.com/reference/java/lang/String.html)>` |  `@[SuppressViolation](/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation)(value = "catch_specific_exceptions")  
[getAppInstanceId](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getAppInstanceId\(\))()`
Retrieves the app instance id from the service, or `null` if
`[ANALYTICS_STORAGE](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE)`
has been set to
`[DENIED](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED)`.  
`static @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics)` |  `@[RequiresPermission](https://developer.android.com/reference/androidx/annotation/RequiresPermission.html)(allOf = [Manifest.permission.INTERNET, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.WAKE_LOCK])  
@[Keep](https://developer.android.com/reference/androidx/annotation/Keep.html)  
[getInstance](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance\(android.content.Context\))(@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html)
[Context](https://developer.android.com/reference/android/content/Context.html)
context)` Returns the singleton FirebaseAnalytics interface.  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)<@[Nullable](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html) [Long](https://developer.android.com/reference/java/lang/Long.html)>` |  `@[SuppressViolation](/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation)(value = "catch_specific_exceptions")  
[getSessionId](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getSessionId\(\))()`
Retrieves the session id from the client.  
`void` |  `[logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent\(java.lang.String,android.os.Bundle\))(@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 40) [String](https://developer.android.com/reference/java/lang/String.html) name, @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [Bundle](https://developer.android.com/reference/android/os/Bundle.html) params)` Logs an app event.  
`void` |  `[resetAnalyticsData](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#resetAnalyticsData\(\))()` Clears all analytics data for this app from the device and resets the app instance id.  
`void` |  `[setAnalyticsCollectionEnabled](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled\(boolean\))(boolean enabled)` Sets whether analytics collection is enabled for this app on this device.  
`void` |  `[setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent\(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>\))(  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Map](https://developer.android.com/reference/java/util/Map.html)<[FirebaseAnalytics.ConsentType](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType), [FirebaseAnalytics.ConsentStatus](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus)> consentSettings  
)` Sets the applicable end user consent state (e.g., for device identifiers)
for this app on this device.  
`void` |  `@[MainThread](https://developer.android.com/reference/androidx/annotation/MainThread.html)  
@[Keep](https://developer.android.com/reference/androidx/annotation/Keep.html)  
~~[setCurrentScreen](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen\(android.app.Activity,java.lang.String,java.lang.String\))~~(  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Activity](https://developer.android.com/reference/android/app/Activity.html) activity,  
    @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 36) [String](https://developer.android.com/reference/java/lang/String.html) screenName,  
    @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 36) [String](https://developer.android.com/reference/java/lang/String.html) screenClassOverride  
)` **This method is deprecated.** To log screen view events, call
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params)
instead.  
`void` |  `[setDefaultEventParameters](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setDefaultEventParameters\(android.os.Bundle\))(@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [Bundle](https://developer.android.com/reference/android/os/Bundle.html) parameters)` Adds parameters that will be set on every event logged from the SDK, including automatic ones.  
`void` |  `[setSessionTimeoutDuration](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setSessionTimeoutDuration\(long\))(long milliseconds)` Sets the duration of inactivity that terminates the current session.  
`void` |  `[setUserId](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setUserId\(java.lang.String\))(@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [String](https://developer.android.com/reference/java/lang/String.html) id)` Sets the user ID property.  
`void` |  `[setUserProperty](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setUserProperty\(java.lang.String,java.lang.String\))(  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 24) [String](https://developer.android.com/reference/java/lang/String.html) name,  
    @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(max = 36) [String](https://developer.android.com/reference/java/lang/String.html) value  
)` Sets a user property to a given value.  
  
### Extension functions  
  
---  
`final void` |  `[AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).[logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).logEvent\(kotlin.String,kotlin.Function1\))(  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [String](https://developer.android.com/reference/java/lang/String.html) name,  
    @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ParametersBuilder](/docs/reference/android/com/google/firebase/analytics/ParametersBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
)` Fluent version of
`[FirebaseAnalytics.logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent\(kotlin.String,android.os.Bundle\))`.  
`final void` |  `[AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).~~[logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).logEvent\(kotlin.String,kotlin.Function1\))~~(  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [String](https://developer.android.com/reference/java/lang/String.html) name,  
    @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ParametersBuilder](/docs/reference/android/com/google/firebase/analytics/ktx/ParametersBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
)` **This method is deprecated.** Migrate to use the KTX API from the main
module: https://firebase.google.com/docs/android/kotlin-migration.  
`final void` |  `[AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).[setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).setConsent\(kotlin.Function1\))(  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
    @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ConsentBuilder](/docs/reference/android/com/google/firebase/analytics/ConsentBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
)` Fluent version of
`[FirebaseAnalytics.setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent\(kotlin.collections.MutableMap\))`.  
`final void` |  `[AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).~~[setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).setConsent\(kotlin.Function1\))~~(  
    @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
    @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ConsentBuilder](/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
)` **This method is deprecated.** Migrate to use the KTX API from the main
module: https://firebase.google.com/docs/android/kotlin-migration.  
  
## Public methods

### getAppInstanceId

    
    
    @[SuppressViolation](/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation)(value = "catch_specific_exceptions")  
    public @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)<@[Nullable](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html) [String](https://developer.android.com/reference/java/lang/String.html)> [getAppInstanceId](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getAppInstanceId\(\))()

Retrieves the app instance id from the service, or `null` if
`[ANALYTICS_STORAGE](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE)`
has been set to
`[DENIED](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED)`.

Returns  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)<@[Nullable](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html) [String](https://developer.android.com/reference/java/lang/String.html)>` |  `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)` with the result of the retrieval  
  
See also  
---  
`[setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent\(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>\))` |   
  
### getInstance

    
    
    @[RequiresPermission](https://developer.android.com/reference/androidx/annotation/RequiresPermission.html)(allOf = [Manifest.permission.INTERNET, Manifest.permission.ACCESS_NETWORK_STATE, Manifest.permission.WAKE_LOCK])  
    @[Keep](https://developer.android.com/reference/androidx/annotation/Keep.html)  
    public static @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) [getInstance](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getInstance\(android.content.Context\))(@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Context](https://developer.android.com/reference/android/content/Context.html) context)

Returns the singleton FirebaseAnalytics interface.

Parameters  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Context](https://developer.android.com/reference/android/content/Context.html) context` |  the context used to initialize Firebase Analytics. Must not be `null`.  
  
### getSessionId

    
    
    @[SuppressViolation](/docs/reference/android/com/google/android/gms/testing/lint/common/SuppressViolation)(value = "catch_specific_exceptions")  
    public @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)<@[Nullable](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html) [Long](https://developer.android.com/reference/java/lang/Long.html)> [getSessionId](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#getSessionId\(\))()

Retrieves the session id from the client. Returns `null` if
`[ANALYTICS_STORAGE](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE)`
has been set to
`[DENIED](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED)`
or session is expired.

Returns  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)<@[Nullable](https://checkerframework.org/api/org/checkerframework/checker/nullness/qual/Nullable.html) [Long](https://developer.android.com/reference/java/lang/Long.html)>` |  `[Task](https://developers.google.com/android/reference/com/google/android/gms/tasks/Task.html)` with the result of the retrieval  
  
See also  
---  
`[setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent\(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>\))` |   
  
### logEvent

    
    
    public void [logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent\(java.lang.String,android.os.Bundle\))(@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 40) [String](https://developer.android.com/reference/java/lang/String.html) name, @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [Bundle](https://developer.android.com/reference/android/os/Bundle.html) params)

Logs an app event. The event can have up to 25 parameters. Events with the
same name must have the same parameters. Up to 500 event names are supported.
Using predefined
`[Event](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event)`
and/or
`[Param](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Param)`
is recommended for optimal reporting.

Parameters  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 40) [String](https://developer.android.com/reference/java/lang/String.html) name` |  The name of the event. Should contain 1 to 40 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores. The name must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. Some event names are reserved. See `[Event](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.Event)` for the list of reserved event names. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used. Note that event names are case-sensitive and that logging two events whose names differ only in case will result in two distinct events.  
`@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [Bundle](https://developer.android.com/reference/android/os/Bundle.html) params` |  The map of event parameters. Passing null indicates that the event has no parameters. Parameter names can be up to 40 characters long and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character and contain only [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters and underscores. String, long and double param types are supported. String parameter values can be up to 100 characters long. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for parameter names.  
  
### resetAnalyticsData

    
    
    public void [resetAnalyticsData](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#resetAnalyticsData\(\))()

Clears all analytics data for this app from the device and resets the app
instance id.

### setAnalyticsCollectionEnabled

    
    
    public void [setAnalyticsCollectionEnabled](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setAnalyticsCollectionEnabled\(boolean\))(boolean enabled)

Sets whether analytics collection is enabled for this app on this device. This
setting is persisted across app sessions. By default it is enabled.

Parameters  
---  
`boolean enabled` |  Whether analytics collection is enabled for this app on this device.  
  
### setConsent

    
    
    public void [setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent\(java.util.Map<com.google.firebase.analytics.FirebaseAnalytics.ConsentType,com.google.firebase.analytics.FirebaseAnalytics.ConsentStatus>\))(  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Map](https://developer.android.com/reference/java/util/Map.html)<[FirebaseAnalytics.ConsentType](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType), [FirebaseAnalytics.ConsentStatus](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus)> consentSettings  
    )

Sets the applicable end user consent state (e.g., for device identifiers) for
this app on this device. Use the consent map to specify individual consent
type values. Settings are persisted across app sessions.

Parameters  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Map](https://developer.android.com/reference/java/util/Map.html)<[FirebaseAnalytics.ConsentType](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType), [FirebaseAnalytics.ConsentStatus](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus)> consentSettings` |  The map of consent types. Supported consent type keys are `[AD_STORAGE](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_STORAGE)`, `[ANALYTICS_STORAGE](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#ANALYTICS_STORAGE)`, `[AD_USER_DATA](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_USER_DATA)` and `[AD_PERSONALIZATION](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentType#AD_PERSONALIZATION)`. Valid values are `[GRANTED](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#GRANTED)` and `[DENIED](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics.ConsentStatus#DENIED)`.  
  
### setCurrentScreen

    
    
    @[MainThread](https://developer.android.com/reference/androidx/annotation/MainThread.html)  
    @[Keep](https://developer.android.com/reference/androidx/annotation/Keep.html)  
    public void ~~[setCurrentScreen](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setCurrentScreen\(android.app.Activity,java.lang.String,java.lang.String\))~~(  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Activity](https://developer.android.com/reference/android/app/Activity.html) activity,  
        @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 36) [String](https://developer.android.com/reference/java/lang/String.html) screenName,  
        @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 36) [String](https://developer.android.com/reference/java/lang/String.html) screenClassOverride  
    )

**This method is deprecated.**  

To log screen view events, call
mFirebaseAnalytics.logEvent(FirebaseAnalytics.Event.SCREEN_VIEW, params)
instead.

Sets the current screen name, which specifies the current visual context in
your app. This helps identify the areas in your app where users spend their
time and how they interact with your app.

Note that screen reporting is enabled automatically and records the class name
of the current Activity for you without requiring you to call this function.
The class name can optionally be overridden by calling this function in the
onResume callback of your Activity and specifying the screenClassOverride
parameter.

If your app does not use a distinct Activity for each screen, you should call
this function and specify a distinct screenName each time a new screen is
presented to the user.

The name and classOverride remain in effect until the current Activity changes
or a new call to setCurrentScreen is made.

This method must be called from the app's main thread.

Parameters  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [Activity](https://developer.android.com/reference/android/app/Activity.html) activity` |  The activity to which the screen name and class name apply.  
`@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 36) [String](https://developer.android.com/reference/java/lang/String.html) screenName` |  The name of the current screen. Set to null to clear the current screen name.  
`@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 36) [String](https://developer.android.com/reference/java/lang/String.html) screenClassOverride` |  The name of the screen class. By default this is the class name of the current Activity. Set to null to revert to the default class name.  
  
### setDefaultEventParameters

    
    
    public void [setDefaultEventParameters](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setDefaultEventParameters\(android.os.Bundle\))(@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [Bundle](https://developer.android.com/reference/android/os/Bundle.html) parameters)

Adds parameters that will be set on every event logged from the SDK, including
automatic ones. The values passed in the parameters bundle will be added to
the map of default event parameters. These parameters persist across app runs.
They are of lower precedence than event parameters, so if an event parameter
and a parameter set using this API have the same name, the value of the event
parameter will be used. The same limitations on event parameters apply to
default event parameters.

Parameters  
---  
`@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [Bundle](https://developer.android.com/reference/android/os/Bundle.html) parameters` |  Parameters to be added to the map of parameters added to every event. They will be added to the map of default event parameters, replacing any existing parameter with the same name. Valid parameter values are String, long, and double. Setting a key's value to null will clear that parameter. Passing in a null bundle will clear all parameters.  
  
### setSessionTimeoutDuration

    
    
    public void [setSessionTimeoutDuration](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setSessionTimeoutDuration\(long\))(long milliseconds)

Sets the duration of inactivity that terminates the current session. The
default value is 1800000 (30 minutes).

Parameters  
---  
`long milliseconds` |  Session timeout duration in milliseconds  
  
### setUserId

    
    
    public void [setUserId](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setUserId\(java.lang.String\))(@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [String](https://developer.android.com/reference/java/lang/String.html) id)

Sets the user ID property. This feature must be used in accordance with
[Google's Privacy Policy](https://www.google.com/policies/privacy).

Parameters  
---  
`@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) [String](https://developer.android.com/reference/java/lang/String.html) id` |  The user ID to ascribe to the user of this app on this device, which must be non-empty and no more than 256 characters long. Setting the ID to null removes the user ID.  
  
### setUserProperty

    
    
    public void [setUserProperty](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setUserProperty\(java.lang.String,java.lang.String\))(  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 24) [String](https://developer.android.com/reference/java/lang/String.html) name,  
        @[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(max = 36) [String](https://developer.android.com/reference/java/lang/String.html) value  
    )

Sets a user property to a given value. Up to 25 user property names are
supported. Once set, user property values persist throughout the app lifecycle
and across sessions.

Parameters  
---  
`@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(min = 1, max = 24) [String](https://developer.android.com/reference/java/lang/String.html) name` |  The name of the user property to set. Should contain 1 to 24 [alphanumeric](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetterOrDigit-int-)characters or underscores and must start with an [alphabetic](https://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#isLetter-int-)character. The "firebase_", "google_" and "ga_" prefixes are reserved and should not be used for user property names.  
`@[Nullable](https://developer.android.com/reference/androidx/annotation/Nullable.html) @[Size](https://developer.android.com/reference/androidx/annotation/Size.html)(max = 36) [String](https://developer.android.com/reference/java/lang/String.html) value` |  The value of the user property. Values can be up to 36 characters long. Setting the value to null removes the user property.  
  
## Extension functions

### AnalyticsKt.logEvent

    
    
    public final void [AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).[logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).logEvent\(kotlin.String,kotlin.Function1\))(  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [String](https://developer.android.com/reference/java/lang/String.html) name,  
        @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ParametersBuilder](/docs/reference/android/com/google/firebase/analytics/ParametersBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
    )

Fluent version of
`[FirebaseAnalytics.logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent\(kotlin.String,android.os.Bundle\))`.

Example use:

    
    
    Firebase.analytics.logEvent("myEvent") {  
      param(Params.VALUE, 3.99)  
      param(Params.CURRENCY, "USD")  
    }

### AnalyticsKt.logEvent

    
    
    public final void [AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).~~[logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).logEvent\(kotlin.String,kotlin.Function1\))~~(  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [String](https://developer.android.com/reference/java/lang/String.html) name,  
        @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ParametersBuilder](/docs/reference/android/com/google/firebase/analytics/ktx/ParametersBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
    )

**This method is deprecated.**  
Migrate to use the KTX API from the main module:
https://firebase.google.com/docs/android/kotlin-migration.

Fluent version of
`[FirebaseAnalytics.logEvent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#logEvent\(kotlin.String,android.os.Bundle\))`.

Example use:

    
    
    Firebase.analytics.logEvent("myEvent") {  
      param(Params.VALUE, 3.99)  
      param(Params.CURRENCY, "USD")  
    }

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to
their respective main modules, and the Kotlin extension (KTX) APIs in
`com.google.firebase.firebase-analytics-ktx` are now deprecated. As early as
April 2024, we'll no longer release KTX modules. For details, see the [FAQ
about this initiative.](https://firebase.google.com/docs/android/kotlin-
migration),

### AnalyticsKt.setConsent

    
    
    public final void [AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).[setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).setConsent\(kotlin.Function1\))(  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
        @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ConsentBuilder](/docs/reference/android/com/google/firebase/analytics/ConsentBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
    )

Fluent version of
`[FirebaseAnalytics.setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent\(kotlin.collections.MutableMap\))`.

Example use:

    
    
    Firebase.analytics.setConsent {  
      adStorage = ConsentStatus.GRANTED  
      analyticsStorage = ConsentStatus.GRANTED  
      adUserData = ConsentStatus.GRANTED  
      adPersonalization = ConsentStatus.GRANTED  
    }

### AnalyticsKt.setConsent

    
    
    public final void [AnalyticsKt](/docs/reference/android/com/google/firebase/analytics/AnalyticsKt).~~[setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#\(com.google.firebase.analytics.FirebaseAnalytics\).setConsent\(kotlin.Function1\))~~(  
        @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [FirebaseAnalytics](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics) receiver,  
        @[ExtensionFunctionType](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-extension-function-type/index.html) @[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) Function1<@[NonNull](https://developer.android.com/reference/androidx/annotation/NonNull.html) [ConsentBuilder](/docs/reference/android/com/google/firebase/analytics/ktx/ConsentBuilder), [Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-unit/index.html)> block  
    )

**This method is deprecated.**  
Migrate to use the KTX API from the main module:
https://firebase.google.com/docs/android/kotlin-migration.

Fluent version of
`[FirebaseAnalytics.setConsent](/docs/reference/android/com/google/firebase/analytics/FirebaseAnalytics#setConsent\(kotlin.collections.MutableMap\))`.

Example use:

    
    
    Firebase.analytics.setConsent {  
      adStorage = ConsentStatus.GRANTED  
      analyticsStorage = ConsentStatus.GRANTED  
    }

**Deprecation Notice:** The Kotlin extensions (KTX) APIs have been added to
their respective main modules, and the Kotlin extension (KTX) APIs in
`com.google.firebase.firebase-analytics-ktx` are now deprecated. As early as
April 2024, we'll no longer release KTX modules. For details, see the [FAQ
about this initiative.](https://firebase.google.com/docs/android/kotlin-
migration),

Send feedback

Except as otherwise noted, the content of this page is licensed under the
[Creative Commons Attribution 4.0
License](https://creativecommons.org/licenses/by/4.0/), and code samples are
licensed under the [Apache 2.0
License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the
[Google Developers Site Policies](https://developers.google.com/site-
policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-11-22 UTC.

[{ "type": "thumb-down", "id": "missingTheInformationINeed", "label":"Missing
the information I need" },{ "type": "thumb-down", "id":
"tooComplicatedTooManySteps", "label":"Too complicated / too many steps" },{
"type": "thumb-down", "id": "outOfDate", "label":"Out of date" },{ "type":
"thumb-down", "id": "samplesCodeIssue", "label":"Samples / code issue" },{
"type": "thumb-down", "id": "otherDown", "label":"Other" }]  [{ "type":
"thumb-up", "id": "easyToUnderstand", "label":"Easy to understand" },{ "type":
"thumb-up", "id": "solvedMyProblem", "label":"Solved my problem" },{ "type":
"thumb-up", "id": "otherUp", "label":"Other" }]  Need to tell us more?  {
"lastModified": "Last updated 2023-11-22 UTC.", "confidential": False }

  * ### Learn

    * [ Guides ](/docs/guides/)
    * [ Reference ](/docs/reference/)
    * [ Samples ](/docs/samples/)
    * [ Libraries ](/docs/libraries/)
    * [ GitHub ](//github.com/firebase/)
  * ### Stay connected

    * [ Blog ](//firebase.blog)
    * [ Firebase Summit ](/summit/)
    * [ Twitter ](//twitter.com/Firebase)
    * [ YouTube ](//www.youtube.com/user/Firebase)
  * ### Support

    * [ Contact support ](/support/)
    * [ Stack Overflow ](//stackoverflow.com/questions/tagged/firebase)
    * [ Slack community ](//firebase.community/)
    * [ Google group ](//groups.google.com/forum/#!forum/firebase-talk)
    * [ Release notes ](/support/releases)
    * [ Brand guidelines ](/brand-guidelines/)
    * [ FAQs ](/support/faq/)

[ ![Google Developers](https://www.gstatic.com/devrel-
devsite/prod/v35e3d347a323c673294794cf0b643760fd66bb529efbd7dccaa22518acef0297/firebase/images/lockup-
google-for-developers.svg) ](https://developers.google.com/)

  * [ Android ](//developer.android.com)
  * [ Chrome ](//developer.chrome.com/home)
  * [ Firebase ](//firebase.google.com)
  * [ Google Cloud Platform ](//cloud.google.com)
  * [ All products ](//developers.google.com/products/)

  * [ Terms ](/terms/)
  * [ Privacy ](//policies.google.com/privacy)
  * Manage cookies 

  * English
  * Español – América Latina
  * Indonesia
  * Português – Brasil
  * 中文 – 简体
  * 日本語
  * 한국어

