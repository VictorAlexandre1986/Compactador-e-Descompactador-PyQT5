import sys
from PyQt5.QtWidgets import QApplication
from ui import CompressorUI

def main():
    app = QApplication(sys.argv)
    window = CompressorUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
