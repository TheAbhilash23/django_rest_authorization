# Django Rest Permissions for Authorization
## In this project we are looking to make authorization a smooth and easy to configure process.


### FLOW
#### 1. Using scan_and_make_authorization_routes method the action methods are created in model ActionMethod for all routes that start with the one specified in the app_settings 
#### 2. Once the routes are created rest_groups can be created to map the apis to that particular group
#### 3. If a particular user needs to be awarded access to some special apis then we can map the user to those apis (in the django admin)
#### 4. At the start of project, we query the database once, and create an object that holds the queryset and the related fields. 
#### 5. When the user is authenticated, a middleware will check if the authenticated user and the request path are available in the queryset object that we created at the start of project.


### OPEN TASKS
#### 1. Currently all request paths are being processed, however it should be processed for only those routes whose parent is mentioned in the app_settings. <span style="color: green;">&#10004;</span>
#### 2. Handle Permission error in API response directly from middleware without reaching view. <span style="color: green;">&#10004;</span>
#### 3. Currently the permissions queryset is cached in the memory at the start of project and any change in the permissions will reflect on the next restart, therefore need to use post_save signal to reset the value

```
SPECIAL THANKS TO:

willeM_ Van Onsem
```
