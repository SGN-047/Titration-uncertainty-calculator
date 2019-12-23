print ("ligma aldrich acid base titration uncertainty propogation calculator")

#moles of naoh 
naoh_prep_mass = float(input("mass of naoh pellets = "))
naoh_prep_mass_unc = float(input("uncertainty of weighing balance = "))
naoh_mol = naoh_prep_mass*(1/39.997)
naoh_mol_unc = (naoh_prep_mass_unc/naoh_prep_mass)
print ("moles of naoh =", naoh_mol, "+/-", naoh_mol_unc*100, "%")

naoh_mol_absunc = naoh_mol_unc*naoh_mol
print ("moles of naoh =", naoh_mol, "+/-", naoh_mol_absunc)

#naoh conc calc
naoh_vol = float(input("water added for naoh prep volume cm3 = "))
naoh_vol = naoh_vol/1000
naoh_vol_uncertainty= float(input("measuring cylinder uncertainty = "))
naoh_vol_uncertainty = naoh_vol_uncertainty/1000
naoh_conc = naoh_mol/naoh_vol
naoh_conc_unc = (naoh_mol_absunc/naoh_mol)*100+(naoh_vol_uncertainty/naoh_vol)*100
print ("concentration of naoh =", (naoh_conc), "+/-", (naoh_conc_unc) )

naoh_conc_absunc = (naoh_conc_unc/100)*naoh_conc
print ("concentration of naoh =", naoh_conc, "+/-", naoh_conc_absunc) 
