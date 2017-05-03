from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Document
from .forms import CreateUserForm

def homepage(request):
    return render(request, 'ta_web/home.html')

@login_required
def show_entries(request):
    # TODO filter by logged in user
    documents = Document.objects.all()
    return render(request, 'ta_web/show_entries.html', {'documents': documents})

@login_required
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
                password=request.POST['password1']
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
