import os
from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# configure the database
database_url = os.environ.get("DATABASE_URL")
if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_recycle": 300,
        "pool_pre_ping": True,
    }
else:
    # Fallback for development
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///latinouch.db"

# initialize the app with the extension
db.init_app(app)


@app.route('/')
def home():
    return render_template('index.html')

# Language content
LANGUAGES = {
    'es': {
        'nav': {
            'home': 'Inicio',
            'about': 'Nosotros',
            'musicians': 'Músicos',
            'presentations': 'Presentaciones',
            'contact': 'Contacto'
        },
        'hero': {
            'title': 'Latinouch',
            'subtitle': 'Fusión Musical Latinoamericana',
            'btn_musicians': 'Conoce al Grupo',
            'btn_about': 'Nuestra Historia'
        },
        'about': {
            'title': 'Nuestra Pasión Musical',
            'description': 'Latinouch nace de la fusión de diferentes culturas y sonidos latinoamericanos, creando una propuesta musical única que combina tradición e innovación.',
            'feature1_title': 'Sonidos Auténticos',
            'feature1_desc': 'Instrumentos tradicionales fusionados con elementos modernos',
            'feature2_title': 'Pasión Latina',
            'feature2_desc': 'Cada nota refleja la esencia y el alma de Latinoamérica',
            'feature3_title': 'Fusión Cultural',
            'feature3_desc': 'Uniendo fronteras a través de la música universal'
        },
        'musicians': {
            'title': 'Nuestros Artistas',
            'subtitle': 'Conoce a los talentosos músicos que dan vida a Latinouch',
            'marjorie': {
                'name': 'Marjorie',
                'instrument': 'Violinista',
                'description': 'Virtuosa del violín con formación clásica y alma latina. Su técnica impecable se combina con la pasión ardiente de los ritmos sudamericanos, creando melodías que tocan el corazón y despiertan los sentidos.',
                'skills': ['Clásico', 'Tango', 'Folk']
            },
            'pierre': {
                'name': 'Pierre',
                'instrument': 'Guitarra Rítmica',
                'description': 'El corazón rítmico de Latinouch. Pierre domina los acordes que sostienen nuestras composiciones, aportando groove y energía. Su experiencia en diferentes géneros latinos le permite crear texturas únicas y envolventes.',
                'skills': ['Bossa Nova', 'Cumbia', 'Reggaeton']
            },
            'romain': {
                'name': 'Romain',
                'instrument': 'Guitarra Líder',
                'description': 'Maestro de los solos y las melodías principales. Romain fusiona técnicas de rock, jazz y música tradicional latina para crear líneas melódicas inolvidables que definen el sonido característico de Latinouch.',
                'skills': ['Jazz Latino', 'Rock', 'Flamenco']
            },
            'neil': {
                'name': 'Neil',
                'instrument': 'Percusión',
                'description': 'El alma percusiva que da vida a nuestros ritmos. Neil domina tanto la batería moderna como instrumentos tradicionales latinos, creando bases rítmicas que invitan al movimiento y conectan con las raíces culturales.',
                'skills': ['Salsa', 'Merengue', 'Samba']
            },
            'juanjose': {
                'name': 'Juan José',
                'instrument': 'Teclado & Bajo Synth',
                'description': 'Versátil multi-instrumentista que aporta las bases armónicas y melódicas. Su dominio del teclado y sintetizadores crea atmósferas únicas, mientras que sus líneas de bajo dan profundidad y groove a nuestras composiciones.',
                'skills': ['Piano', 'Synthwave', 'Funk']
            },
            'fay': {
                'name': 'Fay',
                'instrument': 'Voz Principal',
                'description': 'La voz que emociona y cuenta historias. Fay posee un rango vocal excepcional y la capacidad de transmitir emociones profundas. Su interpretación auténtica da vida a las letras y conecta directamente con el público.',
                'skills': ['Balada', 'Pop Latino', 'R&B']
            }
        },
        'presentations': {
            'title': 'Nuestras Presentaciones',
            'subtitle': 'Revive la magia de nuestros conciertos más memorables'
        },
        'contact': {
            'title': 'Conecta con Nosotros',
            'subtitle': '¿Interesado en colaborar o contratar nuestros servicios?',
            'email': 'Email',
            'phone': 'Teléfono',
            'social': 'Redes Sociales',
            'footer': '© 2025 Latinouch. Todos los derechos reservados.'
        }
    },
    'fr': {
        'nav': {
            'home': 'Accueil',
            'about': 'À Propos',
            'musicians': 'Musiciens',
            'presentations': 'Concerts',
            'contact': 'Contact'
        },
        'hero': {
            'title': 'Latinouch',
            'subtitle': 'Fusion Musicale Latino-Américaine',
            'btn_musicians': 'Découvrez le Groupe',
            'btn_about': 'Notre Histoire'
        },
        'about': {
            'title': 'Notre Passion Musicale',
            'description': 'Latinouch naît de la fusion de différentes cultures et sons latino-américains, créant une proposition musicale unique qui combine tradition et innovation.',
            'feature1_title': 'Sons Authentiques',
            'feature1_desc': 'Instruments traditionnels fusionnés avec des éléments modernes',
            'feature2_title': 'Passion Latine',
            'feature2_desc': 'Chaque note reflète l\'essence et l\'âme de l\'Amérique Latine',
            'feature3_title': 'Fusion Culturelle',
            'feature3_desc': 'Unir les frontières à travers la musique universelle'
        },
        'musicians': {
            'title': 'Nos Artistes',
            'subtitle': 'Rencontrez les musiciens talentueux qui donnent vie à Latinouch',
            'marjorie': {
                'name': 'Marjorie',
                'instrument': 'Violoniste',
                'description': 'Virtuose du violon avec une formation classique et une âme latine. Sa technique impeccable se combine avec la passion ardente des rythmes sud-américains, créant des mélodies qui touchent le cœur et éveillent les sens.',
                'skills': ['Classique', 'Tango', 'Folk']
            },
            'pierre': {
                'name': 'Pierre',
                'instrument': 'Guitare Rythmique',
                'description': 'Le cœur rythmique de Latinouch. Pierre maîtrise les accords qui soutiennent nos compositions, apportant groove et énergie. Son expérience dans différents genres latins lui permet de créer des textures uniques et enveloppantes.',
                'skills': ['Bossa Nova', 'Cumbia', 'Reggaeton']
            },
            'romain': {
                'name': 'Romain',
                'instrument': 'Guitare Solo',
                'description': 'Maître des solos et des mélodies principales. Romain fusionne les techniques de rock, jazz et musique traditionnelle latine pour créer des lignes mélodiques inoubliables qui définissent le son caractéristique de Latinouch.',
                'skills': ['Jazz Latino', 'Rock', 'Flamenco']
            },
            'neil': {
                'name': 'Neil',
                'instrument': 'Percussion',
                'description': 'L\'âme percussive qui donne vie à nos rythmes. Neil maîtrise autant la batterie moderne que les instruments traditionnels latins, créant des bases rythmiques qui invitent au mouvement et se connectent aux racines culturelles.',
                'skills': ['Salsa', 'Merengue', 'Samba']
            },
            'juanjose': {
                'name': 'Juan José',
                'instrument': 'Clavier & Basse Synth',
                'description': 'Multi-instrumentiste polyvalent qui apporte les bases harmoniques et mélodiques. Sa maîtrise du clavier et des synthétiseurs crée des atmosphères uniques, tandis que ses lignes de basse donnent profondeur et groove à nos compositions.',
                'skills': ['Piano', 'Synthwave', 'Funk']
            },
            'fay': {
                'name': 'Fay',
                'instrument': 'Voix Principale',
                'description': 'La voix qui émeut et raconte des histoires. Fay possède une tessiture vocale exceptionnelle et la capacité de transmettre des émotions profondes. Son interprétation authentique donne vie aux paroles et se connecte directement avec le public.',
                'skills': ['Ballade', 'Pop Latino', 'R&B']
            }
        },
        'presentations': {
            'title': 'Nos Concerts',
            'subtitle': 'Revivez la magie de nos performances les plus mémorables'
        },
        'contact': {
            'title': 'Connectez-vous avec Nous',
            'subtitle': 'Intéressé par une collaboration ou engager nos services?',
            'email': 'Email',
            'phone': 'Téléphone',
            'social': 'Réseaux Sociaux',
            'footer': '© 2025 Latinouch. Tous droits réservés.'
        }
    },
    'en': {
        'nav': {
            'home': 'Home',
            'about': 'About',
            'musicians': 'Musicians',
            'presentations': 'Performances',
            'contact': 'Contact'
        },
        'hero': {
            'title': 'Latinouch',
            'subtitle': 'Latin American Musical Fusion',
            'btn_musicians': 'Meet the Band',
            'btn_about': 'Our Story'
        },
        'about': {
            'title': 'Our Musical Passion',
            'description': 'Latinouch is born from the fusion of different Latin American cultures and sounds, creating a unique musical proposal that combines tradition and innovation.',
            'feature1_title': 'Authentic Sounds',
            'feature1_desc': 'Traditional instruments fused with modern elements',
            'feature2_title': 'Latin Passion',
            'feature2_desc': 'Every note reflects the essence and soul of Latin America',
            'feature3_title': 'Cultural Fusion',
            'feature3_desc': 'Uniting borders through universal music'
        },
        'musicians': {
            'title': 'Our Artists',
            'subtitle': 'Meet the talented musicians who bring Latinouch to life',
            'marjorie': {
                'name': 'Marjorie',
                'instrument': 'Violinist',
                'description': 'Violin virtuoso with classical training and a Latin soul. Her impeccable technique combines with the burning passion of South American rhythms, creating melodies that touch the heart and awaken the senses.',
                'skills': ['Classical', 'Tango', 'Folk']
            },
            'pierre': {
                'name': 'Pierre',
                'instrument': 'Rhythm Guitar',
                'description': 'The rhythmic heart of Latinouch. Pierre masters the chords that support our compositions, bringing groove and energy. His experience in different Latin genres allows him to create unique and enveloping textures.',
                'skills': ['Bossa Nova', 'Cumbia', 'Reggaeton']
            },
            'romain': {
                'name': 'Romain',
                'instrument': 'Lead Guitar',
                'description': 'Master of solos and main melodies. Romain fuses rock, jazz and traditional Latin music techniques to create unforgettable melodic lines that define Latinouch\'s characteristic sound.',
                'skills': ['Latin Jazz', 'Rock', 'Flamenco']
            },
            'neil': {
                'name': 'Neil',
                'instrument': 'Percussion',
                'description': 'The percussive soul that brings our rhythms to life. Neil masters both modern drums and traditional Latin instruments, creating rhythmic foundations that invite movement and connect with cultural roots.',
                'skills': ['Salsa', 'Merengue', 'Samba']
            },
            'juanjose': {
                'name': 'Juan José',
                'instrument': 'Keyboard & Bass Synth',
                'description': 'Versatile multi-instrumentalist who provides harmonic and melodic foundations. His mastery of keyboard and synthesizers creates unique atmospheres, while his bass lines give depth and groove to our compositions.',
                'skills': ['Piano', 'Synthwave', 'Funk']
            },
            'fay': {
                'name': 'Fay',
                'instrument': 'Lead Vocals',
                'description': 'The voice that moves and tells stories. Fay possesses an exceptional vocal range and the ability to convey deep emotions. Her authentic interpretation brings lyrics to life and connects directly with the audience.',
                'skills': ['Ballad', 'Latin Pop', 'R&B']
            }
        },
        'presentations': {
            'title': 'Our Performances',
            'subtitle': 'Relive the magic of our most memorable concerts'
        },
        'contact': {
            'title': 'Connect with Us',
            'subtitle': 'Interested in collaborating or hiring our services?',
            'email': 'Email',
            'phone': 'Phone',
            'social': 'Social Media',
            'footer': '© 2025 Latinouch. All rights reserved.'
        }
    }
}

with app.app_context():
    # Import models to ensure tables are created
    import models
    db.create_all()

@app.route('/')
@app.route('/<lang>')
def index(lang='es'):
    """Main landing page for LAtinouch musical project"""
    if lang not in LANGUAGES:
        lang = 'es'
    
    session['language'] = lang
    content = LANGUAGES[lang]
    
    # Try to get musicians from database, fallback to static content
    try:
        musicians_data = models.Musician.query.filter_by(is_active=True).order_by(models.Musician.position_order).all()
        if musicians_data:
            # Convert database musicians to content format
            musicians_dict = {}
            for musician in musicians_data:
                key = musician.name.lower().replace(' ', '').replace('é', 'e')
                bio_field = f'bio_{lang}'
                bio = getattr(musician, bio_field, '') or musician.bio_es or ''
                
                musicians_dict[key] = {
                    'name': musician.name,
                    'instrument': musician.instrument,
                    'description': bio,
                    'skills': musician.skills or []
                }
            
            if musicians_dict:
                content['musicians'].update(musicians_dict)
    except Exception:
        # Use static content if database is not available
        pass
    
    return render_template('index.html', content=content, current_lang=lang)

@app.route('/admin/seed-data')
def seed_data():
    """Seed initial data into the database"""
    try:
        # Check if data already exists
        if models.Musician.query.count() > 0:
            return "Data already exists"
        
        # Create initial musicians
        musicians = [
            {
                'name': 'Marjorie',
                'instrument': 'Violinista',
                'bio_es': 'Virtuosa del violín con formación clásica y alma latina. Su técnica impecable se combina con la pasión ardiente de los ritmos sudamericanos, creando melodías que tocan el corazón y despiertan los sentidos.',
                'bio_fr': 'Virtuose du violon avec une formation classique et une âme latine. Sa technique impeccable se combine avec la passion ardente des rythmes sud-américains, créant des mélodies qui touchent le cœur et éveillent les sens.',
                'bio_en': 'Violin virtuoso with classical training and a Latin soul. Her impeccable technique combines with the burning passion of South American rhythms, creating melodies that touch the heart and awaken the senses.',
                'skills': ['Clásico', 'Tango', 'Folk'],
                'position_order': 1
            },
            {
                'name': 'Pierre',
                'instrument': 'Guitarra Rítmica',
                'bio_es': 'El corazón rítmico de LAtinouch. Pierre domina los acordes que sostienen nuestras composiciones, aportando groove y energía. Su experiencia en diferentes géneros latinos le permite crear texturas únicas y envolventes.',
                'bio_fr': 'Le cœur rythmique de LAtinouch. Pierre maîtrise les accords qui soutiennent nos compositions, apportant groove et énergie. Son expérience dans différents genres latins lui permet de créer des textures uniques et enveloppantes.',
                'bio_en': 'The rhythmic heart of LAtinouch. Pierre masters the chords that support our compositions, bringing groove and energy. His experience in different Latin genres allows him to create unique and enveloping textures.',
                'skills': ['Bossa Nova', 'Cumbia', 'Reggaeton'],
                'position_order': 2
            },
            {
                'name': 'Romain',
                'instrument': 'Guitarra Líder',
                'bio_es': 'Maestro de los solos y las melodías principales. Romain fusiona técnicas de rock, jazz y música tradicional latina para crear líneas melódicas inolvidables que definen el sonido característico de LAtinouch.',
                'bio_fr': 'Maître des solos et des mélodies principales. Romain fusionne les techniques de rock, jazz et musique traditionnelle latine pour créer des lignes mélodiques inoubliables qui définissent le son caractéristique de LAtinouch.',
                'bio_en': 'Master of solos and main melodies. Romain fuses rock, jazz and traditional Latin music techniques to create unforgettable melodic lines that define LAtinouch\'s characteristic sound.',
                'skills': ['Jazz Latino', 'Rock', 'Flamenco'],
                'position_order': 3
            },
            {
                'name': 'Neil',
                'instrument': 'Percusión',
                'bio_es': 'El alma percusiva que da vida a nuestros ritmos. Neil domina tanto la batería moderna como instrumentos tradicionales latinos, creando bases rítmicas que invitan al movimiento y conectan con las raíces culturales.',
                'bio_fr': 'L\'âme percussive qui donne vie à nos rythmes. Neil maîtrise autant la batterie moderne que les instruments traditionnels latins, créant des bases rythmiques qui invitent au mouvement et se connectent aux racines culturelles.',
                'bio_en': 'The percussive soul that brings our rhythms to life. Neil masters both modern drums and traditional Latin instruments, creating rhythmic foundations that invite movement and connect with cultural roots.',
                'skills': ['Salsa', 'Merengue', 'Samba'],
                'position_order': 4
            },
            {
                'name': 'Juan José',
                'instrument': 'Teclado & Bajo Synth',
                'bio_es': 'Versátil multi-instrumentista que aporta las bases armónicas y melódicas. Su dominio del teclado y sintetizadores crea atmósferas únicas, mientras que sus líneas de bajo dan profundidad y groove a nuestras composiciones.',
                'bio_fr': 'Multi-instrumentiste polyvalent qui apporte les bases harmoniques et mélodiques. Sa maîtrise du clavier et des synthétiseurs crée des atmosphères uniques, tandis que ses lignes de basse donnent profondeur et groove à nos compositions.',
                'bio_en': 'Versatile multi-instrumentalist who provides harmonic and melodic foundations. His mastery of keyboard and synthesizers creates unique atmospheres, while his bass lines give depth and groove to our compositions.',
                'skills': ['Piano', 'Synthwave', 'Funk'],
                'position_order': 5
            },
            {
                'name': 'Fay',
                'instrument': 'Voz Principal',
                'bio_es': 'La voz que emociona y cuenta historias. Fay posee un rango vocal excepcional y la capacidad de transmitir emociones profundas. Su interpretación auténtica da vida a las letras y conecta directamente con el público.',
                'bio_fr': 'La voix qui émeut et raconte des histoires. Fay possède une tessiture vocale exceptionnelle et la capacité de transmettre des émotions profondes. Son interprétation authentique donne vie aux paroles et se connecte directement avec le public.',
                'bio_en': 'The voice that moves and tells stories. Fay possesses an exceptional vocal range and the ability to convey deep emotions. Her authentic interpretation brings lyrics to life and connects directly with the audience.',
                'skills': ['Balada', 'Pop Latino', 'R&B'],
                'position_order': 6
            }
        ]
        
        for musician_data in musicians:
            musician = models.Musician(**musician_data)
            db.session.add(musician)
        
        db.session.commit()
        return "Database seeded successfully!"
        
    except Exception as e:
        db.session.rollback()
        return f"Error seeding database: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
