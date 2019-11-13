from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def index(request):
    return render(request,'Cinema/index.html')
def movielist(request):
    return render(request,'Cinema/movielist1.html')
def moviesingle(request):
    return render(request,'Cinema/moviesingle.html')
def user(request):
    return render(request,'Cinema/userprofile.html')
# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#
#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "/"
#
#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "registration/register.html"
#
#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()
#
#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)
#
#
#
# class LoginFormView(FormView):
#     form_class = AuthenticationForm
#
#     # Аналогично регистрации, только используем шаблон аутентификации.
#     template_name = "registration/login.html"
#
#     # В случае успеха перенаправим на главную.
#     success_url = "/"
#
#     def form_valid(self, form):
#         # Получаем объект пользователя на основе введённых в форму данных.
#         self.user = form.get_user()
#
#         # Выполняем аутентификацию пользователя.
#         login(self.request, self.user)
#         return super(LoginFormView, self).form_valid(form)
# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             # Return a 'disabled account' error message
#             ...
#     else:
#         # Return an 'invalid login' error message.
#         ...


# def register(request):
#     if request.method=='POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password1']
#             user=authenticate(username=username,password=password)
#             login(request,user)
#             return redirect('index')
#     else:
#         form=UserCreationForm()
#     context={'form':form}
#     return render(request,'index.html',context)
