import re
import csv

file_path = ("data/data.csv")
no_subject = 0
def check_phrase(sentence, phrase):
    pattern = rf"\b{phrase}\b"
    if re.search(pattern, sentence):
        return True
    else:
        return False


def check_no_subject(school_year, term_1, term_2):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        if school_year == 1:
            position = 0;
        else:
            position = 2
        no_subject = 0
        for row in reader:
            term = row['term']
            if len(term) >= school_year and int(term[position]) == term_1 and int(term[position + 1]) == term_2:
                no_subject = no_subject + 1
        return no_subject

def check_answer(question):
    with open("answer_f.txt", "a", encoding="utf-8") as f:
        number_of_subject = 0
        f.write("Q: " + question + "\n")
    if check_phrase(question, "Có bao nhiêu môn học được dạy"):
        if check_phrase(question, "học kỳ 1"):
            # Học kì 1 và 2
            if check_phrase(question,"và 2"):
                #Học kì 1 và 2 năm học thứ 1
                if check_phrase(question,"năm học thứ 1"):
                    number_of_subject = check_no_subject(1, 1, 2)
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 và 2 năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                    return
                # Học kì 1 và 2 năm học thứ 2
                if check_phrase(question,"năm học thứ 2"):
                    number_of_subject = check_no_subject(2, 1, 2)
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 và 2 năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                    return

            # Học kì 1 năm học thứ 1
            if check_phrase(question, "năm học thứ 1"):
                # Học kì 1 năm học thứ 1 và thứ 2
                if check_phrase(question, "và thứ 2"):
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile, delimiter=';')
                        for row in reader:
                            term = row['term']
                            if int(term[0]) == 1 and int(term[2]) == 1:
                                number_of_subject = number_of_subject + 1
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 năm học thứ 1 và thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                    return
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[0]) == 1:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 1 năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                return
            # Học kì 1 năm học thứ 2
            if check_phrase(question, "năm học thứ 2"):
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[2]) == 1:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 1 năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                return

        if check_phrase(question, "học kỳ 2"):
            # Học kì 2 năm học thứ 1
            if check_phrase(question, "năm học thứ 1"):
                # Học kì 2 năm học thứ 1 và thứ 2
                if check_phrase(question, "và thứ 2"):
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile, delimiter=';')
                        for row in reader:
                            term = row['term']
                            if int(term[1]) == 2 and int(term[3]) == 2:
                                number_of_subject = number_of_subject + 1
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 năm học thứ 1 và thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                    return
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[1]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 2 năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                return
            # Học kì 2 năm học thứ 2
            if check_phrase(question, "năm học thứ 2"):
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[3]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 1 năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                return

        if check_phrase(question, "cả 2 học kỳ "):
            # Ca 2 học kỳ năm học thứ 1
            if check_phrase(question, "năm học thứ 1"):
                # Cả 2 học kỳ năm học thứ 1 va thứ 2
                if check_phrase(question, "và thứ 2"):
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile, delimiter=';')
                        for row in reader:
                            term = row['term']
                            if '0' in term:
                                continue
                            else:
                                number_of_subject = number_of_subject + 1
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Cả 2 học kỳ năm học thứ 1 và thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                    return
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[0]) == 1 and int(term[1]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Cả 2 học kỳ năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                return
            # Ca 2 học kỳ năm học thứ 2
            if check_phrase(question, "năm học thứ 2"):
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[2]) == 1 and int(term[3]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Cả 2 học kỳ năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                return


    with open("answer_f.txt", "a", encoding="utf-8") as f:
        f.write("NO ANSWER - SKIP!\n")
    return