from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from accounts.models import Profile
from idea.models import Idea_image_storage, Idea

def submit(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            IdeaName = request.POST['IdeaName']
            IdeaSubtitle = request.POST['IdeaSubtitle']
            IdeaContent = request.POST['IdeaContent']
            images = request.FILES.getlist('images')
            #contents = request.POST['contents']
            #image = request.FILE.get('image')
            '''
            user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
            idea_title = models.CharField(max_length=20 ,  blank = True)
            idea_subtitle = models.TextField(max_length=100,  blank = True)
            idea_image = models.ImageField(upload_to="", null=True, blank = True)
            idea_description = models.TextField(max_length=500,  blank = True)
            idea_hashtag = models.TextField(max_length=100,  blank = True)
            idea_likecount = models.IntegerField(null=True, blank = True)
            idea_create_data = models.DateTimeField(default = timezone.now) # 생성날짜
            idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
            image = models.ImageField(upload_to="", null = True, blank = True)
            '''

            if request.user.is_authenticated == True:
                profile = get_object_or_404(Profile.objects.all().filter(email = request.user.email))

                if images :

                    newidea = Idea.objects.create(
                        user = profile,
                        idea_title = IdeaName,
                        idea_subtitle = IdeaSubtitle,
                        idea_description = IdeaContent,
                        idea_likecount = 0,
                        idea_image = images[0],
                    )

                    for img in images:
                        newimage = Idea_image_storage.objects.create(
                        idea = newidea,
                        image = img
                    )
            
                    return redirect('/detail/' + str(newidea.id))

                else:
                    newidea = Idea.objects.create(
                        user = profile,
                        idea_title = IdeaName,
                        idea_subtitle = IdeaSubtitle,
                        idea_description = IdeaContent,
                        idea_likecount = 0,
                    )
                    return redirect('/detail/' + str(newidea.id))
            else:
                return render(request, 'submit.html', {
                    "errro" : "this is error"
                })
        else:
            return render(request, 'submit.html', {
                "errro" : "this is error"
            })
    else:
        return render(request, 'signin.html')