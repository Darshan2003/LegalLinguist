import streamlit as st
import pymongo
import hmac
import hashlib


def hash(msg):
    return hmac.new(st.secrets['hashkey'], msg.encode('utf-8'), hashlib.sha256).hexdigest()


def compare_hash(msg, hashed):
    return hmac.compare_digest(hash(msg), hashed)


class Database():
    @st.cache_resource
    def __init__(_self, key) -> None:
        _self.connection = pymongo.MongoClient(key)
        _self.db = _self.connection['test']
        _self.users = _self.db['users']

    def register_user(self, name, email, password):
        exists = self.users.find_one({'email': email})

        if exists is not None:
            return False

        self.users.insert_one({
            'name': name,
            'email': email,
            'password': hash(password)
        })

        return True

    def login_user(self, email, password):
        user = self.users.find_one({'email': email})
        if user is None:
            return False

        st.session_state['verif_email'] = user['email']

        return compare_hash(password, user['password'])
