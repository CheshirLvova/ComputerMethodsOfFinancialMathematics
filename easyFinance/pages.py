# підключення сторінок
from window import *
from chapter2 import *
import SimpleInterestsLibrary as SIL
import SimpleInterestsFinanceParameters as SIFP
import ComplicatedInterestsFinanceParameters as CIFP
import time
import datetime
import calendar


def add_top_menu():
    windowTopMenu = Menu(root)
    root.config(menu=windowTopMenu)
    windowTopMenu.add_command(label='Довідка', command=information)
    windowTopMenu.add_command(label='Вихід', command=root.destroy)


def clear():
    try:
        root.winfo_children()[1].destroy()
    except:
        pass


def information():
    help_info = """Вас вітає фінансовий калькулятор easyFinance. 
      Дякуємо, що скористалися програмою!!!

      З метою полегшення використання програми, пропонуємо Вам 
      детальніше ознайомитись з можливими функціями для перегляду та використання:

      1. На наступній, головній сторінці Ви матимете змогу обрати 
         необхідний розділ для подальшої роботи.

      2. Ви завжди маєте змогу повернутись до цієї сторінки, 
         натиснувши відповідну кнопку вгорі програми.

      3. Перейшовши на головну сторінку, Вам буде відображено 
         меню та перелік існуючих розділів для роботи. 
      """
    clear()
    frame = Frame(root, bg=white_color)
    frame.place(anchor="n", relx=.5)
    frame.pack(expand=1, fill=BOTH)

    nb1 = ttk.Notebook(frame)

    logo = ttk.Frame(nb1)
    nb1.add(logo, text='easyFinance', image=icon0)
    nb1.pack()

    label = Label(frame, text=help_info, bg=white_color)
    label.pack()
    btntomain = Button(frame, text="Продовжити", command=chapter_one_task_one_page)
    btntomain.pack()


def template(nb,fr=None):    # таби з розділами та переходами на кожну задачу
    # Add first tab
    tab1 = ttk.Frame(nb)
    tab2 = ttk.Frame(nb)
    tab3 = ttk.Frame(nb)
    tab4 = ttk.Frame(nb)
    tab7 = ttk.Frame(nb)

    # tab1.grid(row=0, column=0)
    nb.add(tab1, text='1.Прості відсотки')
    nb.add(tab2, text='2.Нарощення та дисконтування за складними відсотковими ставками')
    nb.add(tab3, text='3.Визначення інших параметрів угод із відсотковими ставками')
    nb.add(tab4, text='4.Неперервні відсотки. Неперервне нарощення та дисконтування')
    nb.add(tab7, text='7.Планування погашення заборгованості')


    # Change the sizes of the columns equally
    tab1.columnconfigure(0, minsize=70)
    tab1.columnconfigure(1, minsize=5)
    tab1.columnconfigure(2, minsize=70)
    tab1.columnconfigure(3, minsize=5)
    tab1.columnconfigure(4, minsize=70)
    tab1.columnconfigure(5, minsize=5)
    tab1.columnconfigure(6, minsize=70)
    tab1.columnconfigure(7, minsize=5)
    tab1.columnconfigure(8, minsize=70)
    tab1.columnconfigure(9, minsize=5)
    tab1.columnconfigure(10, minsize=70)
    tab1.columnconfigure(11, minsize=5)
    tab1.columnconfigure(12, minsize=70)
    tab1.columnconfigure(13, minsize=5)
    tab1.columnconfigure(14, minsize=70)
    tab1.columnconfigure(15, minsize=5)
    tab1.columnconfigure(16, minsize=70)
    tab1.columnconfigure(17, minsize=5)
    tab1.columnconfigure(18, minsize=525)

    tab2.columnconfigure(0, minsize=70)
    tab2.columnconfigure(1, minsize=5)
    tab2.columnconfigure(2, minsize=70)
    tab2.columnconfigure(3, minsize=5)
    tab2.columnconfigure(4, minsize=70)
    tab2.columnconfigure(5, minsize=5)
    tab2.columnconfigure(6, minsize=70)
    tab2.columnconfigure(7, minsize=5)
    tab2.columnconfigure(8, minsize=70)
    tab2.columnconfigure(9, minsize=5)
    tab2.columnconfigure(10, minsize=70)
    tab2.columnconfigure(11, minsize=5)
    tab2.columnconfigure(12, minsize=70)
    tab2.columnconfigure(13, minsize=5)
    tab2.columnconfigure(14, minsize=70)
    tab2.columnconfigure(15, minsize=5)
    tab2.columnconfigure(16, minsize=70)
    tab2.columnconfigure(17, minsize=5)
    tab2.columnconfigure(18, minsize=70)
    tab2.columnconfigure(19, minsize=5)
    tab2.columnconfigure(20, minsize=70)
    tab2.columnconfigure(21, minsize=5)
    tab2.columnconfigure(22, minsize=70)
    tab2.columnconfigure(23, minsize=5)
    tab2.columnconfigure(24, minsize=70)
    tab2.columnconfigure(25, minsize=5)
    tab2.columnconfigure(26, minsize=225)

    tab3.columnconfigure(0, minsize=70)
    tab3.columnconfigure(1, minsize=5)
    tab3.columnconfigure(2, minsize=70)
    tab3.columnconfigure(3, minsize=5)
    tab3.columnconfigure(4, minsize=70)
    tab3.columnconfigure(5, minsize=5)
    tab3.columnconfigure(6, minsize=70)
    tab3.columnconfigure(7, minsize=5)
    tab3.columnconfigure(8, minsize=70)
    tab3.columnconfigure(9, minsize=5)
    tab3.columnconfigure(10, minsize=70)
    tab3.columnconfigure(11, minsize=5)
    tab3.columnconfigure(12, minsize=70)
    tab3.columnconfigure(13, minsize=5)
    tab3.columnconfigure(14, minsize=70)
    tab3.columnconfigure(15, minsize=5)
    tab3.columnconfigure(16, minsize=70)
    tab3.columnconfigure(17, minsize=5)
    tab3.columnconfigure(18, minsize=70)
    tab3.columnconfigure(19, minsize=5)
    tab3.columnconfigure(20, minsize=70)
    tab3.columnconfigure(21, minsize=5)
    tab3.columnconfigure(22, minsize=70)
    tab3.columnconfigure(23, minsize=5)
    tab3.columnconfigure(24, minsize=70)
    tab3.columnconfigure(25, minsize=5)
    tab3.columnconfigure(26, minsize=70)
    tab3.columnconfigure(27, minsize=5)
    tab3.columnconfigure(28, minsize=70)
    tab3.columnconfigure(29, minsize=5)
    tab3.columnconfigure(30, minsize=70)
    tab3.columnconfigure(31, minsize=5)
    tab3.columnconfigure(32, minsize=0)

    tab4.columnconfigure(0, minsize=70)
    tab4.columnconfigure(1, minsize=5)
    tab4.columnconfigure(2, minsize=70)
    tab4.columnconfigure(3, minsize=5)
    tab4.columnconfigure(4, minsize=70)
    tab4.columnconfigure(5, minsize=5)
    tab4.columnconfigure(6, minsize=70)
    tab4.columnconfigure(7, minsize=5)
    tab4.columnconfigure(8, minsize=70)
    tab4.columnconfigure(9, minsize=5)
    tab4.columnconfigure(10, minsize=70)
    tab4.columnconfigure(11, minsize=5)
    tab4.columnconfigure(12, minsize=70)
    tab4.columnconfigure(13, minsize=5)
    tab4.columnconfigure(14, minsize=70)
    tab4.columnconfigure(15, minsize=5)
    tab4.columnconfigure(16, minsize=600)

    # tab1
    bt1 = Button(tab1, text='Прості відсотки', image=icon1, compound=TOP, borderwidth=0, command=lambda:defaul_simple_rates(fr))
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=0, column=0, padx=5, pady=5)

    separator0 = ttk.Separator(tab1, orient='vertical')
    separator0.grid(column=1, row=0, sticky='ns')

    bt2 = Button(tab1, text='Змінні відсотки', image=icon1, compound=TOP, borderwidth=0, command=lambda:changing_simple_rates(fr))
    bthint2 = Hovertip(bt2, 'умова')
    bt2.grid(row=0, column=2, padx=5, pady=5)

    separator1 = ttk.Separator(tab1, orient='vertical')
    separator1.grid(column=3, row=0, sticky='ns')

    bt3 = Button(tab1, text='Реінвестування', image=icon1, compound=TOP, borderwidth=0, command=lambda:reinvestment_simple_rates(fr))
    bthint3 = Hovertip(bt3, 'умова')
    bt3.grid(row=0, column=4, padx=5, pady=1)

    separator2 = ttk.Separator(tab1, orient='vertical')
    separator2.grid(column=5, row=0, rowspan=2, sticky='ns')

    bt4 = Button(tab1, text='Змінна сума', image=icon1, compound=TOP, borderwidth=0, command=lambda:simple_rates_for_time_changing_sums(fr))
    bthint4 = Hovertip(bt4, 'умова')
    bt4.grid(row=0, column=6, padx=5, pady=1)

    separator3 = ttk.Separator(tab1, orient='vertical')
    separator3.grid(column=7, row=0, rowspan=2, sticky='ns')

    lbl1 = Label(tab1, text="1.1. Нарощення за простими відсотковими ставками").grid(row=1, column=0, columnspan=5,
                                                                                     padx=0, pady=1)

    bt5 = Button(tab1, text='Разова виплата', image=icon1, compound=TOP, borderwidth=0, command=lambda:single_time_payment(fr))
    bthint5 = Hovertip(bt5, 'умова')
    bt5.grid(row=0, column=8, padx=5, pady=1)

    separator4 = ttk.Separator(tab1, orient='vertical')
    separator4.grid(column=9, row=0, rowspan=2, sticky='ns')

    lbl2 = Label(tab1, text="1.2. Нарахування простих відсотків на змінні в часі суми депозиту").grid(row=1, column=6,
                                                                                                      padx=0,
                                                                                                      pady=1)

    lbl3 = Label(tab1, text="1.3. Нарахування відсотків у користувацькому кредиті").grid(row=1, column=8, padx=0,
                                                                                         pady=1)

    bt6 = Button(tab1, text='Дисконтована вартість', image=icon1, compound=TOP, borderwidth=0, command=lambda:discount_prise(fr))
    bthint6 = Hovertip(bt6, 'умова')
    bt6.grid(row=0, column=10, padx=5, pady=1)

    separator5 = ttk.Separator(tab1, orient='vertical')
    separator5.grid(column=11, row=0, sticky='ns')

    bt7 = Button(tab1, text='Дисконт', image=icon1, compound=TOP, borderwidth=0, command=lambda: discount(fr))
    bthint7 = Hovertip(bt7, 'умова')
    bt7.grid(row=0, column=12, padx=5, pady=5)

    separator6 = ttk.Separator(tab1, orient='vertical')
    separator6.grid(column=13, row=0, sticky='ns')

    bt8 = Button(tab1, text='Дисконтний множник', image=icon1, compound=TOP, borderwidth=0, command=lambda: bank_accounting_rate(fr))
    bthint8 = Hovertip(bt8, 'умова')
    bt8.grid(row=0, column=14, padx=5, pady=5)

    separator7 = ttk.Separator(tab1, orient='vertical')
    separator7.grid(column=15, row=0, sticky='ns')

    bt9 = Button(tab1, text='Облік векселів', image=icon1, compound=TOP, borderwidth=0, command=lambda:bank_accounting(fr))
    bthint9 = Hovertip(bt9, 'умова')
    bt9.grid(row=0, column=16, padx=5, pady=1)

    separator8 = ttk.Separator(tab1, orient='vertical')
    separator8.grid(column=17, row=0, rowspan=2, sticky='ns')

    lbl4 = Label(tab1, text="1.4. Дисконтування та облік за простими відсотковими ставками").grid(row=1, column=10,
                                                                                                  columnspan=7,
                                                                                                  padx=0, pady=1)

    # tab2
    bt1 = Button(tab2, text='Формула 1', image=icon1, compound=TOP, borderwidth=0, command=chapter_two_task_one_page)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=0, column=0, padx=5, pady=5)

    separator0 = ttk.Separator(tab2, orient='vertical')
    separator0.grid(column=1, row=0, sticky='ns')

    bt2 = Button(tab2, text='Формула 2', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint2 = Hovertip(bt2, 'умова')
    bt2.grid(row=0, column=2, padx=5, pady=5)

    separator1 = ttk.Separator(tab2, orient='vertical')
    separator1.grid(column=3, row=0, sticky='ns')

    bt3 = Button(tab2, text='Формула 3', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint3 = Hovertip(bt3, 'умова')
    bt3.grid(row=0, column=4, padx=5, pady=1)

    separator2 = ttk.Separator(tab2, orient='vertical')
    separator2.grid(column=5, row=0, sticky='ns')

    bt4 = Button(tab2, text='Формула 4', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint4 = Hovertip(bt4, 'умова')
    bt4.grid(row=0, column=6, padx=5, pady=1)

    separator3 = ttk.Separator(tab2, orient='vertical')
    separator3.grid(column=7, row=0, sticky='ns')

    bt5 = Button(tab2, text='Формула 5', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint5 = Hovertip(bt5, 'умова')
    bt5.grid(row=0, column=8, padx=5, pady=1)

    separator4 = ttk.Separator(tab2, orient='vertical')
    separator4.grid(column=9, row=0, sticky='ns')

    bt6 = Button(tab2, text='Формула 6', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint6 = Hovertip(bt6, 'умова')
    bt6.grid(row=0, column=10, padx=5, pady=1)

    separator5 = ttk.Separator(tab2, orient='vertical')
    separator5.grid(column=11, row=0, rowspan=2, sticky='ns')

    lbl1 = Label(tab2, text="2.1. Нарахування відсотків у користувацькому кредиті").grid(row=1, column=0, columnspan=11,
                                                                                         padx=0, pady=1)

    bt7 = Button(tab2, text='Формула 7', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint7 = Hovertip(bt7, 'умова')
    bt7.grid(row=0, column=12, padx=5, pady=5)

    separator6 = ttk.Separator(tab2, orient='vertical')
    separator6.grid(column=13, row=0, sticky='ns')

    bt8 = Button(tab2, text='Формула 8', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint8 = Hovertip(bt8, 'умова')
    bt8.grid(row=0, column=14, padx=5, pady=5)

    separator7 = ttk.Separator(tab2, orient='vertical')
    separator7.grid(column=15, row=0, sticky='ns')

    bt9 = Button(tab2, text='Формула 9', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint9 = Hovertip(bt9, 'умова')
    bt9.grid(row=0, column=16, padx=5, pady=1)

    separator8 = ttk.Separator(tab2, orient='vertical')
    separator8.grid(column=17, row=0, sticky='ns')

    bt10 = Button(tab2, text='Формула 10', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint10 = Hovertip(bt10, 'умова')
    bt10.grid(row=0, column=18, padx=5, pady=5)

    separator9 = ttk.Separator(tab2, orient='vertical')
    separator9.grid(column=19, row=0, sticky='ns')

    bt11 = Button(tab2, text='Формула 11', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint11 = Hovertip(bt11, 'умова')
    bt11.grid(row=0, column=20, padx=5, pady=5)

    separator10 = ttk.Separator(tab2, orient='vertical')
    separator10.grid(column=21, row=0, sticky='ns')

    bt12 = Button(tab2, text='Формула 12', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint12 = Hovertip(bt12, 'умова')
    bt12.grid(row=0, column=22, padx=5, pady=1)

    separator11 = ttk.Separator(tab2, orient='vertical')
    separator11.grid(column=23, row=0, sticky='ns')

    bt13 = Button(tab2, text='Формула 13', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint13 = Hovertip(bt13, 'умова')
    bt13.grid(row=0, column=24, padx=5, pady=1)

    separator12 = ttk.Separator(tab2, orient='vertical')
    separator12.grid(column=25, row=0, rowspan=2, sticky='ns')

    lbl2 = Label(tab2, text="2.2. Математичне дисконтування та облік за складними ставками відсотка").grid(row=1,
                                                                                                           column=12,
                                                                                                           columnspan=13,
                                                                                                           padx=0,
                                                                                                           pady=1)

    # tab3
    bt1 = Button(tab3, text='Кількість років', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_n_by_SPi(fr))
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=0, column=0, padx=5, pady=5)

    separator0 = ttk.Separator(tab3, orient='vertical')
    separator0.grid(column=1, row=0, sticky='ns')

    bt2 = Button(tab3, text='Кількість років', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_n_by_SPd(fr))
    bthint2 = Hovertip(bt2, 'умова')
    bt2.grid(row=0, column=2, padx=5, pady=5)

    separator1 = ttk.Separator(tab3, orient='vertical')
    separator1.grid(column=3, row=0, sticky='ns')

    bt3 = Button(tab3, text='Кількість днів', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_t_by_SPi(fr))
    bthint3 = Hovertip(bt3, 'умова')
    bt3.grid(row=0, column=4, padx=5, pady=1)

    separator2 = ttk.Separator(tab3, orient='vertical')
    separator2.grid(column=5, row=0, sticky='ns')

    bt4 = Button(tab3, text='Кількість днів', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_t_by_SPd(fr))
    bthint4 = Hovertip(bt4, 'умова')
    bt4.grid(row=0, column=6, padx=5, pady=1)

    separator3 = ttk.Separator(tab3, orient='vertical')
    separator3.grid(column=7, row=0, sticky='ns')

    bt5 = Button(tab3, text='Відсоткова ставка', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_i_by_SPn(fr))
    bthint5 = Hovertip(bt5, 'умова')
    bt5.grid(row=0, column=8, padx=5, pady=1)

    separator4 = ttk.Separator(tab3, orient='vertical')
    separator4.grid(column=9, row=0, sticky='ns')

    bt6 = Button(tab3, text='Відсоткова ставка', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_i_by_SPt(fr))
    bthint6 = Hovertip(bt6, 'умова')
    bt6.grid(row=0, column=10, padx=5, pady=1)

    separator5 = ttk.Separator(tab3, orient='vertical')
    separator5.grid(column=11, row=0, sticky='ns')

    bt7 = Button(tab3, text='Дисконт', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_d_by_SPn(fr))
    bthint7 = Hovertip(bt7, 'умова')
    bt7.grid(row=0, column=12, padx=5, pady=5)

    separator6 = ttk.Separator(tab3, orient='vertical')
    separator6.grid(column=13, row=0, sticky='ns')

    bt8 = Button(tab3, text='Дисконт', image=icon1, compound=TOP, borderwidth=0, command=lambda:get_d_by_SPt(fr))
    bthint8 = Hovertip(bt8, 'умова')
    bt8.grid(row=0, column=14, padx=5, pady=5)

    separator7 = ttk.Separator(tab3, orient='vertical')
    separator7.grid(column=15, row=0, rowspan=2, sticky='ns')

    lbl1 = Label(tab3, text="3.1. Визначення деяких параметрів фінансових угод з простими ставками").grid(row=1,
                                                                                                          column=0,
                                                                                                          columnspan=15,
                                                                                                          padx=0,
                                                                                                          pady=1)

    bt9 = Button(tab3, text='Формула 9', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint9 = Hovertip(bt9, 'умова')
    bt9.grid(row=0, column=16, padx=5, pady=1)

    separator8 = ttk.Separator(tab3, orient='vertical')
    separator8.grid(column=17, row=0, sticky='ns')

    bt10 = Button(tab3, text='Формула 10', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint10 = Hovertip(bt10, 'умова')
    bt10.grid(row=0, column=18, padx=5, pady=5)

    separator9 = ttk.Separator(tab3, orient='vertical')
    separator9.grid(column=19, row=0, sticky='ns')

    bt11 = Button(tab3, text='Формула 11', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint11 = Hovertip(bt11, 'умова')
    bt11.grid(row=0, column=20, padx=5, pady=5)

    separator10 = ttk.Separator(tab3, orient='vertical')
    separator10.grid(column=21, row=0, sticky='ns')

    bt12 = Button(tab3, text='Формула 12', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint12 = Hovertip(bt12, 'умова')
    bt12.grid(row=0, column=22, padx=5, pady=1)

    separator11 = ttk.Separator(tab3, orient='vertical')
    separator11.grid(column=23, row=0, sticky='ns')

    bt13 = Button(tab3, text='Формула 13', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint13 = Hovertip(bt13, 'умова')
    bt13.grid(row=0, column=24, padx=5, pady=1)

    separator12 = ttk.Separator(tab3, orient='vertical')
    separator12.grid(column=25, row=0, sticky='ns')

    bt14 = Button(tab3, text='Формула 14', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint14 = Hovertip(bt14, 'умова')
    bt14.grid(row=0, column=26, padx=5, pady=1)

    separator13 = ttk.Separator(tab3, orient='vertical')
    separator13.grid(column=27, row=0, sticky='ns')

    bt15 = Button(tab3, text='Формула 15', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint15 = Hovertip(bt15, 'умова')
    bt15.grid(row=0, column=28, padx=5, pady=1)

    separator14 = ttk.Separator(tab3, orient='vertical')
    separator14.grid(column=29, row=0, sticky='ns')

    bt16 = Button(tab3, text='Формула 16', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint16 = Hovertip(bt16, 'умова')
    bt16.grid(row=0, column=30, padx=5, pady=1)

    separator15 = ttk.Separator(tab3, orient='vertical')
    separator15.grid(column=31, row=0, rowspan=2, sticky='ns')

    lbl2 = Label(tab3, text="3.2. Визначення деяких параметрів фінансових угод з складними ставками").grid(row=1,
                                                                                                           column=16,
                                                                                                           columnspan=15
                                                                                                           , padx=0,
                                                                                                           pady=1)

    # tab4
    bt1 = Button(tab4, text='Формула 1', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=0, column=0, padx=5, pady=5)

    separator0 = ttk.Separator(tab4, orient='vertical')
    separator0.grid(column=1, row=0, sticky='ns')

    bt2 = Button(tab4, text='Формула 2', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint2 = Hovertip(bt2, 'умова')
    bt2.grid(row=0, column=2, padx=5, pady=5)

    separator1 = ttk.Separator(tab4, orient='vertical')
    separator1.grid(column=3, row=0, sticky='ns')

    bt3 = Button(tab4, text='Формула 3', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint3 = Hovertip(bt3, 'умова')
    bt3.grid(row=0, column=4, padx=5, pady=1)

    separator2 = ttk.Separator(tab4, orient='vertical')
    separator2.grid(column=5, row=0, sticky='ns')

    bt4 = Button(tab4, text='Формула 4', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint4 = Hovertip(bt4, 'умова')
    bt4.grid(row=0, column=6, padx=5, pady=1)

    separator3 = ttk.Separator(tab4, orient='vertical')
    separator3.grid(column=7, row=0, rowspan=2, sticky='ns')

    lbl1 = Label(tab4, text="4.1. Постійна сила росту").grid(row=1, column=0, columnspan=7, padx=0, pady=1)

    bt5 = Button(tab4, text='Формула 5', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint5 = Hovertip(bt5, 'умова')
    bt5.grid(row=0, column=8, padx=5, pady=1)

    separator4 = ttk.Separator(tab4, orient='vertical')
    separator4.grid(column=9, row=0, sticky='ns')

    bt6 = Button(tab4, text='Формула 6', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint6 = Hovertip(bt6, 'умова')
    bt6.grid(row=0, column=10, padx=5, pady=1)

    separator5 = ttk.Separator(tab4, orient='vertical')
    separator5.grid(column=11, row=0, sticky='ns')

    bt7 = Button(tab4, text='Формула 7', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint7 = Hovertip(bt7, 'умова')
    bt7.grid(row=0, column=12, padx=5, pady=5)

    separator6 = ttk.Separator(tab4, orient='vertical')
    separator6.grid(column=13, row=0, sticky='ns')

    bt8 = Button(tab4, text='Формула 8', image=icon1, compound=TOP, borderwidth=0, command=None)
    bthint8 = Hovertip(bt8, 'умова')
    bt8.grid(row=0, column=14, padx=5, pady=5)

    separator7 = ttk.Separator(tab4, orient='vertical')
    separator7.grid(column=15, row=0, rowspan=2, sticky='ns')

    lbl1 = Label(tab4, text="4.2. Змінна сила росту").grid(row=1, column=8, columnspan=7, padx=0, pady=1)


def chapter_one_task_one_page():
    clear()
    frame = Frame(root)
    frame.place(anchor='nw')    # frame.place(anchor='n', relx=0.5, rely=0, relheight=1, relwidth=1)
    nb = ttk.Notebook(frame)
    nb.grid(row=0, column=0, columnspan=5)
    # main_page
    click_frame=Frame(frame)
    click_frame.grid(row=1, column=0,padx=0)
    lb=Label(click_frame,text="ttuutututut")
    lb.pack()
    template(nb,click_frame)
def clear_frame(frame):
   for x in frame.winfo_children():
      x.destroy()
    
def defaul_simple_rates(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   cap_rate_label=Label(input_frame,text="Капітал: ")
   cap_rate_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)
   input_frame.pack(side=LEFT)
   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      k=365
      t=int((l_day-f_day).days)
      if(calendar.isleap(l_day.year)):
         k=366
      p=float(capital.get())
      i=float(interest.get())
      s= SIL.defaul_simple_rates(p,t,i,k)
      res_var.set("Сума боргу: "+str(s))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def changing_simple_rates(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   cap_rate_label=Label(input_frame,text="Капітал: ")
   cap_rate_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)
   periods_var=StringVar(value="")
   periods_label=Label(frame,textvariable=periods_var)
   t=[]
   i=[]
   def add_period():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      ti=int((l_day-f_day).days)
      t.append(ti)
      ii=float(interest.get())
      i.append(ii)
      periods_var.set(periods_var.get()+"\n"+first_day.get_date()+" "+last_day.get_date()+" "+str(ii))
      
   def del_period():
      try:
         datins=periods_var.get().split("\n")
         del(datins[-1])
         periods_var.set("\n".join(datins))
         del(t[-1])
         del(i[-1])
      except:
         pass

   add_period_btn=Button(input_frame,text="Додати період",command=add_period)
   add_period_btn.grid(row=0,column=2)
   del_period_btn=Button(input_frame,text="Видалити період",command=del_period)
   del_period_btn.grid(row=1,column=2)
   input_frame.pack(side=LEFT)
   periods_label.pack(side=LEFT)
   
   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   

   def clak():
      k=365
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      if(calendar.isleap(l_day.year)):
         k=366
      k=[k]*len(t)
      p=float(capital.get())
      s= SIL.changing_simple_rates(p,t,i,k)
      res_var.set("Сума боргу: "+str(s))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def reinvestment_simple_rates(frame):

   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   cap_rate_label=Label(input_frame,text="Капітал: ")
   cap_rate_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)
   periods_var=StringVar(value="")
   periods_label=Label(frame,textvariable=periods_var)
   t=[]
   i=[]
   def add_period():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      ti=int((l_day-f_day).days)
      t.append(ti)
      ii=float(interest.get())
      i.append(ii)
      periods_var.set(periods_var.get()+"\n"+first_day.get_date()+" "+last_day.get_date()+" "+str(ii))
      
   def del_period():
      try:
         datins=periods_var.get().split("\n")
         del(datins[-1])
         periods_var.set("\n".join(datins))
         del(t[-1])
         del(i[-1])
      except:
         pass

   add_period_btn=Button(input_frame,text="Додати період",command=add_period)
   add_period_btn.grid(row=0,column=2)
   del_period_btn=Button(input_frame,text="Видалити період",command=del_period)
   del_period_btn.grid(row=1,column=2)
   input_frame.pack(side=LEFT)
   periods_label.pack(side=LEFT)
   
   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   

   def clak():
      k=365
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      if(calendar.isleap(l_day.year)):
         k=366
      k=[k]*len(t)
      p=float(capital.get())
      s= SIL.reinvestment_simple_rates(p,t,i,k)
      res_var.set("Сума боргу: "+str(s))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def simple_rates_for_time_changing_sums(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   cap_rate_label=Label(input_frame,text="Залишок на рахунку: ")
   cap_rate_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)
   periods_var=StringVar(value="")
   periods_label=Label(frame,textvariable=periods_var)
   t=[]
   r=[]
   def add_period():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      ti=int((l_day-f_day).days)
      t.append(ti)
      ri=float(capital.get())
      r.append(ri)
      periods_var.set(periods_var.get()+"\n"+first_day.get_date()+" "+last_day.get_date()+" "+str(ri))
      
   def del_period():
      try:
         datins=periods_var.get().split("\n")
         del(datins[-1])
         periods_var.set("\n".join(datins))
         del(t[-1])
         del(r[-1])
      except:
         pass

   add_period_btn=Button(input_frame,text="Додати період",command=add_period)
   add_period_btn.grid(row=0,column=2)
   del_period_btn=Button(input_frame,text="Видалити період",command=del_period)
   del_period_btn.grid(row=1,column=2)
   input_frame.pack(side=LEFT)
   periods_label.pack(side=LEFT)
   
   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   

   def clak():
      k=365
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      if(calendar.isleap(l_day.year)):
         k=366
      i=float(interest.get())
      s= SIL.simple_rates_for_time_changing_sums(r,t,i,k)
      res_var.set("Нарахована сума: "+str(s))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def single_time_payment(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   amount_label=Label(input_frame,text="Кількість виплат: ")
   amount_label.grid(row=2,column=0)
   amount=DoubleVar()
   amount_entry=Entry(input_frame, width = 15, textvariable = amount)
   amount_entry.grid(row=2,column=1)

   input_frame.pack(side=LEFT)
   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      k=365
      t=int((l_day-f_day).days)
      if(calendar.isleap(l_day.year)):
         k=366
      p=float(capital.get())
      i=float(interest.get())
      m=float(amount.get())
      s= SIL.defaul_simple_rates(p,t,i,k)
      print(s)
      r=SIL.single_time_payment(s,t/k,m)
      res_var.set("Сума разової виплати: "+str(r))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def discount_prise(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   end_S_rate_label=Label(input_frame,text="Кінцева сума: ")
   end_S_rate_label.grid(row=1,column=0)
   end_S=DoubleVar()
   end_S_entry=Entry(input_frame, width = 15, textvariable = end_S)
   end_S_entry.grid(row=1,column=1)
   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      k=365
      t=int((l_day-f_day).days)
      if(calendar.isleap(l_day.year)):
         k=366
      s=float(end_S.get())
      i=float(interest.get())
      p= SIL.discount_prise(s,t,i,k)
      res_var.set("Дисконтована вартість: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def discount(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   cap_rate_label=Label(input_frame,text="Капітал: ")
   cap_rate_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)
   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      k=365
      t=int((l_day-f_day).days)
      if(calendar.isleap(l_day.year)):
         k=366
      p=float(capital.get())
      i=float(interest.get())
      D= SIL.discount(t,k,p,i)
      res_var.set("Дисконт: "+str(D))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def bank_accounting_rate(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=0,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   accrual_label=Label(input_frame,text="Сума нарахування: ")
   accrual_label.grid(row=1,column=0)
   accrual=DoubleVar()
   accrual_entry=Entry(input_frame, width = 15, textvariable = accrual)
   accrual_entry.grid(row=1,column=1)
   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      k=365
      t=int((l_day-f_day).days)
      if(calendar.isleap(l_day.year)):
         k=366
      p=float(debt.get())
      s=float(accrual.get())
      d= SIL.bank_accounting_rate(s,p,t,k)
      res_var.set("Дисконтний множник: "+str(d))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def bank_accounting(frame):
   clear_frame(frame)
   frame.grid(row=1, column=0)

   date_frame=Frame(frame)

   first_date_frame=Frame(date_frame)
   start_label=Label(first_date_frame,text="Початок")
   start_label.pack()
   first_day = Calendar(first_date_frame,locale="uk_UA")
   first_day.pack()
   first_date_frame.pack(side=LEFT)
   
   last_date_frame=Frame(date_frame)
   end_label=Label(last_date_frame,text="Кінець")
   end_label.pack()
   last_day = Calendar(last_date_frame,locale="uk_UA")
   last_day.pack()
   last_date_frame.pack(side=LEFT)

   date_frame.pack(side=LEFT)

   input_frame=Frame(frame)

   disc_label=Label(input_frame,text="Дисконтний множник: ")
   disc_label.grid(row=0,column=0)
   disc=DoubleVar()
   disc_entry=Entry(input_frame, width = 15, textvariable = disc)
   disc_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   accrual_label=Label(input_frame,text="Сума нарахування: ")
   accrual_label.grid(row=1,column=0)
   accrual=DoubleVar()
   accrual_entry=Entry(input_frame, width = 15, textvariable = accrual)
   accrual_entry.grid(row=1,column=1)
   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      k=365
      t=int((l_day-f_day).days)
      if(calendar.isleap(l_day.year)):
         k=366
      d=float(disc.get())
      s=float(accrual.get())
      p= SIL.bank_accounting(s,d,t,k)
      res_var.set("Сума боргу: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_n_by_SPi(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      i=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())

      p= SIFP.get_n_by_SPi(s,p,i)
      res_var.set("Кількість років: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_n_by_SPd(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Дисконт: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      d=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())

      p= SIFP.get_n_by_SPd(s,p,d)
      res_var.set("Кількість років: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_t_by_SPi(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Часова база: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      i=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      k=float(base.get())

      p= SIFP.get_t_by_SPi(s,p,i,k)
      res_var.set("Кількість днів: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_t_by_SPd(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Дисконт: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Часова база: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      d=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      k=float(base.get())

      p= SIFP.get_t_by_SPd(s,p,d,k)
      res_var.set("Кількість днів: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_i_by_SPn(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Кількість років: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      n=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())

      p= SIFP.get_i_by_SPn(s,p,n)
      res_var.set("Відсоткова ставка: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_i_by_SPt(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Кількість днів: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Часова база: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      t=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      k=float(base.get())

      p= SIFP.get_i_by_SPt(s,p,t,k)
      res_var.set("Відсоткова ставка: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_d_by_SPn(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Кількість років: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      n=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())

      p= SIFP.get_d_by_SPn(s,p,n)
      res_var.set("Дисконт: "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_d_by_SPt(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Кількість днів: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Капітал: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сума боргу: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Часова база: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      t=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      k=float(base.get())

      p= SIFP.get_d_by_SPt(s,p,t,k)
      res_var.set("дисконт "+str(p))
      print(s)
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def chapter_two_task_one_page():
    clear()
    frame = Frame(root)
    frame.place(anchor='n', relx=0.5, rely=0, relheight=1, relwidth=1)
    nb = ttk.Notebook(frame)
    nb.grid(row=0, column=0, columnspan=5)
    template(nb)

    # page
    formula2_1(frame)