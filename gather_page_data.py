# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 00:42:08 2015

@author: J
@contributor: Ian


"""
from clean_data import get_soup, scrape_page
import urllib
#import shelve
#import itertools
from pymongo import MongoClient

def dbtest():
    pass

def process_url(url):
    soup = get_soup(url)
    terms = [term.get('value') for term in soup.find_all('option')]
    return terms

def main():
    client = MongoClient()
    course_catalog = client.course_catalog
    courses = course_catalog.collection
    course_catalog.drop_collection(courses)
    
    headings = ['CRN',
                'Course',
                'Title',
                'Credits',
                'Type',
                'Days',
                'Times',
                'LOC',
                'Instructor',
                'Seats',
                'Open',
                'Enrolled',
                'Dates',
                'Year',
                'Times'  ]    
    
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
    
    for urlgroup in urls:
        for url in urlgroup:
            for course in scrape_page(url):
                entry = dict(zip(headings, course))
                courses.insert(entry)
                print courses.count()
            
    print '', courses.count(), "courses!"
    print courses.find_one({"Instructor": "Kaplan"})

   
if __name__ == '__main__':
    main()