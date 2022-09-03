#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[26]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[27]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[28]:


html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[29]:


slide_elem.find('div', class_='content_title')


# In[30]:


#use parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[31]:


# use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[32]:


# visit url
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[33]:


#Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[34]:


#parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[35]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[36]:


# use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[37]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[38]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[50]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[58]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for item in range(4):
    hemisphere = {}
        
    #find element on each loop to avoid a stale element exception
    browser.find_by_css("a.product-item h3")[item].click()

    #find sample img anchor tag and extract the <href>
    sample_element = browser.links.find_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    img_url = hemisphere["img_url"]
    #get hemisphere title
    hemisphere["title"] = browser.find_by_css("h2.title").text
    title = hemisphere["title"]
    # append hemisphere object to list of dictionaries
    hemisphere_image_urls.append(hemisphere)

    #navigate backwards
    browser.back()


# In[59]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[60]:


# 5. Quit the browser
browser.quit()


# In[ ]:




