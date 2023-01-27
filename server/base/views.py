from django.shortcuts import render


def Home(req,room_name):
    print(room_name)
    return render(req,'home.html',{
        'room_name':room_name
    })
