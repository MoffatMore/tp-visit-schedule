from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit
from tp_labs.panels import chemistry_panel
from ..constants import DAY1, DAY3, DAY5, DAY7, DAY14, DAY12, DAY10
from ..constants import WEEK16, WEEK10, WEEK8, WEEK6, WEEK4
from .crfs import (
    crfs_d5, crfs_d1, crfs_d3, crfs_prn as default_crfs_prn,
    crfs_unscheduled as default_crfs_unscheduled)
from ..constants import DAY1, DAY3, DAY5
from .requisitions import (
    requisitions_d1, requisitions_d3, requisitions_d5,
    requisitions_prn as default_requisitions_prn)
from edc_visit_schedule.visit.forms_collection import FormsCollection

default_requisitions = None


class Visit(BaseVisit):
    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled or default_crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled or default_requisitions,
            crfs_prn=crfs_prn or default_crfs_prn,
            requisitions_prn=requisitions_prn or default_requisitions_prn,
            **kwargs)


# schedule for new participants
schedule = Schedule(
    name='schedule',
    verbose_name='Day 1 to Day 14 Follow-up',
    onschedule_model='ambition_prn.onschedule',
    offschedule_model='ambition_prn.studyterminationconclusion',
    consent_model='tp_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')


visit0 = Visit(
    code=DAY1,
    title='Day 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d1,
    requisitions_prn=FormsCollection(
        *[r for r in default_requisitions_prn if r.panel != chemistry_panel]),
    crfs=crfs_d1,
    facility_name='7-day clinic')

visit1 = Visit(
    code=DAY3,
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    crfs=crfs_d3,
    facility_name='7-day clinic')

visit2 = Visit(
    code=DAY5,
    title='Day 5',
    timepoint=2,
    rbase=relativedelta(days=4),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    crfs=crfs_d5,
    facility_name='7-day clinic')
visit3 = Visit(
    code=DAY7,
    title='Day 7',
    timepoint=3,
    rbase=relativedelta(days=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d3,
    crfs=crfs_d1,
    facility_name='7-day clinic')

visit4 = Visit(
    code=DAY10,
    title='Day 10',
    timepoint=4,
    rbase=relativedelta(days=9),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d5,
    crfs=crfs_d3,
    facility_name='7-day clinic')

visit5 = Visit(
    code=DAY12,
    title='Day 12',
    timepoint=5,
    rbase=relativedelta(days=11),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions_d1,
    crfs=crfs_d5,
    facility_name='7-day clinic')

visit6 = Visit(
    code=DAY14,
    title='Day 14',
    timepoint=6,
    rbase=relativedelta(days=13),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_d5,
    crfs=crfs_d1,
    facility_name='7-day clinic')

visit7 = Visit(
    code=WEEK4,
    title='Week 4',
    timepoint=7,
    rbase=relativedelta(weeks=4),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions_d1,
    crfs=crfs_d3,
    facility_name='5-day clinic')

visit8 = Visit(
    code=WEEK6,
    title='Week 6',
    timepoint=8,
    rbase=relativedelta(weeks=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=None,
    crfs=crfs_d5,
    facility_name='5-day clinic')


schedule.add_visit(visit=visit0)
schedule.add_visit(visit=visit1)
schedule.add_visit(visit=visit2)
schedule.add_visit(visit=visit3)
schedule.add_visit(visit=visit4)
schedule.add_visit(visit=visit5)
schedule.add_visit(visit=visit6)
schedule.add_visit(visit=visit7)
schedule.add_visit(visit=visit8)