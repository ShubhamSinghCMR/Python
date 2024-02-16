from django.shortcuts import redirect

# Create your views here.
def call_home(request):
	return redirect('blog-home')
	