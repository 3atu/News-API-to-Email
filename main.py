#input = API
#output = Email with data
from send_email import send_email
import requests
topic = "tesla"
topic = topic.title()

api_url = f'https://newsapi.org/v2/everything?q={topic}&from=2022-12-07&sortBy=publishedAt"&apiKey=e30632e8302041bf91521626b875fe0c&language=en'
api_key = 'e30632e8302041bf91521626b875fe0c'

#Make Request
request = requests.get(api_url)

#Get dictionary with data
content = request.json() #gets content as dictionary

#print(content)

#Access artcile information
body = ""
for article in content["articles"][:20]: #article is a key. we are looking for description in the value of the key articles.
    if article["title"]is not None:
        body = f"Subject: Today's {topic} news" + "\n" \
                    + body + article["title"] + "\n" \
                    + article["description"] + "\n" \
                    + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)