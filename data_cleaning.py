#%%
from numpy import float64
import pandas as pd

#%%
df = pd.read_csv('clean_test.csv', delimiter=',')

#%%
pd.read_csv('clean_test.csv')

#%%
print(len(df))

#%%
# Renaming unnamed column to ID
df.rename(columns={'Unnamed: 0':'ID'}, inplace=True )

# %%
df.head()

# %%
# Removing \n
df['Family'] = df['Family'].str.replace('Family\n','')
df['Genus'] = df['Genus'].str.replace('Genus\n','')
df['PlantRange'] = df['PlantRange'].str.replace('Plant range\n','')
df['Foliage'] = df['Foliage'].str.replace('Foliage\n','')
df['Habit'] = df['Habit'].str.replace('Habit\n','')
df['Hardiness'] = df['Hardiness'].str.replace('Fragrance\n','')
df['Hardiness'] = df['Hardiness'].str.replace('Toxicity\n','')
df['Cultivation'] = df['Cultivation'].str.replace('Cultivation\n', '')
df['Propagation'] = df['Propagation'].str.replace('Propagation\n', '')
df['SuggestedPlantingLocation'] = df['SuggestedPlantingLocation'].str.replace('Suggested planting locations and garden types\n', '')
df['Pruning'] = df['Pruning'].str.replace('Pruning\n', '')
df['Pests'] = df['Pests'].str.replace('Pests\n', '')
df['Diseases'] = df['Diseases'].str.replace('Diseases\n', '')
df['Exposure'] = df['Exposure'].str.replace('Exposure\n', '')
df['Aspect'] = df['Aspect'].str.replace('Aspect\n', '')
df['Sunlight'] = df['Sunlight'].str.replace('\n', '')
df['Soil'] = df['Soil'].str.replace('\n', '')
df['Moisture'] = df['Soil'].str.replace('Moisture\n', '')
df['pH'] = df['pH'].str.replace('pH\n', '')
df['UltimateHeight'] = df['UltimateHeight'].str.replace('Ultimate height\n', '')
df['UltimateSpread'] = df['UltimateSpread'].str.replace('Ultimate spread\n', '')
df['TimeToUltimateHeight'] = df['TimeToUltimateHeight'].str.replace('Time to ultimate height\n', '')

#%%
df.columns

#%%
df.head()

#%%
df.dtypes

#%%
print(df["UltimateHeight"].unique())

#%%
df[["UltimateSpread"]]

#%%
"""Ultimate Height Clean"""

# remove metres string
df["UltimateHeight"] = df["UltimateHeight"].str.replace('metres', '')

#%%
df["UltimateHeight_Above_12.0"] = df.UltimateHeight == 'Higher than 12 '
df["UltimateHeight_Above_12.0"]

#%%
df["UltimateHeight_Max_0.1"] = df.UltimateHeight == 'Up to 10 cm'
df["UltimateHeight_Max_0.1"]

#%%
"""Ultimate Spread Clean"""

# remove metres string
df["UltimateSpread"] = df["UltimateSpread"].str.replace('metres', '')
df["UltimateSpread"] = df["UltimateSpread"].str.replace('metre', '')

#%%
df["UltimateSpread_Above_8.0"] = df.UltimateSpread == 'wider than 8 '
df["UltimateSpread_Above_8.0"]

#%%
df["UltimateSpread"].unique()
#%%
# cast values and integer
df["UltimateHeight"] = df[["UltimateHeight"]].astype(float)
#%%
# Convert cm to m
df["UltimateHeight"] = df[["UltimateHeight"] == 10].apply(lambda n = n x 100)
#%%
df.iloc[200]

#%%
df.info()

#%%
df.drop('HeightAbove12', axis=1)


# get images into s3
# process numerical data such as min height, max height
# %%
df.to_csv('cleaned_database.csv')
