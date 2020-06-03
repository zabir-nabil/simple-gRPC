# A procedure which decodes base64 image, runs some machine learning model/ operation(s) (in our case we'll just return the mean of the pixel value)

import numpy as np 
import base64
import zlib

def predict(b64img_compressed, w, h):
    b64decoded = base64.b64decode(b64img_compressed)

    decompressed = b64decoded #zlib.decompress(b64decoded)

    imgarr = np.frombuffer(decompressed, dtype=np.uint8).reshape(w, h, -1)

    return imgarr.shape[2], np.mean(imgarr)