from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    # return render(request,'blog/post_list.html')
    # posts변수에 ORM을 이용해서 전체 post의 리스트(쿼리셋)를 대입
    posts = Post.objects.filter(published_date__lte=timezone.now())
    print(posts)

    context = {
        'title' : 'PostList from post_list view',
        'posts' : posts
    }

    return render(request,'blog/post_list.html',context=context)
