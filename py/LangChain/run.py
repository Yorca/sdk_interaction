import json
import os.path

from trace_builder import get_trace
from context_builder import get_context
from detector import detect
with open("../apps/install/success.txt", "r") as file:
    success_apks = file.readlines()
pkg_list = [apk.replace(".apk\n", "") for apk in success_apks]
for pkg in pkg_list[2:]:
    traces = get_trace(pkg)
    if not traces:
        continue
    trace_path = os.path.join("res/trace", f"{pkg}.json")
    if not os.path.exists(trace_path):
        continue
    print(trace_path)
    with open(trace_path, "r") as file:
        traces = json.loads(file.read())
    context = get_context(pkg, traces)
    # print(context)
    # detect(pkg)












