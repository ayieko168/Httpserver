from PyQt5.QtWidgets import *
from MainDesign import *
from startupDialog import *
import socket


class StartUpDialog(QDialog):

    def __init__(self):

        super().__init__()
        self.StartUpUi = Ui_Form()
        self.StartUpUi.setupUi(self)

        # connections
        self.StartUpUi.SDStartButton.clicked.connect(self.connectCMD)
        self.StartUpUi.SDCancelButton.clicked.connect(self.cancelCMD)

        # variables
        self.IP = 
        self.PORT 

    def connectCMD(self):

        print(f"Dialog connect")
        self.hide()

    def cancelCMD(self):

        self.hide()

    def run(self):

        self.show()
        self.exec_()


class App(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # variables
        local_ip = socket.gethostbyname(socket.gethostname()) 

        
    
    def Connect(self):

        print("Main connect")
        
    
if __name__ == "__main__":
    
    w = QApplication([])
    app = App()

    # show connection dialog first
    dialog = StartUpDialog()
    dialog.run()
    
    # execute main instance
    app.show()
    w.exec_()