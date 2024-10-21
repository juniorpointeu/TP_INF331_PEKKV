import pandas as pd
import random


def generer_dataset(num_entries = 6000):
    sexe_options = ['H', 'F']
    mention_options = ['Passable', 'Assez Bien', 'Bien', 'Très Bien']
    specialite_options = ['Informatique', 'Gestion', 'Droit', 'Marketing', 'Sciences']
    diplome_options = ['Bac', 'Licence', 'Master', 'Doctorat']
    languages = [1, 2, 3, 4]  # Nombre de langues parlées
    softwares = [1, 2, 3, 4, 5]  # Nombre de logiciels maîtrisés

    # Génération des données
    data = []
    for i in range(num_entries):
        candidat_id = i + 1
        sexe = random.choice(sexe_options)
        age = random.randint(20, 40)
        annees_experience = random.randint(0, 15)
        mention_bac = random.choice(mention_options)
        mention_licence = random.choice(mention_options)
        specialite_licence = random.choice(specialite_options)
        dernier_diplome = random.choice(diplome_options)  # Pas de Bac
        langues_parlees = random.choice(languages)
        connaissance_softwares = random.choice(softwares)
        experience_management = random.randint(0, annees_experience)  # Peut pas avoir plus d'expérience en management qu'en expérience totale
        stage_effectue = random.choice([0, 1])
        recrute = random.choice([0, 1])  # 0 ou 1 pour recruté

        data.append([
            candidat_id, sexe, age, annees_experience, 
            mention_bac, mention_licence, specialite_licence,
            dernier_diplome,langues_parlees,
            connaissance_softwares, experience_management, stage_effectue, 
            recrute
        ])

    # Création du DataFrame
    columns = [
        "Candidat_ID", "Sexe", "Age", "Annees_Experience", 
        "Mention_Bac", "Mention_Licence", "Specialite_Licence", 
        "Diplome_Superieur",  "Langues_Parlees", 
        "Connaissance_Softwares", "experience_management","Stage_Effectue", 
        "Recrute"
    ]

    df = pd.DataFrame(data, columns=columns)

    # Enregistrer le DataFrame en CSV
    df.to_csv('dataset_candidats.csv', index=False)

    print("Dataset généré avec succès et enregistré sous le nom 'dataset_candidats.csv'")

generer_dataset()
