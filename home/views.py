from django.shortcuts import render

#home views
# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def user_login(request):
    return render(request, 'register/signin.html')

def user_register(request):
    return render(request, 'register/signup.html')

def teamrankings(request):
    return render(request, 'home/team_rank.html')

def menrankings(request):
    return render(request, 'home/mens_ranking.html')

def womenrankings(request):
    return render(request, 'home/team_rankwo.html')
