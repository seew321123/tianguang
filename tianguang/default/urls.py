from django.conf.urls import url, include
from . import views
from django.urls import path

app_name='default'
urlpatterns = [
    # product
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('load_product/', views.load_product, name='load_product'),
    path('receive_image/', views.receive_image, name='receive_image'),
    path('edit_product/', views.edit_product, name='edit_product'),
    path('get_all_category/', views.get_all_category, name='get_all_category'),
    
    # category
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/', views.edit_category, name='edit_category'),
    path('load_category/', views.load_category, name='load_category'),
    path('delete_category/', views.delete_category, name='delete_category'),

    # scroll
    path('add_scroll/', views.add_scroll, name='add_scroll'),
    path('edit_scroll/', views.edit_scroll, name='edit_scroll'),
    path('load_scroll/', views.load_scroll, name='load_scroll'),
    path('delete_scroll/', views.delete_scroll, name='delete_scroll'),

    # config
    path('add_config/', views.add_config, name='add_config'),
    path('load_config/', views.load_config, name='load_config'),
    path('edit_config/', views.edit_config, name='edit_config'),

    # news
    path('add_news/', views.add_news, name='add_news'),
    path('news_detail/', views.news_detail, name='news_detail'),
    path('delete_news/', views.delete_news, name='delete_news'),
    path('load_news/', views.load_news, name='load_news'),
    path('edit_news/', views.edit_news, name='edit_news'),

    # project
    path('add_project/', views.add_project, name='add_project'),
    path('edit_project/', views.edit_project, name='edit_project'),
    path('load_project/', views.load_project, name='load_project'),
    path('delete_project/', views.delete_project, name='delete_project'),
    path('product_detail/', views.product_detail, name='product_detail'),

    # image
    path('upload_qiniu_image/', views.upload_qiniu_image, name='upload_qiniu_image'),
]