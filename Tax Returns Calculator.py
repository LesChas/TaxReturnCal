import tkinter as tk

fields = ('Cattle', 'Pigs', 'Goats', 'Sheep','Chickens', 'Other',
        'Chemicals','StockFeeds','Tools and Equipment','Transport Costs','Others')
Labelss = ('AllSales','AllPurchases','TaxReturns')

def Calculate(entries):
    # Sales:
    r = float(entries['Cattle'].get())
    s = float(entries['Pigs'].get())
    t = float(entries['Goats'].get())
    u = float(entries['Sheep'].get())
    v = float(entries['Chickens'].get())
    x = float(entries['Other'].get())

    #Purchases

    c = float(entries['Chemicals'].get())
    d = float(entries['StockFeeds'].get())
    e = float(entries['Tools and Equipment'].get())
    f = float(entries['Transport Costs'].get())
    g = float(entries['Others'].get())
    print("r", r,"s", s,"t", t,"u", u,"v", v,"x", x,"c", c,"d", d,"e", e,"f", f,"g", g)

    # Total Sales:
    q = r + s + t + u + v + x
    Sales = q
    Sales = ("%8.2f" % Sales).strip()
    entries['AllSales'].delete(0, tk.END)
    entries['AllSales'].insert(0, Sales )
    print("AllSales: %f" % float(Sales))

    # Total Purchases
    f = c + d + e + f + g 
    Purchases = f
    Purchases = ("%8.2f" % Purchases).strip()
    entries['AllPurchases'].delete(0, tk.END)
    entries['AllPurchases'].insert(0, Purchases )
    print("AllPurchases: %f" % float(Purchases))

    # Tax Returns
    TaxReturns = (float(Sales) * 0.15) - (float(Purchases) * 0.15)
    Purchases = ("%8.2f" % TaxReturns).strip()
    entries['TaxReturns'].delete(0, tk.END)
    entries['TaxReturns'].insert(0, TaxReturns )
    print("TaxReturns: %f" % float(TaxReturns))


def makeform(root, fields):
    root.title("Tax Return Calculator")
    entries = {}
    for field in fields:
        if field == 'Cattle':
            print('Sales')
            row = tk.Frame(root)
            lab1 = tk.Label(row, width=65, text="SALES", anchor='w')
            row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
            lab1.pack(side=tk.LEFT)

        if field == 'Chemicals':
            print('Purchases')
            row = tk.Frame(root)
            lab1 = tk.Label(row, width=65, text="PURCHASES", anchor='w')
            row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
            lab1.pack(side=tk.LEFT)

        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=65, text=field+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, "0")
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[field] = ent

    for lb1 in Labelss:
        if lb1 == 'AllSales':
            print('Results')
            row = tk.Frame(root)
            lab1 = tk.Label(row, width=65, text="RESULTS", anchor='w')
            row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
            lab1.pack(side=tk.LEFT)
        print(lb1)
        row = tk.Frame(root)
        lab = tk.Label(row, width=30, text=lb1+": ", anchor='w')
        ent = tk.Entry(row)
        ent.insert(0, lb1)
        row.pack(side=tk.TOP, 
                 fill=tk.X, 
                 padx=5, 
                 pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, 
                 expand=tk.YES, 
                 fill=tk.X)
        entries[lb1] = ent


    return entries


    

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b2 = tk.Button(root, text='Calculate',
           command=(lambda e=ents: Calculate(e)))
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()