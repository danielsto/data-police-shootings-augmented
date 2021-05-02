# data-police-shootings-augmented
Augmented Washington Post's Fatal Force dataset using [original dataset](https://github.com/washingtonpost/data-police-shootings) and United States census data from 2017.

## Install dependencies

```bash
pip3 install requirements.txt
```

## Run

### Makefile (only Python 3+):

To generate the dataset using local version of `fatal-police-shootings-data.csv` included in this repository (April 2021)
```bash
make run
```
To generate the dataset using last available version of `fatal-police-shootings-data.csv` from Washington Post's [original repository](https://github.com/washingtonpost/data-police-shootings)

```bash
make current
```

### Without Makefile

To generate the dataset using local version of `fatal-police-shootings-data.csv` included in this repository (April 2021)
```bash
python build_dataset.py
```
To generate the dataset using last available version of `fatal-police-shootings-data.csv` from Washington Post's [original repository](https://github.com/washingtonpost/data-police-shootings)

```bash
python build_dataset.py current
```

## Data sources

[1] [The Washington Post](https://github.com/washingtonpost/data-police-shootings)  
[2] [U.S. Census Bureau](https://www.census.gov/newsroom/press-kits/2018/acs-1year.html)


