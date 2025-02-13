from rest_framework.routers import DefaultRouter 

from .views import UserViewSet, ProjectViewSet, CategoryViewSet, PriorityViewSet, TaskViewSet 

 

router = DefaultRouter() 

router.register(r'users', UserViewSet) 

router.register(r'projects', ProjectViewSet) 

router.register(r'categories', CategoryViewSet) 

router.register(r'priorities', PriorityViewSet) 

router.register(r'tasks', TaskViewSet) 

 

urlpatterns = router.urls 

from django.contrib import admin 

from django.urls import path, include 

from .views import contact_view

from django.conf import settings 

from django.conf.urls.static import static 

from .views import share_cv_email 

 

urlpatterns = [ 

    path('admin/', admin.site.urls), 

    path('api/', include('core.urls')), 

    path('contact/', contact_view, name='contact'),

    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT), 

    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'), 

] 