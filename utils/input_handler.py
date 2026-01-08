def get_user_budget():
    """Ber användaren om en budget och hanterar felaktig input."""
    while True:
        user_input = input("Ange din investeringsbudget (SEK): ")
        
        # Student-fix: Ta bort mellanslag (t.ex. "1 000" -> "1000")
        # och byt ut kommatecken mot punkt (t.ex. "10,50" -> "10.50")
        clean_input = user_input.replace(" ", "").replace(",", ".")

        try:
            if not clean_input: # Om användaren bara trycker enter
                print("Du måste skriva något.")
                continue

            value = float(clean_input)
            if value < 0:
                print("Budgeten kan inte vara negativ. Försök igen.")
            else:
                return value
        except ValueError:
            print(f"Felaktig inmatning: '{user_input}'. Vänligen ange ett rent nummer (t.ex. 1000).")
