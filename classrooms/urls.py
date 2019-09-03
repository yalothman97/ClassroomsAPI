
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from apiapp import views as api_views

from rest_framework_simplejwt.views import TokenObtainPairView
# from apiapp.views import ClassroomList, ClassroomDetail, ClassroomCreate, ClassroomUpdate, ClassroomDelete
# from classes.views import classroom_list, classroom_detail, classroom_create, classroom_update, classroom_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),


	path('classroomapi/', api_views.ClassroomList.as_view(), name="classapi-list"), 
    path('classroomapi/<int:classapi_id>/', api_views.ClassroomDetail.as_view(), name="classapi-details"),
    path('classroomapi/<int:classapi_id>/update/', api_views.ClassroomUpdate.as_view(), name="classapi-booking"),
    path('classroomapi/<int:classapi_id>/cancel/', api_views.ClassroomDelete.as_view(), name="classapi-booking"),
    path('classroomapi/create/', api_views.ClassroomCreate.as_view(), name='classapi-create'),


    path('token/', TokenObtainPairView.as_view(), name='token'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
