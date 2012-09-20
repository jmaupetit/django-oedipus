from django.views.generic import TemplateView
from oedipus.utils import get_pickle

class PageView(TemplateView):
    template_name = 'oedipus/page.html'

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        page_name = 'index'
        if kwargs.has_key('page_name'):
            page_name = kwargs['page_name']
        page_data = get_pickle(page_name)
        if not page_data:
            return context
        for k in ('toc', 'body', 'prev', 'next'):
            if not page_data.has_key(k):
                continue
            context[k] = page_data[k]
        return context
