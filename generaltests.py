#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup #html parser
import urllib
import re
import argparse
import  os


parser = argparse.ArgumentParser(description='Test in Websites use selenium ')
parser.add_argument('--file',default="output", help='file name without extension')
parser.add_argument('--search',default="site:wwww.test.com", help='terms to search')
parser.add_argument('--searchkeys',default="test:alberto", help='terms to search')
parser.add_argument('--keyword',default='test1;test2:alber;erto',help='multiple words "word1i;word2" separate by semicolom')
#parser.add_argument( '--keyword', action='store', dest='alist',type=str, nargs='*', default=['item1', 'item2','item3'], help="Examples: -i item1  item2, -i item3")
parser.add_argument('--engine',default="google", help='search engine to find results')
parser.add_argument('--type',default="count_h3_st", help='search engine to find results')
parser.add_argument('--test',default="false", help='test mode read from file')
parser.add_argument('--headless',default="true", help='headless mode activated')
parser.add_argument('--identifier',default="www.example.com", help='Search identifier')
args = parser.parse_args()
print(args.keyword.split(";"))

class Browsertest (unittest.TestCase):
    def __init__(self,test):
        self.url = test.url
        self.search = test.search
        self.keyword = test.keyword
        self.count = test.count
        if  args.headless == 'true':
            self.headless = True
        else:
            self.headless = False
    def init_driver(self):
        print('loading..')
        self.driver=webdriver.Firefox()
    def init_remote_driver(self):

        options=Options()
        if self.headless == True:
            #this server is headless
           command ='http://127.0.0.1:4444/wd/hub'

        else:
           #this server is with head to visual inspection 
           command ='http://127.0.0.1:4445/wd/hub'
        print('loading..')
        self.driver = webdriver.Remote(
                   command_executor=command,
                   browser_profile=webdriver.FirefoxProfile("/home/agalan/.mozilla/firefox/ac7cwnzt.auto"),
                   desired_capabilities={
                       'browserName':'firefox',
                   'javascriptEnabled':True})
    def readhtml_test(self,file):
        # read html from a file
        # for fast testing and have a clear test framework
        print('reading file '+ file)
        f = open(file, "r")
        html=f.read() 
        return html
    def robot_detection(self,html):
        soup= BeautifulSoup(html,"lxml")
        a=soup.find("title")
        if "www.google.com" in soup.title.string:
            return True
        else:
            return False

    def test_google_tag(self,html,tag,keywords,search):
        soup= BeautifulSoup(html,"lxml")
        result=soup.find_all(tag)
        tt=[]
        for ky in keywords:
          data=[x for x in result if  ky in str(x).lower() ]
          tt.append([search+"."+ky+"."+tag,len(data)])
        return tt

    def test_google_class (self,html,clas,keywords,search):
        soup= BeautifulSoup(html,"lxml")
        result=soup.find_all(class_=clas)
        tt=[]
        for ky in keywords:
          data=[x for x in result if  ky in str(x).lower() ]
          tt.append([search+"."+ky+"."+clas,len(data)])
        return tt

    def parse_keyword (self,html,parser,keyword):
        # parse html with a specific parser
        # result an array of text with the matching 
        # result=['a','b','c']
        soup= BeautifulSoup(html,"lxml")
        result=soup.find_all(parser,text=keyword)
        #result=getattr(soup,parser)
        return result

    def parse_extract_element(self,html,parser,element):
        # parse html with a specific parser
        # extract specific element  
        # result is a dictionary array with     
        # {text: aaa , element:'<a>aaa<a>'}
        print('parse_extract_element')
        return result

    def count_keywords(self,arraylist,keyword):
        # count number of matches in an array
        # result is an interger
        return count

    def google_link_extraction(self,html):
        return aaa


    def test_page(self):
        driver=self.driver
        driver.get(self.url)
        self.assertIn("hello",driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    def html_browser(self):
        driver=self.driver
        driver.get(self.url)
        html = driver.page_source
        return html

    def teardown(self):
        self.driver.close()

    def count_keywords(self,html,regex):
        soup = BeautifulSoup(html,"lxml")
        counter = 0
        for hit in soup.findAll(regex):
            print (self.testkeyword ," ",hit.text)
            if self.testkeyword in hit.text.lower():
                counter = counter + 1
        print("number of counts are: " + str(counter))
        return counter

def iszero (num):
    """TODO: Docstring for iszero .
    :returns: TODO

    """
    if num != 0:
        return 1
    else:
        return 0

# Create test as a function:  <03-04-19, yourname> # 
# Make easy data filtering 
#  Data input : test.py  site:xxxx  "s1;s2;s3" "w11;w12;w13::w21;w22;w23::w31;w32"
#  Data ouput (counting the results) : identifier site:xxxx;s1.h3.w11;s1.st.h3.w11;..... " 
#  Data output (set as positive if searched): identifier .....

def test1_scrap_google(test):
    """scrap count words h3 and st in Google search

    :test: TODO
    :returns: string with the results to write in a file

    """
    pass
def merge(list1, list2): 
    merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
    return merged_list 

def umerge(list):
    list1=[list[i][0] for i in range(0,len(list))]
    list2=[list[i][1] for i in range(0,len(list))]
    return [list1,list2]

def wrapresults(res1,res2,identifier,search,keywords):
    d=[]
    d.append(identifier)
    d.append(search)
    d.extend(list(map(str,res1)))
    d.extend(list(map(str,res2)))
    return d

def resolve_robot(test):
    """TODO: Docstring for resolve_robot.
   """
    br2 = Browsertest(test)
    br2.search=args.search
    br2.keyword=args.keyword
    br2.headless=False
    br2.init_remote_driver()
    br2.html_browser()
    assert False , "Robot detection fix manually firefox -p auto"

MyObject = type('MyObject', (object,), {})
test = MyObject()

if args.engine == "google":
   test.url=    'https://www.google.com/search?source=hp&ei=9bScXNWqI87i-AaXyqbADw&q='+ urllib.parse.quote_plus(args.search)
   tagname="h3"
   keyword=args.keyword
   test.search=args.search
   test.keyword=args.keyword
   test.type="h3"
   test.count=3

br1 = Browsertest(test)

if args.test == 'false':
   br1.init_remote_driver()

data=[]
head=[]

# Multiple search iterating from searchs
# merge concatena [[s1,k1],[s2,k2],[s3,k3]]
# k1 could be string of multiple keywords k;kk;kkk
for [sky,ky] in merge(args.searchkeys.split(":"),args.keyword.split(":")):
   br1.search=args.search + ' ' + sky
   if args.test == 'true':
       print('testing not browsing')
       print("query: " + br1.search)
       html=br1.readhtml_test('./tests/html-alberto.html')
   else:
       html=br1.html_browser()

# IF robot detention, then resolve the issue
   if (br1.robot_detection(html)):
     print ('robot detection')
     resolve_robot(test,initparam)
   else:
     # Adding data in a single list  
     data.extend(br1.test_google_tag(html,"h3",ky.split(";"),sky))
     data.extend(br1.test_google_class(html,"st",ky.split(";"),sky))
     head.append(sky+"."+ky+".st")

line=[]
line.append(args.identifier)
line.append(args.search)
line.extend(data)
print (head)
if args.test == 'true':
   print ("this is a test")
   print( line )
else:
   br1.teardown()
   with open(args.file +".csv", 'a') as file:
      print( datares )
      file.write( line+"\n" )

