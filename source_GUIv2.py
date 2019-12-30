import tkinter as tk

fields = ('Mass of NaOH', 'uncertainty of balance', 'Volume of water in solution', 'Uncertainty of m_cylinder', 'titration value', 'absolute uncertainty')

def uncCalc(entries):
    naoh_prep_mass = float(entries['Mass of NaOH'].get())
    naoh_mass_unc = float(entries['uncertainty of balance'].get())
    naoh_vol = float(entries['Volume of water in solution'].get())
    naoh_vol_uncertainty= float(entries['Uncertainty of m_cylinder'].get())
    naoh_mol = naoh_prep_mass*(1/39.997)
    naoh_vol = naoh_vol/1000
    naoh_vol_uncertainty = naoh_vol_uncertainty/1000
    naoh_conc = naoh_mol/naoh_vol
    naoh_mol_unc = (naoh_mass_unc/naoh_prep_mass)
    naoh_mol_absunc = naoh_mol_unc*naoh_mol
    naoh_conc_unc = (naoh_mol_absunc/naoh_mol)*100+(naoh_vol_uncertainty/naoh_vol)*100
    naoh_conc_absunc = (naoh_conc_unc/100)*naoh_conc
    entries['titration value'].delete(0, tk.END)
    entries['titration value'].insert(0, str(naoh_conc) )
    entries['absolute uncertainty'].delete(0, tk.END)
    entries['absolute uncertainty'].insert(0, naoh_conc_absunc)
    print ("moles of naoh =" + str(naoh_mol), "+/-" + str(naoh_mol_unc*100) + "%")
    print ("concentration of naoh =" + str(naoh_conc) + "+/-" + str(naoh_conc_absunc))
    
    

def makeform(root, fields):
    entries = {}
    for field in fields:
        print(field)
        row = tk.Frame(root)
        lab = tk.Label(row, width=22, text=field+": ", anchor='w')
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
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    ents = makeform(root, fields)
    b1 = tk.Button(root, text='Calculate',
           command=(lambda e=ents: uncCalc (e)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Else',
           command=(lambda e=ents: uncCalc (e))) 
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    b3 = tk.Button(root, text='Quit', command=root.quit)
    b3.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()



"""
import tkinter as tk
master = tk.Tk()

def show_entry_fields1():
    naoh_mol = naoh_prep_mass*(1/39.997)
    naoh_vol = naoh_vol/1000
    naoh_vol_uncertainty = naoh_vol_uncertainty/1000
    naoh_conc = naoh_mol/naoh_vol
    naoh_mol_unc = (naoh_prep_mass_unc/naoh_prep_mass)
    naoh_mol_absunc = naoh_mol_unc*naoh_mol
    naoh_conc_unc = (naoh_mol_absunc/naoh_mol)*100+(naoh_vol_uncertainty/naoh_vol)*100
    naoh_conc_absunc = (naoh_conc_unc/100)*naoh_conc
    print ("moles of naoh =" + str(naoh_mol), "+/-" + str(naoh_mol_unc*100) + "%")
    print ("concentration of naoh =" + str(naoh_conc) + "+/-" + str(naoh_conc_unc))
def show_entry_fields():
    print("The GUI works")

tk.Label(master, text="mass of naoh pellets").grid(row=0)
tk.Label(master, text="uncertainty of weighing balance").grid(row=1)
tk.Label(master, text="water added for naoh prep volume cm3").grid(row=2)
tk.Label(master, text="measuring cylinder uncertainty").grid(row=3)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

naoh_prep_mass = str(e1) 
naoh_prep_mass_unc = str(e2)
naoh_vol = str(e3)
naoh_vol_uncertainty = str(e4)

tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=4, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Calculate', command=show_entry_fields).grid(row=4, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)


master = tk.mainloop()
"""























