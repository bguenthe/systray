from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QAction, QLineEdit, QApplication


class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.mapper = QtCore.QSignalMapper(self)
        self.toolbar = self.addToolBar('Foo')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        for text in 'One Two Three'.split():
            action = QAction(text, self)
            self.mapper.setMapping(action, text)
            action.triggered.connect(self.mapper.map)
            self.toolbar.addAction(action)
        self.mapper.mapped['QString'].connect(self.handleButton)
        self.edit = QLineEdit(self)
        self.setCentralWidget(self.edit)

    def handleButton(self, identifier):
        if identifier == 'One':
            text = 'Do This'
        elif identifier == 'Two':
            text = 'Do That'
        elif identifier == 'Three':
            text = 'Do Other'
        self.edit.setText(text)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.resize(300, 60)
    window.show()
    sys.exit(app.exec_())