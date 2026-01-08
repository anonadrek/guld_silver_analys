class MetalAnalyzer:
    def __init__(self, prices, logger):
        self.gold_price = prices.get("gold", 0)
        self.silver_price = prices.get("silver", 0)
        self.logger = logger

    def calculate_gold_silver_ratio(self):
        """Räknar ut hur många gram silver du får för ett gram guld."""
        if self.silver_price == 0:
            self.logger.error("Silverpriset är 0, kan inte dividera.")
            return 0
        
        ratio = self.gold_price / self.silver_price
        return round(ratio, 2)

    def calculate_potential_buying_power(self, budget):
        """Räknar ut hur mycket man kan köpa för budgeten."""
        gold_amount = budget / self.gold_price
        silver_amount = budget / self.silver_price
        
        return {
            "gold_grams": round(gold_amount, 2),
            "silver_grams": round(silver_amount, 2)
        }