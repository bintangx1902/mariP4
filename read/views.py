from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from backend.models import Book, Category
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import *
from django.db.models import Count, Q
from members.models import UserProfile

link = 'link'


class AllBooksList(TemplateView):
    template_name = 'read/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AllBooksList, self).get_context_data(*args, **kwargs)
        fav_book = Book.objects.all().order_by('rating')[:6]
        book_total = Book.objects.all().count()
        member = User.objects.all().count()
        category = Category.objects.all().count()

        context['fav_books'] = fav_book
        context['book_total'] = book_total
        context['member'] = member
        context['category'] = category
        return context


# def like_view(request, pk):
#     book = get_object_or_404(Book, id=request.POST.get('book_id'))
#     current_score = book.current_rate()
#     rated = False
#     # Delete rating the book
#     if book.user_rating.filter(id=request.user.id).exists():
#         pass
#     else:
#         book.user_rating.add(request.user)
#         current_score += int(request.POST.get('rating_point'))
#         rated = True
#
#     return HttpResponseRedirect(reverse('book-detail', args=[str(pk)]))


class BookDetailView(DetailView):
    template_name = 'read/details.html'
    # template_name = 'read/base1.html'
    query_pk_and_slug = True
    slug_url_kwarg = link
    slug_field = link
    model = Book

    def get_context_data(self, *args, **kwargs):
        context = super(BookDetailView, self).get_context_data(*args, **kwargs)
        category = Category.objects.all()
        tile = Book.objects.get(link=self.kwargs['link'])
        profile_ = UserProfile.objects.filter(user_id=Book.objects.get(pk=tile.pk).uploader)
        if profile_ is not None:
            profile = UserProfile.objects.get(user_id=Book.objects.get(pk=tile.pk).uploader)
            context['profile'] = profile
        else:
            pass

        context['category'] = category
        return context


class AddComment(CreateView):
    model = Comment
    form_class = AddCommentForms
    template_name = 'read/add-comment.html'
    query_pk_and_slug = True
    slug_field = link
    slug_url_kwarg = link

    def get_success_url(self):
        return reverse('read:detail', args=[str(self.kwargs[link])])

    def form_valid(self, form):
        pk = Book.objects.get(link=self.kwargs[link])
        form.instance.book_id = pk.pk
        form.instance.name_id = self.request.user.id
        return super().form_valid(form) and HttpResponseRedirect(self.get_success_url())

    @method_decorator(login_required(login_url="/accounts/login/"))
    def dispatch(self, request, *args, **kwargs):
        return super(AddComment, self).dispatch(request, *args, **kwargs)

# def CategorySearch(req, cats):
#     cate = Book.objects.filter(category=cats.replace('-', ' '))
#     con = {
#         'cats': cats.replace('-', ' ').title(),
#         'category_posts': cate
#     }
#     return render(req, '', con)


class AllBookList(ListView):
    model = Book
    template_name = 'read/list.html'
    paginate_by = 6
    ordering = ['-pk']

    def get_queryset(self):
        qq = self.request.GET.get('q')
        if qq is not None:
            object_list = Book.objects.filter(
                Q(title__icontains=qq) | Q(link__icontains=qq) | Q(description__icontains=qq)
            ).order_by('-pk')
        else:
            object_list = Book.objects.all().order_by('-pk')

        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(AllBookList, self).get_context_data(*args, **kwargs)
        fav_book = Book.objects.all().order_by('rating')[:4]
        new_book = Book.objects.all().order_by('-pk')[:1]
        cat = Category.objects.all().order_by('-pk')[:3]

        context['category'] = cat
        context['new_book'] = new_book
        context['fav_books'] = fav_book
        return context
