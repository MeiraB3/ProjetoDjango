from django.shortcuts import render, redirect

# Create your views here.
from .models import Aluno
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list':alunos_list})


def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk = id)
    print(aluno)
    return render (request, 'main/alunoID.html',{'aluno':aluno})

def contact_View(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('name:',name)
        print('Email:',email)
        print('message:',message)
    return render(request, 'main/contact.html')

from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView
from .forms import AlunoForm

class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('aluno-lista')
    template_name = 'main/aluno_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
##############################################
'''def aluno_create_view(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit = False)
            aluno.user = request.user
            aluno.save()
            return redirect(reverse('aluno-lista'))
    else:
        form = AlunoForm()

    return render(request, 'aluno_form.html',{'form':form})'''
##############################################

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    sucess_url = reverse_lazy('aluno-lista')

