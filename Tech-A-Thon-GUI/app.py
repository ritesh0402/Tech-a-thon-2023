import sys
from PIL import *

# 1. Import QApplication and all the required widgets
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# 2. Create an instance of QApplication
app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(0, 0, 500, 500)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)


# 4. Show your application's GUI
window.show()

# 5. Run your application's event loop
sys.exit(app.exec())
