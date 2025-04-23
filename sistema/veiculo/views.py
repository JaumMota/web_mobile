from veiculo.models import Veiculo
from django.views.generic import ListView 

class ListarVeiculos(ListView):
    """
    View para listar todos os veiculos cadastrados.
    """
    model = Veiculo 
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'
