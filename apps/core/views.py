from django.shortcuts import render

def home(request):
    user = request.user
    print(f"Usuário atual: {user} - is_authenticated? {user.is_authenticated} - is_superuser? {user.is_superuser}")
    template_name = 'core/home.html'
    context = {}
    return render(request, template_name, context)
