# List of open-source scrapers
# scrapy

# 1. Get list of names of studies given some specifications: US, 2014 - Present, enrolling 
# 2. Given name, download machine-readable fields in XML format 

## -- 

## Constants 

xml_str_pre  = "https://clinicaltrials.gov/show/" 
xml_str_post = "?displayxml=true"

## File Names 

study_fields = "study_fields.tsv"

import pandas
from pandas import read_table 
import csv 

study_fields_table = read_table( study_fields )



