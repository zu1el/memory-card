import random
import json
from PyQt5.QtWidgets import *

app = QApplication([])
db = json.load(open('db.json', encoding='utf-8'))

window = QWidget()
window.resize(700, 500)

menu_button = QPushButton("Меню")
pause_btn = QPushButton("Відпочити")
spin_box = QSpinBox()
min = QLabel("Хвилин")
question = QLabel("")
grupe_box = QGroupBox("Варіанти відповідей")
vidpovistu = QPushButton("Відповісти")
result_lbl = QLabel("")
result_lbl.hide()
next_quesion = QPushButton("Наступне питання")

answers = [QRadioButton(""), QRadioButton(""), QRadioButton(""), QRadioButton("")]
random.shuffle(answers)



main_line = QVBoxLayout()
firs_H_Line = QHBoxLayout()
firs_H_Line.addWidget(menu_button)
firs_H_Line.addStretch()
firs_H_Line.addWidget(pause_btn)
firs_H_Line.addWidget(spin_box)
firs_H_Line.addWidget(min)
window.setLayout(main_line)
main_line.addLayout(firs_H_Line)
main_line.addWidget(question)

grupe_line = QVBoxLayout()
line1 = QHBoxLayout()
line1.addWidget(answers[0])
line1.addWidget(answers[1])
line2 = QHBoxLayout()
line2.addWidget(answers[2])
line2.addWidget(answers[3])
grupe_line.addLayout(line2)
grupe_line.addLayout(line1)
grupe_box.setLayout(grupe_line)
main_line.addWidget(grupe_box)

main_line.addWidget(result_lbl)

main_line.addWidget(vidpovistu)
main_line.addWidget(next_quesion)

def set_question():
    num = db["cur questoin"]
    question.setText(db["questions"][num]["Запитання"])
    answers[3].setText(db["questions"][num]["Неправильна 1"])
    answers[1].setText(db["questions"][num]["Неправильна 2"])
    answers[2].setText(db["questions"][num]["Неправильна 3"])
    answers[0].setText(db["questions"][num]["Правильна відповідь"])

def answerClick():
    if answers[0].isChecked():
        result_lbl.setText("Правильно!")
    else:
        result_lbl.setText("Не правильно!")
    result_lbl.show()
    for i in range(len(answers)):
        answers[i].hide()

def next_question_func():
    db["cur questoin"] += 1
    set_question()
    for i in range(len(answers)):
        answers[i].show()

set_question()
vidpovistu.clicked.connect(answerClick)
next_question_func.clicked.connect(next_question_func)

window.show()
app.exec()