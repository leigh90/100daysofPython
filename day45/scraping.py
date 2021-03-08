from bs4 import BeautifulSoup


with open('website.html') as website_file:
    contents = website_file.read()

# takes in parameters the content and the parser
soup = BeautifulSoup(contents, "html.parser")

print(soup)
# returns all the page contents
print(soup.prettify())
# indents the tags
print(soup.title)
# <title>Angela's Personal Site</title>
print(soup.title.string)
# Angela's Personal Site
print(soup.a)
# returns the first anchor tag it will find
# <a href="https://www.appbrewery.co/">The App Brewery</a>
# you can ask for any tag you want
all_a_tags = soup.find_all(name="a")
print(all_a_tags)
# get all the tags you want
# [<a href="https://www.appbrewery.co/">The App Brewery</a>, <a href="https://angelabauer.github.io/cv/hobbies.html">My Hobbies</a>, <a href="https://angelabauer.github.io/cv/contact-me.html">Contact Me</a>]

for tag in all_a_tags:
    # print(tag.getText())
# access the text within each tag
    print(tag.get("href"))
# access the value of any attribute e.g href
'''
The App Brewery
https://www.appbrewery.co/
My Hobbies
https://angelabauer.github.io/cv/hobbies.html
Contact Me
https://angelabauer.github.io/cv/contact-me.html

'''

# you can search by attribute and/or id
heading = soup.find(name="h1", id="name")
print(heading)
# <h1 id="name">Angela Yu</h1>

section = soup.find(name="h3", class_="heading")
print(section)
# <h3 class="heading">Books and Teaching</h3>
# .get() method
print(section.getText())
# Books and Teaching
print(section.get('class'))
# ['heading']

# what if you want to drill down to a specific tag without knowing where it is you can use css selectors
# use select()-returns all the occurence matching your selector AND
# select_one() - returns the first occurence
company_url = soup.select_one(selector="p a")
print(company_url)
name = soup.select_one(selector="#name")
print(name)

header=soup.select(".heading")
# returns a list of tags matching your selectors
print(header)





