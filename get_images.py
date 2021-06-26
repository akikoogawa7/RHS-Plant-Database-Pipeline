#%%
from requests.api import get
from selenium import webdriver
from time import sleep
import requests
import boto3
import json
import os

#%%
with open('extract_links.csv') as f:
    links = f.readlines()
# %%
links

#%%
driver = webdriver.Chrome()

#%%
def download_file(src_url, local_destination):
    response = requests.get(src_url)
    with open(local_destination, 'wb+') as f:
        f.write(response.content)
def s3_upload(obj, filename):
    s3 = boto3.resource('s3')
    s3.Object(key=filename).put(Body=json.dumps(obj))

#%%
for id, link in enumerate(links):
    driver.get(link)
    list_of_img_divs = driver.find_elements_by_xpath('//div[@class="owl-stage"]/div//div[@class="cover-image__img"]')
    plant_folder = f'plant_imgs/{id}'

    if not os.path.exists(plant_folder):
        os.mkdir(plant_folder)
    for index, element in enumerate(list_of_img_divs):
        try:
            attr = element.get_attribute('style').replace('background-image: url("', '').replace('");', '')
            print(attr)
            download_file(attr, f'plant_imgs/{id}/{index}.jpg')
        except: Exception
        pass
# %%

