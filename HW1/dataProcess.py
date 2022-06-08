import pandas as pd

# reading the csv
headers=["Price"," Maintenancecost","#ofdoors","#ofpassengers","Luggagecap",'Safetyrating',"VehicleClass"]
df=pd.read_csv('https://raw.githubusercontent.com/mpaydar/CS381/main/HW1/cars-sample35.csv',names=headers,sep=',')
print(df)