from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceIndexView(ListView):
    template_name = 'choice/index.html'
    context_object_name = 'choices'
    model = Choice
    paginate_by = 5
    paginate_orphans = 0


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choice/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        poll.save()
        form.save_m2m()
        return redirect('poll_view', poll.pk)

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'
    context_object_name = 'choice'
    success_url = reverse_lazy('index')
