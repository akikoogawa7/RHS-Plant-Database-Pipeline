#%%
from numpy import float64
import pandas as pd

df = pd.read_csv('clean_test.csv', delimiter=',')
pd.read_csv('clean_test.csv')
print(len(df))

#%%
# Renaming unnamed column to ID
df.rename(columns={'Unnamed: 0':'ID'}, inplace=True )

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
# Get Ulimate Height min and max values 
def getMinValues(s):
    if s == "Higher than 12 metres":
        return '12'
    else:
        if '-' in s:
            s = s.split('-', 1)[0]
            return s

def getMaxValues(s):
    if s == "Up to 10 cm":
        return '10'
    else:
        if '-' in s:
            s = s.split('-', 1)[1]
            return s

# Get Ultimate Spread min and max values

#%%
# Apply UH min max function
df["UltimateHeight_Min"] = df["UltimateHeight"].apply(getMinValues)
df["UltimateHeight_Max"] = df["UltimateHeight"].apply(getMaxValues)

#%%
# Remove metres string
df["UltimateHeight_Min"] = df["UltimateHeight_Min"].str.replace('metres', '')
df["UltimateHeight_Max"] = df["UltimateHeight_Max"].str.replace('metres', '')

#%%
# Cast str to float
df["UltimateHeight_Min"].astype(float64)
df["UltimateHeight_Max"].astype(float64)

#%%
# Check values
df["UltimateHeight_Min"]
df["UltimateHeight_Max"]

df.head()

#%%
# Apply US min and max function
# df["UltimateSpread"].unique()

#%%
# cast values and integer
df["UltimateHeight"] = df[["UltimateHeight"]].astype(float)
#%%
# Convert cm to m
df["UltimateHeight_Max"] = df[["UltimateHeigh_Max"] == 10].apply(lambda n = n x 100)

#%%
df.iloc[220]

#%%
df.info()

# get images into s3
# process numerical data such as min height, max height - different ways of cleaning (higher than, up to, '-')
# %%
df.to_csv('cleaned_database.csv')
