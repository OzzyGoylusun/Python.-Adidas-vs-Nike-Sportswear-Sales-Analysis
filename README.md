# Adidas vs Nike Sportswear Sales Analysis

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

This data analysis project is designed to assist an online sports clothing company particularly with increasing its revenue by making comparisons between sportswear products of Adidas and Nike brands. It also aims at looking into the total volume of products and median revenue between clothing and footwear.

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Adidas%20%26%20Nike.png"  alt="Online Sportswear Shop" width="400">
</p>

Given that sports clothing is a giant sector by its own, worth nearly **$193 billion in 2021***, also having strong growth predictions on its side for the next decade, this analysis highlights the importance of continously paying close attention to the growing data that the online firm maintains to grow the business.


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

1. What is the volume of products and average revenue for Adidas and Nike products based upon listing price quartiles classified by four pre-determined tags (e.g., Budget, Elite)?
2. Do there any differences exist between the word count of a product's description and its mean rating?
3. How does the volume of products and median revenue vary between clothing and footwear?


### Data Analysis

```python

```

### Findings

The critical analysis results are summarised as follows:

1. There is a massive gap in both mean revenue and number of products sold across all budget categories between Adidas and Nike products, as shown below:

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Mean%20Revenue%20by%20Price%20Category%20between%20Adidas%20and%20Nike.png" alt="Mean Revenue by Price Category between Adidas and Nike" width='600'>
  
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Number%20of%20Different%20Products%20by%20PC.png" alt="No of Products by Price Category between Adidas and Nike" width='600'>
</div>

2. The online shop has produced the highest average revenue via **Adidas Elite** items also by selling those products that are 50% higher than the average number of products being sold.

3. 
4. In this respect, all Adidas products have achieved a whopping **350% higher mean revenue** compared to its Nike counterparts.
5. It was rather interesting to note that the higher description length a product has, the higher online rating it has achieved by online customers.
6. Both the volume (number) of and the median revenue for **footwear products** are significantly higher than the equivalent parameter values for clothing products.

<p align="center">
  <img src="https://github.com/OzzyGoylusun/Python.-Adidas-vs-Nike-Sportswear-Sales-Analysis/blob/main/Visuals/Comparison%20of%20Figures%20between%20Footwear%20and%20Clothing.png" alt="Comparison of Figures between Footwear and Clothing" width='700'>
</p>


### Recommendations

Based on the findings above, I propose the following recommendations:

1. 


### Limitations

- The accuracy of the findings and effectiveness of the proposed suggestions are inherently limited by the quality of the datasets provided.
- It is unknown as to the recency of all the data due to the lack of datetime-related information in the datasets.


### References

1. [DataCamp](https://www.datacamp.com/)
2. [Statista: Forecast revenue of the global sports apparel market from 2023 to 2030](https://www.statista.com/statistics/254489/total-revenue-of-the-global-sports-apparel-market/)
