from pathlib import Path
import configparser


def get_save_filename(filename):
    if "." in filename:
        return filename.rsplit(".", 1)[0] + "_predict." + filename.rsplit(".", 1)[1]
    return


BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "media" / "upload"
PREDICT_FOLDER = BASE_DIR / "media" / "predict"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

config = configparser.ConfigParser()
config.read(BASE_DIR / "settings.ini", encoding="utf-8")

url = config["api"]["url"]

file_name = config["image"]["file_name"]
image_show = config.getboolean("image", "show")

file_path = UPLOAD_FOLDER / file_name
save_path = PREDICT_FOLDER / get_save_filename(file_name)
log_path = BASE_DIR / "SSD_portfolio.log"
