from app1.models import Board

for i in range(300):
    b = Board(title = 'title' + str(i),
              content= 'content' + str(i),
              writer= 'user' + str(i)
              )
    b.save()