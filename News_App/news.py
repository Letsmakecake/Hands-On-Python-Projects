import requests  # Import the requests module to make HTTP requests

# API key for NewsAPI – make sure to keep this secure in real applications
api = "e289f9f364d441129d963247ecd3ea62"  # Get your own API key from https://newsapi.org

# Take user input for the topic to search news about
quary = input("Topic ?  ")

# Construct the URL with the query and API key
url = (f"https://newsapi.org/v2/everything?q={quary}&apiKey={api}")

# Send a GET request to the API URL
r = requests.get(url)

# Convert the JSON response into a Python dictionary
data = r.json()

# Extract the list of articles from the response
articles = data["articles"]

# Loop through the articles and print their titles and URLs
for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])  # Print article number, title, and link
    print("\n*******************************\n")  # Separator for readability

    