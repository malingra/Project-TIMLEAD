from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('demand', views.demand, name='demand'),
    path('geography', views.show_geography, name='georgaphy'),
    path('skills', views.show_skills, name='skills'),
    path('vacancies', views.show_vacancies, name='vacancies'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)