import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# ========== LOAD AND PREPROCESS DATA ==========
# Load Excel data
xlsx = pd.ExcelFile('C:/Users/amiru/Desktop/Portfolio/Coding/Honey/Itama Honey.xlsx')
dfs = []
sheet_names = ['Itama (Anaerobic)', 'Itama (Aerobic)']

# Function to load and clean data
def load_and_clean_data(sheet_name):
    df = pd.read_excel(xlsx, sheet_name=sheet_name)
    df = df[df['Temperature'].notna()]  # Remove rows where 'Temperature' is NaN
    df = df.dropna(axis=1, how='all')
    return df

# Load and clean both anaerobic and aerobic sheets
for sheet in sheet_names:
    dfs.append(load_and_clean_data(sheet))

# ========== HANDLE MISSING VALUES AND ZEROES ==========
columns_microbes = ['Y & M (10^-1)', 'LAB (10^-1)', 'Bacillus (10^-1)']

# Function to replace zeroes with temperature-wise mean for each microbe
def replace_zeros(df, cols):
    for temp in df['Temperature'].unique():
        for col in cols:
            mean_val = df[(df['Temperature'] == temp) & (df[col] != 0)][col].mean()
            if pd.isna(mean_val):
                mean_val = 0
            df.loc[(df['Temperature'] == temp) & (df[col] == 0), col] = mean_val
    return df

# Clean both anaerobic and aerobic data
dfs = [replace_zeros(df, columns_microbes) for df in dfs]

# ========== DESCRIPTIVE STATISTICS ==========
# Function to print descriptive statistics for each temperature group
def descriptive_stats(df):
    for temp in df['Temperature'].unique():
        print(f"Descriptive statistics for 'Temperature' = {temp}:")
        print(df[df['Temperature'] == temp].describe())
        print("\n")

# Display descriptive stats for both conditions
for i, df in enumerate(dfs):
    print(f"\nDescriptive Statistics for {sheet_names[i]} Condition:")
    descriptive_stats(df)

# Combine both conditions (Anaerobic + Aerobic) into one dataframe
df_all = pd.concat(dfs, ignore_index=True)

# ========== TWO-WAY ANOVA (Temperature vs Condition) ==========
# Perform ANOVA to check the effects of Temperature and Condition on microbial growth
def two_way_anova(df, microbe):
    print(f"\nANOVA Results for {microbe}")
    model = ols(f'Q("{microbe}") ~ C(Temperature) + C(Condition) + C(Temperature):C(Condition)', data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)

    # Tukey HSD Post-Hoc for pairwise comparisons
    tukey = pairwise_tukeyhsd(endog=df[microbe],
                               groups=df['Temperature'].astype(str) + '_' + df['Condition'],
                               alpha=0.05)
    print(tukey)

# Run ANOVA and Tukey HSD for all microbes
for microbe in columns_microbes:
    two_way_anova(df_all, microbe)

# ========== TREND VISUALIZATION ==========
# Plot trends over time for each microbe, temperature, and condition
def plot_trends(df):
    for microbe in columns_microbes:
        plt.figure(figsize=(10, 6))

        # Create the main plot
        sns.lineplot(data=df, x='Day No.', y=microbe, hue='Temperature', style='Condition', markers=True)
        plt.yscale('log')  # Set y-axis to logarithmic scale
        plt.title(f'{microbe} Trends Over Time')

         # Get Day 0 values for each temperature and condition combination
        day0_values = df[df['Day No.'] == 0][microbe].unique()

        # Add horizontal red lines for each Day 0 value
        for val in day0_values:
            plt.axhline(y=val, color='red', linestyle='-', alpha=0.5, label='Day 0 Value')
        plt.legend(loc='upper left')
        plt.show()

# Visualize trends for all microbes
plot_trends(df_all)

# ========== FINAL RECOMMENDATIONS BASED ON MINIMAL CHANGE FROM DAY 0 ==========
def recommend_best_conditions_by_stability(df, microbe):
    print(f"\nRecommendations based on Stability of {microbe} (Least Change from Day 0):")
    print('==============================================================')

    # Get Day 0 values for each (Temperature, Condition)
    day0_values = df[df['Day No.'] == 0].set_index(['Temperature', 'Condition'])[[microbe]]

    # Calculate absolute change from Day 0 for each row
    df_change = df[df['Day No.'] != 0].copy() # Exclude Day 0 from mean calculation
    df_change['Abs Change'] = df.apply(
        lambda row: abs(row[microbe] - day0_values.loc[(row['Temperature'], row['Condition'])][microbe])
        , axis=1
    )

    # Calculate mean absolute change for each group
    stability = df_change.groupby(['Temperature', 'Condition'])['Abs Change'].mean()

    # Find the minimum mean change
    min_change = stability.min()

    # Get the best conditions
    best_conditions = stability[stability == min_change]

    # Output
    best_df = best_conditions.reset_index()
    best_df.rename(columns={'Abs Change': f'Mean Absolute Change in {microbe}'}, inplace=True)
    print(best_df)

# Run for all microbes
for microbe in columns_microbes:
    recommend_best_conditions_by_stability(df_all, microbe)

# General recommendation across all microbes
print("\nGeneral Recommendation Based on Stability Across All Microbes:")
print('================================================================')

# Calculate mean absolute change for all microbes
df_all_change = df_all.copy()

for microbe in columns_microbes:
    day0_values = df_all[df_all['Day No.'] == 0].set_index(['Temperature', 'Condition'])[[microbe]]
    df_all_change[f'{microbe}_Change'] = df_all.apply(
        lambda row: abs(row[microbe] - day0_values.loc[(row['Temperature'], row['Condition'])][microbe])
        , axis=1
    )

# Average the changes across all microbes
change_cols = [f'{microbe}_Change' for microbe in columns_microbes]
stability_all = df_all_change.groupby(['Temperature', 'Condition'])[change_cols].mean().mean(axis=1)

min_change_all = stability_all.min()

best_conditions_all = stability_all[stability_all == min_change_all]

best_df_all = best_conditions_all.reset_index()
best_df_all.rename(columns={0: "Mean Absolute Change Across All Microbes"}, inplace=True)

print(best_df_all)