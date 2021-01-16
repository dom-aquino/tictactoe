import pygame
import re
import tkinter
import tkinter.messagebox

class GameBoard():
    def __init__(self):
        LENGTH = 450
        WIDTH = 505
        self.screen = pygame.display.set_mode([LENGTH, WIDTH])
        self.screen.fill((255, 255, 255))
        self.current_turn = 'X'
        self.board_mapping = "123456789"

        # Game board
        game_board = pygame.image.load("img/tictactoe_board.png")
        game_board = pygame.transform.scale(game_board, [400, 400])
        self.screen.blit(game_board, (25, 85))

        # Reset button
        reset_button = pygame.image.load("img/reset_button.png")
        reset_button = pygame.transform.scale(reset_button, [150, 70])
        self.screen.blit(reset_button, (150, 10))

        # Markers
        self.x_img = pygame.image.load("img/x_mark.png")
        self.x_img = pygame.transform.scale(self.x_img, (100, 100))
        self.x_img.set_colorkey(1)
        self.o_img = pygame.image.load("img/o_mark.png")
        self.o_img = pygame.transform.scale(self.o_img, (100, 100))
        self.o_img.set_colorkey(1)

        pygame.display.set_caption('TIC-TAC-TOE')
        pygame.display.flip()
        pygame.display.update()

    def update_board(self, x_position, y_position):
        print('current turn: ', self.current_turn)
        if self.current_turn == "X":
            image_to_display = self.x_img
            self.current_turn = "0"
        else:
            image_to_display = self.o_img
            self.current_turn = "X"
        self.screen.blit(image_to_display, (x_position, y_position))
        pygame.display.update()

    def reset(self):
        self.__init__()

# for point in range(0, 501, 50):
#     pygame.draw.line(screen, (0, 255, 255), (point, 0), (point, 500))

# for point in range(0, 501, 50):
#     pygame.draw.line(screen, (0, 255, 255), (0, point), (500, point))

def get_column_and_row_of_the_click(x_coordinate, y_coordinate):

    if x_coordinate in range(30, 163):
        column = 1
    elif x_coordinate in range(169, 282):
        column = 2
    elif x_coordinate in range(288, 414):
        column = 3
    else:
        column = None

    if y_coordinate in range(96, 224):
        row = 1
    elif y_coordinate in range(231, 340):
        row = 2
    elif y_coordinate in range(349, 474):
        row = 3
    else:
        row = None

    return column, row

def get_cell_number(column, row):

    if column == 1:
        if row == 1:
            cell_number = 1
        elif row == 2:
            cell_number = 4
        else:
            cell_number = 7
    elif column == 2:
        if row == 1:
            cell_number = 2
        elif row == 2:
            cell_number = 5
        else:
            cell_number = 8
    elif column == 3:
        if row == 1:
            cell_number = 3
        elif row == 2:
            cell_number = 6
        else:
            cell_number = 9
    else:
        cell_number = None

    return cell_number

def is_the_move_valid(cell_number, board_mapping):
    return str(cell_number) in board_mapping

def get_position_where_to_put_the_mark(cell_num):
    if cell_num == 1:
        x_position = 49
        y_position = 108
    elif cell_num == 2:
        x_position = 178
        y_position = 108
    elif cell_num == 3:
        x_position = 308
        y_position = 108
    elif cell_num == 4:
        x_position = 40
        y_position = 240
    elif cell_num == 5:
        x_position = 176
        y_position = 238
    elif cell_num == 6:
        x_position = 300
        y_position = 237
    elif cell_num == 7:
        x_position = 41
        y_position = 360
    elif cell_num == 8:
        x_position = 177
        y_position = 360
    elif cell_num == 9:
        x_position = 302
        y_position = 367
    else:
        x_position = None
        y_position = None

    return x_position, y_position

def is_there_a_winner(board_state):
    winning_patterns = ["^XXX", "XXX$", "X..X..X..", ".X..X..X.",
                        "..X..X..X", "X...X...X", "..X.X.X..", "...XXX...",
                        "^OOO", "OOO$", "O..O..O..", ".O..O..O.",
                        "..O..O..O", "O...O...O", "..O.O.O..", "...OOO...",]
    is_there_a_match = False

    for pattern in winning_patterns:
        if re.search(pattern, board_state):
            is_there_a_match = True
            break

    return is_there_a_match

def main():
    pygame.init()

    game_board = GameBoard()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_coordinate, y_coordinate = pygame.mouse.get_pos()
                if x_coordinate in range(10, 90) and y_coordinate in range(10, 50):
                    pygame.quit()
                    exit()
                elif x_coordinate in range(159, 292) and y_coordinate in range(17, 69):
                    game_board.reset()
                    continue
                column, row = get_column_and_row_of_the_click(x_coordinate, y_coordinate)
                cell_number = get_cell_number(column, row)
                if is_the_move_valid(cell_number, game_board.board_mapping):
                    x_position, y_position = get_position_where_to_put_the_mark(cell_number)
                    game_board.update_board(x_position, y_position)
                    game_board.board_mapping = game_board.board_mapping.replace(str(cell_number), game_board.current_turn)
                    if is_there_a_winner(game_board.board_mapping):
                        tkinter.messagebox.showinfo("We have a winner!", "OK")
                        break
                    if not re.search('[0-9]', game_board.board_mapping):
                        tkinter.messagebox.showinfo("We have a draw!", "OK")
                        break
                # print("x_coordinate: ", x_coordinate)
                # print("y_coordinate: ", y_coordinate)
                # print('column: ', column)
                # print('row: ', row)
                # print('cell: ', cell_number)

if __name__ == "__main__":
    main()
