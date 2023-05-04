from django.urls import path
from . import views
from .views import AlunoCreateView, AlunoUpdateView

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    #################################
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),
    #################################
    path('contact', views.contact_view, name='aluno-contact'),
    #################################
    path('aluno/create/', AlunoCreateView.as_view(), name='aluno-create'),
    path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),
    path('delete/<int:id>', views.deleteAluno, name="delete-aluno"),

]


