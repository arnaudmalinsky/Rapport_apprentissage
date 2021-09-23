import datetime
import pandas as pd


def save_last_year_age_median_per_modele(concatenated_file_path, output_file_path):
    concat_pdf = pd.read_excel(concatenated_file_path, sheet_name="MARQUE MODELE")

    date_minus_one_year = concat_pdf["stock_date"].max() - datetime.timedelta(days=365)

    concat_pdf = concat_pdf[concat_pdf["stock_date"] > date_minus_one_year]

    age_median_par_marque_pdf = (
        concat_pdf.groupby(["b4_denomination_comm_ref"])
        .agg(
            effectif=("b4_denomination_comm_ref", "size"),
            sum_stock_entier=("TOTAL Stocks VO", "sum"),
            sum_immat_vo=("Immats mois passé", "sum"),
            mean_age_median=("Âge médian stock", "mean"),
        )
        .reset_index()
        .sort_values(by="sum_immat_vo", ascending=False)
        .iloc[:20]
    )

    age_median_par_marque_pdf.to_excel(output_file_path)
