import requests
import json
import webbrowser

"""

time stamp - znak czasu

1 stycznia 1970


"""

from datetime import datetime, timedelta

timeBefore = timedelta(days=7)

searchDate = datetime.today() - timeBefore


params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : int(searchDate.timestamp()),
    "tagged" : "python",

}


r = requests.get("https://api.stackexchange.com/2.2/questions/", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        webbrowser.open_new_tab(question["link"])


