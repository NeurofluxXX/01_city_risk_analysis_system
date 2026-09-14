import geopandas as gpd
from shapely.geometry import Point
import pandas as pd
import matplotlib.pyplot as plt
import json
from shapely.geometry import Polygon

def create_city_gdf(data):
    geometry = [Point(x,y)
                for x,y in zip(data["longitude"],data["latitude"])]
    gdf = gpd.GeoDataFrame(data,geometry=geometry,crs="EPSG:4326")
    return gdf

def calculate_distance(gdf,target_city):
    gdf_projected = gdf.to_crs("EPSG:3857")
    target_geometry = gdf.projected.loc[gdf_projected["city"] == target_city,"geometry"].iloc[0]
    gdf_projected["distance_km"] = gdf_projected.geometry.distance(target_geometry)/1000
    return gdf_projected

cities = {
    "city":["上海","南京","杭州","苏州","无锡"],
    "risk":[0.85,0.60,0.75,0.45,0.70],
    "longitude":[121.47,118.78,120.15,120.58,120.30],
    "latitude":[31.23,32.04,30.27,31.30,31.57]
}

df = pd.DataFrame(cities)

geometry = [Point(x,y) for x,y in zip(df["longitude"],df["latitude"])]

gdf = gpd.GeoDataFrame(df,geometry=geometry,crs="EPSG:4326")

gdf_projected = gdf.to_crs("EPSG:3857")

shanghai_geometry = gdf_projected.loc[gdf_projected["city"]=="上海","geometry"].iloc[0]

gdf_projected["distance_to_shanghai_m"] = gdf_projected.geometry.distance(shanghai_geometry)
gdf_projected["distance_to_shanghai_km"] = gdf_projected["distance_to_shanghai_m"]/1000

other_cities = gdf_projected[gdf_projected["city"] != "上海"]

nearest_city = other_cities.sort_values(by="distance_to_shanghai_km",ascending=True).iloc[0]

print(gdf_projected[["city","risk","distance_to_shanghai_km"]])
#gdf.plot()
#plt.show()

print(f"距离上海最近的城市是："
      f"{nearest_city['city']},"
      f"距离为"
      f"{nearest_city['distance_to_shanghai_km']:.2f}公里")

# 导出GeoJSON（不依赖fiona/pyogrio）
geojson_str = gdf.to_json()
with open("../output/city_risk.geojson", "w", encoding="utf-8") as f:
    json.dump(json.loads(geojson_str), f, ensure_ascii=False, indent=2)

polygon = Polygon([(120,30),
    (122,30),
    (122,32),
    (120,32)
])

regions = gpd.GeoDataFrame({"region":["上海区域"]},geometry = [polygon],crs="EPSG:4326")

gpd.sjoin(gdf,regions,predicate="within")

