import pandas as pd

df=pd.read_csv('retail_sales_dataset.csv')
print(df)
print(df.columns)
print(df.head())
#Calculate the total revenue generated from all transactions.
total_amount=df['Total Amount']
total_sales=total_amount.sum()
print(total_sales)
#What is the average Total Amount per transaction?
average_total_amount=total_amount.mean()
print(average_total_amount)
#What is the median Total Amount?
median_total_amount=total_amount.median()
print(median_total_amount)
#What is the highest Total Amount from a single transaction?
maximum_total_amount=total_amount.max()
print(maximum_total_amount)
#How many unique customers are represented in the dataset?
customers=df['Customer ID']
unique_customer=customers.nunique()
print(unique_customer)
#Part 2: Grouping by One Column
#Calculate the total sales for each gender.
gender_df=df.groupby('Gender')
grouped_gender_sales_df=gender_df.agg(
    total_sales_by_gender=('Total Amount','sum')
)
grouped_gender_sales_df=grouped_gender_sales_df.reset_index()
print(grouped_gender_sales_df)
#Calculate the average Total Amount for each gender.
grouped_gender_avg_sales_df=gender_df.agg(
    average_gender_amount=('Total Amount','mean')
)
grouped_gender_avg_sales_df=grouped_gender_avg_sales_df.reset_index()
print(grouped_gender_avg_sales_df)
#Calculate the total quantity sold for each Product Category.
product_cat_df=df.groupby('Product Category')
quantity_sold_product=product_cat_df.agg(
    total_quantiy_sold=('Quantity','sum')
)
quantity_sold_product=quantity_sold_product.reset_index()
print(quantity_sold_product)
#Calculate the total sales for each Product Category.
sales_product_category=product_cat_df.agg(
    total_per_product_category=('Total Amount','sum')
)
sales_product_category=sales_product_category.reset_index()
print(sales_product_category)
#Count the number of transactions for each product category.
count_num_transaction=product_cat_df.agg(
    number_of_transations=('Transaction ID','count')
)
count_num_transaction=count_num_transaction.reset_index()
print(count_num_transaction)
#Multiple Grouping Columns
#Calculate the total sales for each combination of:Gender,Product Category
#Calculate the average Total Amount for each combination 
gender_product_category=df.groupby(['Gender','Product Category']).agg(
    total_sales_of_gandp=('Total Amount','sum'),
    avg_total_of_gandp=('Total Amount','mean')
).reset_index()
print(gender_product_category)

