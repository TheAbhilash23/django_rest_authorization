<h1> Django Rest Permissions for Authorization</h1> <br>
<br>
In this project we are looking to make authorization a smooth and easy to configure process.


To make it configurable we need to ensure a few things.
1. What base classes are we going to make configurable
2. Configurable yaml permissions file
3. Steps to validate the permissions definition
4. Extract information from yaml, dump into database.
5. Create a cache object to reduce load on db

<h3> FLOW </h3>

1. Dev will add a yaml file.
2. Server will read the yaml to get the access control information from yaml (views, action, methods)
3. Server will validate the yaml
4. Upon successful validation, server will create permissions object in db.
5. The permissions will be non editable since the permissions are derived from the yaml file. 




