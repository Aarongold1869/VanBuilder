from django.db.models import Q
from django.apps import apps
from components.models import *

import pandas as pd
import os
import openpyxl
from datetime import datetime

def extract(f):
    wb = openpyxl.load_workbook(f, data_only=True)
    master_data = {}
    for ws in wb.worksheets:
        for tbl in ws.tables.values():
            data = ws[tbl.ref]
            rows_list = []
            for row in data:
                cols = []
                for col in row:
                    cols.append(col.value)
                rows_list.append(cols)
            df = pd.DataFrame(data=rows_list[1:], index=None, columns=rows_list[0])
            for column in df:
                df[column].fillna(0, inplace=True)
            master_data[ws.title] = df
    return master_data

def load_categories(table):
    for i, row in table.iterrows():
        name = row['name']
        description = row['description']
        category = Category.objects.get_or_create(name=name)[0]
        category.description = description
        category.save()

def load_vans(table):
    for i, row in table.iterrows():
        make = row['make']
        model = row['model']
        year = row['year']
        wheelbase = row['wheelbase']
        van_type = row['van_type']
        van = Van.objects.get_or_create(
            make = make,
            model = model,
            year = year,
            wheelbase = wheelbase,
            van_type = van_type
        )[0]
        van.price_new = row['price_new']
        van.price_used = row['price_used']
        van.max_weight = row['max_weight']
        van.engine = row['engine']
        van.transmission = row['transmission']
        van.drive = row['drive']
        van.passengers = row['passengers']
        van.fuel_tank = row['fuel_tank']
        van.mpg = row['mpg']
        van.cargo_width	= row['cargo_width']
        van.cargo_height = row['cargo_height']
        van.cargo_length = row['cargo_length']
        van.external_width = row['external_width']
        van.external_height = row['external_height']
        van.external_length = row['external_length']
        van.save()

def load_components(master_data):
    for table in master_data:
        if table == "Vans" or table == "Categories":
            continue
        for i, row in master_data[table].iterrows():
            category_name = row['category']
            category = Category.objects.get(name=category_name)
            component = row['component']
            model = apps.get_model(app_label="components", model_name=component)
            obj = model.objects.get_or_create(
                category = category,
                item = row['item'],
                dimensions = row['dimensions']
            )[0]
            ignore_fields = [
                'category',
                'item',
                'dimensions',
                'id'
            ]
            for field in model._meta.get_fields():
                if not field.name in ignore_fields:
                    obj.field = row[field.name]
            obj.save

def load_data(master_data):
    load_categories(master_data['Categories'])
    load_vans(master_data['Vans'])
    load_components(master_data)

def run_extract():
    f = r'components\data\data.xlsx'
    isfile = os.path.isfile(f) # check if file exists
    if isfile == False: # if not
        return ValueError # throw error 
    master_data = extract(f)
    load_data(master_data)