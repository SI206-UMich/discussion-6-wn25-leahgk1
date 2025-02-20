import unittest
import os


def load_csv(f):
    '''
    Params: 
        f, name or path or CSV file: string

    Returns:
        nested dict structure from csv
        outer keys are (str) years, values are dicts
        inner keys are (str) months, values are (str) integers
    
    Note: Don't strip or otherwise modify strings. Don't change datatypes from strings. 
    '''
    import csv

    rows = []
    with open(f, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
            
    d = {}
    headers = rows[0][1:]
    for year in headers:
        d[year] = {}
        
    for row in rows[1:]:
        month = row[0]
        for i, val in enumerate(row[1:]):
            year = headers[i]
            d[year][month] = val
            
    return d

def get_annual_max(d):
    '''
    Params: dictionary from load_csv
    Returns: list of tuples (year, month, value) sorted by year
    '''
    max_list = []
    for year in sorted(d.keys()):
        max_month = max(d[year].items(), key=lambda x: int(x[1]))
        max_list.append((year, max_month[0], max_month[1]))
    return max_list

def get_month_avg(d):
    '''
    Params: 
        d, dict created by load_csv above

    Returns:
        dict where keys are years and vals are floats rounded to nearest whole num or int
        vals are the average vals for months in the year

    Note: Don't strip or otherwise modify strings. Do not change datatypes except where necessary. 
        You'll have to make the vals int or float here and round the avg to pass tests.
    '''
    result = {}
    for year in d:
        total = 0
        count = 0
        for month in d[year]:
            total += int(d[year][month])
            count += 1
        avg = round(total / count)
        result[year] = avg
    return result

class dis7_test(unittest.TestCase):
    '''
    you should not change these test cases!
    '''
    def setUp(self):
        self.flight_dict = load_csv('daily_visitors.csv')
        self.max_tup_list = get_annual_max(self.flight_dict)
        self.month_avg_dict = get_month_avg(self.flight_dict)

    def test_load_csv(self):
        self.assertIsInstance(self.flight_dict['2021'], dict)
        self.assertEqual(self.flight_dict['2020']['JUN'], '435')

    def test_get_annual_max(self):
        self.assertEqual(self.max_tup_list[2], ('2022', 'AUG', '628'))

    def test_month_avg_list(self):
        self.assertAlmostEqual(self.month_avg_dict['2020'], 398, 0)

def main():
    unittest.main(verbosity=2)
    print("----------------------------------------------------------------------")
    flight_dict = load_csv('daily_visitors.csv')
    print("Output of load_csv:", flight_dict, "\n")
    print("Output of get_annual_max:", get_annual_max(flight_dict), "\n")
    print("Output of get_month_avg:", get_month_avg(flight_dict), "\n")


if __name__ == '__main__':
    main()
