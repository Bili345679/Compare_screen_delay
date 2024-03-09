import sys, os, time, json
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer


def format_ms_progress(n):
    result = []
    for i in range(10):
        row = []
        for j in range(10):
            if n > 0:
                row.append(f"{j} {'#' * min(10, n)}{'.' * max(0, 10 - n)}")
                n -= 10
            else:
                row.append(f"{j} {'.' * 10}")
        row.append("10")
        result.append(" ".join(row))
    return "\n".join(result)


class MainWindow(QMainWindow):
    def __init__(
        self, screen, windows, show_progress=True, time_size=200, progress_size=15, **kwargs
    ):
        super(MainWindow, self).__init__()
        self.screen = screen
        self.windows = windows
        self.time_size = time_size
        self.progress_size = progress_size
        self.show_progress = show_progress
        print(time_size)
        print(progress_size)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.time = QLabel(self)
        font = QFont()
        font.setPointSize(self.time_size)
        self.time.setFont(font)
        self.layout.addWidget(self.time)

        if self.show_progress:
            self.progress = QLabel(self)
            font = QFont()
            font.setPointSize(self.progress_size)
            self.progress.setFont(font)
            self.layout.addWidget(self.progress)

        self.layout.addStretch(1)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)

        self.setCentralWidget(self.central_widget)

        self.update_timer()

        rect = self.screen.geometry()
        self.setGeometry(rect)

        self.showMaximized()

    def update_timer(self):
        value = str(time.perf_counter())
        value = value[value.index(".") - 1 :]

        if self.show_progress:
            ms_num = int(value[2:5])
            self.progress.setText(format_ms_progress(ms_num))
            self.progress.adjustSize()

        self.time.setText(value)
        self.time.adjustSize()

        QTimer.singleShot(1, self.update_timer)

    def closeEvent(self, event):
        for window in self.windows:
            window.close()


def main():
    config = {}
    if os.path.exists("./config.json"):
        with open("./config.json", "r") as file:
            config = json.load(file)
            print(config)

    app = QApplication(sys.argv)

    windows = []
    for screen in app.screens():
        win = MainWindow(screen, windows, **config)
        windows.append(win)
        win.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
