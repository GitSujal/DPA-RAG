from selenium import webdriver
import html2text
from selenium.webdriver.chrome.options import Options
import time

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\sujal\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
options.add_argument(r'--profile-directory=Default') #e.g. Profile 3
driver = webdriver.Chrome(executable_path=r'C:\Program Files\chromedriver\chromedriver.exe', chrome_options=options)

# Define the URL to get the HTML from
url = "https://dataprofessionacademy.com/path-player?courseid=data-profession-101&unit=6517c186abfb44d3f203b906Unit"


# Navigate to the URL
driver.get(url)

time.sleep(5)


# Get the HTML from the page
html = driver.page_source

parser = html2text.HTML2Text()
parser.ignore_links = False

# Convert HTML to markdown
markdown = html2text.html2text(html)

# Print the markdown output
# print(markdown)

# write the markdown to a file
with open("output.md", "w") as f:
    f.write(markdown)

# Close the browser
driver.close()