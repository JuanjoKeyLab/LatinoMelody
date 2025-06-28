// Main JavaScript for LAtinouch website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive features
    initScrollAnimations();
    initSmoothScrolling();
    initNavbarEffects();
    initMusicianCards();
    initParallaxEffects();
});

// Smooth scrolling for navigation links
function initSmoothScrolling() {
    const navLinks = document.querySelectorAll('a[href^="#"]');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const navbarHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetSection.offsetTop - navbarHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Navbar scroll effects
function initNavbarEffects() {
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add/remove backdrop blur based on scroll position
        if (currentScroll > 50) {
            navbar.style.background = 'linear-gradient(135deg, rgba(255, 107, 53, 0.98) 0%, rgba(204, 41, 54, 0.98) 100%)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
        } else {
            navbar.style.background = 'linear-gradient(135deg, rgba(255, 107, 53, 0.95) 0%, rgba(204, 41, 54, 0.95) 100%)';
            navbar.style.boxShadow = 'none';
        }
        
        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });
}

// Scroll animations for elements
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                
                // Add staggered animation for musician cards
                if (entry.target.classList.contains('musician-card')) {
                    const cards = document.querySelectorAll('.musician-card');
                    const index = Array.from(cards).indexOf(entry.target);
                    entry.target.style.animationDelay = `${index * 0.1}s`;
                }
            }
        });
    }, observerOptions);
    
    // Observe elements for scroll animations
    const animatedElements = document.querySelectorAll('.musician-card, .feature-icon, .contact-item, .section-header');
    animatedElements.forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });
}

// Enhanced musician card interactions
function initMusicianCards() {
    const cards = document.querySelectorAll('.musician-card');
    
    cards.forEach((card, index) => {
        // Add entrance animation delay
        card.style.animationDelay = `${index * 0.1}s`;
        
        // Enhanced hover effects
        card.addEventListener('mouseenter', function() {
            // Add subtle scale and glow effect
            this.style.transform = 'scale(1.02)';
            this.style.filter = 'drop-shadow(0 15px 35px rgba(255, 107, 53, 0.3))';
            
            // Add subtle vibration effect
            setTimeout(() => {
                this.style.transform = 'scale(1.02) translateY(-5px)';
            }, 100);
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) translateY(0)';
            this.style.filter = 'none';
        });
        
        // Touch support for mobile devices
        card.addEventListener('touchstart', function() {
            this.classList.add('touch-active');
        });
        
        card.addEventListener('touchend', function() {
            setTimeout(() => {
                this.classList.remove('touch-active');
            }, 300);
        });
        
        // Click to flip on mobile
        card.addEventListener('click', function(e) {
            if (window.innerWidth <= 768) {
                e.preventDefault();
                this.classList.toggle('mobile-flipped');
            }
        });
    });
}

// Parallax effects for hero section
function initParallaxEffects() {
    const heroSection = document.querySelector('.hero-section');
    const scrollIndicator = document.querySelector('.scroll-indicator');
    
    window.addEventListener('scroll', function() {
        const scrolled = window.pageYOffset;
        const parallaxSpeed = 0.5;
        
        if (heroSection) {
            // Parallax effect for hero background
            heroSection.style.transform = `translateY(${scrolled * parallaxSpeed}px)`;
            
            // Fade out scroll indicator
            if (scrollIndicator) {
                const opacity = Math.max(0, 1 - scrolled / 300);
                scrollIndicator.style.opacity = opacity;
            }
        }
    });
}

// Add loading animations
window.addEventListener('load', function() {
    const loadingElements = document.querySelectorAll('.loading');
    loadingElements.forEach((el, index) => {
        setTimeout(() => {
            el.classList.add('loaded');
        }, index * 100);
    });
});

// Add CSS class for mobile flip effect
const style = document.createElement('style');
style.textContent = `
    .musician-card.mobile-flipped .card-inner {
        transform: rotateY(180deg);
    }
    
    .musician-card.touch-active {
        transform: scale(0.98);
        transition: transform 0.1s ease;
    }
    
    @media (max-width: 768px) {
        .musician-card:hover .card-inner {
            transform: none;
        }
        
        .musician-card.mobile-flipped .card-inner {
            transform: rotateY(180deg);
        }
    }
`;
document.head.appendChild(style);

// Easter egg: Konami code for special effect
let konamiCode = [];
const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];

document.addEventListener('keydown', function(e) {
    konamiCode.push(e.keyCode);
    
    if (konamiCode.length > konamiSequence.length) {
        konamiCode.shift();
    }
    
    if (konamiCode.join(',') === konamiSequence.join(',')) {
        // Special animation effect
        document.body.style.animation = 'rainbow 2s ease-in-out';
        
        setTimeout(() => {
            document.body.style.animation = '';
        }, 2000);
        
        konamiCode = [];
    }
});

// Add rainbow animation CSS
const rainbowStyle = document.createElement('style');
rainbowStyle.textContent = `
    @keyframes rainbow {
        0% { filter: hue-rotate(0deg); }
        25% { filter: hue-rotate(90deg); }
        50% { filter: hue-rotate(180deg); }
        75% { filter: hue-rotate(270deg); }
        100% { filter: hue-rotate(360deg); }
    }
`;
document.head.appendChild(rainbowStyle);

// Performance optimization: Throttle scroll events
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Apply throttling to scroll events
const throttledScrollHandler = throttle(function() {
    // Scroll-dependent functions can be added here
}, 16); // ~60fps

window.addEventListener('scroll', throttledScrollHandler);
