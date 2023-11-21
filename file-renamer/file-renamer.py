import os #File and Directory function
import shutil #Move/Copy functions
from datetime import datetime #Date/Time manipulation

#Setting up the Sort directory to be used as the container for files to sort
sort_dir = "Sort"
all_files = os.listdir(sort_dir)

#Iterating over all files/folders in the Sort folder
for file in all_files:

    file_path = os.path.join(sort_dir,file) #Joining the Sort directory with the file name to create a usable path
    if os.path.isfile(file_path): #If the iterable is not a file it will break and continue to next iterable

        mod_time = os.path.getmtime(file_path) #Fetching file modification date. 
        date = datetime.fromtimestamp(mod_time) #Formatting the time into a readable timestamp

        year = date.strftime("%Y") #Retrieving Year from timestamp
        month = date.strftime("%m - %B")#Retrieving Month from timestamp
        year_month_path = os.path.join(sort_dir,year,month) #Creating a Year/Month/file path

        #If the path is not already created it will be created
        if not os.path.exists(year_month_path): 
            os.makedirs(year_month_path)

        shutil.move(file_path, os.path.join(year_month_path, file)) #Move the file to its new folder. 
    
print('Completed') #Print statment as confirmation operation is complete