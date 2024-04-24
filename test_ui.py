from PySide import QtGui, QtCore
import maya.OpenMaya as OpenMaya
from pymel.core import selected
Signal = QtCore.Signal
#dsajlgkdsjkfdsjklafsldfsf
class SigController(QtCore.QObject):
    selectionChanged = Signal(list)

class WindowSignal(QtGui.QMainWindow):
    convertClicked = Signal(str)

def create_window(controller, parent=None):
    window = WindowSignal(parent)
    window.setWindowTitle('Testing')
    container = QtGui.QWidget(window)
    label = QtGui.QLabel('Do stuff', container)
    textbox = QtGui.QLineEdit(container)
    button = QtGui.QPushButton('Boom', container)
    statusbar = window.statusBar()

    def onclick():
        window.convertClicked.emit(textbox.text())
    button.clicked.connect(onclick)

    def update_statusbar(newsel):
        if not newsel:
            text = 'nothing selected'
        elif len(newsel) == 1:
            text = '{obj} selected'.format(obj=newsel[0])
        else:
            text = '{num} objects selected'.format(num=len(newsel))
        statusbar.showMessage(text)
    controller.selectionChanged.connect(update_statusbar)

    layout = QtGui.QHBoxLayout(container)
    container.setLayout(layout)
    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)
    window.setCentralWidget(container)
    return window

_window = None
def show():
    global _window

    if _window is None:
        controller = SigController()
        def emit_selchanged(_):
            controller.selectionChanged.emit(selected(type='transform'))
        OpenMaya.MEventMessage.addEventCallback('SelectionChanged', emit_selchanged)
        parent = QtGui.QApplication.activeWindow()
        _window = create_window(controller, parent)
    _window.show()








"""" Python testing Code """
# def _pytest():
#     import random

#     controller = SigController()
#     def nextsel():
#         return random.choice([[], ['single'], ['single', 'double']])   
    
#     def onconvert(words):
#         print 'clicked! {sig}'.format(sig=words)
#         controller.selectionChanged.emit(nextsel())

#     app = QtGui.QApplication([])
#     win = create_window(controller)
#     win.convertClicked.connect(onconvert)
#     win.show()
#     app.exec_()

# if __name__ == '__main__':
#     _pytest()
