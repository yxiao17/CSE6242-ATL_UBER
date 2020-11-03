import pandas as pd

def get_tsv(path,month,out):
    data = pd.read_csv(path, ",")
    del data["standard_deviation_travel_time"]
    del data["geometric_mean_travel_time"]
    del data["geometric_standard_deviation_travel_time"]
    is_month = data["month"] == month
    month_filtered = data[is_month]
    color = []
    for i in month_filtered["mean_travel_time"]:
        if i <=500:
            color.append("1")
        elif i>500  and i<=1000:
            color.append("2")
        elif i>1000 and i<=1500:
            color.append("3")
        elif i>1500 and i<=2000:
            color.append("4")
        else:
            color.append("5")
    ntest = month_filtered.assign(color=color)
#     ntest[ntest["sourceid"]==1]
    final_month = ntest.astype(str).groupby(['sourceid','month','color'])['dstid'].apply(', '.join).reset_index()
    final_month.index.names = ['']
    final_month.columns.names = ['index']
    print(final_month)
    final_month.to_csv("./"+out+".tsv", sep="\t")

get_tsv("../../Downloads/atlanta-censustracts-2019-1-All-MonthlyAggregate.csv", 3,"2019_03")