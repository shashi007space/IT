from django.shortcuts import render, get_object_or_404, redirect
from .models import Platform, Folder, Link
from .forms import PlatformForm, LinkForm

# ------------------------------
# HOME
# ------------------------------
def home(request):
    platforms = Platform.objects.all().order_by('name')
    return render(request, 'links/home.html', {'platforms': platforms})

# ------------------------------
# ADD PLATFORM
# ------------------------------
def add_platform(request):
    if request.method == 'POST':
        form = PlatformForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('links:home')
    else:
        form = PlatformForm()
    return render(request, 'links/add_platform.html', {'form': form})

# ------------------------------
# DELETE PLATFORM
# ------------------------------
def delete_platform(request, slug):
    platform = get_object_or_404(Platform, slug=slug)
    if request.method == "POST":
        platform.delete()
        return redirect("links:home")
    return render(request, "links/confirm_delete.html", {"platform": platform})


# ------------------------------
# PLATFORM DETAIL (FOLDERS LIST)
# ------------------------------
def platform_detail(request, slug):
    platform = get_object_or_404(Platform, slug=slug)
    folders = platform.folders.all()
    return render(request, "links/platform_detail.html", {
        "platform": platform,
        "folders": folders
    })

# ------------------------------
# ADD FOLDER TO PLATFORM
# ------------------------------
def add_folder(request, slug):
    platform = get_object_or_404(Platform, slug=slug)
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Folder.objects.create(platform=platform, name=name)
        return redirect("links:platform_detail", slug=slug)
    return render(request, "links/add_folder.html", {"platform": platform})

# ------------------------------
# FOLDER DETAIL (LINKS LIST)
# ------------------------------
def folder_detail(request, id):
    folder = get_object_or_404(Folder, id=id)
    links = folder.links.all()
    platform = folder.platform  # pass related platform to template
    return render(request, "links/folder_detail.html", {
        "folder": folder,
        "links": links,
        "platform": platform
    })

# ------------------------------
# ADD LINK TO FOLDER
# ------------------------------
def add_link(request, id):
    folder = get_object_or_404(Folder, id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        url = request.POST.get("url")
        if title and url:
            Link.objects.create(platform=folder.platform, folder=folder, title=title, url=url)
        return redirect("links:folder_detail", id=id)
    return render(request, "links/add_link.html", {"folder": folder})

# ------------------------------
# EDIT LINK
# ------------------------------
def edit_link(request, id):
    link = get_object_or_404(Link, id=id)
    if request.method == "POST":
        link.title = request.POST.get("title")
        link.url = request.POST.get("url")
        link.save()
        return redirect("links:folder_detail", id=link.folder.id)
    return render(request, "links/edit_link.html", {"link": link})

# ------------------------------
# DELETE LINK
# ------------------------------
def delete_link(request, id):
    link = get_object_or_404(Link, id=id)
    folder_id = link.folder.id
    link.delete()
    return redirect("links:folder_detail", id=folder_id)

# ------------------------------
# DELETE FOLDER
# ------------------------------
def delete_folder(request, id):
    folder = get_object_or_404(Folder, id=id)
    slug = folder.platform.slug
    folder.delete()
    return redirect("links:platform_detail", slug=slug)
