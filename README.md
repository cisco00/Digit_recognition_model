# Digit_recognition_model
A tensorflow model that was build on fastAPI framework to predict a hand written digits or hand-written numbers. For instance if you download an image that is blurring and you want to confirm if it is a particulare number you can use the api to test.

#PROJECT SETUP
Before going through the steps you need to have the following pre-installed

#Tools
1. python3.8.10
2. fastAPI
3. you can install the requiremnet using 
     a. Linux = [pip install -r requirements\dev.linux.txt]
     b. windows = [pip install -r requirements\dev.windows.txt]
   but if you wish to start the project new use the below to setup
4. create a virtual environment using [python -m venv env] and activate the environment using 
    a. Linux = [source env/bin/activate]
    b. cd [scripts/bin/sctivate]
 
#THE FASTAPI APPLICATION
The model was build using fastAPI framework with two major files, [](main.py) and [](component.py)

REQUIREMENTs
1. fastai==0.63.0
2. tensorflow-cpu==2.5.0
3. uvicorn==0.14.0
4. gunicorn==20.0.4
5. python-multipart==0.0.5
6. Pillow==8.2.0
7. uvloop==0.14.0
8. numpy==1.19.5
9. httptools==0.1.1
10. starlette==0.14.2

#NOTEBOOK
In building the model I used the reference [Digit_recognition_model](https://github.com/cisco00/Digit_recognition_model/blob/master/digit-prediction-model.ipynb) to build the model.

#PROCFILE
In other for the fastAPI app to run on cloud environent there is the need to install gunicorn, while to run on local environment you need to install uvicorn without any of the above you will be having an error either locally or on the cloud environment.
cloud env = web: [gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app]
local-env = [uvicorn]

#RUNTIME
For the application to work on cloud there is the need to specify the python version you use in building the fastAPI.
[python-3.8.10]

#FRONTEND
The frontend of the app was build with HTMl and CSS

#REFERENCE
     1. FastAPI Documentation. [link](https://fastapi.tiangolo.com/)
     2. Requests Documentation. [link](https://docs.python-requests.org/en/master/)
     3. Pytest Documentation. [link](https://docs.pytest.org/en/stable/contents.html)

interacte with the model using the link below
url = https://digit-prediction1.herokuapp.com/

[twitterhandle](https://twitter.com/ikwufrancis)
[linkedin](https://www.linkedin.com/in/idoko-ikwu-633b6134/)


