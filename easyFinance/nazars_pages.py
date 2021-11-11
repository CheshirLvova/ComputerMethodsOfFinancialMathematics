from libs import *
from window import *
import SimpleInterestsLibrary as SIL
import SimpleInterestsFinanceParameters as SIFP
import ComplicatedInterestsFinanceParameters as CIFP
import continuousInterests as CI
import changingInterestsPower as CIP
import time
import datetime
import calendar


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
      res_var.set("Сума боргу: "+'{:,.2f}'.format(s))
   
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
   t=[]
   i=[]
   table=Frame(frame)
   label = Label(table, text="початок", bg="white", padx=3, pady=3)
   label.grid(row=0, column=0, sticky="nsew")
   label = Label(table, text="кінець", bg="white", padx=3, pady=3)
   label.grid(row=0, column=1, sticky="nsew")
   label = Label(table, text="відсоткова ставка", bg="white", padx=3, pady=3)
   label.grid(row=0, column=2, sticky="nsew")
   def add_period():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      ti=int((l_day-f_day).days)
      t.append(ti)
      ii=float(interest.get())
      i.append(ii)
      for r in range(len(t)):
            label = Label(table, text=f_day.date(), bg="white", padx=3, pady=3)
            label.grid(row=r+1, column=0, sticky="nsew")
            label = Label(table, text=l_day.date(), bg="white", padx=3, pady=3)
            label.grid(row=r+1, column=1, sticky="nsew")
            label = Label(table, text=i[r], bg="white", padx=3, pady=3)
            label.grid(row=r+1, column=2, sticky="nsew")
      
   def del_period():
      try:
         for lable in table.grid_slaves():
            if int(lable.grid_info()["row"]) ==len(t):
               lable.grid_forget()
         del(t[-1])
         del(i[-1])
      except:
         pass

   add_period_btn=Button(input_frame,text="Додати період",command=add_period)
   add_period_btn.grid(row=0,column=2)
   del_period_btn=Button(input_frame,text="Видалити період",command=del_period)
   del_period_btn.grid(row=1,column=2)
   input_frame.pack(side=LEFT)
   table.pack(side=LEFT,anchor=N)
   
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
      res_var.set("Сума боргу: "+'{:,.2f}'.format(s))
   
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
   t=[]
   i=[]
   table=Frame(frame)
   label = Label(table, text="початок", bg="white", padx=3, pady=3)
   label.grid(row=0, column=0, sticky="nsew")
   label = Label(table, text="кінець", bg="white", padx=3, pady=3)
   label.grid(row=0, column=1, sticky="nsew")
   label = Label(table, text="відсоткова ставка", bg="white", padx=3, pady=3)
   label.grid(row=0, column=2, sticky="nsew")
   def add_period():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      ti=int((l_day-f_day).days)
      t.append(ti)
      ii=float(interest.get())
      i.append(ii)
      for r in range(len(t)):
            label = Label(table, text=f_day.date(), bg="white", padx=3, pady=3)
            label.grid(row=r+1, column=0, sticky="nsew")
            label = Label(table, text=l_day.date(), bg="white", padx=3, pady=3)
            label.grid(row=r+1, column=1, sticky="nsew")
            label = Label(table, text=i[r], bg="white", padx=3, pady=3)
            label.grid(row=r+1, column=2, sticky="nsew")
      
   def del_period():
      try:
         for lable in table.grid_slaves():
            if int(lable.grid_info()["row"]) ==len(t):
               lable.grid_forget()
         del(t[-1])
         del(i[-1])
      except:
         pass

   add_period_btn=Button(input_frame,text="Додати період",command=add_period)
   add_period_btn.grid(row=0,column=2)
   del_period_btn=Button(input_frame,text="Видалити період",command=del_period)
   del_period_btn.grid(row=1,column=2)
   input_frame.pack(side=LEFT)
   table.pack(side=LEFT,anchor=N)

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
      res_var.set("Сума боргу: "+'{:,.2f}'.format(s))
   
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
   t=[]
   r=[]
   table=Frame(frame)
   label = Label(table, text="початок", bg="white", padx=3, pady=3)
   label.grid(row=0, column=0, sticky="nsew")
   label = Label(table, text="кінець", bg="white", padx=3, pady=3)
   label.grid(row=0, column=1, sticky="nsew")
   label = Label(table, text="Залишок", bg="white", padx=3, pady=3)
   label.grid(row=0, column=2, sticky="nsew")
   def add_period():
      f_day=datetime.datetime.strptime(first_day.get_date(),"%d.%m.%y")
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      ti=int((l_day-f_day).days)
      t.append(ti)
      ri=float(capital.get())
      r.append(ri)
      for rw in range(len(t)):
            label = Label(table, text=f_day.date(), bg="white", padx=3, pady=3)
            label.grid(row=rw+1, column=0, sticky="nsew")
            label = Label(table, text=l_day.date(), bg="white", padx=3, pady=3)
            label.grid(row=rw+1, column=1, sticky="nsew")
            label = Label(table, text=r[rw], bg="white", padx=3, pady=3)
            label.grid(row=rw+1, column=2, sticky="nsew")
      
   def del_period():
      try:
         for lable in table.grid_slaves():
            if int(lable.grid_info()["row"]) ==len(t):
               lable.grid_forget()
         del(t[-1])
         del(r[-1])
      except:
         pass

   add_period_btn=Button(input_frame,text="Додати період",command=add_period)
   add_period_btn.grid(row=0,column=2)
   del_period_btn=Button(input_frame,text="Видалити період",command=del_period)
   del_period_btn.grid(row=1,column=2)
   input_frame.pack(side=LEFT)
   table.pack(side=LEFT,anchor=N)
   
   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   

   def clak():
      k=365
      l_day=datetime.datetime.strptime(last_day.get_date(),"%d.%m.%y")
      if(calendar.isleap(l_day.year)):
         k=366
      i=float(interest.get())
      s= SIL.simple_rates_for_time_changing_sums(r,t,i,k)
      res_var.set("Нарахована сума: "+'{:,.2f}'.format(s))
   
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

      r=SIL.single_time_payment(s,t/k,m)
      res_var.set("Сума разової виплати: "+'{:,.2f}'.format(r))
   
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
      res_var.set("Дисконтована вартість: "+'{:,.2f}'.format(p))
   
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
      res_var.set("Сума боргу: "+'{:,.2f}'.format(p))
   
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
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Сget_n_by_SPi(frame):
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

      p= CIFP.get_n_by_SPi(s,p,i)
      res_var.set("Кількість років: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Cget_n_by_SPd(frame):
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

      p= CIFP.get_n_by_SPi(s,p,d)
      res_var.set("Кількість років: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Cget_n_by_SPmj(frame):
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

   base_label=Label(input_frame,text="Кількість зарахувань: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      j=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      m=float(base.get())

      p= CIFP.get_n_by_SPmj(s,p,m,j)
      res_var.set("Кількість днів "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Cget_n_by_SPmf(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Номінальна ставка: ")
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

   base_label=Label(input_frame,text="Кількість зарахувань: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      f=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      m=float(base.get())

      p= CIFP.get_n_by_SPmf(s,p,m,f)
      res_var.set("Кількість днів "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Cget_i_by_SPn(frame):
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

      p= CIFP.get_i_by_SPn(s,p,N)
      res_var.set("Відсоткова ставка: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Cget_d_by_SPn(frame):
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

      p= CIFP.get_d_by_SPn(s,p,N)
      res_var.set("Дисконт: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Cget_j_by_SPmn(frame):
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

   base_label=Label(input_frame,text="Кількість зарахувань: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      n=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      m=float(base.get())

      p= CIFP.get_j_by_SPmn(s,p,m,n)
      res_var.set("Відсоткова ставка: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def Cget_f_by_SPmn(frame):
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

   base_label=Label(input_frame,text="Кількість зарахувань: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      n=float(interest.get())
      p=float(capital.get())
      s=float(debt.get())
      m=float(base.get())

      p= CIFP.get_j_by_SPmn(s,p,m,n)
      res_var.set("Номінальна ставка: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def continuousSum(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Сила росту: ")
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

   debt_label=Label(input_frame,text="Кількість років: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      delta=float(interest.get())
      p=float(capital.get())
      n=float(debt.get())

      p= CI.continuousSum(p,delta,n)
      res_var.set("Сума нарахування: "+'{:,.2f}'.format(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def continuousRate(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Відсоткова ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      i=float(interest.get())
      p= CI.continuousRate(i)
      res_var.set("Неперервна ставка: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def rate_from_contimuousRate(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Неперервна ставка: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      i=float(interest.get())

      p= CI.rate_from_contimuousRate(i)
      res_var.set("Відсоткова ставка: "+str(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def get_P_from_countinuousSum(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Сила росту: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Сума нарахування: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Кількість років: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      delta=float(interest.get())
      s=float(capital.get())
      n=float(debt.get())

      p= CI.get_P_from_countinuousSum(s,delta,n)
      res_var.set("Сума боргу: "+'{:,.2f}'.format(p))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def AccLinear_rate_power(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Приріст: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Кількість років: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сила приросту: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Сума боргу: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      a=float(interest.get())
      n=float(capital.get())
      asp=float(debt.get())
      p=float(base.get())

      aspf= CIP.linear_rate_power(asp,a,n)
      s=CIP.accrued_amount(p,aspf)
      res_var.set("Нарахована сума: "+'{:,.2f}'.format(s))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def AccExp_rate_power(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Приріст: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Кількість років: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сила приросту: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Сума боргу: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      a=float(interest.get())
      n=float(capital.get())
      asp=float(debt.get())
      p=float(base.get())

      aspf= CIP.exp_rate_power(asp,a,n)
      s=CIP.accrued_amount(p,aspf)
      res_var.set("Нарахована сума: "+'{:,.2f}'.format(s))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def CosLinear_rate_power(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Приріст: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Кількість років: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сила приросту: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Нарахована сума: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      a=float(interest.get())
      n=float(capital.get())
      asp=float(debt.get())
      p=float(base.get())

      aspf= CIP.linear_rate_power(asp,a,n)
      s=CIP.cost(p,aspf)
      res_var.set("Сума виплат: "+'{:,.2f}'.format(s))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)

def CosExp_rate_power(frame):
   clear_frame(frame)
   input_frame=Frame(frame)

   int_rate_label=Label(input_frame,text="Приріст: ")
   int_rate_label.grid(row=0,column=0)
   interest=DoubleVar()
   interest_entry=Entry(input_frame, width = 15, textvariable = interest)
   interest_entry.grid(row=0,column=1)
   input_frame.pack(side=LEFT)

   capital_label=Label(input_frame,text="Кількість років: ")
   capital_label.grid(row=1,column=0)
   capital=DoubleVar()
   capital_entry=Entry(input_frame, width = 15, textvariable = capital)
   capital_entry.grid(row=1,column=1)

   debt_label=Label(input_frame,text="Сила приросту: ")
   debt_label.grid(row=2,column=0)
   debt=DoubleVar()
   debt_entry=Entry(input_frame, width = 15, textvariable = debt)
   debt_entry.grid(row=2,column=1)
   input_frame.pack(side=LEFT)

   base_label=Label(input_frame,text="Нарахована сума: ")
   base_label.grid(row=3,column=0)
   base=DoubleVar()
   base_entry=Entry(input_frame, width = 15, textvariable = base)
   base_entry.grid(row=3,column=1)
   input_frame.pack(side=LEFT)

   input_frame.pack(side=LEFT)

   res_var=StringVar(value="")
   res_label=Label(frame,textvariable=res_var)
   def clak():
      a=float(interest.get())
      n=float(capital.get())
      asp=float(debt.get())
      p=float(base.get())

      aspf= CIP.exp_rate_power(asp,a,n)
      s=CIP.cost(p,aspf)
      res_var.set("Сума виплат: "+'{:,.2f}'.format(s))
   
   calc_btn=Button(frame,text="Розрахувати", command=clak)
   
   calc_btn.pack(side=LEFT)
   res_label.pack(side=LEFT)
