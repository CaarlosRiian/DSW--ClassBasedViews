from django.contrib import admin
from django.urls import path
from aluno  import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('aluno/editar/<int:id>/', views.AlunoEditar.as_view(), name='aluno_editar'),
    path('aluno/criar/', views.AlunoCriar.as_view(), name='aluno_criar'),
    path('aluno/remover/<int:id>/', views.AlunoRemover.as_view(), name='aluno_remover'),
    path('aluno/listar/', views.AlunoListar.as_view(), name='aluno_listar'),

]



