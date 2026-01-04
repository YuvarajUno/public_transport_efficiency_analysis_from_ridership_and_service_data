import pandas as pd

def load_upcoming_cities(filepath):
    """
    Load upcoming city metro project data from a CSV or Excel file.
    """
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)
    return df

def load_ridership(filepath):
    """
    Load ridership logs data from a CSV or Excel file.
    """
    if filepath.endswith(".csv"):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)
    return df


if __name__ == "__main__":
    # File paths to your datasets
    upcoming_cities_path = r"../data/upcoming_city.csv"
    ridership_path = r"../data/Ridership.csv"

    # Load the data
    upcoming_cities_df = load_upcoming_cities(upcoming_cities_path)
    ridership_df = load_ridership(ridership_path)

    # Print first 5 rows to check
    print("Upcoming Cities Data:")
    print(upcoming_cities_df.head())

    print("\nRidership Data:")
    print(ridership_df.head())

