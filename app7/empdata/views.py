from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

# Create your views here.
from empdata.models import Employee


def emphome(request):
    return render(request,'emphome.html')

def empsignup(request):
    return render(request,'empsignup.html')

def empreg(request):
    v1 = request.GET.get('n1')
    v2 = request.GET.get('n2')
    v3 = request.GET.get('n3')
    v4 = request.GET.get('n4')
    v5 = request.GET.get('n5')
    emp1 = Employee(email=v1 , pswd = v2 , fullname = v3 , city = v4 , salary = v5 )
    try:
        emp = Employee.objects.get(email = v1)
        return render(request , "empregfail.html" , {'msg':'Email already Exists Please try another one'})
    except ObjectDoesNotExist:
        emp1.save()
        return render(request , "empregsucess.html" , {'msg':'Registration Done'})


def allempv(request):
    employees = Employee.objects.all()
    return render(request, 'allemp.html',{'emps':employees})

def getempdetail(request):
    return render(request,'getempdetail.html')
def getresultv(request):
    inpemail = request.GET.get('n1')
    try:
        emp = Employee.objects.get(email = inpemail)
        return render(request,'getsuccess.html',{'e1':emp})
    except ObjectDoesNotExist:
        return render(request,'getfail.html',{'msg':'This email does not exist'})
def updatev(request):
    return render(request,'updatedetail.html')
def updatedetailv(request):
    empdata = request.GET.get('n1')
    try:
        emp = Employee.objects.get(email=empdata)
        return render(request,'updateget.html',{'e1':emp})
    except ObjectDoesNotExist:
        return render(request,'getfail.html',{'msg':'This email does not exist'})
def updategetv(request):
    n_email = request.GET.get('n1')
    n_pass = request.GET.get('n2')
    n_name = request.GET.get('n3')
    n_city = request.GET.get('n4')
    n_sal = request.GET.get('n5')
    emp = Employee.objects.get(email = n_email)
    emp.pswd = n_pass
    emp.fullname = n_name
    emp.city = n_city
    emp.salary = n_sal
    emp.save()
    return render(request,'updatesuccess.html',{'e1':emp})

def deletev(request):
    return render(request,'delete.html')
def deletedetail(request):
    n_email = request.GET.get('n1')
    n_pass = request.GET.get('n2')
    try:
        emp = Employee.objects.get(email=n_email,pswd = n_pass)
        emp.delete()
        return render(request , 'emphome.html')
    except ObjectDoesNotExist:
        return render(request,'getfail.html',{'msg':'This email or password does not exist'})



def signinv(request):
    return render(request,'signin.html')
def signinstatusv(request):
    n_email = request.GET.get('n1')
    n_pass = request.GET.get('n2')
    if(n_email == "" or n_pass == "" ):
        return render(request,'signin.html')
    else:
        try:
            emp = Employee.objects.get(email = n_email , pswd = n_pass)
            m1 = "hey " + emp.fullname + ", SignIn success"
            return render(request , "empregsucess.html" , {'msg':m1})
        except:
            return render(request , "empregfail.html" , {'msg':'Email not Exists in DB Please try another one'})

