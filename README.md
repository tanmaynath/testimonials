# testimonials
Backend for testimonial site

# When running for the first time:
python manage.py makemigrations
python manage.py migrate

# To run the app
python manage.py runserver

# To run the tests:
python manage.py test

# API endpoint:
"Lists all posts. Can be used for GET/POST"
http://127.0.0.1:8000/v1/api/testimonials/

# Admin site:
http://127.0.0.1:8000/admin/posts/

# Make post:
http://127.0.0.1:8000/

# Admin credentials:
tanmaynath
ageofspin



# For nginx 
brew install nginx

# Create a symlink for nginx config in nginx server directory
ln -s /path/to/testimonial.conf /usr/local/etc/nginx/servers/

Make sure to update paths in the config files:
-testimonial.conf (nginx)
-testimonials.ini (uwsgi)
