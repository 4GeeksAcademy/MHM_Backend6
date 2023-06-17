from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
# class JournalEntries (db.Model):
#   __tablename__ = 'journal_entries'
#   entry_id = db.Column(db.Integer, primary_key=True)
#   user_id = db.Column(db.Integer)
#   date = db.Column(db.Date, nullable=False)
#   mood = db.Column(db.String(255))
#   content = db.Column(db.Text)

#   def __repr__(self):
#     return f'<JournalEntries {self.date}>'

#   def serialize(self):
#     return {
#       "entry_id": self.entry_id,
#       "user_id": self.user_id,
#       "date": self.date,
#       "mood": self.mood,
#       "content": self.content,
#       "user": self.user
#     }
  
# class MentalHealthResources (db.Model):
#   __tablename__ = 'mental_health_resources'
#   resource_id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(255), nullable=False)
#   description = db.Column(db.Text)
#   type = db.Column(db.String(255))
#   url = db.Column(db.String(255))

#   def __repr__(self):
#     return f'<MentalHealthResources {self.resource}>'

#   def serialize(self):
#     return {
#       "resource_id": self.resource_id,
#       "title": self.title,
#       "description": self.description,
#       "type": self.type,
#       "url": self.url,
#     }
  
# class MeditationSessions (db.Model):
#   __tablename__ = 'meditation_sessions'
#   session_id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(255), nullable=False)
#   duration = db.Column(db.Integer)
#   style = db.Column(db.String(255))
#   theme = db.Column(db.String(255))
#   youtube_url = db.Column(db.String(255))

#   def __repr__(self):
#     return f'<MeditationSessions {self.title}>'

#   def serialize(self):
#     return {
#       "session_id": self.session_id,
#       "title": self.title,
#       "duration": self.duration,
#       "style": self.style,
#       "theme": self.theme,
#       "youtube_url": self.youtube_url
#     }
  
# class SupportGroups (db.Model):
#   __tablename__ = 'support_groups'
#   group_id  = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(255), nullable=False)
#   description = db.Column(db.Text)
#   meeting_link = db.Column(db.String(255))

#   def __repr__(self):
#     return f'<SupportGroups {self.title}>'

#   def serialize(self):
#     return {
#       "group_id": self.group_id,
#       "title": self.title,
#       "description": self.description,
#       "meeting_link": self.meeting_link,
#       "theme": self.theme
#     }
  
#   class Notifications (db.Model):
#     __tablename__ = 'notifications'
#     notification_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, nullable=False)
#     type = db.Column(db.String(255))
#     content = db.Column(db.Text)

#     def __repr__(self):
#       return f'<Notifications {self.content}>'

#     def serialize(self):
#       return {
#         "notification_id": self.notification_id,
#         "user_id": self.user_id,
#         "type": self.type,
#         "content": self.content,
#         "user": self.user
#       }