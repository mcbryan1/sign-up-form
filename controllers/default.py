def sign():
    return dict()
def store():
    submitted_name = request.vars.name
    submitted_username = request.vars.username
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    results = db.users.insert(
        db_name = submitted_name,
        db_username = submitted_username,
        db_email = submitted_email,
        db_password = submitted_password
    )
    if results:
        return "Succefully"
    else:
        return "Error"

def seeUsers():
    users = db().select(db.users.ALL)
    return dict(users=users)

def login():
    return dict()

def authenticate():
    submitted_username = request.vars.username
    submitted_password = request.vars.password

    if db(db.users.db_username==submitted_username and db.users.db_password==submitted_password).count()>0:
        return "User Logged in Succefully"
    else:
        return "User Not Found. Please Sign up"
    