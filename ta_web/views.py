from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Document

def homepage(request):
    # temporary
    documents = Document.objects.all()
    return render(request, 'ta_web/show_entries.html', {'documents': documents})

def show_entries(request):
    documents = Document.objects.all()
    return render(request, 'ta_web/show_entries.html', {'documents': documents})

def entry_detail(request, pk):
    # try:
    #     document = Document.objects.get(pk=pk)
    # except Document.DoesNotExist:
    #     document = None
    #     raise Http404('Document DOES NOT EXIST')
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'ta_web/entry_detail.html', {'document': document})

def add_document(request):
    pass
