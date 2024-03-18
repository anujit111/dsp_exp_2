import pandas as pd
#Load the dataset
cars_df = pd.read_csv('cars.csv')

print("Q1: Find all Null Values in the dataset. If there is any null value in any column, fill it with the mean of that column. \n")
cars_df.fillna(cars_df.mean(), inplace=True)

print("Q2: Check what are the different types of Make are there in our dataset. And, what is the count (occurrence) of each Make in the data? \n")
make_counts = cars_df['Make'].value_counts()
print("Different types of Make and their occurrence count:")
print(make_counts)

print("Q3: Show all the records where Origin is Asia or Europe. \n")
asia_europe_cars = cars_df[cars_df['Origin'].isin(['Asia', 'Europe'])]

print("Q4: Remove all the records (rows) where Weight is above 4000.\n")
cars_df = cars_df[cars_df['Weight'] <= 4000]

print("Q5: Increase all the values of 'MPG_City' column by 3.\n")
cars_df['MPG_City'] += 3

print("Display the modified dataframe ")
print("Modified DataFrame:")
print(cars_df)