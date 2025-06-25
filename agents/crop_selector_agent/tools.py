import pandas as pd

df = pd.read_csv("data/crop_yield.csv")
df = df[df["Crop_Year"] >= 2015]

def get_best_crops(state: str, season: str):
    filtered = df[
        (df["State"].str.strip() == state) &
        (df["Season"].str.strip() == season)
    ]

    if filtered.empty:
        return "No Crop found for that State and Season"

    grouped = (
        filtered.groupby("Crop").agg({
            "Yield" : "mean",
            "Annual_Rainfall" : "mean",
            "Fertilizer" : "mean",
            "Pesticide" : "mean",
            "Area" : "sum" # remove this later
        }).sort_values(by="Yield", ascending=False).head(3).reset_index()
    )

    return grouped.to_dict(orient="records")




