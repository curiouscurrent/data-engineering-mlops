import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Get arguments (including dynamic input path)
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input_path'])

input_path = args['input_path']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

print(f"Reading file from: {input_path}")

# Read CSV
df = spark.read \
    .option("header", "true") \
    .option("mode", "PERMISSIVE") \
    .option("inferSchema", "true") \
    .csv(input_path)

# Remove rows with null values
df_clean = df.dropna()

# Write JSON output
output_path = "s3://amzn-s3-mytarget-bucket/output/"

df_clean.write \
    .mode("overwrite") \
    .json(output_path)

print(f"Data written to: {output_path}")

job.commit()