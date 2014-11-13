#engine.py
#this runs the scraper

import problemscraper as PS
import contentscraper as CS
import requests
import time
import sqlite3
import os
import shutil



headers = {'User-Agent': "CondnsdMattersbot",
            'Email':'condnsdmatters@gmail.com',
            'Purpose':'Learning to Code'}

class Engine(object):
    
    def __init__(self):
        self.domain = 'https://projecteuler.net/'
        self.startpoint = 'problems'
        self.contentlinks = []
        self.problemlinks = []
        self.time = time.time()
        if not os.path.isfile('PE.db'):
            self.db_setup()
            self.run()



    def get_response_content(self, add_on):
        url = self.domain + add_on
        r = requests.get( url, verify=False, headers=headers, stream=True)
        
        timer = int(time.time()-self.time)
        lap = str(timer/60)+':'+str(timer%60) 
        print lap, r.status_code, url

        time.sleep(2)
        return r

    def db_setup(self):
        if os.path.exists('images'):
            shutil.rmtree('images')
        os.makedirs('images')

        with sqlite3.connect('PE.db') as connection:
            cur = connection.cursor()
            cur.execute("CREATE TABLE Project_Euler (\
                Number Integer, Title Text, Text Text, \
                SolveCount Integer, Date Text,\
                Completed Integer, ImageUrl Text, WebUrl Text)")

            connection.commit()
        connection.close()
        print 'database created: PE.db'
        pass

    def store_contents(self, contentlinks):     
        with sqlite3.connect('PE.db') as connection:
            cur = connection.cursor()

            for problem in contentlinks:

                record = (problem['no'], problem['title'],
                        problem['count'], problem['date'], problem['url'])

                cur.execute('INSERT INTO Project_Euler \
                            VALUES(?,?,"Empty",?,?,0,"Empty",?)', record)

                self.problemlinks.append(problem['url'])

            connection.commit()
        connection.close()
        pass
    
    def store_problems(self, problemdata, url):
        with sqlite3.connect('PE.db') as connection:
            cur = connection.cursor()

            record = (problemdata['text'], str(problemdata['images']), url)

            cur.execute('UPDATE Project_Euler SET Text=?, ImageUrl=?\
                        WHERE WebUrl = ?', record)
            connection.commit()
        connection.close()

        if problemdata['images']:
            for link in problemdata['images']:
                r = self.get_response_content(link)
                
                title = link.split('/')
                fname = 'images/%s'%title[-1]
                
                if r.status_code == 200:
                    with open(fname, 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)                            
                       
        pass



    def run(self):
        
        self.time = time.time()
        print time.asctime()
        begin = self.get_response_content(self.startpoint)
        self.contentlinks = CS.get_page_links(begin.text)

        for link in self.contentlinks:
            html = self.get_response_content(link).text
            data = CS.get_problem_data(html)          
            self.store_contents(data)

        for link in self.problemlinks:
            html = self.get_response_content(link).text
            data = PS.get_problem_info(html)
            self.store_problems(data, link)
        pass

    def directory_test(self, data):

        with sqlite3.connect('PE.db') as connection:
            cur= connection.cursor()

            cur.execute('SELECT Text FROM Project_Euler \
                        WHERE Number=? ', (data['no'],))
            result = cur.fetchall() 
            
            if result:
                return True               
            else:
                return False           

                           

    def updater(self):
        #NEED TO INPUT LINES TO UPDATE THE SOLVE COUNT for DIRECTORY
        self.time = time.time()
        print time.asctime()
        begin = self.get_response_content(self.startpoint)
        self.contentlinks = CS.get_page_links(begin.text)

        for link in self.contentlinks:
            html = self.get_response_content(link).text
            data = CS.get_problem_data(html)
 
            while True:
                test = data.pop()
                
                if self.directory_test(test):
                    break
                print "NEW:", test['no'], test['title']
                print "  ", test['date']
                self.store_contents([test])
                if not data:
                    print 'PAGE ADDED'
                    break

        print 'DIRECTORY is Up to Date'        

        with sqlite3.connect('PE.db') as connection:
            cur = connection.cursor()

            cur.execute('SELECT WebUrl FROM Project_Euler\
                        WHERE Text="Empty" ORDER BY Number')
            linktuples = cur.fetchall()
            
        connection.close()

        for ltuple in linktuples:
            p_link = ltuple[0]
            p_html = self.get_response_content(p_link).text
            p_data = PS.get_problem_info(p_html)
            self.store_problems(p_data, p_link)

        print 'DATABASE is Up to Date'

        pass



if __name__ == '__main__':

    e = Engine()
    e.updater()
    print 'done'