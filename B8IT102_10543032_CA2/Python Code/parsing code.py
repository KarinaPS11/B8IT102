
# -*- coding: utf-8 -*-
"""
CCreated on Tue Feb 11 10:21:02 2020

@author: 10543032
"""

# Algorithm to process revision commit to svn.

from commit import Commit


DEBUG = True

# a better way to read the lines of the file into a list in memory
def get_data():
    return [line.strip() for line in open('C:/Users/Karina/OneDrive - Dublin Business School (DBS)/10543032_CA2/changes_python.log.txt')]



def get_commits(data):
    sep = 72 * '-'
    index = 0
    
    commits = []
    
    while index < len(data):
        try:
            details = data[index + 1].split(' | ')
            line_before_comment_index = data.index('',index + 1)
            index = data.index(sep, index + 1)
            comments = []            
            for comment_line in range(line_before_comment_index + 1, index):                  
                comments.append(str(data[comment_line]).replace('-----------','.  ').replace(',','-') )
            commits.append(Commit(details, comments))  
        except:
            index = len(data)
    return commits

 
def main():
    data = get_data()
    if DEBUG:
        print(len(data))
    
    commits = get_commits(data)
    
    if DEBUG:
        print(len(commits))
    save_csv(commits)

def save_csv(commits):    
    csv_file = open('C:/Users/Karina/OneDrive - Dublin Business School (DBS)/10543032_CA2/commits.csv', 'w')
    csv_file.write('revision,name,date,time,day,number, comment,\n')
    for commit in commits:
        csv_file.write(str(commit))
    csv_file.close()
    
main()
