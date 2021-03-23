from django.shortcuts import render, redirect
from .models import Show

def index(request):
    context = {
        "db_show": Show.objects.all()
    }
    return render(request,'index.html',context)
def add_show(request):
    show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect(f"/results/{show.id}")
def display_result(request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id),
        "db_show" : Show.objects.all()
    }
    return render(request, "results.html", context)
def display_all_shows(request):
    context = {
        "db_show" : Show.objects.all()
    }
    return render(request, "all_shows.html", context)
def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect("/all_shows_page")
def edit_page(request, show_id):
    context = {
        "show" : Show.objects.get(id=show_id),
    }
    return render(request, "edit.html", context)
def update(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.description = request.POST['description']
    show.save()
    return redirect(f"/results/{show.id}")
    



