from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import config

ObjectId = String(24)

Model = declarative_base()

from . import models

engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def Relation(cls, col, **kwargs):
    d = dict(**kwargs)
    d['lazy'] = d.get('lazy', 'dynamic')
    if 'primaryjoin' in d: delete d['primaryjoin']
    if 'backref' in d: delete d['backref']
    return relationship(cls, primaryjoin=col + '_obj', backref=col + '_id', **d)

def PrimaryColumn():
    return Column(ObjectId, primary_key=True)

def ObjectRefColumn(name, **kwargs):
    kw = dict(kwargs)
    kw['nullable'] = kw.get('nullable', False)
    return Column(ObjectId, name + '._oid', **kw)

def XHRefColumn(name, **kwargs):
    return Column(Integer, 'xh_' + name + '.id', **kwargs)

def Timestamp():
    return Column(DateTime, nullable=False)