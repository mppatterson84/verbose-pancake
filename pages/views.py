from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['home_active'] = 'active'
        context['home_active_link'] = '#'
        context['home_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        context['about_active'] = 'active'
        context['about_active_link'] = '#'
        context['about_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

class PortfolioPageView(TemplateView):
    template_name = 'pages/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Portfolio'
        context['portfolio_active'] = 'active'
        context['portfolio_active_link'] = '#'
        context['portfolio_active_sr'] = '<span class="sr-only">(current)</span>'
        return context

class FrontendPageView(TemplateView):
    template_name = 'pages/frontend.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Frontend Prototypes'
        context['portfolio_active'] = 'active'
        context['portfolio_active_link'] = '#'
        context['portfolio_active_sr'] = '<span class="sr-only">(current)</span>'
        return context