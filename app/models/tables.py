from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username


class Vagas(db.Model):
   __tablename__ = 'vagas'
   id = db.Column(db.Integer, primary_key=True)
   subject = db.Column(db.String(120), nullable=False)
   task = db.Column(db.String(120), nullable=False)
   area = db.Column(db.String(20), nullable=False)
   place = db.Column(db.String(120), nullable=False)
   city = db.Column(db.String(100), nullable=False)
   state = db.Column(db.String(10), nullable=False)
   wage = db.Column(db.String(30), nullable=False)
   company = db.Column(db.String(150), nullable=False)
   description = db.Column(db.Text, nullable=False)
   assignment = db.Column(db.Text, nullable=False)
   url = db.Column(db.Text, nullable=False)


   def __init__(self, subject, task, area, place, city, state, wage, company, description, assignment, url):
        self.subject = subject
        self.task = task
        self.area = area
        self.place = place
        self.city = city
        self.state= state
        self.wage = wage
        self.company = company
        self.description = description
        self.assignment = assignment
        self.url = url


        def __repr__(self):
            return '<Vagas %r' % self.id 