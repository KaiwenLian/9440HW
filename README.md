# Overview
- This is a repo for CIS 9440 HW 1 & 2. Dataset is picked from DATA.GOV (https://catalog.data.gov/dataset/electric-vehicle-population-data).
- Electric Vehicle Population Data
- This dataset shows the Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing (DOL).
- The insights I'm looking for: Will the electric range affect the market share of electric vehicles in Washington?


## Extract
- The extract was done by API web scraping. After extracting the data, raw data will be pushed to the GCP staging bucket. You can find the scripts in my ETL Scripts folder.


## Data Modeling
- Creating dimensional modeling, breaking down these sources into a data warehouse via Google Cloud Platform (GCP).
- Schema generated for Big Query can be found in my Data Modeling folder.
- For a data warehouse star schema based on this dataset, we can structure it as follows:
 ![image](https://github.com/KaiwenLian/9440HW/assets/77905682/13bad3c5-6c21-4227-9eba-c7c85046b14b)


## Transformation
- Transforming was done by Alteryx. The workflow can be found in my Data Modeling folder.
 ![image](https://github.com/KaiwenLian/9440HW/assets/77905682/66c36f9b-f9fd-4c78-90e2-83c4664c3ea6)

## Load
- The load was done by Pandas and Big Query. After transforming, cleaning, and consolidating the data using Alteryx, I loaded all results from csv files to panda data frames with slight adjustment. All data frames were uploaded to the data warehouse in the Google Cloud Platform. You can find the Transform & Load scripts in my ETL Scripts folder.

## Data Visualization
- Data visualization was one in Power BI.
- Analysis indicates that electric mileage isn't the only factor affecting electric vehicle (EV) ownership. The type of EV—plug-in versus battery-powered—also plays a critical role.
 - For plug-in EVs, buyers prefer models with the longest electric range to maximize energy savings.
 - In contrast, battery-powered EVs show a distinct trend: sales peak for ranges of 150-200 miles and drop off beyond 200 miles, suggesting that consumers consider this range optimal and do not value additional mileage.
![image](https://github.com/KaiwenLian/9440HW/assets/77905682/d7cb29a7-a684-4c97-98ca-2acbe3896769)
![image](https://github.com/KaiwenLian/9440HW/assets/77905682/bc0fc470-775e-4d6a-9d41-ac0ffd6e231c)







