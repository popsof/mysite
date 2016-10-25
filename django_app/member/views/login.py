from django.contrib import messages
from django.contrib.auth \
    import authenticate as auth_auth, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apis import facebook

__all__ = [
    'login',
    'login_facebook'
]

def login( request ):
    next = request.GET.get('next')

    if request.method != 'POST':
        return render( request, "member/login.html", {} )


    try:
        username = request.POST['username']
        password = request.POST['password']
    except KeyError:
        return HttpResponse( "username or password required!!!")

    user = auth_auth( username=username, password=password )

    if user is not None:
        auth_login( request, user )
        messages.success( request, '로그인에 성공하셨습니다.' )
        return redirect( next )
    else:
        messages.error( request, '로그인에 실패하셨습니다.' )
        return render(request, "member/login.html", {})


def login_facebook(request):
    if request.GET.get('error'):
        messages.error(request, '사용자가 페이스북 로그인을 취소하셨습니다.' )
        return redirect( 'login' )

    code = request.GET.get('code')
    print(code)
    redirect_uri = 'http://127.0.0.1:8000/member/login/facebook/'

    access_token = facebook.get_access_token(code, redirect_uri)
    user_id = facebook.get_user_id_from_token(access_token)
    user_info = facebook.get_user_info(user_id)

    user = auth_auth(user_info=user_info)
    if user is None:
        messages.error(request, '페이스북 로그인에 실패하였습니다.')
        return render(request, "member/login.html", {})
    else:
        auth_login(request, user)
        messages.success(request, '페이스북 로그인에 성공하였습니다.')
        return redirect( 'post_list')

    # messages.success(request, '페이스북 로그인에 성공하셨습니다. {}'.format(url_user_info))
    # return render(request, "member/login.html", {} )



