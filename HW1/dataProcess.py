import pandas as pd

# reading the csv
headers=["Price"," Maintenancecost","#ofdoors","#ofpassengers","Luggagecap",'Safetyrating',"VehicleClass"]
df=pd.read_csv("https://raw.githubusercontent.com/mpaydar/CS381/main/HW1/cars-sample35.csv",names=headers)
price=[]
maintenance=[]
doors=[]
passengers=[]
luggage=[]
safetyRating=[]
vehicle=[]



price=df['Price'].tolist()
maintenance=df[' Maintenancecost'].tolist()
doors=df['#ofdoors'].tolist()
passengers=df['#ofpassengers'].tolist()
luggage=df['Luggagecap'].tolist()
safetyRating=df['Safetyrating'].tolist()
vehicles=df['VehicleClass'].tolist()

print(len(price))

priceIndexes = [p for p in range(len(price)) if price[p]=='med']
print(priceIndexes)





# price =[print(p) for p in range(len(price)) if p=='med']
# print(price)



# maintenance=[m for m in maintenance ]
# print(maintenance)
