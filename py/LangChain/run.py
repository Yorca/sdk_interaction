import json
import os
import time

from trace_builder import get_trace
from context_builder import get_context
from detector import detect, detect_v2, detect_v3, detect_v4, detect_v5
from chain_detector import chain_detector, chain_detector_v2
from profile_builder import get_profile
logs = os.listdir("res/detection")
log_pkgs = [pkg.removesuffix('.log') for pkg in logs]


with open("../Dynamic/res/success_apks.log", "r") as file:
    pkgs = file.read().split('\n')
detected_path = "res/detected_apks.log"
with open(detected_path, "a") as file:
    file.write("")
with open(detected_path, "r") as file:
    detected_pkgs = file.read().split("\n")
for pkg in pkgs:
    try:
        if pkg in detected_pkgs:
            continue
        with open(detected_path, "a") as file:
            file.write(f"{pkg}\n")
        print(f"start {pkg}")
        print(f"fetching trace")
        traces = get_trace(pkg)
        # if not traces:
        #     print(f"no trace!")
        #     continue
        # print(f"fetching profile")
        # profile = get_profile(pkg)
        # # trace_path = os.path.join("res/trace", f"{pkg}.json")
        # # if not os.path.exists(trace_path):
        # #     continue
        # # print(trace_path)
        # # with open(trace_path, "r") as file:
        # #     traces = json.loads(file.read())
        # print(f"fetching context")
        # context = get_context(pkg, traces)
        # print(f"start detect")
        # chain_detector_v2(pkg)
    except Exception as e:
        with open("res/error.log", "a") as file:
            file.write(f"pkg: {pkg}   error: {e} \n ")


    # time.sleep(600)











