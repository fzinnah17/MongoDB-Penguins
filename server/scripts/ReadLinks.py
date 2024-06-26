import logging
import sys

# Demonstrate web page reader
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# using SimpleWebReader
from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader # type: ignore
from llama_index.readers.web import TrafilaturaWebReader
from trafilatura import fetch_url, extract
from llama_index.core.node_parser import HTMLNodeParser
from llama_index.readers.file import FlatReader
from pathlib import Path
import requests
from IPython.display import Markdown, display
import os




'''
documents2 = TrafilaturaWebReader(sitemap_search=True).load_data(
    ["https://www.linkedin.com/in/ayan-das-02982b1b6/"]
)

index2 = SummaryIndex.from_documents(documents=documents2)

# set logging to DEBUG for more detailed outputs
query_engine2 = index.as_query_engine()
response2 = query_engine2.query("What is this webpage about?")
display(Markdown(f"{response2}"))

print("\nSecond attempt at response:")
print(response2)  
'''

# download a web page

url0 = "https://github.com/DeveloperMindset123"
url1 = 'https://github.com/DeveloperMindset123?tab=repositories'
url2 = "https://github.com/DeveloperMindset123?page=2&tab=repositories"
url3 = "https://github.com/DeveloperMindset123?page=3&tab=repositories"
specific_repo1 = "https://github.com/DeveloperMindset123/PriceScape_Navigator"
specific_repo2 = "https://github.com/DeveloperMindset123/ivyhacks-second-insight"
specific_repo3 = "https://github.com/DeveloperMindset123/FlixterPlus"
specific_repo4 = "https://github.com/DeveloperMindset123/Scholarly-Llama"
specific_repo5 = "https://github.com/DeveloperMindset123/mapillary-python-sdk"

# the following are links relevant to about us 
googleAboutUs = "https://about.google"
microsoftAboutUs = "https://www.microsoft.com/en-us/about"
trunkToolsAboutUs = "https://trunktools.com"
mongoDBAboutUs = "https://www.mongodb.com/company"
nomicAboutUs = "https://www.nomic.ai"
etsyAboutUs = "https://www.etsy.com/about"
appleAboutUs = "https://www.apple.com"
americanExpressAboutUs = "https://www.americanexpress.com/en-us/company/who-we-are/"
chaseAboutUs = "https://www.chase.com/digital/resources/about-chase"

#downloaded_url1 = fetch_url(url1)
#downloaded is None  # assuming the download was successful
#False

# extract information from HTML
'''
result = extract(downloaded_url1)
print(result)
'''
# define the parser, we only need to define the parser once
parser = HTMLNodeParser()

r0 = requests.get(url0)
#print("Status Code for Response 0:")
#print(r0.status_code)
extracted_html0 = r0.content
#print("\nExtracted HTML content for Github Repository Homepage:")
#print(extracted_html0)

#save the resulting out
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/githubRepo-HomePage.html', 'wb+') as f:
    f.write(r0.content)

# make sure the filename for html matches what the html file was saved as
html_content_github_repo_home = FlatReader().load_data(Path("../Data/html/githubRepo-HomePage.html"))
node0 = parser.get_nodes_from_documents(html_content_github_repo_home)
#print("\n\nResulting Nodes:")
#print("\nNode 0 for Github Home Page Content:")
#print(node0)


r1 = requests.get(url1)
#print("\nStatus Code for Response 2:")
#print(r1.status_code)
extracted_html1 = r1.content
#print("\nExtracted HTML content for Github Repository Page 1:")
#print(extracted_html1)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/githubRepo-Page1.html', 'wb+') as f:
    f.write(r1.content)

html_content_github_repo1 = FlatReader().load_data(Path("../Data/html/githubRepo-Page1.html"))
node1 = parser.get_nodes_from_documents(html_content_github_repo1)
#print("\nNode 1 for Github Repository page 1:")
#print(node1)

# request 3
r3 = requests.get(url2)
#print("\nStatus Code for Response 3:")
#print(r3.status_code)
extracted_html2 = r3.content
#print("\nExtracted HTML content for Github Repository Page 2:")
#print(extracted_html2)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/githubRepo-Page2.html', 'wb+') as f:
    f.write(r3.content)

html_content_github_repo2 = FlatReader().load_data(Path("../Data/html/githubRepo-Page2.html"))
node2 = parser.get_nodes_from_documents(html_content_github_repo2)
#print("\nNode 2 for Github Repository page 2:")
#print(node2)

# request 4
r4 = requests.get(url3)
#print("\nStatus Code for Response 4:")
#print(r4.status_code)
extracted_html3 = r4.content
#print("\nExtracted HTML content for Github Repository Page 3:")
#print(extracted_html3)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/githubRepo-Page3.html', 'wb+') as f:
    f.write(r4.content)

html_content_github_repo3 = FlatReader().load_data(Path("../Data/html/githubRepo-Page3.html"))
node3 = parser.get_nodes_from_documents(html_content_github_repo2)
#print("\nNode 2 for Github Repository page 3:")
#print(node3)

# request 5
r5 = requests.get(specific_repo1)
#print("\nStatus Code for Response 5:")
#print(r5.status_code)
extracted_html4 = r5.content
#print("\nSpecific Repo Content:")
#print(extracted_html4)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/specificRepo0.html', 'wb+') as f:
    f.write(r5.content)

html_content_github_repo4 = FlatReader().load_data(Path("../Data/html/specificRepo0.html"))
node4 = parser.get_nodes_from_documents(html_content_github_repo4)
#print("\nNode 4 for Specific Repo:")
#print(node4)

# request 6
r6 = requests.get(specific_repo2)
#print("\nStatus Code for Response 6:")
#print(r6.status_code)
extracted_html5 = r6.content
#print("\nSpecific Repo Content:")
#print(extracted_html5)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/specific-repo2.html', 'wb+') as f:
    f.write(r6.content)

html_content_github_repo5 = FlatReader().load_data(Path("../Data/html/specific-repo2.html"))
node5 = parser.get_nodes_from_documents(html_content_github_repo5)
#print("\nNode 5 for Specific Repo 2:")
#print(node5)

# request 7
r7 = requests.get(specific_repo3)
#print("\nStatus Code for Response 7:")
#print(r7.status_code)
extracted_html6 = r7.content
#print("\nSpecific Repo Content:")
#print(extracted_html6)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/specific-repo3.html', 'wb+') as f:
    f.write(r7.content)

html_content_github_repo6 = FlatReader().load_data(Path("../Data/html/specific-repo3.html"))
node6 = parser.get_nodes_from_documents(html_content_github_repo5)
#print("\nNode 6 for Specific Repo:")
#print(node6)


# request 8
r8 = requests.get(specific_repo4)
#print("\nStatus Code for Response 8:")
#print(r8.status_code)
extracted_html7 = r8.content
#print("\nSpecific Repo Content:")
#print(extracted_html7)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/specific-repo4.html', 'wb+') as f:
    f.write(r8.content)

html_content_github_repo7 = FlatReader().load_data(Path("../Data/html/specific-repo4.html"))
node7 = parser.get_nodes_from_documents(html_content_github_repo7)
#print("\nNode 7 for Specific Repo:")
#print(node7)

# request 9
r9 = requests.get(specific_repo5)
#print("\nStatus Code for Response 8:")
#print(r9.status_code)
extracted_html8 = r9.content
#print("\nSpecific Repo Content:")
#print(extracted_html8)

# save the extracted html in an actual html file
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/specific-repo5.html', 'wb+') as f:
    f.write(r9.content)

html_content_github_repo8 = FlatReader().load_data(Path("../Data/html/specific-repo5.html"))
node8 = parser.get_nodes_from_documents(html_content_github_repo8)
#print("\nNode 8 for Specific Repo:")
#print(node8)


#print("The following are HTML extracted content for various companies:")

# The following are links to parse through the About me section for the companies
googleRequest = requests.get(googleAboutUs)
#print(googleRequest.status_code)
google_html = googleRequest.content
#print(google_html)

#save the resulting out
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/googleAboutUs.html', 'wb+') as f:
    f.write(googleRequest.content)

# make sure the filename for html matches what the html file was saved as
google_html_extracted = FlatReader().load_data(Path("../Data/html/googleAboutUs.html"))
googleNode = parser.get_nodes_from_documents(google_html_extracted)
#print("Google Node")
#print(googleNode)


microsoftRequest = requests.get(microsoftAboutUs)
#print(microsoftRequest.status_code)
microsoft_html = microsoftRequest.content
#print("Extracted Microsoft HTML:")
#print(microsoft_html)

#save the resulting out
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/microsoftAboutUs.html', 'wb+') as f:
    f.write(microsoftRequest.content)

# make sure the filename for html matches what the html file was saved as
microsoft_html_extracted = FlatReader().load_data(Path("../Data/html/microsoftAboutUs.html"))
microsoftNode = parser.get_nodes_from_documents(microsoft_html_extracted)
#print("\n\nResulting Microsoft Nodes:")
#print(microsoftNode)



trunkToolsRequest = requests.get(trunkToolsAboutUs)
#print(trunkToolsRequest.status_code)
trunkTools_html = trunkToolsRequest.content
#print("Extracted TrunkTools HTML:")
#print(trunkTools_html)

#save the resulting out
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/trunkToolsAboutUs.html', 'wb+') as f:
    f.write(trunkToolsRequest.content)

# make sure the filename for html matches what the html file was saved as
trunkTools_html_extracted = FlatReader().load_data(Path("../Data/html/trunkToolsAboutUs.html"))
trunkToolsNode = parser.get_nodes_from_documents(trunkTools_html_extracted)
#print("\n\nResulting Trunk Tools Nodes:")
#print(trunkToolsNode)



mongodbRequest = requests.get(trunkToolsAboutUs)
#print(mongodbRequest.status_code)
mongodbRequest_html = mongodbRequest.content
#print("Extracted mongoDB HTML:")
#print(mongodbRequest_html)

#save the resulting out
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/mongodbAboutUs.html', 'wb+') as f:
    f.write(mongodbRequest.content)

# make sure the filename for html matches what the html file was saved as
mongodb_html_extracted = FlatReader().load_data(Path("../Data/html/mongodbAboutUs.html"))
mongodb_Node = parser.get_nodes_from_documents(mongodb_html_extracted)
#print("\n\nResulting Mongo DB Nodes:")
#print(mongodb_Node)


nomicRequest = requests.get(nomicAboutUs)
#print(nomicRequest.status_code)
nomic_Request_html = nomicRequest.content
#print("Extracted Nomic HTML:")
#print(nomic_Request_html)

#save the resulting out
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/nomicAboutUs.html', 'wb+') as f:
    f.write(nomicRequest.content)

# make sure the filename for html matches what the html file was saved as
nomic_html_extracted = FlatReader().load_data(Path("../Data/html/nomicAboutUs.html"))
nomic_Node = parser.get_nodes_from_documents(nomic_html_extracted)
#print("\n\nResulting Trunk Tools Nodes:")
#print(nomic_Node)



etsyRequest = requests.get(etsyAboutUs)
#print(etsyRequest.status_code)
etsy_Request_html = etsyRequest.content
#print("Extracted Etsy HTML:")
#print(etsy_Request_html)

#save the resulting out
with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/etsyAboutUs.html', 'wb+') as f:
    f.write(etsyRequest.content)

# make sure the filename for html matches what the html file was saved as
etsy_html_extracted = FlatReader().load_data(Path("../Data/html/etsyAboutUs.html"))
etsy_Node = parser.get_nodes_from_documents(etsy_html_extracted)
#print("\n\nResulting Etsy Nodes:")
#print(etsy_Node)


appleRequest = requests.get(appleAboutUs)
#print(appleRequest)
apple_request_html = appleRequest.content
#print("Extracted Apple HTML:")
#print(apple_request_html)

with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/appleAboutUs.html', 'wb+') as f:
    f.write(appleRequest.content)

apple_html_extracted = FlatReader().load_data(Path("../Data/html/appleAboutUs.html"))
apple_Node = parser.get_nodes_from_documents(apple_html_extracted)
#print("\n\nResulting Apple Nodes:")
#print(apple_Node)



americanExpressRequest = requests.get(americanExpressAboutUs)
#print(americanExpressRequest)
americanExpress_request_html = americanExpressRequest.content
#print("Extracted American HTML:")
#print(americanExpress_request_html)

with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/americanExpressAboutUs.html', 'wb+') as f:
    f.write(americanExpressRequest.content)

americanExpress_html_extracted = FlatReader().load_data(Path("../Data/html/americanExpressAboutUs.html"))
americanExpress_Node = parser.get_nodes_from_documents(americanExpress_html_extracted)
#print("\n\nResulting American Express Nodes:")
#print(americanExpress_Node)

chaseRequest = requests.get(chaseAboutUs)
#print(chaseRequest)
chase_request_html = chaseRequest.content
#print("Extracted Chase HTML:")
#print(chase_request_html)

with open('/Users/ayandas/Desktop/VS_Code_Projects/mongodb-testrepo/server/Data/html/chaseAboutUs.html', 'wb+') as f:
    f.write(americanExpressRequest.content)

chase_html_extracted = FlatReader().load_data(Path("../Data/html/chaseAboutUs.html"))
chase_Node = parser.get_nodes_from_documents(chase_html_extracted)
#print("\n\nResulting Chase Nodes:")
#print(chase_Node)




#next request
'''
parser = HTMLNodeParser()  # optional list of tags
nodes = parser.get_nodes_from_documents(extracted_html)

print(nodes)
'''
'''
documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["http://paulgraham.com/worked.html"]  # test with my own linkedin to see if it works as intended --> failed, only works with HTML
)

#print("Processed Document:\n")
#print(documents)  # seems like SimpleWebReader doesn't work as intended

index = SummaryIndex.from_documents(documents=documents)
# set logging to debug for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("What is this website about?")
#print(display(Markdown(f"<b>{response}</b>")))

#print("\nTerminal Output:")
print(response)

'''