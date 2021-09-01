from contact.models import ContactSubmission
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

# Create your views here.

def contact_submission_view(request, *args, **kwargs):
    if request.method == 'POST':
        form_data = request.POST
        submission = ContactSubmission.objects.create(
            subject = form_data['subject'],
            message = form_data['message']
        )
        if request.user.is_authenticated:
            user = request.user
            submission.user = user
            submission.name = user.username
            submission.email = user.email
            submission.save()
        else:
            submission.name = form_data['name']
            submission.email = form_data['email']
            submission.save()
            
        return redirect('/')

    context = {
        'title': 'Contact Us'
    }
    return render(request, 'contact/contact.html', context)