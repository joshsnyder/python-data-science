# This program is an example parsing a csv file and importing into Python
# Joshua Snyder - 04/05/2020

import csv
import xlrd
import sys

def ExceltoCSV(excel_file, csv_file_base_path):
    workbook = xlrd.open_workbook(excel_file)
    for sheet_name in workbook.sheet_names():
        print(f'processing - {sheet_name}') 
        worksheet = workbook.sheet_by_name(sheet_name)
        csv_file_full_path = csv_file_base_path + sheet_name.lower().replace(" - ", "_").replace(" ","_") + '.csv'
        csvfile = open(csv_file_full_path, 'wt')
        writetocsv = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for rownum in range(worksheet.nrows):
            writetocsv.writerow(
                list(x.encode('utf-8') if type(x) == type(u'') else x for x in worksheet.row_values(rownum)
                )
            )
        csvfile.close()
    print(f'{sheet_name} has been saved - {csv_file_full_path}')
if __name__ == '__main__':
    ExceltoCSV(excel_file = "C:\code\Git\Python\dataScience\python-data-science\module11\COVID19_03242020_ByCounty.xlsx", csv_file_base_path = "C:\code\Git\Python\dataScience\python-data-science\module11\output")