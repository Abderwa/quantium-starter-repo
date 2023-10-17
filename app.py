import pandas as pd

df = pd.concat(
    map(pd.read_csv, ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']), ignore_index=True)


df["price"] = df["price"].str.replace("$", "").astype(float)
df['sales'] = df['quantity'] * df['price']
sales = df[(df['product'] == 'pink morsel')]
#result = df.dtypes

df1 = df[['sales', 'date', 'region']]
print(df1)
df1.to_csv('sales_data.csv')

