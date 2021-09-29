from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Item, ItemImage
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request):
    posts = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts':posts})


def detail(request, pk):
    post = get_object_or_404(Item, pk=pk)
    photos = ItemImage.objects.filter(post=post)
    pos = Item.objects.filter(pk=pk)
    releated = Item.objects.all()
    

    return render(request, 'detail.html', {
        'post':post,
        'photos':photos,
        'pos':pos,
        'releated' : releated,
       
    })  
  

def mobile(request):
    list = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 18)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'mobiles.html', {'posts' : posts}) 
        
def accsesories(request):
    list = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 18)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'accessories.html', {'posts' : posts}) 

def discount(request):
    list = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 18)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'discount.html', {'posts' : posts})

def search(request):
    if request.method =="POST":
      search = request.POST['search']
      posts = Item.objects.filter(title__contains=search)

      return render(request, 'search.html', {'search':search, "posts":posts}) 
    else:
        return render(request, 'search.html',  {}) 

def home(request):
    list = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 18)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'posts':posts})

def contact(request):
    
    return render(request, 'contact.html')


def disac(request):
    list = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 18)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'discountaccess.html', {'posts':posts})


def dismob(request):
    list = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 18)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'discountmobile.html', {'posts':posts})

  
def products(request):
    list = Item.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    paginator = Paginator(list, 18)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {'posts':posts})

def send(request):
    if request.method == "POST":
        name= request.POST.get('Name')
        email=request.POST.get('Email')
        phone=request.POST.get('Phone')
        text= request.POST.get('Text')
    
        data = {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'text'  : text
        }
    
        print(f'dsd da es ki kaia kacio {data}')
        
        alert="შეტყობინება წარმატებით გაიგზავნა, უახლოეს პერიოდში დაგიკავშირდბით, მადლობთ თქვენი აზრი ჩვენთვის მნიშვნელოვანია."

        message = '''
        New message: {}

        from: {}
        '''.format(data['text'],  data['phone'])
        send_mail(data['name'], message, '', ['zurabi.begadze563@ens.tsu.edu.ge' ])
        return render(request, 'index.html', {'alert':alert})
        
    else :
        return HttpResponse('შეტყობინება ვერ გაიგზავნა')
    
    