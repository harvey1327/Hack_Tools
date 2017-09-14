#!/usr/bin/env python

import requests

#token_array = [{'user_id': 1, 'token': 'JhjqCzT79ofx94SxL6rn'},{'user_id': 2, 'token': '7Dsk5VR6xD_goeKcxFps'},{'user_id': 3, 'token': 'EmSLzXwfKddc2y28pcxW'}, {'user_id': 4, 'token': 'yBETvpQLH7UkAmXbdGo-'}]

token_array = [{'user_id': 2, 'token': '7Dsk5VR6xD_goeKcxFps', 'user_name':'balh'},{'user_id': 3, 'token': 'EmSLzXwfKddc2y28pcxW', 'user_name':'test1'}, {'user_id': 4, 'token': 'yBETvpQLH7UkAmXbdGo-', 'user_name':'user4'}]

group_array = [{'group_id': 1, 'group_name': 'group1'},{'group_id': 2, 'group_name': 'group2'},{'group_id': 3, 'group_name': 'group3'},{'group_id':4, 'group_name': 'testgroup'}, {'group_id':5, 'group_name': 'group4'}]

new_user_id = 2
domain = 'http://127.0.0.1:10080'

for groupD in group_array:
    for tokenD in token_array:
        user_id = tokenD['user_id']
        user_name = tokenD['user_name']
        token = tokenD['token']
        group_id = groupD['group_id']
        group_name = groupD['group_name']

        if user_id != new_user_id:
            url = '%s/api/v3/groups/%s/members' % (domain, group_name)
            payload = {'id': group_name, 'user_id': new_user_id, 'access_level': '30'}
            headers = {'PRIVATE-TOKEN': token}
            
            r = requests.post(url, data=payload, headers=headers)
            output = 'StatusCode-%s, GroupName-%s, AuthUser-%s, Text-%s' % (r.status_code, group_name, user_name, r.text)
            if r.status_code == 201:
                print output
                break
            else:
                print output
