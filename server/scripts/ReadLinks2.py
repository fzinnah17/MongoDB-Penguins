import requests
from trafilatura import fetch_url, extract

# download a web page
url1 = 'https://github.com/DeveloperMindset123?tab=repositories'
downloaded_url1 = fetch_url(url1)
#downloaded is None  # assuming the download was successful
#False

# extract information from HTML
result = extract(downloaded_url1)
print(result)

r = requests.get(url1)
extracted_html = r.content



