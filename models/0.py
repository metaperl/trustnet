from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'Referral Bank'
settings.subtitle = 'powered by web2py'
settings.author = 'Terrence Brannon'
settings.author_email = 'schemelab@gmail.com'
settings.keywords = 'home business'
settings.description = 'home business referral network'
settings.layout_theme = 'Default'
settings.database_uri = 'postgresql://metaperl:m0ney123@localhost/refbank'
settings.security_key = '59b7a88a-8157-445a-9efd-4ce05fdb1c95'
settings.email_server = 'localhost'
settings.email_sender = 'schemelab@gmail.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
