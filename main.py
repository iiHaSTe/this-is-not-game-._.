import time #Import time
import random #Import random
import sys #Import system
#pyQT 5
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox, QLabel
from PyQt5.QtGui import QFont

#VARS

#Functions
def hh():
	con = int(scoor.text()) + 1
	ran = str(round(random.uniform(1, 5000)))
	ranX = round(random.uniform(100, 1000))
	rany = round(random.uniform(100, 700))
	btn2.setGeometry(ranX, rany, 70, 70)
	btn2.setText(ran)
	btn1.setFont(QFont("arail", 30))
	scoor.setText(str(con))
	btn1.hide()
	btn2.show()
def hhh():
	con = int(scoor.text()) + 1
	ran = str(round(random.uniform(0, 2000)))
	ranX = round(random.uniform(100, 900))
	rany = round(random.uniform(100, 600))
	btn1.setGeometry(ranX, rany, 70, 70)
	btn1.setText(ran)
	btn1.setFont(QFont("arail", 30))
	scoor.setText(str(con))
	btn1.show()
	btn2.hide()

def r():
	question = QMessageBox.question(root, "سؤال", "هل انت متأكد ؟", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
	if question==QMessageBox.Yes:
		btn1.setGeometry(640, 400, 70, 70)
		btn1.setText("click me")
		btn2.setGeometry(560, 400, 70, 70)
		btn1.setFont(QFont("arail", 10))
		scoor.setText("0")
		btn1.show()
		btn2.hide()

def exit():
	question = QMessageBox.question(root, "سؤال", "هل انت حقا تريد الخروج ؟", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
	if question==QMessageBox.Yes:
		root.destroy()
#Windows
a = QApplication(sys.argv)
root = QWidget()
root.resize(1280, 800)

main = QWidget()
main.resize(1280, 800)
#buttons
btn1 = QPushButton("click me", root)
btn1.setGeometry(640, 400, 70, 70)
btn1.pressed.connect(hh)
btn1.setFont(QFont("arail", 10))

btn2 = QPushButton("", root)
btn2.setGeometry(560, 400, 70, 70)
btn2.pressed.connect(hhh)
btn2.setFont(QFont("arail", 30))

rest = QPushButton("Rest", root)
rest.setGeometry(0, 0, 70, 70)
rest.clicked.connect(r)
rest.setFont(QFont("arail", 22))

exite = QPushButton("Exit", root)
exite.setGeometry(1210, 0, 70, 70)
exite.clicked.connect(exit)
exite.setFont(QFont("arail", 22))
#texts
scoor = QLabel(root)
scoor.setGeometry(1280/2, 0, 300, 45)
scoor.setText("0")
scoor.setFont(QFont("arail", 50))

#shows
btn1.show()
root.show()
box = QMessageBox.question(root, "سؤااال", "هل تريد لعب لعبتي الخايسة؟", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
if box==QMessageBox.No:
	root.destroy()
elif box==QMessageBox.Yes:
	t = str(time.time())
	timee = QLabel(root)
	timee.setText(t)
	timee.setFont(QFont("arail", 50))
	#timee.move(200, 0)
#Hides
btn2.hide()
main.hide()
sys.exit(a.exec_())
