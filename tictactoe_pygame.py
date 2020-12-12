import pygame
import re

pygame.init()
LENGTH = 800
WIDTH = 640
screen = pygame.display.set_mode([LENGTH, WIDTH])
screen.fill((255, 255, 255))
game_board = pygame.image.load("img/tictactoe_board.jpg")
game_board = pygame.transform.scale(game_board, [LENGTH, WIDTH])
screen.blit(game_board, (0, 0))
pygame.display.update()

x_img = pygame.image.load("img/x_mark.png")
x_img = pygame.transform.scale(x_img, (100, 100))
x_img.set_colorkey(1)
o_img = pygame.image.load("img/o_mark.png")
o_img = pygame.transform.scale(o_img, (100, 100))
o_img.set_colorkey(1)

def get_column_and_row_position_of_the_click():
    x_coordinate, y_coordinate = pygame.mouse.get_pos()

    print("x_coordinate: ", x_coordinate)
    print("y_coordinate: ", y_coordinate)

    if x_coordinate in range(160, 290):
        column = 1
    elif x_coordinate in range(320, 470):
        column = 2
    elif x_coordinate in range(502, 620):
        column = 3
    else:
        column = None

    if y_coordinate in range(50, 200):
        row = 1
    elif y_coordinate in range(221, 392):
        row = 2
    elif y_coordinate in range(415, 590):
        row = 3
    else:
        row = None

    return column, row

def get_cell_number_in_the_board(column, row):
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

def get_position_where_to_put_the_mark(cell_num):
    if cell_num == 1:
        x_position = 180
        y_position = 80
    elif cell_num == 2:
        x_position = 350
        y_position = 80
    elif cell_num == 3:
        x_position = 520
        y_position = 80
    elif cell_num == 4:
        x_position = 180
        y_position = 260
    elif cell_num == 5:
        x_position = 350
        y_position = 260
    elif cell_num == 6:
        x_position = 520
        y_position = 260
    elif cell_num == 7:
        x_position = 180
        y_position = 450
    elif cell_num == 8:
        x_position = 350
        y_position = 450
    elif cell_num == 9:
        x_position = 520
        y_position = 450
    else:
        x_position = None
        y_position = None

    return x_position, y_position

def is_the_move_valid(cell_number, board_mapping):
    return str(cell_number) in board_mapping

def update_board(current_turn, x_position, y_position):
    if current_turn == "X":
        image_to_display = x_img
        current_turn.replace("X", "O")
    else:
        image_to_display = o_img
        current_turn.replace("O", "X")
    screen.blit(image_to_display, (x_position, y_position))
    pygame.display.update()

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

    GAME_IS_ONGOING = True
    current_turn = 'X'
    board_mapping = "123456789"

    while GAME_IS_ONGOING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_IS_ONGOING = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                column, row = get_column_and_row_position_of_the_click()
                print("Column: ", column)
                print("Row: ", row)
                cell_number = get_cell_number_in_the_board(column, row)
                if is_the_move_valid(cell_number, board_mapping):
                    x_pos, y_pos = get_position_where_to_put_the_mark(cell_number)
                    update_board(current_turn, x_pos, y_pos)
                    board_mapping = board_mapping.replace(str(cell_number), current_turn)
                    print('board_mapping: ', board_mapping)
                    if is_there_a_winner(board_mapping):
                        print("We have a winner!!!")
                        break
                    if not re.search('[0-9]', board_mapping):
                        print("We have a draw!!!")
                        break
                    current_turn = 'O' if current_turn == 'X' else 'X'

if __name__ == "__main__":
    main()
