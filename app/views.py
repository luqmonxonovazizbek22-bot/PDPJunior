from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from app.form import ContactForm
from app.models import Mentor


class IndexView(TemplateView):
    template_name = 'index.html'




class CourseView(TemplateView):
    template_name = 'courses.html'

class MentorView(TemplateView):
    template_name = 'mentors.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mentors'] = Mentor.objects.all()
        return context

class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

class TeamView(TemplateView):
    template_name = 'team.html'


class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)