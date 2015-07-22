import csv
from itertools import chain
from string import maketrans
import html2text
import HTMLParser
import unicodedata

class CSVPipeline(object):

   def __init__(self):
      self.csvwriter = csv.writer(open('Output.csv', 'wb'), delimiter=b',')
      self.csvwriter.writerow(['names','date','location','starts','subjects','reviews'])

   def process_item(self, item, ampa):

      for i in range(len(item['names'])):
         item['names'][i] = item['names'][i].encode('utf-8','ignore')
         
      for a in range(len(item['date'])):
         item['date'][a] = item['date'][a].encode('utf-8','ignore')
         
      for b in range(len(item['location'])):
         item['location'][b] = item['location'][b].encode('utf-8','ignore')
         
      for c in range(len(item['stars'])):
         item['stars'][c] = item['stars'][c].encode('utf-8','ignore')
         
      for d in range(len(item['subjects'])):
         item['subjects'][d] = item['subjects'][d].encode('utf-8','ignore')
         
      for e in range(len(item['reviews'])):
         item['reviews'][e] = item['reviews'][e].encode('utf-8','ignore')
         

      rows = zip(item['names'],item['date'],item['location'],item['stars'],item['subjects'],item['reviews'])

      for row in rows:
         self.csvwriter.writerow(row)#[item['names'][i],item['date'][i],item['location'][i],item['stars'][i],item['subjects'][i],item['reviews'][i]])
      

##      for row in bruh:
##         self.csvwriter.writerow(row)

      

      
      return item



      
