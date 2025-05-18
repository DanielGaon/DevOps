def person_info(name,height,age,like,**others):
    print("Name: {name}, Height: {height}, Age: {age}")
    if like=='yes':
        print('I like this person')
    else:
        print('I dont like this person')
    



person_info('Dave',1.68,24,'No',phone=99999)

