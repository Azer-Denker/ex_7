from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from webapp.forms import PollForm
from webapp.models import Poll


class IndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 0


class PollView(DetailView):
    template_name = 'poll/view.html'
    context_object_name = 'poll'
    model = Poll


class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('index')
