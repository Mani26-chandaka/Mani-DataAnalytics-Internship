import pandas as pd
df = pd.read_excel(r"c:\Users\manic\OneDrive\Desktop\Task 1-Data Immersion&Wrangling\data.csv.xlsx") 
# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Handle missing values
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Feature engineering: tenure groups
df['TenureGroup'] = pd.cut(df['tenure'],
                           bins=[0,12,24,36,48,60,72],
                           labels=['0-12','13-24','25-36','37-48','49-60','61-72'])
df.to_csv("cleaned_data.csv", index=False)
