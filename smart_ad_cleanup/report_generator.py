# Generates a report of AD cleanup recommendations

def generate_report(results):
    print('AD Cleanup Recommendations:')
    for obj in results:
        details = []
        if obj['type'] == 'user':
            details.append(f"Department: {obj.get('department', 'N/A')}")
            details.append(f"Email: {obj.get('email', 'N/A')}")
        elif obj['type'] == 'computer':
            details.append(f"OS: {obj.get('os', 'N/A')}")
            details.append(f"Owner: {obj.get('owner', 'N/A')}")
        details_str = ', '.join(details)
        if obj['status'] == 'stale':
            print(f"{obj['type'].capitalize()} '{obj['name']}' is stale and should be reviewed for cleanup. [{details_str}]")
        else:
            print(f"{obj['type'].capitalize()} '{obj['name']}' is active. [{details_str}]")
