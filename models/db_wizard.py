### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_business_labels',
    Field('f_name', type='string',
          label=T('Name')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_business_labels_archive',db.t_business_labels,Field('current_record','reference t_business_labels',readable=False,writable=False))

########################################
db.define_table('t_business',
    Field('f_name', type='string',
          label=T('Name')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_business_archive',db.t_business,Field('current_record','reference t_business',readable=False,writable=False))

########################################
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

db.define_table('t_user_business_archive',db.t_user_business,Field('current_record','reference t_user_business',readable=False,writable=False))

########################################
db.define_table('t_user_swaps',
    Field('f_trustee_id', type='reference auth_user',
          label=T('Trustee Id')),
    Field('f_truster_id', type='reference auth_user',
          label=T('Truster Id')),
    Field('f_trustee_user_business_id', type='reference t_user_business',
          label=T('Trustee User Business Id')),
    Field('f_truster_user_business_id', type='reference t_user_business',
          label=T('Truster User Business Id')),
    Field('f_trustee_ack', type='string',
          label=T('Trustee Ack')),
    Field('f_truster_ack', type='string',
          label=T('Truster Ack')),
    auth.signature,
    format='%(f_trustee_id)s',
    migrate=settings.migrate)

db.define_table('t_user_swaps_archive',db.t_user_swaps,Field('current_record','reference t_user_swaps',readable=False,writable=False))
