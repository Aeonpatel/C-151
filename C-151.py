from tkinter import*
root=Tk()
root.title("Sales record")
root.geometry("600x600")

max_profit_sales=Label(root,fg="green" , bg="white")
min_profit_sales=Label(root,fg="black" , bg="red")
month_l=Label(root)
Sales_l=Label(root)

Months=("January","Febuary","March","April","May","June","July","August","September","October","November","December")
month_l["text"] = Months

Sales=(22000,46000,93000,74000,62000,34000,76000,98000,12000,73000,91000,30000)
Sales_l["text"] = Sales

def maximum_sales():
    max_profit=max(Sales)
    max_profit_ind=Sales.index(max_profit)

    max_profit_month=Months[max_profit_ind]
    max_profit_sales["text"] = "Your maximum number of sales in this year are " + str(max_profit) + " and the month in which you got the maxium number of sales is " + str(max_profit_month)

btn_max=Button(root,text="Show maximum profit",command=maximum_sales)

def minimum_sales():
    min_profit=min(Sales)
    min_profit_ind=Sales.index(min_profit)


    min_profit_month=Months[min_profit_ind]
    min_profit_sales["text"] = "Your minimum number of sales in this year are " + str(min_profit) + " and the month in which you got the minimum profit is " + str(min_profit_month)

btn_min=Button(root,text="Show minimum profit",command=minimum_sales)

month_l.pack()
Sales_l.pack()
btn_max.pack()
max_profit_sales.pack()
btn_min.pack()
min_profit_sales.pack()

root.mainloop()