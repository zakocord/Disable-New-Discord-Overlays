import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QFileDialog, QMessageBox, QTextEdit, QHBoxLayout
)
import sys
import os

version = "1.0.0"
installer = "1.0"

class OverlayModifier(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fuckin Discord Overlay | v1.0 | github.com/Zakocord")
        self.setGeometry(100, 100, 600, 400)

        # Layout setup
        layout = QVBoxLayout()

        # Log display area
        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setFixedHeight(150)  
        layout.addWidget(self.log_box)

        self.patch_button = QPushButton("Patch")
        self.patch_button.setStyleSheet("background-color: purple; color: white; font-size: 18px; padding: 10px;")
        self.patch_button.clicked.connect(self.search_and_modify)
        self.patch_button.clicked.connect(self.restart)
        layout.addWidget(self.patch_button)

        self.setLayout(layout)

    def search_and_modify(self):
        user_name = os.environ.get("USERNAME") or os.environ.get("USER")
        if not user_name:
            self.log_box.append("Unable to retrieve username")
            return
        
        base_path = f"C:\\Users\\{user_name}\\AppData\\Local\\Discord"
        if not os.path.exists(base_path):
            self.log_box.append("Discord base folder not found")
            return

        found = False
        for folder in os.listdir(base_path):
            if folder.startswith("app-"):
                target_path = os.path.join(base_path, folder, "modules", "discord_desktop_overlay-1", "discord_desktop_overlay", "index.js")
                if os.path.isfile(target_path):
                    self.log_box.append(f"index.js Found: {target_path}")
                    self.modify_index_js(target_path)
                    found = True
                    break

        if not found:
            self.log_box.append("index.js Not Found")

    def modify_index_js(self, path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"""
console.log("injected E-Cord")
   console.log(`
███████╗     ██████╗ ██████╗ ██████╗ ██████╗ 
██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗
█████╗█████╗██║     ██║   ██║██████╔╝██║  ██║
██╔══╝╚════╝██║     ██║   ██║██╔══██╗██║  ██║
███████╗    ╚██████╗╚██████╔╝██║  ██║██████╔╝
╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
   `);

console.log ("Disabled | New Game Overlay")
console.warn("Made By Zakocord");
console.warn("v{version} | github/Zakocord")
console.warn("Installer Version: {installer}")

""")
            QMessageBox.information(self, "Success", "index.js has been Injected")
            self.log_box.append(f"[+] Modification successful: {path}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            self.log_box.append(f"[!] Injection failed: {str(e)}")

    def restart(self):
        os.system("taskkill /F /IM Discord.exe")
        self.log_box.append("Killed Discord.exe")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OverlayModifier()
    window.show()
    sys.exit(app.exec_())
