from django.shortcuts import render, redirect
from .models import Donation, DonatedPeople, DonationAutherization, ClientMessages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from .forms import ClientMessageForm
from django.views import defaults


def index(request):
    if request.method == 'POST':
        form = ClientMessageForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index.html')


@login_required(login_url='login')
def client_message(request):
    if not request.user.is_staff:
        return defaults.permission_denied(request, PermissionDenied, template_name='error/403.html')
    else:
        context = {
            'messages': ClientMessages.objects.all()
        }
        return render(request, "client_messages.html", context=context)


@login_required(login_url='login')
def del_client_message(request, id):
    if not request.user.is_staff:
        return defaults.permission_denied(request, PermissionDenied, template_name='error/403.html')
    else:
        ClientMessages.objects.get(id=id).delete()
    return redirect('client_messages')


@login_required(login_url='login')
def donate_cards(request):
    cards = Donation.objects.all()
    total = []
    for x in cards:
        total_prize = 0
        for y in DonatedPeople.objects.filter(card=x):
            total_prize += y.amount
        total.append(total_prize)
    if request.method == 'POST':
        donation_successfull(request, request.POST.get('card_no'))
    context = {
        'cards': cards,
        'objects_list': zip(cards, total)
    }
    return render(request, 'donate_card.html', context=context)


@login_required(login_url='login')
def donation_successfull(request, pk):
    donation_card = Donation.objects.get(id=pk)
    exist_in_auther = False
    for x in DonationAutherization.objects.filter(card=donation_card):
        if str(x.user) == str(request.user.username):
            exist_in_auther = True
            people = DonationAutherization.objects.get(user=request.user, card=donation_card)
            people.amount += request.POST.get('donation_amount')
            people.save()
            messages.add_message(request, messages.INFO,
                                 'Thank You! Your Donation Will Be Listed After Admin Confirmation.')
            return redirect('donate_cards')
    if not exist_in_auther:
        DonationAutherization.objects.create(card=donation_card, user=request.user, amount=request.POST.get('donation_amount'))
        messages.add_message(request, messages.INFO,
                             'Thank You! Your Donation Will Be Listed After Admin Confirmation.')

    return redirect('donate_cards')


@login_required(login_url='login')
def donated_people_card(request, pk):
    donation_card = Donation.objects.get(id=pk)
    donated_peoples = DonatedPeople.objects.filter(card=donation_card)
    total = 0
    for x in DonatedPeople.objects.filter(card=donation_card):
        total += x.amount
    context = {
        'peoples': donated_peoples,
        'users': User.objects.all(),
        'total': total,
        'card_head': donation_card.title,
        'to_be_fetched': donation_card.money_need,
        'not_fetched': User.objects.all().count() - DonatedPeople.objects.filter(card=donation_card).count()
    }
    return render(request, 'donated_people.html', context=context)


@login_required(login_url='login')
def check_who_not_donated(donation_card):
    total = User.objects.all().count()
    people_donated = DonatedPeople.objects.filter(card=donation_card).count()
    return total - people_donated


@login_required(login_url='login')
def donation_autharization(request, pk):
    if not request.user.is_staff:
        return defaults.permission_denied(request, PermissionDenied, template_name='error/403.html')
    else:
        donation_card = Donation.objects.get(id=pk)
        cards = DonationAutherization.objects.filter(card=donation_card)
        context = {
            'cards': cards
        }
        return render(request, 'autherization.html', context)


@login_required(login_url='login')
def donation_autherized(request, pk, card_num):
    if not request.user.is_staff:
        return defaults.permission_denied(request, PermissionDenied, template_name='error/403.html')
    else:
        donation_card = Donation.objects.get(id=pk)
        donated_user = DonationAutherization.objects.get(id=card_num).user
        exist_in_auther = False
        for x in DonatedPeople.objects.filter(card=donation_card):
            if str(x.user) == str(donated_user.username):
                exist_in_auther = True
                people = DonatedPeople.objects.get(user=donated_user, card=donation_card)
                people.amount += DonationAutherization.objects.get(id=card_num, user=donated_user).amount
                people.save()
                DonationAutherization.objects.get(card=donation_card,
                                                  user=DonationAutherization.objects.get(id=card_num).user).delete()
                return redirect('donate_cards')
        if not exist_in_auther:
            DonatedPeople.objects.create(card=donation_card, user=donated_user, amount=DonationAutherization.objects.get(id=card_num, user=donated_user).amount)
        DonationAutherization.objects.get(card=donation_card,
                                          user=DonationAutherization.objects.get(id=card_num).user).delete()
        return redirect('donate_cards')


@login_required()
def donation_not_autherized(request, pk):
    DonationAutherization.objects.get(id=pk).delete()
    return redirect('donate_cards')


def contact_us(request):
    return render(request, 'contact_us.html')


# Error resource

def handler404(request, *args, **argv):
    response = render_to_response('error/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render_to_response('error/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response
