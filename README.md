# Stores
Simple store app created with Django and PostgreSQL.


## Table of Contents
* [Introduction](#introduction)
* [Functionality](#functionality-with-screenshots)
* [Technologies](#technologies)
* [Status](#Status)

## Introduction
Simple app showing stores registered - for each store: 
- its products by category
- location of the store on map
###### Application created with knowledge gained through Python Web course.


## Functionality with screenshots
### If there is no store added:
![not_logged_no_store](https://user-images.githubusercontent.com/48320090/153177899-ff856002-7851-4261-9d19-80c882e1d11f.png)

### If not authenticated user tries to add/change something:
![not_logged_add_sth](https://user-images.githubusercontent.com/48320090/153178575-59f8b930-6852-45e1-b48e-f4c25466ebd4.png)

### If not authenticated, but there is store one can only READ index page:
![not_logged_in_store](https://user-images.githubusercontent.com/48320090/153179134-698a77e9-b06a-408d-a72e-17f8ea620596.png)

### If authorized is able to update store:
![logged_in_store_owner](https://user-images.githubusercontent.com/48320090/153180217-c009162d-2746-484e-8e8b-2ed48b6de6bb.png)

### If authenticated but not authorized, not able to update:
![logged_in_store_not_owner](https://user-images.githubusercontent.com/48320090/153180458-93ce5d4d-5a38-4a60-a7b6-d099e4ea0bd0.png)

### If authenticated /private pages/:
* able to add store/category/product etc.
![logged_in_add_sth](https://user-images.githubusercontent.com/48320090/153180924-069f2bde-6634-465f-8ccd-a22067b3597e.png)
* if user profile not completed - there is notification, showing on each page:
![profile_not_completed](https://user-images.githubusercontent.com/48320090/153181795-6acf3ef1-363b-4779-b739-5864cc6b48d1.png)
* when user profile is completed - notification does not appear:
![logged_in_add_sth](https://user-images.githubusercontent.com/48320090/153182113-5025daaa-fb2a-41c1-bca9-2e33381bffcf.png)
* able to add products from category list to purchase - if user has enough budget:
![logged_in_show_category](https://user-images.githubusercontent.com/48320090/153182685-54b3fe92-9434-401a-b5ef-1de119928cda.png)
* not able to add products from category list to purchase - if user has not enough budget:
![logged_in_budget_not_enough](https://user-images.githubusercontent.com/48320090/153182896-4ba53452-2820-4d17-9df8-3582ba0ca43c.png)
* one is able to 'purchase' order:
![logged_in_order_not_sent](https://user-images.githubusercontent.com/48320090/153183348-f2884e3f-45a3-4c99-a096-f95cd113e624.png)
* when order is 'purchased':
![logged_in_order_sent](https://user-images.githubusercontent.com/48320090/153183640-6329605f-8241-4cc2-818f-7032d51622b2.png)
* edit user profile/same as user profile not completed:
![logged_in_edit_profile](https://user-images.githubusercontent.com/48320090/153184001-9a0d56e2-21f0-488b-acd8-fb4389621769.png)

### Other public pages:
* Bottom of the index page:
![logged_in_store_bottom](https://user-images.githubusercontent.com/48320090/153184487-2e21e001-5b75-4535-95c4-1554afd1ea75.png)
* Location of the store on the map:
![store_location](https://user-images.githubusercontent.com/48320090/153184608-3cfeb0f8-70e8-4e5a-86b4-520493279be0.png)



## Technologies
* Python 3.7
* Django 3.2
* PostgreSQL 
* Pillow
* Bootstrap 4 and 5
* Folium
* Geocoder

## Status
### Todo:
* Replace FBV with CBV
* Add tests
