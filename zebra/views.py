from django.http import Http404
from django.shortcuts import render

from . import labels

# Create your views here.


def index(request):
    return render(request, "index.html", {"sample_names": labels.zpl_samples.keys()})


def print_concise(request, label_type):
    try:
        context = {"label_data": labels.zpl_samples[label_type]}
    except KeyError:
        raise Http404(f"No sample label data for '{label_type}' exists")
    return render(request, "print/label_concise.html", context)


def print_verbose(request, label_type):
    try:
        context = {
            "label_data": labels.zpl_samples[label_type],
            "config_label_data": labels.zpl_samples["config"],
            "label_type": label_type,
        }
    except KeyError:
        raise Http404(f"No sample label data for '{label_type}' exists")
    return render(request, "print/label_verbose.html", context)


def edc(request):
    return render(
        request,
        "edc/index.html",
        # Append '_label_data' onto each key to match target template
        dict((f"{k}_label_data", v) for k, v in labels.zpl_samples.items()),
    )


def sample(request):
    return render(request, "sample/index.html")
