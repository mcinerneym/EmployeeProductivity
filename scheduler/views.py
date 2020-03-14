from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F
from .models import Employee, Shift, Note
import datetime

class IndexView(generic.ListView):
    template_name = 'scheduler/index.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.order_by('name')

class ShiftView(generic.DetailView):
    model = Employee
    template_name = 'scheduler/shift.html'
    
def addShift(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    new_shift = employee.shift_set.create(start_time = request.POST['start_time'], end_time = request.POST['end_time'], 
    date = request.POST['date'], status = request.POST['status'], reason = request.POST['reason'])
    new_shift.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    
    return HttpResponseRedirect(reverse('scheduler:shift', args=(employee.id,)))

def showShift(request, employee_id, shift_id):
    return render(request, 'scheduler/showShift.html', {
            'employee': get_object_or_404(Employee, pk=employee_id),
            'shift': get_object_or_404(Shift, pk=shift_id),
        })

def editShift(request, employee_id, shift_id):
    shift = get_object_or_404(Shift, pk=shift_id)
    if(shift.employee.id == employee_id):
        shift.start_time = request.POST['start_time']
        shift.end_time = request.POST['end_time']
        shift.date = request.POST['date']
        shift.status = request.POST['status']
        shift.reason = request.POST['reason']
        shift.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    
    return HttpResponseRedirect(reverse('scheduler:showShift', args=(employee_id, shift_id,)))

def getDayStatus(request):
    shifts = Shift.objects.all().filter(date__exact=request.GET['date']).order_by('start_time', 'end_time')
    notes = Note.objects.all().filter(date__exact=request.GET['date'])
    return render(request, 'scheduler/dayStatus.html', {
        'shifts': shifts,
        'notes': notes,
        'date': request.GET['date'],
    })

def addEmployee(request):
    new_employee = Employee(name=request.POST['name'])
    new_employee.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    
    return HttpResponseRedirect(reverse('scheduler:shift', args=(new_employee.id,)))

