<template>
  <div id="buscaeventos">
    <div class="row">
      <div class="col s12 m4">
        <label for="titulo">Título do evento</label>
        <input type="text" name="titulo">
      </div>
      <div class="col s12 m2">
        <label for="data_inicial">Data do evento</label>
        <input type="text" name="data_inicial">
      </div>
      <div class="col s12 m1">
        <p>a</p>
      </div>
      <div class="col s12 m2">
        <input type="text" name="data_final">
      </div>
    </div>
    <div class="row">
      <div class="col s12 m4">
        <p>
          <h5 class="label">Publicação do evento</h5>
          <label>
            <input name="pub_evento" type="radio" checked>
            <span>Todos</span>
          </label>
          <label>
            <input name="pub_evento" type="radio" checked>
            <span>Rascunho</span>
          </label>
          <label>
            <input name="pub_evento" type="radio" checked>
            <span>Publicado</span>
          </label>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "buscaeventos",
  components: {},
  mounted: function() {}
};
</script>
