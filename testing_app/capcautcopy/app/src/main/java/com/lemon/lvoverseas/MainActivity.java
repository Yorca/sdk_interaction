package com.lemon.lvoverseas;

import android.os.Bundle;
import com.applovin.sdk.AppLovinSdkConfiguration;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;

import androidx.core.view.WindowCompat;
import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.lemon.lvoverseas.databinding.ActivityMainBinding;

import android.view.Menu;
import android.view.MenuItem;

import com.applovin.sdk.AppLovinSdk;
import com.applovin.sdk.AppLovinPrivacySettings;
import com.facebook.ads.AdSettings;

import android.util.Log;
import com.facebook.ads.AudienceNetworkAds;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class MainActivity extends AppCompatActivity {

    private AppBarConfiguration appBarConfiguration;
    private ActivityMainBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        binding = ActivityMainBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        setSupportActionBar(binding.toolbar);

        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_content_main);
        appBarConfiguration = new AppBarConfiguration.Builder(navController.getGraph()).build();
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);

        binding.fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAnchorView(R.id.fab)
                        .setAction("Action", null).show();
            }
        });

        initApplovin();
    }

    private void initApplovin() {
//        AudienceNetworkAds.initialize(this);
//        Log.d("AudienceNetworkAds.initialize", "" + AudienceNetworkAds.isInitialized(this));

//        AppLovinPrivacySettings.setIsAgeRestrictedUser(true, this);
        AppLovinPrivacySettings.setHasUserConsent(true, this);
        AppLovinPrivacySettings.setDoNotSell(true,this);
        AppLovinSdk.getInstance( this ).setMediationProvider( "max" );
        AppLovinSdk.initializeSdk( this, new AppLovinSdk.SdkInitializationListener() {
            @Override
            public void onSdkInitialized(final AppLovinSdkConfiguration configuration)
            {
                Log.d("onSdkInitialized", "onSdkInitialized");
                Log.d("facebook mixed", "" + AdSettings.isMixedAudience());

            }

        } );

//        HashMap<String, String > map = new HashMap<String, String >();
//        map.put("test", "1");

        HashSet<String> map = new HashSet<String>();
        map.add("new item");


        testHook();
        map.add("new item 2");
        testHook();


    }

    public void testHook() {
        System.out.println("ree");
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public boolean onSupportNavigateUp() {
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_content_main);
        return NavigationUI.navigateUp(navController, appBarConfiguration)
                || super.onSupportNavigateUp();
    }
}