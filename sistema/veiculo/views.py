from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.views import View
from veiculo.models import Veiculo
from veiculo.forms import FormularioVeiculo
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from veiculo.serializers import SerializadorVeiculo

class ListarVeiculos(LoginRequiredMixin, ListView):
    """
    View para listar todos os veiculos cadastrados.
    """
    model = Veiculo 
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class CriarVeiculos(LoginRequiredMixin, CreateView):
    """
    View para a criação de novos veiculos.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):
    """
    View para retornar a foto de um veiculo.
    """
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
            return Http404('Foto não encontrada ou acesso negado.')
        except Exception as exception:
            return exception
        

class EditarVeiculos(LoginRequiredMixin, UpdateView):

    """
    View para editar veiculos ja cadastrados.
    """
    
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    """
    View para deletar veiculos ja cadastrados.
    """
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

class APIListarVeiculos(ListAPIView):

    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()