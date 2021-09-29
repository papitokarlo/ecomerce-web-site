from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from django.conf.urls import url


from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blog_view, name='home'),
    path('home', views.home, name="home"),
    url(r'^item/(?P<pk>\d+)/$', views.detail, name='detail'),
    path('mobiles', views.mobile, name="mobiles"),
    path('accessories', views.accsesories, name="accessories"),
    path('discount_page', views.discount, name= "discount_page"),
    path('search', views.search, name="search" ),
    path('contact', views.contact, name="contact"),
    path('discount/discountmobiles', views.dismob, name= "discountmobiles"),
    path('discount/discountaccessories', views.disac, name= "discountaccess"),
    path('send', views.send, name="send"),
    path('products', views.products, name="products"),
    
] 

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)