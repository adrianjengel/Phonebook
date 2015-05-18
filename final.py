#!usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple phonebook module."""
import pickle


def dump():
    """For saving new contacts when added.

    Args: None
    Returns: None
    Examples:
        >>> Enter your choice (1-4) here: 1
        >>> Enter new contact name: sam
        >>> Enter contact child name: sammy
        >>> Enter contact phone number: 12345
        .... You have added a new contact!
    """
    phonebook = open('phonebook.txt', 'wb')
    pickle.dump(CONTACTS, phonebook)
    phonebook.close()


def load():
    """For loading past contacts.

    Args: None
    Returns: None
    Examples:
        >>> Enter your choice (1-4) here: 1
        ... JIM ('JIMMY', '88888')
        ... KIM ('KIMMY', '12335')
        ... SAM ('SAMMY', '12345')
        ... TIM ('TIMMY', '22222')
    """
    global CONTACTS
    try:
        phonebook = open('phonebook.txt', 'rb')
        CONTACTS = pickle.load(phonebook)
    except IOError or EOFError:
        CONTACTS = {}

load()

ANSWER = True
while ANSWER:
    print '-------Phonebook Menu-------''\n'
    print '1. Add a new contact name'
    print '2. Delete an existing contact'
    print '3. Edit existing contact'
    print '4. Search for an existing contact by name'
    print '5. Display all'
    print '6. Exit phonebook'
    ANSWER = raw_input('\nEnter your choice (1-4) here: ')
    print '---------------------------''\n'
    if ANSWER == '1':
        NAME = raw_input('\nEnter new contact name: ')
        CHILD = raw_input('\nEnter contact child name: ')
        PHONE = raw_input('\nEnter contact phone number: ')
        CONTACTS[NAME] = [CHILD, PHONE]
        print '---------------------------''\n'
        print 'You have added a new contact!''\n'
        dump()

    elif ANSWER == '2':
        REMOVE = raw_input('\nEnter the name you wish to delete: ')
        if REMOVE in CONTACTS:
            del CONTACTS[REMOVE]
            print REMOVE.upper(), ':', 'Has been removed from the the phonebook'
            dump()
        else:
            print '---------------------------''\n'
            print REMOVE.upper(), ':', 'Does not exist in the phonebook!'
            dump()

    elif ANSWER == '3':
        EDIT = raw_input('\nEnter the name you wish to edit: ').upper()
        if EDIT in CONTACTS:
            print EDIT
            NAME = raw_input('Enter new name: ')
            CHILD = raw_input('Enter new child: ')
            PHONE = raw_input('Enter new phone number: ')
            CONTACTS[NAME] = [CHILD, PHONE]
            del CONTACTS[EDIT]
            print '\n''You have updated your contact!'
            dump()

    elif ANSWER == '4':
        SEARCH = raw_input('\nWho are you looking for? ')
        print '---------------------------''\n'
        if SEARCH in CONTACTS:
            print SEARCH.upper(), ':'
            print CONTACTS[SEARCH][0].upper(), CONTACTS[SEARCH][1]
        else:
            print SEARCH.upper(), ':', 'Does not exist in the phonebook!'
    elif ANSWER == '5':
        print '---------------------------''\n'
        for key, value in sorted(CONTACTS.items()):
            print key.upper(), (value[0].upper(), value[1])

    elif ANSWER == '6':
        print 'Have a nice day!'
        break
