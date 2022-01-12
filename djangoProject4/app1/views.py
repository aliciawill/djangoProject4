from django.shortcuts import render

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

def one(request):
    pass

def insert(request):
    pass

def delete(request):
    pass

def update(request):
    pass

def update2(request):
    pass