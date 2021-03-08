from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
print(response)

y_webpage = response.text
soup = BeautifulSoup(y_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
# print(articles)
# article_text = articles.getText()
# article_link = articles.get("href")
# print(article_link)
# article_upvote = soup.find_all(name="span", class_="score")
# print(article_upvote)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_upvotes)
article_texts = []
article_links = []
article_upvote = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

most_votes = max(article_upvotes)
print(most_votes)
largest_index = article_upvotes.index(most_votes)
print(largest_index)

print(article_texts[largest_index])
print(article_links[largest_index])



# print(article_texts)
# print(article_links)
# print(article_upvotes)

# instead of the list comprehension
# article_upvotes = soup.find_all(name="span", class_="score")
# vote_tally = []
# for vote in article_upvotes:
#     vote = vote.getText().split()[0]
#     # vote = vote.split()[0]
#     vote_tally.append(int(vote))
# print(vote_tally)










