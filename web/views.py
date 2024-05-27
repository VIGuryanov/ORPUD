from django.shortcuts import render, redirect
import datetime

from web.models import SomeObject
from web.forms import ObjectForm

# Create your views here.
def main_view(request):
    db_count = SomeObject.objects.count()
    db_highter_id = SomeObject.objects.order_by('id').last().id
    return render(request, "web/default.html", {
        "db_count": db_count,
        "db_highter_id": db_highter_id
    })

def obj_list(request):
    return render(request, "web/objlist.html", {
        "objects": SomeObject.objects.all()}
        )

def obj_single(request, id):
    return render(request, "web/objsingle.html", {
        "object": SomeObject.objects.get(id = id)}
        )

def obj_create(request):
    form = ObjectForm()
    if request.method == 'POST':
        form = ObjectForm(data=request.POST)
        if form.is_valid:
            SomeObject.objects.create(Data=form.data['data'], Created=datetime.datetime.now())
            return render(request, "web/objcreatesucc.html")
    return render(request, "web/objcreate.html", {
        "form": form}
        )

def obj_delete(request, id):
    SomeObject.objects.filter(id = id).delete()
    return redirect('../../object')

def obj_modify(request, id):
    form = ObjectForm()
    if request.method == 'POST':
        form = ObjectForm(data=request.POST)
        if form.is_valid:
            SomeObject.objects.filter(id = id).update(Data=form.data['data'], Modified=datetime.datetime.now())
            return redirect('../../object')
    return render(request, "web/objmodify.html", {
        "form": form}
        )

def obj_statistic(request, id):
    obj = SomeObject.objects.get(id = id)
    return render(request, "web/objstatistic.html", {
    "created": obj.Created,
    "modified": obj.Modified}
    )