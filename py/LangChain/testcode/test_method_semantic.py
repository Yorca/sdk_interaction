import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

def has_semantic_meaning(method_name):
    # Tokenize the method name
    doc = nlp(method_name)
    meaningful_words = []

    # Check each token to see if it has semantic meaning
    for token in doc:
        # Check if the token is an English word and is not a stop word or punctuation
        if token.is_alpha and not token.is_stop and token.has_vector:
            meaningful_words.append(token.text)

    # Return True if any meaningful words are found, otherwise False
    return len(meaningful_words) > 0, meaningful_words

method_name = "dasd"
has_meaning, words = has_semantic_meaning(method_name)
print(f"Method name has semantic meaning: {has_meaning}")
if has_meaning:
    print(f"Meaningful words found: {words}")