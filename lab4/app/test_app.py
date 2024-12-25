import pytest
from flask import Flask
from flask_login import login_user
from app import app, db
import mysql.connector

import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import app, db  # Убедитесь, что db - это экземпляр SQLAlchemy

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False 

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://test:test@192.168.1.4/test'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

    with app.test_client() as client:
        yield client


def test_login(client):

    response = client.post('/login', data={
        'login': 'user123',
        'password': '123'
    })
    
    assert response.status_code == 302 


    assert response.location is not None 
    response = client.get(response.location)  


    assert 'alert alert-success' in response.get_data(as_text=True)
    assert 'Вы успешно вошли!' in response.get_data(as_text=True)


