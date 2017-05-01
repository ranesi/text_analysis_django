from django.shortcuts import render, get_object_or_404, redirect
from .models import Document

def homepage(request):
    documents = Document.objects.all()
    return render(request, 'ta_web/show_entries.html', {'documents': documents})

def show_entries(request):
    documents = Document.objects.all()
    return render(request, 'ta_web/show_entries.html', {'documents': documents})

def entry_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'ta_web/entry_detail.html', {'document': document})
