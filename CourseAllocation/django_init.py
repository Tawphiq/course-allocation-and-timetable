import os
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CourseAllocation.settings')

# Initialize Django settings
import django
django.setup()
