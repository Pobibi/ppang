from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Panguser
from .models import Panglist
from .models import Pangstore
from django.contrib.auth.hashers import check_password

# Create your views here.

#페이지 연결
def like(request):
    return render(request,'paro/paro_user_like.html')

#로그인
def login(request):
    if request.method=="GET":
        return render(request,'pang/paro_login.html')
    elif request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        #유효성 처리
        res_data={}
        if not (username and password):
            res_data['error']="아이디와 비밀번호 모두 입력해주세요"
        else:
            #기존DB에 있는 panguser 모델과 같은 값을 가져온다
            panguser=Panguser.objects.get(usernum=username)

            #비밀번호가 맞는지 확인한다.
            if check_password(password,panguser.pw):
                #응답 데이터 세션에 값 추가. 수신측 쿠키에 저장됨
                request.seesion['user']=panguser.usernum

                #리다이렉트
                return redirect('/')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다"
        return render(request,'pang/paro_login.html',res_data) #응답 데이터 res_data 전달


#빵 리스트 보여주기
def pang(request):
    panglists=Panglist.objects.all() # 빵 리스트 가져오기
    context={'panglists':panglists}  
    return render(request,'pang/paro_main.html',context)

