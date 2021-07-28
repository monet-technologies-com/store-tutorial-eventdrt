# ぴあAPIで取得したイベント情報を利用しやすい形に加工
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import xmltodict
import json
import csv
import datetime

# 一旦ぴあAPIのレスポンスを保存して、そちらを読み込む
with open("example/events.xml", "r") as f:
    data = f.read()

# CSV形式にコンバート
d = xmltodict.parse(data)
with open("example/events.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "venueCode", "venueName", "venueLat", "venueLon"])

    event_releases = d["result"]["eventReleases"]["eventRelease"]
    idx = 1
    for event_release in event_releases:
        event = event_release["event"]
        performs = event_release["performs"]["perform"]
        if not isinstance(performs, list):
            performs = [performs]

        for perform in performs:
            venue = perform["venue"]
            venue_name = venue["venueName"]
            venue_code = venue["venueCode"]
            if ("worldLatitude" not in venue.keys()) or ("worldLongitude" not in venue.keys()):
                continue

            venue_lat = float(venue["worldLatitude"])
            venue_lon = float(venue["worldLongitude"])

            # 東京会場のみに絞る
            if venue["prefectureCode"] != "13":
                continue

            writer.writerow(
                [idx, venue_code, venue_name, venue_lat, venue_lon])
            idx += 1

# イベント会場を抽出
df = pd.read_csv("example/events.csv")
df_reduced = df.loc[:, ["venueCode", "venueName", "venueLat", "venueLon"]]
df_reduced = df_reduced.drop_duplicates()
df_reduced.to_csv("example/venues.csv", index=False)

# イベント会場をまとめたポイントを生成

df = pd.read_csv("example/venues.csv")

# イベント会場を7クラスタに分割
staNum = 7
kmeans_model = KMeans(n_clusters=staNum, random_state=10).fit(
    df.loc[:, ["venueLat", "venueLon"]])
labels = kmeans_model.labels_
print("---assigned label---")
print(labels)
print("---------")

df["nearestPointId"] = labels + 1
df.to_csv("example/fixed_venues.csv", index=False)

with open("example/reduced_venues.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "meanLat", "meanLon"])
    for i in range(staNum):
        name = f"イベント会場{i+1}"
        mean_lat = df[df["nearestPointId"] == (i+1)].mean()["venueLat"]
        mean_lon = df[df["nearestPointId"] == (i+1)].mean()["venueLon"]
        writer.writerow([i + 1, name, mean_lat, mean_lon])

print("done!!!")
