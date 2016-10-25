from django.shortcuts import render
from member.forms import SignupForm



def signup(request):
    if request.method != 'POST':
        return render( request, 'member/signup.html', {} )




# def signup(request):
#
#     if request.method != 'POST':
#         form = MyUserForm()
#         context = {
#             'form': form,
#         }
#         return render( request, 'member/signup.html', context )
#
#     form = MyUserForm( request.POST )
#
# # 회원가입 post 요청
#     email = request.POST['email']
#
#     if MyUser.objects.filter( email=email ).exists():
#         messages.error( request,
#                        '{}은/는 이미 사용중인 이메일 주소입니다.'.format( email ) )
#         context = {
#             'form': form,
#         }
#         return render( request, 'member/signup.html', context )
#
#     nickname = request.POST['nickname']
#     if MyUser.objects.filter( nickname=nickname ).exists():
#         messages.error( request,
#                        '{}은/는 이미 사용중인 nickname 입니다.'.format( nickname ) )
#         context = {
#             'form': form,
#         }
#         return render( request, 'member/signup.html', context )
#
#     if not form.is_valid():
#
#
#
#
#
#
#
#         newUser = form.save( commit=False )
#         newUser.set_password( newUser.password )
#         newUser.save()
#
#
#
#
#     messages.success( request, '{}님 회원가입에 성공하셨습니다.'.format( 'user' ) )
#     return redirect( 'post_list' )
