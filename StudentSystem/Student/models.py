from django.db import models

# models.py

class Domain(models.Model):
    domain_name = models.CharField(max_length=200)
    domain_code = models.CharField(max_length=20)

    class Meta:
        ordering = ('domain_name',)
        verbose_name_plural = 'domains'
        
    def __str__(self):
        return self.domain_name


class Student(models.Model):
    stu_num = models.PositiveIntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='student_images', null=False, blank=False, default='Student2.jpg')
    gpa = models.FloatField()
    domain = models.ForeignKey(Domain, related_name='students', on_delete=models.CASCADE)
#Here domain having foregin key means each Student can have one domain name and code but each doamin code and name can have many students.
    class Meta:
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
