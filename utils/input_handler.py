def get_user_budget():
    """Ber användaren om en budget och hanterar felaktig input."""
    while True:
        user_input = input("Ange din investeringsbudget (SEK): ")
        try:
            value = float(user_input)
            if value < 0:
                print("Budgeten kan inte vara negativ. Försök igen.")
            else:
                return value
        except ValueError:
            print("Felaktig inmatning. Vänligen ange ett nummer.")