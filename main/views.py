from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main/main.html', {})

def psy_test(request):
    return render(request, 'psy_test/psy_test.html', {})

def mind_tree(request):
    return render(request, 'psy_test/mind_tree.html', {})


def secret_diary(request):
    return render(request, 'psy_test/secret_diary.html', {})


def missing_voice(request):
    return render(request, 'psy_test/missing_voice.html', {})