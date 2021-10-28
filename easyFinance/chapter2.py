from libs import *


def formula2_1(frame):
    frame.columnconfigure(0, minsize=300)
    frame.columnconfigure(1, minsize=10)
    frame.columnconfigure(2, minsize=200)
    frame.columnconfigure(3, minsize=100)
    frame.columnconfigure(4, minsize=850)
    description = """
Наведена вище формула і є формулою нарощення складних
відсотків. Вираз (1+i) прийнято називати множником
нарощення за складними відсотками.
    """
    lbl1 = Label(frame, text=description, font="Arial 8", justify=LEFT).grid(row=1, column=0, rowspan=9, padx=0, pady=1)
    separatordecription = ttk.Separator(frame, orient='vertical').grid(column=1, row=1, rowspan=9, sticky='ns')

    Pvalue = DoubleVar()
    nvalue = DoubleVar()
    ivalue = DoubleVar()

    def calculate():
        S = round(Pvalue.get() * ((1 + ivalue.get()) ** nvalue.get()), 4)
        lblres = Label(frame, text="Нарощена сума (з відсотками) на кінець терміну S = {0}".format(S)).grid(row=7,
                                                                                                            column=2,
                                                                                                            columnspan=2
                                                                                                            , padx=0,
                                                                                                            pady=1,
                                                                                                            sticky='w')

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
