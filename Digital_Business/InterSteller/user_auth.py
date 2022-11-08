def authonticate(email):
    auth = userlogin.objects.filter(Emails=email).values()
    user_id = ""
    for item in auth:
        if item['Emails'] == email :
          user_id = item['Emails']
        # if item == cheking_user:
        #     user_id = 'logged'
        # else:
        #     user_id = 'unknown'
    return user_id