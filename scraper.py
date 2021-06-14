#%%
from selenium import webdriver

driver = webdriver.Chrome()

#%%
main = driver.get('https://www.rhs.org.uk/Plants/Search-Results?form-mode=true&context=l%3Den%26q%3D%2523all%26sl%3DplantForm')
#%%
# Begins looping through elements for links
def get_all_plants_on_page():
  plant_list = []
  plants = driver.find_elements_by_xpath('//*[@id="planet_search_list"]/div/plants-search-result-list/div/ul/li')
  for target_plant in plants:
      scientific_name = target_plant.find_element_by_xpath('.//h3').text
      synonym = target_plant.find_element_by_xpath('.//h4').text
      description_url = target_plant.find_element_by_xpath('.//div/a[1]').get_attribute('href')
      link = target_plant.find_element_by_class_name("btn-2").get_attribute('href')
      plant_list_dict = {
              'Common Name': scientific_name,                     
              'Synonym': synonym, 
              'Description URL': description_url
              }
      plant_list.append(plant_list_dict)
      print(link)
  return plant_list
#%%
# Loops through all pages up to 100
all_plants_list = []
for i in range(100):
  base_url = 'https://www.rhs.org.uk/plants/search-results?context=b%253D0%2526hf%253D10%2526l%253Den%2526q%253D%252523all%2526s%253Ddesc%252528plant_merged%252529%2526sl%253Dplants&s=desc(plant_merged)&form-mode=true&page='
  driver.get(base_url + str(i))
  new_plants = get_all_plants_on_page()
  all_plants_list.extend(new_plants)
# %%
driver.quit()
# %%
