from django.shortcuts import render, redirect

# Create your views here.
from app1.models import Board


def index(request):
    return render(request, 'app1/index.html')

def list(request):
    print('list함수 호출됨.')
    # board에서 전체 리스트를 검색해서 가지고 온다.
    board_list = Board.objects.order_by('-id')
    print('db에서 가지고 온 data>> ' , board_list)
    # 가지고 온 데이터를 dic만들어준다.
    context = {
        'list' : board_list
    }
    # 데이터를 넣어서 보내줄 template지정, 데이터를 넘겨줌.
    return render(request, 'app1/list.html', context)

def one(request, id):
    print('받은 id는>> ', id)
    # id를 가지고 검색해주세요.
    one = Board.objects.get(id = id)
    # dic로 만들어주세요.
    context = {
        "one" : one
    }
    # template에 넣어주세요.
    return render(request, 'app1/one.html', context)

def insert(request):
    return render(request, 'app1/insert.html')

def delete(request, id):
    print('받은 id는>> ', id)
    # id를 가지고 일단 검색해오세요.
    one = Board.objects.get(id = id)
    # 삭제하세요.
    one.delete()
    print('삭제완료 id는>> ', id)
    # 리스트로 다음페이지를 호출하게 해주세요.
    return redirect('/app1/list')

def update(request):
    pass

def update2(request):
    pass