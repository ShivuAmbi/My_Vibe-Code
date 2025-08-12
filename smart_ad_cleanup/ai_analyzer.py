# AI Analyzer for AD objects
# Classifies objects as active/inactive/stale

from datetime import datetime

def analyze_ad_objects(ad_objects):
    threshold_stale = datetime(2024, 7, 1)
    results = []
    for obj in ad_objects:
        last_login = datetime.strptime(obj['last_login'], '%Y-%m-%d')
        if last_login < threshold_stale:
            status = 'stale'
        else:
            status = 'active'
        obj_with_status = obj.copy()
        obj_with_status['status'] = status
        results.append(obj_with_status)
    return results
