import pandas as pd

# Sample DataFrame with a categorical field
data = {'Cricketer': ['Virat Kohli', 'MS Dhoni', 'AB De Villers', 'Glenn Maxwell']}

df = pd.DataFrame(data)
df_original = df.copy()

# Mapping categorical values to numerical categories
# Creating a mapping dictionary
mapping = {'Virat Kohli': 18, 'MS Dhoni': 7, 'AB De Villers': 17,'Glenn Maxwell':43}

# Replacing categorical values with numerical categories
df['Jersey Number'] = df['Cricketer'].map(mapping)

print("Original DataFrame:")
print(df_original)

print("\nReexpressed DataFrame:")
print(df)