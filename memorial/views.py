from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PersonForm, MemoryForm
from .models import Person, Memory
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.views.generic import DeleteView


# Create your views here.
def index(request):
    return render(request, 'memorial/index.html')

def page(request, page):
    return render(request, 'memorial/'+page+'.html')


class PermissionMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(PermissionMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied()
        else:
            return obj

def add_person(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse('account_signup'))
   # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            person = form.save(commit=False)
            person.user = request.user
            person.save()
            return HttpResponseRedirect(reverse(view_person, args=(person.slug,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    person = Person.objects.filter(user=request.user)
    return render(request, 'memorial/add_person.html', {'form': form, 'person' : person})


def view_person(request, person):
    p = Person.objects.get(slug=person)
    memories = Memory.objects.filter(person=p)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MemoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return HttpResponseRedirect(reverse(view_person, args=(p.slug,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MemoryForm({'person' : p})

    return render(request, 'memorial/view_person.html', context={'form' : form, 'person' : p, 'memories' : memories})


class MemoryDelete(DeleteView):
    model = Memory
    
    def get_success_url(self):
    # Assuming there is a ForeignKey from Comment to Post in your model
        person = self.object.person
        return reverse( 'view_person', kwargs={'person': person.slug})