import re
import nltk
from nltk.corpus import stopwords, words
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('words')
def clear_content(log_content, contains_method_call):
    log_lines = log_content.strip().split('\n')

    unique_lines = set()

    meaningful_lines = []

    english_words = set(words.words())
    stop_words = set(stopwords.words('english'))
    def is_obfuscated(method_name):
        method_name = method_name.lower()
        if method_name in english_words:
            return False
        vowels = set('aeiou')
        num_vowels = sum(1 for char in method_name if char in vowels)
        if len(method_name) == 0:
            return True
        vowel_ratio = num_vowels / len(method_name)
        if vowel_ratio < 0.3:
            return True
        if not any(char in vowels for char in method_name):
            return True
        return False

    method_call_pattern = re.compile(r'^Call method (\w+);')

    for line in log_lines:
        line = line.strip()
        if line not in unique_lines:
            unique_lines.add(line)
            words_in_line = word_tokenize(line)
            meaningful_words = [word for word in words_in_line if word.lower() not in stop_words and word.isalpha()]
            if meaningful_words:
                meaningful_lines.append(line)


    cleaned_log = '\n'.join(meaningful_lines)
    return cleaned_log