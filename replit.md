# LAtinouch Musical Project

## Overview

LAtinouch is a musical project website built with Flask, featuring a modern and responsive design. The application serves as a landing page for a musical group, showcasing musicians and providing contact information. The site is designed with a vibrant orange and red color scheme, targeting Spanish-speaking audiences.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 (Flask's default templating engine)
- **CSS Framework**: Bootstrap 5 for responsive grid system and components
- **Custom Styling**: CSS3 with custom properties for consistent theming
- **JavaScript**: Vanilla JavaScript for interactive features
- **Icons**: Font Awesome 6.4.0 for iconography
- **Fonts**: Google Fonts (Poppins family)

### Backend Architecture
- **Framework**: Flask (Python microframework)
- **Server**: Development server (Flask's built-in)
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

## Data Flow

1. **Request Handling**: Flask receives HTTP requests on the root route (`/`)
2. **Template Rendering**: Jinja2 processes the HTML template with any context data
3. **Static Asset Serving**: Flask serves CSS, JavaScript, and other static files
4. **Client-Side Interactions**: JavaScript handles navigation, animations, and user interactions

## External Dependencies

### CDN Resources
- **Bootstrap 5.3.0**: CSS framework for responsive design
- **Font Awesome 6.4.0**: Icon library for UI elements
- **Google Fonts**: Poppins font family for typography

### Python Dependencies
- **Flask**: Web framework for Python
- **Standard Library**: OS module for environment variable access

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

## Changelog

Changelog:
- June 28, 2025. Initial setup