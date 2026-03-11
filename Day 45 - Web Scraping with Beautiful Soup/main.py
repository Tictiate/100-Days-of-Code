from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
site = response.text

soup = BeautifulSoup(site, "html.parser")

movies = soup.find_all(name="h3", class_ = "title")
print(movies)

with open("movies.txt", "w") as file:
    for movie in movies[::-1]:
        file.write(movie.getText() + "\n")