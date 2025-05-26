from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('admit-card/', views.admit_card, name='admit_card'),
    path('download-admit-card/', views.download_admit_card, name='download_admit_card'),
    path('download-download-documents/', views.download_download_documents, name='download_download_documents'),
    path('results/', views.results, name='results'),
    path('logout/', views.user_logout, name='logout'),
]
