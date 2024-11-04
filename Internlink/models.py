from django.db import models

class Intern(models.Model):
    
    photo = models.ImageField(null=True,upload_to='images/')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    intern_id = models.CharField(max_length=50)
    team = models.CharField(max_length=50, choices=[
        ('Rewards Team', 'Rewards Team'),
        ('Skill Team', 'Skill Team'),
        ('Academics', 'Academics'),
        ('T&P', 'T&P'),
        ('R&D', 'R&D'),
        ('PIC', 'PIC'),
    ])
    mobile_number = models.CharField(max_length=15)
    alt_mobile_number = models.CharField(max_length=15, blank=True)
    personal_email = models.EmailField(max_length=100)
    institution_email = models.EmailField(max_length=100)
    reporting_head = models.CharField(max_length=50)
    stipend = models.DecimalField(max_digits=10, decimal_places=2)
    working_duration = models.IntegerField()
    
    
    interview_date = models.DateField()
    joining_date = models.DateField()
    selection_status = models.CharField(max_length=50, choices=[
        ('Selected', 'Selected'),
        ('Waiting List', 'Waiting List'),
    ])
    working_status = models.CharField(max_length=50, choices=[
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ])
    
   
    dob = models.DateField()
    gender = models.CharField(max_length=50, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ])
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=50)
    blood_group = models.CharField(max_length=3)
    current_address = models.TextField()
    permanent_address = models.TextField()
    
  
    school_10th_name = models.CharField(max_length=100)
    percentage_10th = models.DecimalField(max_digits=5, decimal_places=2)
    year_of_passing_10th = models.IntegerField()
    school_12th_name = models.CharField(max_length=100)
    percentage_12th = models.DecimalField(max_digits=5, decimal_places=2)
    year_of_passing_12th = models.IntegerField()
    
    
    ug_college_name = models.CharField(max_length=100)
    ug_course = models.CharField(max_length=50)
    ug_degree = models.CharField(max_length=50)
    ug_cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    ug_year_of_passing = models.IntegerField()
    

    pg_college_name = models.CharField(max_length=100, blank=True)
    pg_course = models.CharField(max_length=50, blank=True)
    pg_degree = models.CharField(max_length=50, blank=True)
    pg_cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    pg_year_of_passing = models.IntegerField(null=True, blank=True)
    
   
    previous_company = models.CharField(max_length=100, blank=True)
    job_title = models.CharField(max_length=50, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    
    
    resume_upload = models.FileField(null=True,upload_to='resumes/')
    linkedin = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

