from django.shortcuts import redirect, render
from . models import Category,Photo 
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy



def galler(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)



    categories = Category.objects.all()
    
    context = {'categories': categories, 'photos':photos}
    return render(request, 'galapp/gallery.html', context)

def add(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        print('date:', data)
        print('image:', image)

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None
        
        photo = Photo.objects.create(
            category=category,
            description = data['description'],
            images = image,
        )

        return redirect('gallery')



    context = {'categories': categories}
    return render(request, 'galapp/add.html', context)


def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'galapp/photo.html', {'photo': photo})

class viewdelete(DeleteView):
    model = Photo
    template_name = 'galapp/delete.html'
    success_url = reverse_lazy('gallery')
    context_object_name = 'photo'

