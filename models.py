from . import database as db

# 学校列表（预留）
class School(db.Model):
    __tablename__ = 'schools'
    _oid = db.PrimaryColumn()
    name = db.Column(db.Text, default='未命名学校')
    on_campus = db.Column(db.Float, default=25.0)
    off_campus = db.Column(db.Float, default=15.0)
    social_practice = db.Column(db.Float, default=18.0)
    on_to_off_rate = db.Column(db.Float, default=1/3)
    on_to_off_limit = db.Column(db.Float, default=1/0)
    off_to_on_rate = db.Column(db.Float, default=0.5)
    off_to_on_limit = db.Column(db.Float, default=1/0)
    time_unit_hrs = db.Column(db.Float, default=0.5)
    xuehai_id = db.XHRefColumn('schools', default=-1)
    validity = db.Column(db.Integer, default=1)
    classes = db.Relation('Class', 'school')
    timestamp = db.Timestamp()

# 班级列表
class Class(db.Model):
    __tablename__ = 'classes'
    _oid = db.PrimaryColumn()
    id = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.Text, default='未命名班级')
    year = db.Column(db.Integer, default=0)
    school_id = db.ObjectRefColumn('schools')
    xuehai_id = db.XHRefColumn('classes', default=-1)
    students = db.Relation('User', 'class')
    timestamp = db.Timestamp()

# 用户列表
class User(db.Model):
    _oid = db.PrimaryColumn()
    id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.Text, default='新用户')
    class_id = db.ObjectRefColumn('classes')
    password = db.Column(db.Text)
    sec_questions = db.Column(db.Text)
    sec_answers = db.Column(db.Text)
    on_campus = db.Column(db.Float, default=0.0)
    off_campus = db.Column(db.Float, default=0.0)
    social_practice = db.Column(db.Float, default=0.0)
    status = db.Column(db.Integer, default=0)
    xuehai_id = db.XHRefColumn('users', default=-1)
    exports = db.Relation('ExportRecord', 'user')
    history = db.Relation('UserHistory', 'user')
    participated = db.Relation('ActivityMember', 'user')
    created = db.Relation('Activity', 'creator')
    audited = db.Relation('Activity', 'auditor')
    timestamp = db.Timestamp()

class UserHistory(db.Model):
    __tablename__ = 'user_history'
    _oid = db.PrimaryColumn()
    user_id = db.ObjectRefColumn('users')
    type = db.Column(db.Integer, default=-1)
    id = db.Column(db.Integer, default=-1)
    name = db.Column(db.Text, default='')
    log_id = db.ObjectRefColumn('logs')
    timestamp = db.Timestamp()

class LogEntry(db.Model):
    __tablename__ = 'logs'
    _oid = db.PrimaryColumn()
    type = db.Column(db.Integer, default=-1)
    operator = db.ObjectRefColumn('users')
    data = db.Column(db.Text, default='{}')
    ip = db.Column(db.Text, default='unknown')
    token = db.Column(db.Text, default='')
    timestamp = db.Column(db.Text, default='')