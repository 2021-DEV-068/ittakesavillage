from django.views.generic import TemplateView

from website.filters.parent.caregiver import CaregiverFilter


class HomeView(TemplateView):
    template_name = "website/parent/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CaregiverFilter().form
        return context

    def categoriesFilter(event):
            #event['some_data_from_page']
            print(event)
            #return http.HttpRespones("Some response from server")
