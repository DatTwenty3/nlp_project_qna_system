import spacy

# Khởi tạo mô hình spaCy cho tiếng Việt
nlp = spacy.load("en_core_web_sm")

# Nhập câu tiếng Việt
cau = "Con mèo đen đang ngủ trên chiếc ghế sofa."

# Phân tích cú pháp câu
doc = nlp(cau)

# Duyệt qua các token trong câu
for token in doc:
    # In ra thông tin token
    print(f"Token: {token.text}")
    print(f"Từ loại: {token.pos_}")
    print(f"Quan hệ cú pháp: {token.dep_}")
    print(f"Chủ ngữ: {token.head.text}")
    print()

# In ra cây phân tích cú pháp
print(doc.sents[0].subtree)