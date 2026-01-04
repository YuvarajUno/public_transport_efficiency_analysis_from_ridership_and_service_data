import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================
# CONFIG
# =============================
ROUTE_COL = 'bus'   # Route identifier from your dataset

# =============================
# Utility functions
# =============================
def save_table(df, filename, folder='tables'):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    try:
        if filename.endswith('.xlsx'):
            df.to_excel(path, index=False)
        else:
            df.to_csv(path, index=False)
        print(f"Table saved: {path}")

    except ModuleNotFoundError:
        # Fallback if openpyxl is not installed
        csv_path = path.replace('.xlsx', '.csv')
        df.to_csv(csv_path, index=False)
        print(f"openpyxl not found → table saved as CSV: {csv_path}")


def save_figure(fig, filename, folder='figures'):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    fig.savefig(path, format='pdf', bbox_inches='tight')
    plt.close(fig)
    print(f"Figure saved: {path}")


# =============================
# RQ1: Peak-hour congestion by route
# =============================
def generate_rq1_table(df):
    peak_df = df[df['peak_offpeak'] == 'peak']

    summary = (
        peak_df
        .groupby(ROUTE_COL)['total_rides']
        .sum()
        .reset_index()
        .sort_values(by='total_rides', ascending=False)
    )

    save_table(summary, 'RQ1_Table1.xlsx')


# =============================
# RQ2: Ridership variation over time
# =============================
def plot_rq2_figure(df):
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.lineplot(
        data=df,
        x='service_date',
        y='total_rides',
        hue='peak_offpeak',
        ax=ax
    )

    ax.set_title('Ridership Over Time: Peak vs Off-Peak')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Rides')

    save_figure(fig, 'RQ2_Fig1.pdf')


# =============================
# RQ3: Load factor efficiency
# =============================
def plot_rq3_figure(df):
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.boxplot(
        data=df,
        x='peak_offpeak',
        y='load_factor',
        ax=ax
    )

    ax.set_title('Load Factor Distribution by Time Period')
    ax.set_xlabel('Time Period')
    ax.set_ylabel('Load Factor')

    save_figure(fig, 'RQ3_Fig1.pdf')


def generate_rq3_table(df):
    summary = (
        df
        .groupby(ROUTE_COL)['load_factor']
        .mean()
        .reset_index()
        .sort_values(by='load_factor', ascending=False)
    )

    save_table(summary, 'RQ3_Table1.xlsx')


# =============================
# RQ4: Underutilized routes
# =============================
def generate_rq4_table(df, threshold=0.3):
    summary = (
        df
        .groupby(ROUTE_COL)['load_factor']
        .mean()
        .reset_index()
    )

    underutilized = summary[summary['load_factor'] < threshold]
    save_table(underutilized, 'RQ4_Table1.xlsx')


# =============================
# Main execution
# =============================
if __name__ == "__main__":
    import sys
    sys.path.append("..")

    from feature_engineering.features import add_peak_offpeak_flag, calculate_load_factor
    from data_ingestion.load_data import load_ridership
    from data_cleaning.clean_data import clean_ridership

    ridership_path = r"../data/Ridership.csv"

    # Load and preprocess data
    df = load_ridership(ridership_path)
    df = clean_ridership(df)
    df = add_peak_offpeak_flag(df)
    df = calculate_load_factor(df)

    print("Dataset columns:", list(df.columns))

    # Generate outputs
    generate_rq1_table(df)
    plot_rq2_figure(df)
    plot_rq3_figure(df)
    generate_rq3_table(df)
    generate_rq4_table(df)

    print("\n✅ All figures and tables generated successfully")
