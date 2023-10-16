In the case_notebook folder, you can find all the data analyses and machine learning model training and evaluation code for the loan_approval_dataset. The best-performing model is saved within this notebook.

Inside the model_service folder, you'll find the code for deploying the trained model. In app.py, a service is developed using Flask to return the model's prediction result based on the given data.

The deployment of the model is carried out using Dockerfile.