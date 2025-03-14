from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSpacerItem, QSizePolicy, QMenu, QMessageBox, QLineEdit
from PySide6.QtCore import Qt
import sys, random


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.__init__ui()
    
    def __init__ui(self):
        self.setWindowTitle('Математика для детей')

        _screen_width = int(QApplication.primaryScreen().geometry().width() * 0.5)
        _screen_height = int(QApplication.primaryScreen().geometry().height() * 0.8)
        _x = ((_screen_width * 2) - _screen_width) / 2
        _y = ((_screen_height * 1.25) - _screen_height) / 2
        self.setGeometry(_x, _y, _screen_width, _screen_height)

        self.setStyleSheet("""
            QWidget { 
                background-color: #2c3e50;
            }
            QPushButton { 
                background-color: #1abc9c;
                padding: 10px;
                border-radius: 10px;
                font-size: 20px;
            }
            QPushButton:hover { 
                background-color: #16a085;
            }
            QLabel {
                font-family: JetBrains Mono;
                color: white; 
            }
            #titleLabel {
                font-size: 36px;
                font-weight: bold;
            }               
            #textLabel {
                font-size: 24px;
                font-weight: bold;    
            }
            #contactsLabel {
                font-size: 18px;      
            }
        """)

        self.layout = QVBoxLayout()
        self.layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.2), QSizePolicy.Minimum, QSizePolicy.Minimum))

        self._title_label = QLabel("Здравствуйте!")
        self._title_label.setAlignment(Qt.AlignCenter)
        self._title_label.setObjectName("titleLabel")
        self.layout.addWidget(self._title_label)

        self._text_label = QLabel("Это приложение для изучения \n математики детьми всех возрастов")
        self._text_label.setAlignment(Qt.AlignCenter)
        self._text_label.setObjectName("textLabel")
        self.layout.addWidget(self._text_label)

        self.layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.2), QSizePolicy.Minimum, QSizePolicy.Minimum))

        self._button = QPushButton("Перейти")
        self._button.setObjectName("button")
        self._button.clicked.connect(self._init_train_room)
        self.layout.addWidget(self._button, alignment=Qt.AlignCenter)

        self.layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.1), QSizePolicy.Minimum, QSizePolicy.Minimum))
        
        self._contacts_label = QLabel('Обратная связь')
        self._contacts_label.setOpenExternalLinks(True)
        self._contacts_label.setTextFormat(Qt.RichText)
        self._contacts_label.setText('<a href="https:/scr1pt0.gim@gmail.com">Обратная связь</a>')
        self._contacts_label.setAlignment(Qt.AlignCenter)
        self._contacts_label.setObjectName("contactsLabel")
        self.layout.addWidget(self._contacts_label)

        self.setLayout(self.layout)

    def resizeEvent(self, event):
        """ Адаптивный размер кнопки при изменении окна """
        button_width = int(self.width() * 0.25)
        button_height = int(self.height() * 0.07)
        self._button.setFixedSize(button_width, button_height)
        super().resizeEvent(event)
    
    def _init_train_room(self):
        self._train_room = TrainWindow()
        self._train_room.show()
        self.hide()


class TrainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__init__ui()
        self.selected_level = None
        self.selected_topic = None
    
    def __init__ui(self):
        self.setWindowTitle('Математика для детей')

        _screen_width = int(QApplication.primaryScreen().geometry().width() * 0.5)
        _screen_height = int(QApplication.primaryScreen().geometry().height() * 0.8)
        _x = ((_screen_width * 2) - _screen_width) / 2
        _y = ((_screen_height * 1.25) - _screen_height) / 2
        self.setGeometry(_x, _y, _screen_width, _screen_height)

        self.setStyleSheet("""
            QWidget { 
                background-color: #2c3e50;
            }
            QPushButton { 
                background-color: #1abc9c;
                padding: 10px;
                border-radius: 10px;
                font-size: 20px;
            }
            QPushButton:hover { 
                background-color: #16a085;
            }
            QLabel {
                font-family: JetBrains Mono;
                color: white;
                font-size: 28px;
                font-weight: bold;
                color: #808080;
            }
            QMenu {
                font-size: 20px;
                color: black;
                background-color: white;
            }
        """)
        
        self._layout = QVBoxLayout()

        self._layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.2), QSizePolicy.Minimum, QSizePolicy.Minimum))

        self._lvl_label = QLabel('Уровень')
        self._lvl_label.setAlignment(Qt.AlignCenter)
        self._layout.addWidget(self._lvl_label, alignment=Qt.AlignCenter)

        self._topic_label = QLabel('Тема')
        self._topic_label.setAlignment(Qt.AlignCenter)
        self._layout.addWidget(self._topic_label, alignment=Qt.AlignCenter)

        self._layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.15), QSizePolicy.Minimum, QSizePolicy.Minimum))
        
        self._lvl_button = QPushButton('Выбор уровня')
        self._lvl_button.clicked.connect(self.show_level_menu)
        self._layout.addWidget(self._lvl_button, alignment=Qt.AlignCenter)

        self._topic_button = QPushButton('Выбор темы')
        self._topic_button.clicked.connect(self.show_topic_menu)
        self._layout.addWidget(self._topic_button, alignment=Qt.AlignCenter)

        self._start_button = QPushButton('Начать')
        self._start_button.clicked.connect(self.start_exercises)
        self._layout.addWidget(self._start_button, alignment=Qt.AlignCenter)

        self.back_btn = QPushButton("Назад")
        self.back_btn.clicked.connect(self.go_back)
        self._layout.addWidget(self.back_btn, alignment=Qt.AlignCenter)

        self._layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.2), QSizePolicy.Minimum, QSizePolicy.Expanding))


        self.setLayout(self._layout)

    def resizeEvent(self, event):
        """ Адаптивный размер кнопки при изменении окна """
        button_width = int(self.width() * 0.25)
        button_height = int(self.height() * 0.07)
        self._lvl_button.setFixedSize(button_width, button_height)
        self._topic_button.setFixedSize(button_width, button_height)
        self._start_button.setFixedSize(button_width, button_height)
        self.back_btn.setFixedSize(button_width, button_height)
        super().resizeEvent(event)
    
    def start_exercises(self):
        if not self.selected_level or not self.selected_topic:
            QMessageBox.warning(self, "Ошибка", "Выберите уровень и тему!")
            return
            
        self.exercise_window = ExerciseWindow(self.selected_level, self.selected_topic)
        self.exercise_window.show()
        self.close()

    def show_level_menu(self):
        """ Показать меню для выбора уровня """
        menu = QMenu(self)
        levels = ["Легкий", "Средний", "Сложный"]
        for level in levels:
            action = menu.addAction(level)
            action.triggered.connect(lambda checked, lvl=level: self.on_level_selected(lvl))
        menu.exec_(self._lvl_button.mapToGlobal(self._lvl_button.rect().center()))

    def show_topic_menu(self):
        """ Показать меню для выбора темы """
        menu = QMenu(self)
        topics = ["Сложение", "Вычитание", "Умножение", "Деление", "Деление с остатком"]
        for topic in topics:
            action = menu.addAction(topic)
            action.triggered.connect(lambda checked, tpc=topic: self.on_topic_selected(tpc))
        menu.exec_(self._topic_button.mapToGlobal(self._topic_button.rect().center()))

    def on_level_selected(self, level):
        """ Обработчик выбора уровня """
        self.selected_level = level
        self._lvl_label.setText(f"{level}")
        self._lvl_label.setStyleSheet('color: white')

    def on_topic_selected(self, topic):
        """ Обработчик выбора темы """
        self.selected_topic = topic
        self._topic_label.setText(f"{topic}")
        self._topic_label.setStyleSheet('color: white')
    
    def go_back(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()


class ExampleGenerator:
    def __init__(self, level, operation):
        self.level = level
        self.operation = operation
        self.operators = {
            'Сложение': '+',
            'Вычитание': '-',
            'Умножение': '*',
            'Деление': '//',
            'Деление с остатком': '/'
        }
    
    def truncate(self, number, digits):
        if number == int(number):
            return int(number)
        else:
            return float(f"{number:.{digits}f}") 

    def generate(self):
        op = self.operators[self.operation]
        level_ranges = {
            'Легкий': (1, 9),
            'Средний': (10, 99),
            'Сложный': (100, 999)
        }
        a = random.randint(*level_ranges[self.level])
        b = random.randint(*level_ranges[self.level])
        
        if op == '//':
            a = a * b
            question = f"{a} {op} {b}"
            answer = a // b
        elif op == '/':
            question = f"{a} {op} {b}"
            answer = self.truncate(a / b, 6)
        else:
            question = f"{a} {op} {b}"
            answer = eval(question)
            
        return question, answer

class ExerciseWindow(QWidget):
    def __init__(self, level, topic):
        super().__init__()
        self.level = level
        self.topic = topic
        self.total_exercises = 5
        self.solved = 0
        self.correct = 0
        self.mistake = 0
        self.generator = ExampleGenerator(level, topic)
        self.__init__ui()
        self.next_question()

    def __init__ui(self):
        self.setWindowTitle('Математика для детей')

        self.setStyleSheet("""
            QWidget { 
                background-color: #2c3e50;
            }
            QLabel {
                color: white;
                font-size: 24px;
                font-family: JetBrains Mono;
            }
            QLineEdit {
                background-color: transparent;
                border-radius: 10px;
                padding: 10px;
                font-size: 24px;
                border: none;
                border-bottom: 2px solid #808080;
                border-radius: 0;
                
            }
            QPushButton {
                background-color: #1abc9c;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 24px;
            }
            #counterLabel {
                font-size: 18px;           
            }
            #hintLabel {
                font-size: 14px;
            }
        """)

        _screen_width = int(QApplication.primaryScreen().geometry().width() * 0.5)
        _screen_height = int(QApplication.primaryScreen().geometry().height() * 0.8)
        _x = ((_screen_width * 2) - _screen_width) / 2
        _y = ((_screen_height * 1.25) - _screen_height) / 2
        self.setGeometry(_x, _y, _screen_width, _screen_height)

        self._layout = QVBoxLayout()

        self._layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.1), QSizePolicy.Minimum, QSizePolicy.Minimum))

        self._counter_label = QLabel(f"Выполнено {self.solved} задач из {self.total_exercises}")
        self._counter_label.setObjectName('counterLabel')
        self._layout.addWidget(self._counter_label, alignment=Qt.AlignCenter)

        self.question_label = QLabel()
        self.question_label.setAlignment(Qt.AlignCenter)
        self._layout.addWidget(self.question_label)

        self.answer_input = QLineEdit()
        self.answer_input.returnPressed.connect(self.check_answer)
        self.answer_input.setPlaceholderText("Введите ответ")
        self._layout.addWidget(self.answer_input, alignment=Qt.AlignCenter)

        buttons_container = QVBoxLayout()
        buttons_container.setSpacing(10)
        buttons_container.setAlignment(Qt.AlignCenter)

        self.submit_btn = QPushButton("Ввести")
        self.submit_btn.clicked.connect(self.check_answer)

        self.back_btn = QPushButton("Назад")
        self.back_btn.clicked.connect(self.go_back)

        buttons_container.addWidget(self.submit_btn)
        buttons_container.addWidget(self.back_btn)
        self._layout.addLayout(buttons_container)

        self._layout.addSpacerItem(QSpacerItem(0, int(_screen_height * 0.2), QSizePolicy.Minimum, QSizePolicy.Minimum))
    
        self.hint_label = QLabel()
        self.hint_label.setOpenExternalLinks(True)
        self.hint_label.setTextFormat(Qt.RichText)
        self.hint_label.setText('<a href="https://example.com">Нужна помощь? Посмотрите примеры здесь</a>')
        self.hint_label.setObjectName('hintLabel')
        self.hint_label.hide()
        self._layout.addWidget(self.hint_label, alignment=Qt.AlignCenter)

        self.setLayout(self._layout)

    
    def check_answer(self):
        user_answer = self.answer_input.text()
        if user_answer == str(self.current_answer):
            self.hint_label.hide()
            self.mistake = 0
            self.correct += 1
            self.solved += 1
            self._counter_label.setText(f"Выполнено {self.solved} задач из {self.total_exercises}")
            if self.solved < self.total_exercises:
                self.next_question()
            else:
                self.answer_input.setEnabled(False)
                self.submit_btn.setEnabled(False)
                self._counter_label.setText("✅ Поздравляем! Все задачи решены!")
        else:
            self.mistake += 1
            if self.mistake >= 3:
                self.hint_label.show()
            self.answer_input.clear()
            self.answer_input.setFocus()


    def next_question(self):
        self.current_question, self.current_answer = self.generator.generate()
        self.question_label.setText(self.current_question + " = ")
        self.answer_input.clear()
        self.answer_input.setFocus()

    def resizeEvent(self, event):
        """ Адаптивный размер кнопки при изменении окна """
        button_width = int(self.width() * 0.25)
        button_height = int(self.height() * 0.07)
        self.submit_btn.setFixedSize(button_width, button_height)
        self.back_btn.setFixedSize(button_width, button_height)
        super().resizeEvent(event)
    
    def go_back(self):
        self.train_room = TrainWindow()
        self.train_room.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
