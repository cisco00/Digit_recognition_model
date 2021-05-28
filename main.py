import uvicorn
from io import BytesIO
from tkinter import Image
from starlette.responses import RedirectResponse
from fastapi import FastAPI, File, UploadFile
from components import predict
from PIL import Image

app = FastAPI()


def read_image_file(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image

@app.get('/index')
async def image_upload_test():
    return "ready for image upload"


@app.get("/predict/image")
async def index():
    return RedirectResponse(url="/docs")


async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(",")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg, jpeg or png format"
    image = read_image_file(await file.read())
    prediction = predict(image)

    return prediction


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
