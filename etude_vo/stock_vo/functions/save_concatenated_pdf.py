from pathlib import Path
import pandas as pd


def save_concatenated_pdf(input_directory_str, concatenated_file_path):
    month_stock_path_list = list(Path(input_directory_str).rglob("*.xlsx"))
    month_stock_vo_pdf_dict = {"MARQUE": [], "MARQUE MODELE": [], "DEPT": [], "ENERGIE": []}

    for month_stock_path in month_stock_path_list:
        for key, item in month_stock_vo_pdf_dict.items():
            item += [_import_monthly_stock_vo_file(str(month_stock_path), key)]

    _write_pdf_to_excel(month_stock_vo_pdf_dict, concatenated_file_path)

    print("fichier sauvegardé !")


def _write_pdf_to_excel(month_stock_vo_pdf_dict, concatenated_file_path):
    writer = pd.ExcelWriter(  # pylint: disable=abstract-class-instantiated
        concatenated_file_path, engine="xlsxwriter"
    )
    for key, item in month_stock_vo_pdf_dict.items():
        concatenated_pdf = pd.concat(item).reset_index(drop=True)
        if "MARQUE" in key:
            concatenated_pdf = _merge_with_segment_pdf(concatenated_pdf)
        concatenated_pdf.to_excel(writer, sheet_name=key)
    writer.save()


def _merge_with_segment_pdf(concatenated_pdf):
    segment_pdf_path = "/home/container/notebooks/bases/missions-cways/webinauto_stock_vo/"
    segment_pdf_path += "other_ressources/gamme_segmentation_v2.csv"
    segment_to_join_pdf = pd.read_csv(segment_pdf_path)
    merged_pdf = concatenated_pdf.merge(segment_to_join_pdf, on="b4_marque_ref", how="left")
    return merged_pdf


def _import_monthly_stock_vo_file(month_stock_path_str, sheet_name):
    month_stock_vo_pdf = pd.read_excel(month_stock_path_str, sheet_name=sheet_name)
    stock_pdf_date, stock_pdf_year, stock_pdf_month = _get_stock_date(month_stock_path_str)
    month_stock_vo_pdf["stock_date"] = stock_pdf_date
    month_stock_vo_pdf["stock_date"] = pd.to_datetime(
        month_stock_vo_pdf["stock_date"], infer_datetime_format=True
    )
    month_stock_vo_pdf["stock_year"] = stock_pdf_year
    month_stock_vo_pdf["stock_year"] = month_stock_vo_pdf["stock_year"].astype(int)
    month_stock_vo_pdf["stock_month"] = stock_pdf_month
    month_stock_vo_pdf["stock_month"] = month_stock_vo_pdf["stock_month"].astype(int)
    return month_stock_vo_pdf


def _get_stock_date(month_stock_path):
    stock_pdf_date = month_stock_path[-22:-12]
    stock_pdf_year = month_stock_path[-22:-18]
    stock_pdf_month = month_stock_path[-17:-15]
    return stock_pdf_date, stock_pdf_year, stock_pdf_month
