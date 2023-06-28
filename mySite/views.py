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
    """get the 'search' value(default if empty) from the HttpRequest 
    # from client server"""
    removepunc = request.GET.get('removepunc', 'off')
    """
    get after requesting the value returned by 'removepunc' HttpRequest
    and stored returned value in removepunc variable
    """
    fullcaps = request.GET.get('fullcaps', 'off')
    """
        get after requesting the value returned by 'fullcaps' HttpRequest
        and stored returned value in fullcaps variable 
    """
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}  # params stand for parameters
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)
    elif spaceremover == 'on':
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed extra spaces', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)

    elif charcounter == 'on':
        chars = {}
        for i in djtext:
            if i in chars:
                chars[i] += 1
            else:
                chars.update({i: 1})
        params = {'purpose': 'character counter', 'analyzed_text': chars}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')
