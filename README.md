"# Workshop_1" 


I have created a custom user model where users can sign with their emails instead of username.

Using signals a profile is being created for each register user and later on they can complete the profile information.

Users can login with their email and password directly.

I have used template inheritance and different CRUD operations for the models. CRUD operations are concentrated on the Animal model. 
Each animal has its details which are shown (type, is it a mammal, photo) and to each animal can be added more photos which are stored in a different model and connected using PK.

There is a big use of media and static files. Each user and anima can have a picture which is uploaded using CRUD operations.

The project is completely function based.

I have used some templatetags to load information on different templates and custom filters that are mostly applied in the animals list template just for test purposes.
