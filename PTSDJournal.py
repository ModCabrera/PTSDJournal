#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PTSD Journal Main Module"""
from collections import OrderedDict
import datetime
import json
import os
import sys     
        

def journal():
    """Journal Navigation, Execution.
    Args:
        choice (bool) default:None = Menu Choice.
    Returns:
        None
    Examples:
    >>>journal()
    A] ---- Add Journal Entry
    S] ---- Search Journal Entry
    V] ---- View Journal Entry
    Make A Selection:
    """
    choice = None
    while choice != 'Q':
        for key, value in main_menu.items():
            print '%s] ---- %s' % (key, value.__doc__)
        choice = raw_input('Make A Selection: ').upper().strip()
        if choice in main_menu:
            main_menu[choice]()


def add_page():
    "Add Journal Entry."
    """
    Args:
        user_input (str) = Log for Journal Entry.
        day (str) = Date in Year-Month-Day.
    Returns:
        None
    Examples:
        Hello, Please Enter Journal Log for Today: I want to add a page
        Save entry? [Yes or No]y
        ************************************************************************
        Entry Log Complete
        ________________________________________________________________________
    """
    user_input = raw_input('Hello, Please Enter Journal Log for Today: ')
    day = str(datetime.date.today())
    if user_input and raw_input('Save entry? [Yes or No]')[:1].strip().lower() != 'n':
        log = {}
        if os.path.isfile('Journal_Log'):
            with open('Journal_Log', 'r+') as open_file:
                read_entry = json.load(open_file)
                for date, entry in read_entry.items():
                    log[date] = entry
                log[day] = user_input
            add_entry = open('Journal_Log', 'w')
            json.dump(log, add_entry, sort_keys=True)
            print '*' * 80
            print 'Entry Log Complete'
            print '_' * 80
        else:
            log = {day:user_input}
            with open('Journal_Log', 'w+') as new_entry:
                json.dump(log, new_entry, sort_keys=True)
            new_entry.close()
            print '*' * 80
            print 'Entry Log Complete'
            print '_' * 80
            

def search_page():
    "Search Journal Entry"
    """
    Args:
        page_year = Search Year.
        page_month = Search Month.
        page_day = Search Day.
    Returns:
        None
    Examples:
        Enter Year: 2015
        Enter Month: 05
        Enter Day: 17
        ************************************************************************
        Journal Entry Date: 2015-05-17
        ________________________________________________________________________
        Journal Entry Does Not Exist.
        ************************************************************************
    """
    try:
        if os.path.isfile('Journal_Log'):
            page_year = raw_input('Enter Year: ')
            page_month = raw_input('Enter Month: ')
            page_day = raw_input('Enter Day: ')
            date_search = (page_year+'-'+page_month+'-'+page_day)
            search_result = {}
            with open('Journal_Log', 'r') as search_entry:
                opensearch = json.load(search_entry)
                for date, entry in opensearch.items():
                    if date_search == date:
                        search_result[date] = entry
                print '*' * 80
                print 'Journal Entry Date: '+ date_search
                print '_' * 80
                print search_result[date_search]
                print '_' * 80
    except LookupError:
        print 'Journal Entry Does Not Exist.'
        print '*' * 80


def view_page():
    "View Journal Entry"
    """
    Args:
        view_all = Opens Journal File.
    Returns:
        None
    Examples:
        Make A Selection: v
        ************************************************************************
        Entry Date: 2015-05-17
        ========================================================================
        I want to add a page
        ________________________________________________________________________
    """
    if os.path.isfile('Journal_Log'):
        with open('Journal_Log', 'r') as view_file:
            view_all = json.load(view_file)
            for date, entry in view_all.items():
                print '*' * 80
                print 'Entry Date: ' + date
                print '=' * 80
                print entry
                print '_' * 80


main_menu = OrderedDict([('A', add_page),
                         ('S', search_page),
                         ('V', view_page)
                         ])


if __name__ == '__main__':
    PTSD_JOURNAL = journal()
