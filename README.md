# Adidas vs Nike Sportswear Product Sales Analysis

## Table of Contents

- [Data Analysis](#data-analysis)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Findings](#findings)

### Project Overview
---
<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Wars-Sales-Analysis/blob/main/Visuals/Online%20Sportswear%20Shop.png"
 alt="Online Sportswear Shop">
</p

This data analysis project is designed to assist an online sports clothing company particularly with increasing its revenue by making comparisons between Adidas and Nike-branded sportswear products that it sells. The analysis also looks into the total volume of products and median revenue between clothing and footwear-type items.

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Adidas%20%26%20Nike.png"  alt="Online Sportswear Shop" width="400">
</p>

Given that sports clothing is a giant sector by its own, worth nearly **$193 billion in 2021***, also having strong growth predictions on its side for the next decade, this analysis aims at highlighting the importance of continously paying close attention to the growing data that the online firm maintains to further expand the business at the maximum capacity possible.


### Data Sources

There were four fundamental datasets harnessed for this analysis:

- brands.csv
- finance.csv
- info.csv
- reviews.csv
  

### Tools

- [Anaconda Navigator: ](https://www.anaconda.com/download)
  - To access the Jupyter Notebook for **Python**


### Data Preparation

No data preparation tasks were required as all the data provided had already been cleaned out prior.



### Exploratory Data Analysis

By analysing all the four datasets, EDA sought to answer the following key questions:

1. What are the volume of distinct products and average revenue for Adidas and Nike-branded items, based upon listing price quartiles to be classified by four pre-determined tags (i.e., Budget, Average, Expensive, Elite)?
2. Does there any correlation exist between the word count of a product's description and its mean rating?
3. How do the volume of distinct products and median revenue vary between clothing and footwear-type items?


### Data Analysis

What challenged me most was that when I needed to separate footwear products of both brands from their clothing counterparts, I first created a keyword in the form of a string and then subset all appropriate rows of our main DataFrame based on that condition.

Afterwards, I created a counter DataFrame that shall retain all data whose product IDs are not found in our first subset DataFrame, in order to be able to separate both types of sportswear from one another.

```python
footwear_keyword = "shoe*|trainer*|foot*"

# Filtering for footwear products

shoes_df = merged_df[merged_df['description'].str.contains(footwear_keyword)]
footwear_filter = list(shoes_df['product_id'])

# Filtering for clothing product

clothing_df = merged_df[~merged_df.isin(footwear_filter)] #It still returns all, but non-matching ones get null
clothing_df.dropna(inplace=True)
```

### Findings

The critical analysis results are summarised as follows:

1. There is an astronomical gap in both average revenue and number of distinct products sold across all price categories between Adidas and Nike-branded items, as shown below:

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Mean%20Revenue%20by%20Price%20Category%20between%20Adidas%20and%20Nike.png" alt="Mean Revenue by Price Category between Adidas and Nike" width='600'>
</p>

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Number%20of%20Different%20Products%20by%20PC.png" alt="No of Products by Price Category between Adidas and Nike" width='600'>
</p>

2. Adidas products have achieved a whopping **350% higher mean revenue** compared to its Nike counterparts.
3. It was determined that the longer description length a particular product has, the higher online rating it has achieved, attributed by the firm's online customers.
   The scatterplot below demonstrates that there is a strong correlation between these two variables:

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Correlation%20Between%20Desc%20Length%20and%20Mean%20Rating.png" alt="Correlation between Description Length and Mean Rating of a Product" width='600'>
</p>
  
4. Both the volume (number) of and the median revenue for **footwear products** are, irrespective of the brand, significantly higher than the equivalent parameter values for clothing products.

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Comparison%20of%20Figures%20between%20Footwear%20and%20Clothing.png" alt="Comparison of Figures between Footwear and Clothing" width='700'>
</p>


### Recommendations

Based on the findings above, I propose the following recommendations for the firm to put itself in a better position to begin increasing its revenue: 

1. Shift the focus toward offering more Nike products to customers, particularly from the Budget and Elite categories, seeing that the larger product variety appears to have **a positive correlation with achieving higher revenue.**
2. Continue to offer Adidas products of all categories to maintain the elevated levels of mean revenue from this brand.
3. Undertake e-commerce customer research in an attempt to unearth the root cause(s) of the strong correlation between the long description length of products and product ratings.
4. Consider introducing significantly higher number of clothing products by bringing the ratio of difference between clothing vs footwear-type items to 1:2 (i.e., %50 percent). The same ratio currently stands at 1:5.


### Limitations

- The accuracy of the findings and effectiveness of the proposed suggestions are inherently limited by the quality of the datasets provided.
- Please note that our merged DataFrame retains information of aggregated sales data for each particular product. 
- It is unknown as to the recency of all the data due to the lack of datetime parameter in the datasets.


### References

1. [DataCamp](https://www.datacamp.com/)
2. [Statista: Forecast revenue of the global sports apparel market from 2023 to 2030](https://www.statista.com/statistics/254489/total-revenue-of-the-global-sports-apparel-market/)
3. [Seaborn: Regression Plot](https://seaborn.pydata.org/generated/seaborn.regplot.html)
