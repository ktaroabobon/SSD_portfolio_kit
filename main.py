import logging

import settings
import tools

logging.basicConfig(level=logging.INFO, filename=settings.log_path)

if __name__ == "__main__":
    tools.get_predict_image()
