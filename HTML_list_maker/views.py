from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    order = request.POST.get('order', 'off')
    unorder = request.POST.get('unorder', 'off')
    newLine = request.POST.get('newLine', 'off')
    comma = request.POST.get('comma', 'off')
    semiColon = request.POST.get('semiColon', 'off')
    dot = request.POST.get('dot', 'off')

    # Check which checkbox is on
    if order == "on":
        if newLine == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ol>\n<li>' + str.replace('\r\n', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ol>'
            params = {'purpose': 'ordered List', 'analyzed_text': analyzed}
        elif comma == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ol>\n<li>' + str.replace(',', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ol>'
            params = {'purpose': 'ordered List', 'analyzed_text': analyzed}
        elif semiColon == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ol>\n<li>' + str.replace(';', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ol>'
            params = {'purpose': 'ordered List', 'analyzed_text': analyzed}
        elif dot == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ol>\n<li>' + str.replace('.', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ol>'
            params = {'purpose': 'ordered List', 'analyzed_text': analyzed}

    if (unorder == "on"):
        if newLine == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ul>\n<li>' + str.replace('\r\n', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ul>'
            params = {'purpose': 'unordered List', 'analyzed_text': analyzed}
        elif comma == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ul>\n<li>' + str.replace(',', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ul>'
            params = {'purpose': 'unordered List', 'analyzed_text': analyzed}
        elif semiColon == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ul>\n<li>' + str.replace(';', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ul>'
            params = {'purpose': 'unordered List', 'analyzed_text': analyzed}
        elif dot == "on":
            analyzed = ""
            str = ""
            for char in djtext:
                str = str + char
                analyzed = '<ul>\n<li>' + str.replace('.', '</li>\n<li>')
            analyzed = analyzed + '</li>\n</ul>'
            params = {'purpose': 'unordered List', 'analyzed_text': analyzed}
    if ((order != "on" and unorder != "on") or (newLine != "on" and comma != "on" and semiColon != "on" and dot!="on")):
        param = {'data': djtext}
        return render(request, 'index.html', param)

    return render(request, 'analyze.html', params)
