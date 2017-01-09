I have a database table which references the web2py-supplied
`auth_user` table:

db.define_table('t_user_business',
    Field('f_user_id', type='reference auth_user',
          label=T('User Id')),
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_link', type='string',
          label=T('Link')),
    Field('f_importance', type='integer',
          label=T('Importance')),
    auth.signature,
    format='%(f_user_id)s',
    migrate=settings.migrate)

I would like to design a page which has a form that lists all the
current entries in this table for the authenticated
user. E.g. something along the lines of 

    db.t_user_business.f_user_id==3

Where `3` is replaced with the `auth_user.id` value of the currently
logged in user.

Also, s same page, I would like to have a form that allows the user to
enter a new record for this table and upon submission it commits this
validated record to the database.
