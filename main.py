import random

from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(700, 500)

menu_button = QPushButton("Меню")
pause_btn = QPushButton("Відпочити")
spin_box = QSpinBox()
min = QLabel("Хвилин")
question = QLabel("Яблука")
grupe_box = QGroupBox("Варіанти відповідей")

answers = [QRadioButton("building"), QRadioButton("application"), QRadioButton("cellerpiller"), QRadioButton("apple")]
random.shuffle(answers)

vidpovistu = QPushButton("Відповісти")

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
grupe_line.addWidget(answers[0])
grupe_line.addWidget(answers[1])
grupe_line.addWidget(answers[2])
grupe_line.addWidget(answers[3])
grupe_box.setLayout(grupe_line)
main_line.addWidget(grupe_box)

main_line.addWidget(vidpovistu)

window.show()
app.exec()