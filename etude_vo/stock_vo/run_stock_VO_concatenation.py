# import pandas as pd
import sys

# from datetime import datetime

sys.path.insert(
    0, "/home/container/notebooks/missions-cways/webinauto-stock_vo/webinauto_stock_vo/"
)

from save_concatenated_pdf import save_concatenated_pdf

# from save_monthly_stock_table import save_monthly_stock_table

PROJECT_DATA_FOLDER_PATH = "/home/container/notebooks/bases/missions-cways/webinauto_stock_vo/"

INPUTS_FOLDER_PATH = PROJECT_DATA_FOLDER_PATH + "input_files_from_autoways/"

CONCATENATED_FILE_PATH = PROJECT_DATA_FOLDER_PATH + "concatenated_file/france-concat-16092021.xlsx"

# FINAL_OUTPUT_FOLDER_PATH = PROJECT_DATA_FOLDER_PATH + "final_outputs/"

save_concatenated_pdf(INPUTS_FOLDER_PATH, CONCATENATED_FILE_PATH)

# save_monthly_stock_table(CONCATENATED_FILE_PATH, FINAL_OUTPUT_FOLDER_PATH)
