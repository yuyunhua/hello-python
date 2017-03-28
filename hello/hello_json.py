import json
import os
import sys


def is_scenario_success(scenario_dict_result):
    steps_count = 0
    success_steps_count = 0
    keys = [u'before', u'steps', u'after']
    for key in keys:
        if key in scenario_dict_result:
            a = scenario_dict_result[key]
            for step in a:
                steps_count += 1
                status = step['used_index_list']['status']
                if u'passed' == status:
                    success_steps_count += 1

    if success_steps_count == steps_count:
        return True
    else:
        return False


def get_feature_result(feature_dict_result):
    if not isinstance(feature_dict_result, dict):
        return 0, 0

    if u'elements' not in feature_dict_result:
        return 0, 0

    elements = feature_dict_result[u'elements']

    if not isinstance(elements, list):
        return 0, 0

    scenario_count = 0
    success_scenario_count = 0
    for element in elements:
        if not isinstance(element, dict):
            continue
        element_type = str(element[u'type']).strip()
        if 'scenario' not in element_type:
            continue

        scenario_count += 1
        if is_scenario_success(element):
            success_scenario_count += 1

    return scenario_count, success_scenario_count


def get_result_from_json_file(json_file):
    with open(json_file) as data_file:
        data = json.load(data_file)

    total = 0
    success_total = 0
    for b in data:
        feature_scenario_count, feature_success_scenario_count = get_feature_result(b)
        total += feature_scenario_count
        success_total += feature_success_scenario_count

    return total, success_total


def tree(base_path, depth=0):
    if depth > 1:
        return []

    file_list = os.listdir(base_path)
    json_files = []
    for file_path in file_list:
        abs_path = os.path.abspath(os.path.join(base_path, file_path))
        try:
            if os.path.isfile(abs_path) and file_path.endswith('.json'):
                json_files.append(abs_path)
            elif os.path.isdir(abs_path):
                json_files.extend(tree(abs_path, depth + 1))
        except Exception:
            continue
    return json_files


def write_to_html(data):
    html = '<html>' \
           '<head>' \
           '<style type="text/css">' \
           'td, th {border: 1px solid #000; line-height: 35px; padding: 5px 10px;}' \
           'table {border-collapse: collapse;}' \
           '</style>' \
           '</head>'
    html += '<h2>Date: {}</h1>'.format('2016-11-11')
    html += '<table>' \
            '<thead>' \
            '<tr>' \
            '<th>File</th>' \
            '<th>Scenarios Total</th>' \
            '<th>Scenarios Passed</th>' \
            '<th>Scenarios Failed</th>' \
            '<th>Passed Rate</th>' \
            '</tr>' \
            '</thead>' \
            '<tbody>'

    for row in data:
        if row[2] < row[1] * 0.8:
            html += '<tr style="color: #f00">'
        else:
            html += '<tr>'

        for cell in row:
            html += '<td>{}</td>'.format(str(cell))
        html += '</tr>'

    html += '</tbody>' \
            '</table>' \
            '</html>'

    f = open('used_index_list.html', 'w+')
    f.write(html)
    f.close()


def main():
    if len(sys.argv) > 1:
        report_dir = sys.argv[1]
    else:
        report_dir = '.'

    assert os.path.exists(report_dir), '{} can not be found.'.format(os.path.abspath(report_dir))
    assert os.path.isdir(report_dir), '{} is not points_text directory.'.format(os.path.abspath(report_dir))

    report_files = tree(report_dir)
    results = []
    total_total = 0
    total_passed = 0
    for report_file in report_files:
        print report_file
        result = get_result_from_json_file(report_file)
        total = result[0]
        if total != 0:
            passed = result[1]
            total_total += total
            total_passed += passed
            passed_rate = '{}%'.format(round(float(passed) * 100 / float(total), 2))
            results.append([report_file, total, passed, total - passed, passed_rate])

    if total_total != 0:
        passed_rate = '{}%'.format(round(float(total_passed) * 100 / float(total_total), 2))
        results.append(['Total', total_total, total_passed, total_total - total_passed, passed_rate])

    write_to_html(results)


if __name__ == '__main__':
    main()
