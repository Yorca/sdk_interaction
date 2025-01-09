import re
from nltk.corpus import words

# 加载英文词汇表
english_words = set(words.words())


def camel_case_to_words(method_name):
    # 将驼峰命名转换为单词列表
    words_list = re.findall(r'[A-Za-z][a-z]*|[A-Z][a-z]*', method_name)

    # 检查是否所有拆分出的部分都是有效的英文单词
    if all(word.lower() in english_words for word in words_list):
        return ' '.join(words_list)
    else:
        return None


# 示例
print(camel_case_to_words("setRequestConfiguration"))  # 输出: 'get User Name'
print(camel_case_to_words("zza"))  # 输出: None
