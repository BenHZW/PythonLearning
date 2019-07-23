from django.db import models


class New(models.Model):
    id = models.IntegerField(primary_key=True)
    artid = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    pubtime = models.CharField(max_length=255)
    content = models.TextField()
    detailcontent = models.TextField()
    arttype = models.CharField(max_length=255)


    class Meta:
        db_table = 'news'  # 指明数据库表名
        verbose_name = '新闻'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name