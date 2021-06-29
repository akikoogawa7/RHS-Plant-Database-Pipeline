#%%
from requests.api import get
from selenium import webdriver
from time import sleep
from csv import reader
import threading
import concurrent.futures
import pandas as pd

driver = webdriver.Chrome()
#%%
main = driver.get('https://www.rhs.org.uk/Plants/Search-Results?form-mode=true&context=l%3Den%26q%3D%2523all%26sl%3DplantForm')
#%%
# Begins looping through elements for links
def get_all_plants_on_page():
  """Function to add to the list of all plants with links"""
  plant_list = []
  plants = driver.find_elements_by_xpath('//*[@id="planet_search_list"]/div/plants-search-result-list/div/ul/li')
  for target_plant in plants:
      link = target_plant.find_element_by_class_name("btn-2").get_attribute('href')
      plant_list.append(link)
      print(link)
  return plant_list
  # def __init__(self):
  #   t = threading.Thread(target=self.get_all_plants_on_page)
  #   t.start() 
sleep(5)
# Loops through all pages 1 by 1 in 50s
# Out of 30518 pages
all_plants_list = []
for i in range(450, 500): #450,500 (rhs test database)
  base_url = 'https://www.rhs.org.uk/plants/search-results?context=b%253D0%2526hf%253D10%2526l%253Den%2526q%253D%252523all%2526s%253Ddesc%252528plant_merged%252529%2526sl%253Dplants&s=desc(plant_merged)&form-mode=true&page='
  driver.get(base_url + str(i))
  new_plants = get_all_plants_on_page()
  all_plants_list.extend(new_plants)
#%%
# Scrape data from all_plants_list
all_plants_data = []
colour_imgs_autumn = []
colour_imgs_spring = []
colour_imgs_summer = []
colour_imgs_winter = []
for plant in all_plants_list:
  try:
    plant_item_details = driver.get(plant)
    plant_detail_box = driver.find_elements_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[1]')
    """Type"""
    scientific_name = driver.find_element_by_xpath('.//h1').text
    print(scientific_name)
    common_name = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[1]/div/div[2]/div/div[1]/h2').text
    print(common_name)
    other_common_names = driver.find_element_by_xpath('.//p').text
    print(other_common_names)
    family = driver.find_element_by_xpath('.//*[@id="ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li15"]/p').text
    print(family)
    genus = driver.find_element_by_xpath('.//*[@id="ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li2"]/p').text
    print(genus)
    plant_range = driver.find_element_by_xpath('.//*[@id="ctl00_ctl00_ctl00_plcMainContent_plcMainContent_plcMainContent_PlantDetail1_Li4"]/p').text
    print(plant_range)
    """Characteristics"""
    foliage = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li[1]/p').text
    print(foliage)
    habit = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li[2]/p').text
    print(habit)
    hardiness = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/ul/li[3]/p').text
    print(hardiness)
    """Sunlight"""
    sunlight = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/div[1]/ul').text
    print(sunlight)
    aspect = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/div[2]/ul/li[1]/p').text
    print(aspect)
    exposure = driver.find_element_by_xpath('//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[3]/div/div/div[2]/ul/li[2]/p').text
    print(exposure)
    """Soil"""
    soil = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div/div[1]/ul').text
    print(soil)
    moisture = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[1]/p').text
    print(moisture)
    pH = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[4]/div/div/div[2]/ul/li[3]/p').text
    print(pH)
    """Size"""
    ultimate_height = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[5]/div/div/div/ul/li[1]/p').text
    print(ultimate_height)
    ultimate_spread = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[5]/div/div/div/ul/li[2]/p').text
    print(ultimate_spread)
    time_to_ultimate_height = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[2]/div/div[5]/div/div/div/ul/li[3]/p').text
    print(time_to_ultimate_height)
    """How to Grow"""
    cultivation = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/p[1]').text
    print(cultivation)
    propagation = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/p[2]').text
    print(propagation)
    suggested_planting_locations = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[1]/p[3]').text
    print(suggested_planting_locations)
    """How to Care"""
    pruning = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/p[1]').text
    print(pruning)
    pests = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/p[2]').text
    print(pests)
    diseases = driver.find_element_by_xpath('.//*[@id="skip-content"]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/p[3]').text
    print(diseases)
    """Colour in Season Images"""
    all_autumn_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[1]/ul/li/div/div/img')]
    print(all_autumn_imgs)
    all_spring_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[2]/ul/li/div/div/img')]
    print(all_spring_imgs)
    all_summer_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[3]/ul/li/div/div/img')]
    print(all_summer_imgs)
    all_winter_imgs = [img.get_attribute('src') for img in driver.find_elements_by_xpath('.//div[4]/ul/li/div/div/img')]
    print(all_winter_imgs)
    sleep(5)

    all_plants_data_dict = {
      'ScientificName': scientific_name,
      'CommonName': common_name,
      'OtherCommonNames': other_common_names,
      'Family': family,
      'Genus': genus,
      'PlantRange': plant_range,
      'Foliage': foliage,
      'Habit': habit,
      'Hardiness': hardiness,
      'Sunlight': sunlight,
      'Aspect': aspect,
      'Exposure': exposure,
      'Soil': soil,
      'Moisture': moisture,
      'pH': pH,
      'UltimateHeight': ultimate_height,
      'UltimateSpread': ultimate_spread,
      'TimeToUltimateHeight': time_to_ultimate_height,
      'Cultivation': cultivation,
      'Propagation': propagation,
      'SuggestedPlantingLocation': suggested_planting_locations,
      'Pruning': pruning,
      'Pests': pests,
      'Diseases': diseases,
      'ColourInAutumn': all_autumn_imgs,
      'ColourInSpring': all_spring_imgs,
      'ColourInSummer': all_summer_imgs,
      'ColourInWinter': all_winter_imgs,
    }
    colours_autumn = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInAutumn': all_autumn_imgs,
    }
    colours_spring = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInSpring': all_spring_imgs,
    }
    colours_summer = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInSummer': all_summer_imgs,
    }
    colours_winter = {
      'CommonName': common_name,
      'ScientificName': scientific_name,
      'ColourInWinter': all_winter_imgs,
    }
    all_plants_data.append(all_plants_data_dict)
    colour_imgs_autumn.append(colours_autumn)
    colour_imgs_spring.append(colours_spring)
    colour_imgs_summer.append(colours_summer)
    colour_imgs_winter.append(colours_winter)
  except: Exception
  pass

# with concurrent.futures.ThreadPoolExecutor() as executor:
#   executor.map(get_all_plants_on_page, )
#%%
df = pd.DataFrame(all_plants_data)
print(df)
#%%
df.to_csv('rhs_plant_database500.csv')
#%%
# Append to original csv
df.to_csv('rhs_plant_database.csv', mode='a')