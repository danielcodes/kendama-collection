# Kendama List Application

This application will display kendamas in a Instagram like grid view.

Primarily starting this app to work with WTForms

## User stories

* [x] The main page displays a 3 column grid that displays pictures of kendamas
* [x] Under the image, there is a header with the name and a table with further description, brand, link to buy
* [x] There is a form, that allows me to add a name and link to the kendama picture
* [x] Kendamas can be deleted through a button (individually)
* [ ] There is a tab with instagram tab with the #kendama filter to see kendama posts

## TODOS

* Work on edit feature, pop up a modal and do a PUT request that update an item in the database
* Start looking into Instagram's API 
* Page needs some redesign now that it is functional
* Replace images with shots of your own
* Handle error in a better manner, making sure form is completed, etc

## Things I have learned

* using text-center and center-block, to center text and images with bootstrap
* had this problem before where images become pixelated, resize images to 600x350 for a good fit
* how to use pinta, use rectangle select, go to image up top and click crop to selection
* using ajax to do a POST request, thanks to this article http://stackoverflow.com/questions/14908864/how-can-i-use-data-posted-from-ajax-in-flask
* removing an image from the file system, 3 steps, cd into dir, check if image is there, delete it and change back to original dir path

## Notes

* http://statusq.org/archives/2014/10/25/6161/ to set up Bower with Flask
* https://github.com/BlackrockDigital/startbootstrap-3-col-portfolio 3 column instagram looking page
* https://flask-wtf.readthedocs.org/en/latest/quickstart.html 
* https://wtforms.readthedocs.org/en/latest/crash_course.html

