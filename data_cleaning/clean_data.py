import pandas as pd

def clean_upcoming_cities(df):
    """
    Clean upcoming cities data:
    - Strip whitespace from string columns
    - Check for missing values
    """
    df = df.copy()
    # Trim strings
    for col in ['City', 'Country', 'Name']:
        if col in df.columns:
            df[col] = df[col].str.strip()

    # Example: Fill missing 'Projected up Lines' with 1 (or as appropriate)
    if 'Projected up Lines' in df.columns:
        df['Projected up Lines'] = df['Projected up Lines'].fillna(1)

    # Return cleaned dataframe
    return df

def clean_ridership(df):
    """
    Clean ridership logs:
    - Convert date columns to datetime
    - Fill or drop missing values
    - Filter invalid records if needed
    """
    df = df.copy()
    # Convert service_date to datetime
    if 'service_date' in df.columns:
        df['service_date'] = pd.to_datetime(df['service_date'], errors='coerce')

    # Drop rows where service_date conversion failed
    df = df.dropna(subset=['service_date'])

    # Fill missing numeric columns with 0
    numeric_cols = ['bus', 'rail_boardings', 'total_rides']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    return df

if __name__ == "__main__":
    import sys
    sys.path.append("..")  # to import from data_ingestion

    from data_ingestion.load_data import load_upcoming_cities, load_ridership

    upcoming_cities_path = r"../data/upcoming_city.csv"
    ridership_path = r"../data/Ridership.csv"

    upcoming_df = load_upcoming_cities(upcoming_cities_path)
    ridership_df = load_ridership(ridership_path)

    cleaned_upcoming_df = clean_upcoming_cities(upcoming_df)
    cleaned_ridership_df = clean_ridership(ridership_df)

    print("Cleaned Upcoming Cities Data Sample:")
    print(cleaned_upcoming_df.head())
    print("\nCleaned Ridership Data Sample:")
    print(cleaned_ridership_df.head())