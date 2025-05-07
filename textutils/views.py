from django.http import HttpResponse 
from django.shortcuts import render  


def index(request):
    return render(request,'index.html')
def analyze(request):
      if request.method=="GET":
          text =request.GET.get("textname","default")
          removepunc =request.GET.get("removepunc","off")

          punctuations="""!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
          if removepunc == "on":
              analyzed=  ""
              for char in text:
                  if char not in punctuations:
                      analyzed=analyzed+char

              data={
                'texts':analyzed
              }
          else:
               return HttpResponse("ERROR") 
          
      return render(request,"analyze.html",data)

