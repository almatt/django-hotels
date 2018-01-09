import json
from functools import reduce

from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.generic import ListView,DetailView

from .decorators import ajax_required
from .models import Hotels,Advantages,Ratings


class HotelList(ListView):
    template_name = 'dashboard/index.html'
    context_object_name = 'hotels'

    def get_queryset(self):
        return Hotels.objects.order_by('id')


class HotelDetail(DetailView):
    model=Hotels
    template_name='dashboard/details.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super(HotelDetail, self).get_context_data(**kwargs)
        context["advs"] = Advantages.objects.filter(hotel=self.kwargs['pk'])
        rate_exist = Ratings.objects.filter(user=self.request.user)

        rates = Ratings.objects.filter(hotel=self.kwargs['pk'])
        rates = [x.rate for x in rates]
        if(len(rates) < 1):
            rates = 0
        else:
            rates = (reduce(lambda x,y:x+y,rates))/len(rates)
            rates = rates*100/5
        context["rate"] = int(rates)
        context["rate_exist"] = len(rate_exist)
        return context

@ajax_required
def rate(request):
    answer = {'response':'error'}
    rate_exist = Ratings.objects.filter(user=request.user)
    if(request.POST and request.POST['id'] and request.POST['rate'] and len(rate_exist) < 1):
        hotel = Hotels.objects.get(pk=request.POST['id'])
        rate = Ratings(rate=request.POST['rate'],hotel=hotel,user=request.user)
        rate.save()
        answer.update({'response': 'success'})
        return HttpResponse(json.dumps(answer), content_type="application/json")
    return HttpResponseBadRequest(json.dumps(answer))
