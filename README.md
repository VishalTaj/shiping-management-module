# shiping-management-module
SHIP OBJECT CREATION
Note: Install ‘Sales Management’module first
Create a "Ship" object, manage its menu as the child of Sales --> Configuration --> Ship
Information, and add the following fields to the Ship object:
64 bit char fields:
a) IMO (unique)
b) Hull Number
c) Engine Number
d) Vessel Name
e) Build Year
Drop down list fields of the res.partner object:
f) Ship Yard
g) Ship Owner
h) Ship Management
i) Engine Builder
Also create tree and form views
2.2 ADD SHIP FIELD TO SALES ORDER AND ORDER LINES
2.2.1 Add the field
In the form view of SO, add the Ship field as a drop down list field of the Ship object to the
main page. Also add it to the list view of the SO.
Add the Ship field as a drop down list field of the Ship object to the order lines next to quantity.
2.2.2 Update the field to SO Lines
Create a button under ship field 'Update to Order Lines', update the same Ship information to the order
lines. When creating a new order line, in the Ship field by default show the Ship information of the SO
(use context).
