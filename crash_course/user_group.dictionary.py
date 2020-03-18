def groups_per_user(group_dictionary):
	user_groups = {}
	# iterate over group_dictionary with 2 iteration variables (key, value) and apply items() method
	for group, value in group_dictionary.items():
		# sub-iterate over only value of the group_dictionary
		for user in value:
		  if user not in user_groups: 
		    # ofcourse user IS NOT in the empty users_group dictionary. We just do that to find the initial value for the key
		    user_groups[user] = [group]
		  else:
		    user_groups[user].append(group) 
		    # the user_groups[user] is essentially the list [group] that we set before. So, after each iteration, we append values to this list
			
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))