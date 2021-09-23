import pandas as pd
from cmaps.layers import PlainLayer, Choropleth
from cmaps.map import Map
from cmaps.tools import Cut, CustomBinsColor
from cmaps.legends import Legend

PROJECT_DATA_FOLDER_PATH = "/home/container/notebooks/bases/missions-cways/webinauto_stock_vo/"

FINAL_OUTPUT_FILE_PATH = (
    PROJECT_DATA_FOLDER_PATH + "final_outputs/france-historic-per-dept-last-year.xlsx"
)


data_choropleth = pd.read_excel(
    FINAL_OUTPUT_FILE_PATH,
    dtype={"dept_util": str},
)
data_choropleth["dept_util"] = data_choropleth["dept_util"].replace(
    {"20 - 2A": "2A", "20 - 2B": "2B"}
)
data_choropleth = data_choropleth[data_choropleth["mean_ratio_immat_sur_stock"] != 0]

map_test = PlainLayer(
    scale="departement",
)

cut = Cut(
    data=data_choropleth,
    column_to_cut="mean_ratio_immat_sur_stock",
    bins_list=[0.0, 2.0, 2.25, 2.5, 3],
)

custom_color = CustomBinsColor(
    cut,
)

choropleth = Choropleth(
    data=data_choropleth,
    column_to_plot="mean_ratio_immat_sur_stock",
    column_to_join="dept_util",
    custom_color=custom_color,
    add_legend=True,
    legend_title=["Ratio immatriculations sur stock VO des 12 derniers mois"],
)


legend = Legend(box=(1.61, 1), legend_background_color="white", legend_precision=2)

test_map = Map(
    legend=legend,
    map=map_test,
    choropleth=choropleth,
)

test_map.plot(
    output_file="mean_ratio_immat_sur_stock_16092021.png",
    title="Moyenne sur 12 mois du ratio Immatriculations sur stock VO",
)
