# Software Engineering Final Project
# Classroom Base Note Collaborating P2P System
# Ian Lam (iil209)
# Runxi Bai (rb4287)

import socket
import threading
from db_firestore import addNote, addOutline, retrieveOutline
from course import Course
from note import Note

class Server:
    lecture_outline = ""
    connections = []
    peers = []

    def __init__(self, name, course, note):
        self.username = name
        self.course = course
        self.note = note
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', course.course_port))
        sock.listen(1)

        print(self.username + " is now the Facilitator in this classroom...")

        while True:
            c, a = sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            self.peers.append(a[0])
            print(str(a[0]) + ':' + str(a[1]), "connected")
            self.sendPeers()

    def handler(self, c, a):
        while True:
            data = c.recv(1024)

            if not data:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                self.connections.remove(c)
                self.peers.remove(a[0])
                c.close()
                self.sendPeers()
                break

            if data[0:11] == b'::addnote()':
                self.addNote()

            elif data[0:12] == b'::syncnote()':
                data_to_send = "[sync]" + self.note.body
                self.sendSpecific(c, data_to_send.encode('UTF-8'))

            elif data[0:15] == b'::lecturenote()':
                self.retrieveLectureOutline(c)

            elif data[0:2] == b'::':
                data_to_send = "[chat] ".encode('UTF-8') + data[2:]
                self.broadcast(data_to_send)

            else:
                print(a, ":", data.decode('UTF-8'))
                self.note.body = self.note.body + data.decode('UTF-8') + "\n"
                self.broadcast(data)

    def sendPeers(self):
        p = ""
        for peer in self.peers:
            p = p + peer + ","

        for connection in self.connections:
            connection.send(b'\x11' + bytes(p, 'utf-8'))

    def broadcast(self, data_to_broadcast):
        for connection in self.connections:
            connection.send(bytes(data_to_broadcast))

    def sendSpecific(self, sock, data_to_send):
        sock.send(bytes(data_to_send))

    def retrieveLectureOutline(self, c):
        if self.lecture_outline != "":
            self.sendSpecific(c, ("[lecture]Today's lecture note:\n" + self.lecture_outline).encode('UTF-8'))
        else:
            self.lecture_outline = retrieveOutline(self.course.course_name)
            if self.lecture_outline == "":
                self.sendSpecific(c, "[lecture]The professor have not uploaded lecture notes today".encode('UTF-8'))
            else:
                self.sendSpecific(c, ("[lecture]Today's lecture note:\n" + self.lecture_outline).encode('UTF-8'))

    def addNote(self):
        print("Adding the following note to database")
        print(self.note.body)
        addNote(self.course.course_name, self.username, self.note.body)
        msg = "[addnote]One of the notetakers have added the current note to cloud database..."
        self.broadcast(msg.encode('utf-8'))
