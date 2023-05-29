from my_sqlalchemy.school.models import Group, session

group_1 = Group("tms3")
group_2 = Group("tms4")
session.add_all([group_1, group_2])
session.commit()
