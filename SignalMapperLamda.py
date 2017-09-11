from datetime import time
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QApplication
from PyQt5.QtWidgets import QPushButton


class MyForm(QMainWindow):
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        layout = QHBoxLayout()

        for pic in range(3):
            button = QPushButton()
            cmd = lambda button, func=self.on_button: func(pic)
            button.clicked.connect(cmd)

        # button = QPushButton('Button 1')
        #
        # button.clicked.connect(lambda: self.on_button(1))
        # layout.addWidget(button)
        #
        # button = QPushButton('Button 2')
        # button.clicked.connect(lambda: self.on_button(2))
            layout.addWidget(button)

        main_frame = QWidget()
        main_frame.setLayout(layout)

        self.setCentralWidget(main_frame)

    def on_button(self, n):
        print('Button {0} clicked'.format(n))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MyForm()
    form.show()
    app.exec_()