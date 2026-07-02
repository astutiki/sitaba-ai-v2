"""
User Service
"""

from database.models import User


def cari_user_email(
    db,
    email
):

    return (

        db.query(User)

        .filter(User.email == email)

        .first()

    )


def tambah_user(
    db,
    fullname,
    email,
    password
):

    user = User(

        fullname=fullname,

        email=email,

        password=password,

    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def ambil_user(
    db,
    user_id
):

    return (

        db.query(User)

        .filter(User.id == user_id)

        .first()

    )