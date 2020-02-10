# This program will read and write to a local file on disk, as well as rename that file based on input
# Joshua Snyder 02/08/2020

import os
def main()  :
    # First read file
    fileName = input('Enter file name: ')
    try:
        openedFile = open(fileName, 'r')
    except IOError:
        print('An Error occured when trying to open the file.')
    else:
        for line in openedFile  :
            print(line)
        response = input('Continue to write? (y/n) ')
        openedFile.close()

        # Now write in file
        if str(response.lower()).__contains__('yes') or str(response.lower()).__contains__('y')  :
            openedFile = open(fileName,'w')
            response = input('Enter new values for file: ')
            openedFile.writelines(response)
            response = input('Do you want to rename this file? ')
            if str(response.lower()).__contains__('yes') or str(response.lower()).__contains__('y')  :
                openedFile.close()
                newFileName = input('Enter new file name: ')
                os.rename(fileName, newFileName)
                openedFile.close()
                renamed = True
            openedFile.close()
            response = input('Read file again? (y/n) ')

            # Now read new file contents
            if str(response.lower()).__contains__('yes') or str(response.lower()).__contains__('y') :
                if (renamed)    :
                    openedFile = open(newFileName, 'r')
                else    :
                    openedFile = open(fileName, 'r')
                for line in openedFile  :
                    print(line)
                openedFile.close()
        
# Call program
main()