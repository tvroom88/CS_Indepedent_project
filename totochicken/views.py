from django.shortcuts import render, redirect


# ------------------------------
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
# -------------------------------

# ------------------------------
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# ------------------------------

# Create your views here.
def toto_restaurant_home_view(request):

    return render(request, 'toto_home.html')

def toto_menu_view(request):

    return render(request, 'toto_menu.html')


# def toto_contact_view(request):
#
#     return render(request, 'toto_contact.html')


# new imports that go at the top of the file


# our view
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name  = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content  = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            try:
                send_mail(contact_name, form_content,contact_email, ['tvroom9102@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')



            # email = EmailMessage(
            #     "New contact form submission",
            #     content,
            #     "Your website" + '',
            #     ['tvroom9102@gmail.com'],
            #     headers = {'Reply-To': contact_email }
            # )
            # email.send()
            return redirect('contact')

    return render(request, 'toto_contact.html', {
        'form': form_class,
    })