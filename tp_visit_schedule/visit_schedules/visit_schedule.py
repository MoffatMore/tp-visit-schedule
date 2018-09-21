from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import schedule
# from .schedule_w10 import schedule_w10

app_label = 'tp_subject'

visit_schedule = VisitSchedule(
    name='visit_schedule',
    verbose_name='Trainee Project',
    offstudy_model=f'ambition_prn.studyterminationconclusion',
    death_report_model=f'ambition_prn.deathreport',
    locator_model='edc_locator.subjectlocator',
    previous_visit_schedule=None)

visit_schedule.add_schedule(schedule)
site_visit_schedules.register(visit_schedule)
