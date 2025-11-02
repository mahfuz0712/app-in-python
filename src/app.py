

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt


def main() -> int:
	app = QApplication(sys.argv)

	window = QWidget()
	window.setWindowTitle("Hello World")
	window.resize(400, 200)

	label = QLabel("Hello, World!")
	label.setAlignment(Qt.AlignmentFlag.AlignCenter)

	layout = QVBoxLayout()
	layout.addWidget(label)
	window.setLayout(layout)

	# Center the window on the primary screen
	frame_geo = window.frameGeometry()
	screen_center = QDesktopWidget().availableGeometry().center()
	frame_geo.moveCenter(screen_center)
	window.move(frame_geo.topLeft())

	window.show()
	return app.exec_()


if __name__ == "__main__":
	raise SystemExit(main())