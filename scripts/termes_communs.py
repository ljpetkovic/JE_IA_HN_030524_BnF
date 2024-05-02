import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load the CSV file
    file_path = '../output/charcot_autres_comparaison.csv'  # Update this with the path to your CSV file
    data = pd.read_csv(file_path)

    # Specify the column names which contain the terms
    column1 = 'Charcot'  # Update this with the actual column name
    column2 = 'Autres'  # Update this with the actual column name

    # Extract terms from both columns
    terms1 = set(data[column1].dropna())
    terms2 = set(data[column2].dropna())

    # Find common terms
    common_terms = list(terms1.intersection(terms2))

    # Limit to top 15 common terms (assuming you want the first 15 alphabetically)
    common_terms = sorted(common_terms)[:15]

    # Visualize the top 15 common terms using a bar chart
    plt.figure(figsize=(10, 8))
    plt.barh(common_terms, range(1, 16))  # Assuming each term appears once
    plt.xlabel('Number of Occurrences (Assumed to be 1 for each)')
    plt.title('Top 15 Common Terms Visualization')
    plt.show()

if __name__ == '__main__':
    main()
