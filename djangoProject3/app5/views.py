from django.shortcuts import render

# Create your views here.
def start5(request):
    print('==================== start5호출됨.')
    context = {"today" : "금요일", "when" : "2022년 1월 7일"}
    return render(request, "app5/start5.html", context)

def js01(request):
    print('=================== js01호출됨.')
    return render(request, "app5/js01.html")

def js02(request):
    print('=================== js02호출됨.')
    return render(request, "app5/js02.html")

def js03(request):
    print('=================== js03호출됨.')
    return render(request, "app5/js03.html")

def js04(request):
    print('=================== js04호출됨.')
    return render(request, "app5/js04.html")

def js05(request):
    print('=================== js05호출됨.')
    return render(request, "app5/js05.html")

def js06(request):
    print('=================== js06호출됨.')
    return render(request, "app5/js06.html")

def js07(request):
    print('=================== js07호출됨.')
    return render(request, "app5/js07.html")

def js08(request):
    print('=================== js08호출됨.')
    return render(request, "app5/js08.html")

def js09(request):
    print('=================== js09호출됨.')
    return render(request, "app5/js09.html")

def js10(request):
    print('=================== js10호출됨.')
    #db연동 결과를 검색해서 가지고 온다.
    #결과를 html에 보내주어야 한다.
    context = {'userName': 'hong',
               'field' : 'shoes',
               'email' : 'aliciawill@kakao.com',
               'contact' : '010-4904-2996',
               'payValue' : 5000
               }
    return render(request, "app5/js10.html", context)

def js100(request):
    print('=================== js100호출됨.')
    #db연동 결과를 검색해서 가지고 온다.
    #결과를 html에 보내주어야 한다.
    context = {'site': [100, 200, 300],
               'url' : {'u1': 'naver', 'u2': 'daum', 'u3': 'google'},
               'name' : ['hong', 'kim', 'apple'],
               }
    return render(request, "app5/js100.html", context)

def map1(request):
    print('=================== map1호출됨.')
    # 3장소의 위도 경도를 만들어서, html에 표시 
    return render(request, "app5/map1.html")

def map2(request):
    print('=================== map2호출됨.')
    # 37.51725181697697, 126.90373968262504
    return render(request, "app5/map2.html")