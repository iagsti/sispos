from django.shortcuts import render, redirect, resolve_url as r
from sispos.report.forms import ReportForm, ParecerOrientadorMestradoForm
from sispos.report.models import Report, ParecerOrientadorMestrado
from django.conf import settings
from django.forms.models import model_to_dict


def report_list(request):
    report_list = Report.objects.all()
    context = {'report_list': report_list}
    return render(request, 'report_list.html', context)


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


def parecer_form(request, slug):
    report_dict = dict(report=slug)
    form = ParecerOrientadorMestradoForm(report_dict)
    report = Report.objects.get(uuid=slug)
    if hasattr(report, 'parecerorientadormestrado'):
        parecer = report.parecerorientadormestrado
        parecer_dict = model_to_dict(parecer)
        data = dict(parecer_dict, **report_dict)
        form = ParecerOrientadorMestradoForm(data)
    return render(request, 'parecer_orientador_mestrado.html', {'form': form})


def create_parecer_orientador_mestrado(request):
    form = ParecerOrientadorMestradoForm(request.POST)
    if form.is_valid():
        report = Report.objects.get(uuid=form.cleaned_data['report'])
        form.cleaned_data['report'] = report
        data = form.cleaned_data
        parecer_data = dict(s1_desempenho=data['s1_desempenho'], s1_projeto=data['s1_projeto'],
                            s1_outras_atividades=data['s1_outras_atividades'], report=data['report'])
        parecer, created = ParecerOrientadorMestrado.objects.get_or_create(**parecer_data)
        ParecerOrientadorMestrado.objects.update(**form.cleaned_data)
    to = report.get_absolute_url() + '/parecer-orientador-mestrado'
    return redirect(to=to)


def confirmation(request, slug):
    report = Report.objects.get(uuid=slug)
    return render(request, 'report_confirmation.html', {'report': report})