# Smart AD Cleanup Assistant
# Entry point for pulling AD objects and running analysis

from ai_analyzer import analyze_ad_objects
from report_generator import generate_report

# Placeholder: Replace with actual AD pull logic
ad_objects = [
    {'name': 'user1', 'last_login': '2024-01-01', 'type': 'user', 'department': 'IT', 'email': 'user1@company.com'},
    {'name': 'user2', 'last_login': '2022-01-01', 'type': 'user', 'department': 'HR', 'email': 'user2@company.com'},
    {'name': 'user3', 'last_login': '2023-05-15', 'type': 'user', 'department': 'Finance', 'email': 'user3@company.com'},
    {'name': 'user4', 'last_login': '2021-11-20', 'type': 'user', 'department': 'IT', 'email': 'user4@company.com'},
    {'name': 'comp1', 'last_login': '2023-12-01', 'type': 'computer', 'os': 'Windows 10', 'owner': 'user1'},
    {'name': 'comp2', 'last_login': '2022-08-10', 'type': 'computer', 'os': 'Windows 11', 'owner': 'user2'},
    {'name': 'comp3', 'last_login': '2024-06-01', 'type': 'computer', 'os': 'Linux', 'owner': 'user3'},
    {'name': 'comp4', 'last_login': '2020-03-15', 'type': 'computer', 'os': 'Windows 7', 'owner': 'user4'},
]

results = analyze_ad_objects(ad_objects)
generate_report(results)
