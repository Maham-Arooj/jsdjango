

from django.urls import path
from . import views



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
