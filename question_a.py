from pyvi import ViTokenizer, ViPosTagger
import re

def analyze_sentence(sentence):
    raw_sentence = sentence
    #Loại bỏ ký tự đặc biệt và khoảng trắng cuối câu
    sentence = re.sub(r'[^\w\s]', '', sentence)
    sentence = sentence.strip()
    # Phân đoạn câu thành các từ
    sentence = ViTokenizer.tokenize(sentence)
    # Phân loại từng từ trong câu
    tagged_words = ViPosTagger.postagging(sentence)
    tagged_words = list(zip(tagged_words[0], tagged_words[1]))
    with open("answer_a.txt", "a", encoding="utf-8") as f:
        f.write("Câu được phân tích: " + raw_sentence + "\n")
    # Ghi kết quả vào file
    for word, tag in tagged_words:
        with open("answer_a.txt", "a", encoding="utf-8") as f:
            f.write(f"Word: {word}, Tag: {tag}\n")