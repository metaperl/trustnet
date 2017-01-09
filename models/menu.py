response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description

response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]


def logged_in_menu():

    response.menu += [
        (T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
        (T('Add Program'),URL('member','user_business_manage')==URL(),URL('member','user_business_manage'),[]),
        (T('User Swaps'),URL('default','user_swaps_manage')==URL(),URL('default','user_swaps_manage'),[]),
        (T('Business'),URL('default','business_manage')==URL(),URL('default','business_manage'),[]),

        (T('Business Labels'),URL('default','business_labels_manage')==URL(),URL('default','business_labels_manage'),[]),
        ]

def menu_item(menu_item_text, url, sub_menu=[], display=True):
    # First element of tuple is the text of the meny item.
    retval = list(menu_item_text)

    # Second element of the tuple indicates if this menu item is the
    # current active one.
    retval.append(url == URL())

    # Third element is the link to follow when this item is selected.
    retval.append(url)

    # The fourth item is an optional sub_menu.
    retval.append(sub_menu)

    # The fifth menu item determines whether to display it.
    retval.append(display)

    return retval


def public_menu_verbose():

    response.menu += [
        ('How it Works', URL('default','how_it_works')==URL(), URL('default','how_it_works'),[]),
        ('Testimonials', URL('default','testimonials')==URL(), URL('default','testimonials'),[]),
        ('Sign Up Now!', URL('default', 'user', args=['register'])==URL(), URL('default','user', args=['register']),[]),
        ('Login', URL('default', 'user', args=['login'])==URL(),URL('default','user', args=['login']),[]),
        ]

def public_menu():
    response.menu += [
        menu_item('How it Works', URL('default','how_it_works')),
        menu_item('Testimonials', URL('default','testimonials')),
        menu_item('Sign Up Now!', URL('default', 'user', args=['register'])),
        menu_item('Login', URL('default', 'user', args=['login']))
        ]


if auth.is_logged_in():
    logged_in_menu()
else:
    public_menu()
