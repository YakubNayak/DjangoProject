from django.shortcuts import render
def homev(request):
    return render(request,'Home.html')
def aboutv(request):
    return render(request,'About.html')
def contactv(request):
    return render(request,'Contact.html')
def donatev(request):
    return render(request,'Donate.html')
