from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import config
from .util import jwt

ObjectId = String(24)

Model = declarative_base()

from . import models

engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def Relation(cls, col, **kwargs):
    d = dict(**kwargs)
    d['lazy'] = d.get('lazy', 'dynamic')
    return relationship(cls, primaryjoin=col + '_obj', backref=col + '_id', **d)

def PrimaryColumn():
    return Column(ObjectId, primary_key=True)

def ObjectRefColumn(name, **kw):
    d = dict(kw)
    d['nullable'] = d.get('nullable', False)
    return Column(ObjectId, name + '._oid', **d)

def XHRefColumn(name, **kw):
    d = dict(kw)
    d['default'] = d.get('default', -1)
    return Column(Integer, 'xh_' + name + '.id', **d)

def Timestamp():
    return Column(DateTime, nullable=False)