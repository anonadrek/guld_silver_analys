import logging
import os

def setup_logger(name, log_folder):
    """Sätter upp en logger som sparar till fil och skriver till konsolen."""
    
    # Skapa mappen om den inte finns
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Förhindra dubbla loggar om funktionen körs flera gånger
    if not logger.handlers:
        # Filhanterare
        file_handler = logging.FileHandler(os.path.join(log_folder, "app.log"))
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        
        # Konsolhanterare (så du ser det på skärmen)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(file_format)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    
    return logger