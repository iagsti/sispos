from django.shortcuts import render, redirect, resolve_url as r
from django.http import HttpResponseRedirect, HttpResponse
from sispos.report.forms import ReportForm
from sispos.report.models  import Report, Semestre
from sispos.accounts.models import User
from django.conf import settings


def new(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    if request.method == 'POST':
        return create(request)
    form = ReportForm()
    return render(request, 'report_form.html', {'form': form})

def create(request):
    form = ReportForm(request.POST, request.FILES)
    if not form.is_valid():
        print('not valid')
    report, created = Report.objects.get_or_create(aluno=request.user)
    report.semestre_set.create(**form.cleaned_data)
    return redirect(r('report:confirmation', slug=report.uuid))

def confirmation(request, slug):
    report = Report.objects.get(uuid=slug)
    return render(request, 'report_confirmation.html', {'report': report})