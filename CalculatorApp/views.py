from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

global equation

def evaluater(request):
    try:
        equation = request.GET['calc']
    except:
        equation = '0'
    try:
        answer = eval(equation)
    except:
        if equation == "":
            answer = 0
        else:
            answer = 'Invaid Input'
        #print('notworking')
    return render(request, r"D:\Projects_SLA_2021\WebCalculator\template_html\template.html",{"ans_": answer})
