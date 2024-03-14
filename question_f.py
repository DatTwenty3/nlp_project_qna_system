import re
import csv

file_path = ("data/data.csv")

no_subject = 0
term_11 = 0
term_12 = 1
term_21 = 2
term_22 = 3

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
        question = question.lower()
    if check_phrase(question, "nhiêu môn") or check_phrase(question, "mấy môn"):
        if check_phrase(question, "kỳ 1"):
            # Học kì 1 và 2
            if check_phrase(question,"và 2"):
                #Học kì 1 và 2 năm học thứ 1
                if check_phrase(question,"năm học thứ 1") or check_phrase(question,"năm 1") or check_phrase(question,"năm nhất"):
                    number_of_subject = check_no_subject(1, 1, 2)
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 và 2 năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                    return
                # Học kì 1 và 2 năm học thứ 2
                if check_phrase(question,"năm học thứ 2") or check_phrase(question,"năm 2") or check_phrase(question,"năm hai"):
                    number_of_subject = check_no_subject(2, 1, 2)
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 và 2 năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                    return

            # Học kì 1 năm học thứ 1
            if check_phrase(question,"năm học thứ 1") or check_phrase(question,"năm 1") or check_phrase(question,"năm nhất"):
                # Học kì 1 năm học thứ 1 và thứ 2
                if check_phrase(question, "và thứ 2") or check_phrase(question, "và năm 2") or check_phrase(question, "và năm hai"):
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile, delimiter=';')
                        for row in reader:
                            term = row['term']
                            if int(term[term_11]) == 1 and int(term[term_21]) == 1:
                                number_of_subject = number_of_subject + 1
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 năm học thứ 1 và thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                    return
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[term_11]) == 1:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 1 năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                return
            # Học kì 1 năm học thứ 2
            if check_phrase(question,"năm học thứ 2") or check_phrase(question,"năm 2") or check_phrase(question,"năm hai"):
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[term_21]) == 1:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 1 năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                return

        if check_phrase(question, "kỳ 2"):
            # Học kì 2 năm học thứ 1
            if check_phrase(question,"năm học thứ 1") or check_phrase(question,"năm 1") or check_phrase(question,"năm nhất"):
                # Học kì 2 năm học thứ 1 và thứ 2
                if check_phrase(question, "và thứ 2") or check_phrase(question, "và năm 2") or check_phrase(question, "và năm hai"):
                    with open(file_path, newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile, delimiter=';')
                        for row in reader:
                            term = row['term']
                            if int(term[term_12]) == 2 and int(term[term_22]) == 2:
                                number_of_subject = number_of_subject + 1
                    with open("answer_f.txt", "a", encoding="utf-8") as f:
                        f.write("A: Học kì 1 năm học thứ 1 và thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                    return
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[term_12]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 2 năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                return
            # Học kì 2 năm học thứ 2
            if check_phrase(question,"năm học thứ 2") or check_phrase(question,"năm 2") or check_phrase(question,"năm hai"):
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[term_22]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Học kì 1 năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                return

        if check_phrase(question, "2 học kỳ ") or check_phrase(question, "2 kỳ"):
            # Ca 2 học kỳ năm học thứ 1
            if check_phrase(question,"năm học thứ 1") or check_phrase(question,"năm 1") or check_phrase(question,"năm nhất"):
                # Cả 2 học kỳ năm học thứ 1 va thứ 2
                if check_phrase(question, "và thứ 2") or check_phrase(question, "và năm 2") or check_phrase(question, "và năm hai"):
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
                        if int(term[term_11]) == 1 and int(term[term_12]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Cả 2 học kỳ năm học thứ 1 có " + str(number_of_subject) + " môn học được dạy\n")
                return
            # Ca 2 học kỳ năm học thứ 2
            if check_phrase(question,"năm học thứ 2") or check_phrase(question,"năm 2") or check_phrase(question,"năm hai"):
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=';')
                    for row in reader:
                        term = row['term']
                        if int(term[term_22]) == 1 and int(term[term_22]) == 2:
                            number_of_subject = number_of_subject + 1
                with open("answer_f.txt", "a", encoding="utf-8") as f:
                    f.write("A: Cả 2 học kỳ năm học thứ 2 có " + str(number_of_subject) + " môn học được dạy\n")
                return

    with open("answer_f.txt", "a", encoding="utf-8") as f:
        f.write("NO ANSWER - SKIP!\n")
    return