def fetch_market_prices():
    """
    Simulerar hämtning av dagsaktuella priser.
    Returnerar en dictionary med priser per gram i SEK.
    """
    # I ett riktigt projekt hade vi kanske läst en CSV eller API här.
    # Nu hårdkodar vi datan för enkelhetens skull.
    prices = {
        "gold": 680.50,  # Pris per gram
        "silver": 8.20   # Pris per gram
    }
    return prices