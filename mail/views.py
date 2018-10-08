from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic.list import ListView

from .models import mails
from .forms import MailFrom


class IndexView(View):

    def get(self,request):
        return render(request, 'mail/index.html')


class ListView(ListView):
    model = mails

    def get_context_data(self):
        context = super().get_context_data()
        return context


class AddView(View):

    def get(self, request):

        form = MailFrom
        return render(request, 'mail/add.html', {'form': form})

    def post(self, request):

        form = MailFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'List Added')
            return redirect('list')

        return render(request, 'mail/add.html', {'form': form})
