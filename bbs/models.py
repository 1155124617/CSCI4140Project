from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Client(models.Model):
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    grade = models.IntegerField()
    major = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Admin(models.Model):
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)
    borrower_id = models.IntegerField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class Transfer(models.Model):
    transfer_time = models.DateTimeField()
    borrower_id = models.IntegerField()
    lender_id = models.IntegerField()
    book_id = models.IntegerField()
    img = models.ImageField(upload_to="images")
    borrower_confirm = models.BooleanField(default=False)
    lender_confirm = models.BooleanField(default=False)


class TransferRequest(models.Model):
    borrower_id = models.IntegerField()
    book_name = models.CharField(max_length=30)
    request_time = models.DateTimeField()
    location = models.CharField(max_length=50)
    message = models.CharField(max_length=100)


class Reservation(models.Model):
    borrower_id = models.IntegerField()
    book_name = models.CharField(max_length=30)
    is_book_valid = models.BooleanField(default=False)
    book_id = models.IntegerField(null=True)
    location = models.CharField(max_length=50, null=True)
    valid_date = models.DateField(null=True)
    is_finished = models.BooleanField(default=False)