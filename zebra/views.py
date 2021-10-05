from django.shortcuts import render

from . import labels

# Create your views here.


def index(request):
    return render(request, "index.html")


def edc(request):

    context = {
        # EDC test labels
        "requisition_label_data": labels.get_requisition_sample(),
        "aliquot_label_data": labels.get_aliquot_sample(),
        # For troubleshooting
        "config_label_data": "~wc",
        "sample_barcode_label_data": "^XA^FO50,50^B8N,100,Y,N^FD1234567^FS^XZ",
    }
    return render(request, "edc/index.html", context)


def sample(request):
    return render(request, "sample/index.html")
