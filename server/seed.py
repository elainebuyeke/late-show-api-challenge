from server.app import create_app
from server.models import db, User, Guest, Episode, Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username='admin')
    user.set_password('password')
    db.session.add(user)

    guest1 = Guest(name='Tom Hanks', occupation='Actor')
    guest2 = Guest(name='Taylor Swift', occupation='Singer')
    db.session.add_all([guest1, guest2])

    episode1 = Episode(date='2023-01-01', number=1)
    episode2 = Episode(date='2023-01-02', number=2)
    db.session.add_all([episode1, episode2])

    db.session.commit()

    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()
    print('Database seeded!') 