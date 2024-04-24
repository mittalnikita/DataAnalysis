import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
# print(df)        # To see the whole dataframe
# print(df.head(20))   # it is used to see the uppermost 20 rows of the dataframe
# print(df.info())    # To get the desription of the content of the dataframe

# Now as we can see here the info of all the attributes of our table and there are two 
# columns which have no values so we should delete that ---> Data Mining

df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
# print(df.info())

# if we want to check the null values
# print(pd.isnull(df))
# print(pd.isnull(df).sum())

# To drop all the null values
df.dropna(inplace = True)
# print(pd.isnull(df).sum())

# # for example
# dummy_data = [['Nikita', 22], ['Nikita', 23], ['Parminder', ], ['Payal', 25]]
# dummy_df = pd.DataFrame(dummy_data, columns=['Name', 'Id'])
# print(dummy_df)
# dummy_df.dropna(inplace = True)  # To delete permanently use inplace
# # OR to temporarily delete and store that deleted in other df
# # new_dummy_df = dummy_df.dropna()
# print(pd.isnull(dummy_df).sum())


#  If you want to change the datatype of any column

df['Amount'] = df['Amount'].astype('int')
# print(df['Amount'].dtypes)

# to see the columns list
# print(df.columns)

# to rename any column temporarily
# print(df.rename(columns = {'Occupation' : 'Profession'}))

# returns the description of all the numerical columns
# print(df.describe())

# for specific columns
# print(df[['Age', 'Orders', 'Amount']].describe())


## Exploratory Data Analysis


## GENDER
# ax = sns.countplot(x = 'Gender', data = df)

# for bars in ax.containers:  ## for counting the bove data
#     ax.bar_label(bars) 

# plt.show()

# sales_gen = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
# sns.barplot(x = 'Gender', y = 'Amount', data = sales_gen)
# plt.show()

## from above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men


## AGE GROUP
# ay = sns.countplot(x = 'Age Group', data= df, hue = 'Gender')
# for bars in ay.containers:
#     ay.bar_label(bars)
# plt.show()

## Total amount vs Age Group
# sales_age = df.groupby(['Age Group'], as_index = False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
# sns.barplot(x = 'Age Group', y = 'Amount', data = sales_age)
# plt.show()

## from above graphs we can see that most of the buyers are of age group between 26-35 years


## STATE

# # total number of orders from top 10 states

# sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

# sns.set(rc={'figure.figsize':(18,5)})
# sns.barplot(data = sales_state, x = 'State',y= 'Orders')
# plt.show()

# # total amount/sales from top 10 states

# sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

# sns.set(rc={'figure.figsize':(18,5)})
# sns.barplot(data = sales_state, x = 'State',y= 'Amount')
# plt.show()

## From the above graphs we can see most of the orders and total sales/amount are from Uttar Pradesh, Maharastra, Karnataka respectively


## MARITAL STATUS

# bx = sns.countplot(data = df, x = 'Marital_Status')

# sns.set(rc={'figure.figsize':(7,5)})
# for bars in bx.containers:
#     bx.bar_label(bars)
# plt.show()

# sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

# sns.set(rc={'figure.figsize':(6,5)})
# sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
# plt.show()

## from above graphs we can see that most of the buyers are married women and they have high purchasing power


## OCCUPATION

# sns.set(rc={'figure.figsize':(20,5)})
# cx = sns.countplot(data = df, x = 'Occupation')

# for bars in cx.containers:
#     cx.bar_label(bars)
# plt.show()

# sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

# sns.set(rc={'figure.figsize':(20,5)})
# sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')
# plt.show()

## Most of the buyers are working in IT, healthcare and activation sector


## PRODUCT CATEGORY

# sns.set(rc={'figure.figsize':(20,5)})
# ax = sns.countplot(data = df, x = 'Product_Category')

# for bars in ax.containers:
#     ax.bar_label(bars)
# plt.show()

# sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

# sns.set(rc={'figure.figsize':(20,5)})
# sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')
# plt.show()

## Most of the sold products are from food, clothing and electronic category

# sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

# sns.set(rc={'figure.figsize':(20,5)})
# sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')
# plt.show()

# ## OR
# ##  top 10 most sold products (same thing as above)

# fig1, ax1 = plt.subplots(figsize=(12,7))
# df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
# plt.show()