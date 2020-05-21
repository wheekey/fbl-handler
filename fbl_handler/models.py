from django.db import models
from datetime import datetime

class Message(models.Model):
    message_id = models.CharField(max_length=20, db_index=True)
    email = models.CharField(max_length=20, default='')
    is_unsubscribed = models.BooleanField(default=False)
    pub_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.email