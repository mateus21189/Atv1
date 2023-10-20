from inserirFull import inserir
from PySide6 import QtWidgets




class telaPrincipal(QtWidgets.QWidget):
    def __init__ (self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("untitled.ui")
        self.componen