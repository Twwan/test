from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup, QPushButton, QGroupBox, 
QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QCheckBox)
i = 0
b = 0
c = 0
result = 0
def test1():
    btn_answer1.show()
    btn_answer2.show()
    btn_answer3.show()
    btn_answer4.show()
    btn_answer1t.hide()
    btn_answer2t.hide()
    btn_answer3t.hide()
    btn_answer4t.hide()
    question.setText(quest1.question)
    btn_answer1.setText(quest1.wrong2)
    btn_answer2.setText(quest1.wrong1)
    btn_answer3.setText(quest1.right_answer)
    btn_answer4.setText(quest1.wrong3)
    last.hide()
    test1start.hide()
    test2start.hide()
    welcome.hide()
    test1text.hide()
    test2text.hide()
    trueansw.hide()
    trueansw2.hide()
    trueansw3.hide()
    Quest1GrBox.show()
    question.show()
    answer.show()
def test2():
    question.setText(test2_quest1.question)
    btn_answer1.setText(test2_quest1.right_answer)
    btn_answer2.setText(test2_quest1.wrong1)
    btn_answer3.setText(test2_quest1.wrong2)
    btn_answer4.setText(test2_quest1.wrong3)
    last.hide()
    test1start.hide()
    test2start.hide()
    welcome.hide()
    test1text.hide()
    test2text.hide()
    trueans.hide()
    trueans2.hide()
    trueans3.hide()
    question.show()
    Quest1GrBox.show()
    test2_answer.show()
def test2_result1():
    if btn_answer1.isChecked():
        global i
        i = i + 1
        question.hide()
        true.show()
        Quest1GrBox.hide()
        test2_answer.hide()
        test2_next_question.show()
    elif btn_answer2.isChecked() or btn_answer3.isChecked() or btn_answer4.isChecked():
        question.hide()
        nottrue.show()
        Quest1GrBox.hide()
        False1GrBox.show()
        test2_answer.hide()
        test2_next_question.show()
    else:
        victory_win = QMessageBox()
        victory_win.setText('Может всё-таки ответишь?')
        victory_win.exec_()
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def test2_result2():
    if btn_answer4.isChecked():
        global i
        i = i + 1
        question.hide()
        true.show()
        Quest1GrBox.hide()
        test2_answer_2.hide()
        test2_next_question2.show()
    elif btn_answer1.isChecked() or btn_answer2.isChecked() or btn_answer3.isChecked():
        question.hide()
        nottrue.show()
        Quest1GrBox.hide()
        False2GrBox.show()
        test2_answer_2.hide()
        test2_next_question2.show()
    else:
        victory_win = QMessageBox()
        victory_win.setText('Может всё-таки ответишь?')
        victory_win.exec_()
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def test2_result3():
    if btn_answer1t.isChecked() and btn_answer2t.isChecked() and btn_answer3t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь только два ответа')
        victory_win.exec_()
    elif btn_answer1t.isChecked() and btn_answer2t.isChecked() and btn_answer4t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь только два ответа')
        victory_win.exec_()
    elif btn_answer1t.isChecked() and btn_answer3t.isChecked() and btn_answer4t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь только два ответа')
        victory_win.exec_()
    elif btn_answer2t.isChecked() and btn_answer3t.isChecked() and btn_answer4t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь только два ответа')
        victory_win.exec_()
    elif btn_answer2t.isChecked() and btn_answer3t.isChecked():
        global i
        i = i + 1
        question.hide()
        true.show()
        Quest1GrBox.hide()
        test2_answer_3.hide()
        test2_end.show()
    elif btn_answer2t.isChecked() and btn_answer4t.isChecked():
        i = i + 0.5
        question.hide()
        truee.show()
        Quest1GrBox.hide()
        False3GrBox.show()
        test2_answer_3.hide()
        test2_end.show()
    elif btn_answer3t.isChecked() and btn_answer4t.isChecked():
        i = i + 0.5
        question.hide()
        truee.show()
        Quest1GrBox.hide()
        False3GrBox.show()
        test2_answer_3.hide()
        test2_end.show()
    elif btn_answer1t.isChecked() and btn_answer2t.isChecked():
        i = i + 0.5
        question.hide()
        truee.show()
        Quest1GrBox.hide()
        False3GrBox.show()
        test2_answer_3.hide()
        test2_end.show()
    elif btn_answer1t.isChecked() and btn_answer3t.isChecked():
        i = i + 0.5
        question.hide()
        truee.show()
        Quest1GrBox.hide()
        False3GrBox.show()
        test2_answer_3.hide()
        test2_end.show()
    elif btn_answer1t.isChecked() and btn_answer4t.isChecked():
        question.hide()
        nottrue.show()
        Quest1GrBox.hide()
        False3GrBox.show()
        test2_answer_3.hide()
        test2_end.show()
    elif btn_answer1t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь два ответа')
        victory_win.exec_()
    elif btn_answer2t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь два ответа')
        victory_win.exec_()
    elif btn_answer3t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь два ответа')
        victory_win.exec_()
    elif btn_answer4t.isChecked():
        victory_win = QMessageBox()
        victory_win.setText('Здесь два ответа')
        victory_win.exec_()  
    else:
        victory_win = QMessageBox()
        victory_win.setText('Может всё-таки ответишь?')
        victory_win.exec_()
def test2_next_q():
    question.show()
    question.setText(test2_quest2.question)
    btn_answer1.setText(test2_quest2.wrong1)
    btn_answer2.setText(test2_quest2.wrong2)
    btn_answer3.setText(test2_quest2.wrong3)
    btn_answer4.setText(test2_quest2.right_answer)
    False1GrBox.hide()
    Quest1GrBox.show()
    true.hide()
    nottrue.hide()
    test2_next_question.hide()
    test2_answer_2.show()
def test2_next_q2():
    question.show()
    question.setText(test2_quest3.question)
    btn_answer1t.show()
    btn_answer2t.show()
    btn_answer3t.show()
    btn_answer4t.show()
    btn_answer1.hide()
    btn_answer2.hide()
    btn_answer3.hide()
    btn_answer4.hide()
    False2GrBox.hide()
    Quest1GrBox.show()
    true.hide()
    nottrue.hide()
    test2_next_question2.hide()
    test2_answer_3.show()
def test2_end_q3():
    False3GrBox.hide()
    empty.show()
    test2_EndBox.show()
    true.hide()
    nottrue.hide()
    truee.hide()
    question.hide()
    endtext.show()
    test2_end.hide()
    back.show()
    global b
    b = 1
    result = QLabel(str(i) + '/3')
    layoutH_end_test2.addWidget(result, alignment = Qt.AlignCenter)    
#тест про основателей
def result1():
    if btn_answer3.isChecked():
        global i
        i = i + 1
        question.hide()
        true.show()
        Quest1GrBox.hide()
        answer.hide()
        next_question.show()
    elif btn_answer1.isChecked() or btn_answer2.isChecked() or btn_answer4.isChecked():
        question.hide()
        nottrue.show()
        Quest1GrBox.hide()
        False1GrBox.show()
        answer.hide()
        next_question.show()
    else:
        victory_win = QMessageBox()
        victory_win.setText('Может всё-таки ответишь?')
        victory_win.exec_()
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def result2():
    if btn_answer1.isChecked():
        global i
        i = i + 1
        question.hide()
        true.show()
        Quest1GrBox.hide()
        answer2.hide()
        next_question2.show()
    elif btn_answer3.isChecked() or btn_answer2.isChecked() or btn_answer4.isChecked():
        question.hide()
        nottrue.show()
        Quest1GrBox.hide()
        False2GrBox.show()
        answer2.hide()
        next_question2.show()
    else:
        victory_win = QMessageBox()
        victory_win.setText('Может всё-таки ответишь?')
        victory_win.exec_()
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
def result3():
    if btn_answer2.isChecked():
        global i
        i = i + 1
        question.hide()
        true.show()
        Quest1GrBox.hide()
        answer3.hide()
        end.show()
    elif btn_answer1.isChecked() or btn_answer3.isChecked() or btn_answer4.isChecked():
        question.hide()
        nottrue.show()
        Quest1GrBox.hide()
        False3GrBox.show()
        answer3.hide()
        end.show()
    else:
        victory_win = QMessageBox()
        victory_win.setText('Может всё-таки ответишь?')
        victory_win.exec_()
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
#следующий вопрос (1-2)
def next_q():
    question.show()
    question.setText(quest2.question)
    btn_answer1.setText(quest2.right_answer)
    btn_answer2.setText(quest2.wrong1)
    btn_answer3.setText(quest2.wrong2)
    btn_answer4.setText(quest2.wrong3)
    False1GrBox.hide()
    Quest1GrBox.show()
    true.hide()
    nottrue.hide()
    next_question.hide()
    answer2.show()
#следующий вопрос (2-3)
def next_q2():
    question.setText(quest3.question)
    btn_answer1.setText(quest3.wrong1)
    btn_answer2.setText(quest3.right_answer)
    btn_answer3.setText(quest3.wrong2)
    btn_answer4.setText(quest3.wrong3)
    False2GrBox.hide()
    Quest1GrBox.show()
    true.hide()
    nottrue.hide()
    question.show()
    next_question2.hide()
    answer3.show()
#завершение
def end_q3():
    False3GrBox.hide()
    EndBox.show()
    true.hide()
    nottrue.hide()
    question.hide()
    global c
    c = 1
    endtext.show()
    end.hide()
    back.show()
    result = QLabel(str(i) + '/3')
    layoutH_end.addWidget(result, alignment = Qt.AlignCenter)
def back_to_menu1():
    if c == 1 and b == 1:
        EndBox.hide()
        test2_EndBox.hide()
        endtext.hide()
        back.hide()
        endend.show()
    elif c == 1:
        global i
        i = 0
        EndBox.hide()
        test2_EndBox.hide()
        endtext.hide()
        back.hide()
        test2start.show()
        last.show()
        test2text.show()
        trueansw.show()
        trueansw2.show()
        trueansw3.show()
    elif b == 1:
        i = 0
        EndBox.hide()
        test2_EndBox.hide()
        endtext.hide()
        back.hide()
        test1start.show()
        last.show()
        test1text.show()
        trueans.show()
        trueans2.show()
        trueans3.show()
    else:
        EndBox.hide()
        test2_EndBox.hide()
        endtext.hide()
        back.hide()
        welcome.show()
    empty.hide()
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
class Question2():
    def __init__(self, question, right_answer, right_answer2, wrong1, wrong2):
        self.question = question
        self.right_answer = right_answer
        self.right_answer2 = right_answer2
        self.wrong1 = wrong1
        self.wrong2 = wrong2   
quest1 = Question('Кто создал Windows?', 'Билл Гейтс', 'Энди Рубин', 'Винтон Серф', 'Роберт Эллиот Кан')
quest2 = Question('Как зовут создателя Facebook?', 'Марк Цукерберг', 'Павел Дуров', 'Джефф Безос', 'Стив Джобс')
quest3 = Question('Один из создателей Google?', 'Ларри Пейдж', 'Мартин Гудмен', 'Конрад Цузе', 'Линус Торвальдс')
test2_quest1 = Question('Какая серия игр относится к Electronic Arts?', 'Need for Speed', 'Grand Theft Auto', 'Mafia', 'Saints Row')
test2_quest2 = Question('Главный герой игры Mafia 2?', 'Вито Скалетта', 'Карл Джонсон', 'Томас Анджело', 'Линкольн Клей')
test2_quest3 = Question2('Жанр игры Minecraft?', 'Приключения', 'Песочница', 'Шутер', 'Стратегии')
#создание окна
app = QApplication([])
main_win = QWidget()
main_win.setFixedSize(350, 260)
main_win.setWindowTitle('Тестер')
#выбор
test1start = QPushButton('Начать')
test2start = QPushButton('Начать')
welcome = QLabel('Добро пожаловать! Выберите тест:')
test1text = QLabel('Основатели')
test2text = QLabel('Игры')
layoutHtests = QHBoxLayout()
layoutHwelcome_text = QHBoxLayout()
layoutHstart_button = QHBoxLayout()
#кнопка Назад
back = QPushButton('<- В меню')
back.hide()
back2 = QPushButton('<- В меню')
back2.hide()
layoutHback = QHBoxLayout()
endend = QLabel('На этом всё!')
endend.hide()
last = QLabel('Тест пройден, остался ещё один')
last.hide()
layoutHempty = QHBoxLayout()
empty = QLabel('')
empty.hide()
#вопрос 1
question = QLabel('здесь вопрос')
question.setText(quest1.question)
question.hide()
answer = QPushButton('Ответить')
answer.hide()

btn_answer1 = QRadioButton('ответ 1')
btn_answer1.setText(quest1.wrong2)
btn_answer2 = QRadioButton('ответ 2')
btn_answer2.setText(quest1.wrong1)
btn_answer3 = QRadioButton('ответ 3')
btn_answer3.setText(quest1.right_answer)
btn_answer4 = QRadioButton('ответ 4')
btn_answer4.setText(quest1.wrong3)

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

btn_answer1t = QCheckBox()
btn_answer1t.setText(test2_quest3.wrong1)
btn_answer1t.hide()

btn_answer2t = QCheckBox()
btn_answer2t.setText(test2_quest3.right_answer2)
btn_answer2t.hide()

btn_answer3t = QCheckBox()
btn_answer3t.setText(test2_quest3.right_answer)
btn_answer3t.hide()

btn_answer4t = QCheckBox()
btn_answer4t.setText(test2_quest3.wrong2)
btn_answer4t.hide()

next_question = QPushButton('Следующий вопрос')
next_question.hide()
next_question2 = QPushButton('Следующий вопрос')
next_question2.hide()
#вопрос 2
answer2 = QPushButton('Ответить')
answer2.hide()
#вопрос 3
answer3 = QPushButton('Ответить')
answer3.hide() #прячем кнопку 
#конец
end = QPushButton('Завершить')
end.hide() #прячем кнопку 
endtext = QLabel('Спасибо за уделённое время!')
endtext.hide()
#боксы с ответами
Quest1GrBox = QGroupBox('Варианты ответов:')
Quest1GrBox.hide()
EndBox = QGroupBox('Ваш результат:')
EndBox.hide()
#верные ответы
trueans = QLabel('Ответ: Билл Гейтс')
trueans2 = QLabel('Ответ: Марк Цукерберг')
trueans3 = QLabel('Ответ: Ларри Пейдж')
#боксы верно/неверно 1
true = QLabel('Верно! Возьми печеньку')
true.hide()
nottrue = QLabel('Неверно!')
nottrue.hide()
truee = QLabel('Верно наполовину! Возьми половину печеньки')
truee.hide()
#
test2_answer = QPushButton('Ответить')
test2_answer.hide()

test2_next_question = QPushButton('Следующий вопрос')
test2_next_question.hide()

test2_answer_2 = QPushButton('Ответить')
test2_answer_2.hide()

test2_next_question2 = QPushButton('Следующий вопрос')
test2_next_question2.hide()

test2_answer_3 = QPushButton('Ответить')
test2_answer_3.hide()

test2_end = QPushButton('Завершить')
test2_end.hide()

trueansw = QLabel('Ответ: Need for Speed')
trueansw2 = QLabel('Ответ: Вито Скалетта')
trueansw3 = QLabel('Ответ: Песочница и Приключения')

test2GrBox = QGroupBox('Варианты ответов:')
test2GrBox.hide()
test2GrBox2 = QGroupBox('Варианты ответов:')
test2GrBox2.hide()
test2GrBox3 = QGroupBox('Варианты ответов:')
test2GrBox3.hide()
test2_EndBox = QGroupBox('Ваш результат:')
test2_EndBox.hide()

False1GrBox = QGroupBox()
False1GrBox.hide()
#боксы верно/неверно 2
False2GrBox = QGroupBox()
False2GrBox.hide()
#боксы верно/неверно 3
False3GrBox = QGroupBox()
False3GrBox.hide()
#поле с вопросом
layoutH1_quest = QHBoxLayout()
layoutH1_test2 = QHBoxLayout()
#к вопросу первый
layoutH2_ans = QHBoxLayout()
layoutH3_ans = QHBoxLayout()
layoutV1_box1 = QVBoxLayout()
layoutH2_test2 = QHBoxLayout()
layoutH3_test2 = QHBoxLayout()
layoutV1_test2 = QVBoxLayout()
#к вопросу второму
layoutH22_ans = QHBoxLayout()
layoutH33_ans = QHBoxLayout()
layoutV2_box2 = QVBoxLayout()
layoutH22_test2 = QHBoxLayout()
layoutH33_test2 = QHBoxLayout()
layoutV2_test2 = QVBoxLayout()
#к вопросу третьему
layoutH222_ans = QHBoxLayout()
layoutH333_ans = QHBoxLayout()
layoutV3_box3 = QVBoxLayout()
layoutH222_test2 = QHBoxLayout()
layoutH333_test2 = QHBoxLayout()
layoutV3_test2 = QVBoxLayout()
#к правильному первому
layoutH1_True = QHBoxLayout()
layoutV1_True = QHBoxLayout()
layoutH1_True2 = QHBoxLayout()
layoutV1_True2 = QHBoxLayout()
#к правильному второму
layoutH2_True = QHBoxLayout()
layoutV2_True = QHBoxLayout()
layoutH2_True2 = QHBoxLayout()
layoutV2_True2 = QHBoxLayout()
#к правильному второму
layoutH3_True = QHBoxLayout()
layoutV3_True = QHBoxLayout()
layoutH3_True2 = QHBoxLayout()
layoutV3_True2 = QHBoxLayout()
#завершение
layoutH_end = QHBoxLayout()
layoutV4_box4 = QVBoxLayout()

#кнопка "след. вопрос"
layoutH4_button = QHBoxLayout()
layoutH_end_test2 = QVBoxLayout()
layoutV4_test2 = QVBoxLayout()
#
layoutHwelcome_text.addWidget(welcome, alignment = Qt.AlignCenter)
layoutHwelcome_text.addWidget(endend, alignment = Qt.AlignCenter)
layoutHwelcome_text.addWidget(last, alignment = Qt.AlignCenter)
layoutHback.addWidget(back, alignment = Qt.AlignCenter)
layoutHback.addWidget(back2, alignment = Qt.AlignCenter)
layoutHtests.addWidget(test1text, alignment = Qt.AlignCenter)
layoutHtests.addWidget(test2text, alignment = Qt.AlignCenter)
layoutHstart_button.addWidget(test1start, alignment = Qt.AlignCenter)
layoutHstart_button.addWidget(test2start, alignment = Qt.AlignCenter)
#привязка вопросов к первому layout
layoutH1_quest.addWidget(question, alignment = Qt.AlignCenter)
layoutH1_quest.addWidget(true, alignment = Qt.AlignCenter)
layoutH1_quest.addWidget(truee, alignment = Qt.AlignCenter)
layoutH1_quest.addWidget(nottrue, alignment = Qt.AlignCenter)

layoutHempty.addWidget(empty, alignment = Qt.AlignCenter)
layoutH1_quest.addWidget(endtext, alignment = Qt.AlignCenter)
#привязка ответов 1 к layout
layoutH4_button.addWidget(answer, alignment = Qt.AlignCenter)
layoutH4_button.addWidget(back, alignment = Qt.AlignCenter)
layoutH4_button.addWidget(next_question, alignment = Qt.AlignCenter)
layoutH2_ans.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2_ans.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3_ans.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3_ans.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutH2_ans.addWidget(btn_answer1t, alignment = Qt.AlignCenter)
layoutH2_ans.addWidget(btn_answer2t, alignment = Qt.AlignCenter)
layoutH3_ans.addWidget(btn_answer3t, alignment = Qt.AlignCenter)
layoutH3_ans.addWidget(btn_answer4t, alignment = Qt.AlignCenter)

#привязка ответов 2 к layout
layoutH4_button.addWidget(answer2, alignment = Qt.AlignCenter)
layoutH4_button.addWidget(next_question2, alignment = Qt.AlignCenter)

#привязка ответов 3 к layout
layoutH4_button.addWidget(answer3, alignment = Qt.AlignCenter)
layoutH4_button.addWidget(end, alignment = Qt.AlignCenter)

layoutH4_button.addWidget(test2_answer, alignment = Qt.AlignCenter)
layoutH4_button.addWidget(test2_next_question, alignment = Qt.AlignCenter)

layoutH4_button.addWidget(test2_answer_2, alignment = Qt.AlignCenter)
layoutH4_button.addWidget(test2_next_question2, alignment = Qt.AlignCenter)

layoutH4_button.addWidget(test2_answer_3, alignment = Qt.AlignCenter)
layoutH4_button.addWidget(test2_end, alignment = Qt.AlignCenter)

#привязка правильного ответа 1 к layout
layoutH1_True.addWidget(trueans, alignment = Qt.AlignCenter)
layoutH1_True.addWidget(trueansw, alignment = Qt.AlignCenter)
layoutH2_True.addWidget(trueans2, alignment = Qt.AlignCenter)
layoutH2_True.addWidget(trueansw2, alignment = Qt.AlignCenter)
layoutH3_True.addWidget(trueans3, alignment = Qt.AlignCenter)
layoutH3_True.addWidget(trueansw3, alignment = Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(layoutHempty)
layout_main.addLayout(layoutH1_quest)
#привязываем боксы с ответами к вертикальному layout
Quest1GrBox.setLayout(layoutV1_box1)

test2GrBox.setLayout(layoutV1_test2)
test2GrBox2.setLayout(layoutV2_test2)
test2GrBox3.setLayout(layoutV3_test2)

False1GrBox.setLayout(layoutV1_True)
False2GrBox.setLayout(layoutV2_True)
False3GrBox.setLayout(layoutV3_True)

EndBox.setLayout(layoutV4_box4)
test2_EndBox.setLayout(layoutV4_test2)

layoutV1_box1.addLayout(layoutH2_ans)
layoutV1_box1.addLayout(layoutH3_ans)
layoutV2_box2.addLayout(layoutH22_ans)
layoutV2_box2.addLayout(layoutH33_ans)
layoutV3_box3.addLayout(layoutH222_ans)
layoutV3_box3.addLayout(layoutH333_ans)
layoutV1_True.addLayout(layoutH1_True)
layoutV2_True.addLayout(layoutH2_True)
layoutV3_True.addLayout(layoutH3_True)

layoutV1_test2.addLayout(layoutH2_test2)
layoutV1_test2.addLayout(layoutH3_test2)
layoutV2_test2.addLayout(layoutH22_test2)
layoutV2_test2.addLayout(layoutH33_test2)
layoutV3_test2.addLayout(layoutH222_test2)
layoutV3_test2.addLayout(layoutH333_test2)

layoutV4_box4.addLayout(layoutH_end)
layoutV4_test2.addLayout(layoutH_end_test2)

layout_main.addWidget(Quest1GrBox, alignment = Qt.AlignCenter)
layout_main.addWidget(False1GrBox, alignment = Qt.AlignCenter)
layout_main.addWidget(False2GrBox, alignment = Qt.AlignCenter)
layout_main.addWidget(False3GrBox, alignment = Qt.AlignCenter)

layout_main.addWidget(EndBox, alignment = Qt.AlignCenter)
layout_main.addWidget(test2_EndBox, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutHwelcome_text)
layout_main.addLayout(layoutHback)
layout_main.addLayout(layoutHtests)
layout_main.addLayout(layoutHstart_button)
layout_main.addLayout(layoutH1_test2)
layout_main.addWidget(test2GrBox, alignment = Qt.AlignCenter)
layout_main.addWidget(test2GrBox2, alignment = Qt.AlignCenter)
layout_main.addWidget(test2GrBox3, alignment = Qt.AlignCenter)
layout_main.addWidget(test2_EndBox, alignment = Qt.AlignCenter)
layout_main.addLayout(layoutH4_button)

main_win.setLayout(layout_main)
#
test1start.clicked.connect(test1)
test2start.clicked.connect(test2)
#реакция на нажатие (ответы 1)
answer.clicked.connect(result1)
next_question.clicked.connect(next_q)

test2_answer.clicked.connect(test2_result1)
test2_next_question.clicked.connect(test2_next_q)
#реакция на нажатие (ответы 2)
answer2.clicked.connect(result2)
next_question2.clicked.connect(next_q2)

test2_answer_2.clicked.connect(test2_result2)
test2_next_question2.clicked.connect(test2_next_q2)
#реакция на нажатие (ответы 3)
answer3.clicked.connect(result3)
end.clicked.connect(end_q3)

test2_answer_3.clicked.connect(test2_result3)
test2_end.clicked.connect(test2_end_q3)
back.clicked.connect(back_to_menu1)

main_win.show()
app.exec_()