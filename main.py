from typing import Union

from fastapi import FastAPI
from typing import Union, List
from fastapi import FastAPI, UploadFile, File
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from fastapi.middleware.cors import CORSMiddleware
import io
import os

origins = [
    "*"
]
app = FastAPI()
# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"Hello": "World"}

from_recognizer_endpoint = "https://foysal360.cognitiveservices.azure.com/"
form_recognizer_key = "f2f33d180dbb4f9683a74d637bd7838c"
@app.post("/upload/")
async def upload_file(file: UploadFile):

    document_analysis_client = DocumentAnalysisClient(
        endpoint= from_recognizer_endpoint, credential=AzureKeyCredential(form_recognizer_key)
    )
    image_date=await file.read()
    result = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-read", document=image_date
    ).result()

    return {"filename": file.filename,
        "analysis_result": result.content
        }
   


