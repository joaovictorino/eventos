<template>
  <div id="eventos">
    <div class="row">
      <div class="col s12">
        <h2>Eventos</h2>
        <p>{{$store.state.eventos.count}} itens cadastrados</p>
        <a class="btn btn-flat green">Adicionar novo</a>
      </div>
    </div>
    <div class="row">
      <div class="col s12">
        <BuscaEventos></BuscaEventos>
      </div>
    </div>
    <div class="row">
      <div class="col s12">
        <GridEventos></GridEventos>
      </div>
    </div>
  </div>
</template>

<script>
import BuscaEventos from '@/components/BuscaEventos/BuscaEventos.vue'
import GridEventos from '@/components/GridEventos/GridEventos.vue'

export default {
  name: 'eventos',
  components: {
    BuscaEventos,
    GridEventos
  },
  mounted: function () {}
}
</script>
