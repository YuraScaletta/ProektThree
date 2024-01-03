from PyQt5 import Qt
from PyQt5.QtWidgets import*

app = QApplication([])



window = QWidget()
window.setWindowTitle('Окошко для горошка')
window.move(300,5)
window.resize(300,300)
name = QLabel('Введіть імя')
name2 = QLineEdit()

label = QLabel('повна назва гри Gta IV')
r1=QRadioButton('Grand Table auto IV')
r2=QRadioButton('Green table auto IV')
r3=QRadioButton('Grand theft auto IV')
q1=QButtonGroup()
q1.addButton(r1)
q1.addButton(r2)
q1.addButton(r3)
labell = QLabel('скільки шкіл в Україні?')
ch1=QRadioButton('10000')
ch2=QRadioButton('13000')
ch3=QRadioButton('15000')
q2=QButtonGroup()
q2.addButton(ch1)
q2.addButton(ch2)
q2.addButton(ch3)
labelll = QLabel('4 самі популярні авто?')
b1=QRadioButton('Chevrole, Audi, Bmw, Mercedes')
b2=QRadioButton('Chevrole, Toyota, Bmw, Volvo')
b3=QRadioButton('Chevrole, Toyota, Bmw, Mercedes')
q3=QButtonGroup()
q3.addButton(b1)
q3.addButton(b2)
q3.addButton(b3)
labellll = QLabel('якого жанру серіал "Кухня"?')
a1=QRadioButton('Комедія')
a2=QRadioButton('Детектив')
a3=QRadioButton('фантастик')
a4=QRadioButton('Боевик')
q4=QButtonGroup()
q4.addButton(a1)
q4.addButton(a2)
q4.addButton(a3)
q4.addButton(a4)
labelllll = QLabel("які самі популярні празники?")
l1=QRadioButton('День свят, новий рік, пьятница')
l2=QRadioButton('день народження, новий рік, масляніца')
l3=QRadioButton('день народження, новий день, пьятница')
l4=QRadioButton('день сюрпризів, новий день, пьятница')
q5=QButtonGroup()
q5.addButton(l1)
q5.addButton(l2)
q5.addButton(l3)
q5.addButton(l4)
labellllll = QLabel("Який Президент України 2023")
p1=QRadioButton('Володимир Зеленьский')
p2=QRadioButton('Віктор Петрович')
p3=QRadioButton('Володимир Путін')
p4=QRadioButton('Тарас Шевченко')
q6=QButtonGroup()
q6.addButton(p1)
q6.addButton(p2)
q6.addButton(p3)
q6.addButton(p4)
v=QVBoxLayout()

v.addWidget(name)
v.addWidget(name2)
# вопрос 1
v.addWidget(label)
v.addWidget(r1)
v.addWidget(r2)
v.addWidget(r3)
# вопрос 2
v.addWidget(labell)
v.addWidget(ch1)
v.addWidget(ch2)
v.addWidget(ch3)

#3
v.addWidget(labelll)
v.addWidget(b1)
v.addWidget(b2)
v.addWidget(b3)
#4
v.addWidget(labellll)
v.addWidget(a1)
v.addWidget(a2)
v.addWidget(a3)
v.addWidget(a4)
#5
v.addWidget(labelllll)
v.addWidget(l1)
v.addWidget(l2)
v.addWidget(l3)
v.addWidget(l4)
#6
v.addWidget(labellllll)
v.addWidget(p1)
v.addWidget(p2)
v.addWidget(p3)
v.addWidget(p4)
g1=QPushButton("Ok")
v.addWidget(g1)
        
window.setLayout(v)

i=0
def hello():
    global i
    if r3.isChecked():
         i+=3
            
    if ch2.isChecked():
            i+=1

    if b3.isChecked():
         i+=3
            
    if a1.isChecked():
            i+=1
    
    if l2.isChecked():
         i+=2
            
    if p1.isChecked():
            i+=3
 
    info_win=QMessageBox()
    info_win.setWindowTitle('Результат')
    info_win.setText('Дякуємо, ваш тест завершено \n  ваш результат \n'+str(i)+" балів")
    info_win.exec_()
    with open("1.txt", "a",encoding="utf-8") as file:
        file.write("Ім'я  "+name2.text()+" результат "+str(i)+" балів")
        
        
g1.clicked.connect(hello)

window.show()
app.exec_()