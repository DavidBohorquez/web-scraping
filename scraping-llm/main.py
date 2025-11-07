import os
import pandas as pd
import re
from serpapi import GoogleSearch
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

class GooglePlayAnalyzer:
    def __init__(self):
        self.all_apps = []
        
    def clean_installs_count(self, installs_text):
        """Convertit le texte de téléchargements en nombre numérique"""
        if not installs_text:
            return 0
            
        installs_text = str(installs_text).upper().replace(",", "").replace("+", "")
        
        multipliers = {
            'K': 1000,
            'M': 1000000,
            'B': 1000000000
        }
        
        try:
            match = re.search(r'([\d.]+)\s*([KMB]?)', installs_text)
            if match:
                number = float(match.group(1))
                multiplier = match.group(2)
                if multiplier in multipliers:
                    return int(number * multipliers[multiplier])
                return int(number)
            return 0
        except:
            return 0
    
    def clean_text(self, text):
        """Nettoie le texte des caractères spéciaux"""
        if not text:
            return ""
        cleaned = re.sub(r'[^\w\s.,!?;:()\-&@#%$*+=]', '', str(text))
        return cleaned.strip()

    def extract_apps_from_response(self, results, query):
        """Extrait les applications de la réponse SerpAPI"""
        apps_data = []
        
        # 1. Extraire des items_highlight (carrousel en haut)
        items_highlight = results.get("items_highlight", [])
        if items_highlight and len(items_highlight) > 0:
            for app in items_highlight[0]:  # Premier élément de la liste
                try:
                    app_info = {
                        "title": self.clean_text(app.get("title")),
                        "developer": app.get("author", ""),
                        "rating": 0.0,  # Pas de rating dans highlight
                        "installs_text": "",
                        "installs_numeric": 0,
                        "category": "",
                        "description": self.clean_text(app.get("subtitle", "")),
                        "product_id": app.get("product_id", ""),
                        "query": query,
                        "source": "highlight",
                        "scraping_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    if app_info["title"]:
                        apps_data.append(app_info)
                        print(f"✅ Highlight: {app_info['title']}")
                except Exception as e:
                    print(f"❌ Erreur highlight: {str(e)}")
        
        # 2. Extraire des organic_results (résultats principaux)
        organic_results = results.get("organic_results", [])
        for section in organic_results:
            items = section.get("items", [])
            for app in items:
                try:
                    app_info = {
                        "title": self.clean_text(app.get("title")),
                        "developer": app.get("author", ""),
                        "rating": float(app.get("rating", 0)) if app.get("rating") else 0.0,
                        "installs_text": app.get("downloads", ""),
                        "installs_numeric": self.clean_installs_count(app.get("downloads", "")),
                        "category": app.get("category", ""),
                        "description": self.clean_text(app.get("description", "")),
                        "product_id": app.get("product_id", ""),
                        "query": query,
                        "source": "organic",
                        "scraping_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    if app_info["title"]:
                        apps_data.append(app_info)
                        print(f"✅ Organic: {app_info['title']} - Note: {app_info['rating']}")
                except Exception as e:
                    print(f"❌ Erreur organic: {str(e)}")
        
        return apps_data

    def search_google_play(self, query, num_results=20):
        """Recherche d'applications sur Google Play"""
        params = {
            "engine": "google_play",
            "q": query,
            "store": "apps",
            "hl": "en",
            "gl": "us",
            "api_key": SERPAPI_KEY,
            "num": num_results
        }
        
        try:
            print(f"  Envoi requête: {query}")
            search = GoogleSearch(params)
            results = search.get_dict()
            
            # Vérifier s'il y a une erreur
            if "error" in results:
                print(f"❌ Erreur API: {results['error']}")
                return []
            
            print(f"  Format de réponse: {list(results.keys())}")
            
            # Extraire les applications
            apps_data = self.extract_apps_from_response(results, query)
            
            return apps_data
            
        except Exception as e:
            print(f"❌ Erreur lors de la recherche: {str(e)}")
            return []

    def collect_apps_data(self):
        """Collecte les données d'applications"""
        print("Début de la collecte des données Google Play...")
        
        # Applications populaires par catégorie
        categories = [
            "social media",
            "games",
            "productivity", 
            "education",
            "health fitness",
            "finance",
            "entertainment",
            "shopping",
            "travel",
            "photo video"
        ]
        
        for category in categories:
            print(f"\nRecherche catégorie: '{category}'")
            apps = self.search_google_play(category, num_results=15)
            self.all_apps.extend(apps)
            print(f"  {len(apps)} applications trouvées")
            
            # Pause pour respecter les limites de l'API
            import time
            time.sleep(2)
        
        # Supprimer les doublons
        self.remove_duplicates()
        print(f"\nTotal d'applications uniques collectées: {len(self.all_apps)}")
    
    def remove_duplicates(self):
        """Supprime les doublons basés sur product_id"""
        seen_ids = set()
        unique_apps = []
        
        for app in self.all_apps:
            app_id = app.get("product_id") or app.get("title", "").lower()
            if app_id and app_id not in seen_ids:
                seen_ids.add(app_id)
                unique_apps.append(app)
        
        self.all_apps = unique_apps
    
    def save_to_csv(self, filename=None):
        """Sauvegarde les données en CSV"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"google_play_apps_{timestamp}.csv"
        
        if not self.all_apps:
            print("Aucune donnée à sauvegarder")
            return None
            
        df = pd.DataFrame(self.all_apps)
        
        # Réorganiser les colonnes pour plus de clarté
        columns_order = [
            'title', 'developer', 'rating', 'installs_text', 'installs_numeric',
            'category', 'description', 'product_id', 'query', 'source', 'scraping_date'
        ]
        df = df.reindex(columns=columns_order)
        
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Données sauvegardées en CSV: {filename}")
        
        # Afficher un aperçu des données
        print(f"\nAperçu des données sauvegardées:")
        print(f"Colonnes: {list(df.columns)}")
        print(f"Nombre d'applications: {len(df)}")
        
        if len(df) > 0:
            print(f"\nQuelques applications:")
            for i, row in df.head(5).iterrows():
                rating_display = f"{row['rating']}/5" if row['rating'] > 0 else "N/A"
                installs_display = row['installs_text'] or "N/A"
                print(f"  {i+1}. {row['title']} - Note: {rating_display} - Téléch.: {installs_display}")
            
        return filename

def main():
    analyzer = GooglePlayAnalyzer()
    
    try:
        # Collecte des données
        analyzer.collect_apps_data()
        
        if not analyzer.all_apps:
            print("\nAucune donnée collectée.")
            return
        
        # Sauvegarde en CSV
        csv_file = analyzer.save_to_csv()
        
        print("\n" + "="*50)
        print("COLLECTE TERMINÉE AVEC SUCCÈS!")
        print("="*50)
        print(f"Fichier CSV généré: {csv_file}")
        print(f"Total applications: {len(analyzer.all_apps)}")
        
    except Exception as e:
        print(f"Erreur lors de l'analyse: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()