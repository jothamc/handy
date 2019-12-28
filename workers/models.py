from django.db import models
from user.models import HandyUser as User
from occupations.models import Occupation

# Create your models here.
class Worker(models.Model):
  # TODO: Define fields here
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  occupation = models.ManyToManyField(Occupation)
  years_of_experience = models.SmallIntegerField(default=0)
  phone = models.CharField(max_length=14,null=True)
  state = models.CharField(max_length=20,null=True) 
  city = models.CharField(max_length=20,null=True)
  home = models.CharField(max_length=150,null=True)
  work_email = models.EmailField(null=True)
  birth_date = models.DateField(null=True)
  image = models.ImageField(upload_to="workers")

  BANK_NAME = (
    ("ACC","Access Bank"),
    ("DIA","Diamond Bank"),
    ("ECO","Eco Bank"),
    ("FBN","First Bank"),
    ("FCM","First City Monument Bank"),
    ("GTB","Guaranty Trust Bank"),
    ("KEY","Keystone Bank"),
    ("POL","Polaris Bank"),
    ("STE","Sterling Bank"),
    ("UBA","United Bank for Africa"),
    ("UNI","Union Bank"),
    ("UNT","Unity Bank"),
    ("WEM","Wema Bank"),
    ("ZEN","Zenith Bank"),
  )
  bank_name = models.CharField(max_length=3,choices=BANK_NAME,null=True)
  bank_account_name = models.CharField(max_length=100,null=True)
  bank_account_number = models.CharField(max_length=10,null=True)
  bank_bvn = models.CharField(max_length=11,null=True)
  WORK_STATUS = (
  	("NW","Not Working"),
  	("CW","Currently Working"),
  	("AA","Awaiting Approval"),
  )
  ONLINE_STATUS = (
  	("OF","Offline"),
  	("BU","Busy"),
  	("ON","Online")
  )
  work_status = models.CharField(max_length=2,choices=WORK_STATUS)
  online_status = models.CharField(max_length=2,choices=ONLINE_STATUS)
  class Meta:
  	verbose_name = "Worker"
  	verbose_name_plural = "Workers"

  @property
  def address(self):
    home = self.home
    city = self.city
    state = self.state
    if self.home == None or len(self.home)<2:
      home = ""
    if self.city == None or len(self.city)<2:
      city = ""
    if self.state == None or len(self.state)<2:
      state = ""
    address = home +", "+ city +", "+ state
    if len(address) <5:
      return ""
    return address
  
  def __str__(self):
    return self.user.get_full_name()

  def get_absolute_url(self):
    return reverse("workers:detail",kwargs={username:self.user.username})
