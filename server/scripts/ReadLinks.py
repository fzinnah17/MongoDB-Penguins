import logging
import sys

# Demonstrate web page reader
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


# using SimpleWebReader
from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader # type: ignore
from llama_index.readers.web import TrafilaturaWebReader

from IPython.display import Markdown, display
import os


documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["http://paulgraham.com/worked.html"]  # test with my own linkedin to see if it works as intended --> failed, only works with HTML
)

print("Processed Document:\n")
print(documents)  # seems like SimpleWebReader doesn't work as intended

index = SummaryIndex.from_documents(documents=documents)
# set logging to debug for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("What is this website about?")
print(display(Markdown(f"<b>{response}</b>")))

print("\nTerminal Output:")
print(response)


documents2 = TrafilaturaWebReader(sitemap_search).load_data(
    ["https://www.linkedin.com/in/ayan-das-02982b1b6/"]
)

index2 = SummaryIndex.from_documents(documents=documents2)

# set logging to DEBUG for more detailed outputs
query_engine2 = index.as_query_engine()
response2 = query_engine2.query("What is this webpage about?")
display(Markdown(f"{response2}"))

print("\nSecond attempt at response:")
print(response2)
