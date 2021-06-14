#%%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

#%%
main = driver.get('https://www.rhs.org.uk/Plants/Search-Results?form-mode=true&context=l%3Den%26q%3D%2523all%26sl%3DplantForm')

plants = driver.find_elements_by_xpath('//*[@id="planet_search_list"]/div/plants-search-result-list/div/ul/li')
plant_list = []
plant_links = []

#%%
# Loops through target elements in whole website
# page_number = 1
# if page_number < 3000:
#     page_number + 1
#     pagenav_url = f'https://www.rhs.org.uk/plants/search-results?context=b%253D0%2526hf%253D10%2526l%253Den%2526q%253D%252523all%2526s%253Ddesc%252528plant_merged%252529%2526sl%253Dplants&s=desc(plant_merged)&form-mode=true&page={page_number}'
# else:
#     print('All pages browsed.')

# Begins looping through elements for links
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

    element = WebDriverWait(driver,10).until(EC.presence_of_element_located(
    (By.CLASS, "btn-2")))
# %%
print(plant_list)
#%%
element.click()
# Transform into DataFrame
# plant_df = pd.DataFrame(plant_list)
# print(plant_df)

#%%
# plant_df.head()
# %%
driver.quit()
# %%
