# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 00:42:08 2015

@author: J
@contributor: Ian


"""
from clean_data import get_soup, scrape_page, pretty_courses
import user_input
import back_up_db
import urllib
import shelve
import itertools

def process_url(url):
    soup = get_soup(url)
    terms = [term.get('value') for term in soup.find_all('option')]
    return terms

def main():
    url = r'http://ycpweb.ycp.edu/schedule-of-classes/'
    soup = get_soup(url)
    terms = [term.get("value") for term in soup.find_all('option')
                if len(term.get("value")) == 6]                    
    schedules = [schedule.get("value") for schedule in soup.find_all('option')
                    if len(schedule.get("value"))==1]
    
    queries = [urllib.urlencode(
    
                                  {
                                    'term' : term,
                                    'stype' : schedule
                                  }
                )
                                            for term in terms
                                                for schedule in schedules
            ]
    urls = [url + 'index.html?' + q for q in queries]
    urls = [[url + '&' + urllib.urlencode({  
                                        'dmode' : 'D',
                                        'dept' : term
                                }
                )
                                for term in process_url(url)]
                                                    for url in urls]
    class_info = shelve.open('ycp_classes_1.db')
    counter = itertools.count()
    try:
        for urlgroup in urls:
            for url in urlgroup:
                for course in scrape_page(url):
                    class_info[str(counter.next())] = course
                    pretty_courses(course)
                    print "\n"
    finally:
        class_info.close()            

    print '', counter.next()-1, "courses!"
    back_up_db.backup()
    
if __name__ == '__main__':
    main()