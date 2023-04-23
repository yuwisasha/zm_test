import sessions, db

from multiprocessing import Pool


if __name__ == '__main__':
    db.create_and_fill_db()
    profiles = db.get_profiles()

    p = Pool(processes=5)
    p.starmap(sessions.session, profiles)

