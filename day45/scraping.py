from bs4 import BeautifulSoup
import lxml

with open('website.html') as file:
    contents = file.read()
# syntax is
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(document,'parser')
soup = BeautifulSoup(contents, 'html.parser')
# retrieve objects
# print(type(soup.title))
# print(soup.title.string)
# # apply indentation
# print(soup.prettify())

# RETURN THE FIRST INSTANCE OF A SPECIFIC ELEMENT
# print(soup.a)
# # >>> <a href="https://www.appbrewery.co/">The App Brewery</a>
# print(soup.li)
# # >>> <li>The Complete iOS App Development Bootcamp</li>
# print(soup.p)
# >>> <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery<((v(vi

# CALLING ALL INSTANCES OF A SPECIFIC TAG
# find_all() takes a parameter name which expects the name of the tag you are looking for

all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
# [<a href="https://www.appbrewery.co/">The App Brewery</a>,
# <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

# Get all the text in all the 'a' tags
# for tag in all_anchor_tags:
#     # print(tag.getText())
# #     use the get() method to get the value of the attributes of the 'a tags
#     print(tag.get('href'))
    # returns all the links the href of the 'a' tag
    # https: // www.appbrewery.co /
    # https: // angelabauer.github.io / cv / hobbies.html
    # https: // angelabauer.github.io / cv / contact - me.html

# retrieve elements by class or id
heading = soup.find(name="h1", id="name")
print(heading)
# >>> <h1 id="name">Angela Yu</h1>

sctn_hdg = soup.find(name="h3", class_='heading')
print(sctn_hdg)
# >>><h3 class="heading">Books and Teaching</h3>
print(sctn_hdg.getText())
# >>> Books and Teaching
# getText() -returns the string inside the text
print(sctn_hdg.name)
# returns the name of the tag
print(sctn_hdg.get('class'))
# get returns the value of an attribute

# use find_all() to return all instances
h3_heading = soup.find_all("h3", class_="heading")
print(name)

name = soup.select_one(selector="#name")


