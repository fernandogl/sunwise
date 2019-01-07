from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views


router = DefaultRouter()
router.register(r'urls', views.UrlViewSet)

urlpatterns = [
    path('archivo_url/', views.ArchivoUrlView.as_view(), name='archivo_url' ),
    path('api/', include(router.urls)),
    path('urls/', views.UrlListView.as_view()),
    path('<slug:codigo>/', views.redirige, name='redirige' ),
]