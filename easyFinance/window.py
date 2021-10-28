# підключення внутрішніх бібліотек
from libs import *

# кольори
background_color = "#E3E2DE"
main_color = "#E5E4E1"
active_color = "#F2F1ED"
white_color = "#ffffff"

# створення вікна та загальні налаштування
root = Tk()
root.title("easyFinance")
root.iconbitmap("icons/program.ico")
root.wm_geometry("1520x780+0+0")  # розмір = ширина х висота + початкова_точка_х + початкова_точка_у //583x683
root.configure(bg=background_color)
root.minsize(583, 600)

# іконки для панелі управління (sizex32)
icon0 = PhotoImage(file=r"icons\program.png")
icon1 = PhotoImage(file=r"icons\task_icon.png")
icon2 = PhotoImage(file=r"icons\task.png")
icon3 = PhotoImage(file=r"icons\task1.png")
