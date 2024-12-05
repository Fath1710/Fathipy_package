import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton,QDialog,QDialogButtonBox, QFormLayout,QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from Fathipy import Rotation, StandardModelParticle, ThreeVector

class FathipyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        #ventana principal
        self.setWindowTitle("Fathipy - Interfaz Gráfica")
        self.setGeometry(200, 200, 600, 400)
        
        # Cambiar color de fondo a negro y texto a blanco
        self.setStyleSheet("background-color: black; color: white;")


        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Logo 
        logo_label = QLabel(self)
        pixmap = QPixmap("logo.jpg")  # Cambia esto al nombre del archivo de tu logo
        pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Escala el logo
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Mensaje de presentación
        welcome_label = QLabel("¡Bienvenid@ a Fathipy!")
        welcome_label.setFont(QFont("Arial", 16, QFont.Bold))
        welcome_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(welcome_label)
        
        # Botón 1: ThreeVector
        btn_threevector = QPushButton("Crear ThreeVector", self)
        btn_threevector.clicked.connect(self.open_threevector_dialog)
        layout.addWidget(btn_threevector)
        
        # Botón 2: Rotation
        btn_rotation = QPushButton("Crear Rotation", self)
        btn_rotation.clicked.connect(self.open_rotation_dialog)
        layout.addWidget(btn_rotation)

        # Botón 3: StandardModelParticle
        btn_smparticle = QPushButton("Crear StandardModelParticle", self)
        btn_smparticle.clicked.connect(self.open_smparticle_dialog)
        layout.addWidget(btn_smparticle)

        # Resultado
        self.result_label = QLabel("", self)
        self.result_label.setFont(QFont("Arial", 12))
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        # Descripción del proyecto
        description_label = QLabel(
            "Fathipy es una paquetería Python para la representación y manipulación de vectores,\n"
            "partículas del modelo estándar y operaciones físicas."
        )
        description_label.setFont(QFont("Arial", 12))
        description_label.setAlignment(Qt.AlignCenter)
        description_label.setWordWrap(True)
        layout.addWidget(description_label)

        # Configuración del diseño
        central_widget.setLayout(layout)
        
    def open_threevector_dialog(self):
        dialog = InputDialog("ThreeVector", ["x", "y", "z"], self)
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()
            vector = ThreeVector(float(values["x"]), float(values["y"]), float(values["z"]))
            self.result_label.setText(f"ThreeVector creado: x={vector.vector[0]}, y={vector.vector[1]}, z={vector.vector[2]}")

    def open_rotation_dialog(self):
        dialog = InputDialog("Rotation", ["Ángulo (rad)", "Eje X", "Eje Y", "Eje Z"], self)
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()
            axis = ThreeVector(float(values["Eje X"]), float(values["Eje Y"]), float(values["Eje Z"]))
            rotation = Rotation(float(values["Ángulo (rad)"]), axis)
            self.result_label.setText(f"Matriz de rotación:\n{rotation.rotation_matrix}")

    def open_smparticle_dialog(self):
        dialog = InputDialog("StandardModelParticle", ["Nombre", "Símbolo", "Masa", "Carga", "Spin"], self)
        if dialog.exec_() == QDialog.Accepted:
            values = dialog.get_values()
            particle = StandardModelParticle(
                name=values["Nombre"],
                symbol=values["Símbolo"],
                mass=float(values["Masa"]),
                charge=float(values["Carga"]),
                spin=float(values["Spin"]),
                type_of_particle="fermion"
            )
            self.result_label.setText(particle.info())

class InputDialog(QDialog):
    def __init__(self, title, fields, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.layout = QFormLayout(self)
        self.inputs = {}

        # Crear campos de entrada
        for field in fields:
            line_edit = QLineEdit(self)
            self.inputs[field] = line_edit
            self.layout.addRow(field, line_edit)

        # Botones de aceptar y cancelar
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout.addWidget(buttons)

    def get_values(self):
        # Obtener valores de los campos de entrada
        return {field: self.inputs[field].text() for field in self.inputs}


def main():
    app = QApplication(sys.argv)
    main_window = FathipyApp()
    main_window.show()
    sys.exit(app.exec_())
