from django.db import models


class Paperboy(models.Model):
    name = models.CharField(max_length=100, blank=False)
    experience = models.IntegerField(default=0, blank=False)
    earnings = models.PositiveIntegerField(default=0, blank=False)
    quota = models.PositiveIntegerField(default=50, blank=False)

    def __str__(self):
        return f"{self.name} - {self.earnings}"

    @classmethod
    def total_delivered(cls):
        total_delivered = cls.objects.all().aggregate(models.Sum("experience"))
        return total_delivered["experience__sum"]

    @classmethod
    def total_earned(cls):
        total_earned = cls.objects.all().aggregate(models.Sum("earnings"))
        return total_earned["earnings__sum"]

    def increase_quota(self):
        self.quota = self.earnings / 2
        # self.save()

    def deliver(self, start_address, end_address):
        papers_delivered = abs(end_address - start_address)
        self.experience += papers_delivered
        # self.save()

        if papers_delivered < self.quota:
            self.earnings -= 2
            # self.save()

            for paper in range(papers_delivered):
                self.earnings += 0.25
                # self.save()
            self.increase_quota()

        elif papers_delivered >= self.quota:
            for paper in range(papers_delivered):
                self.earnings += 0.25
                # self.save()
            for paper in range(papers_delivered - self.quota):
                self.earnings += 0.25
                # self.save()
            self.increase_quota()
