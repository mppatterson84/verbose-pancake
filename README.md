# Michael-Patterson.com
My personal website.

Built with Django and hosted with Heroku.


A list of technologies used include: 

* Postgres database.
* CKEditor for rich text editing in blog posts.
* highlight.js for displaying synax highlighted code snippets in blog posts.
* Bootstrap 4.
* SendGrid for receiving contact emails.
* Set environment variables via an .env file to protect sensitive information.
* Use of template variables via view context to display unique information within a visited page.


A list of Django Apps which I've built include:

* A pages app to simply display static pages.
* A sendemail app that allows a user to send contact emails to me which are delivered via SendGrid. 
  I've also included the functionality to collect the email address, email subject, email body, and created at date and time. When the form is submitted, the email is sent and all the information is saved to the database.
* A blog app which features include:

  * User-end templates for creating, updating, and deleting posts.
  * A search form which allows users to search for terms within the blog and display a list of distinct posts.
  * A rich text editor via CKEditor which can be used in the user-end create and update templates, as well as in the admin backend.
  * The ability to select whether to publish a post or not. If unpublished the post will not be visible to anyone except the author.
    Also, a banner will display at the top of the post which clearly informs the author that the post is not published.
  * A post will display a "Created at" date and time as well as an "Updated at" date and time. 
    The "Updated at:" text will not be displayed when the post is created. Only when the post has been later updated 
    will it display "Updated at:" with it's respective date and time.
  * The ability to create post categories and tag a post with any number of categories. Post categories are created with their own
    model and linked to the post model with a many-to-many field.
