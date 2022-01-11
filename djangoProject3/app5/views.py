from django.http import HttpResponse, JsonResponse
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
    location = """
    lats = [ 37.5705805429368, 37.560260, 37.689447 ]
    lngs = [ 126.99212654046664, 126.942149, 127.046558 ]
    """
    context = {'location' : location }
    return render(request, "app5/map1.html", context)

def map2(request):
    print('=================== map2호출됨.')
    # 37.51725181697697, 126.90373968262504
    return render(request, "app5/map2.html")

def ajax0(request):
    print('=================== ajax0호출됨.')
    return render(request, "app5/ajax0.html")

def ajax1(request):
    print('=================== ajax1호출됨.')
    return render(request, "app5/ajax1.html")

def target0(request):
    print('=================== target0호출됨.')
    context = {'result' : 100, 'sum' : 1000}
    return render(request, "app5/target0.html", context)

def target00(request):
    print('=================== target00호출됨.')
    context = {'today': -10, 'today2': 'bad'}
    return render(request, "app5/target00.html", context)

def target(request):
    print('=================== target호출됨.')
    context = {'result' : 100, 'age' : 100, 'tel' : [100, 200, 300]}
    # return render(request, "app5/target.html", context)
    # return HttpResponse(context)
    return JsonResponse(context)

def ajax2(request):
    print('=================== ajax2호출됨.')
    return render(request, "app5/ajax2_.html")

def target2(request):
    print('=================== target2호출됨.')
    context = {"lat" : 37.570580, "lng" : 126.99212654}
    return JsonResponse(context)

def target3(request):
    print('=================== target3호출됨.')
    context = {"lat" : 37.5642135, "lng" : 127.0016985}
    return JsonResponse(context)