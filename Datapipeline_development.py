import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sqlalchemy import create_engine


def extract_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    print("Data Extracted Successfully")
    return df, iris.target_names


def transform_data(df, target_names):
    scaler = StandardScaler()
    df.iloc[:, :-1] = scaler.fit_transform(df.iloc[:, :-1])

    
    le = LabelEncoder()
    df['species'] = le.fit_transform(df['species'])

    print("Data Transformed Successfully")
    return df, scaler, le


def load_data(df, db_url, table_name):
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print("Data Loaded Successfully")


if __name__ == "__main__":
    db_url = "sqlite:///iris_data.db"  
    table_name = "iris_cleaned"

    df, target_names = extract_data()
    transformed_df, scaler, encoder = transform_data(df, target_names)
    load_data(transformed_df, db_url, table_name)
