#%%
from numpy import float64, integer
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
# Get Ulimate Height min and max values 
def getUHMin(s):
    if s == "Higher than 12 metres":
        return '12'
    else:
        if '-' in s:
            s = s.split('-', 1)[0]
            return s
def getUHMax(s):
    if s == "Up to 10 cm":
        return '10'
    else:
        if '-' in s:
            s = s.split('-', 1)[1]
            return s
# Get Ultimate Spread min and max values
def getUSMin(s):
    if s == "wider than 8 metres":
        return '8'
    else:
        if '-' in s:
            s = s.split('-', 1)[0]
            return s
def getUSMax(s):
    if '-' in s:
        s = s.split('-', 1)[1]
        return s

#%%
# Apply UH min max function
# Cast str to float
# Strip str to remove whitespace
# Convert 10cm to 0.1me
df["UltimateHeight_Min"] = df["UltimateHeight"].apply(getUHMin).str.replace('metres', '').str.replace('metre', '').str.strip()
df["UltimateHeight_Max"] = df["UltimateHeight"].apply(getUHMax).str.replace('metres', '').str.replace('metre', '').str.replace('10', '0.1').str.strip()
# Apply US min max function, cast str to float
df["UltimateSpread_Min"] = df["UltimateSpread"].apply(getUSMin).str.replace('metres', '').str.replace('metre', '').str.strip()
df["UltimateSpread_Max"] = df["UltimateSpread"].apply(getUSMax).str.replace('metres', '').str.replace('metre', '').str.strip()

#%%
df["UltimateHeight_Min"].astype(float)
df["UltimateHeight_Max"].astype(float)
df["UltimateSpread_Min"].astype(float)
df["UltimateSpread_Max"].astype(float)

#%%
df[["Foliage", "Hardiness", "Soil", "Pests", "Diseases", "pH", "Pruning", "Propagation"]]

# %%
df.to_csv('cleaned_test_database.csv')
