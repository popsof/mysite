from django.shortcuts import render, redirect
from member.forms import SignupModelForm
from django.contrib.auth import login


def signup3(request):
    context = {}

    if request.method != 'POST':
        form = SignupModelForm()
        context['form'] = form
        return render( request, 'member/signup2.html', context )

    form = SignupModelForm( request.POST )
    if form.is_valid():
        user = form.save()

        login( request, user )
        return redirect( 'post_list' )
    else:
        context['form'] = form
        return render(request, 'member/signup2.html', context)

