package com.sdkint.applovinfacebook2;

import android.util.Log;

public class testClass2 {


    public void testFrida2() {
        Log.d("huzhaojie", "test");
    }
    public static void testFrida() {

        Thread currentThread = Thread.currentThread();

        // 输出当前线程的信息
        Log.d("huzhaojie", "Current thread" + currentThread.getName());
        Log.d("huzhaojie", "test");
    }
}