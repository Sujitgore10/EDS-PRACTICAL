
import pandas as pd 
df=pd.read_csv('grainsales.csv') 
print(df)
# 1. Which was the best month for sales? How much was earned that month?
import pandas as pd 
df=pd.read_csv('grainsales.csv')
bms=df.groupby('Months')['Sales'].sum().idxmax()
bmsa=df.groupby('Months')['Sales'].sum().max()
print("The Best Months for Sale is :",bms,"And the Total Sales Amount is:",bmsa)
# 2. Which product sold the most? Why do you think it did?
mps=df.groupby('GrainName')['Sales'].sum().idxmax()
mpsa=df.groupby('GrainName')['Sales'].sum().max()
print("The product sold the most:",mps,"And the total sale amount is:",mpsa)
# 3. Which city sold the most products?
mpsc=df.groupby('City')['Sales'].sum().idxmax() 
mpsca=df.groupby('City')['Sales'].sum().max()
print("The city sold the most product:",mpsc,"And the total sale amount is:",mpsca)
# 4. What products are most often sold together?
product_combinations = df.groupby('City')['GrainName'].apply(lambda x: ', '.join(x.unique()[:2]))
print("Products Most Often Sold Together:",product_combinations)