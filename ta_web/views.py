from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Document
from .forms import CreateUserForm

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

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password2']
            )
            login(request, user)
            return redirect('ta_web:homepage')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = CreateUserForm()
        return render(request, 'registration/register.html', {'form': form})

def logout_message(request):
    return render(request, 'ta_web/logout_message.html')
