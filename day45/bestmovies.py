from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify())
# Get the list of movies
movies = soup.find('h3',class_="jsx-2692754980")


print(movies)
# class_="jsx-2692754980"
# print(movies[3].prettify())
# <div class="jsx-2692754980 listicle-header">
# <span class="jsx-2692754980 icon">
# <svg aria-labelledby="icon_labelledby_3819992" style="width:1.5rem;height:1.5rem" viewbox="0 0 24 24">
# <title id="icon_labelledby_3819992">Gallery</title>
# <path d="M22,16V4A2,2 0 0,0 20,2H8A2,2 0 0,0 6,4V16A2,2 0 0,0 8,18H20A2,2 0 0,0 22,16M11,12L13.03,14.71L16,11L20,16H8M2,6V20A2,2 0 0,0 4,22H18V20H4V6" style="fill:currentColor"></path></svg></span>
# <h2 class="jsx-2692754980">Empires 100 Greatest Movies Of All Time</h2></div>

