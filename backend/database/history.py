"""
History Service
"""

from database.models import ChatHistory


def simpan_history(
    db,
    session_id,
    user_id,
    question,
    answer,
    intent,
    source,
):

    history = ChatHistory(

        session_id=session_id,

        user_id=user_id,

        question=question,

        answer=answer,

        intent=intent,

        source=source,
    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return history


def ambil_history_user(
    db,
    user_id
):

    return (

        db.query(ChatHistory)

        .filter(ChatHistory.user_id == user_id)

        .order_by(ChatHistory.created_at.desc())

        .all()

    )


def hapus_history_user(
    db,
    user_id
):

    (

        db.query(ChatHistory)

        .filter(ChatHistory.user_id == user_id)

        .delete()

    )

    db.commit()