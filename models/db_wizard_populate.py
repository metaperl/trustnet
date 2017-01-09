from gluon.contrib.populate import populate
if db(db.auth_user).isempty():
     populate(db.auth_user,10)
     populate(db.t_business_labels,10)
     populate(db.t_business,10)
     populate(db.t_user_business,10)
     populate(db.t_user_swaps,10)
