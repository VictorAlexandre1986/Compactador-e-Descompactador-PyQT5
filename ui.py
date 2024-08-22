from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QListWidget)

class CompressorUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Compressor')
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()

        self.file_list = QListWidget()
        layout.addWidget(self.file_list)
        
        self.select_button = QPushButton('Selecionar Arquivos')
        self.select_button.clicked.connect(self.select_files)
        layout.addWidget(self.select_button)
        
        self.compress_button = QPushButton('Compactar')
        self.compress_button.clicked.connect(self.compress_files)
        layout.addWidget(self.compress_button)
        
        self.decompress_button = QPushButton('Descompactar')
        self.decompress_button.clicked.connect(self.decompress_file)
        layout.addWidget(self.decompress_button)
        
        self.setLayout(layout)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, 'Selecionar Arquivos')
        if files:
            self.file_list.addItems(files)

    def compress_files(self):
        files = [self.file_list.item(i).text() for i in range(self.file_list.count())]
        if files:
            output_zip, _ = QFileDialog.getSaveFileName(self, 'Salvar Arquivo Zip', '', 'Zip Files (*.zip)')
            if output_zip:
                from compressor import compress_files
                compress_files(files, output_zip)

    def decompress_file(self):
        zip_file, _ = QFileDialog.getOpenFileName(self, 'Selecionar Arquivo Zip', '', 'Zip Files (*.zip)')
        if zip_file:
            output_dir = QFileDialog.getExistingDirectory(self, 'Selecionar Diretório de Extração')
            if output_dir:
                from compressor import decompress_file
                decompress_file(zip_file, output_dir)
