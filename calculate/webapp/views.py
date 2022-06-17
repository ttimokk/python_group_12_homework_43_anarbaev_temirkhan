from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')


def calculate_page(request):
    if request.method == 'GET':
        return render(request, 'calculate_page.html')
    else:
        act_nums = {
            'first_num': request.POST.get('first_num'),
            'second_num': request.POST.get('second_num'),
            'add': request.POST.get('add'),
            'subtract': request.POST.get('subtract'),
            'multiply': request.POST.get('multiply'),
            'divide': request.POST.get('divide'),
        }
        print(request.POST)
        if request.POST.get('add'):
            add = int(act_nums['first_num']) + int(act_nums['second_num'])
            act_nums['add'] = add
            return render(request, 'add.html', act_nums)
        elif request.POST.get('subtract'):
            subtract = int(act_nums['first_num']) - int(act_nums['second_num'])
            act_nums['subtract'] = subtract
            return render(request, 'subtract.html', act_nums)
        elif request.POST.get('multiply'):
            multiply = int(act_nums['first_num']) * int(act_nums['second_num'])
            act_nums['multiply'] = multiply
            return render(request, 'multiply.html', act_nums)
        elif request.POST.get('divide'):
            divide = int(act_nums['first_num']) // int(act_nums['second_num'])
            act_nums['divide'] = divide
            return render(request, 'divide.html', act_nums)
