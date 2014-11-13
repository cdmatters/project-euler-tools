from bs4 import BeautifulSoup, SoupStrainer
import requests
import io

def get_problem_info(raw_html):
    strainer = SoupStrainer(class_='problem_content')
    problemSoup = BeautifulSoup(raw_html, 'html.parser', parse_only=strainer)

    imageurls = []
    problemdict = {}

#ongoing formatting of problems

    image = problemSoup.find_all('img')
    count = 1
    for i in image:
        imageurls.append(i['src'])
        i.string = '[IMAGE %s]' % count
        count += 1
        print  '\t' + i['src']


    superscripts = problemSoup.find_all('sup')
    for s in superscripts:
        if s.text:
            s.string = '^'+s.text + ''


    subscripts = problemSoup.find_all('sub')
    for s in subscripts:
        if s.text:
            s.string = '.sub('+s.text+')'



    problemdict = {
                'text' : problemSoup.get_text(),
                'images' :imageurls
                }

    return problemdict


if __name__ == '__main__':

    r = requests.get('https://projecteuler.net/problem=316', verify=False)
    hey = get_problem_info(r.text)

    with io.open('test2.txt','w', encoding='utf8') as f:
        f.write(hey['text'])
        f.write(unicode('\n\n'))
        for link in hey['images']:
            f.write(unicode('https://projecteuler.net/'+link+'\n'))



