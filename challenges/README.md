# Challenges

Ce dossier contient les défis proposés lors des cours. Ces notebooks incluent les exercices pratiques, les solutions développées et les implémentations de différents concepts algorithmiques et de programmation.

## Contenu

### arbres.ipynb
**Défi sur les structures de données arborescentes**

Ce notebook explore les arbres (trees) comme structure de données. Il contient :
- Implémentation d'une structure de nœuds avec gestion hiérarchique
- Organisation de données clients par catégories (âge, ville, département)
- Méthodes de parcours et d'affichage d'arbres
- Comptage et agrégation de données dans une structure arborescente

**Concepts abordés** : Structures de données, arbres, récursivité, organisation hiérarchique

---

### genetic.ipynb
**Défi sur les algorithmes génétiques - Optimisation d'emploi du temps**

Implémentation complète d'un algorithme génétique pour résoudre un problème d'optimisation d'emploi du temps scolaire. Le notebook contient :

- **Représentation** : Chaque solution (chromosome) représente un emploi du temps avec 30 cours
- **Fonction de fitness** : Évaluation basée sur :
  - Détection des conflits (même salle, même créneau, même jour)
  - Capacité des salles vs nombre d'étudiants
  - Respect des préférences des enseignants
  - Charge de travail des professeurs
- **Opérateurs génétiques** :
  - Croisement (crossover) entre deux solutions parentes
  - Mutation (changement de salle ou de créneau)
  - Sélection par tournoi
  - Élitisme (conservation des meilleures solutions)
- **Configuration** : 6 salles, 6 cours, 3 professeurs avec préférences

**Concepts abordés** : Algorithmes génétiques, optimisation, heuristiques, problèmes de contraintes

---

### challenge.ipynb
**Défis variés sur la manipulation de données**

Collection d'exercices pratiques sur l'analyse et la manipulation de données avec pandas et NumPy. Le notebook inclut :

- **MultiIndex & Indexation Avancée** :
  - Création de MultiIndex complexes (Région → Département → Grade → Année)
  - Indexation hiérarchique de données d'employés
  - Manipulation de DataFrames avec index multiples
- **Analyse de données d'employés** :
  - Traitement de fichiers CSV
  - Agrégations et groupements avancés
  - Analyse par régions, départements et grades

**Concepts abordés** : Pandas, MultiIndex, manipulation de données, analyse de données

---

### numpy.ipynb
**Défi sur NumPy - Calculs numériques**

Notebook d'apprentissage et de pratique avec la bibliothèque NumPy pour le calcul scientifique. Contenu :

- **Statistiques de base** :
  - Calcul de moyenne, somme, variance
  - Opérations statistiques sur des tableaux
- **Manipulation des tableaux** :
  - Création et manipulation de tableaux multidimensionnels
  - Opérations vectorielles
  - Indexation et slicing avancés
- **Fonctions mathématiques** :
  - Opérations élémentaires sur les tableaux
  - Calculs numériques efficaces

**Concepts abordés** : NumPy, calculs numériques, tableaux multidimensionnels, vectorisation

---

## Objectifs pédagogiques

Ces défis permettent de pratiquer :
- **Structures de données** : Arbres, listes, dictionnaires
- **Algorithmes** : Algorithmes génétiques, optimisation
- **Manipulation de données** : Pandas, NumPy, CSV
- **Programmation orientée objet** : Classes, méthodes, encapsulation
- **Résolution de problèmes** : Approches heuristiques, gestion de contraintes

## Notes

- Tous les notebooks sont exécutables et contiennent du code fonctionnel
- Les solutions sont commentées pour faciliter la compréhension
- Certains défis peuvent nécessiter l'installation de bibliothèques (numpy, pandas)

## Utilisation

Pour exécuter les notebooks :
1. Assurez-vous d'avoir installé les dépendances nécessaires (numpy, pandas, jupyter)
2. Ouvrez le notebook dans Jupyter ou JupyterLab
3. Exécutez les cellules dans l'ordre
4. Explorez et modifiez le code pour mieux comprendre les concepts

