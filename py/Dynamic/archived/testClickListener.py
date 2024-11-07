import frida
import time


script = """
Java.perform(function() {
    Java.deoptimizeEverything(); // Deoptimizes everything, not necessary in many cases
    var Button = Java.use("android.widget.Button");

    // Hook 按钮的 setOnClickListener 方法
    console.log("Button.setOnClickListener.overloads[0] = " + Button.setOnClickListener.overloads[0])
    Button.setOnClickListener.implementation = function(listener) {
        // 调用原始的 setOnClickListener 方法
        this.setOnClickListener(listener);
        console.log("enter")
        // Hook 按钮的 onClick 方法
        console.log("Button.onClick.overloads[0]=" + Button.onClick)
        var onClickListener = Java.use("android.view.View$OnClickListener");

        Button.onClick.overloads[0].implementation = function(view) {
            // 获取点击的按钮
            console.log("enter2")
            var button = Java.cast(view, Button);
            // 获取按钮的文本
            var buttonText = button.getText().toString();
            console.log("Button clicked: " + buttonText);
            // 调用原始的 onClick 方法
            this.onClick(view);
        };
    };
});


"""

def on_message(message, data):
    if 'payload' in message:
        print(message)


try:
    package_name = "com.xingin.xhs"
    print(f'start {package_name}')
    device = frida.get_usb_device()
    print(package_name)
    print(device)
    pid = device.spawn([package_name])
    session = device.attach(pid)
    script = session.create_script(script)
    # with open("script.txt", "a") as file:
    #     file.write(get_script_code(package_name))

    script.on('message', on_message)
    script.load()
    device.resume(pid)
    time.sleep(100)
    session.detach()
except Exception as e:
    print(f"error + {e}")