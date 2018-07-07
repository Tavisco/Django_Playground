from django.urls import path
from .views import persons_list, persons_new, persons_update, persons_delete


urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id_person>/', persons_update, name='persons_update'),
    path('delete/<int:id_person>/', persons_delete, name='persons_delete'),
]
