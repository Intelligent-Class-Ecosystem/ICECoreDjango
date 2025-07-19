from django.db import models

# Create your models here.
class Organization(models.Model):
    """
    组织类。
    :cvar name: 组织名称
    :cvar description: 组织描述
    :ivar classrooms: 组织包含的教室列表 (定义在 Classroom 类中)
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'classrooms': [classroom.get_dict() for classroom in self.classrooms.all()],
        }

class Classroom(models.Model):
    """
    教室类。

    :cvar name: 教室名称
    :cvar description: 教室描述
    :cvar belong_organization: 【从属关系变量】教室所属的组织
    :ivar classrooms: 教室包含的周期列表 (定义在 Cycle 类中)
    :ivar today_timetable: 教室的今天的课程表 (定义在 Timetable 类中)
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    belong_organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='classrooms')


    def get_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            # 'belong_organization': self.belong_organization.get_dict(),
            'cycles': [cycle.get_dict() for cycle in self.cycles.all()],
            'today_timetable': self.today_timetable.get_dict() if hasattr(self, "today_timetable") else None,
        }

class Cycle(models.Model):
    """
    周期类。

    :cvar name: 周期名称
    :cvar description: 周期描述
    :cvar belong_classroom: 【从属关系变量】周期所属的教室
    :ivar cycles: 周期包含的时间表列表 (定义在 Timetable 类中)
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    belong_classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='cycles')
    def get_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'timetables': [timetable.get_dict() for timetable in self.timetables.all()],
        }

class Timetable(models.Model):
    """
    时间表类。

    :cvar name: 时间表名称
    :cvar description: 时间表描述
    :cvar date: 时间表日期
    :cvar belong_cycle: 【从属关系变量】时间表所属的周期
    :cvar belong_today: 【从属关系变量】时间表所属的今天的课程表
    :ivar periods: 时间表包含的时间段列表 (定义在 Period 类中)
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    # 从属的变量
    belong_cycle = models.ManyToManyField(Cycle, related_name='timetables')
    belong_today = models.OneToOneField(Classroom, on_delete=models.CASCADE, related_name='today_timetable')
    def get_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'date': self.date,
            'periods': [period.get_dict() for period in self.periods.all()],
        }

class Activity(models.Model):
    """
    活动类。

    :cvar name: 活动名称
    :cvar description: 活动简介
    :cvar belong_periods: 活动所属的时间段 (定义在 Period 类中)
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    def get_dict(self):
        return {
            'name': self.name,
            'description': self.description,
        }

class Period(models.Model):
    """
    时段类。

    一个时段只能有一个活动，而一个活动可以属于多个时段。

    :cvar start_time: 时段的起始时间
    :cvar end_time: 时段的终止时间
    :cvar activity: 时间段内的活动
    :cvar belong_timetables: 【从属关系变量】时间段所属的时间表
    """
    start_time = models.TimeField()
    end_time = models.TimeField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='belong_periods')
    # 从属的变量
    belong_timetables = models.ManyToManyField(Timetable, related_name='periods')

    def get_dict(self):
        return {
            'start_time': self.start_time,
            'end_time': self.end_time,
            'activity': self.activity.get_dict() if hasattr(self, "activity") else None,
        }





    








   




