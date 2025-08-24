import enum

class Permission(enum.IntFlag):
    SECRETARY=1
    AUDITOR=2
    DEPARTMENT=4
    ADMIN=8
    SUPERADMIN=16

@enum.unique
class ActivityStatus(enum.IntEnum):
    DRAFT=0
    PENDING=1
    EFFECTIVE=2
    REJECTED=3
    MERGED=4
    UNMERGED=5
    RECYCLED=6

@enum.unique
class TokenType(enum.IntEnum):
    FIRSTLOGIN=0
    PERSIST=1
    AUTHORIZE=2
    REFRESH=3
    RECOVERY=4
    DYNAMIC=5
    XHAUTH=127

@enum.unique
class UserHistoryType(enum.IntEnum):
    CREATE=0
    RENAME=1
    CHANGE_PWD=2
    CHANGE_CLASS=3
    CHANGE_PERM=4