from django.db import models



class Status(models.Model):
    status_code = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=100)
    status_color = models.CharField(max_length=50)

    def __unicode__(self):
        return self.status_name


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField()
    create_timestamp = models.DateTimeField()
    complete_timestamp = models.DateTimeField()
    status = models.ForeignKey(Status)

    class Meta:
        verbose_name_plural = "1. Projects"



class Milestone(models.Model):
    milestone_name = models.CharField(max_length=100)
    milestone_description = models.TextField()
    create_timestamp = models.DateTimeField()
    complete_timestamp = models.DateTimeField()
    status = models.ForeignKey(Status)
    project = models.ForeignKey(Project)

    class Meta:
        verbose_name_plural = "2. Milestones"


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    create_timestamp = models.DateTimeField()
    complete_timestamp = models.DateTimeField()
    status = models.ForeignKey(Status)
    project = models.ForeignKey(Project)
    milestone = models.ForeignKey(Milestone)

    class Meta:
        verbose_name_plural = "3. Tasks"

