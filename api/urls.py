# api/urls.py

from django.urls import path
from .views import SignupView, LoginView, BookAppointmentView, UploadMedicalHistoryView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('appointments/book/', BookAppointmentView.as_view(), name='book-appointment'),
    path('medical-history/upload/', UploadMedicalHistoryView.as_view(), name='upload-medical-history'),
]
