# The purpose of this program is to analyze a regional grouping of addresses and their validity against a popular address validation API.
# The json input file has already been run against the address validation API to gather their statistics on the input address list.
# The intent of this program is to now analyze this outout from the address validation API and conclude on the error rate of manual 
# user entry via an ERP system, versus validation against a popular USPS address validation API. Additionally, extracting additional 
# interesting information from the data set.
#
# Joshua Snyder 04/25/2020
#   

import pandas as pd

# Global variables for analysis
valid_count = 0
valid_perct = 0.0
invalid_count = 0
invalid_perct = 0.0
high_lat_long_count = 0
low_lat_long_count = 0
lat_long_precision_perct = 0.0
highest_lat_long_precision = "Zip9"
total_count_size = 0
total_nan_count = 0

# Additional interesting information
# dpv codes (delivery point validations via USPS mailing capabilities)
total_bb_count = 0 # BB code indicates a 100% confirmed address based on input
total_bb_perct = 0.0
total_cc_count = 0 # CC code indicates a confirmed address, but only by dropping the secondary input address info
total_cc_perct = 0.0
total_dpv_count = 0 # summary of all dpv code counts denoted above
total_n1_count = 0 # N1 code indicates a confirmed address, but is missing the secondary input address info
total_n1_perct = 0.0

def main() :
    inputAnswer = input('Is data local to solution? (Y/N): ')
    if inputAnswer == "y" or inputAnswer == "Y":
        file_name = ".\\final\\addressList.csv"
    else:
        file_name = input('Enter file location: ')
    try:
        # import csv into dataframe
        df = pd.read_csv(file_name)
    except IOError:
        print('An Error occured when trying to open the file.')
    else:
        # Output entire data frame
        print(df)
        global total_count_size
        total_count = df.count(1)
        total_count_size = total_count.size
        
        ############################################################
        # Analyze dataframe and compute various counts/percentages #
        ############################################################
        # Address validity
        (valid_count, invalid_count, valid_perct, invalid_perct) = analyze_validity(df, total_count_size)
        # Address validity precision
        (high_lat_long_count, low_lat_long_count, lat_long_precision_perct, total_nan_count) = analyze_latlong_precision(df)
        # Address validity dpv codes
        (total_bb_count, total_cc_count, total_n1_count, total_dpv_count, total_bb_perct, total_cc_perct, total_n1_perct) = analyze_dpv_codes(df)
        
        # Output analysis
        print("======================================================")
        print("                   Analysis Output                    ")
        print("======================================================")
        print(f'Total count: {str(total_count_size)}')
        print(f'Total valid: {str(valid_count)}')
        print(f'Total valid percentage: {str(valid_perct)}')
        print("======================================================")
        print(f'Total count: {str(total_count_size)}')
        print(f'Total invalid: {str(invalid_count)}')
        print(f'Total invalid percentage: {str(invalid_perct)}')
        print("======================================================")
        print(f'Total NAN count: {str(total_nan_count)}')
        print(f'Total high lat/long precision count: {str(high_lat_long_count)}')
        print(f'Total low lat/long precision count: {str(low_lat_long_count)}')
        print(f'Total high lat/long precision percentage: {str(lat_long_precision_perct)}')
        print("======================================================")
        print("          Additional Analysis Output (DPV Codes)      ")
        print("======================================================")
        print(f'Total DPV count: {str(total_dpv_count)}')
        print(f'Total DPV BB code count: {str(total_bb_count)}')
        print(f'Total DPV BB code percentage: {str(total_bb_perct)}')
        print(f'Total DPV CC code count: {str(total_cc_count)}')
        print(f'Total DPV CC code percentage: {str(total_cc_perct)}')
        print(f'Total DPV N1 code count: {str(total_n1_count)}')
        print(f'Total DPV N1 code percentage: {str(total_n1_perct)}')
        print("======================================================")

def analyze_validity(df, int) :
    for element in df.isvalidated :
            if element == True :
                global valid_count
                valid_count = (valid_count + 1)
            else:
                if element == False :
                    global invalid_count
                    invalid_count = (invalid_count + 1)

    # Compute percentages
    global valid_perct
    global invalid_perct
    valid_perct = (valid_count/total_count_size)
    invalid_perct = (invalid_count/total_count_size)

    return (valid_count, invalid_count, valid_perct, invalid_perct)    

def analyze_latlong_precision(df) :
    for element in df.latlongprecision :
            if not pd.isna(element) and element == highest_lat_long_precision :
                global high_lat_long_count 
                high_lat_long_count = (high_lat_long_count + 1)
            else:
                if not pd.isna(element) and element != highest_lat_long_precision :
                    global low_lat_long_count
                    low_lat_long_count = (low_lat_long_count + 1)
    
    # Compute percentages
    global lat_long_precision_perct
    global total_nan_count
    total_nan_count = (high_lat_long_count + low_lat_long_count)
    lat_long_precision_perct = (high_lat_long_count/total_nan_count)
    
    return (high_lat_long_count, low_lat_long_count, lat_long_precision_perct, total_nan_count)

def analyze_dpv_codes(df) :
    # Split out all dpv codes from column based on pipe delimiter
    dpv_codes = []
    for element in df.dpvfootnotes :
        if not pd.isna(element) :
            dpv_split = element.split(" | ")
            # iterate over dpv split to ensure element doesn't already exist in list
            for dpv_code in dpv_split :
                dpv_code_counter(dpv_code)
                if dpv_code not in dpv_codes :
                    # Not found in list, add it
                    dpv_codes.append(dpv_code)
    
    # Compute counts/percentages
    global total_dpv_count
    global total_bb_perct
    global total_cc_perct
    global total_n1_perct
    total_dpv_count = (total_bb_count + total_cc_count + total_n1_count)
    total_bb_perct = (total_bb_count/total_dpv_count)
    total_cc_perct = (total_cc_count/total_dpv_count)
    total_n1_perct = (total_n1_count/total_dpv_count)

    return (total_bb_count, total_cc_count, total_n1_count, total_dpv_count, total_bb_perct, total_cc_perct, total_n1_perct)

def dpv_code_counter(dpv_code) :
    global total_bb_count
    global total_cc_count
    global total_n1_count
    if dpv_code == "BB - ZIP+4 matched; confirmed entire address; address is valid" :
        total_bb_count = (total_bb_count + 1)
    if dpv_code == "CC - Confirmed address by dropping secondary (apartment, suite, etc.) information" :
        total_cc_count = (total_cc_count + 1)
    if dpv_code == "N1 - Confirmed with missing secondary information; address is valid but it also needs a secondary number (apartment, suite, etc.)" :
        total_n1_count = (total_n1_count + 1)

# Execute main program
main()
