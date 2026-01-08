import json
import os

def load_config(config_name="config.json"):
    """Läser in konfigurationen från en JSON-fil."""
    try:
        # Hämta den absoluta sökvägen till mappen där scriptet körs
        base_path = os.getcwd()
        full_path = os.path.join(base_path, config_name)
        
        with open(full_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: Kunde inte hitta {config_name}")
        return None