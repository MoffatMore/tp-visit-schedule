from tp_labs import  chemistry_panel
from edc_visit_schedule import FormsCollection, Requisition

requisitions_prn = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=False, additional=False),
    name='requisitions_prn')

requisitions_d1 = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=False, additional=False),
    name='requisitions_day1'
)

requisitions_d3 = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=False, additional=False),
    name='requisitions_day3'
)

requisitions_d5 = FormsCollection(
    Requisition(
        show_order=10,
        panel=chemistry_panel, required=True, additional=False),
    name='requisitions_default')
