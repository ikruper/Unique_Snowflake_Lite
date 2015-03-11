# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 02:42:53 2015

@author: Ian
"""

import shelve
import os
import shutil
import cPickle

def backup():
    ycp_courses = shelve.open('ycp_classes_1.db')
    
    try:
        with open('backup_db.txt', 'w') as f:
            contents = str(ycp_courses.__repr__)
            f.write(contents)
    finally:
        ycp_courses.close()
        
    print "Done!"
    
def main(): #Test to see if working
    backup()
    with open('backup_db.txt', 'r') as f:
        print f.readline()
    
if __name__=='__main__':
    main()