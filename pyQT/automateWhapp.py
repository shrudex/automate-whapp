import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QTextEdit, QFileDialog
import openpyxl
import pyautogui as pt
import pyperclip
import webbrowser

class AutomateWhapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AutomateWhapp")
        self.setGeometry(100, 100, 800, 600)
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.file_label = QLabel("Select Excel File:")
        self.layout.addWidget(self.file_label)

        self.file_entry = QTextEdit()
        self.layout.addWidget(self.file_entry)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)
        self.layout.addWidget(self.browse_button)

        self.message_label = QLabel("WhatsApp Message:")
        self.layout.addWidget(self.message_label)

        self.message_entry = QTextEdit()
        self.layout.addWidget(self.message_entry)

        self.send_button = QPushButton("Send BULK messages!")
        self.send_button.clicked.connect(self.send_messages)
        self.layout.addWidget(self.send_button)

        self.success_label = QLabel()
        self.layout.addWidget(self.success_label)

    def browse_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Excel File", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
        if file_path:
            self.file_entry.setPlainText(file_path)

    def send_messages(self):
        file_path = self.file_entry.toPlainText()
        message = self.message_entry.toPlainText()

        # Process the uploaded file and send messages
        workbook = openpyxl.load_workbook(file_path)
        worksheet = workbook.active
        webbrowser.open("https://github.com/shrudex")
        data = []

        for row in worksheet.iter_rows(min_row=2, values_only=True):
            name, number, date, time = map(str, row)
            if name and number and date and time and name.lower() != "name":
                formatted_number = "+91" + str(number)
                data.append([name, formatted_number, date, time])

        screenWidth, screenHeight = pt.size()
        pt.sleep(3)

        for name, number, date, time in data:
            if name and date and time:
                formatted_message = message.replace("NAME", name).replace("DATE", date).replace("TIME", time)

                waLink = "https://web.whatsapp.com/send?phone=" + str(number)
                waLink = waLink.lower()
                pyperclip.copy(formatted_message)

                webbrowser.open(waLink)
                pt.sleep(15)
                pt.click(x=(screenWidth * 3) // 4, y=(screenHeight * 9) // 10)

                pt.hotkey('ctrl', 'v')
                pt.sleep(1)
                pt.press("enter")
                pt.sleep(3)
                pt.hotkey("ctrl", "w")

        pt.hotkey("ctrl", "w")
        self.success_label.setText('Messages sent successfully.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutomateWhapp()
    window.showFullScreen()  # Show the application in full screen
    sys.exit(app.exec_())
