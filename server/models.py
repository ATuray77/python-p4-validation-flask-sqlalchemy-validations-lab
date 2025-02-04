from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("name")
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise ValueError("Author name must be a string")
        if not name:
            raise ValueError("No author name provided")
        return name

    @validates("phone_number")
    def validate_phone_number(self, key, phone_number):
        if not phone_number.isdigit():
            raise ValueError('Phone number must contain only digits')
        if len(phone_number) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
    
    


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("content")
    def validate_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Post content must be at least 250 characters")
        return content
    
    @validates("summary")
    def validate_summary(self, key, summary):
        if len(summary) <= 250:
            raise ValueError("Post summary must not be above 250 characters")
        return summary
    
    @validates("category")
    def validate_category(self, key, category):
        if category != "Fiction" and category != "Non-Fiction":
            raise ValueError("Category must be be either Fiction or Non-Fiction")
    
    @validates('title')
    def validate_title(self, key, title):
        clickbait_phrases = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(phrase in title for phrase in clickbait_phrases):
            raise ValueError("Title must be clickbait-y")
        return title
    
    # @validates("title")
    # def validate_title(self, key, title):
    #     if title not in:
    #         raise ValueError("All post must have a title")
    
    # @validates('title')
    # def validate_title(self, key, title):
    #     clickbait_phrases = ['', 'shocking', 'incredible']
    #     if title.endswith("?") or any(phrase in title.lower() for phrase in clickbait_phrases):
    #         raise ValueError("Title can't be clickbait")
    #     return title

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
