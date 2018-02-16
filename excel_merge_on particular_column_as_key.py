import pandas as pd

df = []
 final = "final.xlsx" #where you want to save the data
#For reading the sheet
for f in ['merge.xlsx']:
	df1 = pd.read_excel(f, 'Sheet 1') #give the exact sheet name
	df2 = pd.read_excel(f, 'Sheet 2') #give the exact sheet name

#For reading the separate excel
'''
df1 = pd.read_excel('dataPart1.xlsx')
df2 = pd.read_excel('dataPart2.xlsx')
'''
df=pd.merge(df1,df2, on='Symbol')
df.to_excel(final)