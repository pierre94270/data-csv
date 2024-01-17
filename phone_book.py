import csv

#url='https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/phone_book.csv > data/phone_book.csv'

"""with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        print(f"{row[1]}: {row[2]}" )
        line_count += 1"""
        
with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
    #line_count = 0
    for row in csv_reader:
        print(row['last_name'] +': '+ row['phone_number'] )
        #line_count += 1
#print(type(row))
