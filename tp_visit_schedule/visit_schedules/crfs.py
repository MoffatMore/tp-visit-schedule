from edc_visit_schedule import FormsCollection, Crf

crfs_prn = FormsCollection(
    Crf(show_order=1, model='tp_subject.demographic'),
    Crf(show_order=2, model='tp_subject.education'),
    Crf(show_order=3, model='tp_subject.educationhoh',
        required=False),
    Crf(show_order=4, model='tp_subject.communityengagement'),
    name='prn')

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model='tp_subject.demographic'),
    Crf(show_order=2, model='tp_subject.communityengagement'),
    name='unscheduled'
)

crfs_d1 = FormsCollection(
    Crf(show_order=1, model='tp_subject.education'),
    Crf(show_order=2, model='tp_subject.educationhoh',
        required=False),
    Crf(show_order=3, model='tp_subject.demographic'),
    name='day1'
)

crfs_d3 = FormsCollection(
#     Crf(show_order=1, model='tp_subject.bloodresult'),
    Crf(show_order=1, model='tp_subject.education'),
    Crf(show_order=2, model='tp_subject.educationhoh',
        required=False),
    name='day3'
)

crfs_d5 = FormsCollection(
#     Crf(show_order=1, model='tp_subject.bloodresult'),
    Crf(show_order=1, model='tp_subject.communityengagement'),
    name='day5'
)
