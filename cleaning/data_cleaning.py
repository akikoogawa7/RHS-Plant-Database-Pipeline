#%%
import pandas as pd
from numpy import float64

df = pd.read_csv('rhs_plant_database.csv', delimiter=',')
pd.read_csv('rhs_plant_database.csv')
#%%
df.head

#%%
# Renaming unnamed column to ID
df.rename(columns={'Unnamed: 0':'ID'}, inplace=True )
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
df['TimeToUltimateHeight'] = df['TimeToUltimateHeight'].str.replace('Time to ultimate height', '')
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
# Get Time to Ultimate Height min and max values
def getTUHMin(s):
    if s == 'more than 50 years':
        return '50'
    else:
        if '-' in s:
            s = s.split('-', 1)[0]
        return s
def getTUHMax(s):
    if '1 year' in s:
        return '1'
    else:
        if '-' in s:
            s = s.split('-', 1)[1]
        return s
#%%
df["UltimateHeight_Min"] = df["UltimateHeight"].apply(getUHMin).str.replace('metres', '').str.replace('metre', '').str.strip()
df["UltimateHeight_Max"] = df["UltimateHeight"].apply(getUHMax).str.replace('metres', '').str.replace('metre', '').str.replace('10', '0.1').str.strip()
df["UltimateSpread_Min"] = df["UltimateSpread"].apply(getUSMin).str.replace('metres', '').str.replace('metre', '').str.replace('Ultimate spread', '').str.strip()
df["UltimateSpread_Max"] = df["UltimateSpread"].apply(getUSMax).str.replace('metres', '').str.replace('metre', '').str.replace('Ultimate spread', '').str.strip()
df["TimeToUltimateHeight_Min"] = df["TimeToUltimateHeight"].apply(getTUHMin).str.replace('years', '').str.replace('year', '').str.replace('more than', '').str.strip()
df["TimeToUltimateHeight_Max"] = df["TimeToUltimateHeight"].apply(getTUHMax).str.replace('years', '').str.replace('year', '').str.replace('more than', '').str.strip()
#%%
nan_value = float("NaN")
df.replace("", nan_value, inplace=True)
df["UltimateHeight_Min"].astype(float)
df["UltimateHeight_Max"].astype(float)
df["UltimateSpread_Min"].astype(float)
df["UltimateSpread_Max"].astype(float)
df["TimeToUltimateHeight_Min"].astype(float)
df["TimeToUltimateHeight_Max"].astype(float)
# %%
df.columns
