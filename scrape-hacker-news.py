import requests
from bs4 import BeautifulSoup
import pprint

# Objective: Grab title and link of posts with over 100 votes

response1 = requests.get('https://news.ycombinator.com/news')
soup1 = BeautifulSoup(response1.text, 'html.parser')

posts1 = soup1.select('.titleline > a')
subtext1 = soup1.select('.subtext')

response2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(response2.text, 'html.parser')

posts2 = soup2.select('.titleline > a')
subtext2 = soup2.select('.subtext')

posts = posts1 + posts2
subtext = subtext1 + subtext2


def sorting_list(hn_list):
    return sorted(hn_list, key=lambda score: score['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sorting_list(hn)


my_list = create_custom_hn(posts, subtext)
print()
pprint.pprint(my_list)
