"""
    import existing model from django database 
"""
from django.db import models


class Domain(models.Model):
    """
    Represents a Domain.
    """
    domain_name = models.CharField(max_length=200)
    domain_code = models.CharField(max_length=20)

    class Meta:
        """
        Meta options for Domain model.

        Attributes:
            ordering (tuple): A tuple of field names to use for ordering the results.
            verbose_name_plural (str): The plural name to use for the model in the admin interface.
        """
        ordering = ('domain_name',)
        verbose_name_plural = 'domains'

    def __str__(self):
        """
        Returns the string representation of the Domain object.

        Returns:
            str: The domain name.
        """
        return self.domain_name


class Student(models.Model):
    """
    Represents a Student.
    """
    stu_num = models.PositiveIntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    image = models.ImageField(
        upload_to='student_images', null=False, blank=False, default='Student2.jpg')
    gpa = models.FloatField()
    domain = models.ForeignKey(Domain, related_name='students', on_delete=models.CASCADE)

    class Meta:
        """
        Meta options for Student model.

        Attributes:
            ordering (tuple): A tuple of field names to use for ordering the results.
        """
        ordering = ('last_name', 'first_name')

    def __str__(self):
        """
        Returns the string representation of the Student object.

        Returns:
            str: The full name of the student.
        """
        return f'{self.first_name} {self.last_name}'
        