from django.shortcuts import render


def index_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        fnumber = int(request.POST.get('fnumber'))
        snumber = int(request.POST.get('snumber'))
        select = request.POST.get('select')
        sim = res_view(fnumber, snumber, select)
        # print(sim)
        res = f'{fnumber} {sim[1]} {snumber} = {sim[0]}'
        # print(res)
        return render(request, 'index.html', {'res': res})


def res_view(fnumber, snumber, select):
    if select == 'add':
        return fnumber + snumber, '+'
    elif select == 'subtract':
        return fnumber - snumber, '-'
    elif select == 'multiple':
        return fnumber * snumber, '*'
    elif select == 'divide':
        return fnumber / snumber, '/'

# Create your views here.
