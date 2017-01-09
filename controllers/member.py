# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()

@auth.requires_login()
def user_swaps_manage():
    form = SQLFORM.smartgrid(db.t_user_swaps,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def business_manage():
    form = SQLFORM.smartgrid(db.t_business,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def user_business_manage():
    form = SQLFORM.smartgrid(db.t_user_business,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def business_labels_manage():
    form = SQLFORM.smartgrid(db.t_business_labels,onupdate=auth.archive)
    return locals()

