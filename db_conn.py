#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from magic_cifer import encrypt, decrypt
import pymysql.cursors
import random


def get_random_message():
    phrase_list = []
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='keyboard',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `phrase_text` FROM `phrases`"
            cursor.execute(sql)
            result = cursor.fetchall()
            # print(result)
            for i in range(len(result)):
                for key, value in result[i].items():
                    phrase_list.append(value)
            return decrypt(random.choice(phrase_list))
    finally:
        connection.close()

def get_message_id(message):
    db_message = encrypt(message)
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                db='keyboard',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT `id` FROM `phrases` WHERE `phrase_text` = %s"
            cursor.execute(sql, db_message)
            result = cursor.fetchall()
            for key, value in result[0].items():
                return value
    finally:
        connection.close()

def insert_user(login, pass_code, ideal_value, difference):
    connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='keyboard',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT into `users`(`username`, `passphrase`, `ideal_value`, `difference`) values (%s,%s,%s,%s);"
            cursor.execute(sql, (login, pass_code, ideal_value, difference))
        connection.commit()
    finally:
        connection.close()

def get_user_info(login):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                db='keyboard',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `users` WHERE `username` = %s"
            cursor.execute(sql, login)
            result = cursor.fetchall()
            passphrase = result[0]['passphrase']
            ideal = result[0]['ideal_value']
            difference = result[0]['difference']
            login = result[0]['username']
            return login, passphrase, ideal, difference
            # for key, value in result[0].items():
                # return value
    finally:
        connection.close()

def check_username(login):
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='root',
                                db='keyboard',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `users` WHERE `username` = %s"
            cursor.execute(sql, login)
            result = cursor.fetchall()
            if result:
                return True
            else:
                return False
            # passphrase = result[0]['passphrase']
            # ideal = result[0]['ideal_value']
            # difference = result[0]['difference']
            # login = result[0]['username']
            # return login, passphrase, ideal, difference
            # # for key, value in result[0].items():
                # return value
    finally:
        connection.close()
# if check_username("пуфик"):
#     print("ъуъ")
# else:
#     print("Nope")
# name = "Push"
# passphrase = 1
# ideal = 0.2
# difference = 0.004
# insert_user(name, passphrase, ideal, difference)

# print(passhrase)
# print(get_random_message())
