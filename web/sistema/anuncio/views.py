from django.shortcuts import render
from django.urls import reverse_lazy
from anuncio.models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from anuncio.forms import FormularioAnuncio

class ListarAnuncios(ListView):

    """
    View para listar veiculos cadastrados.
    """

    model = Anuncio
    context_object_name = 'anuncios'
    template_name = 'anuncio/listar.html'


class CriarAnuncios(LoginRequiredMixin, CreateView):

    
    #View para a criação de novos veiculos.
    
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')

class EditarAnuncios(LoginRequiredMixin, UpdateView):

    """
    View para editar veiculos ja cadastrados.
    """
    
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar.html'
    success_url = reverse_lazy('listar-anuncios')

class DeletarAnuncio(LoginRequiredMixin, DeleteView):

    """
    View para deletar veiculos.
    """

    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('listar-anuncios')