from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('blog-single/',views.blog_single,name='blog-single'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('doctor-detail/',views.doctor_detail,name='doctor-detail'),
    path('doctors/',views.doctors,name='doctors'),
    path('details/<int:pk>/',views.details,name='details'),
    path('book-appointment/<int:pk>/',views.book_appointment,name='book-appointment'),
    path('paitent-appointment/',views.paitent_appointment,name='paitent-appointment'),
    path('cancel-appointment-patient/<int:pk>/',views.cancel_appointment_patient,name='cancel-appointment-patient'),
    path('cancel-appointment-doctor/<int:pk>/',views.cancel_appointment_doctor,name='cancel-appointment-doctor'),
    path('doctor-appointment/',views.doctor_appointment,name='doctor-appointment'),
    path('attend-appointment/<int:pk>/',views.attend_appointment,name='attend-appointment'),
    path('ajax/validate_email/',views.validate_signup,name='validate_email'),
]