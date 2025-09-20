from fastapi import FastAPI
from service.api.api import main_router
import onnxruntime as rt

app = FastAPI(project_name="Emotion Detection method")

app.include_router(main_router)

providers = ['CPUExecutionProvider']
m = rt.InferenceSession(
        r"C:\Users\RKCINDIA\object_detection -task\effect_quatized.onnx",
        providers=providers)

@app.get("/")
def root():
    return {"hello": "world"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

