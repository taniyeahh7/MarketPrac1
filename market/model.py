from market import db

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(length=30),nullable=False,unique=True)
    email_address=db.Column(db.String(length=50),nullable=False,unique=True)
    #not going to saving passwords as plain text making it vulnerable
    #need hashing algorithm
    password_hash=db.Column(db.String(length=60),nullable=False)#its okay if two people have the same password
    budget=db.Column(db.Integer(),nullable=False,default=1000)#want users to have some money at first
    items=db.relationship("Item",backref='owned_user',lazy=True)#sql wont grab all objects in one shot if not mentioned this here
    #items is not a column

class Item(db.Model):
    id=db.Column(db.Integer(),primary_key=True);#primary key and should always be there
    name=db.Column(db.String(length=30),nullable=False,unique=True);#to limit the number of characters ,value cannot be null and every entry must be unique
    price=db.Column(db.Integer(),nullable=False);#prices need not be unique
    barcode=db.Column(db.String(length=12),nullable=False,unique=True);#barcode wont be used anywhere therefore can just pass as string
    description=db.Column(db.String(length=1000),nullable=False,unique=True)
    #to let know that what ever follows will be put into a table later
    owner=db.Column(db.Integer(),db.ForeignKey('user.id'))#says foreignkey related to other models primary key
    def __repr__(self):
        return f'Item {self.name}'
