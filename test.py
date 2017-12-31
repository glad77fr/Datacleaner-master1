
import pandas as pd
a=4
if a==4 :
    print('cool')
else:
    print('Pas cool')

def afficher(p):
    return print(p)

afficher('toto')

def fonction(didi,parameter):
    return didi(parameter)

fonction(afficher,'Serge')
#df['Nom'][0].str.count()


#print(df['Prénom'].get_loc('Julie')

#print(df['Prénom'].str.contains('Julie'))
#print(df['Prénom'].str.find('Julie'))
#a = df[df['Prénom']=='Julie']

#print(a)

#df['count'] = map(lambda x: x.count("1"), df['Quarters'])


#print(df['Nom'].value_counts())
# df = xls_file.parse('Feuil1')
# for cel in df['Nom']:
# if cel[0] == 'A':
# print(cel)

# wb = Workbook()

# root = tk.Tk()
# root.withdraw()  # pour ne pas afficher la fenêtre Tk

# path = askopenfilename()  # lance la fenêtre et recupère le chemin

# wb = load_workbook(path)
# ws = wb.active

# c = ws['B3']
