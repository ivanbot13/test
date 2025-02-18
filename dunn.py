
# Import necessary libraries
import pandas as pd
import scikit_posthocs as sp
import seaborn as sns
import matplotlib.pyplot as plt

# Define the dataset for Trials #1-12
data_trials_1_12 = {
    "0mL bacteria": [10, 11, 7, 10, 6, 5, 9, 8, 9, 7, 7, 8],
    "0.5mL bacteria": [11, 11, 10, 1, 2, 5, 13, 7, 8, 10, 9, 8],
    "1mL bacteria": [10, 9, 12, 8, 8, 8, 4, 12, 9, 5, 9, 6],
    "2mL bacteria": [9, 10, 10, 9, 1, 7, 10, 8, 9, 11, 9, 10],
    "4mL bacteria": [10, 9, 10, 11, 5, 9, 8, 10, 9, 10, 9, 6]
}

# Define the dataset for Trials #13-24
data_trials_13_24 = {
    "0mL bacteria": [5, 9, 9, 7, 9, 9, 6, 7, 9, 10, 8, 7],
    "0.5mL bacteria": [7, 12, 7, 11, 9, 10, 6, 8, 11, 9, 10, 11],
    "1mL bacteria": [8, 8, 9, 13, 11, 9, 9, 8, 9, 10, 7 ,7],
    "2mL bacteria": [9, 10, 12, 12, 9, 7, 5, 9, 10, 12, 3, 6],
    "4mL bacteria": [13, 11, 9, 8, 12, 8, 5, 9, 9, 10, 8, 9]
}

# Convert to DataFrames
df_trials_1_12 = pd.DataFrame(data_trials_1_12)
df_trials_13_24 = pd.DataFrame(data_trials_13_24)

# Perform Dunn’s post hoc test with Bonferroni correction for Trials #1-12
dunn_results_1_12 = sp.posthoc_dunn(df_trials_1_12, p_adjust='bonferroni')

# Perform Dunn’s post hoc test with Bonferroni correction for Trials #13-24
dunn_results_13_24 = sp.posthoc_dunn(df_trials_13_24, p_adjust='bonferroni')

# Function to plot Dunn's test results
def plot_dunn_heatmap(dunn_results, title):
    plt.figure(figsize=(8, 6))
    sns.heatmap(dunn_results, annot=True, cmap="coolwarm", linewidths=0.5)
    plt.title(title)
    plt.xlabel("Bacterial Treatment (mL)")
    plt.ylabel("Bacterial Treatment (mL)")
    plt.show()

# Plot results for both sets of trials
plot_dunn_heatmap(dunn_results_1_12, "Dunn’s Post Hoc Test (Trials #1-12)")
plot_dunn_heatmap(dunn_results_13_24, "Dunn’s Post Hoc Test (Trials #13-24)")