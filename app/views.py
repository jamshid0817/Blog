from django.shortcuts import render
from .models import ProfileDate
from .models import About,SocialLink,Tools,Service,Projects,Category,Post, PostCategory, Post
from django.core.paginator import Paginator
from django.shortcuts  import  get_object_or_404

def home(request):
    profile = ProfileDate.objects.first()
    about = About.objects.first()
    
    links = SocialLink.objects.all()
    
    
    Tool = Tools.objects.all()
    
    services= Service.objects.all()
    
    projects = Projects.objects.all()
    
    cotegorys = Category.objects.all()

    post = Post.objects.all()

    postCategory = PostCategory.objects.all()

    context = {'profile':profile,
                'about':about,
                'links': links,
                'tools':Tool,
                'services':services,
                'projects':projects,
                'cotegorys':cotegorys,
                'post': post,
                'postcotegory':postCategory}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about-us.html")

def portfolio(request):
    return render(request,"portfolio.html")

def blog(request):
    posts = Post.objects.all()
    links = SocialLink.objects.all()
    profile = ProfileDate.objects.first()

    search = request.GET.get("search")

    if search:
       posts = posts.filter(name__icontains=search)

   
    paginator = Paginator(posts, 2)
    page_number = request.GET.get("page")
    page_objs = paginator.get_page(page_number)
    #popular post list
    popular_posts = Post.objects.all()[:2]

    search = request.GET.get("search")


    return render(request,"blog.html", {"posts": page_objs,
                                         "profile": profile,
                                           "links": links,
                                             "popular_posts":popular_posts })
    

def blog_detail(request, pk):
    post=get_object_or_404(Post, id=pk)
    

    return render(request, "single-blog.html", {'post':post})