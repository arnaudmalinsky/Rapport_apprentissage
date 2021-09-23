import pandas as pd

PROJECT_DATA_FOLDER_PATH = "/home/container/notebooks/bases/missions-cways/webinauto_stock_vo/"

CONCATENATED_FILE_PATH = PROJECT_DATA_FOLDER_PATH + "concatenated_file/france-concat-16092021.xlsx"

IMMAT_FOLDER_PATH = PROJECT_DATA_FOLDER_PATH + "immats_VO/"

NEW_CONCAT_FILE = (
    PROJECT_DATA_FOLDER_PATH + "concatenated_file/france-concat-w-newimmats-16092021.xlsx"
)
sheet_dict = {
    "MARQUE": [
        "marque",
        ["stock_month", "stock_year", "b4_marque_ref"],
        ["mois", "annee", "marque"],
    ],
    "MARQUE MODELE": [
        "marque_modele",
        ["stock_month", "stock_year", "b4_marque_ref", "b4_denomination_comm_ref"],
        ["mois", "annee", "marque", "modele"],
    ],
    "DEPT": [
        "departement",
        ["stock_month", "stock_year", "dept_util"],
        ["mois", "annee", "departement"],
    ],
    "ENERGIE": [
        "energie",
        ["stock_month", "stock_year", "energie"],
        ["mois", "annee", "energie"],
    ],
}
writer = pd.ExcelWriter(  # pylint: disable=abstract-class-instantiated
    NEW_CONCAT_FILE, engine="xlsxwriter"
)
for sheet_stock_name, item in sheet_dict.items():

    sheet_concat_stock_pdf = pd.read_excel(CONCATENATED_FILE_PATH, sheet_name=sheet_stock_name)
    correspondant_immat_pdf = pd.read_csv(f"{IMMAT_FOLDER_PATH}vpo_{item[0]}.csv", sep=";")
    k = 0
    for column_name in item[2]:
        correspondant_immat_pdf = correspondant_immat_pdf.rename(columns={column_name: item[1][k]})
        k += 1
    if sheet_stock_name == "DEPT":
        correspondant_immat_pdf["dept_util"] = correspondant_immat_pdf["dept_util"].replace(
            {"2A": "20 - 2A", "2B": "20 - 2B"}
        )
    merged_pdf = (
        sheet_concat_stock_pdf.merge(correspondant_immat_pdf, on=item[1], how="inner")
        .drop("Immats mois passé", axis=1)
        .rename(columns={"sum(nb_vpo)": "Immats mois passé"})
        .to_excel(writer, sheet_name=sheet_stock_name)
    )
writer.save()
