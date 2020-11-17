from django.shortcuts import render
from django.views import View
import pickle as pkl
import numpy as np
# Create your views here.

model_path = './models/car_price.pkl'


file = open(model_path , 'rb')
model = pkl.load(file)


class MainView(View) :
    def get(self , request , *args , **kwargs):
        content = {}
        return render(request ,'car_price/home.html', content)
    def post(self , request, *args , **kwargs):
        L = [val for key ,val in request.POST.items()]
        del L[0]
        if L[4] == '01' :
            L[4] = [0,1]
        elif L[4] == '10' :
            L[4] = [1,0]
        else :
            L[4] = [1,1]
        print(L)
        L1 = L[:4]
        l = L[4]
        L2 = L[5:]

        print(L1 ,L2 ,l)
        for x in l :
            L1.append(x)
        L = L1 + L2
        L = [float(x) for x in L]
        X = np.array(L)
        X =np.expand_dims(X ,0)
        content = {'pred' : model.predict(X)[0]}


        return render(request ,'car_price/prediction.html',content)

class PredView(View) :
    def get(self , request , *args , **kwargs):
        content = {}
        return render(request ,'car_price/prediction.html', content)
