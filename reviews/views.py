from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms
from .models import Review
from django.views import View

# Create your views here.


class ReviewView(View):
    def get(self, request):
        form = forms.ReviewForm()
        return render(request, "feedback/review.html", {
            "form": form
        })

    def post(self, request):
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "feedback/review.html", {
            "form": form
        })


def review(request):
    # if request.method == 'POST':
    #     entered_username = request.POST["username"]
    #     if entered_username == "":
    #         return render(request, "feedback/review.html", {
    #             "has_error": True
    #         })
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
    # return render(request, "feedback/review.html", {
    #     "has_error": False
    # })
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        # Wanna update existing data?
        # existing_model = Review.objects.all().get(pk=1)
        # form = forms.ReviewForm(request.POST,instance=existing_model)
        if form.is_valid():
            # review = Review(user_name = form.cleaned_data["user_name"], review_text = form.cleaned_data["review_text"],rating = form.cleaned_data["rating"],)
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = forms.ReviewForm()
    return render(request, "feedback/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "feedback/thank_you.html")
