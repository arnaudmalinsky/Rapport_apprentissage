import sys

# from datetime import datetime

sys.path.insert(
    0, "/home/container/notebooks/missions-cways/webinauto-stock_vo/webinauto_stock_vo/"
)

from save_last_year_age_median_per_modele import save_last_year_age_median_per_modele

PROJECT_DATA_FOLDER_PATH = "/home/container/notebooks/bases/missions-cways/webinauto_stock_vo/"

CONCATENATED_FILE_PATH = (
    PROJECT_DATA_FOLDER_PATH + "concatenated_file/france-concat-w-newimmats-16092021.xlsx"
)

FINAL_OUTPUT_FILE_PATH = (
    PROJECT_DATA_FOLDER_PATH + "final_outputs/france-last-year-age-median-par-modele.xlsx"
)

save_last_year_age_median_per_modele(CONCATENATED_FILE_PATH, FINAL_OUTPUT_FILE_PATH)
