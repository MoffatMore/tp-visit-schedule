from tp_labs import chemistry_alt_panel, chemistry_panel, csf_chemistry_panel
from edc_visit_schedule import FormsCollection, Requisition

requisitions_prn = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=chemistry_alt_panel, required=False, additional=False),
    Requisition(
        show_order=30,
        panel=csf_chemistry_panel, required=False, additional=False),
    name='requisitions_prn')

requisitions_d1 = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=chemistry_alt_panel, required=False, additional=False),
    Requisition(
        show_order=30,
        panel=csf_chemistry_panel, required=False, additional=False),
    name='requisitions_day1'
)

requisitions_d3 = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=False, additional=False),
    Requisition(
        show_order=20,
        panel=chemistry_alt_panel, required=False, additional=False),
    Requisition(
        show_order=30,
        panel=csf_chemistry_panel, required=False, additional=False),
    name='requisitions_day3'
)

requisitions_d5 = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=True, additional=False),
    name='requisitions_default')
