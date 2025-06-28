from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Musician(db.Model):
    """Model for storing musician information"""
    __tablename__ = 'musicians'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    instrument = db.Column(db.String(100), nullable=False)
    bio_es = db.Column(db.Text)
    bio_fr = db.Column(db.Text)
    bio_en = db.Column(db.Text)
    skills = db.Column(db.JSON)  # Store skills as JSON array
    image_url = db.Column(db.String(255))
    video_url = db.Column(db.String(255))
    position_order = db.Column(db.Integer, default=0)  # For ordering musicians
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Musician {self.name} - {self.instrument}>'


class ContactMessage(db.Model):
    """Model for storing contact form messages"""
    __tablename__ = 'contact_messages'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(2), default='es')  # Language used when submitting
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContactMessage from {self.email}>'


class Gallery(db.Model):
    """Model for storing photos and videos"""
    __tablename__ = 'gallery'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title_es = db.Column(db.String(200))
    title_fr = db.Column(db.String(200))
    title_en = db.Column(db.String(200))
    description_es = db.Column(db.Text)
    description_fr = db.Column(db.Text)
    description_en = db.Column(db.Text)
    media_type = db.Column(db.String(20), nullable=False)  # 'photo' or 'video'
    file_url = db.Column(db.String(255), nullable=False)
    thumbnail_url = db.Column(db.String(255))
    is_featured = db.Column(db.Boolean, default=False)
    position_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Gallery {self.media_type} - {self.title_es}>'


class Event(db.Model):
    """Model for storing upcoming events and performances"""
    __tablename__ = 'events'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title_es = db.Column(db.String(200), nullable=False)
    title_fr = db.Column(db.String(200))
    title_en = db.Column(db.String(200))
    description_es = db.Column(db.Text)
    description_fr = db.Column(db.Text)
    description_en = db.Column(db.Text)
    venue = db.Column(db.String(200))
    address = db.Column(db.String(300))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))
    event_date = db.Column(db.DateTime, nullable=False)
    ticket_url = db.Column(db.String(255))
    is_published = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Event {self.title_es} - {self.event_date}>'


class SiteSettings(db.Model):
    """Model for storing site-wide settings and content"""
    __tablename__ = 'site_settings'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value_es = db.Column(db.Text)
    value_fr = db.Column(db.Text)
    value_en = db.Column(db.Text)
    setting_type = db.Column(db.String(50), default='text')  # text, html, json, boolean
    is_active = db.Column(db.Boolean, default=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<SiteSetting {self.key}>'