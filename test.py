import pandas as pd
# Create a Pandas dataframe from some data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
#writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
#df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
#writer.save()
print(df.iloc[0,0])
df.at[0, 'Data'] = 40
print(df.iloc[0,0])
#print(df)



didi = ()


a = 2

if a == 2:
    print("cool")
else:
    print("pas cool")

def test(a):
    if a == 1:
        return False


if test(1) is False:
    print('False')




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
