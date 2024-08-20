plugins {
    id("com.android.application")
}

android {
    namespace = "com.sdkint.applovinfacebook2"
    compileSdk = 3

    defaultConfig {
        applicationId = "com.sdkint.applovinfacebook2"
        minSdk = 33
        targetSdk = 33
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

    implementation("androidx.appcompat:appcompat:+")
    implementation("com.google.android.material:material:+")
    implementation("androidx.constraintlayout:constraintlayout:+")
    implementation("androidx.navigation:navigation-fragment:+")
    implementation("androidx.navigation:navigation-ui:+")
    implementation("com.applovin:applovin-sdk:+")
    implementation("com.applovin.mediation:facebook-adapter:+")
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
}