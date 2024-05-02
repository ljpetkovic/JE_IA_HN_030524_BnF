import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load the CSV file
    file_path = '../output/charcot_autres_kpv_comparaison.csv'  # Update this with the path to your CSV file
    data = pd.read_csv(file_path)

    # Specify the column names which contain the terms
    charcot_column = 'Charcot'  # Update this with the actual column name for Charcot terms
    autres_column = 'Autres'  # Update this with the actual column name for Autres terms

    # Extract terms from both columns
    charcot_terms = data[charcot_column].dropna().unique()
    autres_terms = data[autres_column].dropna().unique()

    # Create sets for quick lookup
    charcot_set = set(charcot_terms)
    autres_set = set(autres_terms)

    # Find common terms and select the top 15
    common_terms = sorted(charcot_set.intersection(autres_set))[:15]

    # Map terms to their positions
    charcot_positions = {term: i for i, term in enumerate(common_terms)}
    autres_positions = {term: i for i, term in enumerate(common_terms)}

    # Create the figure and axis
    plt.figure(figsize=(10, 8))  # Adjusted for better fit
    ax = plt.gca()

    # Set x-coordinates for the labels and points
    x_charcot = 0.3  # X-coordinate for Charcot terms
    x_autres = 0.7   # X-coordinate for Autres terms

    # Plot Charcot terms and points on the left
    for term, pos in charcot_positions.items():
        ax.text(x_charcot, pos, term, ha='right', va='center', fontsize=20, color='black')
        ax.scatter([x_charcot + 0.05], [pos], color='blue', s=10)  # Offset the point

    # Plot Autres terms and points on the right
    for term, pos in autres_positions.items():
        ax.text(x_autres, pos, term, ha='left', va='center', fontsize=20, color='black')
        ax.scatter([x_autres - 0.05], [pos], color='blue', s=10)  # Offset the point
        # Draw a line between the points
        ax.plot([x_charcot + 0.05, x_autres - 0.05], [pos, pos], color='blue', linestyle='-', linewidth=1)

    # Adjusted lines for better alignment
    ax.text(x_charcot + -0.14, -1.5, 'Charcot', ha='center', va='top', fontsize=12, color='black')  # Adjust the x offset as needed
    ax.text(x_autres + 0.14, -1.5, 'Autres', ha='center', va='top', fontsize=12, color='black')

    # Set limits and hide axes
    ax.set_xlim(0, 1)
    ax.set_ylim(-3, len(common_terms))  # Adjusted lower limit to accommodate labels
    ax.axis('off')

    # Adjust layout and save in high quality
    plt.tight_layout()
    plt.savefig('Top_15_Common_Terms_Visualization.png', dpi=1200, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    main()
