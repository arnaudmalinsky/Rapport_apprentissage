import sys

# from datetime import datetime

sys.path.insert(
    0, "/home/container/notebooks/missions-cways/webinauto-stock_vo/webinauto_stock_vo/"
)

from save_global_historic import save_global_historic_table

PROJECT_DATA_FOLDER_PATH = "/home/container/notebooks/bases/missions-cways/webinauto_stock_vo/"

CONCATENATED_FILE_PATH = (
    PROJECT_DATA_FOLDER_PATH + "concatenated_file/france-concat-w-newimmats-16092021.xlsx"
)

FINAL_OUTPUT_FILE_PATH = (
    PROJECT_DATA_FOLDER_PATH + "final_outputs/france-global-historic-2019-2021.xlsx"
)

save_global_historic_table(CONCATENATED_FILE_PATH, FINAL_OUTPUT_FILE_PATH)
