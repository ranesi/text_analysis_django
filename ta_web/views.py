from django.shortcuts import render, get_object_or_404

def homepage(request):
    return render(request, 'ta_web/base.html', {})

def document_detail(request, pk):
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'ta_web/document_detail.html', {'document': document})
