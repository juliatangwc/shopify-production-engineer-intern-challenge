"""Script to seed database with test data."""
"""Warehouse data: 5 warehouse; Inventory data: 20 items"""

import os
import json
import server
import helper

from model import connect_to_db, db, Inventory, Warehouse

os.system("dropdb inventory_production")
os.system('createdb inventory_production')

connect_to_db(server.app)
db.create_all()

# Load warehouse data from JSON file
with open('data/warehouse.json') as f:
    warehouse_data = json.loads(f.read())

#Create new instances of warehouse in database
for warehouse in warehouse_data:
    city_code = warehouse['city_code']
    city_name = warehouse['city_name']
    coordinates = helper.get_city_geocode(city_name)
    lon = coordinates['lon']
    lat = coordinates['lat']

    new_warehouse = Warehouse.create_warehouse (city_code, city_name, lon, lat)
    db.session.add(new_warehouse)

# Load inventory data from JSON file
with open('data/inventory.json') as f:
    inventory_data = json.loads(f.read())

#Create new instances of inventory item in database
for item in inventory_data:
    sku = item['sku']
    warehouse_id = item['warehouse_id']
    name = item['name']
    description = item['description']
    quantity = item['quantity']
    unit = item['unit']
    unit_cost = item['unit_cost']

    new_item = Inventory.create_inventory_item (sku, warehouse_id, name, description,
                                                quantity, unit, unit_cost)
    db.session.add(new_item)

db.session.commit()
    