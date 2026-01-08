from utils.config_loader import load_config
from utils.logger import setup_logger
from utils.input_handler import get_user_budget
from core.data_loader import fetch_market_prices
from core.analyzer import MetalAnalyzer
import sys

def main():
    # 1. Ladda inställningar
    config = load_config()
    if not config:
        sys.exit("Kunde inte starta programmet: Config saknas.")

    # 2. Starta logger
    logger = setup_logger(config["app_name"], config["log_folder"])
    logger.info("Programmet startar...")

    # 3. Hämta data
    prices = fetch_market_prices()
    logger.info(f"Dagens priser inlästa: Guld={prices['gold']} kr, Silver={prices['silver']} kr")

    # 4. Initiera analys-klassen
    analyzer = MetalAnalyzer(prices, logger)
    
    # Gör en beräkning (Gold/Silver ratio)
    ratio = analyzer.calculate_gold_silver_ratio()
    print(f"\n--- ANALYS ---")
    print(f"Guld/Silver-ratio idag är: {ratio}")
    print("Detta betyder att 1g guld är värt lika mycket som " + str(ratio) + "g silver.\n")

    # 5. Hantera användarinput (Säker input)
    budget = get_user_budget()
    logger.info(f"Användaren angav budget: {budget} SEK")

    # 6. Bearbeta data baserat på input
    result = analyzer.calculate_potential_buying_power(budget)

    # 7. Skriv ut resultat
    print("\n--- RESULTAT ---")
    print(f"För {budget} kr kan du köpa:")
    print(f"- {result['gold_grams']} gram Guld")
    print(f"- {result['silver_grams']} gram Silver")
    
    logger.info("Analys klar. Avslutar programmet.")

if __name__ == "__main__":
    main()