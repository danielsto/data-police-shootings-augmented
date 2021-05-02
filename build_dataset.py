import pandas as pd
import sys

ARROW_DOWN = "\U00002B07  "
FOLDER = "\U0001F4C1 "
CHECK = "\U00002714  "

def download_current_data():
    url = "https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv"
    return pd.read_csv(url)


if __name__ == "__main__":

    if "current" in sys.argv:
        print(f"{ARROW_DOWN}Downloading last available data from GitHub repository...")
        shootings = download_current_data()
    else:
        print(f"{FOLDER}Using local version, there's a more recent version of this dataset at https://github.com/washingtonpost/data-police-shootings")
        shootings = pd.read_csv("fatal-police-shootings-data.csv")

    census = pd.read_csv("statepop.csv", sep=";")

    # Join both dataframes by the state abbreviation
    res = pd.merge(shootings, census, on="state")

    res.to_csv("police-shootings-data-census.csv")
    print(f"{CHECK}Dataset written as police-shootings-data-census.csv in current working directory")
