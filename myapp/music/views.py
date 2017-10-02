from django.http import HttpResponse
from django.http import Http404
#from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Album


def index(request):
	html = ''
	all_albums = Album.objects.all()
	# print(all_albums)
	# for album in all_albums:
	# 	url = '/music/' + str(album.id) +  '/'
	# 	html += '<a href=" ' + url + '">' + album.album_title + '</a><br>'
	#template = loader.get_template('music/index.html')
	# context = {
	# 	'all_albums': all_albums,
	# }
	#return HttpResponse(template.render(context,request))
	#return HttpResponse(html)
	return render(request,'music/index.html',{'all_albums': all_albums})


def detail(request,album_id):
	#return HttpResponse("<h2> Details for album id" + str(album_id) + "</h2>")
	# try:
	# 	album = Album.objects.get(pk=album_id)
	# except:
	# 	raise Http404('album does not exist')
	#template = loader.get_template('music/detail.html')
	#return HttpResponse(template.render({'album': album}))
	album =  get_object_or_404(Album,pk=album_id)
	return render(request,'music/detail.html',{'album': album})
