from django.shortcuts import render, redirect
from django.views.generic import View

from webapp.models import Answer, Poll, Choice


class AnswerView(View):
    template_name = 'answer/view.html'
    context_object_name = 'answers'
    model = Answer

    def get(self, request, *args, **kwargs):
        context = {}
        context['poll'] = Poll.objects.get(pk=kwargs['pk'])
        print(context)
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=kwargs['pk'])
        choice = Choice.objects.get(pk=request.POST.get('choice'))

        Answer.objects.create(poll=poll, choice=choice)
        return redirect('index')
