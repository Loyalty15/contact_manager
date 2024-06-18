from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import MpakaUser, MpakaContact, MpakaGroup
 
# Create your views here.
class MpakaRegisterView(CreateView):
    model = MpakaUser
    form_class = UserCreationForm
    success_url = '/Mpaka-login/'

class MpakaContactListView(ListView):
    model = MpakaContact
    context_object_name = 'contacts'

    def get_queryset(self):
        return self.request.user.mpakacontacts.all()

class MpakaContactCreateView(CreateView):
    model = MpakaContact
    fields = ['name', 'phone', 'email', 'address']
    success_url = '/Mpaka-contacts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MpakaContactUpdateView(UpdateView):
    model = MpakaContact
    fields = ['name', 'phone', 'email', 'address']
    success_url = '/Mpaka-contacts/'

class MpakaContactDeleteView(DeleteView):
    model = MpakaContact
    success_url = '/Mpaka-contacts/'

class MpakaGroupListView(ListView):
    model = MpakaGroup
    context_object_name = 'groups'

    def get_queryset(self):
        return MpakaGroup.objects.filter(Mpakacontacts__user=self.request.user).distinct()

class MpakaGroupCreateView(CreateView):
    model = MpakaGroup
    fields = ['name', 'Mpakacontacts']
    success_url = '/Mpaka-groups/'

class MpakaGroupUpdateView(UpdateView):
    model = MpakaGroup
    fields = ['name', 'Mpakacontacts']
    success_url = '/Mpaka-groups/'

class MpakaGroupDeleteView(DeleteView):
    model = MpakaGroup
    success_url = '/Mpaka-groups/'