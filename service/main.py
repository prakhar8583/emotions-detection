from fastapi import FastAPI
from service.api.api import main_router
import onnxruntime as rt
import os


app = FastAPI(project_name="Emotion Detection method")

app.include_router(main_router)

providers = ['CPUExecutionProvider']

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "effect_quatized.onnx")  # <- removed "models"
m = rt.InferenceSession(model_path, providers=providers)

@app.get("/")
def root():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

