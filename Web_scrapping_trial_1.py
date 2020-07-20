import requests   
import bs4
from bs4 import BeautifulSoup
page = requests.get('https://www.livescience.com/24310-flat-earth-belief.html')
content_list = []

soup = BeautifulSoup(page.text, 'html.parser')# BeautifulSoup object
body_tag = soup.body
article_body = soup.find("div", id = "article-body" )
article_body_children = article_body.children
for html_tag in article_body :
  if isinstance(html_tag, bs4.element.Tag) :
    content_list.append(html_tag.get_text())

txt_file = open("Txt_Trial_1.txt",'r+')
txt_file.truncate(0) # clearing file before writing
txt_file.seek(0) # pointing cursor ar initial position
for line in content_list :
  txt_file.write(line)
  txt_file.write("\n")

txt_file.close()
