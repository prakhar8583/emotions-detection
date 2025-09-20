from fastapi import APIRouter, UploadFile, HTTPException
from PIL import Image
from io import BytesIO
import numpy as np
from service.core.logic.onnx_inference import emotions_detector
from service.core.schemas.output import APIOutput
from pydantic import BaseModel


detect_router = APIRouter()

class APIOutput(BaseModel):
    emotion: str
    time_elapse:str
    time_elapse_preprocees:str

@detect_router.post("/detect",response_model=APIOutput)
def detect(im: UploadFile):
    if im.filename.split(".")[-1].lower() not in ("jpg", "jpeg", "png"):
        raise HTTPException(
            status_code=415,
            detail="Not an Image"
        )
    
    # Open image and convert to numpy array
    image = Image.open(BytesIO(im.file.read()))
    image = np.array(image)

    return emotions_detector(image)
