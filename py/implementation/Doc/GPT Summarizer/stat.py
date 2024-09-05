import os

sdk_list = []
for dr in os.listdir("summaries2.0"):
    sdk_list.append(dr.replace(".json", ""))
print(sdk_list)

for dr2 in os.listdir("plaintext_summaries2.0"):
    sdk = dr2.replace(".txt", "")
    if sdk not in sdk_list:
        print(sdk)