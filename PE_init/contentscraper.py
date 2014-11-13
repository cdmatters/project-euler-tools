from bs4 import BeautifulSoup, SoupStrainer
import requests

#This program gets all useful data from the problems page of PE


def get_page_links( raw_text):
    strainer = SoupStrainer('div', class_ = "pagination")
    PagesSoup = BeautifulSoup(raw_text, "html.parser", parse_only=strainer)
    crawl_urls = []
    
    for linkSoup in PagesSoup.find_all('a'):
        link = linkSoup.get('href')
        crawl_urls.append(link)

    c_urls = list(set(crawl_urls))
    c_urls.sort()

    return c_urls

def get_problem_data( raw_text):
    strainer = SoupStrainer('table')
    PagesSoup = BeautifulSoup(raw_text, "html.parser", parse_only=strainer)

    dict_list = []

    soupList = PagesSoup.find_all('tr')
    soupList.pop(0)

    for problemSoup in soupList:
        mini_dict = {}
        #print problemSoup.prettify(), '\n\n\n'

        prob_no = problemSoup.td.text
        url = problemSoup.a['href']
        upload_date = problemSoup.a['title']
        title = problemSoup.a.text
        solve = problemSoup.div.text

        mini_dict = {
            'url': url,
            'no' : prob_no,
            'date' : upload_date,
            'title' : title,
            'count' : solve
            }
        
        dict_list.append(mini_dict)

    return dict_list


if __name__ == '__main__':
    r = requests.get( 'https://projecteuler.net/problems', verify=False)
    html =  r.text
    print get_page_links(html)
    print get_problem_data(html)

