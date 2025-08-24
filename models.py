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
    xuehai_id = db.XHRef('schools')
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
    school_id = db.ObjectRef('schools')
    xuehai_id = db.XHRef('classes')
    students = db.Relation('User', 'class')
    timestamp = db.Timestamp()

# 用户列表
class User(db.Model):
    _oid = db.PrimaryColumn()
    id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.Text, default='新用户')
    class_id = db.ObjectRef('classes')
    password = db.Column(db.Text)
    permission = db.Column(db.Integer, default=0)
    sec_questions = db.Column(db.Text)
    sec_answers = db.Column(db.Text)
    on_campus = db.Column(db.Float, default=0.0)
    off_campus = db.Column(db.Float, default=0.0)
    social_practice = db.Column(db.Float, default=0.0)
    status = db.Column(db.Integer, default=0)
    xuehai_id = db.XHRef('users')
    exports = db.Relation('ExportRecord', 'user')
    history = db.Relation('UserHistory', 'user')
    joined = db.Relation('ActivityMember', 'user')
    created = db.Relation('Activity', 'creator')
    audited = db.Relation('Activity', 'auditor')
    tokens = db.Relation('UserToken', 'user')
    devices = db.Relation('Device', 'user')
    last_login = db.Timestamp()
    timestamp = db.Timestamp()

class UserHistory(db.Model):
    __tablename__ = 'user_history'
    _oid = db.PrimaryColumn()
    user_id = db.ObjectRef('users')
    type = db.Column(db.Integer, default=0)
    id = db.Column(db.Integer, default=0)
    name = db.Column(db.Text, default='')
    log_id = db.ObjectRef('logs')
    timestamp = db.Timestamp()

class LogEntry(db.Model):
    __tablename__ = 'logs'
    _oid = db.PrimaryColumn()
    type = db.Column(db.Integer, default=-1)
    actioner_id = db.ObjectRef('users')
    data = db.Column(db.Text, default='{}')
    ip = db.Column(db.Text, default='unknown')
    device_id = db.ObjectRef('devices')
    token = db.Column(db.Text, default='')
    timestamp = db.Timestamp()

# 义工列表
class Activity(db.Model):
    __tablename__ = 'activities'
    _oid = db.PrimaryColumn()
    name = db.Column(db.Text, default='未命名')
    description = db.Column(db.Text, default='')
    template_id = db.ObjectRef('templates')
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.Text, default='')
    status = db.Column(db.Integer, default=0)
    creator_id = db.ObjectRef('users')
    auditor_id = db.ObjectRef('users', nullable=True)
    merged_to_id = db.ObjectRef('activities', nullable=True)
    members = db.Relation('ActivityMember', 'activity')
    history = db.Relation('ActivityHistory', 'activity')
    merges = db.Relation('Activity', 'merged_to')
    timestamp = db.Timestamp()

class ActivtyHistory(db.Model):
    _oid = db.PrimaryColumn()
    activity_id = db.ObjectRef('activities')
    actioner_id = db.ObjectRef('users')
    type = db.Column(db.Integer, default=-1)
    data = db.Column(db.Text, default='{}')
    log_id = db.ObjectRef('logs')
    timestamp = db.Timestamp()

# 统一令牌管理，用于 util.jwt.validate_token()
class UserToken(db.Model):
    _oid = db.PrimaryColumn()
    token = db.Column(db.Text, nullable=False, unique=True)
    user = db.ObjectRef('users')
    device = db.ObjectRef('devices', nullable=True)
    app_ver = db.Column(db.Integer, default=-1)
    type = db.Column(db.Integer, default=0)
    expires = db.Column(db.DateTime)

