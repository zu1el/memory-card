import json
from PyQt5.QtWidgets import *

db = json.load(open('db.json', encoding='utf-8'))


def menu_window():
    window = QDialog()

    main_line = QVBoxLayout()
    firs_H_Line = QHBoxLayout()
    quest = QLabel("Питання")
    answer = QLabel("правильна відповід")
    false_answer1 = QLabel("не правильна відповідь")
    false_answer2 = QLabel("не правильна відповідь")
    false_answer3 = QLabel("не правильна відповідь")
    quest_ = QLineEdit()
    false_answer1_ = QLineEdit()
    false_answer2_ = QLineEdit()
    false_answer3_ = QLineEdit()
    answer_ = QLineEdit()
    firs_H_Line.addWidget(quest)
    firs_H_Line.addWidget(quest_)
    firs_H_Line.addWidget(answer)
    firs_H_Line.addWidget(answer_)
    firs_H_Line.addWidget(false_answer1)
    firs_H_Line.addWidget(false_answer1_)
    firs_H_Line.addWidget(false_answer2)
    firs_H_Line.addWidget(false_answer2_)
    firs_H_Line.addWidget(false_answer3)
    firs_H_Line.addWidget(false_answer3_)
    second_H_line = QHBoxLayout()
    add_quest = QPushButton("Додати питання")
    second_H_line.addWidget(add_quest)
    main_line.addLayout(firs_H_Line)
    main_line.addLayout(second_H_line)


    def db_update():
        question = {
            "Запитання": quest_.text(),
            "Правильна відповідь": answer_.text(),
            "Неправильна 1": false_answer1_.text(),
            "Неправильна 2": false_answer2_.text(),
            "Неправильна 3": false_answer3_.text()
        }
        db["questions"].append(question)
        with open("db.json", "w", encoding="utf-8") as file:
            json.dump(db, file, ensure_ascii=False)

    add_quest.clicked.connect(db_update)
    window.setLayout(main_line)
    window.exec()

def edit_window():
    window = QDialog()
    question = db["questions"][db["cur questoin"]]

    main_line = QVBoxLayout()
    firs_H_Line = QHBoxLayout()
    quest = QLabel("Питання")
    answer = QLabel("правильна відповід")
    false_answer1 = QLabel("не правильна відповідь")
    false_answer2 = QLabel("не правильна відповідь")
    false_answer3 = QLabel("не правильна відповідь")
    quest_ = QLineEdit(question["Запитання"])
    false_answer1_ = QLineEdit(question["Неправильна 1"])
    false_answer2_ = QLineEdit(question["Неправильна 2"])
    false_answer3_ = QLineEdit(question["Неправильна 3"])
    answer_ = QLineEdit(question["Правильна відповідь"])
    firs_H_Line.addWidget(quest)
    firs_H_Line.addWidget(quest_)
    firs_H_Line.addWidget(answer)
    firs_H_Line.addWidget(answer_)
    firs_H_Line.addWidget(false_answer1)
    firs_H_Line.addWidget(false_answer1_)
    firs_H_Line.addWidget(false_answer2)
    firs_H_Line.addWidget(false_answer2_)
    firs_H_Line.addWidget(false_answer3)
    firs_H_Line.addWidget(false_answer3_)
    second_H_line = QHBoxLayout()
    edit_quest = QPushButton("редагувати питання")
    second_H_line.addWidget(edit_quest)
    main_line.addLayout(firs_H_Line)
    main_line.addLayout(second_H_line)


    def db_update():
        question = {
            "Запитання": quest_.text(),
            "Правильна відповідь": answer_.text(),
            "Неправильна 1": false_answer1_.text(),
            "Неправильна 2": false_answer2_.text(),
            "Неправильна 3": false_answer3_.text()
        }
        print(question)
        db["questions"][db["cur questoin"]] = question
        with open("db.json", "w", encoding="utf-8") as file:
            json.dump(db, file, ensure_ascii=False)

    edit_quest.clicked.connect(db_update)
    window.setLayout(main_line)
    window.exec()

