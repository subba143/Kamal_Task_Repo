from firebase_config import db

def add_user_to_firestore(name, email, age):
    # Example: Adding a document to a collection
    doc_ref = db.collection('users').document()
    doc_ref.set({
        'name': name,
        'email': email,
        'age': age
    })


