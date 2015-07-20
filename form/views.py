from django.views.generic.edit import CreateView, DeleteView
from django.views import generic
from form.models import FarmDescription
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from form import instantiate
from form.forms import NewFarmForm
from django.core.urlresolvers import reverse_lazy


class CreateFarmView(CreateView):
    model = FarmDescription
    form_class = NewFarmForm
    def form_valid(self, form):
        farm = form.save(commit=False)
        #farm.owner = User.objects.get(username=self.request.user)
        farm.owner = self.request.user.username
        farm.save()
        return super(CreateFarmView, self).form_valid(form)

class DeleteFarmView(DeleteView):
    model = FarmDescription
    success_url = reverse_lazy('list_farm')
    template_name_suffix = '_confirm_delete'
    context_object_name = 'delete_farm'

class DisplayFarmView(generic.DetailView):
   model = FarmDescription
   context_object_name = 'farm_description'

   def get_queryset(self):
      return FarmDescription.objects


class ListFarmView(generic.ListView):
   context_object_name = 'farm_list'
   def get_queryset(self):
      """Return the list of farms belonging to the user."""
      #return FarmDescription.objects.all()
      return FarmDescription.objects.filter(owner=self.request.user.username)



def instantiate_view(request, pk):
    template = loader.get_template('form/instantiate.html')
    if request.method == 'POST':
        farm = FarmDescription.objects.get(id=pk)
        access=farm.ec2_access_key
        secret=farm.ec2_secret_key
        flavour=farm.master_flavour
        image=farm.master_image
        #retval=instantiate.main(access, secret, flavour,image)
        retval=instantiate.main(farm)
        context = RequestContext(request, { 'retval': retval,})
        return HttpResponse(template.render(context))

    else:
        return HttpResponse(status=400) # bad request

