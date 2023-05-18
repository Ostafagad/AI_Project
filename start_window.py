from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QRadioButton, QPushButton


class ConnectFourWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Connect Four Game")
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("connect4.png"))

        # Create the level selection group box
        level_group_box = QGroupBox("Select Level")
        level_layout = QVBoxLayout()
        self.easy_radio = QRadioButton("Easy")
        self.medium_radio = QRadioButton("Medium")
        self.hard_radio = QRadioButton("Hard")
        level_layout.addWidget(self.easy_radio)
        level_layout.addWidget(self.medium_radio)
        level_layout.addWidget(self.hard_radio)
        level_group_box.setLayout(level_layout)

        # Create the algorithm selection group box
        algorithm_group_box = QGroupBox("Select Algorithm")
        algorithm_layout = QVBoxLayout()
        self.minimax_radio = QRadioButton("Minimax")
        self.alphabeta_radio = QRadioButton("Alpha-Beta")
        algorithm_layout.addWidget(self.minimax_radio)
        algorithm_layout.addWidget(self.alphabeta_radio)
        algorithm_group_box.setLayout(algorithm_layout)

        # Create the start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_game)

        # Create the exit button
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit_game)

        # Create the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(level_group_box)
        main_layout.addWidget(algorithm_group_box)
        main_layout.addWidget(self.start_button)
        main_layout.addWidget(self.exit_button)

        # Set the main layout for the window
        self.setLayout(main_layout)

        self.exit_flag = False  # Flag variable to control the while loop

    def start_game(self):
        if self.easy_radio.isChecked():
            selected_level = "Easy"
        elif self.medium_radio.isChecked():
            selected_level = "Medium"
        elif self.hard_radio.isChecked():
            selected_level = "Hard"
        else:
            selected_level = "Unknown"

        if self.minimax_radio.isChecked():
            selected_algorithm = "Minimax"
        elif self.alphabeta_radio.isChecked():
            selected_algorithm = "Alpha-Beta"
        else:
            selected_algorithm = "Unknown"

        # Close the window
        self.close()
        return selected_level, selected_algorithm

    def exit_game(self):
        self.exit_flag = True
        self.close()
