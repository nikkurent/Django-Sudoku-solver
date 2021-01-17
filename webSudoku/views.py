from django.shortcuts import render, redirect
from .solver import solve, print_board

# Create your views here.
def home_view(request, *args, **kwargs):
    
    board= []
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    row8 = []
    row9 = []
    if request.method =='POST':
        # Create row 1
        for i in range(1, 10):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row1.append(num)
        board.append(row1)

        # Create row 2
        for i in range(10, 19):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row2.append(num)
        board.append(row2)

        # Create row 3
        for i in range(19, 28):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row3.append(num)
        board.append(row3)

        # Create row 4
        for i in range(28, 37):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row4.append(num)
        board.append(row4)

        # Create row 5
        for i in range(37, 46):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row5.append(num)
        board.append(row5)

        # Create row 6
        for i in range(46, 55):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row6.append(num)
        board.append(row6)

        # Create row 7
        for i in range(55, 64):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row7.append(num)
        board.append(row7)

        # Create row 8
        for i in range(64, 73):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row8.append(num)
        board.append(row8)

        # Create row 9
        for i in range(73, 82):
            num = request.POST[f'num{i}']
            if num == '':
                num = 0
            num = int(num)
            row9.append(num)
        board.append(row9)

    # solve function from solve.py    
    solve(board)
    if board:
        context={
            'board': board
        }
        return render(request, 'templates/solved.html', context)
    return render(request, 'templates/index.html')