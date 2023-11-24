from django.contrib import admin
from django.urls import path
from hospedagem import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('hospedagem/editar/<int:id>/', views.HospedagemEditar.as_view(), name='hospedagem_editar'),
    path('hospedagem/criar/', views.HospedagemCriar.as_view(), name='hospedagem_criar'),
    path('hospedagem/remover/<int:id>/', views.HospedagemRemover.as_view(), name='hospedagem_remover'),
    path('hospedagem/listar/', views.HospedagemListar.as_view(), name='hospedagem_listar'),

]



