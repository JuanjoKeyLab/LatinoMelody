# Latinouch Musical Project

## Overview

Latinouch is a multilingual musical project website built with Flask and PostgreSQL, featuring a modern and responsive design. The application serves as a landing page for a musical group, showcasing musicians and providing contact information. The site supports three languages (Spanish, French, English) with a vibrant orange and red color scheme, targeting international audiences.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **CSS Framework**: Bootstrap 5 for responsive grid system and components
- **Custom Styling**: CSS3 with custom properties for consistent theming
- **JavaScript**: Vanilla JavaScript for interactive features
- **Icons**: Font Awesome 6.4.0 for iconography
- **Fonts**: Google Fonts (Poppins family)
- **Internationalization**: Multi-language support with flag-based language selector

### Backend Architecture
- **Framework**: Flask (Python microframework)
- **Database**: PostgreSQL with Flask-SQLAlchemy ORM
- **Server**: Gunicorn WSGI server for production deployment
- **Session Management**: Flask sessions with configurable secret key
- **Environment Configuration**: Environment variables for sensitive data

## Key Components

### Application Structure
- **app.py**: Main Flask application with route definitions
- **main.py**: Application entry point for deployment
- **templates/**: Jinja2 HTML templates
- **static/**: Static assets (CSS, JavaScript, images)

### Frontend Components
- **Navigation**: Fixed-top responsive navbar with smooth scrolling
- **Hero Section**: Landing area with overlay effects
- **Responsive Design**: Mobile-first approach with Bootstrap grid
- **Interactive Elements**: Scroll animations and parallax effects

### Styling System
- **CSS Variables**: Centralized color scheme management
- **Gradient System**: Multiple gradient combinations for visual appeal
- **Typography**: Poppins font family with multiple weights
- **Color Palette**: Orange-to-red gradient theme with dark backgrounds

## Database Schema

### Core Models
- **Musicians**: Stores musician profiles with multilingual bios, skills, and positioning
- **ContactMessage**: Handles contact form submissions with language tracking
- **Gallery**: Manages photos and videos with multilingual metadata
- **Event**: Stores upcoming performances and concerts
- **SiteSettings**: Configurable site-wide content and settings

### Data Flow

1. **Request Handling**: Flask receives HTTP requests with language routing (/, /es, /fr, /en)
2. **Database Integration**: SQLAlchemy queries PostgreSQL for dynamic content
3. **Language Processing**: Content served based on URL language parameter with fallbacks
4. **Template Rendering**: Jinja2 processes HTML templates with database and static content
5. **Static Asset Serving**: Flask serves CSS, JavaScript, and other static files
6. **Client-Side Interactions**: JavaScript handles navigation, animations, and user interactions

## External Dependencies

### CDN Resources
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Font Awesome 6.4.0**: Icon library for UI elements
- **Google Fonts**: Poppins font family for typography

### Python Dependencies
- **Flask**: Web framework for Python
- **Flask-SQLAlchemy**: Database ORM for PostgreSQL integration
- **psycopg2-binary**: PostgreSQL adapter for Python
- **Gunicorn**: WSGI HTTP server for production deployment
- **Standard Library**: OS, datetime, uuid modules

## Deployment Strategy

### Development Environment
- **Host**: 0.0.0.0 (accepts connections from any IP)
- **Port**: 5000 (standard Flask development port)
- **Debug Mode**: Enabled for development with auto-reload
- **Session Security**: Environment-based secret key with fallback

### Configuration Management
- **Environment Variables**: SESSION_SECRET for production security
- **Fallback Values**: Development defaults for local testing

## User Preferences

Preferred communication style: Simple, everyday language.

## Recent Changes

- **June 28, 2025 - Brand Name Correction**: Corrected all references from "LAtinouch" to "Latinouch" throughout the entire application including templates, CSS comments, content dictionaries, and documentation files.
- **June 28, 2025 - Language Selector Enhancement**: Fixed flag visibility in full-screen mode with improved contrast and positioning. Flags now display without text labels and are positioned left of the mobile menu button.
- **June 28, 2025 - Mobile Menu Improvements**: Added auto-close functionality when clicking outside the menu or on navigation links. Reduced menu content size for better mobile experience.
- **June 28, 2025 - Presentations Section**: Added new "Presentaciones/Concerts/Performances" section with 5 video presentation cards. Each card includes video placeholder, concert description, date, and location details. Implemented responsive design with hover animations and gradient backgrounds.
- **June 28, 2025 - Navigation Transparency**: Modified navigation bar to be completely transparent, allowing background colors to show through. Updated language selector for better mobile responsiveness and compact flag-only display.
- **June 28, 2025 - Logo Integration**: Added Latinouch PNG logo to replace text branding in navigation header with hover effects and responsive sizing.
- **June 28, 2025 - Database Integration**: Added PostgreSQL database with comprehensive data models for musicians, contact messages, gallery, events, and site settings. Implemented multilingual content storage and dynamic content loading.
- **June 28, 2025 - Multilingual Support**: Added language selector with Spanish, French, and English support, including flag-based navigation and URL routing (/es, /fr, /en).
- **June 28, 2025 - Initial Setup**: Created responsive website with orange-red gradient design, interactive musician cards with 3D flip animations, and smooth scrolling navigation.

## Changelog

- June 28, 2025: Database integration with PostgreSQL
- June 28, 2025: Multilingual support implementation
- June 28, 2025: Initial project setup