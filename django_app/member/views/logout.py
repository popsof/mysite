from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

def logout( request ):
    auth_logout( request )
    messages.info( request, '로그아웃 되었습니다.')
    return redirect( 'post_list' )
