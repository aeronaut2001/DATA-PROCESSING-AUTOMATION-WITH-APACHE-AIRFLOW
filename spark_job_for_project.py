from pyspark.sql import SparkSession
from datetime import datetime


def process_data(input_file_name):
    # Create a Spark session
    spark = SparkSession.builder.appName("DataprocOrderProcessing").getOrCreate()

    try:
        # Extract the date part from the input file name
        date_str = input_file_name.split('_')[1]

        # Convert the date part from 'YYYYMMDD' to '%Y-%m-%d' format
        formatted_date = datetime.strptime(date_str, "%Y%m%d").strftime("%Y-%m-%d")
        # strptime (string parse time) from the datetime module to parse the date_str variable

        # Define your GCS bucket and paths
        bucket = "daily-csv-files"
        # Define the path where the files are located for the given date
        input_path = f"gs://{bucket}/orders_{formatted_date}.csv"
        output_path = f"gs://{bucket}/daily_analysis_{formatted_date}.csv"

        # Read dataset
        df = spark.read.csv(input_path, header=True, inferSchema=True)

        # 1. Count the number of products in each category
        category_count = df.groupBy("product_category_tree").count().orderBy("count", ascending=False)

        # 2. Calculate average discount percentage across all products
        average_discount = df.select(((df["retail_price"] - df["discounted_price"]) / df["retail_price"]) * 100) \
            .agg({"((retail_price - discounted_price) / retail_price) * 100": "avg"})

        # 3. Identify products with the highest ratings
        highest_rated_products = df.orderBy(df["product_rating"].desc()).select("product_name", "product_rating").limit(
            10)

        # 4. Determine the most common brands and their counts
        brand_counts = df.groupBy("brand").count().orderBy("count", ascending=False)

        # 5. Extract FK Advantage products and their counts
        fk_advantage_products = df.filter(df["is_FK_Advantage_product"] == "Yes")
        fk_advantage_products_count = fk_advantage_products.count()

        # Create database if not exists
        spark.sql("CREATE DATABASE IF NOT EXISTS flipkart_analysis")

        # Save the DataFrames as Hive tables
        category_count.write.mode('overwrite').saveAsTable("flipkart_analysis.category_count")
        average_discount.write.mode('overwrite').saveAsTable("flipkart_analysis.average_discount")
        highest_rated_products.write.mode('overwrite').saveAsTable("flipkart_analysis.highest_rated_products")
        brand_counts.write.mode('overwrite').saveAsTable("flipkart_analysis.brand_counts")
        fk_advantage_products.write.mode('overwrite').saveAsTable("flipkart_analysis.fk_advantage_products")

        print("Processing completed and tables saved successfully.")

    finally:
        # Stop the SparkSession when done
        spark.stop()





