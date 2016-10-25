from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from member.forms import SignupForm

from member.models import MyUser


def signup2(request):
    context = {}

    if request.method != 'POST':
        form = SignupForm()
        context['form'] = form
        return render( request, 'member/signup2.html', context )

    form = SignupForm( request.POST )
    if not form.is_valid():
        context['form'] = form
        return render( request, 'member/signup2.html', context)

    email = form.cleaned_data['email']
    password1 = form.cleaned_data['password1']
    password2 = form.cleaned_data['password2']
    last_name = form.cleaned_data['last_name']
    first_name = form.cleaned_data['first_name']
    nickname = form.cleaned_data['nickname']

    if password1 != password2:
        return HttpResponse( "패스워드가 다릅니다." )
    user = MyUser.objects.create_user(
        email=email,
        last_name=last_name,
        first_name=first_name,
        nickName=nickname,
        password=password1,
    )

    login( request, user )
#    messages.info( request, "회원가입 성공")
    return redirect( 'post_list' )

