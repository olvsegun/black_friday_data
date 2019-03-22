# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:11:36 2019

@author: shale
"""
#import relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#import dataset as a dataframe

df= pd.read_csv('BlackFriday.csv')

#check the shape of our dataset, head, and info as well as columns list

df.shape
df.head()
df.info()
df.columns

#Looks like there a lot of missing numbers in certain columns
#Also, there seems to be some columns that should be labelled categorical datatype

df[['Gender','Age', 'Occupation','City_Category', 'Marital_Status']]= df[['Gender','Age', 'Occupation','City_Category', 'Marital_Status']].astype('category')
df.info()
df.isnull().any()

#the missing data are in the product_category_2 and product_category_3. we need to fill the missing data 
df[['Product_Category_2', 'Product_Category_3']]= df[['Product_Category_2', 'Product_Category_3']].fillna(value=0)
df.isnull().any()

#Now we have our data ready for analysis. we need to decide what our exploration would be like
#in terms of gender, who is more likely to shop on black friday
#what age group are likely to shop on black friday
#does marital status affect black friday interest in people?
#what product category are people likely to buy on black friday
#Does the city affect the black friday sale?
#Now we have all our question, let us get to work and try to answer these questions.

#first all, who is more interested in black friday, male or female.
#I am going to be grouping by user_id as this is duplicated in the data. hence we have one person buying more than one product on black friday
df.groupby(['Gender'])['User_ID'].count()



#Now let us explore who is more interested, male or female.
sns.countplot(df['Gender'])
#looks like there were more male than female shopping on blackfriday

sns.countplot(df['Age'])
sns.countplot(x = df['Age'], hue = df['Gender'])
#Male between 26-35 years shopped more on this day than any age group, and there were more male than female in all age categories.
#We need to look at the product category as that would tell us what they bought most or what they are interested in
#but before then, let us see the marital status distribution between the genders shoppping
sns.countplot(df['Marital_Status'])
sns.countplot(df['Marital_Status'], hue= df['Gender'])



#There were more single people than married people shopping on black Friday in both gender. Is there a product that these particular group are buying more than unmarried and more male are buying than female?
#But again how is this distributed in the age groups
sns.countplot(df['Age'], hue= df['Marital_Status'])

#This ha not highlighted any surprising trend as we expect the distribution that was observed.
#let us look at the product categories.
sns.countplot(df['Product_Category_1'])
sns.countplot(df['Product_Category_2'])
sns.countplot(df['Product_Category_2'])
#The category 0 which is for missing data overshadowed the rest of the categories, so it was excluded
sns.countplot(df['Product_Category_3'][df['Product_Category_3'] > 0])
sns.countplot(df['Product_Category_2'][df['Product_Category_2'] > 0])
#in product category 1, category 5 was the most bought product category followed closely by 1 then 8
#in product category 2, category 8 was most puirchased and a cluster of categories 14 to 16
#in product category 3, category 16 was most purchased.
#let us see how the the genders bought this categories

sns.countplot(x= df['Product_Category_1'], hue =df['Gender'])
sns.countplot(x= df['Product_Category_2'][df['Product_Category_2'] > 0], hue =df['Gender'])
sns.countplot(x= df['Product_Category_3'][df['Product_Category_3'] > 0], hue =df['Gender'])

#For all product categories, there were more purchase by male than female. If we know the product categories then we can discuss further on why that is the case

#Let us explore who are those likely to spend on black Friday, new or old residents of the cities.
sns.countplot(x = df['Stay_In_Current_City_Years'])
#new residents of the city spent more on Black Friday than old resident. What about the age group. What age groups fall in these categories of length of stay
sns.countplot(x = df['Stay_In_Current_City_Years'], hue = df['Age'])

#So far, we know that our taeget group would have to be young people between the age of 26-35
#we also need to check if these age group had more purchase in terms of revenue.
df.groupby('Age')['Purchase'].sum()
df.groupby('Age')['Purchase'].sum().plot(kind = 'bar')
plt.ylabel('Purchase in $')

#What is the average purchase per occupation?
df.groupby('Occupation')['Purchase'].mean().plot(kind = 'bar')
plt.ylabel('Average Purchase ($)')