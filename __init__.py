import sys

from start_window import *
from game_logic import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConnectFourWindow()

    while not window.exit_flag:
        while True:
            window.show()
            app.exec_()
            level, algorithm = window.start_game()
            if level != "Unknown" and algorithm != "Unknown":
                print("Selected Level:", level)
                print("Selected Algorithm:", algorithm)
                break
            elif window.exit_flag:
                break
            else:
                print("Please choose the level and the algorithm to start")

        level, algorithm = window.start_game()
        if level == "Easy":
            depth = 1
        elif level == "Medium":
            depth = 3
        else:
            depth = 5

        if algorithm == "Minimax" and not window.exit_flag:
            minimax_game(depth)
        elif algorithm == "Alpha-Beta" and not window.exit_flag:
            alpha_bete_game(depth)

    sys.exit()
