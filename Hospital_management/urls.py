from django.urls import path
from Hospital_management import views,admin_views,nurse_view,custom_views

urlpatterns = [
        path('',views.new_temp,name='new_temp'),
        path('new',views.new_Admin,name='new_Admin'),
        # path('create',views.new_user,name='User'),
        # path('path',views.new_Nurse,name='Nurse'),
        path('custom',views.customer_user,name='new_Nurse'),
        path('cust',views.Nurse_form,name='Note'),
        path('all',views.All_form,name='allform'),
        path('login_view',views.login_view,name='login_view'),
        path('hospital_add', admin_views.hospital_add, name='hospital_add'),
        path('hospital_view', admin_views.hospital_view, name='hospital_view'),
        path('hospital_update/<int:id>', admin_views.hospital_update, name='hospital_update'),
        path('hospital_delete/<int:dl>', admin_views.hospital_delete, name='hospital_delete'),
        path('vaccin_add', admin_views.vaccin_add, name='vaccin_add'),
        path('vaccin_view', admin_views.vaccin_view, name='vaccin_view'),
        path('vaccin_update/<int:id>', admin_views.vaccin_update, name='vaccin_update'),
        path('vaccin_delete/<int:dl>', admin_views.vaccin_delete, name='vaccin_delete'),
        path('nurse_page', nurse_view.nurse_log, name='nurse_log'),
        path('nurse_complaint_add', nurse_view.nurse_complaint_add, name='nurse_complaint_add'),
        path('nurse_complaint_view', nurse_view.nurse_complaint_view, name='nurse_complaint_view'),
        path('nurse_complaint_update/<int:id>', nurse_view.nurse_complaint_update, name='nurse_complaint_update'),
        path('nurse_complaint_delete/<int:dl>', nurse_view.nurse_complaint_delete, name='nurse_complaint_delete'),
        path('cust_page', custom_views.cust_log, name='cust_log'),
        path('complaint_add',custom_views.complaint_add,name='complaint_add'),
        path('complaint_view',custom_views.complaint_view,name='complaint_view'),
        path('complaint_update/<int:id>', custom_views.complaint_update, name='complaint_update'),
        path('complaint_delete/<int:dl>', custom_views.complaint_delete, name='complaint_delete'),
        path('logout_view',views.logout_view,name='logout_view'),
        path('admin_reply', admin_views.admin_reply, name='admin_reply'),
        path('give_reply/<int:id>',admin_views.reply_now,name='reply_now'),
        path('edit_reply/<int:id>',admin_views.reply_edit,name='reply_edit'),
        path('schedule_add',nurse_view.schedule_add,name='schedule_add'),
        path('schedule_view',nurse_view.schedule_view,name='schedule_view'),
        path('schedule_update/<int:id>', nurse_view.schedule_update, name='schedule_update'),
        path('schedule_delete/<int:dl>', nurse_view.schedule_delete, name='schedule_delete'),
        path('custom_schedule_view', custom_views.custom_schedule_view, name='custom_schedule_view'),
        path('book_add/<int:id>', custom_views.book_add,name='book_add'),
        path('book_view', custom_views.book_view,name='book_view'),
        path('admin_view',admin_views.appoinment_view,name='appoinment_view'),
        path('accept-appointment/<int:id>/', admin_views.accept_appointment, name='accept_appointment'),
        path('reject-appointment/<int:id>/', admin_views.reject_appointment, name='reject_appointment'),
]
