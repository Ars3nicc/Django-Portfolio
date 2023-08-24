from django.db import models
from datetime import date

class ToolStacks(models.Model):
    stackid = models.AutoField(primary_key=True)
    teck_stacks = models.CharField(max_length=50, verbose_name='Tech Stacks')
    design_stacks = models.CharField(max_length=50, verbose_name='Design Stacks')
    documentation_stacks = models.CharField(max_length=50, verbose_name='Documentation Stacks')
    
    def __str__(self):  
        return self.stackid
    

