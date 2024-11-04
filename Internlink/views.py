from django.shortcuts import render,redirect
from .forms import *
from django.shortcuts import get_object_or_404

def index(request):
    teams = ['Skill Team', 'PIC', 'Academics', 'Rewards Team', 'T&P', 'R&D']
    team_counts = {team: 0 for team in teams}

 
    for team in teams:
        team_counts[team] = Intern.objects.filter(team=team).count()

   
    chart_data = {
        'labels': teams,
        'data': list(team_counts.values()),  
    }

    context = {
        'total_interns': Intern.objects.count(),
        'male_interns': Intern.objects.filter(gender='Male').count(),
        'female_interns': Intern.objects.filter(gender='Female').count(),
        'chart_data': chart_data, 
    }

    return render(request,'index.html',context)

def search(request):
    interns = Intern.objects.all()  
    return render(request, 'search.html', {'interns': interns})




def add(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES) 
        if form.is_valid():
            intern= form.save()  
            return redirect('view', intern_id=intern.intern_id)
        else:
            print(form.errors) 

    else:
        form = InternForm()
    
    return render(request, 'add.html', {'form': form}) 



def login(request):
    return render(request,'login.html')

def view_function(request,intern_id):
    intern = get_object_or_404(Intern, intern_id=intern_id)
    return render(request, 'view.html', {'intern': intern})
   

def editintern(request,intern_id):
    intern = get_object_or_404(Intern, intern_id=intern_id)
    if request.method == 'POST':
        intern_form = InternForm(request.POST, instance=intern)
        if intern_form.is_valid():
            intern_form.save()  
            return redirect('view', intern_id=intern_id)  
    else:
        intern_form = InternForm(instance=intern)  
    context= {
        "intern_form":InternForm(instance=intern)
    }
    return render(request,'editintern.html',context)

def deleteintern(request,intern_id):
    intern = get_object_or_404(Intern, intern_id=intern_id)
    intern.delete()
    return redirect('/Internlink/search')