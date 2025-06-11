import cv2
import numpy as np
from pyzbar.pyzbar import decode

def ler_qrcode(imagem_bytes):
    nparr = np.frombuffer(imagem_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    decodificados = decode(img)
    return decodificados[0].data.decode('utf-8') if decodificados else None
