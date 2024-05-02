import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def main():
    # Load the CSV file
    file_path = '../output/charcot_autres_keybert_comparaison.csv'  # Adjust this to your actual file path
    data = pd.read_csv(file_path)

    # Prepare and count terms
    charcot_terms = data['Charcot'].dropna().value_counts()
    autres_terms = data['Autres'].dropna().value_counts()

    # Convert series to dataframes for merging
    df_charcot = charcot_terms.reset_index()
    df_charcot.columns = ['Term', 'Count_Charco']

    df_autres = autres_terms.reset_index()
    df_autres.columns = ['Term', 'Count_Autres']

    # Merge and find common terms
    common_terms = pd.merge(df_charcot, df_autres, on='Term')
    common_terms['Total_Count'] = common_terms['Count_Charco'] + common_terms['Count_Autres']
    top_common_terms = common_terms.sort_values(by='Total_Count', ascending=False).head(15)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 8))
    top_common_terms.set_index('Term')['Total_Count'].sort_values().plot(kind='barh', color='steelblue', ax=ax)
    ax.set_xlabel("Fréquence d'apparition du terme", fontsize=18)
    ax.set_ylabel('Termes', fontsize=18)
    
    # Set tick parameters for both axes
    ax.tick_params(axis='both', labelsize=22)  # Sets the fontsize for x and y ticks

    # Set the x-axis to show only integer values
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # Ensures x-axis has only integer labels

    plt.tight_layout()
    plt.savefig('Top_15_Common_Terms_Visualization.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    main()
