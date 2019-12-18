# Michael-Patterson.com
My personal website.

Built with Django and hosted with Heroku.


A list of technologies used include: 

* Postgres database.
* CKEditor for rich text editing in blog posts.
* highlight.js for displaying synax highlighted code snippets in blog posts.
* Bootstrap 4.
* django-todo app for bug tracking, project management, and personal to-dos.
* SendGrid for receiving contact emails.
* Set environment variables via an .env file to protect sensitive information.
* Use of template variables via view context to display unique information within a visited page.


A list of Django Apps which I've built include:

* A pages app to simply display static pages.
* A sendemail app which allows a user to send contact emails to me which are delivered via SendGrid. 
  I've also included the functionality to collect the email address, email subject, and email body from the form submission
  and store it all in the database.
* A blog app which features include:

  * User-end templates for creating, updating, and deleting posts.
  * A search form which allows users to search for terms within the blog and display a list of distinct posts.
  * A rich text editor via CKEditor which can be used in the user-end create and update templates, as well as in the admin backend.
  * The ability to select whether to publish a post or not. If unpublished the post will not be visible to anyone except the author.
    Also, a banner will display at the top of the post which clearly informs the author that the post is not published.
  * A post will display a "Created at" date and time as well as an "Updated at" date and time. 
    The "Updated at:" text will not be displayed when the post is created. Only when the post has actually been later updated 
    will it display "Updated at:" with it's respective date and time.