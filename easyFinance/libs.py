# підключення необхідних для роботи бібліотек
import os
import glob
import json
import subprocess
from datetime import date
from pprint import pprint
from numpy import *
from math import fabs

# підключення бібліотек для створення віконної програми
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu
from tkinter import Frame
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# для побудови графіків всередині програми
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# для оновлень
import webbrowser

# для підказок при наведенні на кнопки чи компоненти ГТН
from idlelib.tooltip import Hovertip

# для можливості обирати дати з календаря
from tkcalendar import Calendar 
def clear_frame(frame):
   for x in frame.winfo_children():
      x.destroy()
