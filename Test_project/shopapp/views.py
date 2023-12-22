from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Item
from django.views.generic import CreateView, DetailView
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def main(request):
    context={
    'items': Item.objects.all(),
    }

    return render(request, 'shopapp/main.html', context=context)

class CreateItem(CreateView):
    model = Item
    fields = "name", "price", "descriptions"
    success_url = reverse_lazy("main")

class ItemDetailsView(DetailView):
    template_name='shopapp/product_details.html'
    model = Item
    context_object_name = "item"

def buy(request, id):
    item = get_object_or_404(Item, id=id)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),  # Stripe requires amount in cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(item.get_absolute_url()),
        cancel_url=request.build_absolute_uri(reverse_lazy("main")),
    )

    return JsonResponse({'sessionId': session.id})




