from django.db import models
from django.utils import timezone
from django.conf import settings
from apis.mail import send_mail
from apis.sms import send_sms

class Post(models.Model):
    author = models.ForeignKey( settings.AUTH_USER_MODEL )
    title = models.CharField( max_length=50 )
    text = models.TextField()
    created_date = models.DateTimeField( auto_now_add = True )
    published_date = models.DateTimeField( null=True, blank=True )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

        print(self.post.author.email)

        recipient_list = [self.post.author.email]
        send_mail('댓글이 달렸습니다.', '확인해보세요', recipient_list)

        print(self.post.author.phone)

        send_sms(self.post.author.phone, '댓글이 달렸습니다.\n확인해보세요.')





