import spacy

# Khởi tạo mô hình spaCy cho tiếng Việt
nlp = spacy.load("vi")

# Tạo câu
cau = "Con mèo đang ngủ trên ghế sofa."

# Phân tích câu
doc = nlp(cau)

# Lấy các quan hệ ngữ pháp
for token in doc:
    print(token.text, token.dep_, token.head.text)