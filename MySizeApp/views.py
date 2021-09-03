from django.shortcuts import render,redirect
from .models import Clothes, Size
from django.views.generic import  UpdateView

# Create your views here.
def home(request):
   return render(request, 'home.html', {})

def mypage(request):
    length1 = Clothes.objects.get(name="My size")
    length = length1.size.all()
    return render(request, 'mypage.html', {'length':length})

def editMypage(request, editsize_pk):
    editSize1 = Clothes.objects.get(name="My size")
    editSize = editSize1.size.get(pk=editsize_pk)
    if request.method =='POST':
        editSize.size1 = request.POST.get('size1')
        editSize.size2 = request.POST.get('size2')
        editSize.size3 = request.POST.get('size3')
        editSize.size4 = request.POST.get('size4')
        editSize.save()
        # editSize.objects.get(pk=editsize_pk).update(
        #     size1 = request.POST['size1'],
        #     size2 = request.POST['size2'],
        #     size3 = request.POST['size3'],
        #     size4 = request.POST['size4'],
          
        # )
        return redirect('mypage')
    return render(request, 'editMypage.html',{'editSize': editSize})

    

def topView(request):
    clothes = Clothes.objects.all()
    tops = clothes.filter(category = "상의").exclude(name="My size")

    return render(request, 'top.html', {'tops':tops})

def compareView(request, id):
    target1 = Clothes.objects.get(id=id)
    target =target1.size.all()
    num =target1.size.all().count()
    mySize1 = Clothes.objects.get(name="My size")
    mySize = mySize1.size.all()
    
    targetArr = []
    myArr=[]
    totalArr= []
    for i in range(num):
        targetArr.append(target[i].size1)
        targetArr.append(target[i].size2)
        targetArr.append(target[i].size3)
        targetArr.append(target[i].size4)
 
    myArr.append(mySize[0].size1)
    myArr.append(mySize[0].size2)
    myArr.append(mySize[0].size3)
    myArr.append(mySize[0].size4)

    num2 =len(targetArr)
    for i in range(num2):
        if(i<4):
             totalArr.append(float(targetArr[i])-float(myArr[i]))
        elif(i>=24):
            totalArr.append(float(targetArr[i])-float(myArr[i-24]))
        elif(i>=20):
            totalArr.append(float(targetArr[i])-float(myArr[i-20]))
        elif(i>=16):
            totalArr.append(float(targetArr[i])-float(myArr[i-16]))
        elif(i>=12):
            totalArr.append(float(targetArr[i])-float(myArr[i-12]))
        elif(i>=8):
            totalArr.append(float(targetArr[i])-float(myArr[i-8]))
        elif(i>=4):
            totalArr.append(float(targetArr[i])-float(myArr[i-4]))
    

        

    # num =target1.size.all().count()
    # for i in range(num):
    #     for j in range(4):
    #         totalArr.append(float(targetArr[j])-float(myArr[j]))


    return render(request, 'compare.html', { 'myArr':myArr,'totalArr':totalArr, 'targetArr':targetArr, 'target':target, 'num':num,'num2':num2})

# def compareView(request, id):
#     target1 = Clothes.objects.get(id=id)
#     target =target1.size.all()
#     mySize1 = Clothes.objects.get(name="My size")
#     mySize = mySize1.size.all()
    
    


#     return render(request, 'compare.html', { 'target':target})