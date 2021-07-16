

from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    
    path('productimg/',views.home, name= 'index1'),
    path('',views.home, name= 'index1'),
    path('about/',views.about , name= 'about'),
    path('services/',views.services , name= 'typography'),
    
    path('single/',views.single , name= 'single'),
    path('contact/',views.contact , name= 'contact'),
    path('blog/',views.blog , name= 'index1'),
    path('shop/',views.shop , name= 'shop'),
    path('login/',views.loginPage , name= 'login'),
    path('logout/',views.logoutUser , name= 'logout'),
    path('reg_form/',views.registerPage , name= 'reg_form'),

    path('oauth/', include('social_django.urls', namespace='social')), 
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"), name="reset_password"),
    path('reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), name="password_reset_complete"),


    path('indeximg/',views.image_get , name= 'index1'),
    #path('blogimg/',views.image_get , name= 'blog1'),
    path('about1/',views.image , name= 'about1'),
    path('customer/',views.customer,name='Customer'),  
    path('customers/',views.savecustomer,name='customer'),
    path('edit/<str:pk>/',views.edit_data,name='edit'), 
    #path('delete/<str:id>/',views.del_customer,name='delete'), 
    # path('single/',views.single , name= 'single'),
    #path('update_customers/<str:pk>/',views.updatecustomers,name='updatecustomers'),
         
    
]
