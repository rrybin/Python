import os
import tkinter
import random

IMG_DIR = 'nums'
FIELD_SIZE = 4

files_names = os.listdir(IMG_DIR)

files_path = []

for file_name in files_names:
    files_path.append(os.path.join(IMG_DIR, file_name))

main_window = tkinter.Tk()
main_window.title('Игра 15')

images = []

for file_path in files_path:
    images.append(tkinter.PhotoImage(file=file_path))

labels = []
    
for row in range(FIELD_SIZE):
    _tmp_row = []
    for col in range(FIELD_SIZE):
        _x = row * FIELD_SIZE + col
        _label = tkinter.Label(main_window, image=images[_x])
        _label.grid(row=row, column=col)
        _label.x = _x
        _label.row = row
        _label.col = col
        _tmp_row.append(_label)
    labels.append(_tmp_row)

cur = labels[-1][-1]


def exchange_items(near):
    near.row, cur.row = cur.row, near.row
    near.col, cur.col = cur.col, near.col
    labels[near.row][near.col], labels[cur.row][cur.col] = \
        labels[cur.row][cur.col], labels[near.row][near.col]


def render_item(arg):
    arg.grid(row=arg.row, column=arg.col)


def check_win():
    check = True
    for _row in range(FIELD_SIZE):
        for _col in range(FIELD_SIZE):
            if labels[_row][_col].x != labels[_row][_col].row * FIELD_SIZE + labels[_row][_col].col:
                check = False
    if check:
        print('Вы выиграли')


def key_press(arg):
    near = None
    if arg == 'Up' and cur.row > 0:
        near = labels[cur.row - 1][cur.col]
    elif arg == 'Down' and cur.row < FIELD_SIZE - 1:
        near = labels[cur.row + 1][cur.col]
    elif arg == 'Left' and cur.col > 0:
        near = labels[cur.row][cur.col - 1]
    elif arg == 'Right' and cur.col < FIELD_SIZE - 1:
        near = labels[cur.row][cur.col + 1]
    if near:
        exchange_items(near)
        render_item(cur)
        render_item(near)
        check_win()


def shuffle_game():
    action = ['Up', 'Down', 'Left', 'Right']
    for _ in range(10):
        current_action = random.sample(action, 1)[0]
        key_press(current_action)


main_window.bind('<KeyPress>', lambda arg: key_press(arg.keysym))

main_window.after(2000, shuffle_game)

main_window.mainloop()
