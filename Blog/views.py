import os
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from . models import Blog
from django.conf import settings
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

# An email will be sent to these id's with a link attached to aprrove the blog requests that people submit

admin_emails = ['mayankchaurasia.bsp@gmail.com','yash199649@gmail.com']

def blog(request):
    blogs = Blog.objects.filter(allow=True)
    blogs = sorted(blogs,key=lambda x: x.created,reverse=True)
    return render(request,'Blog/blog.html',{'blogs':blogs})

IMAGE_FILE_TYPES = ['png','jpg','jpeg']
def add_blog(request):
    if request.method == 'GET':
        return render(request,'Blog/blog_add_new.html')
    else:
        print("POST BLOG REQUEST")
        name = request.POST['name']
        description = request.POST['description']
        designation = request.POST['designation']
        title = request.POST['title']
        try:
            image = request.FILES['image']
        except Exception as e:
            print(e)
            image = 'default.png'
        type = str(image).split('.')[-1]
        type = type.lower()
        if type not in IMAGE_FILE_TYPES:
            print("Wrong image format")
            return HttpResponse("wrong_image_format")

        blog = Blog()
        blog.author = name
        blog.designation = designation
        blog.description = description
        blog.title = title
        blog.image = image
        blog.save()
        approve = str(request.get_host()) + "/blog/approve/" + str(blog.pk)
        message = "<b>Author</b> : " + str(name)
        message += "<br><b>Designation</b> : " + str(designation)
        message += "<br><b>Title</b> : "+str(title)
        message += "<br><b>Description</b> : "+str(description)
        message += "<br>Click <a href=\""+"http://127.0.0.1:8000/blog/approve/"+str(blog.id)+"\">here</a> to approve this post"
        try :
            fp = open(os.path.join(settings.MEDIA_ROOT, str(image)), 'rb')
            msg_img = MIMEImage(fp.read())
            email = EmailMultiAlternatives("Approve a Blog request", message, settings.EMAIL_HOST_USER, to=admin_emails)
            email.content_subtype = 'html'
            email.mixed_subtype = 'related'
            email.attach(msg_img)
            email.send()
        except Exception as e:
            print(e)
            return HttpResponse("could_not_send_email")
        print("Successful in sending email for blog request")
        return HttpResponse("successful")

def approve_blog(request,blog_id):
    blogs = Blog.objects.filter(allow=True)
    blogs = sorted(blogs, key=lambda x: x.created, reverse=True)
    if request.user.is_authenticated():
        try :
            blog = Blog.objects.get(pk=int(blog_id))
        except Exception as e:
            print(e)
            return redirect('/blog')
        blog.allow = "True"
        blog.save()
        print("Successfully approved a blog..")
        return render(request, 'Blog/blog.html', {'blogs': blogs,'message':"Approval accepted"})

    else:
        print("Forbidden. Admin not logged in !")
        return render(request, 'Blog/blog.html', {'blogs': blogs, 'message': "Forbidden. Admin not logged in !"})

def blog_full(request,blog_id):
    print(blog_id)
    try:
        blog = Blog.objects.get(pk=int(blog_id))
    except Exception as e:
        print(e)
        return redirect('/blog')
    return render(request,'Blog/blog_full_new.html',{'blog':blog})







