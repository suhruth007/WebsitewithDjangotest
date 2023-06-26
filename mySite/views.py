# I have created this file - Perugu
from django.http import HttpResponse
from django.shortcuts import render


# code for video (Practice)6
# def index(request):
#     return HttpResponse('''<h1>suhruth</h1> <a href ='https://www.youtube.com/watch?v=AepgWsROO4k&list
#     =PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7&ab_channel=CodeWithHarry'> Django code with harry</a>>
#     <a href = ' https://www.chess.com/home' >Chess.com</a>>
#     <a href = ' https://www.instagram.com' >instagram</a>>
#     <a href = ' https://www.google.com' >google</a>>
#     <a href = ' https://mail.google.com/' >Gmail</a>>
#     <a href = ' https://lichess.org/' >Lichess</a>>''')
#
#
# def about(request):
#     return HttpResponse('about')


# Code for video(practice) 7
# def capfirst(request):
#     return HttpResponse("Capitalize first")
#
#
# def newlineremove(request):
#     return HttpResponse('new line remove')
#
#
# def spaceremove(request):
#     return HttpResponse('space remover')
#
#
# def charcount(request):
#     return HttpResponse('charcount')


def index(request):
    # perugu = {'name': 'james bond', 'age': '007'}
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyze(request):
    # Get the text
    djtext = request.GET.get('search', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover =='on':
        return HttpResponse('shut the f up')
    else:
        return HttpResponse('Error')
