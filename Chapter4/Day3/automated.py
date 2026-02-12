import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".xlsx"):
        return pd.read_excel(path)
    elif path.endswith(".json"):
        return pd.read_json(path)
    else:
        raise ValueError("unsupported file type")
    
def inspect_data(df):
    info = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "dtypes": df.dtypes,
        "memory_usage_mb": df.memory_usage(deep=True).sum() / 1024**2
    }
    return info

def missing_report(df):
    report = pd.DataFrame({
        "missing_count": df.isna().sum(),
        "missing_percent": df.isna().mean() * 100
    })
    return report.sort_values("missing_percent", ascending=False)

def detect_feature_types(df):
    numeric = df.select_dtypes(include="number").columns.tolist()
    categorical = df.select_dtypes(include="object").columns.tolist()
    datetime = df.select_dtypes(include="datetime").columns.tolist()

    return numeric, categorical, datetime

def clean_data(df, missing_threshold=0.4):
    # drop columns with too many missing values
    df = df.loc[:, df.isna().mean() < missing_threshold]

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna(df[col].median())

    df = df.drop_duplicates()
    return df

def numeric_summary(df, numeric_cols):
    return df[numeric_cols].describe().T

def plot_numeric(df, numeric_cols):
    for col in numeric_cols:
        df[col].hist(bins=30)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel("frequency")
        plt.savefig(f'Plot for {col}.png')

df = load_data("tips.csv")
print(inspect_data(df))
print(missing_report(df))
num_cols, cat_cols, date_cols = detect_feature_types(df)
df = clean_data(df)
print(numeric_summary(df, num_cols))
plot_numeric(df, num_cols)
