def aggregate_ridership_by_peak(df):
    """
    Group by peak/offpeak and summarize total rides.
    """
    grouped = df.groupby('peak_offpeak')['total_rides'].sum().reset_index()
    return grouped

if __name__ == "__main__":
    import sys
    sys.path.append("..")

    from feature_engineering.features import add_peak_offpeak_flag, calculate_load_factor
    from data_ingestion.load_data import load_ridership
    from data_cleaning.clean_data import clean_ridership


    ridership_path = r"../data/Ridership.csv"
    ridership_df = load_ridership(ridership_path)
    ridership_clean = clean_ridership(ridership_df)
    ridership_features = add_peak_offpeak_flag(ridership_clean)
    ridership_features = calculate_load_factor(ridership_features)

    summary = aggregate_ridership_by_peak(ridership_features)
    print("Ridership Summary by Peak/Off-Peak:")
    print("",summary)
