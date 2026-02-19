import pandas as pd
df = pd.read_csv(r"C:/Users/samiy/OneDrive/Desktop/sales_data_sample.csv", encoding="latin-1")
print(df.head())
df  = df.drop_duplicates()  #remove duplicate rows
df = df.fillna(0)  #replace missing values with 0
print(df.head()) #check the cleaned data
print(df.columns)
print(df.groupby("PRODUCTLINE")["SALES"].sum())#👉 Total sales by product line
print(df.groupby("COUNTRY")["SALES"].sum()) #👉 Total sales by countrys
print(df.groupby("YEAR_ID")["SALES"].sum()) #👉 Total sales by year
print(df.groupby("STATUS")["ORDERNUMBER"].count()) #👉 Total orders by status
print(df.groupby("DEALSIZE")["SALES"].sum())#👉 Sales by deal size
df.to_csv("cleaned_sales_data.csv", index=False)






