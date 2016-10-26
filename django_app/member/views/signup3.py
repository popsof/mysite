from django.shortcuts import render, redirect
from member.forms import SignupModelForm
from django.contrib.auth import authenticate, login



def signup3(request):
    context = {}

    if request.method != 'POST':
        form = SignupModelForm()
        context['form'] = form
        return render(request, 'member/signup2.html', context)

    form = SignupModelForm(request.POST)
    # print(form.password1)
    # print(form.password2)

#    print(form.__dict__)
    if form.is_valid():
        user = form.save()

        # user = authenticate(username=user.email,
        #                     password=form.cleaned_data['password1'])
        login(request, user,
              backend='django.contrib.auth.backends.ModelBackend')
        return redirect('post_list')
    else:
        context['form'] = form
        return render(request, 'member/signup2.html', context)

