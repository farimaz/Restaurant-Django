from django.shortcuts import render,get_object_or_404
from .models import Blog,Tag,Category,Comments
from .forms import CommentForms
from django.core.paginator import Paginator 

def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,2)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)

    context={'blog_list':blog_list}
    return render(request,'blog/blog.html',context)

def blog_detail(request,id):
    blog = get_object_or_404(Blog,id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    category = Category.objects.all()
    recent = Blog.objects.order_by('-created_at')[:4]
    comments = Comments.objects.all().filter(blog=blog)
    if request.method == "POST":
        form = CommentForms(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_massage = form.cleaned_data["massage"]

            new_comment= Comments(blog=blog,name=new_name,email=new_email,massage=new_massage)
            new_comment.save()

    context = {'blog': blog,'tags':tags,'category':category,'recent':recent, 'comments':comments}
    return render(request,'blog/blog-details.html',context)

def blog_tag(request,tag):
    blogs = Blog.objects.filter(tags__slug=tag)
    context={'blogs':blogs}
    return render(request,'blog/blog.html',context)

def blog_category(request,category):
    blogs = Blog.objects.filter(Category__slug=category)
    context={'blogs':blogs}
    return render(request,'blog/blog.html',context)

def search(request):
    if request.method == 'GET':
        q = request.GET.get('search')
    blog = Blog.objects.filter(title__icontains=q)
    paginator = Paginator(blog,2)
    page_number = request.GET.get('page')
    blog_list = paginator.get_page(page_number)

    return render(request,'blog/blog.html',{'blog_list':blog_list})
    
