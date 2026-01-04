def add_peak_offpeak_flag(df):
    """
    Add a column 'peak_offpeak' based on the 'day_type' column.
    Assumes:
      - 'W' means Weekday (peak)
      - 'U' or 'A' means Weekend or other off-peak days
    If 'day_type' is missing, sets flag as 'unknown'.
    """
    df = df.copy()
    if 'day_type' in df.columns:
        df['peak_offpeak'] = df['day_type'].apply(lambda x: 'peak' if x == 'W' else 'offpeak')
    else:
        df['peak_offpeak'] = 'unknown'
    return df

def calculate_load_factor(df, vehicle_capacity=100):
    """
    Calculate a new column 'load_factor' as total rides divided by vehicle capacity.
    Assumes 'total_rides' column exists.
    Default vehicle_capacity is 100 (can be adjusted).
    """
    df = df.copy()
    if 'total_rides' in df.columns:
        df['load_factor'] = df['total_rides'] / vehicle_capacity
    else:
        df['load_factor'] = 0
    return df

if __name__ == "__main__":
    import sys
    sys.path.append("..")  # So we can import from other folders

    from data_cleaning.clean_data import clean_ridership
    from data_ingestion.load_data import load_ridership

    # Update this path to your actual file location

    ridership_path = r"../data/Ridership.csv"

    # Load and clean ridership data
    ridership_df = load_ridership(ridership_path)
    ridership_clean = clean_ridership(ridership_df)

    # Add features
    ridership_features = add_peak_offpeak_flag(ridership_clean)
    ridership_features = calculate_load_factor(ridership_features)

    # Print sample to verify
    print(ridership_features[['service_date', 'day_type', 'peak_offpeak', 'total_rides', 'load_factor']].head())