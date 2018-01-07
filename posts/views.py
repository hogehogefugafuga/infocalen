from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.


def index(request):
    # render 外部のhtmlファイルを読みに行く
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {"posts": posts})


# 詳細の表示
def post_detail(request, post_id):
    # post_idのインデックスのpostを持ってくる
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'posts/post_detail.html', {'post': post})


# 商品の検索をする
def post_search(request, search_str):
    # post_idのインデックスのpostを持ってくる
    # post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_search.html', {'search_str': search_str})

