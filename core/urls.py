from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import home, about, contact, task_list, task_create, task_update, task_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('tasks/', task_list, name='task_list'),
    path('tasks/new/', task_create, name='task_create'),
    path('tasks/<int:pk>/edit/', task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
