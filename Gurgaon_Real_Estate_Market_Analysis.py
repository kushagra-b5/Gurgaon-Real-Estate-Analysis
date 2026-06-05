import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
df = pd.read_csv("Real_Estate_DATA.csv")


#-------------------------------------------------------------------------


# Data Cleaning


df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')   

# Numeric columns: 'price' , 'rate_per_sqft'

df['price'] = df['price'].str.replace(',', '').astype(float)  
df['rate_per_sqft'] = df['rate_per_sqft'].str.replace(',', '').astype(int)  



# Categorical columns:  'status' , 'rera' , 'flat_type'

df['status'] = df['status'].str.strip().str.lower()  
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})  
df['flat_type'] = df['flat_type'].str.strip().str.lower()


df=df.drop_duplicates()


#-------------------------------------------------------------------------


# Answering Business Questions with Analysis
# Exploratory Data Analysis (EDA)


# Question 1: Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print("Costliest Flat Details:")
print(costliest_flat)



# Question 2: Which locality has the highest average price?
locality_avg_price = df.groupby('locality')['price'].mean().sort_values(ascending=False)
print("\nLocality with the Highest Average Price:")
print(locality_avg_price.head(1))



# Question 3: Which locality has the highest rate per square foot?
locality_avg_rate = df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False)
print("\nLocality with the Highest Average Rate per Square Foot:")
print(locality_avg_rate.head(1)) 



# Question 4: Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean() 
if ready_to_move_avg_price > under_construction_avg_price:
    print("\nReady-to-move properties cost more on average.") 
else:    
    print("\nUnder-construction properties cost more on average.")



# Question 5: Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
if rera_approved_avg_price > not_rera_approved_avg_price:
    print("\nRERA-approved properties command a price premium on average.")
else:    
    print("\nRERA-approved properties do not command a price premium on average.")


 
# Question 6: How does area (sqft) impact property price?
sns.scatterplot(x='area', y='price', data=df)
plt.title('Area (sqft) vs Price')
plt.xlabel('Area (sqft)')
plt.ylabel('Price') 
plt.show()



# Question 7: Which BHK configuration is the most expensive on average based on per square foot rate
bhk_avg_rate = df.groupby('bhk_count')['rate_per_sqft'].mean().sort_values(ascending=False)
print("\nBHK Configuration with the Highest Average Rate per Square Foot:")
print(bhk_avg_rate.head(1))



# Question 8: Which property type (Apartment, Floor, Plot) is the costliest?
property_type_avg_price = df.groupby('flat_type')['rate_per_sqft'].mean().sort_values(ascending=False)
print("\nCostliest Property Type:")
print(property_type_avg_price.head(1))



# Question 9: Do certain builders or companies consistently price higher?
company_avg_price = df.groupby('company_name')['rate_per_sqft'].mean().sort_values(ascending=False)
print("\nCompanies with the Highest Average rate per Square Foot:")
print(company_avg_price.head(5))

# Question 10: Are larger homes always more expensive per square foot?
sns.scatterplot(x='area', y='rate_per_sqft', data=df)
plt.title('Area (sqft) vs Rate per Square Foot')
plt.xlabel('Area (sqft)')
plt.ylabel('Rate per Square Foot')  
plt.show()