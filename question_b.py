from pyvi import ViTokenizer, ViPosTagger
import re

def extract_syntax_relations(sentence):
    raw_sentence = sentence
    # Phân đoạn câu thành các từ
    words = ViTokenizer.tokenize(sentence).split(" ")

    # Loại bỏ ký tự đặc biệt và khoảng trắng cuối câu
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.strip()

    # Phân đoạn câu thành các từ
    sentence = ViTokenizer.tokenize(sentence)
    # Phân loại từng từ trong câu
    tagged_words = ViPosTagger.postagging(sentence)
    tagged_words = list(zip(tagged_words[0], tagged_words[1]))

    with open("answer_b.txt", "a", encoding="utf-8") as f:
        f.write("Câu được phân tích: " + raw_sentence + "\n")
    for i in range(len(tagged_words)):
        word, tag = tagged_words[i]
        if i > 0:
            prev_word, prev_tag = tagged_words[i-1]
            with open("answer_b.txt", "a", encoding="utf-8") as f:
                f.write(f"{prev_word} ({prev_tag}) -> {word} ({tag})\n")