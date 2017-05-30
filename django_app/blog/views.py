from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from .forms import PostCreateForm

User = get_user_model()


# Create your views here.

def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    # return render(request,'blog/post_list.html')
    # posts변수에 ORM을 이용해서 전체 post의 리스트(쿼리셋)를 대입
    # posts = Post.objects.filter(published_date__lte=timezone.now())
    posts = Post.objects.all().order_by('-created_date')
    print(posts)

    context = {
        'title': 'PostList from post_list view',
        'posts': posts
    }

    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk):
    print("post_detail pk : ", pk)
    # post라는 키값으로 pk또는 id값이 매개변수로 주어진 pk변수와 같은 Post객체에 전달
    posts = Post.objects.get(pk=pk)
    context = {
        'post': posts

    }
    return render(request, 'blog/post_detail.html', context)


def post_create(request):
    if request.method == 'GET':  # get url에 접근했을때 요청
        form = PostCreateForm()
        context = {
            'form' : form,
        }
        return render(request, 'blog/post_create.html', context)
    elif request.method == 'POST':  # 데이터를 변경했을때의 요
        # Form클래스의 생성자에 POST데이터를 전달하여 Form인스턴스를 생성
        form = PostCreateForm(request.POST)
        # Form인스턴의 유효성을 검사하는 is_valid메서드
        if form.is_valid():
            title = form.cleaned_date['title']
            text = form.cleaned_data['text']
        # title = data['title']
        # text = data['text']
            user = User.objects.first()
            post = Post.objects.create(
            title=title,
            text=text,
            author=user,
            )
            return redirect('post_detail', pk=post.pk)
        else:
            context = {
                'form': form,
            }
            return render(request, 'blog/post_create.html', context)
