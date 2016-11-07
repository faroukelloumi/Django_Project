from django.db.models import F
from models import Page
from djcelery.models import TaskMeta
from django.contrib import messages


class StatsMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        try:
            p = Page.objects.get(url=request.path)
            p.nb_visites = F('nb_visites') + 1
            p.save()
        except Page.DoesNotExist:
            Page(url=request.path).save()

    def process_response(self, request, response):
        if response.status_code == 200:
            p = Page.objects.get(url=request.path)
            response.content += bytes("Cette page a ete vue {0} fois.".format(p.nb_visites))
        return response

class CeleryMessageMiddleware(object):

    def process_request(self,request):
        if request.user.is_authenticated():
            tasks = TaskMeta.objects.filter(status = "SUCCESS")
            for task in tasks:
                task_result = "None"
                if task.result != None:
                    task_result = task.result
                messages.add_message(request, messages.INFO,u"Tache terminee :"+task_result)
                task.delete()