<template>
  <div id="eventos">
    <div class="row">
      <div class="col s12">
        <h2>Eventos</h2>
        <p>{{$store.state.eventos.count}} itens cadastrados</p>
        <router-link to="/eventos/adicionar" class="btn btn-flat green white-text">Adicionar novo</router-link>
      </div>
    </div>
    <div class="buscaeventos">
      <BuscaEventos></BuscaEventos>
    </div>
    <div class="grideventos">
      <GridEventos></GridEventos>
    </div>
  </div>
</template>

<script>
import BuscaEventos from '@/components/BuscaEventos/BuscaEventos.vue';
import GridEventos from '@/components/GridEventos/GridEventos.vue';

export default {
  name: 'eventos',
  components: {
    BuscaEventos,
    GridEventos
  },
  mounted: function () {}
};
</script>
