# Overview

This is a repo for CIS 9440 HW 1 & 2. Dataset is picked from DATA.GOV (https://catalog.data.gov/dataset/electric-vehicle-population-data).

- Electric Vehicle Population Data
- This dataset shows the Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing (DOL).
- Insights: Examine how electric range impacts the popularity and perceived value of vehicles (correlation with MSRP and type of electric vehicle).


## Extract

- The extract was done by API web scraping. You can find the script in **"9440_HW1_KaiwenLian.ipynb"**

## Transform

- Transforming was done by Alteryx. The workflow can be found here:


## Data Modeling
- Creating dimensional modeling, breaking down these sources into a data warehouse via Google Cloud Platform (GCP). 
- For a data warehouse star schema based on this dataset, we can structure it as follows:
<img width="1163" alt="image" src="https://github.com/KaiwenLian/9440HW/assets/77905682/7194bd0c-d2ae-488f-86fe-26520b5f5020">


- Schema generated for Big Query can be found in **"Dimensional Modeling Schema"**

