from django.shortcuts import get_object_or_404, render
from posts.models import Post

# Create your views here.


def index(request):
    latest_question_list = Post.objects.all()[:5]

    return render(request, "posts/index.html", {"latest_question_list": latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Post, pk=question_id)
    return render(request, "posts/detail.html", {"question": question})
