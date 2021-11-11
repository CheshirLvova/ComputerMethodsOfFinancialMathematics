from libs import *
from window import *


def chapter_two_task_one_page(frame):
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
    На практиці в середньо- та довготермінових фінансовокредитних операціях 
    в основному використовують нарощення за
    складними відсотками, тобто коли відсотки одразу після
    нарахування не сплачуються, а приєднуються до суми боргу.
    База для нарахування таких відсотків збільшується з кожним
    кроком у часі. Нарощення за складними відсотками є
    послідовним реінвестуванням коштів, які вкладені на один
    період під простий відсоток. Оскільки відсотки приєднуються до
    суми, яка є базою для нарахування в наступному періоді, маємо
    справу з капіталізацією.
    Запишемо формулу нарощення за складними відсотками.
    Для цього використаємо такі ж позначення, як і у випадку
    нарощення за простими відсотками. Нагадаємо, що P –
    початкова величина боргу (позики, кредиту, капіталу і т. п.), S –
    нарощена сума (з процентами) на кінець терміну,
    n – кількість років нарощення,
    i – річна ставка складних відсотків (у вигляді
    десяткового дробу). Неважко переконатися, що в кінці першого
    року отримані проценти становитимуть
    P*i, а нарощена сума –
    S = P + P*i = P(1+ i). Отже, на
    кінець n -го року матимемо:
    \t\t\t S = P(1+i)ⁿ
    Наведена вище формула і є формулою нарощення складних
    відсотків. Вираз (1+i)ⁿ прийнято називати множником
    нарощення за складними відсотками.
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    Pvalue = DoubleVar()
    nvalue = DoubleVar()
    ivalue = DoubleVar()

    def calculate():
        try:
            i = DoubleVar()
            if ivalue.get() > 1:
                i.set(ivalue.get()/100)
            else:
                i.set(ivalue.get())
            S = round(Pvalue.get() * ((1 + i.get()) ** nvalue.get()), 4)
            lblres = Label(frame, text="Нарощена сума (з відсотками) на кінець терміну S = {0}".format(S)).grid(
                row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')
        except TclError:
            lblres = Label(frame, text="Введіть коректні параметри").grid(
                row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Початкова величина боргу P").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input1 = Entry(frame, textvariable=Pvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Кількість років нарощення n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Річна ставка складних відсотків i").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=ivalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_two_task_two_page(frame):
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
    Коли потрібно вирахувати проценти за весь період
    нарощення за складними відсотками, використовують наступну
    формулу:
    I = S - P = P(1+i)ⁿ - P

        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=0, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=0, rowspan=9, sticky='ns')

    Pvalue = DoubleVar()
    nvalue = DoubleVar()
    ivalue = DoubleVar()

    def calculate():
        I = round((Pvalue.get() * ((1 + ivalue.get()) ** nvalue.get())) - Pvalue.get(), 4)
        lblres = Label(frame, text="Проценти за весь період нарощення за складними відсотками I = {0}".format(I)).grid(
            row=6, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Початкова величина боргу P").grid(row=0, column=2, padx=0, pady=1, sticky='w')
    input1 = Entry(frame, textvariable=Pvalue).grid(row=0, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Кількість років нарощення n").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Річна ставка складних відсотків i").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=ivalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=4, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=5, columnspan=2, sticky='ns')


def chapter_two_task_three_page(frame):
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
    Для нарощення за номінальною ставкою j маємо формулу
    S = P(1 + j/m)ᵐ-ⁿ, де
    n – тривалість угоди в роках, m – кількість нарахувань у
    році. Таким чином, річний множник нарощення за номінальною
    ставкою j дорівнює (1 + j/m)ᵐ.
    Зауважимо, що при збільшенні кількості періодів
    нарахувань зростає темп нарощення, оскільки капіталізація
    відбувається частіше. При цьому найбільший приріст у
    нарощенні дасть перехід від щорічних нарахувань до
    щопіврічних, а найменший – перехід від щомісячних до
    щоденних нарахувань.
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    Pvalue = DoubleVar()
    nvalue = DoubleVar()
    jvalue = DoubleVar()
    mvalue = DoubleVar()

    def calculate():
        S = round(Pvalue.get() * ((1 + (jvalue.get() / mvalue.get())) ** (mvalue.get() - nvalue.get())), 4)
        lblres = Label(frame, text="Нарощена сума  за номінальною ставкою {0} % на кінець терміну S = {1}".format(
            jvalue.get(), S)).grid(row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Початкова величина боргу P").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input1 = Entry(frame, textvariable=Pvalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Тривалість угоди в роках n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Річна ставка складних відсотків j").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=jvalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Kількість нарахувань у році m").grid(row=4, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=mvalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')

    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_two_task_four_page(frame):
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
    З використанням номінальної ставки тісно пов’язане
    поняття дійсної, або ефективної відсоткової ставки, що
    відповідає даній номінальній ставці. Ефективна ставка
    відображає реальний відносний дохід отриманий за рік, тобто –
    це річна ставка складних відсотків, яка дає такий самий
    результат, як і m – разове нарахування за ставкою j/m .
    Позначимо через iₑ ефективну ставку, що відповідає
    номінальній ставці j. Тоді, прирівнюючи множники нарощення
    за обома ставками матимемо:
    j = m((1+iₑ)¹/ᵐ - 1)
    Заміна в угоді номінальної ставки на ефективну не змінює
    відносин сторін, тому що ці ставки еквівалентні у фінансовому
    відношенні.
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    nvalue = DoubleVar()
    jvalue = DoubleVar()  # iₑ
    mvalue = DoubleVar()

    def calculate():
        i = round(((1 + jvalue.get() / mvalue.get()) ** mvalue.get()) - 1, 4)
        j = round(mvalue.get() * ((1 + i) ** (1 / mvalue.get()) - 1), 4)
        lblres = Label(frame, text="Величина номінальної ставки {0} = {1}%".format(
            jvalue.get(), j)).grid(row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl4 = Label(frame, text="Величина номінальної ставки j").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=jvalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Kількість нарахувань у році n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl5 = Label(frame, text="m").grid(row=4, column=2, padx=0, pady=1, sticky='w')
    input5 = Entry(frame, textvariable=mvalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')
    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_two_task_five_page(frame):
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
        З використанням номінальної ставки тісно пов’язане
        поняття дійсної, або ефективної відсоткової ставки, що
        відповідає даній номінальній ставці. Ефективна ставка
        відображає реальний відносний дохід отриманий за рік, тобто –
        це річна ставка складних відсотків, яка дає такий самий
        результат, як і m – разове нарахування за ставкою j/m .
        Позначимо через iₑ ефективну ставку, що відповідає
        номінальній ставці j. Тоді, прирівнюючи множники нарощення
        за обома ставками матимемо:
        j = m((1+iₑ)¹/ᵐ - 1)
        Заміна в угоді номінальної ставки на ефективну не змінює
        відносин сторін, тому що ці ставки еквівалентні у фінансовому
        відношенні.
            """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    nvalue = DoubleVar()
    jvalue = DoubleVar()  # iₑ
    mvalue = DoubleVar()

    def calculate():
        i = round(((1 + jvalue.get() / mvalue.get()) ** mvalue.get()) - 1, 4)
        j = round(mvalue.get() * ((1 + i) ** (1 / mvalue.get()) - 1), 4)
        lblres = Label(frame, text="Величина номінальної ставки {0} = {1}%".format(
            jvalue.get(), j)).grid(row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl4 = Label(frame, text="Величина номінальної ставки j").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=jvalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Kількість нарахувань у році n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl5 = Label(frame, text="m").grid(row=4, column=2, padx=0, pady=1, sticky='w')
    input5 = Entry(frame, textvariable=mvalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')
    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame).grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_two_task_six_page(frame):
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
    Як і у випадку використання простої відсоткової ставки,
    математичне дисконтування за складною ставкою відсотків,
    тобто знаходження значення P за відомим значенням S, 
    відбувається за формулою:
    P = S/(1+i)ⁿ = Svⁿ
    Вираз vⁿ = 1/(1+i)ⁿ називається дисконтним множником
    складних відсотків
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    Svalue = DoubleVar()
    nvalue = DoubleVar()
    ivalue = DoubleVar()  # iₑ
    mvalue = DoubleVar()

    def calculate():
        P = round((Svalue.get() / ((1 + ivalue.get()) ** nvalue.get())), 4)
        lblres = Label(frame, text="Дисконт суми {0} = {1}%".format(
            Svalue.get(), P)).grid(row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Складна відсоткова ставка S").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input1 = Entry(frame, textvariable=Svalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Кількість років нарощення n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Величина ставки i").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=ivalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')
    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame, orient='horizontal').grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_two_task_seven_page(frame):
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
    У випадку, коли відсотки нараховуються
    m разів на рік за
    номінальною відсотковою ставкою j маємо::
    P = S/(1+j/m)ᵐⁿ = Svⁿᵐ
    Вираз vⁿᵐ = 1/(1+j/m)ᵐⁿ називається дисконтним множником
    складних відсотків
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    Svalue = DoubleVar()
    nvalue = DoubleVar()
    ivalue = DoubleVar()  # iₑ
    mvalue = DoubleVar()

    def calculate():
        P = round((Svalue.get() / ((1 + ivalue.get() / mvalue.get()) ** (nvalue.get() * mvalue.get()))), 4)
        lblres = Label(frame, text="Дисконт суми {0} = {1} (D = S - P)".format(
            Svalue.get(), Svalue.get() - P)).grid(row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Складна відсоткова ставка S").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input1 = Entry(frame, textvariable=Svalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Кількість років нарощення n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Величина ставки j").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=ivalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')
    bt1 = Button(frame, text='Обчислити', command=calculate)
    lbl5 = Label(frame, text="Kількість нарахувань у році m").grid(row=4, column=2, padx=0, pady=1, sticky='w')
    input5 = Entry(frame, textvariable=mvalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')

    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame, orient='horizontal').grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_two_task_eight_page(frame):
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
    Банківський облік за складною обліковою ставкою
    проводять за розрахунковою формулою
    P = S(1-d)ⁿ
    де P – сучасна (теперішня) сума боргу,
    S – майбутня сума боргу,
    d – складна облікова ставка, n – тривалість угоди в
    роках.
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    Svalue = DoubleVar()
    nvalue = DoubleVar()
    dvalue = DoubleVar()

    def calculate():
        P = round(Svalue.get() * ((1 - dvalue.get()) ** nvalue.get()), 4)
        lblres = Label(frame, text="сучасна (теперішня) сума боргу = {0}".format(
            P)).grid(row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Майбутня сума боргу S").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input1 = Entry(frame, textvariable=Svalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Тривалість угоди в роках n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Складна облікова ставка d").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=dvalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')
    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame, orient='horizontal').grid(column=2, row=6, columnspan=2, sticky='ns')


def chapter_two_task_nine_page(frame):
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
    Банківський облік за складною обліковою ставкою
    проводять за розрахунковою формулою
    P = S(1-d)ⁿ
    де P – сучасна (теперішня) сума боргу,
    S – майбутня сума боргу,
    d – складна облікова ставка, n – тривалість угоди в
    роках.
        """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    Svalue = DoubleVar()
    mvalue = DoubleVar()
    nvalue = DoubleVar()
    fvalue = DoubleVar()

    def calculate():
        P = round(Svalue.get() * ((1 - fvalue.get() / mvalue.get()) ** (mvalue.get() * nvalue.get())), 4)
        lblres = Label(frame, text="сучасна (теперішня) сума боргу = {0}".format(
            P)).grid(row=7, column=2, columnspan=2, padx=0, pady=1, sticky='w')

    lbl2 = Label(frame, text="Майбутня сума боргу S").grid(row=1, column=2, padx=0, pady=1, sticky='w')
    input1 = Entry(frame, textvariable=Svalue).grid(row=1, column=3, padx=0, pady=1, sticky='w')
    lbl3 = Label(frame, text="Тривалість угоди в роках n").grid(row=2, column=2, padx=0, pady=1, sticky='w')
    input3 = Entry(frame, textvariable=nvalue).grid(row=2, column=3, padx=0, pady=1, sticky='w')
    lbl4 = Label(frame, text="Hомінальна річна облікова ставка f").grid(row=3, column=2, padx=0, pady=1, sticky='w')
    input4 = Entry(frame, textvariable=fvalue).grid(row=3, column=3, padx=0, pady=1, sticky='w')
    lbl5 = Label(frame, text="Kількість нарахувань у році m").grid(row=4, column=2, padx=0, pady=1, sticky='w')
    input5 = Entry(frame, textvariable=mvalue).grid(row=4, column=3, padx=0, pady=1, sticky='w')
    bt1 = Button(frame, text='Обчислити', command=calculate)
    bthint1 = Hovertip(bt1, 'умова')
    bt1.grid(row=5, column=2, padx=5, pady=5)

    separator0 = ttk.Separator(frame, orient='horizontal').grid(column=2, row=6, columnspan=2, sticky='ns')
