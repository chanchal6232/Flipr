import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flipr_project.settings')
django.setup()

from main.models import Project, Client

print('=' * 50)
print('ADDING SAMPLE DATA TO DATABASE')
print('=' * 50)

# Sample Projects Data
projects_data = [
    {
        'name': 'E-commerce Website',
        'description': 'Built a full-featured e-commerce platform with payment gateway integration and inventory management system.',
        'category': 'Web Development',
        'location': 'New York'
    },
    {
        'name': 'Brand Identity Design',
        'description': 'Created complete brand identity including logo, business cards, and marketing materials for a startup.',
        'category': 'Design',
        'location': 'San Francisco'
    },
    {
        'name': 'Digital Marketing Campaign',
        'description': 'Executed a 3-month digital marketing campaign across social media, Google Ads, and email marketing.',
        'category': 'Marketing',
        'location': 'Chicago'
    },
    {
        'name': 'Business Consultation',
        'description': 'Provided strategic business consultation to optimize operations and increase profitability.',
        'category': 'Consultation',
        'location': 'Boston'
    },
    {
        'name': 'Mobile App Development',
        'description': 'Developed a cross-platform mobile application for both iOS and Android with real-time features.',
        'category': 'Mobile Development',
        'location': 'Austin'
    }
]

# Sample Clients Data
clients_data = [
    {
        'name': 'Sarah Johnson',
        'designation': 'CEO',
        'company': 'TechNova Solutions',
        'description': 'Working with this team was exceptional. They delivered our project ahead of schedule with outstanding quality.'
    },
    {
        'name': 'Michael Chen',
        'designation': 'Marketing Director',
        'company': 'Global Brands Inc.',
        'description': 'The marketing campaign they designed increased our sales by 45% in just 3 months. Highly recommended!'
    },
    {
        'name': 'Priya Sharma',
        'designation': 'Founder',
        'company': 'StartUpHub',
        'description': 'From consultation to execution, their team provided excellent guidance and technical expertise.'
    },
    {
        'name': 'Robert Williams',
        'designation': 'Operations Manager',
        'company': 'RetailPlus',
        'description': 'Professional, timely, and delivered beyond our expectations. Will definitely work with them again.'
    }
]

print('\n1. Adding Sample Projects...')
for project_info in projects_data:
    # Check if project already exists
    if not Project.objects.filter(name=project_info['name']).exists():
        project = Project.objects.create(**project_info)
        print(f'   ✓ Added: {project.name} - {project.category}')
    else:
        print(f'   ⚠ Already exists: {project_info["name"]}')

print('\n2. Adding Sample Clients...')
for client_info in clients_data:
    # Check if client already exists
    if not Client.objects.filter(name=client_info['name']).exists():
        client = Client.objects.create(**client_info)
        print(f'   ✓ Added: {client.name} - {client.designation}')
    else:
        print(f'   ⚠ Already exists: {client_info["name"]}')

print('\n' + '=' * 50)
print('DATABASE SUMMARY:')
print('=' * 50)
print(f'Total Projects: {Project.objects.count()}')
print(f'Total Clients: {Client.objects.count()}')
print('\nSample data added successfully!')
print('\nYou can now visit:')
print('- Homepage: http://127.0.0.1:8000/')
print('- Admin Panel: http://127.0.0.1:8000/dashboard/')