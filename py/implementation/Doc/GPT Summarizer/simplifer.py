import json
import os

from sentence_transformers import SentenceTransformer, util

# Load the pre-trained sentence transformer model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
similarity_threshold = 0.8
# Function to find and keep the most detailed sentence
def filter_similar_sentences(sentences):
    if len(sentences) <= 1:
        return sentences
    threshold = similarity_threshold
    embeddings = model.encode(sentences, convert_to_tensor=True)
    kept_sentences = []
    skip_indices = set()

    # Compare each sentence with every other sentence
    for i, sentence in enumerate(sentences):
        if i in skip_indices:
            continue

        # Compare sentence i with all others
        for j in range(i + 1, len(sentences)):
            if j in skip_indices:
                continue

            similarity = util.pytorch_cos_sim(embeddings[i], embeddings[j]).item()

            if similarity > threshold:
                # Keep the more detailed sentence based on length
                if len(sentences[i]) >= len(sentences[j]):
                    skip_indices.add(j)  # Skip j
                else:
                    skip_indices.add(i)  # Skip i
                    break

        if i not in skip_indices:
            kept_sentences.append(sentences[i])

    return kept_sentences

summary_dir = "summary/merged"
filter_dir = "summary/filtered2"
original_count = 0
new_count = 0
for file_name in os.listdir(summary_dir):
    file_path = os.path.join(summary_dir, file_name)
    print(file_path)
    with open(file_path, 'r') as file:
        data = file.read()
    js_data = json.loads(data)
    for api in js_data["privacy_APIs"]:
        print(api["effects"])
        original_count += len(api["conditions"]) + len(api["effects"])
        api["conditions"] = filter_similar_sentences(api["conditions"])
        api["effects"] = filter_similar_sentences(api["effects"])
        new_count += len(api["conditions"]) + len(api["effects"])
        for config in api["parameter_configurations"]:
            original_count += len(config["conditions"]) + len(config["effects"])
            config["conditions"] = filter_similar_sentences(config["conditions"])
            config["effects"] = filter_similar_sentences(config["effects"])
            new_count += len(config["conditions"]) + len(config["effects"])


    new_data = json.dumps(js_data, indent=4)
    with open(os.path.join(filter_dir, file_name), "w") as file:
        file.write(new_data)

print(f"remove : {original_count-new_count} / {original_count}")

# print(filter_similar_sentences([
#                         "User has provided consent for GDPR.",
#                         "User has given their consent",
#                         "User has given consent for data processing under GDPR.",
#                         "User has provided consent",
#                         "User consent is obtained for GDPR"
#                     ]))
