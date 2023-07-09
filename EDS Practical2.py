import csv
# Read data from Sales.csv def read_csv(filename):
data = [] 
with open("Sales.csv", 'r') as file:
  reader = csv.reader(file)
next(reader) # Read the header
for row in reader: 
    data.append(row) 
# File location of Sales.csv
filename = r"C:\Users\91928\OneDrive\Desktop\New folder\Sales.csv"
# Store product details in a list 
product_details = reader.csv(filename)
# Store supplier details in a dictionary 
supplier_details = {} 
for product in product_details:
  supplier_name = product[2] # Assuming supplier name is in the third column 
  if supplier_name not in supplier_details: 
    supplier_details[supplier_name] = 0 
    supplier_details[supplier_name] += 1
# Store customer details in a tuple 
customer_details = tuple(set([product[3] for product in product_details]))
# Find the most popular product for sale
popular_product = max(product_details, key=lambda x: int(x[0].replace("P", ""))) # Assuming
most_popular_product = popular_product[1]  

# Find the best supplier for sales 
best_supplier = max(supplier_details, key=supplier_details.get)
# Find the customer who buys most of the products 
customer_purchases = {customer: 0 for customer in customer_details} 
for product in product_details:
  customer_purchases[product[3]] += 1 
  customer_most_purchases = max(customer_purchases,key=customer_purchases.get)
# Find the number of customers who are 'Female'
female_customers = sum(1 for product in product_details if product[4] == 'Female') 
# Assuming gender is in the fifth column
# Print the results 
print("Most popular product:", most_popular_product) 
print("Best supplier for sales:", best_supplier) 
print("Customer who buys most products:", customer_most_purchases) 
print("Number of female customers:", female_customers)

