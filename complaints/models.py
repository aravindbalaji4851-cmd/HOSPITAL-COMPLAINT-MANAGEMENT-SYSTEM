from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Complaint(models.Model):

    COMPLAINT_TYPES = (
        ("Cleanliness","Cleanliness"),
        ("Staff Behavior","Staff Behavior"),
        ("Waiting Time","Waiting Time"),
        ("Billing","Billing"),
        ("Equipment","Equipment")
    )

    DEPARTMENTS = (
    ("Cardiology", "Cardiology"),
    ("Neurology", "Neurology"),
    ("Oncology", "Oncology"),
    ("Orthopedics", "Orthopedics"),
    ("Pediatrics", "Pediatrics"),
    ("Gynecology", "Gynecology"),
    ("Dermatology", "Dermatology"),
    ("Psychiatry", "Psychiatry"),
    ("General Medicine", "General Medicine"),
    ("General Surgery", "General Surgery"),
    ("Urology", "Urology"),
    ("Nephrology", "Nephrology"),
    ("Gastroenterology", "Gastroenterology"),
    ("Pulmonology", "Pulmonology"),
    ("Ophthalmology", "Ophthalmology"),
    ("ENT", "ENT"),
    ("Dentistry", "Dentistry"),
    ("Emergency", "Emergency"),
    ("Intensive Care Unit", "Intensive Care Unit"),
    ("Operation Theatre", "Operation Theatre"),
    ("Outpatient Department", "Outpatient Department"),
    ("Inpatient Department", "Inpatient Department"),
    ("Nursing", "Nursing"),
    ("Pharmacy", "Pharmacy"),
    ("Radiology", "Radiology"),
    ("Laboratory", "Laboratory"),
    ("Blood Bank", "Blood Bank"),
    ("Physiotherapy", "Physiotherapy"),
    ("Dialysis", "Dialysis"),
    ("Maternity", "Maternity"),
    ("Pediatrics ICU", "Pediatrics ICU"),
    ("Anesthesiology", "Anesthesiology"),
    ("Pathology", "Pathology"),
    ("Microbiology", "Microbiology"),
    ("Nutrition and Dietetics", "Nutrition and Dietetics"),
    ("Medical Records", "Medical Records"),
    ("Billing", "Billing"),
    ("Insurance and Claims", "Insurance and Claims"),
    ("Reception", "Reception"),
    ("Patient Relations", "Patient Relations"),
    ("Housekeeping", "Housekeeping"),
    ("Maintenance", "Maintenance"),
    ("Security", "Security"),
    ("Cafeteria", "Cafeteria"),
    ("Ambulance Services", "Ambulance Services"),
    ("Hospital Administration", "Hospital Administration"),
    ("Information Technology", "Information Technology"),
    ("Laundry", "Laundry"),
    ("Medical Equipment", "Medical Equipment"),
    ("Other", "Other")
    )

    PRIORITIES = (
        ("Low","Low"),
        ("Medium","Medium"),
        ("High","High"),
        ("Critical","Critical")
        )

    STATUS = (
        ("Submitted","Submitted"),
        ("Under Review","Under Review"),
        ("In Progress","In Progress"),
        ("Resolved","Resolved")
    )

    title = models.CharField(max_length=200)

    description = models.TextField(max_length=500)

    complaint_type = models.CharField(max_length=200,choices=COMPLAINT_TYPES)

    department = models.CharField(max_length=200,choices=DEPARTMENTS)

    priority = models.CharField(max_length=100,choices=PRIORITIES,default="Medium")

    status = models.CharField(max_length=100,choices=STATUS,default="Submitted")

    reported_date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title