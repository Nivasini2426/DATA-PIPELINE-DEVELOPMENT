# DATA-PIPELINE-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: NIVASINI SK

*INTERN ID*: CTO8OUS

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:

Automating the ETL Process for the Iris Dataset Using Pandas, Scikit-learn, and SQLAlchemy

Introduction
Data processing is a critical step in any data science project, ensuring that raw data is properly collected, cleaned, transformed, and stored for analysis and model development. The Extract, Transform, Load (ETL) process is widely used in data engineering to automate data handling, making it ready for further applications such as machine learning, reporting, or business intelligence.

This project focuses on building an ETL pipeline for the Iris dataset, a well-known dataset in machine learning. The pipeline consists of three main stages:
Extracting data from an inbuilt dataset in Scikit-learn.
Transforming the data using preprocessing techniques such as standardization and label encoding.
Loading the transformed data into a structured SQLite database for future access.

By automating this ETL process, we ensure that data is clean, structured, and ready for use in various analytical and machine learning tasks.

Step 1: Data Extraction
The first step in the ETL process is data extraction. In this case, we use the Iris dataset, which is available in Scikit-learn's dataset module. This dataset contains 150 samples of iris flowers, categorized into three species: Setosa, Versicolor, and Virginica. Each sample includes four numerical features:

Sepal length
Sepal width
Petal length
Petal width
To make this dataset usable, it is loaded into a pandas DataFrame, with an additional column for the species labels. These labels are originally stored as numerical values (0, 1, 2) corresponding to the three flower species.

By extracting the data in this structured format, we prepare it for further transformation steps.

Step 2: Data Transformation
Raw data often requires preprocessing to improve its quality and make it suitable for analysis and machine learning. In this step, we perform two essential transformations:

Feature Scaling:

Since the four numerical features have different ranges, we apply standardization using the StandardScaler from Scikit-learn.
Standardization ensures that each feature has a mean of 0 and a standard deviation of 1, making it suitable for machine learning models that rely on feature magnitudes.
Label Encoding:

The target variable (species) is encoded using LabelEncoder, which converts categorical labels into numerical format.
This step is crucial for machine learning algorithms that require numerical input.
By applying these transformations, we ensure that the dataset is normalized, structured, and machine-learning-ready.

Step 3: Data Loading
After transformation, the cleaned data is stored in a relational database using SQLAlchemy. In this project, we use an SQLite database, a lightweight and easy-to-use database solution.

The cleaned dataset is saved in a database table, allowing easy access for future machine learning training, visualization, or analysis. Using a database instead of raw CSV files provides several benefits:

Data persistence: Unlike in-memory storage, databases retain data even after the program stops.
Structured storage: Data is stored in a tabular format, making it easy to query.
Scalability: This approach can be extended to larger datasets and integrated with cloud-based databases.
This final step ensures that the transformed data is stored efficiently and can be retrieved whenever needed.

Benefits of the ETL Pipeline
Automation: The entire data processing workflow is automated, eliminating manual intervention.
Scalability: The pipeline can be extended to handle other datasets or larger data volumes.
Machine Learning Readiness: Data is preprocessed, making it ready for model training without additional effort.
Efficient Data Storage: Using a database ensures that the transformed data is structured and easily accessible.
Reusability: The pipeline can be reused for similar datasets with minor modifications.
Conclusion
This project demonstrates a complete ETL pipeline for handling the Iris dataset, from data extraction to transformation and storage. By applying feature scaling, label encoding, and database storage, the pipeline ensures that raw data is clean, structured, and ready for analysis.

This approach is fundamental in real-world data engineering and data science applications, where raw data must be systematically processed before use. By automating the ETL process, we can streamline workflows and enhance the efficiency of data-driven projects.

*OUTPUT*:
![Image](https://github.com/user-attachments/assets/66d1b70b-4cf9-46c4-9095-6b7928f6b03b)





