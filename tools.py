import base64
import json
import logging

import requests
import cv2
import numpy as np

import settings

logger = logging.getLogger(__name__)


def get_predict_image(file_path=str(settings.file_path), save_path=str(settings.save_path)):
    logger.info({"action": "get_predict_image", "status": "start"})
    data = base64.b64encode(open(file_path, "rb").read())
    obj = {"body": data.decode("utf-8")}

    logger.info({"action": "get_predict_image", "function": "POST API", "status": "start"})
    r = requests.post(settings.url, json=obj)
    logger.info({"action": "get_predict_image", "function": "POST API", "status": "done"})

    contents = json.loads(r.text)
    logger.info({"action": "get_predict_image", "function": "JSON load"})
    try:
        image_body = base64.b64decode(contents["body"].encode())
    except Exception as e:
        logger.info({"action": "get_predict_image", "message": e})
        return

    img = np.frombuffer(image_body, dtype=np.uint8)
    # raw image <- jpg
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    # 画像を保存
    cv2.imwrite(save_path, img)
    logger.info({"action": "get_predict_image", "status": "done"})

    if settings.image_show:
        logger.info({"action": "get_predict_image", "message": "predict image show"})
        # 画像を表示
        cv2.imshow("Predict Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
