# Software Engineering Final Project
# Classroom Base Note Collaborating P2P System
# Ian Lam (iil209)
# Runxi Bai (rb4287)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, date

# --- This is commented out since we don't want to put the private key on Github..... -------
# cred = credentials.Certificate('[path to json file of the private key of the Firestore Database ]')
# firebase_admin.initialize_app(cred)
# db = firestore.client()

def addNote(class_name, name, new_note):

    print("adding note to database")

    # ---- the following can be uncommented out when we are actually connecting to firestore -----

    # document_id = class_name + "_" + str(date.today())
    #
    # new_note = new_note.replace("\n"," <br>")
    # doc_ref = db.collection(u'notes').document(document_id)
    #
    # doc = doc_ref.get()
    # if doc.exists:
    #     doc_ref.update({'body': new_note})
    #     print("done updating note...")
    # else:
    #     doc_ref.set({
    #         u'title': document_id,
    #         u'body': new_note,
    #         u'timestamp': firestore.SERVER_TIMESTAMP
    #     })
    #     print("done adding note...")

def addOutline(class_name, new_outline):

    print("adding outline to database")

    # ---- the following can be uncommented out when we are actually connecting to firestore -----

    # document_id = class_name + "_" + str(date.today())
    # doc_ref = db.collection(u'lectures').document(document_id)
    # doc_ref.set({
    #     u'outline': new_outline,
    #     u'timestamp': firestore.SERVER_TIMESTAMP
    # })
    # print("done uploading...")

def retrieveOutline(class_name):

    outline = ""

    # ---- the following can be uncommented out when we are actually connecting to firestore -----

    # document_id = class_name + "_" + str(date.today())
    # doc_ref = db.collection(u'lectures').document(document_id)
    # print("checking in database...")
    # doc = doc_ref.get()
    # if doc.exists:
    #     outline = doc.to_dict()["outline"]
    #     print(outline + "\n from retrieve_outline")

    return outline
