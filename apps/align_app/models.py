from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASSWORD_REGEX = re.compile(r'(^[A-Za-z0-9@#$%^&+=]+$)')

class UserManager(models.Manager):

    def basic_validator(self, postData, isCreate):
        errors = {}

        if len(postData["email"]) < 5:
            errors["email_length"] = "Email must be at least 5 characters long"

        elif not EMAIL_REGEX.match(postData["email"]):
            errors["email_valid"] = "Must be a valid email"
        
        if isCreate == True:

            if len(postData["username"]) < 2:
                errors["username"] = "Username must be at least 2 characters long"

            user = User.objects.filter(email=postData["email"])
            if len(user):
                errors["email"] = "User already exists"

            if len(postData["password"]) < 8:
                errors["password_length"] = "Password must be at least 8 chars"

            elif postData["password"] != postData["confirm"]:
                errors["password_match"] = "Passwords must match"

        else:

            if len(User.objects.filter(email=postData["email"])) == 0:
                errors["no_user"] = "Login failed"
            
            else:
                user = User.objects.get(email=postData["email"])
                encoded_pw = user.password.encode()

                if bcrypt.hashpw(postData["password"].encode(), user.password.encode()) != encoded_pw:
                    errors["pw_fail"] = "Login failed"

        return errors

class User(models.Model):

    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    sun_sign = models.CharField(max_length=45)
    moon_sign = models.CharField(max_length=45)
    rising_sign = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __repr__(self):
        return "<User: {} {}>".format(self.id, self.first_name)

class Message(models.Model):

    user = models.ForeignKey(User, related_name="messages_posted")
    recipient = models.ForeignKey(User, related_name="messages_received")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):

    message = models.ForeignKey(Message, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



