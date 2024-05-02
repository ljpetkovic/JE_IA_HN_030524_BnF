import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def main():
    # Load the CSV file
    file_path = '../output/autres_keybert.csv'  # Adjusted file path to the actual file path
    data = pd.read_csv(file_path)

    # Sort the data by 'Scores' and select the top 15 entries
    top_terms = data.sort_values(by='Score', ascending=False).head(15)

    # Plotting
    plt.figure(figsize=(12, 8))  # Set the figure size
    ax = top_terms.set_index('Autres')['Score'].plot(kind='barh', color='skyblue')  # Create a horizontal bar chart
    ax.set_xlabel('Score', fontsize=18)  # Set the x-axis label
    ax.set_ylabel('Termes', fontsize=18)  # Set the y-axis label
    # ax.set_title('15 premiers termes dans le corpus Autres')  # Set the title
    plt.gca().invert_yaxis()  # Invert the y-axis to have the highest score on top

    # Set tick parameters for both axes
    ax.tick_params(axis='both', labelsize=22)  # Sets the fontsize for x and y ticks
    
    # Ensure x-axis ticks are integers if scores are integer values
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # Only integer labels on x-axis

    plt.tight_layout()  # Adjust subplots to give the plot a little more room
    plt.savefig('Top_15_Terms_Autres_Corpus.png', dpi=300)  # Save the plot as a PNG file
    plt.show()

if __name__ == '__main__':
    main()
