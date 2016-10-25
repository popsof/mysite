from django.shortcuts import render, get_object_or_404, HttpResponse
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list( request ):
    posts = Post.objects\
            .filter(
                Q(published_date__lte=timezone.now()) |
                Q(published_date=None)
            ).order_by('published_date')

    num_list = [ n for n in range(10) ]

    cities = [
        {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
        {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
        {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
        {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
        {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]

    context = {
        'post_list':posts,
        'title':'My Blog!!!',
        'num_list':num_list,
        'cities':cities,
    }

    return render( request, 'blog/post_list.html', context )


def post_detail( request, pk ):
#    post = Post.objects.get( pk=pk )
    post = get_object_or_404( Post, pk=pk )
    comments = post.comment_set.all().order_by('-created_date')

    context = {
        'post':post,
        'comments':comments,
    }

    return render( request, 'blog/post_detail.html', context )


from django.shortcuts import redirect

def post_new( request ):
    user = request.user
    if not user.is_authenticated():
        return HttpResponse( "로그인하세요")

    if request.method != 'POST':
        form = PostForm()
        return render( request, 'blog/post_edit.html', { 'form': form } )

    form = PostForm( request.POST )

    if form.is_valid():
        post = form.save( commit=False )
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect( post_detail, pk=post.pk )


def post_edit( request, pk ):

    post = get_object_or_404( Post, pk=pk )

    if request.method != 'POST':
        form = PostForm( instance=post )
        return render( request, 'blog/post_edit.html', { 'form':form } )

    form = PostForm( request.POST, instance=post )
    if form.is_valid():
        post = form.save( commit=False )
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect( post_detail, pk=post.pk )


    #
    # data_form_is_valid = form.is_valid()
    #
    # data_title = request.POST['title']
    # data_text = request.POST['text']
    #
    # print( data_title, data_text )
    # data_str = "title [{}] text [{}] valid {}".format(
    #             data_title, data_text, data_form_is_valid )
    #
    # return HttpResponse( data_str )

def comment_add(request, pk):
    if request.method != 'POST':
        pass

    post = get_object_or_404(Post, pk=pk)

    text = request.POST.get('text')
    post.comment_set.create(author=request.user, post=post, text=text)

    return redirect( post_detail, pk=pk )
