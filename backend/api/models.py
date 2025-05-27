from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

# TODO: Add this for when I want an `owner` field in StampCard
# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User,
#         related_name="user_profile",
#         on_delete=models.CASCADE,
#     )


class StampCard(models.Model):
    title = models.CharField(max_length=100)
    stamps_needed = models.PositiveIntegerField(default=10)
    date_created = models.DateTimeField(auto_now_add=True)
    is_removed = models.BooleanField(default=False)
    is_redeemed = models.BooleanField(default=False)

    class Meta:
        db_table = "stampcard"

    def __str__(self):
        return self.title

    @property
    def total_stamps(self):
        return self.entries.count()

    @property
    def stamps_collected(self):
        return self.entries.filter(is_active=True).count()


class StampEntry(models.Model):
    stamp_card = models.ForeignKey(
        StampCard,
        on_delete=models.CASCADE,
        related_name='entries',
    )
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)  # Toggle for active/inactive stamp
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "stampentry"

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"StampEntry for {self.stamp_card.title} on {self.date_created} ({status})"

