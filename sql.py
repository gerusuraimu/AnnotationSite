from project import db, create_app, models


def main():
    app = create_app()

    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    main()
