from django.views.generic import View, TemplateView, DetailView

from opinno.apps.starwars.models import Planet, Starship, Character, Film, CharacterImage, RecentlyVisited


class RecentlyVisitedMixin(View):
    def dispatch(self, request, *args, **kwargs):
        output = super().dispatch(request, *args, **kwargs)

        try:
            RecentlyVisited.objects.create(
                session=request.session.session_key,
                url=request.build_absolute_uri()
            )
        except Exception as e:
            pass

        return output


class HomeView(TemplateView, RecentlyVisitedMixin):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characters'] = Character.objects.all()
        context['films'] = Film.objects.all()
        return context


class RecentlyVisitedView(TemplateView, RecentlyVisitedMixin):
    template_name = 'recently_visited.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recently_visited'] = RecentlyVisited.objects.filter(session=self.request.session.session_key).order_by('-created_at')[:10]
        return context


class PlanetView(DetailView, RecentlyVisitedMixin):
    template_name = 'planet.html'
    model = Planet


class StarshipView(DetailView, RecentlyVisitedMixin):
    template_name = 'starship.html'
    model = Starship


class CharacterView(DetailView, RecentlyVisitedMixin):
    template_name = 'character.html'
    model = Character


class FilmView(DetailView, RecentlyVisitedMixin):
    template_name = 'film.html'
    model = Film
