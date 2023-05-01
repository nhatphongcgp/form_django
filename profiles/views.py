from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from profiles.forms import ProfileForm
from profiles.models import UserProfiles
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.


def store_files(file):
    with open("temp/image.jpg", 'wb+') as des:
        for chunk in file.chunks():
            des.write(chunk)


class CreateProfileView(CreateView):
    model = UserProfiles
    template_name = "profiles/create_profile.html"
    fields = "__all__"
    success_url = "/profiles"


class ProfilesView(ListView):
    model = UserProfiles
    template_name = "profiles/user_profiles.html"
    context_object_name = "profiles"


# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, "profiles/create_profile.html", {
#             "form": form
#         })

#     def post(self, request):
#         submited_form = ProfileForm(request.POST, request.FILES)
#         if submited_form.is_valid():
#             # store_files(request.FILES["user_image"])
#             profile = UserProfiles(image = request.FILES["user_image"])
#             profile.save()
#             return HttpResponseRedirect("/profiles")
#         return render(request, "profiles/create_profile.html", {
#             "form": submited_form
#         })
