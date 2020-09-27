from django.shortcuts import render
import pickle
import os
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
Pkl_Filename = os.path.join(BASE_DIR, "app/tweet.pkl")

with open(Pkl_Filename, 'rb') as file:  
    Pickled_LR_Model = pickle.load(file)

# Create your views here.
def index(request):
	
	if request.method=="POST":

		textinp = request.POST["textinp"]
		print(textinp)
		flag = Pickled_LR_Model.predict(pd.Series(textinp)) 
		print(flag)
		if(flag[0] == 0):
			fd = True
		else:
			fd = False
		context = {
			"flag" : fd
		}
		return render(request,'app/index.html', context)	


	else:
		return render(request,'app/index.html')	