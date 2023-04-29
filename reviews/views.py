from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, CreateView
from .forms import ReviewForm
from .models import Review
from django.views import View


# Create your views here.

class ReviewView(CreateView):
    model = Review
    template_name = "reviews/review.html"
    form_class = ReviewForm
    success_url = "/thank-you"


# class ReviewView(FormView):
#     template_name = "reviews/review.html"
#     form_class = ReviewForm
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewView(View):
#     def get(self, request):
#         form = forms.ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#     def post(self, request):
#         form = forms.ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")
#         return render(request, "reviews/review.html", {
#             "form": form
#         })


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
        form = ReviewForm(request.POST)
        # Wanna update existing data?
        # existing_model = Review.objects.all().get(pk=1)
        # form = forms.ReviewForm(request.POST,instance=existing_model)
        if form.is_valid():
            # review = Review(user_name = form.cleaned_data["user_name"], review_text = form.cleaned_data["review_text"],rating = form.cleaned_data["rating"],)
            # review.save()
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form
    })


# class ThankYouView(View):
#     def get(self, request):
#         return render(request, "feedback/thank_you.html")

class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works !"
        return context


# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context
class ReviewListView(ListView):
    model = Review
    template_name = "reviews/review_list.html"
    # defaut context_object_name = "object_list"
    context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=2)
    #     return data


# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         context["review"] = selected_review
#         return context
class SingleReviewView(DetailView):
    model = Review
    template_name = "reviews/single_review.html"
    # defaut object_name = "object"
