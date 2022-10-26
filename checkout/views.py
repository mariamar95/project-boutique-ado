from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LwqDHKuWNP6On0qima5X8Niw4tm6zVq4oyOpZjiSv3YXXKki1OH98EA0BRI7drp5wAivIFHl5PUkVFGCKT21xQC00pw2k0OPy',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
