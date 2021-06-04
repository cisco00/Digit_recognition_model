import io
import os
import requests
import pytest
from cv2.cv2 import FileStorage

from fastapi.testclient import TestClient 
from main import ap


@pytest.fixture
def client():
    return TestClient


def test_upload_image_data(client):
    file_name = "fake-text-stream.png"
    data = {'image': (io.BytesIO(b"some initail text data"), file_name)
            }
    response = client.post('/upload', data=data)
    assert response.status_code == 404

    
def test_output_image_data(client):
    response = client.get('/predict')
    response_data = response.BytesIO()

    assert response_data.status_code == 404
    assert response_data.BytesIo()["output"] in [response]
