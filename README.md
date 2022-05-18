# Shopify Production Engineer Intern Challenge

An inventory tracking web application for a logistics company with basic CRUD functionalities:
- Create inventory items
- Edit inventory items
- Delete inventory items
- View a list of inventory items

Additional features:
- Ability to create warehouses and assign inventory to specific locations
- Display of current weather condition for warehouse locations

## Contents
- [Tech Stack](#tech-stack)
- [Justification](#justification)
- [Feature Details](#feature-details)
- [Future Features](#future-features)
- [Installation](#installation)
- [Demo](#demo)
- [About the Developer](#about-the-developer)

## Tech Stack

**Backend:** Python, Flask, SQLAlchemy, Jinja

**Frontend:** HTML

**Database:** PostgreSQL

## Justification
In the backend, I chose to use Flask, a lightweight Python web framework, because of its flexibility in customization and ease in creating routes. For the database, I used the relational database postgreSQL due to its consistency to help ensure completeness of data, which is important for an inventory app. Finally, I used SQLAlchemly as the ORM to make queries in my Flask web app. 

## Feature Details

At the homepage, users are shown a navigation links to do the following:

**Create inventory items**

Users will enter details for a new item, including its stock keeping unit(SKU), name, description, quantity, unit and unit cost. A dropdown with existing warehouses allows users to select which warehouse item is located.
Backend algorithms validate inputs before committing to database.

**View all inventory items**

Users can view all inventory items in a table, sorted by SKU. Warehouse and weather information are also displayed.

**View details of an inventory item**

Users can view details of an inventory item by clicking on the SKU or searching for an item by its SKU.

**Edit the details of an inventory item**

Users can edit details of an inventory items. Form will be populated with existing data.

**Delete an inventory item**

Users can delete an item. Alert is raised to confirm deletion before removing from database.

**Search for an inventory item**

Users can search for an item by its SKU. Successful search will be redirected to corresponding item detail page. 

**Add a warehouse**

Users can create a new warehouse by entering its city name and city code. Backend algorithms validate input before committing to database.

**View all warehouses**

Users can view all existing warehouses in a table, sorted by warehouse ID. Information displayed includes warehouse ID, city name and code, and current weather information.

**View details of a warehouse**

Users can view details of a warehouse by clicking on its warehouse ID or city name. Details include city name, city code, current weather condition, and all inventory in the particular warehouse.

**Delete a warehouse**

Users can delete a warehouse. 

## Future Features

- Assignment of inventory upon deletion of warehouse

## Installation

**Prerequisites**

To run the inventory web app, you will need to have Python 3 and PostgreSQL installed on your machine.

**Running the inventory web app on your machine**

Clone this repository
```shell
git clone https://github.com/juliatangwc/shopify-production-engineer-intern-challenge.git
```
Optional: Create and activate a virtual environment using virtualenv
```shell
pip3 install virtualenv
virtualenv env
source env/bin/activate
```
Install dependencies from requirements.txt
```shell
pip3 install -r requirements.txt
```
Create your database & seed sample data
```shell
createdb inventory_production
python3 seed_database.py
```
Run the app on localhost
```shell
python3 server.py
```
## Demo
Run the inventory app on [Replit](https://replit.com/join/rruscqcvah-juliatangwc) and play with the [Demo](https://shopify-coding-challenge.juliatangwc.repl.co)

## About the Developer
Julia is a naturally curious person who enjoys problem-solving and learning new things along the way. She started a career in research upon graduating as a registered dietitian. For the past 6 years, she led research projects to develop dietetic service for the first cancer care center in Hong Kong and obtained a PhD in public health in the process. During that time, her research projects on health reminders and facilitative e-tasks in nutrition counseling introduced her to the exciting world of software engineering. She was inspired by how technology is changing every aspect of our lives and aspired to be part of the change. She graduated from Hackbright Academy in April 2022 and is excited to start making a positive impact with her skills.

[![LinkedIn][LinkedInImg]][LinkedInLink]

[LinkedInImg]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[LinkedInLink]: https://www.linkedin.com/in/juliatangwc