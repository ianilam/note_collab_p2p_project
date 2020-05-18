# Classroom Based P2P Note Collaborating System
## NYU Software Engineering 2020 Final Project
Ian Lam (iil209), Runxi Bai (rx4287)

## Overview
This is a terminal based application which allows users in the same network to collaborate and share notes. The application is built with a P2P network that uses the TCP Protocol to transfer data among peers. The ideal targets of this application include students and teachers in a school system.

## Problem Statement
Due to the ongoing COVID19 pandemic, all of New York University’s courses are turned into remote instruction through Zoom. The school wants to develop a note collaborating system that will allow students to share and contribute to notes taken during Zoom class meetings.

## Features of the Application
* Collaborate in real-time among students and professor of the same course
* Share notes among peers in the same network
* Export working note into local directory
* Back up working note to a Cloud Database
  * The Database used is the NoSQL database Cloud Firestore from Firebase and Google Cloud Platform
* Upload lecture outline to a Cloud Database
* Due to its P2P architecture, the application will run as long as there are at least two users in the network. One user will act as the Facilitator and the other as the Notetaker.
  * If one of the Facilitator becomes disconnected, one of the remaining Notetakers will become the new Facilitator.

## Components
1. `chat.py`
  * `NotetakingApp`: entry point of this application. All users of this application logs in from this point.
  * `SystemInfo`: contains information for all users and the courses information.
2. `users.py`
  * `User`: base class. It has the collaborating function to join a P2P network
  * `Professor`: extends from User. In addition to collaborating, the Professor can also upload lecture notes to a cloud database.
  * `Administrator`: manages the SystemInfo. Updates course information or course information.
3. `course.py`
  * `Course`: Course object. Includes the course name and the socket port it is assigned to.
4. `note.py`
  * `Note`: Note object. Includes the actual content of the note and the course it's for.
5. `server.py`
  * `Server`: Facilitates the interactions between Clients.
6. `client.py`
  * `Client`: Takes note, exports notes.
7. `db_firestore.py`: methods used for interacting with the Cloud Firestore database.

## How to Run Application
Type the following in the terminal:  
`python chat.py`

This should immediately starts a prompt that asks for user name and the course.
```
What is your name?
What course is this for?
```
Once those questions are answered properly, if the person is a User or a Professor, he/she can begin using the collaborating part of the application.

Anything the user types at this point will be recorded as the note for the course, unless he/she begins the message with two colons, `::`, then in that case, the message will just be transmitted as a normal chat message and is not recorded.

Functions that the Notetaker can type in the terminal include:  
```
::seenote()  
::exportnote()  
::addnote()  
::syncnote()  
::lecturenote()
```

`::seenote()`: see the current version of notes   
`::exportnote()`: export notes as text file to local directory  
`::addnote()`: add note to Cloud database  
`::syncnote()`: obtain most updated version of note from Facilitator  
`::lecturenote()`: retrieve the lecture note the Professor uploaded from the Cloud database

To disconnect from the application, the user just type `Ctrl+C` in their terminal to disconnect from the network.


## Example Run

First user Ian joins the P2P network and becomes the Facilitator. Ian will see all the messages that are being sent throughout the network.
```
ian@Ians-MacBook-Air note_collab_p2p_project % python chat.py
What is your name? ian
What course is this for? OS
Trying to connect...
ian is now the Facilitator in this classroom...
127.0.0.1:52036 connected
('127.0.0.1', 52036) : What is Operating System?
('127.0.0.1', 52036) : An operating system (OS) is system software
127.0.0.1:52045 connected
```

Second user Vicky joins the P2P network and becomes the Notetaker. Vicky will start inputting note and this note will be spread across everyone in network.
```
ian@Ians-MacBook-Air note_collab_p2p_project % python chat.py
What is your name? vicky
What course is this for? OS
Trying to connect...
You are now connected as one of the Notetakers in this classroom.
What is Operating System?
[note] What is Operating System?
An operating system (OS) is system software
[note] An operating system (OS) is system software
::seenote()
------------ Current Version of Note for OS ----------
What is Operating System?
An operating system (OS) is system software

-------------------- End of Note ---------------------
```

Third user Kelly, a professor, will use the app and uploads the lecture outline to the cloud database before joining the P2P network. Kelly will also become a Notetaker. Here Kelly uploads the lecture note and begins to chat.

```
ian@Ians-MacBook-Air note_collab_p2p_project % python chat.py
What is your name? kelly
What course are you here for? OS
What is the filename for the lecture outline? test_lecture.txt
lecture outline
* Introduction
* Types of Operating Systems
	** Single-tasking and multi-tasking
	** Single - and mult-user
	** Distributed
	** Templated
	** Embedded
	** Real
	** Library

Uploading lecture outline to cloud database
done uploading...
Trying to connect...
You are now connected as one of the Notetakers in this classroom.
::Hello everyone, this is Professor Kelly joining
[chat] Hello everyone, this is Professor Kelly joining
```
