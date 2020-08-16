#
# This is Created by Moinuddin Shovan
from django.http import HttpResponse
from django.shortcuts import render


# Code for harry 6

# def home(request):
#
#     return HttpResponse('''
#     <a href = "https://docs.djangoproject.com/en/3.1/releases/3.1/">Django 3.1 Doc</a> &nbsp
#     <a href = "https://docs.djangoproject.com/en/3.1/releases">Django releases</a> &nbsp
#     <a href = "https://docs.djangoproject.com/en/3.1/">Django</a>
#
#     ''')
#
#
# def about(request):
#     return HttpResponse('About MK Shovan')

# Code for harry 7


def home(request):
    params = {'name': 'Shovan', 'place': 'Bangladesh'}
    return render(request, 'index.html', params)
    # return HttpResponse('Home')


# def remove_punc(request):
#     #Get text from html
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze
#     return HttpResponse('Remove Punctuation')
#
#
# def capitalize(request):
#     return HttpResponse('Capitalize Words')
#
#
# def newline_remove(request):
#     return HttpResponse('Newline Remover')
#
#
# def space_remove(request):
#     return HttpResponse('Space remover')
#
#
# def char_count(request):
#     return HttpResponse('Character Counter')


def analyze(request):
    punctuations = '''[]{}-!"#$%&.\/:;<=>?@_`|'()*+,^'''
    # Get text from html
    djremove = request.POST.get('removepunctuation', 'off')
    djuppercase = request.POST.get('uppercase', 'off')
    djspaceremove = request.POST.get('removespace', 'off')
    djnewlineremove = request.POST.get('newlineremove', 'off')
    djcharcount = request.POST.get('charcount', 'off')
    djtext = request.POST.get('text', 'default')


    # Multi Functional

    strr = djtext
    purpose = ""

    if djremove == 'on':
        tempStr = ""
        for i in djtext:
            if i not in punctuations:
                tempStr = tempStr + i
        params = {'purpose': 'remove Punctuations', 'answer': tempStr}
        strr = tempStr
        purpose += " | Remove Punctuations "
        # return render(request, 'analyze.html', params)
    if djuppercase == 'on':
        strr = strr.upper()
        params = {'purpose': 'Caps', 'answer': strr}
        purpose += "| Uppercase "
        # return render(request, 'analyze.html', params)

    if djnewlineremove == 'on':
        tempStr = ""
        for i in strr:
            if i != '\n' and i != '\r':
                tempStr += i
        params = {'purpose': 'New Line remove', 'answer': tempStr}
        strr = tempStr
        purpose += "| new line removal "
        # return render(request, 'analyze.html', params)

    if djspaceremove == 'on':
        tempStr = ""
        for index, ch in enumerate(strr):
            if not (strr[index] == " " and strr[index + 1] == " "):
                tempStr += ch
        params = {'purpose': 'spaces remove', 'answer': tempStr}
        strr = tempStr
        purpose += "| Spaces removal "

    if djcharcount == 'on':
        count = 0
        for char in djtext:
            if char != ' ' or char != '\n':
                count = count + 1
        strr += f'\tNumber of chars = {count}'
        params = {'purpose': 'Char Counter', 'answer': strr}
        purpose += '|Counter'

    params = {'purpose': purpose, 'answer': strr}

    if djremove == 'on' or djuppercase == 'on' or djnewlineremove == 'on' or djspaceremove == 'on' or djcharcount == 'on':
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error by Input or Internal System')

def contactus(request):
    return render(request, 'contactus.html')

