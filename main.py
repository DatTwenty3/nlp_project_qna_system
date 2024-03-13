import question_a as qa
import question_b as qb
import re

# Đường dẫn tới file "query.txt"
file_path = "data/query.txt"

def clear_file(file_path):
    # Mở file với chế độ ghi mới, làm cho nội dung bên trong trống rỗng
    with open(file_path, "w", encoding="utf-8") as f:
        pass

try:
    # Mở file và đọc nội dung
    with open(file_path, "r", encoding="utf-8") as file:
        queries = file.readlines()
        question = 0
        #Xoá trắng file answer_a.txt
        clear_file("answer_a.txt")
        clear_file("answer_b.txt")
        # In ra màn hình từng câu trong file
        for query in queries:
            question = question + 1
            query_content = re.sub(r"^\d+\)\s*", "", query.strip())
            qa.analyze_sentence(query_content)
            print("Đã ghi kết quả câu", question, "vào file answer_a.txt")
            qb.extract_syntax_relations(query_content)
            print("Đã ghi kết quả câu", question, "vào file answer_b.txt")
except FileNotFoundError:
    print(f"Không tìm thấy file '{file_path}'")