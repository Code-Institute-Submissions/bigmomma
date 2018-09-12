[![Build Status](https://travis-ci.org/90t/bigmomma.svg?branch=master)](https://travis-ci.org/90t/bigmomma)

#### Code Institute - Stream 3 Project
### by Clive Noonan
## What my Appliaction does and the needs it fulfils

# This Appliaction is a eCommerce SurfStore website. the concept of this idea came from a few days surfing in inchadoni. The website is needed for e-commerce, advertising and providing all the necessary information about the beauty salon. It provides details about treatments and prices, news and special offers, contact and location. It also provides an online store for buying beauty products.
The website has a customer registration/Login area. This is currently needed for purchasing products online and writing customer reviews. --The customer has a profile area where they can track the status of an order and view all past orders. -- It also contains all reviews made by the customer and the customer can edit or delete these reviews as they wish. Along with that the customer can also amend and update their username or email address.
The project also allows staff members to add, edit or delete news and special offer posts directly from the website once they are logged in.
-- All other admin can be done from the django admin panel.
Technologies used:
HTML - hypertext markup language
CSS - cascading style sheets
Javascript - client side scripting language
Python - Programming Language
Git Bash & GitHub -for version control and backup of code
Bootstrap - A framework for developing responsive, mobile first websites.
Django - python web framework
Libraries i needed to install
django forms bootstrap library for styling of forms
pillow needed for using images
ckeditor for rich text editing in creating and editing posts
Plugin - Coverage - I needed this during my testing of code. It generates reports which show you how much of your code you have tested.
Stripe - needed for online payment transactions for purchasing products
EmailJs - needed for the contact format
Gmail - needed for emails
Tiny Png - Used to optimise all photos used in the project https://tinypng.com/
Testing
I have outlined my testing in a seperate file testing.md - click here to view it
Problems encountered
I committed my env.py which held my private develpment envrionmet variables to GitHub. To solve the problem i deleted the env.py file from all my previous Git Commits and added the the env.py file to .gitignore for all future commits
git filter-branch --tree-filter 'rm env.py' HEAD
git push origin master --force
git for-each-ref --format='delete%(refname)'refs/original|git update-ref --stdin
git reflog expire --expire=now --all
git gc --prune=now
echo env.py >> .gitignore

I committed my SECRET KEY to GitHub. to solve this problem I generated a new SECRET_KEY using a SECRET KEY Generator I then added this new SECRET KEY to the env.py file -I deleted the old SECRET KEY from the settings.py file and added the following code to the settings.py file to point to the new SECRET KEY in the env.py file. SECRET_KEY = os.environ.get('SECRET_KEY')

Iterating a dictionary and trying to remove using .pop() method. I tried to iterate through my cart and pop/remove any items that had a 0 quantity value. Everytime the for loop poped/removed a value i would get a runtime error dictionary changed size during iteration. When i read up on this i discovered that you can not change a dictionary size during iteration. I came across an article QUORA Article and used there tip to change the dictionary to a list and then iterate and pop. This worked perfectly.

    for id, quantity in list(cart.items()):
            
        if quantity == 0:
            cart.pop(id)
The edit_profile view. When manually testing the view I discovered that you could change the username and email address to the same username or email address of other users. I had to add extra python code to the view to check that other users did not have the same username or email address as what the user wanted to change to.

When testing my checkout views.py. I could not test with my STRIPE_PUBLISHABLE key. It would return an error. After researching the Stripe documentation i came across the test card numbers and tokens. The token I needed for the card number i was using was tok_visa

References
Django Documentation helped me with all backend aspects of my project.
Thanks to Dalibor Nasevic's article which helped me with the commands to remove all env.py files from my git commit history.
I used the CKEDITOR documentation to give me a text editor and image uploader for my News & Special Offers content field.
QUORA Article This article helped me with the "RUNTIME ERROR dictionary changed size during iteration" I used their tip to change the dictionary to a list.
Max Goodridge's YouTube Video helped put me in the right direction with setting up editing the user profile by talking about the UserChangeForm.
Stripe Documentation - helped me with my stripe payments and testing


bigmommas

Django-2.1

(bigmomma_venv) clivenoonan:~/workspace (master) 
super
clivedennisnoona@gmail.com
thebigfree1




name;tom
user:tomas
email;tom@gmail.com
password:5689kjiutfg


If you want to have the reset password functionality in your Django project, you need to use the django.contrib.auth module.

Basically you need to import the following views (functions):

1.- password_reset

2.- password_reset_done

3.- password_reset_confirm

4.- password_reset_complete

For you to use these views in the perfect cushion urls.py file, you need to do the following:

1.- Import the re_path module (This is for us to some regular expressions in order to map the the views from the auth module).

from django.urls import path, include, re_path 

2.- Import the above mentioned views as this:

from django.contrib.auth import views as authViews 

Basically I am renaming the views as authViews.

Now for the views (I will call them by numbers), you will have to do this in the urls.py file. All these after the sign out url.

1.password_reset:

re_path(r'^account/password_reset/$', authViews.password_reset, {'template_name' : 'accounts/reset_password.html' }, name='password_reset'), 

This url will provide the password_reset form, so an email field will appear on the form so the user can put the email address and once the user has submitted the email, he/she will receive a reset password email.

Basically I am mapping a url (In this case, account/password_reset) and also I am making sure the URL DISPATCHER maps the password_reset view from the django.contrib.auth.views (Module views.py file). Also I have created a custom template and saved it at accounts folder that is at the shop->templates folder...You need to make sure this url maps the template as explained in above code and finally you put a name for the url (In this case, password_reset). 

2.- password_reset_done:

re_path(r'^account/password_reset/done/$', authViews.password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'), 

This url will inform the user that an email address has been sent so the user can click on a link to reset the password.

As explained on point one, we map the URL account/password_reset/done/, also a the password_reset_done view is mapped and a custom template is mapped as well (accounts/reset_password_done.html) and finally you put a name for the url password_reset_done.

3.- password_reset_confirm:

This URL will provide a change password form to the user so a new password can be typed in. But please keep in mind that that this url will use a regular expression so a token can be mapped and generated for the user (You don't want to change another users' passwords by mistake and this is the reason why a token is generated for a specific user).

re_path(r'^account/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', authViews.password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html'}, name='password_reset_confirm'), 

Same procedure or principle...A URL, a view and a custom template will be mapped.

4.- password_reset_complete:

re_path(r'^account/reset/done/$', authViews.password_reset_complete, {'template_name': 'accounts/reset_done.html'}, name='password_reset_complete'), 

This url will mapped a custom html template and a view to inform the user that the password has been changed or set so the user can sign in on the website again.

O.K. So far so good :-)

Now it is time to show you the content on the custom HTML templates (They have to be saved at shop->templates->accounts).