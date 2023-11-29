# DATA PROCESSING AUTOMATION WITH APACHE AIRFLOW
 
 <p align="left"> <img src="https://komarev.com/ghpvc/?username=aeronaut2001&label=Profile%20views&color=0e75b6&style=flat" alt="aeronaut2001" /> </p>
 
[![View My Profile](https://img.shields.io/badge/View-My_Profile-green?logo=GitHub)](https://github.com/aeronaut2001) 
 [![View Repositories](https://img.shields.io/badge/View-My_Repositories-blue?logo=GitHub)](https://github.com/aeronaut2001?tab=repositories)

---

## Automate daily processing and analysis of CSV files stored in Google Cloud Storage using Apache Airflow and Google Cloud Dataproc.
📝 Gain the skills 
---

 <h3 align="left">Languages and Tools:</h3>

<p align="left"> Cloud: </p>

<a href="https://cloud.google.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/google_cloud/google_cloud-icon.svg" alt="gcp" width="40" height="40"/> </a> </p>

<p align="left"> Version Control System: </p>

 <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> </p>

<p align="left"> Programming Language - PYTHON: </p>
    <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 

<p align="left"> BIG DATA TOOL AND SOFTWARES: </p> 
  <a href="https://hadoop.apache.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/apache_hadoop/apache_hadoop-icon.svg" alt="hadoop" width="40" height="40"/> </a> 
  <a href="https://hive.apache.org" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Apache_Hive_logo.svg" alt="Apache Hive" width="40" height="40"/> </a> 
  <a href="https://spark.apache.org" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg" alt="Apache Spark" width="40" height="40"/> </a> 
<a href="https://www.linux.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> </p>

<p align="left"> WORKFLOW MANAGEMENT: </p> 
<a href="https://airflow.apache.org" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png" alt="Apache Airflow" width="40" height="40"/> </a></p>
 
 ---

## 📙 Project Structures :

- [x] **Project Introduction:**
-  Daily CSV Analysis on Google Cloud Platform
- [x] **Cluster Management:**
-  Creates a Dataproc cluster to execute PySpark jobs for data processing.
-  Deletes the cluster upon completion to optimize costs.
- [x] **Data Processing Workflow:**
-  GCS Sensor checks for the existence of a daily CSV file (orders_{date}.csv) in the specified bucket (daily-csv-files).
-  PySpark job (spark_job_for_project.py) processes the CSV data, performing various analyses like product category counts, discount calculations, top-rated products identification, etc.
- [x] **Storage and Analysis:**
-  Processed results are stored as Hive tables in a database (flipkart_analysis), facilitating efficient querying and further analysis of insights derived from the daily CSV files.
- [x] **Data Backfilling:**
-  The system is designed to handle backfilling of historical data, ensuring that previous dates' CSV files are processed seamlessly for complete and consistent historical analysis.
- [x] **PySpark Data Processing::**
-  SparkSession Initialization:
    -  The PySpark script initializes a SparkSession named "DataprocOrderProcessing" to interact with Spark APIs and perform distributed data processing.
-  Input Data Retrieval:
    -  Reads the input CSV file (gs://{bucket}/orders_{formatted_date}.csv) from Google Cloud Storage into a Spark DataFrame.
-  Data Processing Operations:
    -  Product Category Count: tilizes groupBy() to count the number of products in each category.
    -  Discount Calculation: alculates the average discount percentage across all products.
    -  Top-Rated Products: dentifies top-rated products by sorting based on product rating and selecting the top 10.
    -  Brand Counts: Determines the most common brands and their respective counts.
    -  FK Advantage Products: Filters FK Advantage products and counts them separately.
    -  Hive Table Creation and Data Saving.
    -  Creates a database named flipkart_analysis if it doesn't exist.
    -  Saves the processed results as Hive tables (category_count, average_discount, highest_rated_products, brand_counts, fk_advantage_products) within the flipkart_analysis database.
-  SparkSession Termination:
    -  Properly stops the SparkSession to release resources after data processing is complete.
-  Error Handling: Incorporates error handling to manage potential failures during data processing.



- [x] **Key Takeaways:**
- The project's objective is to automate the extraction of valuable insights from daily CSV files. It provides a robust framework for both daily processing and historical data backfilling, ensuring comprehensive analysis and decision-making based on the stored insights.
