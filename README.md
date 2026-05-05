# data-engineering-mlops

## USECASE-1 : Trigger Glue Job Using AWS Lambda

**CODEFILES : https://github.com/curiouscurrent/data-engineering-mlops/tree/main/Trigger-GlueJob-Using-AWSLambda**

1. We have data incoming to our S3 bucket in CSV file format
2. We need to create one AWS Glue Job (ETL) , which will transfer data from AWS S3 input bucket to another AWS S3 target bucket in the form of JSON.
3. We have to trigger this Glue Job using AWS Lambda.
4. When the glue job is triggered, it fetches the glue job script from Glue Job Script bucket. (which can be set in (Glue "Job Details - Advanced Properties")

### Steps : 
1. Create 3 buckets : for input, target and to store the Glue Job script.
   
   <img width="892" height="430" alt="image" src="https://github.com/user-attachments/assets/2712a000-dccb-4b34-bcb5-9e49d5b7c82e" />
   
2. Now create a ETL - AWS Glue job
   
   <img width="1338" height="502" alt="image" src="https://github.com/user-attachments/assets/294eb66d-57b2-4a07-9341-8977ffce1f69" />
   
3. Create an IAM role for the Glue Job, and assign the following permissions : Allows Glue to call AWS services on your behalf.
   
   <img width="1319" height="403" alt="image" src="https://github.com/user-attachments/assets/365daf22-fc91-4acc-8a30-7854ee8f4a9f" />

4. Now create a Lambda function and add the trigger : Only triggered when a user pushes a .csv file into the input bucket (only allow the "PUT" Event)
   
   <img width="1119" height="554" alt="image" src="https://github.com/user-attachments/assets/0565caa1-7107-43a2-9fcd-05ac65392686" />

5. Add the IAM role for the Lambda function and assign the same permissions as attached to AWS Glue Job. Now deploy the code

   <img width="1064" height="458" alt="image" src="https://github.com/user-attachments/assets/f378e62f-5952-4f34-8668-934626c7b362" />

6. Now let us upload a .csv file in input S3 bucket

  <img width="1016" height="316" alt="image" src="https://github.com/user-attachments/assets/13050c3b-ee9a-4ff1-9f52-7190b956716a" />

7. Now check if the GLue Job has executed

  <img width="1322" height="607" alt="image" src="https://github.com/user-attachments/assets/c508f674-5c14-4c1d-9ceb-36476acc7937" />

8. Now check the target bucket, you should find a .json 

  <img width="1039" height="374" alt="image" src="https://github.com/user-attachments/assets/976e6cee-e5ae-4667-a4c0-64252ce8b8de" />

9. Check the logs via CloudWatch
   
   <img width="1307" height="509" alt="image" src="https://github.com/user-attachments/assets/45f190dc-d644-4cb4-b829-723553851a78" />





   


