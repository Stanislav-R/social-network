# Test task for StarNavi

###Deploy:

For deployment to your PC use next steps:
1. Clone repo: https://github.com/Stanislav-R/social-network.git
2. Create virtualenv and activate it:
   - python3 -m venv venv
   - venv/bin/activate
3. Install all source packages: pip install -r requirements.txt
4. Make migration: python manage.py migrate
5. Run application: python manage.py runserver
6. Application will be available at: http://127.0.0.1:8000/

###Available api's:

1. Users:
   - /api/users/
     - /register
     - /login
     - /user
     - /logout
2. Posts:
   - /api/posts/
     - /posts_list (CRUD)
     - /likes_list (CRUD)
3. Analytics:
   - /users/activity (Last login & last request)
   - /posts/analytics (Count of likes)