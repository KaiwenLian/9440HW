# Overview
- This is a repo for CIS 9440 HW 1 & 2. Dataset is picked from DATA.GOV (https://catalog.data.gov/dataset/electric-vehicle-population-data).
- Electric Vehicle Population Data
- This dataset shows the Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing (DOL).
- Insights: Examine how electric range impacts the popularity and perceived value of vehicles (correlation with MSRP and type of electric vehicle).


## Extract
- The extract was done by API web scraping. After extracting the data, raw data will be pushed to the GCP staging bucket. You can find the scripts in my ETL Scripts folder.


## Data Modeling
- Creating dimensional modeling, breaking down these sources into a data warehouse via Google Cloud Platform (GCP).
- Schema generated for Big Query can be found in my Data Modeling folder.
- For a data warehouse star schema based on this dataset, we can structure it as follows:
<img width="1163" alt="image" src="https://github.com/KaiwenLian/9440HW/assets/77905682/7194bd0c-d2ae-488f-86fe-26520b5f5020">

## Transform
- Transforming was done by Alteryx. The workflow can be found in my Data Modeling folder.
![image](https://github.com/KaiwenLian/9440HW/assets/77905682/66c36f9b-f9fd-4c78-90e2-83c4664c3ea6)



