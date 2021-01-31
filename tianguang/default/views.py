from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import Product, Category, Scroll, Config, News, Project
import datetime
from tianguang import settings
from uuid import uuid4
from qiniu import Auth, put_file, etag
import qiniu.config

# 产品相关
def add_product(request):
    response = {}
    print('request.POST', request.POST)
    try:
        category = Category.objects.get(pk=request.POST.get('category'))
        product = Product(
            name=request.POST.get('name'),
            datetime=datetime.datetime.now().isoformat(),
            image=request.POST.get('image'),
            description=request.POST.get('desc'),
            category=category,
        )
        product.save()
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def edit_product(request):
    response = {}
    pk = int(request.POST.get('pk'))
    try:
        category = Category.objects.get(pk=request.POST.get('category'))
        product = Product.objects.filter(pk=pk)
        product.update(
            name=request.POST.get('name'),
            image=request.POST.get('image'),
            description=request.POST.get('desc'),
            price=request.POST.get('price'),
            category=category,
        )
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def load_product(request):
    response = {}
    limit = int(request.GET.get('limit'))
    offset = int(request.GET.get('offset'))
    try:
        products = Product.objects.all().order_by('-pk')[offset:(offset+limit)]
        total_count = Product.objects.all().count()
        response['objects'] = json.loads(serializers.serialize("json", products))
        response['total_count'] = total_count
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def product_detail(request):
    response = {}
    pk = int(request.GET.get('pk'))
    print('pk', pk)
    try:
        products = Product.objects.filter(pk=pk)
        print('1')
        res = json.loads(serializers.serialize("json", products))[0]
        categorys = Category.objects.filter(pk=res['fields']['category'])
        category_res = json.loads(serializers.serialize("json", categorys))[0]
        res['fields']['category'] = category_res['fields']['name']
        response['object'] = res
        print('2')
        # response['object'] = dict(
        #     name=product.name
        #     datetime=product.datetime
        #     image=product.image
        #     price=product.price
        #     description=product.description
        #     category=product.category
        # )
        # print("response['object']", product.name)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_product(request):
    response = {}
    pk = int(request.GET.get('pk'))
    try:
        product = Product.objects.get(pk=pk)
        product.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def receive_image(request):
    response = {}
    image_obj = request.FILES.get('image')
    url = settings.MEDIA_ROOT
    file_name = url+"/"+str(round(datetime.datetime.now().timestamp()))+'.'+image_obj.name.split('.')[-1]
    print(111)
    print('url',url)
    with open(file_name,'wb+') as f:
        f.write(image_obj.read())
    # try:
    #     products = Product.objects.all().order_by('-pk')[offset:(offset+limit)]
    #     response['objects'] = json.loads(serializers.serialize("json", products))
    #     response['msg'] = 'success'
    #     response['error_num'] = 0
    # except  Exception as e:
    #     response['msg'] = str(e)
    #     response['error_num'] = 1
    response['msg'] = file_name
    return JsonResponse(response)

def get_all_category(request):
    response = {}
    try:
        categorys = Category.objects.all().order_by('-pk')
        response['objects'] = json.loads(serializers.serialize("json", categorys))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 分类相关
def add_category(request):
    response = {}
    print('request.POST', request.POST)
    try:
        category = Category(
            name=request.POST.get('name'),
            image=request.POST.get('image'),
        )
        category.save()
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def edit_category(request):
    response = {}
    pk = int(request.POST.get('pk'))
    try:
        category = Category.objects.filter(pk=pk)
        category.update(
            name=request.POST.get('name'),
            image=request.POST.get('image'),
        )
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def load_category(request):
    response = {}
    limit = int(request.GET.get('limit'))
    offset = int(request.GET.get('offset'))
    try:
        categorys = Category.objects.all().order_by('-pk')[offset:(offset+limit)]
        total_count = Category.objects.all().count()
        response['objects'] = json.loads(serializers.serialize("json", categorys))
        response['total_count'] = total_count
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_category(request):
    response = {}
    pk = int(request.GET.get('pk'))
    try:
        category = Category.objects.get(pk=pk)
        category.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 滚动图相关
def add_scroll(request):
    response = {}
    print('request.POST', request.POST)
    try:
        scroll = Scroll(
            image=request.POST.get('image'),
        )
        scroll.save()
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def edit_scroll(request):
    response = {}
    pk = int(request.POST.get('pk'))
    try:
        scroll = Scroll.objects.filter(pk=pk)
        scroll.update(
            image=request.POST.get('image'),
        )
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def load_scroll(request):
    response = {}
    limit = int(request.GET.get('limit'))
    offset = int(request.GET.get('offset'))
    try:
        scrolls = Scroll.objects.all().order_by('-pk')[offset:(offset+limit)]
        total_count = Scroll.objects.all().count()
        response['objects'] = json.loads(serializers.serialize("json", scrolls))
        response['total_count'] = total_count
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_scroll(request):
    response = {}
    pk = int(request.GET.get('pk'))
    print('pk', pk)
    try:
        scroll = Scroll.objects.get(pk=pk)
        scroll.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

# 配置相关
def add_config(request):
    response = {}
    print('request.POST', request.POST)
    try:
        config = Config(
            headerImage=request.POST.get('headerImage'),
            aboutUs=request.POST.get('aboutUs')
        )
        config.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def load_config(request):
    print(123)
    response = {}
    try:
        config = Config.objects.first()
        response['object'] = model_to_dict(config)
        # response['object'] = json.loads(serializers.serialize("json", config))
        response['msg'] = 'success'
        response['error_num'] = 0
        print(response)
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def edit_config(request):
    response = {}
    id = int(request.POST.get('id'))
    try:
        config = Config.objects.filter(pk=id)
        config.update(
            headerImage=request.POST.get('headerImage'),
            aboutUs=request.POST.get('aboutUs'),
        )
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 新闻相关
def add_news(request):
    response = {}
    print('request.POST', request.POST)
    try:
        news = News(
            name=request.POST.get('name'),
            datetime=datetime.datetime.now().isoformat(),
            image=request.POST.get('image'),
            description=request.POST.get('desc'),
        )
        news.save()
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def news_detail(request):
    response = {}
    pk = int(request.GET.get('pk'))
    print('pk', pk)
    try:
        news = News.objects.filter(pk=pk)
        print('1')
        res = json.loads(serializers.serialize("json", news))[0]
        response['object'] = res
        print('2')
        # response['object'] = dict(
        #     name=product.name
        #     datetime=product.datetime
        #     image=product.image
        #     price=product.price
        #     description=product.description
        #     category=product.category
        # )
        # print("response['object']", product.name)
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def edit_news(request):
    response = {}
    pk = int(request.POST.get('pk'))
    try:
        news = News.objects.filter(pk=pk)
        news.update(
            name=request.POST.get('name'),
            image=request.POST.get('image'),
            description=request.POST.get('desc'),
        )
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def load_news(request):
    response = {}
    limit = int(request.GET.get('limit'))
    offset = int(request.GET.get('offset'))
    try:
        news = News.objects.all().order_by('-pk')[offset:(offset+limit)]
        total_count = News.objects.all().count()
        response['objects'] = json.loads(serializers.serialize("json", news))
        response['total_count'] = total_count
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_news(request):
    response = {}
    pk = int(request.GET.get('pk'))
    try:
        news = News.objects.get(pk=pk)
        news.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 项目相关
def add_project(request):
    response = {}
    print('request.POST', request.POST)
    try:
        project = Project(
            name=request.POST.get('name'),
            image=request.POST.get('image'),
        )
        project.save()
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def edit_project(request):
    response = {}
    pk = int(request.POST.get('pk'))
    try:
        project = Project.objects.filter(pk=pk)
        project.update(
            name=request.POST.get('name'),
            image=request.POST.get('image'),
        )
        response['msg'] = 'success'
        response['name'] = request.POST.get('name')
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def load_project(request):
    response = {}
    limit = int(request.GET.get('limit'))
    offset = int(request.GET.get('offset'))
    try:
        project = Project.objects.all().order_by('-pk')[offset:(offset+limit)]
        total_count = Category.objects.all().count()
        response['objects'] = json.loads(serializers.serialize("json", project))
        response['total_count'] = total_count
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

def delete_project(request):
    response = {}
    pk = int(request.GET.get('pk'))
    try:
        project = Project.objects.get(pk=pk)
        project.delete()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 七牛图片处理
def upload_qiniu_image(request):
    print('step1', request)
    # image = request.POST.get('image')
    image = request.FILES.get('image', None)
    print('step2', image)
    uuid = str(uuid4())
    file_name = uuid + '.' + image.name.split('.')[-1]
    with open(file_name, 'wb+') as f:
        f.write(image.read())
    
    access_key = 'VxETw_LcNTYG8nciV9HvHAIYMMwZxssBQIt4rwKW'
    secret_key = 'CY_TZUfBU4ueQCXaB6AHv-RESeWV-W27_yCVvWDX'
    #构建鉴权对象
    q = Auth(access_key, secret_key)
    #要上传的空间
    bucket_name = 'jerry19940930'
    #上传后保存的文件名
    key = file_name
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    #要上传文件的本地路径
    localfile = file_name
    ret, info = put_file(token, key, localfile)
    domain = "http://qn22vegbe.hn-bkt.clouddn.com/"
    res = domain + ret['key']
    response = {
        'file_path': res
    }
    # response = await async_upload_file_to_qiniu(file_name, uuid + "." + image.name.split('.')[-1])
    # context.log('response', response)
    result = {
        'status': 'success',
        'response': response
    }
    # text = json.dumps(result)
    return JsonResponse(result)
