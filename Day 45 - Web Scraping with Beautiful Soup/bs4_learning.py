from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

article_texts = []
article_links = []

spans = soup.find_all(name="span", class_ = "titleline")
for span in spans:
    article_tag = span.contents[0]
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)




# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# #
# # print(soup.prettify())
# #
# # print(soup.a)
#
# # all_anchor_tags = soup.find_all(name="a")
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# headings = soup.select(".heading")
# print(headings)