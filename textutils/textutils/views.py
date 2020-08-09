# i have created this file ----- sourabh mishra
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


def analys(request):



    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'removed punctuations', 'analyzed_text': analyzed}
        return render(request, 'analys.html', params)
    elif fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analys.html', params)
    elif newlineremover=="on":
        analyzed = ""
        for char in djtext:
            if char !="\n":
             analyzed = analyzed + char
        params = {'purpose': 'remove new line', 'analyzed_text': analyzed}
        return render(request, 'analys.html', params)
    elif spaceremover=="on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == "" and djtext[index+1]==""):
                   analyzed = analyzed + char
        params = {'purpose': 'remove space', 'analyzed_text': analyzed}
        return render(request, 'analys.html', params)
    else:
     return HttpResponse("error")





#
#
# def capfirst(request):
#     return HttpResponse("capfirst")
# def newlineremover(request):
#     return HttpResponse("new liner remove first")
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</a>")