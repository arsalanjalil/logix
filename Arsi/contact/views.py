from django.http import HttpResponse
from django.shortcuts import render

from contact.forms import CommentValidaion
from contact.models import Comment


# Create your views here.


def contact(request):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        cm = Comment()
        form = CommentValidaion(request.POST)
        if form.is_valid():

            if request.user.is_authenticated:
                cm.text = request.POST['text']
                cm.email = request.POST['email']
                cm.title = request.POST['title']
                cm.phone = request.POST['phone']
                cm.user = request.user
                cm.save()

            else:
                return HttpResponse("Please do login")
        else:
            return render(request, 'contact/contact.html', {'form': form})

        return render(request, 'contact/contact.html', {'message': {'text': "از پیشنهادات شما متشکریم"}, 'cm': cm})
    else:

        return render(request, 'contact/contact.html', {'form': CommentValidaion(request.POST).errors,
                                                        'message': {'text': "لطفا خطا های زیر را برطرف کنید."}})


