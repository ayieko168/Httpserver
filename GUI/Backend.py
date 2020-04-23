from PyQt5.QtWidgets import *
from MainDesign import *
from startupDialog import *
import socket, datetime

LOCALHOST = socket.gethostbyname(socket.gethostname())


class StartupDialog(QDialog):

    def __init__(self):

        super().__init__()
        self.StartUi = Ui_Form()
        self.StartUi.setupUi(self)

        ## Connections
        self.StartUi.SDStartButton.clicked.connect(self.StartButtonCMD)
        self.StartUi.SDHostEntry.textChanged.connect(self.updateVariables)
        self.StartUi.SDPortEntry.textChanged.connect(self.updateVariables)
        self.StartUi.SDPasswordEntry.textChanged.connect(self.updateVariables)
        self.StartUi.SDCancelButton.clicked.connect(self.cancelCMD)

        ## Variables
        self.HostIp = LOCALHOST
        self.Port = self.StartUi.SDPortEntry.text()
        self.Pass = self.StartUi.SDPasswordEntry.text()
        self.state = "DISCONNECTED"
    
    def StartButtonCMD(self):

        self.state = "CONNECT"
        print(f"IP == {self.HostIp}\nPort == {self.Port}\nPassword == {self.Pass}\nState == {self.state}")
        self.hide()
    
    def updateVariables(self):

        if self.StartUi.SDHostEntry.text() == "localhost":
            self.HostIp = LOCALHOST
        elif self.StartUi.SDHostEntry.text().replace(".", "").isnumeric():
            self.HostIp = self.StartUi.SDHostEntry.text()
        else:
            self.HostIp = LOCALHOST
        
        self.Port = self.StartUi.SDPortEntry.text()
        self.Pass = self.StartUi.SDPasswordEntry.text()

        return (self.state, self.HostIp, self.Port, self.Pass)

    def cancelCMD(self):
        self.hide()
        


class MainApplication(QMainWindow):

    def __init__(self):

        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # variables
        local_ip = socket.gethostbyname(socket.gethostname()) 

        # Start Up Setup
        startDialog = StartupDialog()
        self.serverState, self.serverHost, self.serverPort, self.serverPass = startDialog.updateVariables()
        QtCore.QTimer.singleShot(100, lambda: startDialog.exec())
        self.consoleLog(logGood="Welcome To the Party Part one")
        self.initializeServer()
        

    def initializeServer(self):

        if self.serverState == "CONNECT":
            self.consoleLog(logGood=f"Server Started At {self.serverHost}")
        else:
            self.consoleLog(logCritical=f"Server Not Connected!")

    def Connect(self):

        print("Main connect")
    
    def consoleLog(self, log="", logWarning="", logCritical="", logGood=""):
        ui = self.ui

        if logWarning != "":
            html = f"""<html><head/><body><p><span style=" font-size:9pt; color:#0055ff;">[{self.curTime}] [WARNING] >>> {logWarning} </span></p></body></html>"""
            ui.eventLogEdit.insertHtml(html)
            ui.eventLogEdit.insertPlainText("\n")
        elif logCritical != "":
            html = f"""<html><head/><body><p><span style=" font-size:9pt; color:#ff0000;">[{self.curTime}] [CRITICAL] >>> {logCritical} </span></p></body></html>"""
            ui.eventLogEdit.insertHtml(html)
            ui.eventLogEdit.insertPlainText("\n")
        elif logGood != "":
            html = f"""<html><head/><body><p><span style=" font-size:9pt; color:#00ff00;">[{self.curTime}] [INFO] >>> {logGood} </span></p></body></html>"""
            ui.eventLogEdit.insertHtml(html)
            ui.eventLogEdit.insertPlainText("\n")
        elif log != "":
            ui.eventLogEdit.insertPlainText(f"[{self.curTime}] >>> {log} \n")
    
    @property
    def curTime(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__":
    
    w = QApplication([])
    app = MainApplication()
    app.show()
    w.exec_()