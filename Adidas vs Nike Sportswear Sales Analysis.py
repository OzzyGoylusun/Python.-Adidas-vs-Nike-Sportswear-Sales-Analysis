#!/usr/bin/env python
# coding: utf-8

# In[97]:


# Loading all libraries to be utilised

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



# Loading and merging all DataFrames and then dropping 'null' values

brands = pd.read_csv("Datasets/brands.csv") 
finance = pd.read_csv("Datasets/finance.csv")
info = pd.read_csv("Datasets/info.csv")
reviews = pd.read_csv("Datasets/reviews.csv")

merged_df = info.merge(finance, on="product_id")
merged_df = merged_df.merge(reviews, on="product_id")
merged_df = merged_df.merge(brands, on="product_id")

merged_df.dropna(inplace=True)



# In[98]:


# 1. What is the volume of products and mean revenue for Adidas and Nike products based on 
# listing price quartiles?


# Using QCut(), labeling products priced up to quartile one as "Budget", quartile two as "Average", 
# quartile three as "Expensive", and quartile four as "Elite"

price_labels = ['Budget', "Average", "Expensive", "Elite"]
merged_df['price_category'] = pd.qcut(merged_df['listing_price'], q=4, labels=price_labels)


# Doing my aggregate operations below to answer the question at hand

adidas_vs_nike = merged_df.groupby(['brand', 'price_category'])['revenue'].agg(['count','mean']).round(2)
adidas_vs_nike.rename(columns={'count':'num_products', 'mean':'mean_revenue'}, inplace=True )
adidas_vs_nike.reset_index(inplace=True)

print(adidas_vs_nike)
print('\n')


# In[99]:


# 1.1 Visualising the Adidas_vs_Nike DataFrame by mean revenue using a Seaborn Barplot

sns.set(style="whitegrid")


# Creating a grouped bar chart

plt.figure(figsize=(10, 6))
sns.barplot(x='brand', y='mean_revenue', hue='price_category', data=adidas_vs_nike, palette='viridis')

# Adding labels and title

plt.xlabel('Brand')
plt.ylabel('Average Revenue')
plt.title('Average Revenue by Price Category between Adidas and Nike')

# Adding legend

plt.legend(title='Price Category', title_fontsize='12')

# Showing the plot

plt.show()


# In[100]:


# 1.2 Visualising the Adidas_vs_Nike DataFrame by number of different products using a Seaborn Barplot

sns.set(style="whitegrid")


# Creating a grouped bar chart

plt.figure(figsize=(10, 6))
sns.barplot(x='brand', y='num_products', hue='price_category', data=adidas_vs_nike, palette='flare')

# Adding labels and title

plt.xlabel('Brand')
plt.ylabel('Number of Products Offered')
plt.title('Number of Different Products by Price Category between Adidas and Nike')

# Adding legend

plt.legend(title='Price Category', title_fontsize='12')

# Showing the plot

plt.show()


# In[101]:


# 2. Do any differences exist between the word count of a product's description and its mean rating?


# Calculating the maximum description length of character to decide the bin size

print(f"Maximum description length is currently at {max(merged_df['description'].str.len())} characters.")
print('\n')

desc_length_bins = [0, 100, 200, 300, 400, 500, 600, 700]
desc_length_labels = ['100', '200', '300', '400', '500', '600', '700']            
          


# Using Cut(), splitting product description length into bins of 100 characters, calculating the average rating 
# and number of reviews

merged_df['description_length'] = pd.cut(merged_df['description'].str.len(), bins=desc_length_bins, 
                                         labels=desc_length_labels)

df_desc_length = merged_df.groupby('description_length', as_index=False).agg({'rating':'mean',
                                                            'reviews':'count'}).round(2)

df_desc_length.rename(columns={'rating':'mean_rating', 'reviews':'num_reviews'}, inplace=True)



# Converting the description_length column from string to integer 

df_desc_length.description_length = df_desc_length.description_length.astype(int) 


# Printing the DataFrame in question

print(df_desc_length)


# In[102]:


# 2.1 Visualising the correlation between description length and mean rating of each product 
# using a Seaborn Regression Plot


# Calculating correlation coefficient

correlation_coefficient = np.corrcoef(df_desc_length.description_length, df_desc_length.mean_rating)[0, 1]

# Creating a scatter plot with a regression line

plt.figure(figsize=(8, 6))
sns.regplot(x=description_length, y=mean_rating, data=df_desc_length, color='green', scatter_kws={'s': 50})

plt.title(f'Scatter Plot with Correlation Line (Correlation Coefficient: {correlation_coefficient:.2f})')
plt.xlabel('Description Length')
plt.ylabel('Mean Rating')

plt.show()


# In[103]:


# 3. How does the volume of products and median revenue vary between clothing and footwear?


# Listing footwear keywords to search the description column for any of these keywords

footwear_keyword = "shoe*|trainer*|foot*"


# Filtering for footwear products

shoes_df = merged_df[merged_df['description'].str.contains(footwear_keyword)]
footwear_filter = list(shoes_df['product_id'])


# Filtering for clothing products

clothing_df = merged_df[~merged_df.isin(footwear_filter)] #It still returns all, but non-matching ones get null
clothing_df.dropna(inplace=True)


# Creating our final footwear_vs_clothing DataFrame and printing the result stored in another DataFrame

final_df_footwear_vs_clothing = pd.DataFrame({'num_clothing_products': len(clothing_df),
                             'median_clothing_revenue': clothing_df['revenue'].median(),
                             'num_footwear_products': len(shoes_df),
                             'median_footwear_revenue': shoes_df['revenue'].median()},
                            index=[0])

print(final_df_footwear_vs_clothing)


# In[104]:


# 3.1 Visualising the final_df_footwear_vs_clothing DataFrame using a Seaborn Barplot


# Making a copy of our final_df_footwear_vs_clothing DataFrame in a new DataFrame

copy_of_final_data = {
    'Category': ['Clothing', 'Footwear'],
    'Num_Products': [478, 2639],
    'Median_Revenue': [625.07, 3073.3]
}

df = pd.DataFrame(copy_of_final_data)


# Setting up the matplotlib figure

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

# Bar plotting for number of different products

sns.barplot(x='Category', y='Num_Products', data=df, ax=axes[0], palette='pastel')
axes[0].set_title('Total Number of Different Products Sold')
axes[0].set_ylabel('Number of Products')

# Bar plotting for median revenue

sns.barplot(x='Category', y='Median_Revenue', data=df, ax=axes[1], palette='pastel')
axes[1].set_title('Total Median Revenue Generated')
axes[1].set_ylabel('Median Revenue')

# Adjusting layout

plt.tight_layout()

# Showing the plots

plt.show()

