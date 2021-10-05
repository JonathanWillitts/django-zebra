from datetime import datetime, timezone


def _get_base_label_data():
    return dict(
        protocol="Meta III",
        site="123",
        clinician_initials="ZZ",
        alpha_code="321",
        barcode_value="012345678912",
        panel="HbA1c",
        subject_identifier="123-456-789",
        initials="AA",
        dob="01-Jan-2000",
        gender="Male",
        drawn_datetime=datetime.now(timezone.utc).strftime("%d-%b-%Y @ %H:%M:%S %Z"),
    )


def get_requisition_sample():
    return (
        "^XA^PR4"
        "^FO315,15^A0N,20,15^FD{protocol} Site {site} {clinician_initials} {alpha_code} {item}/{item_count}^FS"
        "^FO315,34^BY1^BCN,50,N,N,N,A"
        "^FD${barcode_value}^FS"
        "^FO315,92^A0N,20,15^FD{requisition_identifier}   {panel}^FS"
        "^FO315,112^A0N,20,15^FD{subject_identifier} ({initials})^FS"
        "^FO315,132^A0N,20,15^FDDOB: {dob} {gender}^FS"
        "^FO315,152^A0N,20,15^FD{drawn_datetime}^FS"
        "^XZ"
    ).format(
        item="1",
        item_count="3",
        requisition_identifier="4567",
        **_get_base_label_data()
    )


def get_aliquot_sample():
    return (
        "^XA^PR4"
        "^FO315,15^A0N,20,15^FD{protocol} Site {site} {clinician_initials} {alpha_code} {aliquot_count}/{children_count} {primary}^FS"
        "^FO315,34^BY1^BCN,50,N,N,N,A"
        "^FD{barcode_value}^FS"
        "^FO315,92^A0N,20,15^FD{aliquot_identifier}^FS"
        "^FO315,112^A0N,20,15^FD{subject_identifier} ({initials})^FS"
        "^FO315,132^A0N,20,15^FDDOB: {dob} {gender}^FS"
        "^FO315,152^A0N,20,15^FD{drawn_datetime}  {panel}^FS"
        "^XZ"
    ).format(
        aliquot_identifier="6789",
        aliquot_count="2",
        children_count="4",
        primary="xXx",
        **_get_base_label_data()
    )
