from my_sqlalchemy.school.models import Group, session

group_1 = Group("tms1")
group_2 = Group("tms2")
session.add_all([group_1, group_2])
session.commit()