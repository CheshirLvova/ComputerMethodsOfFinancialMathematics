from libs import *
from window import *


def chapter_seven_task_one_page(frame):
    clear_frame(frame)
    frame.grid(row=1, column=0)
    frame_inside = Frame(frame)
    # page
    frame_inside.columnconfigure(0, minsize=300)
    frame_inside.columnconfigure(1, minsize=10)
    frame_inside.columnconfigure(2, minsize=200)
    frame_inside.columnconfigure(3, minsize=100)
    frame_inside.columnconfigure(4, minsize=850)
    description = """
    Для планування погашення заборгованості будемо
    використовувати наступні позначення:
    D – величина заборгованості,
    Y – термінова виплата,
    I – проценти за позикою,
    R – витрати на погашення основної частини боргу,
    g – відсоткова ставка за позикою,
    n – тривалість позики,
    L – тривалість пільгового періоду. За означенням витрати на
    обслуговування боргу (термінова виплата) становлять
    Y = I + R .

    Нехай фонд формується шляхом надходження регулярних
    щорічних внесків R , на які нараховуються складні відсотки за
    ставкою i% річних. Крім того, відбувається виплата відсотків за
    борг за ставкою g%. В такому випадку термінова виплата
    становитиме: Y = Dg + R

    Друге обчислення*:
    якщо б угодою передбачалося приєднання відсотків до
    основної суми боргу"""
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=0, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=0, rowspan=9, sticky='ns')

    Dvalue = DoubleVar()
    nvalue = DoubleVar()
    gvalue = DoubleVar()
    ivalue = DoubleVar()
    one = DoubleVar()
    one.set(1.0)

    def calculate():
        sni_formula = ((one.get() - ((one.get() + ivalue.get()) ** (-nvalue.get()))) / ivalue.get()) * (
                (one.get() + ivalue.get()) ** nvalue.get())
        Y = round(Dvalue.get() * gvalue.get() + (Dvalue.get() / sni_formula), 4)
        lblres = Label(frame, text="Величина термінової виплати Y = {0} грн.".format(Y)).grid(
            row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Сума позики D").grid(row=0, column=2, padx=0, pady=1, sticky='w')
    input2 = Entry(frame, textvariable=Dvalue).grid(row=0, column=3, padx=0, pady=1, sticky='w')

    lbl3 = Label(frame, text="Тривалість позики n").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Відсоткова ставка за позикою g").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=gvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl5 = Label(frame, text="Відсоткова ставка погашення боргу i").grid(row=4, column=2, padx=0, pady=1, sticky='w')
    input5 = Entry(frame, textvariable=ivalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, '''Клієнт взяв позику у  D грн. терміном на N років
    під g річних. Для погашення даної заборгованості
    створюється відповідний фонд, на вкладені у нього кошти
    нараховуються відсотки за ставкою i річних. Визначити
    величину термінової виплати, якщо фонд формується протягом
    п’яти років, а внески у нього надходять вкінці кожного року
    однаковими сумами''')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')

    def calculate1():
        sni_formula = ((one.get() - ((one.get() + ivalue.get()) ** (-nvalue.get()))) / ivalue.get()) * (
                (one.get() + ivalue.get()) ** nvalue.get())
        Y = round((Dvalue.get() * ((one.get() + gvalue.get()) ** nvalue.get())) / sni_formula, 4)
        lblres = Label(frame, text="Величина термінової виплати Y = {0} грн.".format(Y)).grid(
            row=7, column=3, columnspan=2, padx=0, pady=1, sticky='w')

    bt2 = Button(frame, text='Обчислити', command=calculate1)
    bthint2 = Hovertip(bt2, '''Продовжимо попередній приклад, взявши до уваги, що
термінові виплати включають проценти, а інші умови
зберігаються. Нехай внески у фонд надходять тільки останні
чотири роки''')
    bt2.grid(row=5, column=3, padx=5, pady=5)


def chapter_seven_task_two_page(frame):
    clear_frame(frame)
    frame.grid(row=1, column=0)
    frame_inside = Frame(frame)
    # page
    frame_inside.columnconfigure(0, minsize=300)
    frame_inside.columnconfigure(1, minsize=10)
    frame_inside.columnconfigure(2, minsize=200)
    frame_inside.columnconfigure(3, minsize=100)
    frame_inside.columnconfigure(4, minsize=850)
    description = """
        Для планування погашення заборгованості будемо
        використовувати наступні позначення:
        D – величина заборгованості,
        Y – термінова виплата,
        I – проценти за позикою,
        R – витрати на погашення основної частини боргу,
        g – відсоткова ставка за позикою,
        n – тривалість позики,
        L – тривалість пільгового періоду. За означенням витрати на
        обслуговування боргу (термінова виплата) становлять
        Y = I + R .

        Нехай фонд формується шляхом надходження регулярних
        щорічних внесків R , на які нараховуються складні відсотки за
        ставкою i% річних. Крім того, відбувається виплата відсотків за
        борг за ставкою g%. В такому випадку термінова виплата
        становитиме: Y = Dg + R
        Припустимо, що фонд потрібно сформувати за N років. У
        такому випадку внески у фонд утворюють постійну ренту. Нехай
        мова йтиме про ренту постнумерандо. Тоді R = D/sₙᵢ"""
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=0, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=0, rowspan=9, sticky='ns')

    Dvalue = DoubleVar()
    nvalue = DoubleVar()
    gvalue = DoubleVar()
    ivalue = DoubleVar()
    one = DoubleVar()
    one.set(1.0)

    lbl2 = Label(frame, text="Сума позики D").grid(row=0, column=2, padx=0, pady=1, sticky='w')
    input2 = Entry(frame, textvariable=Dvalue).grid(row=0, column=3, padx=0, pady=1, sticky='w')

    lbl3 = Label(frame, text="Тривалість позики n").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Відсоткова ставка за позикою g").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=gvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl5 = Label(frame, text="Відсоткова ставка погашення боргу i").grid(row=4, column=2, padx=0, pady=1, sticky='w')
    input5 = Entry(frame, textvariable=ivalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')

    def calculate2():
        sni_formula = ((one.get() - ((one.get() + ivalue.get()) ** (-nvalue.get()))) / ivalue.get()) * (
                (one.get() + ivalue.get()) ** nvalue.get())
        R = round(Dvalue.get() / sni_formula, 4)
        lblres = Label(frame, text=" Pентa постнумерандо R = {0} грн.".format(R)).grid(
            row=9, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    bt3 = Button(frame, text='Обчислити', command=calculate2)
    bthint3 = Hovertip(bt3, '''Клієнт взяв позику у  D грн. терміном на N років
                під g річних. Для погашення даної заборгованості
                створюється відповідний фонд, на вкладені у нього кошти
                нараховуються відсотки за ставкою i річних. Визначити
                величину термінової виплати, якщо фонд формується протягом
                п’яти років, а внески у нього надходять вкінці кожного року
                однаковими сумами у разі якщо б угодою передбачалося приєднання відсотків до
                основної суми боргу''')
    bt3.grid(row=8, column=2, padx=5, pady=5)


def chapter_seven_task_three_page(frame):
    clear_frame(frame)
    frame.grid(row=1, column=0)
    frame_inside = Frame(frame)
    # page
    frame_inside.columnconfigure(0, minsize=300)
    frame_inside.columnconfigure(1, minsize=10)
    frame_inside.columnconfigure(2, minsize=200)
    frame_inside.columnconfigure(3, minsize=100)
    frame_inside.columnconfigure(4, minsize=100)
    frame_inside.columnconfigure(5, minsize=100)
    frame_inside.columnconfigure(6, minsize=100)
    frame_inside.columnconfigure(7, minsize=550)
    description = """
            Для планування погашення заборгованості будемо
            використовувати наступні позначення:
            D – величина заборгованості,
            Y – термінова виплата,
            I – проценти за позикою,
            R – витрати на погашення основної частини боргу,
            g – відсоткова ставка за позикою,
            n – тривалість позики,
            L – тривалість пільгового періоду. За означенням витрати на
            обслуговування боргу (термінова виплата) становлять
            Y = I + R .

            Заборгованість у D грн. потрібно виплатити
            впродовж n років однаковими щорічними виплатами.
            Побудувати план погашення заборгованості за умови, що за
            позику виплачується g% річних, а виплати постнумерандо.
    """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=0, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=0, rowspan=9, sticky='ns')

    Dvalue = DoubleVar()
    nvalue = DoubleVar()
    gvalue = DoubleVar()
    one = DoubleVar()
    one.set(1.0)

    def calculate():
        d = Dvalue.get() / nvalue.get()
        lblres = Label(frame, text="Величина, що йде на погашення основного боргу d = {0} грн.".format(d)).grid(
            row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')
        Title = ['Рік', 'Залишок боргу на початок року', 'Витрати за позикою', 'Виплати боргу', 'Проценти']
        for row in range(8, int(nvalue.get()) + 9):
            for col in range(2, 7):
                if row == 8:
                    label = Label(frame, text=Title[col - 2], bg="white", padx=3, pady=3)
                    label.grid(row=row, column=col, sticky="nsew")
                else:
                    if col == 2:
                        label = Label(frame, text=row - 8, bg="white", padx=3, pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    elif col == 3:
                        label = Label(frame, text="{0} грн".format(int(Dvalue.get() - (d * (row - 9)))), bg="white",
                                      padx=3, pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    elif col == 4:
                        label = Label(frame, text=int(((Dvalue.get() - (d * (row - 9))) * 0.1) + d), bg="white", padx=3,
                                      pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    elif col == 5:
                        label = Label(frame, text=int(d), bg="white", padx=3, pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    if col == 6:
                        label = Label(frame, text=int((Dvalue.get() - (d * (row - 9))) * 0.1), bg="white", padx=3,
                                      pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    else:
                        frame.grid_columnconfigure(col, weight=1)

    lbl2 = Label(frame, text="Сума D").grid(row=0, column=2, padx=0, pady=1, sticky='w')
    input2 = Entry(frame, textvariable=Dvalue).grid(row=0, column=3, padx=0, pady=1, sticky='w')

    lbl3 = Label(frame, text="Тривалість n").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Відсоткова ставка g").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=gvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, '''Заборгованість у D грн. потрібно виплатити
впродовж n років однаковими щорічними виплатами.
Побудувати план погашення заборгованості за умови, що за
позику виплачується g% річних, а виплати постнумерандо.''')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_seven_task_four_page(frame):
    clear_frame(frame)
    frame.grid(row=1, column=0)
    frame_inside = Frame(frame)
    # page
    frame_inside.columnconfigure(0, minsize=300)
    frame_inside.columnconfigure(1, minsize=10)
    frame_inside.columnconfigure(2, minsize=200)
    frame_inside.columnconfigure(3, minsize=100)
    frame_inside.columnconfigure(4, minsize=100)
    frame_inside.columnconfigure(5, minsize=100)
    frame_inside.columnconfigure(6, minsize=100)
    frame_inside.columnconfigure(7, minsize=550)
    description = """
У цьому методі витрати на
обслуговування боргу будуть постійними впродовж усього
впродовж усього терміну погашення, при чому частина з них
йтиме на погашення процентів, а частина – на погашення
основного боргу. Таким чином маємо, що, Y = Dₜg + Rₜ

де Dₜ – залишок боргу на початок періоду t , Rₜ – виплата
основного боргу в періоді t. Нехай задано термін позики n.
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=0, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=0, rowspan=9, sticky='ns')

    Dvalue = DoubleVar()
    nvalue = DoubleVar()
    gvalue = DoubleVar()
    one = DoubleVar()
    one.set(1.0)

    def calculate():
        ani_formula = ((one.get() - ((one.get() + gvalue.get()) ** (-nvalue.get()))) / gvalue.get())
        Y = round(Dvalue.get() / ani_formula, 4)
        lblres = Label(frame, text="Величина, що йде на погашення основного боргу Y = {0} грн.".format(Y)).grid(
            row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')
        Title = ['Рік', 'Залишок боргу на початок року', 'Термінові виплати', 'Проценти', 'Погашення основного боргу']
        debt = [Y / ((1 + gvalue.get()) ** (nvalue.get() - i)) for i in range(int(nvalue.get() + 1))]
        for row in range(8, int(nvalue.get() + 1) + 9):
            for col in range(2, 7):
                if row == 8:
                    label = Label(frame, text=Title[col - 2], bg="white", padx=3, pady=3)
                    label.grid(row=row, column=col, sticky="nsew")
                elif row == int(nvalue.get() + 1) + 8 and (col == 3 or col == 4 or col == 5):
                    label = Label(frame, text=0, bg="white", padx=3, pady=3)
                    label.grid(row=row, column=col, sticky="nsew")
                elif (row == 9) and col == 3:
                    label = Label(frame, text="{0} грн".format(Dvalue.get()), bg="white", padx=3, pady=3)
                    label.grid(row=row, column=col, sticky="nsew")
                elif (row == int(nvalue.get() + 1) + 8) and col == 6:
                    label = Label(frame, text="{0} грн".format(Dvalue.get()), bg="white", padx=3, pady=3)
                    label.grid(row=row, column=col, sticky="nsew")
                else:
                    if col == 2:
                        label = Label(frame, text=row - 8, bg="white", padx=3, pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    elif col == 3:
                        label = Label(frame, text="{0} грн".format(Dvalue.get() - debt[row - 10]), bg="white",
                                      padx=3, pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    elif col == 4:
                        label = Label(frame, text=Y * 0.01, bg="white", padx=3, pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    elif col == 5:
                        label = Label(frame, text=(Dvalue.get() - debt[row - 10]) * gvalue.get(), bg="white", padx=3,
                                      pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    if col == 6:
                        label = Label(frame, text=debt[row - 9], bg="white", padx=3,
                                      pady=3)
                        label.grid(row=row, column=col, sticky="nsew")
                    else:
                        frame.grid_columnconfigure(col, weight=1)

    lbl2 = Label(frame, text="Сума D").grid(row=0, column=2, padx=0, pady=1, sticky='w')
    input2 = Entry(frame, textvariable=Dvalue).grid(row=0, column=3, padx=0, pady=1, sticky='w')

    lbl3 = Label(frame, text="Тривалість n").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Відсоткова ставка g").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=gvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, '''Заборгованість у D грн. потрібно виплатити за
n років рівними терміновими виплатами. Скласти план
погашення заборгованості за умови, що за позику виплачується
g% річних, а виплати відбуваються постнумерандо''')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_seven_task_five_page(frame):
    clear_frame(frame)
    frame.grid(row=1, column=0)
    frame_inside = Frame(frame)
    # page
    frame_inside.columnconfigure(0, minsize=300)
    frame_inside.columnconfigure(1, minsize=10)
    frame_inside.columnconfigure(2, minsize=200)
    frame_inside.columnconfigure(3, minsize=100)
    frame_inside.columnconfigure(4, minsize=850)
    description = """
Нехай кредит у сумі D грн. видано під g% річних
на N років. В цей же час ринкова відсоткова ставка становить
i% річних. Визначити умовну втрату для кредитора.
    """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=0, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=0, rowspan=9, sticky='ns')

    Dvalue = DoubleVar()
    nvalue = DoubleVar()
    gvalue = DoubleVar()
    ivalue = DoubleVar()
    one = DoubleVar()
    one.set(1.0)

    def calculate():
        ang_formula = ((one.get() - ((one.get() + gvalue.get()) ** (-nvalue.get()))) / gvalue.get())
        ani_formula = ((one.get() - ((one.get() + ivalue.get()) ** (-nvalue.get()))) / ivalue.get())
        w = ani_formula / ang_formula
        W = round(w * Dvalue.get(), 3)
        lblres = Label(frame, text="Умовна втрата для кредитора W = {0} грн.".format(W)).grid(
            row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Kредит D").grid(row=0, column=2, padx=0, pady=1, sticky='w')
    input2 = Entry(frame, textvariable=Dvalue).grid(row=0, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Тривалість позики n").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Відсоткова ставка g").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=gvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl5 = Label(frame, text="Ринкова відсоткова ставка погашення боргу i").grid(row=4, column=2, padx=0, pady=1,
                                                                                 sticky='w')
    input5 = Entry(frame, textvariable=ivalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_seven_task_six_page(frame):
    clear_frame(frame)
    frame.grid(row=1, column=0)
    frame_inside = Frame(frame)
    # page
    clear_frame(frame)
    frame.grid(row=1, column=0)
    frame_inside = Frame(frame)
    # page
    frame_inside.columnconfigure(0, minsize=300)
    frame_inside.columnconfigure(1, minsize=10)
    frame_inside.columnconfigure(2, minsize=200)
    frame_inside.columnconfigure(3, minsize=100)
    frame_inside.columnconfigure(4, minsize=100)
    frame_inside.columnconfigure(5, minsize=100)
    frame_inside.columnconfigure(6, minsize=650)
    description = """
Знайти термінову виплату і величину
несплаченого основного боргу на початок t-го року погашення.
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=0, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=0, rowspan=9, sticky='ns')

    Dvalue = DoubleVar()
    nvalue = DoubleVar()
    tvalue = DoubleVar()
    gvalue = DoubleVar()
    mvalue = DoubleVar()
    one = DoubleVar()
    one.set(1.0)

    def calculate():
        Y = round((Dvalue.get() * gvalue.get() / mvalue.get() * (
                    (one.get() + gvalue.get() / mvalue.get()) ** (mvalue.get() * nvalue.get()))) / (
                              ((one.get() + gvalue.get() / mvalue.get()) ** (mvalue.get() * nvalue.get())) - 1), 3)
        t = mvalue.get()*(nvalue.get()-tvalue.get()-one.get())-one.get()
        S = round(Dvalue.get()*((((one.get() + gvalue.get() / mvalue.get()) ** (mvalue.get() * nvalue.get())) - ((one.get() + gvalue.get() / mvalue.get()) ** t)) / (
                    (one.get() + gvalue.get() / mvalue.get()) ** (mvalue.get() * nvalue.get()) - 1)), 2)
        lblres = Label(frame,
                       text="Термінова виплата і величина несплаченого основного боргу S = {0} грн.".format(S)).grid(
            row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Kредит D").grid(row=0, column=2, padx=0, pady=1, sticky='w')
    input2 = Entry(frame, textvariable=Dvalue).grid(row=0, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Kількість років кредиту n").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl6 = Label(frame, text="t").grid(row=1, column=4, padx=0, pady=1, sticky='w')
    input6 = Entry(frame, textvariable=tvalue).grid(row=1, column=5, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Відсоткова ставка g").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=gvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl5 = Label(frame, text="Kількість періодів нарахування відсотків у році і кількість виплат у році m").grid(
        row=4, column=2, padx=0, pady=1, sticky='w')
    input5 = Entry(frame, textvariable=mvalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')
