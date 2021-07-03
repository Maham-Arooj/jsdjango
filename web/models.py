from django.db import models

from django.utils import timezone
today = timezone.now

class Employee(models.Model):
    Name = models.CharField(max_length=30)
    job_name = models.CharField(max_length=30)
    Hiring_date=models.CharField(max_length=30)
    Employement_year= models.CharField(max_length=30)
    Salary= models.CharField(max_length=30)
    Bonus= models.CharField(max_length=30)
    Account_number= models.CharField(max_length=30)
    Growth= models.CharField(max_length=30)
    Duty_Start_time= models.CharField(max_length=30)
    Duty_End_time=models.CharField(max_length=30)
    Total_hours= models.CharField(max_length=30)
    leaves_allows= models.CharField(max_length=30)
    Description= models.CharField(max_length=30)
    Remarks= models.CharField(max_length=30)
    Date_Time= models.DateTimeField(default=today)

    def __str__(self):
        return self.Name

class Personal_Data(models.Model):
    Father_name = models.CharField(max_length=30)
    CNIC = models.CharField(max_length=30)
    Age= models.CharField(max_length=2)
    Address= models.CharField(max_length=30)
    City= models.CharField(max_length=30)
    Country= models.CharField(max_length=30)
    Gender= models.CharField(max_length=30)
    Material_Status= models.CharField(max_length=30)
    Employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.CNIC

class Qualification(models.Model):
    Degree = models.CharField(max_length=30)
    Years_of_Passing = models.CharField(max_length=30)
    Category= models.CharField(max_length=30)
    Institute= models.CharField(max_length=30)
    Total_Marks= models.CharField(max_length=30)
    Obtain_Marks= models.CharField(max_length=30)
    Grade= models.CharField(max_length=30)
    Date_Time= models.DateTimeField(default=today)
    Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.Years_of_Passing


class Previous_Experience(models.Model):
    Previous_Organization = models.CharField(max_length=30)
    Job_Name = models.CharField(max_length=30)
    Description= models.CharField(max_length=30)
    Duty_Start_time= models.TimeField((""), auto_now=False, auto_now_add=False)
    Duty_End_time= models.TimeField((""), auto_now=False, auto_now_add=False)
    Date_Time= models.DateTimeField(default=today)
    Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.Job_Name


class Skills(models.Model):
    Skill_name = models.CharField(max_length=30)
    Organization = models.CharField(max_length=30)
    Certification= models.CharField(max_length=30)
    Duty_Start_time= models.TimeField((""), auto_now=False, auto_now_add=False)
    Duty_End_time= models.TimeField((""), auto_now=False, auto_now_add=False)
    Date_Time= models.DateTimeField(default=today)
    Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.Skill_name

class Contact_Detail(models.Model):
    LandLine_Number = models.CharField(max_length=30)
    Mobile_Number1 = models.CharField(max_length=30)
    Mobile_Number2 = models.CharField(max_length=30)
    Email= models.EmailField()
    Date_Time= models.DateTimeField(default=today)
    Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return self.Email

class Product_Category(models.Model):
    Product_Name = models.CharField(max_length=30)
    Product_type = models.CharField(max_length=30)
    Description= models.CharField(max_length=30)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Product_Name

class Supplier(models.Model):
    Name = models.CharField(max_length=30)
    Organization_Name = models.CharField(max_length=30)
    ISO_Certification = models.CharField(max_length=30)
    Address= models.CharField(max_length=30)
    City= models.CharField(max_length=30)
    Country= models.CharField(max_length=30)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Name

class Product_Type(models.Model):
    Name = models.CharField(max_length=30)
    Size_Available = models.CharField(max_length=30)
    Color_Available= models.CharField(max_length=30)
    Description= models.CharField(max_length=30)
    Product_Category=models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    Supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=30)
    Quality = models.CharField(max_length=30)
    Unit_Price= models.CharField(max_length=30)
    Size= models.CharField(max_length=30)
    Color= models.CharField(max_length=30)
    Division= models.CharField(max_length=30)
    Description= models.CharField(max_length=30)
    Re_Order_Level= models.CharField(max_length=30)
    Product_Category=models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    Supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Product_Type=models.ForeignKey(Product_Type, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Name

class S_Order_Booking(models.Model):
    Invoice_Number = models.CharField(max_length=30)
    Total_Bill= models.CharField(max_length=30)
    Supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Invoice_Number

class S_Order_Detail(models.Model):
    
    Quantity= models.CharField(max_length=30)
    Unit_Price= models.CharField(max_length=30)
    Bulk_Price = models.CharField(max_length=30)
    Packing_Details = models.CharField(max_length=30)
    Supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Product=models.ForeignKey(Product, on_delete=models.CASCADE)
    S_Order_Booking=models.ForeignKey(S_Order_Booking, on_delete=models.CASCADE)
    Unit_sales_Price= models.CharField(max_length=30)
    Bulk_sales_Price = models.CharField(max_length=30)
    Discount= models.CharField(max_length=30)
    def __str__(self):
        return self.Quantity

class S_Payment(models.Model):
    Payment_Medium= models.CharField(max_length=30)
    Payment_Amount= models.CharField(max_length=30)
    S_Order_Booking=models.ForeignKey(S_Order_Booking, on_delete=models.CASCADE)
    Employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)

    def __str__(self):
        return self.Payment_Amount

class S_Contact_Detail(models.Model):
    Toll_free_Number= models.CharField(max_length=30)
    LandLine_Number = models.CharField(max_length=30)
    Mobile_Number1 = models.CharField(max_length=30)
    Mobile_Number2 = models.CharField(max_length=30)
    Postal_Code= models.CharField(max_length=10)
    Email= models.EmailField()
    Supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Email

class S_Contact_Person(models.Model):
    Name= models.CharField(max_length=30)
    Mobile_Number1 = models.CharField(max_length=30)
    Mobile_Number2 = models.CharField(max_length=30)
    Email= models.EmailField()
    Supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Name

class Customer(models.Model):
    Name= models.CharField(max_length=30)
    CNIC = models.CharField(max_length=30)
    Mobile_Number = models.CharField(max_length=30)
    Whatsapp_Number = models.CharField(max_length=30)
    Email= models.EmailField()
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Name
    

class Corderbooking(models.Model):
    Invoice_Number = models.CharField(max_length=30)
    Customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Invoice_Number

class corderdetail(models.Model):
    Quantity= models.CharField(max_length=30)
    Price= models.CharField(max_length=30)
    Product=models.ForeignKey(Product, on_delete=models.CASCADE)
    Corderbooking=models.ForeignKey(Corderbooking, on_delete=models.CASCADE)
    Sales_Price= models.CharField(max_length=30)
    Purchase_Price= models.CharField(max_length=30)
    Discount= models.CharField(max_length=30)
    def __str__(self):
        return self.Sales_Price

class C_Payment(models.Model):
    Payment_Amount= models.CharField(max_length=30)
    Payment_Medium = models.CharField(max_length=30)
    Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    Corderbooking= models.ForeignKey(Corderbooking, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Payment_Amount

class Daily_Expense(models.Model):
    Expenditure_Type= models.CharField(max_length=30)
    Amount= models.CharField(max_length=30)
    Discription = models.CharField(max_length=300)
    Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Expenditure_Type

class Current_Stock(models.Model):
    Unit_Price= models.CharField(max_length=30)
    Number_of_Current_Items = models.CharField(max_length=30)
    SKU = models.CharField(max_length=30)
    Employee= models.ForeignKey(Employee, on_delete=models.CASCADE)
    Product= models.ForeignKey(Product, on_delete=models.CASCADE)
    Date_Time= models.DateTimeField(default=today)
    def __str__(self):
        return self.Unit_Price

class productimg(models.Model):
    product_image= models.ImageField(upload_to='images')
    name= models.CharField(max_length=100) 
    price= models.IntegerField(default=0)
    def __str__(self):
        return self.name

class images(models.Model):
    product_image= models.ImageField(upload_to='images')
    product_text= models.CharField(max_length=30)
    def __str__(self):
        return self.product_text

class Contact(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=254)    
    subject= models.CharField(max_length=30)
    message= models.TextField(max_length=254)
    def __str__(self):
        return self.name
        
class Comment(models.Model):
    name= models.CharField(max_length=30)
    email= models.EmailField(max_length=254)    
    message= models.TextField(max_length=254)
    def __str__(self):
        return self.name

class indeximg(models.Model):
    product_image= models.ImageField(upload_to='images')
    product_text= models.CharField(max_length=30)
    def __str__(self):
        return self.product_text




