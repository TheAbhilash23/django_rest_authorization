<h1> Django Rest Permissions for Authorization</h1> <br>
<br>
In this project we are looking to make authorization a smooth and easy to configure process.


<h3> FLOW </h3>

1. Using scan_and_make_authorization_routes method the action methods are created in model ActionMethod for all routes that start with the one specified in the app_settings 
2. Once the routes are created rest_groups can be created to map the apis to that particular group
3. If a particular user needs to be awarded access to some special apis then we can map the user to those apis (in the django admin)
4. At the start of project, we query the database once, and create an object that holds the queryset and the related fields. 
5. When the user is authenticated, a middleware will check if the authenticated user and the request path are available in the queryset object that we created at the start of project.


## SPECIAL THANKS TO: <br>
### willeM_ Van Onsem
