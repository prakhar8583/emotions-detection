from fastapi import APIRouter,UploadFile,HTTPException
from PIL import Image
from io import BytesIO
import numpy as np

test_router=APIRouter()
# here we use get methord and path would be detect
@test_router.get("test/")
def testing():
   
    
    
 return {"testing": "testing"}
    

    