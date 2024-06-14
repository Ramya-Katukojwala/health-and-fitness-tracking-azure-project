# Health-and-fitness-tracking-azure-project
This project is a health and fitness tracking application built on Microsoft Azure. It empowers users to monitor their progress towards their health and fitness goals by providing a comprehensive platform for data collection, analysis, and visualization. For this project microsoft azure resources are used.



**Data Source**

This dataset was taken from kaggle which was generated by respondents to a distributed survey via Amazon Mechanical Turk between 03.12.2016-05.12.2016. Thirty eligible Fitbit users consented to the submission of personal tracker data, including minute-level output for physical activity, heart rate, and sleep monitoring. Individual reports can be parsed by export session ID (column A) or timestamp (column B). Variation between output represents use of different types of Fitbit trackers and individual tracking behaviors / preferences.
Link: https://www.kaggle.com/datasets/arashnic/fitbit

Only the data that is required for the analysis is selected and taken. Those files are uploaded under the file "data/raw-data" 



**Data Ingestion**


Step 1: Here we upload the files first to the github
Step 2: Create a Azure storage account in the azure portal
Step 3: Create a new container and create two files "raw-data" and "transform-data"
Step 4: Create a data factory and add data through pipeline
Step 5: Data can be added using the raw page of the data from the github and choose the correct file from the storage account
Step 6: Once the pipeline is debugged the files we automatically appear in the container



**Data Transformation**


Step 1: Create an Azure Databricks Workspace
Step 2: Launch Workspace
Step 3: Create a compute using the compute tab
Step 4: Create an Azure App Registration and collect the "client ID", "tenant id", and :Secret id".
Step 5: Use the "code_transform.py" in the workspace by changing the above key
step 6: The transformed data will be visible in the the storage container.(The transformed files are given in the path "data/transform-data")



**Data Visualization**


The transformed data is to analyse and vizualize the data
This is connected to the the azure devops for th applications
The visualizations are given below:



**Home Page:**


![Screenshot 2024-06-14 090836](https://github.com/Ramya-Katukojwala/health-and-fitness-tracking-azure-project/assets/103170953/c03f4525-59e4-4f33-a54d-150e19f682c3)



**Daily Activity Page:**


![Screenshot 2024-06-14 083920](https://github.com/Ramya-Katukojwala/health-and-fitness-tracking-azure-project/assets/103170953/68958fd5-0c1e-4954-9b5e-c57659619675)


**Hourly Activity Page:**


![Screenshot 2024-06-14 085200](https://github.com/Ramya-Katukojwala/health-and-fitness-tracking-azure-project/assets/103170953/384bcd81-2dbb-43a8-9941-34b39f7c0774)



**Minutely Activity Page**


![Screenshot 2024-06-14 090057](https://github.com/Ramya-Katukojwala/health-and-fitness-tracking-azure-project/assets/103170953/c4cdbb29-fb9f-4579-9d89-50767716edec)
