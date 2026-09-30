import sys
from pathlib import Path

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget


def load_ui(ui_file_path):
    ui_file = QFile(str(ui_file_path))
    ui_file.open(QFile.ReadOnly)
    
    loader = QUiLoader()
    window = loader.load(ui_file)
    
    ui_file.close()
    
    return window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        project_path = Path(__file__).parent
        
        login_path = project_path / "ui" / "login.ui"
        products_path = project_path / "ui" / "products.ui"
        
        self.login_window = load_ui(login_path)
        self.products_window = load_ui(products_path)
        
        self.stack.addWidget(self.login_window)
        self.stack.addWidget(self.products_window)
        
        self.stack.setCurrentWidget(self.login_window)

def main():
    app =  QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
        
    
    