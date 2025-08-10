from django.shortcuts import render

#user views
# Create your views here.
def user_logout(request):
    return render(request, 'home/index.html')

def user_profile(request):
    return render(request, 'user/profile.html')

def user_matches(request):
    return render(request, 'user/matches.html')

# Create your views here.


def user_editprof(request):
    return render(request, 'user/editprof.html')

def rankings(request):
    return render(request, 'user/team_rank.html')


