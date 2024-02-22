from django.views.generic import TemplateView, DetailView, FormView, ListView
from .models import Post
from .forms import PostForm
from django.contrib import messages

class HomePage(ListView):
    http_method_names=["get"]
    template_name="home.html"
    model=Post
    context_object_name="all_posts"
    queryset=Post.objects.all().order_by('-id')[0:30]



class HomePageView(TemplateView):
    template_name="home.html"

    def get_posts(self):
        all_posts=Post.objects.all().order_by('-id')
        return all_posts

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['all_posts']=self.get_posts()
        return context

class PostDetailView(DetailView):
    template_name="detail.html"
    model=Post

class AddPostView(FormView):
    template_name="new_post.html"
    form_class=PostForm
    success_url="/"

    def dispatch(self,request,*args,**kwargs):
        self.request=request
        return super().dispatch(request,*args,**kwargs)
    
    def form_valid(self, form):
        new_object=Post.objects.create(
            text=form.cleaned_data['text'],
            image=form.cleaned_data['image'],
            description=form.cleaned_data['description'],
            author = self.request.user
        )
        messages.add_message(self.request,messages.SUCCESS,"Image shared successfully...")
        return super().form_valid(form)

