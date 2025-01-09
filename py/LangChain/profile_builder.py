
import env
import os
import json
from loaders import load_web

def get_app_property(pkg_name, fields):

    path = os.path.join(env.app_detail_path, pkg_name)
    if not os.path.exists(path):
        print("no exist")
        return None
    with open(path, "r") as file:
        data = file.read()
    data = json.loads(data)
    if fields:
        data = {k: v for k, v in data.items() if k in fields}
    print(f"data = {data}")
    return data

def get_profile(pkg):
    profile = ""

    # load env
    profile += f"**Running Environment:**\n{env.runtime_environment}\n"

    # load APK property
    property = get_app_property(pkg, ["title", "summary", "contentRating", "contentRatingDescription", "adSupported", "containsAds"])
    if property:
        des = f"The target user of this app is {property['contentRating']}\n"
        if property["contentRatingDescription"]:
            des += f"description: {property['contentRatingDescription']}\n"
        support_ads = "supports" if property["adSupported"] else "does not support"
        contains_ads = "contains" if property["containsAds"] else "does not contain"
        des += f"This APP {support_ads} ads\n"
        des += f"This APP {contains_ads} ads\n"
        with open("res/laws/google_play_family.log", "r") as file:
            apks = file.read().split('\n')
        if pkg in apks:
            des += "This app is committed to follow the Play Families Policy"
        # datasafety_info = "Null"#load_web(f"https://play.google.com/store/apps/datasafety?id={pkg}&hl=en&gl=us")
        # # property["data safety"] = "\n".join([doc.page_content for doc in datasafety_info])
        profile += f"**APP Property:**\n{des}\n"
    with open(f"res/profile/{pkg}.log", "a") as file:
        file.write(profile)
    return profile