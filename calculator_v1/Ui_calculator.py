from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QWidget
from PyQt5 import uic
from Calculator_2 import Calculator
import sys

class CalculatorUI(QMainWindow, Calculator):
    def __init__(self) -> None:
        super(CalculatorUI, self).__init__()
        
        uic.loadUi('calculator.ui', self)

        self.widget = self.findChild(QWidget, 'widget')

        self.number_display = self.findChild(QLabel, 'Number_Display')

        self.ac_button = self.findChild(QPushButton, 'AC')
        self.backspace_button = self.findChild(QPushButton, 'Backspace')
        self.percentage_button = self.findChild(QPushButton, 'Percentage')
        self.divide_button = self.findChild(QPushButton, 'Divide')
        self.seven_button = self.findChild(QPushButton, 'Seven')
        self.eight_button = self.findChild(QPushButton, 'Eight')
        self.nine_button = self.findChild(QPushButton, 'Nine')
        self.multiply_button = self.findChild(QPushButton, 'Multiply')
        self.four_button = self.findChild(QPushButton, 'Four')
        self.five_button = self.findChild(QPushButton, 'Five')
        self.six_button = self.findChild(QPushButton, 'Six')
        self.subtract_button = self.findChild(QPushButton, 'Subtract')
        self.one_button = self.findChild(QPushButton, 'One')
        self.two_button = self.findChild(QPushButton, 'Two')
        self.three_button = self.findChild(QPushButton, 'Three')
        self.plus_button = self.findChild(QPushButton, 'Plus')
        self.zero_button = self.findChild(QPushButton, 'Zero')
        self.decimal_point_button = self.findChild(QPushButton, 'Decimal_Point')
        self.equals_button = self.findChild(QPushButton, 'Equals')

        widget_min_max_size = 351, 541
        self.widget.setMinimumSize(widget_min_max_size[0], widget_min_max_size[1])
        self.widget.setMaximumSize(widget_min_max_size[0], widget_min_max_size[1])

        self.ac_button.clicked.connect(lambda: self.button_pressed(self.ac_button.text()))
        self.backspace_button.clicked.connect(lambda: self.button_pressed(self.backspace_button.text()))
        self.percentage_button.clicked.connect(lambda: self.button_pressed(self.percentage_button.text()))
        self.divide_button.clicked.connect(lambda: self.button_pressed(self.divide_button.text()))
        self.seven_button.clicked.connect(lambda: self.button_pressed(self.seven_button.text()))
        self.eight_button.clicked.connect(lambda: self.button_pressed(self.eight_button.text()))
        self.nine_button.clicked.connect(lambda: self.button_pressed(self.nine_button.text()))
        self.multiply_button.clicked.connect(lambda: self.button_pressed(self.multiply_button.text()))
        self.four_button.clicked.connect(lambda: self.button_pressed(self.four_button.text()))
        self.five_button.clicked.connect(lambda: self.button_pressed(self.five_button.text()))
        self.six_button.clicked.connect(lambda: self.button_pressed(self.six_button.text()))
        self.subtract_button.clicked.connect(lambda: self.button_pressed(self.subtract_button.text()))
        self.one_button.clicked.connect(lambda: self.button_pressed(self.one_button.text()))
        self.two_button.clicked.connect(lambda: self.button_pressed(self.two_button.text()))
        self.three_button.clicked.connect(lambda: self.button_pressed(self.three_button.text()))
        self.plus_button.clicked.connect(lambda: self.button_pressed(self.plus_button.text()))
        self.zero_button.clicked.connect(lambda: self.button_pressed(self.zero_button.text()))
        self.decimal_point_button.clicked.connect(lambda: self.button_pressed(self.decimal_point_button.text()))
        self.equals_button.clicked.connect(lambda: self.button_pressed(self.equals_button.text()))

        self.show()

    numbers: list = []
    nth_term = []
    operation = ''
    current_number = ''
    result = 0
    past_operation = ''

    def button_pressed(self, button):
        print(f'log: {button} is pressed')
        # button_int = 0
        if button.isdecimal():
            self.current_number += button
            self.update_calculator_screen(self.current_number)
            button_int = int(button)
            self.nth_term.append(button_int)
            print(f'log: {self.nth_term} nth_term')
        # elif button == '=':
        #     self.numbers.append(self.nth_term)
        #     if self.operation == '+':
        #         print(self.sum(self.numbers))
        #     elif self.operation == '-':
        #         print(self.difference(self.numbers))
        #     elif self.operation == '*':
        #         print(self.product(self.numbers))
        #     elif self.operation == '/':
        #         print(self.quotient(self.numbers))

        #     self.numbers.append(self.nth_term)
        #     print(f'log: {self.numbers}')
        #     for term in self.numbers:
        #         nth_term = sum(term)
        #         self.numbers[self.numbers.index(term)] = nth_term #type:ignore
        #         print(f'log: {self.numbers}')
        #     else:
        #         self.numbers = sum(self.numbers) #type:ignore
        #         print(f'log: {self.numbers}')
                
        else:
            # self.result = int(self.current_number)
            if self.result == 0:
                if self.current_number == '0':
                    pass
                elif button == '+':
                    self.result += int(self.current_number)
                elif button == '-':
                    self.result -= int(self.current_number)
                elif button == '*':
                    self.result *= int(self.current_number)
                elif button == '/':
                    self.result /= int(self.current_number)
            else:
                if self.current_number == '0':
                    pass
                elif self.operation == '+':
                    self.result += int(self.current_number)
                elif self.operation == '-':
                    self.result -= int(self.current_number)
                elif self.operation == '*':
                    self.result *= int(self.current_number)
                elif self.operation == '/':
                    self.result /= int(self.current_number)
            # elif button == '=' and self.operation == '+':
            #     self.result += int(self.current_number)
            # elif button == '=' and self.operation == '-':
            #     self.result -= int(self.current_number)
            # elif button == '=' and self.operation == '*':
            #     self.result *= int(self.current_number)
            # elif button == '=' and self.operation == '/':
            #     self.result /= int(self.current_number)

            self.current_number = ''
            self.update_calculator_screen(str(self.result))
            self.numbers.append(self.nth_term)
            self.nth_term = []
            self.operation = button
            print(f'log: {self.numbers} else')
            print(f'log: {self.operation}')

        print(self.numbers)

    def update_calculator_screen(self, text):
        self.number_display.setText(text)

app = QApplication(sys.argv)
UiWindow = CalculatorUI()
app.exec_()
