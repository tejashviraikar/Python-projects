# Create a simple drawing application with basic shapes and colors.

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QColorDialog, QFileDialog, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QPainter, QPen, QImage
from PyQt5.QtCore import Qt, QPoint

class DrawingApp(QMainWindow):
    """Class to create a simple drawing application with PyQt5."""

    def __init__(self):
        """Initialize the DrawingApp with a PyQt5 main window."""
        super().__init__()
        self.setWindowTitle("Basic Drawing App")
        self.setGeometry(100, 100, 600, 400)
        
        # Initialize drawing settings
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_color = Qt.black
        self.brush_size = 2
        self.last_point = QPoint()

        # Set up the main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Canvas area: the space above buttons
        self.canvas = QWidget(self)
        main_layout.addWidget(self.canvas)  # Add canvas to the main layout

        # Add horizontal layout for buttons at the bottom
        button_layout = QHBoxLayout()
        main_layout.addLayout(button_layout)

        # Add buttons for tools
        pencil_btn = QPushButton("Pencil", self)
        pencil_btn.clicked.connect(self.select_pencil)
        button_layout.addWidget(pencil_btn)

        rect_btn = QPushButton("Rectangle", self)
        rect_btn.clicked.connect(self.select_rectangle)
        button_layout.addWidget(rect_btn)

        color_btn = QPushButton("Color", self)
        color_btn.clicked.connect(self.select_color)
        button_layout.addWidget(color_btn)

        save_btn = QPushButton("Save", self)
        save_btn.clicked.connect(self.save_image)
        button_layout.addWidget(save_btn)

    def select_pencil(self):
        """Select the pencil tool for drawing."""
        self.tool = 'pencil'

    def select_rectangle(self):
        """Select the rectangle tool for drawing."""
        self.tool = 'rectangle'

    def select_color(self):
        """Open a color dialog to choose the drawing color."""
        color = QColorDialog.getColor()
        if color.isValid():
            self.brush_color = color

    def save_image(self):
        """Save the drawn image to a file."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if file_path:
            self.image.save(file_path)

    def mousePressEvent(self, event):
        """Handle mouse press events for drawing."""
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        """Handle mouse move events for drawing."""
        if event.buttons() & Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        """Handle mouse release events to stop drawing."""
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        """Update the canvas to display the drawn elements."""
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

# Run the PyQt5 application
app = QApplication([])
window = DrawingApp()
window.show()
app.exec_()  
