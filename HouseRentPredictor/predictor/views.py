from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from scipy.stats import boxcox
from scipy.special import inv_boxcox
from sklearn.preprocessing import StandardScaler
import pickle 
import pandas as pd
import numpy as np

# class MyModel:
#     def __init__(self, model, lambda_value):
#         self.model = model
#         self.lambda_value = lambda_value

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def predictor(request):
    return render(request, 'predictor.html')

def predict(request):
    if(request.method == 'POST'):
        city = request.POST['city']
        if(city == 'Mumbai'): 
            city = int(1)
        else:
            city = int(0)
        area_type = request.POST['area_type']
        if(area_type == 'Super Area'):
            area_type = int(1)
        else:
            area_type = int(0)
        furnishing = request.POST['furnishing']
        # tenant = request.POST['tenant']
        contact = int(1)
        bhk = request.POST['bhk']
        bhk = int(bhk)
        floorlvl = request.POST['floor_level']
        floorlvl = int(floorlvl)
        # totalfloors = request.POST['total_floors']
        bathrooms = request.POST['bathrooms']
        bathrooms = int(bathrooms)
        size = request.POST['size']
        size = int(size)
        val = np.array([[contact,city,bathrooms,bhk,size]])
        print(val)
        file = "./model.pkl"
        with open(file, 'rb') as f:
            model = pickle.load(f)

        # lam = -0.297859738284799
        # model = my_model_object.model

        res = model.predict(val)
        print(type(res))   
        result = np.expm1(res)
        print(type(result))
        # result = inv_boxcox(result,lam)
        # result = "hello world"
        print("context result ->",*result)
        context = {"result" : result}
    return render(request,"predict.html",context)    

def link2dataset(request):
    return HttpResponseRedirect("https://www.kaggle.com/datasets/f3fcbc8053a9243797d18047789e027fbffc29deed67c3c323b830c94b9e8fe3")

def link2notebook(request):
    return HttpResponseRedirect("https://github.com/Chinmay575/House-Rent-Prediction") 