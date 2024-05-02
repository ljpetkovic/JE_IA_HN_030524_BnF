import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load the CSV file
    file_path = '../output/charcot_autres_comparaison.csv'  # Update this with the path to your CSV file
    data = pd.read_csv(file_path)

    # Spécifier les noms des colonnes contenant les termes
    charcot_column = 'Charcot'  
    autres_column = 'Autres' 

    # Extraire les termes des deux colonnes
    charcot_terms = data[charcot_column].dropna()
    autres_terms = data[autres_column].dropna()

    # Compter le nombre d'occurrences de chaque terme dans les deux corpus
    all_terms = pd.concat([charcot_terms, autres_terms])
    term_counts = all_terms.value_counts()

    # Sélectionner les 15 premiers termes pour visualiser
    top_terms = term_counts.head(15)

    # Visualiser des 15 premiers termes partagés
    plt.figure(figsize=(10, 8))  # Ajuster la taille de la figure pour la meilleure lisibilité
    bars = plt.barh(top_terms.index, top_terms.values)
    plt.xlabel("Fréquence d'apparition du terme", fontsize=16)
    # plt.title('Les 15 termes les plus fréquents dans les corpus Charcot et Autres.')
    plt.gca().invert_yaxis()  # Inverser l'axe Y pour afficher le terme avec la fréquence la plus élevée en haut
    plt.xticks(fontsize=16)  # Ajuster la taille de la police sur l'axe X si nécessaire
    plt.yticks(fontsize=20)  # Augmenter la taille de la police sur l'axe Y pour une meilleure lisibilité

    # Ajuster les marges et la mise en page
    plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)  # Ajuster ces valeurs si besoin
    plt.tight_layout()

    # Sauvegarder le graphique dans un fichier
    plt.savefig('termes_partages.png', dpi=300, bbox_inches='tight')

    plt.show()

if __name__ == '__main__':
    main()
