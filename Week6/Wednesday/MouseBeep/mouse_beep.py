import pyautogui


def get_coord():
    a, b = pyautogui.position().x, pyautogui.position().y
    yield (a, b)


def mouse_beep():
    while True:
        if next(get_coord()) == (0, 0):
            print('\a', end = "")
