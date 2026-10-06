\# E-commerce Data Engineering \& Analytics Pipeline



A complete \*\*Data Engineering project\*\* implementing an ETL pipeline to process, transform, store, and analyze e-commerce sales data.



The project demonstrates the main stages of a modern data workflow:



\*\*Extract → Transform → Load → Analyze\*\*



The pipeline processes raw sales data, cleans and transforms it using Python and Pandas, loads it into PostgreSQL running with Docker, and performs business-oriented data analysis and visualization.



\## 🎯 Project Objectives



\* Build an end-to-end ETL pipeline using Python.

\* Clean and transform raw e-commerce data.

\* Store structured data in PostgreSQL.

\* Perform SQL and Pandas-based data analysis.

\* Implement data quality checks.

\* Generate business KPIs and insights.

\* Visualize sales performance using Matplotlib.

\* Practice Git and GitHub for project versioning and portfolio development.



\## 🏗️ Pipeline Architecture



```text

Raw CSV Data

&#x20;    │

&#x20;    ▼

&#x20; Extract

&#x20;    │

&#x20;    ▼

&#x20; Transform

(Python / Pandas)

&#x20;    │

&#x20;    ▼

&#x20; Clean Data

&#x20;    │

&#x20;    ▼

&#x20;  Load

(PostgreSQL)

&#x20;    │

&#x20;    ▼

&#x20;  Analyze

(SQL / Pandas)

&#x20;    │

&#x20;    ▼

Visualization \& KPIs



\## 🛠️ Technologies



| Category               | Technologies            |

| ---------------------- | ----------------------- |

| Programming            | Python                  |

| Data Processing        | Pandas                  |

| Database               | PostgreSQL              |

| Database Driver        | psycopg2                |

| Visualization          | Matplotlib              |

| Environment Management | python-dotenv           |

| Containerization       | Docker / Docker Compose |

| Data Analysis          | SQL / Pandas            |

| Version Control        | Git / GitHub            |



\## 🔄 ETL Pipeline



\### 1. Extract



Raw e-commerce sales data is provided as a CSV file containing information such as:



\* Order ID

\* Order date

\* Product

\* Category

\* Quantity

\* Unit price

\* City



The raw data is loaded and processed using Python.



\### 2. Transform



The transformation phase cleans and prepares the data before loading it into the database.



Main operations include:



\* Data type conversion

\* Date normalization

\* Data validation

\* Revenue calculation

\* Data consistency checks

\* Generation of a cleaned dataset



The transformed data is stored in:



```text

data/sales\_clean.csv

```



\### 3. Load



The cleaned data is loaded into a \*\*PostgreSQL database\*\* running inside a Docker container.



The main table is:



```text

sales

```



with fields including:



```text

order\_id

order\_date

product

category

quantity

unit\_price

city

total\_amount

```



\### 4. Analyze



The stored data is analyzed using both \*\*SQL and Pandas\*\*.



The analysis covers:



\* Revenue by city

\* Revenue by product

\* Revenue by category

\* Monthly revenue

\* Average Order Value (AOV)

\* Product contribution

\* Sales KPIs

\* Business performance indicators



\## 📊 Data Analysis \& Results



The project includes several business-oriented analyses to evaluate e-commerce performance.



\### 💰 General KPIs



| KPI                 |  Result |

| ------------------- | ------: |

| Total Revenue       | 770,455 |

| Total Orders        |   1,000 |

| Units Sold          |   3,027 |

| Average Order Value |  770.46 |



\### 🏙️ Revenue by City



The analysis shows that \*\*Tangier\*\* generated the highest revenue:



| City       | Revenue |

| ---------- | ------: |

| Tangier    | 131,655 |

| Oujda      | 119,825 |

| Marrakech  | 117,125 |

| Casablanca | 109,370 |

| Agadir     | 104,600 |

| Rabat      |  94,440 |

| Fes        |  93,440 |



\### 🏆 Top Products by Revenue



| Product    | Revenue | Contribution |

| ---------- | ------: | -----------: |

| Laptop     | 277,500 |       36.02% |

| Smartphone | 166,500 |       21.61% |

| Tablet     |  78,900 |       10.24% |

| Desk       |  70,750 |        9.18% |

| Monitor    |  60,500 |        7.85% |



The \*\*Laptop and Smartphone\*\* together represent approximately \*\*57.63% of total revenue\*\*.



\### 📅 Monthly Revenue



The highest monthly revenue was recorded in \*\*September 2026\*\*, with:



```text

105,950

```



\### 🔎 Key Business Insights



\* \*\*Laptop\*\* is the best-performing product by revenue.

\* \*\*Tangier\*\* is the highest-revenue city.

\* \*\*Electronics\*\* is the dominant product category.

\* Laptop and Smartphone account for more than half of total revenue.

\* September 2026 was the strongest month in terms of revenue.

\* The dataset contains \*\*1,000 orders\*\* and \*\*3,027 units sold\*\*.



> Note: October contains only a small number of orders in the dataset, so its monthly revenue should not be compared directly with complete months.



\## ✅ Data Quality



Data quality checks were implemented before and during the analysis phase.



The following validations were performed:



\* Null value detection

\* Duplicate record detection

\* Validation of positive quantities

\* Validation of positive unit prices

\* Validation of positive revenue values

\* Verification of calculated revenue:



```text

total\_amount = quantity × unit\_price

```



\### Validation Results



| Check                          | Result |

| ------------------------------ | -----: |

| Null values                    |      0 |

| Duplicate records              |      0 |

| Invalid quantities             |      0 |

| Invalid prices                 |      0 |

| Invalid revenue values         |      0 |

| Revenue calculation mismatches |      0 |



The dataset passed all implemented data quality checks.



\## 📁 Project Structure



```text

ecommerce-data-eng/

│

├── data/

│   ├── sales.csv

│   └── sales\_clean.csv

│

├── src/

│   ├── analyze.py

│   ├── create\_tables.sql

│   ├── db\_connection.py

│   ├── generate\_data.py

│   ├── load.py

│   └── transform.py

│

├── .gitignore

├── docker-compose.yml

├── requirements.txt

└── README.md

```



\### Main Components



\*\*`generate\_data.py`\*\*

Generates the raw e-commerce dataset.



\*\*`transform.py`\*\*

Cleans and transforms the raw data.



\*\*`load.py`\*\*

Loads the cleaned dataset into PostgreSQL.



\*\*`create\_tables.sql`\*\*

Defines the PostgreSQL database schema.



\*\*`db\_connection.py`\*\*

Handles the PostgreSQL database connection.



\*\*`analyze.py`\*\*

Performs data analysis, KPI calculations, data quality checks, and visualizations.



\## 🚀 Installation \& Setup



\### 1. Clone the repository



```bash

git clone https://github.com/Sabchaymae/ecommerce-data-eng.git

cd ecommerce-data-eng

```



\### 2. Create a virtual environment



On Windows:



```powershell

python -m venv .venv

.venv\\Scripts\\activate

```



\### 3. Install dependencies



```powershell

pip install -r requirements.txt

```



\### 4. Configure environment variables



Create a `.env` file in the project root:



```env

DB\_HOST=localhost

DB\_PORT=5433

DB\_NAME=ecommerce

DB\_USER=datauser

DB\_PASSWORD=datapass

```



> The `.env` file is excluded from Git using `.gitignore`.



\### 5. Start PostgreSQL with Docker



Make sure Docker Desktop is running, then:



```powershell

docker compose up -d

```



Verify that the PostgreSQL container is running:



```powershell

docker ps

```



\### 6. Create the database table



Execute the SQL schema:



```powershell

psql -h localhost -p 5433 -U datauser -d ecommerce -f src/create\_tables.sql

```



\### 7. Run the ETL pipeline



Transform the raw data:



```powershell

python src/transform.py

```



Load the cleaned data into PostgreSQL:



```powershell

python src/load.py

```



\### 8. Run the analysis



```powershell

python src/analyze.py

```



The analysis generates:



\* Business KPIs

\* Revenue analysis

\* Product performance analysis

\* City performance analysis

\* Monthly revenue analysis

\* Data quality reports

\* Matplotlib visualizations



\## 📌 Future Improvements



Possible extensions for this project include:



\* Building a dashboard with Power BI

\* Adding automated ETL scheduling with Apache Airflow

\* Adding unit and integration tests

\* Implementing incremental data loading

\* Containerizing the complete ETL pipeline

\* Adding a cloud data warehouse such as BigQuery or Snowflake



