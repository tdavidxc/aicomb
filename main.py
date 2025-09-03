#entry point for the application
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QPushButton,
    QLabel, QTextEdit, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor #for designing and colouring

class ChatBubble(QFrame):
    """Custom message bubble widget."""
    def __init__(self, text, role="assistant"):
        super().__init__()

        self.setStyleSheet("""
            QFrame {
                border-radius: 12px;
                padding: 8px;
                font-size: 14px;
            }
        """)

        label = QLabel(text)
        label.setWordWrap(True)

        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

        # Different colors based on role
        if role == "user":
            self.setStyleSheet("""
                QFrame {
                    background-color: #2d89ef;  /* blue */
                    color: white;
                    border-radius: 12px;
                    padding: 8px;
                    font-size: 14px;
                }
            """)
        else:  # assistant
            self.setStyleSheet("""
                QFrame {
                    background-color: #3a3a3a;  /* dark gray */
                    color: #f0f0f0;
                    border-radius: 12px;
                    padding: 8px;
                    font-size: 14px;
                }
            """)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("aicomb")
        self.setGeometry(200, 100, 1200, 700)

        # === Central Widget ===
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # === Root Layout (3 columns) ===
        root_layout = QHBoxLayout(central_widget)

        # -------------------------
        # Sidebar 1 (LLMs)
        # -------------------------
        sidebar1 = QVBoxLayout()
        sidebar1.setAlignment(Qt.AlignTop)

        sidebar1.addWidget(QPushButton("🤖⚙"))  # GPT
        sidebar1.addWidget(QPushButton("🌐⚙"))  # Gemini
        sidebar1.addWidget(QPushButton("🐦⚙"))  # Grok
        sidebar1.addWidget(QPushButton("🔍⚙"))  # DeepSeek
        sidebar1.addWidget(QPushButton("🧠⚙"))  # Claude

        sidebar1_widget = QWidget()
        sidebar1_widget.setLayout(sidebar1)
        sidebar1_widget.setFixedWidth(80)
        root_layout.addWidget(sidebar1_widget)

        # -------------------------
        # Sidebar 2 (Chats)
        # -------------------------
        sidebar2 = QVBoxLayout()
        sidebar2.setAlignment(Qt.AlignTop)

        sidebar2.addWidget(QPushButton("+ New Chat"))
        sidebar2.addWidget(QPushButton("Chat 1"))
        sidebar2.addWidget(QPushButton("Chat 2"))
        sidebar2.addWidget(QPushButton("Research"))
        sidebar2.addWidget(QPushButton("Drafts"))

        sidebar2_widget = QWidget()
        sidebar2_widget.setLayout(sidebar2)
        sidebar2_widget.setFixedWidth(150)
        root_layout.addWidget(sidebar2_widget)

        # -------------------------
        # Main Area
        # -------------------------
        main_area = QVBoxLayout()

        # Header
        header = QLabel("GPT-4")
        header.setStyleSheet("font-size: 20px; font-weight: bold; padding: 10px;")
        main_area.addWidget(header)

        # Scrollable Chat Display
        chat_scroll = QScrollArea()
        chat_scroll.setWidgetResizable(True)
        self.chat_container = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.chat_container.setLayout(self.chat_layout)
        chat_scroll.setWidget(self.chat_container)
        main_area.addWidget(chat_scroll)

        # Add some example bubbles
        self.chat_layout.addWidget(ChatBubble("Hello, how can I help?", role="assistant"))
        self.chat_layout.addWidget(ChatBubble("Summarise this document", role="user"))
        self.chat_layout.addWidget(ChatBubble("Sure, here’s a summary...", role="assistant"))

        # Input Bar
        input_bar = QHBoxLayout()
        input_box = QTextEdit()
        input_box.setFixedHeight(50)
        send_button = QPushButton("Send ▶")
        input_bar.addWidget(input_box)
        input_bar.addWidget(send_button)
        main_area.addLayout(input_bar)

        main_widget = QWidget()
        main_widget.setLayout(main_area)
        root_layout.addWidget(main_widget)



#passing in the system argument into the application
def main():
    app = QApplication(sys.argv)

    #dark theme pallete
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(30, 30, 30))
    palette.setColor(QPalette.Base, QColor(45, 45, 45))
    palette.setColor(QPalette.Text, QColor(220, 220, 220))
    palette.setColor(QPalette.Button, QColor(60, 60, 60))
    palette.setColor(QPalette.ButtonText, QColor(220, 220, 220))
    app.setPalette(palette)
    #setting the global default stylesheet for qpushbutton to allow texts to be seen
    app.setStyleSheet("""
    QPushButton {
        background-color: #3c3c3c;
        color: #f0f0f0;
        border: 1px solid #5a5a5a;
        border-radius: 6px;
        padding: 6px 10px;
    }
    QPushButton:hover {
        background-color: #505050;
    }
    QPushButton:pressed {
        background-color: #2d2d2d;
    }
    QPushButton:disabled {
        background-color: #2a2a2a;
        color: #777777;
        border: 1px solid #444444;
    }
""")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

