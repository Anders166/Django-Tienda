from django.urls import path
from . import views

urlpatterns = [
    # Productos
    path('', views.lista_productos, name='lista_productos'),
    path('productos/nuevo/', views.crear_producto, name='crear_producto'),

    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categorias/<int:pk>/', views.detalle_categoria, name='detalle_categoria'),
    path('categorias/<int:pk>/editar/', views.editar_categoria, name='editar_categoria'),
    path('categorias/<int:pk>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
]
