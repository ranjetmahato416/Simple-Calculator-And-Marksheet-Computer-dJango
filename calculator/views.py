from tkinter import Variable
from django.http import HttpResponse
from django.shortcuts import render

result = 0
def index(request):

    try:
        if request.method == "POST":
            global result
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('operation')
            
            if opr == "+":
                result = n1+n2;
            elif opr == "-":
                result = n1 - n2;
            elif opr == "*":
                result = n1*n2;
            elif opr == "/":
                result = n1/n2;
            elif opr == "%":
                result = n1%n2;

    except:
        result = "Invalid operation.";
    print(result);
    return render(request, "index.html", {'result':result})

def marksheet(request):

    if request.method == "POST":
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))
        s6 = eval(request.POST.get('subject6'))

        t = s1+s2+s3+s4+s5+s6
        print(t)
        p = t*100/600
        "%.2f" % round(p, 2)
        if p>80:
            d = "Distinction"
        elif p>60:
            d ="First Division"
        elif p>45:
            d = "Second Division"
        elif p>30:
            d = "Third Division"
        else:
            d = "FAil!"
        data={
            'total': t,
            'percentage' : p,
            'division' : d,
        }
        return render (request, "Marksheet.html", data)
    return render(request, "Marksheet.html");