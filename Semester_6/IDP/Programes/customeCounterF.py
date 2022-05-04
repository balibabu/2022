#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:05:05 2022

@author: student
"""

users = [{"id":0, "name":"Hero"},{"id":1,"name":"Dunn"},{"id":2, "name":"Sue"},{"id":3,"name":"Chi"},{"id":4, "name":"Thor"},{"id":5,"name":"Clive"},{"id":6, "name":"Hicks"},{"id":7, "name":"Devin"},{"id":8, "name":"Kate"},{"id":9, "name":"Klein"}]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1,3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6,8), (7, 8), (8, 9)]

friendsId=[user['id'] for user in users]

friends={user['id']:[] for user in users}
for i,j in friendship_pairs:
    friends[i].append(j)
    friends[j].append(i)

from collections import Counter # not loaded by default
friendships=friends
def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id] # For each of my friends,
            for foaf_id in friendships[friend_id] # find their friends
                if foaf_id != user_id and foaf_id not in friendships[user_id] # and aren't my friends.
    )
#print(friends_of_friends(users[3]))
#print(friends)


def counter(friends_of_user,user):
    mutualF=set()
    tempFr=friends_of_user[user]
    for i in tempFr:
        for j in friends_of_user[i]:
            if j not in tempFr and j!=user:
                mutualF.add(j)
    
    
    c=dict()
    for i in mutualF:
        c[i]=len(set(friends_of_user[i])&set(tempFr))
    print(c)
                   
    
counter(friends,3)
    
    
'''tempFr=friends[i]
for j in tempFr:
   for fr in friends[j]:
       if fr not in tempFr and fr!=i: 
           mutualF[i].add(fr)'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    