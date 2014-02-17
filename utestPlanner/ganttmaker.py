__author__ = 'Jonathan'

from googlegantt import GanttChart, GanttCategory


gc = GanttChart('Test Chart', width=1000, height=300, progress=(2011, 02, 27))

on_time = GanttCategory('On Time', '333')
late = GanttCategory('Late', '333')
upcoming = GanttCategory('Upcoming', '333')

t1 = gc.add_task('Write test plan', (2014, 03, 20), (2014, 03, 25), category=late)
t2 = gc.add_task('Recruit participants', depends_on=t1, duration=3, category=on_time)
t3 = gc.add_task('Conduct test', depends_on=t2, duration=2, category=upcoming)

url = gc.get_url()
image = gc.get_image()

print url