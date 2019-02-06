from django.views import generic
from .models import Record, Recordwoman, Recordroadman, Recordroadwoman, Recordtrackworldman, Recordtrackworldwoman, Recordroadworldman, Recordroadworldwoman


class IndexView(generic.ListView):
    model = Record



class IndextrackwomanView(generic.ListView):
    model = Recordwoman


class IndexroadmanView(generic.ListView):
    model = Recordroadman


class IndexroadwomanView(generic.ListView):
    model = Recordroadwoman

class IndextrackworldmanView(generic.ListView):
    model = Recordtrackworldman
"""

class IndextrackworldwomanView(generic.ListView):
    model = Recordtrackworldwoman


class IndexroadworldmanView(generic.ListView):
    model = Recordroadworldman


class IndexroadworldwomanView(generic.ListView):
    model = Recordroadworldwoman
"""