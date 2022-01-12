from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from app1.models import Board


def index(request):
    return render(request, 'app1/index.html')


def list(request):
    print('list함수 호출됨.')
    # board에서 전체 리스트를 검색해서 가지고 온다.
    page = request.GET.get('page', 1)
    board_list = Board.objects.order_by('-id')
    print('db에서 가지고 온 data>> ' , board_list)
    # 가지고 온 데이터를 dic만들어준다.
    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)

    context = {
        'list' : page_obj
    }
    # context = {
    #     'list' : board_list
    # }
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

def insert2(request):
    data = request.POST
    print(data)
    print('게시물의 title >> ', data.get('title'))
    print('게시물의 content >> ', data.get('content'))
    print('게시물의 writer >> ', data.get('writer'))
    ### 받은 데이터로 db에 저장해야함.
    ### 객체 생성--> save()
    title = data.get('title')
    content = data.get('content')
    writer = data.get('writer')
    board = Board(title= title, content= content, writer= writer)
    board.save()
    return redirect('/app1/list')

def delete(request, id):
    print('받은 id는>> ', id)
    # id를 가지고 일단 검색해오세요.
    one = Board.objects.get(id = id)
    # 삭제하세요.
    one.delete()
    print('삭제완료 id는>> ', id)
    # 리스트로 다음페이지를 호출하게 해주세요.
    return redirect('/app1/list')

def update(request, id):
    print('받은 id는>> ', id)
    # 받은 id를 가지고 db에서 가지고 온다.
    # dic로 만든 데이터를 template에 넘겨준다.
    # id를 가지고 검색해주세요.
    one = Board.objects.get(id=id)
    # dic로 만들어주세요.
    context = {
        "one": one
    }
    # template에 넣어주세요.
    return render(request, 'app1/update.html', context)

def update2(request):
    data = request.POST
    id = data.get('id')
    title = data.get('title')
    content = data.get('content')
    writer = data.get('writer')

    #수정을 할 때는 미리 검색을 한 번 하고,
    row = Board.objects.get(id = id)
    #해당 컬럼값 변경해주고
    row.title = title
    row.content = content
    row.writer = writer

    #수정된 것 저장.
    row.save()
    return redirect('/app1/list')

def many_insert(request):
    for i in range(300):
        b = Board(title='title' + str(i),
                  content='content' + str(i),
                  writer='user' + str(i)
                  )
        b.save()
    return redirect('/app1/list')