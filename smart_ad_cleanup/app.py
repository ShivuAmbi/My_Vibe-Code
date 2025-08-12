from flask import Flask, render_template_string, request
from ai_analyzer import analyze_ad_objects

app = Flask(__name__)

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

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Smart AD Cleanup Assistant</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        h1 { color: #2c3e50; }
        table { border-collapse: collapse; width: 100%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #f4f4f4; }
        .stale { background: #ffe6e6; }
        .active { background: #e6ffe6; }
        .btn { padding: 10px 20px; background: #3498db; color: #fff; border: none; cursor: pointer; margin-top: 20px; }
        .btn:hover { background: #2980b9; }
    </style>
</head>
<body>
    <h1>Smart AD Cleanup Assistant</h1>
    <form method="post">
        <button class="btn" type="submit">Run Analysis</button>
    </form>
    <table>
        <tr>
            <th>Name</th><th>Type</th><th>Last Login</th><th>Department</th><th>Email</th><th>OS</th><th>Owner</th><th>Status</th>
        </tr>
        {% for obj in results %}
        <tr class="{{ obj.status }}">
            <td>{{ obj.name }}</td>
            <td>{{ obj.type }}</td>
            <td>{{ obj.last_login }}</td>
            <td>{{ obj.get('department', '') }}</td>
            <td>{{ obj.get('email', '') }}</td>
            <td>{{ obj.get('os', '') }}</td>
            <td>{{ obj.get('owner', '') }}</td>
            <td>{{ obj.status }}</td>
        </tr>
        {% endfor %}
    </table>
    <p><b>{{ summary }}</b></p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        results = analyze_ad_objects(ad_objects)
        stale_count = sum(1 for obj in results if obj.get('status') == 'stale')
        summary = f"Analysis complete. {stale_count} stale object(s) found."
    else:
        results = ad_objects
        summary = "Click 'Run Analysis' to analyze AD objects."
    return render_template_string(TEMPLATE, results=results, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
