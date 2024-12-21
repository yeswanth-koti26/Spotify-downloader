import logging

def setup_logger():
    logging.basicConfig(
        filename="spotify_downloader.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()

logger = setup_logger()
