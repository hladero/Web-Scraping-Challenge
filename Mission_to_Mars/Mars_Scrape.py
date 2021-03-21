from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}


def scrape():
    browser = Browser ('chrome', **executable_path, headless = False)
    title,paragraph = news(browser)

    mars={
        "title":title,
        "paragraph": paragraph,
        'image': image(browser),
        'facts': facts(),
        'hemispheres': hemispheres(browser) 
    }
    return mars





# ### NASA Mars News
# 
# * Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 

# In[6]:


#website
url= 'https://mars.nasa.gov/news/'
#visit the website
browser.visit(url)


# In[7]:


Title=browser.find_by_css('div.content_title a').text
Title


# In[8]:


#html object
html = browser.html
#parse with a beautiful soup
soup = BeautifulSoup(html, 'html.parser')


# In[9]:


#browser.find_by_css('div.class_=rollover_description_inner').text
Paragraph = soup.find('div',class_='article_teaser_body').text
Paragraph


# In[ ]:





# In[15]:





# ### JPL Mars Space Images - Featured Image

# In[10]:


#set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser ('chrome', **executable_path, headless = False)


# In[15]:


#website
url= 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
#visit the website
browser.visit(url)

#Find and Save the featured image
browser.click_link_by_partial_text('FULL IMAGE')
browser.find_by_css('img.fancybox-image')['src']


# In[43]:


#website
url= 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
#visit the website
browser.visit(url)


# In[44]:


html=browser.html
#create beautifulsoup object with parse
soup = BeautifulSoup(html, 'html.parser')


# In[45]:


#get the results and return those as a list


# In[47]:


#get the featured image 
featured_image_url = soup.find_all('img',class_='headerimage fade-in')


# In[48]:


featured_image_url


# In[ ]:


### Mars Facts
# Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
pd.read_html('https://space-facts.com/mars/')[0].to_html()




# ### Mars Hemispheres

# * Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.
# 
# * You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
# 
# * Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys `img_url` and `title`.
# 
# * Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
# 
# ```python
# # Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]
# ```
# 
# - - -
# 

# In[30]:


url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#visit the website
browser.visit(url)


# In[31]:


links = browser.find_by_css('a.itemLink h3')


# In[32]:


List=[]

for i in range(len(links)):
    hemisphere = {}
    hemisphere['title']=browser.find_by_css('a.itemLink h3')[i].text
    browser.find_by_css('a.itemLink h3').click()
    hemisphere['url']=browser.find_by_text('Sample')['href']
    browser.back()
    List.append(hemisphere)
browser.quit()
List


# ### Step 2 - MongoDB and Flask Application

# Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.
# 
# * Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
# 
# * Next, create a route called `/scrape` that will import your `scrape_mars.py` script and call your `scrape` function.
# 
#   * Store the return value in Mongo as a Python dictionary.
# 
# * Create a root route `/` that will query your Mongo database and pass the mars data into an HTML template to display the data.
# 
# * Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.
# 
# ![final_app_part1.png](Images/final_app_part1.png)
# ![final_app_part2.png](Images/final_app_part2.png)

# In[ ]:





# In[ ]:





# In[ ]:




