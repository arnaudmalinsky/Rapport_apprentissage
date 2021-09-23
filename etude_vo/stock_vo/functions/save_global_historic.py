import pandas as pd


def save_global_historic_table(concatenated_file_path, output_file_path):
    concat_pdf = pd.read_excel(concatenated_file_path, sheet_name="MARQUE")

    historic_pdf = (
        concat_pdf.groupby(["stock_date"])
        .agg(
            count_marque=("b4_marque_ref", "size"),
            sum_stock_entier=("TOTAL Stocks VO", "sum"),
            sum_immat_vo=("Immats mois passé", "sum"),
            sum_stock_0_1=("0 - 01 an", "sum"),
            sum_stock_1_2=("01 - 02 ans", "sum"),
            sum_stock_2_5=("02 - 05 ans", "sum"),
            sum_stock_5_7=("05 - 07 ans", "sum"),
            sum_stock_7_10=("07 - 10 ans", "sum"),
            mean_age_median=("Âge médian stock", "mean"),
            median_age_median=("Âge médian stock", "median"),
        )
        .reset_index()
    )
    historic_pdf["ratio_immat_sur_stock"] = (
        historic_pdf["sum_immat_vo"] / historic_pdf["sum_stock_entier"]
    )
    historic_pdf.to_excel(output_file_path)
