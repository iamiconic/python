import os
import shutil
from datetime import datetime

all_files = os.listdir(os.getcwd())

for file in all_files:


    if os.path.isfile(file):

        mod_time = os.path.getmtime(file)
        date = datetime.fromtimestamp(mod_time)


        year = date.strftime("%Y")
        month = date.strftime("%B")
        year_month_path = os.path.join(year,month)

        if not os.path.exists(year_month_path):
            os.makedirs(year_month_path)


        shutil.copy2(file, os.path.join(year_month_path, file))