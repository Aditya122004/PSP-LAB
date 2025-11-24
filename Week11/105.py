import pandas as pd

file_path = "Restaurant_Reviews.tsv"

df = pd.read_csv(file_path,sep='\t')

print(df.head())

print(df.info())

