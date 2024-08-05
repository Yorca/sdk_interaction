plugins {
    id("com.android.application")
}

android {
    namespace = "com.sdkint.sdkintappodealvungle"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.sdkint.sdkintappodealvungle"
        minSdk = 34
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }
    buildFeatures {
        viewBinding = true
    }
}

dependencies {

    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("com.google.android.material:material:1.12.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    implementation("androidx.navigation:navigation-fragment:2.7.7")
    implementation("androidx.navigation:navigation-ui:2.7.7")
    implementation("com.appodeal.ads:sdk:3.3.2.0") {
        exclude(group = "com.appodeal.ads.sdk.networks", module = "admob")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "amazon")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "applovin")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "applovin_max")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "bigo_ads")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "dt_exchange")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "inmobi")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "ironsource")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "meta")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "mintegral")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "my_target")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "pangle")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "unity_ads")
        exclude(group = "com.appodeal.ads.sdk.networks", module = "yandex")
        exclude(group = "com.appodeal.ads.sdk.services", module = "adjust")
        exclude(group = "com.appodeal.ads.sdk.services", module = "appsflyer")
        exclude(group = "com.appodeal.ads.sdk.services", module = "facebook_analytics")
        exclude(group = "com.appodeal.ads.sdk.services", module = "firebase")
        exclude(group = "io.bidmachine", module = "ads.networks.amazon")
        exclude(group = "io.bidmachine", module = "ads.networks.meta_audience")
        exclude(group = "io.bidmachine", module = "ads.networks.mintegral")
        exclude(group = "io.bidmachine", module = "ads.networks.my_target")
        exclude(group = "io.bidmachine", module = "ads.networks.pangle")
        exclude(group = "org.bidon", module = "admob-adapter")
        exclude(group = "org.bidon", module = "gam-adapter")
        exclude(group = "org.bidon", module = "amazon-adapter")
        exclude(group = "org.bidon", module = "applovin-adapter")
        exclude(group = "org.bidon", module = "bigoads-adapter")
        exclude(group = "org.bidon", module = "dtexchange-adapter")
        exclude(group = "org.bidon", module = "inmobi-adapter")
        exclude(group = "org.bidon", module = "mintegral-adapter")
        exclude(group = "org.bidon", module = "meta-adapter")
        exclude(group = "org.bidon", module = "unityads-adapter")
    }
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
}