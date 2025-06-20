from django.db import models

class FBI_Agent(models.Model):
    name = models.CharField(max_length=100, verbose_name="探員姓名")
    badge_number = models.CharField(max_length=10, unique=True, verbose_name="徽章編號")
    join_year = models.IntegerField(verbose_name="入職年份")
    specialization = models.CharField(max_length=100, verbose_name="專長領域", blank=True)

    class Meta:
        verbose_name = "FBI探員"
        verbose_name_plural = "FBI探員"

    def __str__(self):
        return f"{self.name} ({self.badge_number})"

class Serial_Killer(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    alias = models.CharField(max_length=100, verbose_name="別名", blank=True)
    crime_period_start = models.IntegerField(verbose_name="犯罪開始年份")
    crime_period_end = models.IntegerField(verbose_name="犯罪結束年份")
    victim_count = models.IntegerField(verbose_name="受害人數量")
    description = models.TextField(verbose_name="犯罪描述", blank=True)

    class Meta:
        verbose_name = "連環殺手"
        verbose_name_plural = "連環殺手"

    def __str__(self):
        return f"{self.name} ({self.alias})" if self.alias else self.name

class Capture(models.Model):
    agent = models.ForeignKey(FBI_Agent, on_delete=models.CASCADE, verbose_name="負責探員")
    serial_killer = models.ForeignKey(Serial_Killer, on_delete=models.CASCADE, verbose_name="連環殺手")
    capture_date = models.DateField(verbose_name="捉拿日期")
    location = models.CharField(max_length=200, verbose_name="捉拿地點")
    details = models.TextField(verbose_name="捉拿詳情", blank=True)

    class Meta:
        verbose_name = "捉拿記錄"
        verbose_name_plural = "捉拿記錄"

    def __str__(self):
        return f"{self.serial_killer} 於 {self.capture_date} 在 {self.location} 被捕"