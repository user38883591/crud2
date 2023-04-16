from django. shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from . models import Book


def book_list(request):
    data = Book.objects.all()
    context = {"data": data}
    return render(request, 'book_list.html', context)
def Edit(request):
    return  render(request,'edit.html')
def insertData(request):
    if request.method == "POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        publication_date=request.POST.get('publication_date')
        genre=request.POST.get('genre')

        query=Book(title=title,author=author,publication_date=publication_date,genre=genre)
        query.save()
        return redirect("/")
    return render(request, 'index.html')




def updateData(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        genre = request.POST.get('genre')

        edit = Book.objects.get(id=id)
        edit.title = title
        edit.author = author
        edit.publiction_date = publication_date
        edit.genre = genre
        edit.save()
        return redirect("/")
    d = Book.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)


def deleteData(request, id):
    d = Book.objects.get(id=id)
    d.delete()
    return redirect("/")

    return render(request, "index.html")