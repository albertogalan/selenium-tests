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
parser.add_argument('--file',default="output.txt", help='output file')
parser.add_argument('--search',default="test alberto", help='terms to search')
parser.add_argument('--keyword',default='alberto;gala',help='multiple words "word1i;word2" separate by semicolom')
#parser.add_argument( '--keyword', action='store', dest='alist',type=str, nargs='*', default=['item1', 'item2','item3'], help="Examples: -i item1  item2, -i item3")
parser.add_argument('--engine',default="google", help='search engine to find results')
parser.add_argument('--type',default="count_h3_st", help='search engine to find results')
parser.add_argument('--test',default="false", help='test mode read from file')
args = parser.parse_args()
print(args.keyword.split(";"))

class Browsertest (unittest.TestCase):
    def __init__(self,test):
        self.url = test.url
        self.search = test.search
        self.keyword = test.keyword
        self.count = test.count
    def init_driver(self):
        print('loading..')
        self.driver=webdriver.Firefox()
 
    def init_remote_driver(self):

        options=Options()
        options.headless = True
        print('loading..')
        self.driver = webdriver.Remote(
                   command_executor='http://127.0.0.1:4444/wd/hub',
                   browser_profile=webdriver.FirefoxProfile("/home/agalan/.mozilla/firefox/ac7cwnzt.auto"),
                   desired_capabilities={
                       'browserName':'firefox',
                   'javascriptEnabled':True})
    def readhtml_test(self,file):
        # read html from a file
        # for fast testing and have a clear test framework
        print('readhtml')
        f = open(file, "r")
        html=f.read() 
        return html
    def robot_detection(self,html):
        soup= BeautifulSoup(html)
        a=soup.find("title")
        if "www.google.com" in soup.title.string:
            return True
        else:
            return False

    def test_google_tag(self,html,tag):
        soup= BeautifulSoup(html)
        result=soup.find_all(tag)
        tt=[]
        for ky in self.keyword.split(';'):
          data=[x for x in result if  ky in str(x).lower() ]
          tt.append(len(data))
        return tt

    def test_google_class (self,html,clas):
        soup= BeautifulSoup(html)
        result=soup.find_all(class_=clas)
        tt=[]
        for ky in self.keyword.split(';'):
          data=[x for x in result if  ky in str(x).lower() ]
          tt.append(len(data))
        return tt

    def parse_keyword (self,html,parser,keyword):
        # parse html with a specific parser
        # result an array of text with the matching 
        # result=['a','b','c']
        soup= BeautifulSoup(html)
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

    def test_words(self):
        driver=self.driver
        driver.get(self.url)
        #elem = driver.find_element_by_name("q")
        #elem.send_keys(self.keyword)
        #elem.send_keys(Keys.RETURN)
      #  assert "No results found." not in driver.page_source
        # load complete HTML file
        html = driver.page_source

        # regular expression
        #result=re.findall(self.keyword,body)
        #print(result.count(self.keyword)) 
        # search HTML file
        total = self.count_keywords(html,'h3')
        try:
            assert (total) > self.count
            print('hypothesis true')
        except AssertionError:
            print("hypothesis failed")

    def teardown(self):
        self.driver.close()

    def count_keywords(self,html,regex):
        soup = BeautifulSoup(html)
        counter = 0
        for hit in soup.findAll(regex):
            print (self.testkeyword ," ",hit.text)
            if self.testkeyword in hit.text.lower():
                counter = counter + 1
        print("number of counts are: " + str(counter))
        return counter


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
br1.search=args.search
br1.keyword=args.keyword

if args.test == 'true':
   html=br1.readhtml_test('./tests/html-alberto.html')
else:
   br1.init_remote_driver()
   html=br1.html_browser()
assert not (br1.robot_detection(html)), "Robot detection fix manually firefox -p auto"
 
res=br1.test_google_tag(html,"h3")
res2=br1.test_google_class(html,"st")
print("total count h3 " + str(res))
print("total count st " + str(res2))

result=""
idx=0
for ky in args.keyword.split(";"):
    result=result+( args.search +";" + ky +";"+args.type+";"+ str(res[idx])+";"+
            str(res2[idx]) +"\n")
    idx=idx+1

if args.test == 'true':
   print ("this is a test")
   print( result )
else:
   br1.teardown()
   with open(args.file, 'a') as file:
      #file.write("\"" + args.search +"\"" + )
      print( result )
      file.write( result )

