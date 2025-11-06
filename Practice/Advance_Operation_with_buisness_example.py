import numpy as np #Allows us to create array of the given data and perform operations
import matplotlib.pyplot as plt   #Allows us to plot the data from the given matrix
# Data structure: [restaurant_id, 2021, 2022, 2023, 2024] 

sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani ---> NAME OF THE RESTRAUNT
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites ---> NAME OF THE RESTRAUNT
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub ---> NAME OF THE RESTRAUNT
    [4, 180000, 210000, 240000, 270000],  # Burger Point ---> NAME OF THE RESTRAUNT
    [5, 160000, 185000, 205000, 230000]   # Chai Point ---> NAME OF THE RESTRAUNT
])

print("\n<================================ZOMATO SALES ANALYSIS=================================================>\n")
print("\nShape of the Sales Data ARRAY :",sales_data.shape)
print("\n<=================================================================================>\n")
#Printing the sales for the first 3 restraunts :
print("THE SALES DATA OF THE FIRST 3 RESTRAUNTS IS :\n",sales_data[:3])
print("\n<=================================================================================>\n")
#printing the Total sales per year :
print("\nTOTAL SALES PER YEAR FOR EACH RESTRAUNT IS :\n",np.sum(sales_data[:, 1:],axis=1))
print("\n<=================================================================================>\n")
#printing the minimum sales for each restraunt :
print("\nTHE MINIMUM SALES FOR EACH RESTRAUNT IS :\n",np.min(sales_data[:, 1:],axis=1))
print("\n<=================================================================================>\n")
#printing the maximum sales for each restraunt :
print("\nTHE MAXIMUM SALES FOR EACH RESTRAUNT IS :\n",np.max(sales_data[:, 1:], axis=0))
print("\n<=================================================================================>\n")
#printing the average sales for eaach restraunt :
print("\nTHE AVERAGE SALES FOR EACH OF THE RESTRAUNTS IS :\n",np.mean(sales_data[:, 1:],axis=1))
print("\n<=================================================================================>\n")

#printing the cumulative sales :
cumulative_sales=np.cumsum(sales_data[:, 1:],axis=1)
print("\nTHE CUMULATIVE SALES FOR THE GIVEN DATA IS :\n",cumulative_sales)
print("\n<=================================================================================>\n")

#printing the monthly average :
monthly_avg = sales_data[:, 1:] / 12
print("\n<=================================================================================>\n")
print("\nTHE Monthly Average of the Sales is :\n",monthly_avg)
print("\n<=================================================================================>\n")

#Plotting a graph to Examine the Cumulative Sales :
plt.figure(figsize=(8,6))
plt.plot(np.mean(cumulative_sales,axis=0))
plt.title("Avg Cumulative sales across all the restraunts")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()



