import datetime
import pandas as pd


def save_last_year_historic_per_dept(concatenated_file_path, output_file_path):
    concat_pdf = pd.read_excel(
        concatenated_file_path,
        sheet_name="DEPT",
        dtype={"dept_util": str},
    )

    date_minus_one_year = concat_pdf["stock_date"].max() - datetime.timedelta(days=365)

    concat_pdf = concat_pdf[concat_pdf["stock_date"] > date_minus_one_year]
    concat_pdf["ratio_immat_sur_stock"] = (
        concat_pdf["Immats mois passé"] / concat_pdf["TOTAL Stocks VO"]
    )
    historic_per_dept_pdf = (
        concat_pdf.groupby(["dept_util"])
        .agg(
            mean_ratio_immat_sur_stock=("ratio_immat_sur_stock", "mean"),
        )
        .reset_index()
    )
    historic_per_dept_pdf["dept_util"] = historic_per_dept_pdf["dept_util"].astype(str)
    # historic_per_dept_pdf = historic_per_dept_pdf.pivot(index="stock_date", columns="dept_util")
    historic_per_dept_pdf.to_excel(output_file_path)  # , float_format="%.2f"
