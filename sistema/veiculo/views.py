from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy

class ListarVeiculos(ListView):
    """
    View para listar todos os veiculos cadastrados.
    """
    model = Veiculo 
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculos(CreateView):
    """
    View para a criação de novos veiculos.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')
