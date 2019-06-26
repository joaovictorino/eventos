<template>
  <div id="buscaeventos">
    <div class="row">
      <div class="col s12 m5">
        <label for="titulo">Título do evento</label>
        <input type="text" name="titulo">
      </div>
      <div class="col s5 m1">
        <label for="data_inicial">Inicial</label>
        <input type="text" name="data_inicial">
      </div>
      <div class="col m0 center-align">
        <p>a</p>
      </div>
      <div class="col s5 m1">
        <label for="data_final">Final</label>
        <input type="text" name="data_final">
      </div>

      <div class="col s12 m4">
        <p>
          <label>Publicação do evento</label>
          <br>
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

    <div class="row"></div>

    <div class="row">
      <div class="col s12 m4">
        <select multiple>
          <option value disabled>Subprefeitura</option>
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
        </select>
        <label>Subprefeitura</label>
      </div>

      <div class="col s12 m4">
        <select multiple>
          <option value disabled>Local</option>
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
        </select>
        <label>Local</label>
      </div>

      <div class="col s12 m3">
        <select multiple>
          <option value disabled>Categorias</option>
          <option value="1">Option 1</option>
          <option value="2">Option 2</option>
          <option value="3">Option 3</option>
        </select>
        <label>Categorias</label>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "buscaeventos",
  components: {},
  mounted: function() {
    var Selectelems = document.querySelectorAll("select");
    var Selectinstances = M.FormSelect.init(Selectelems); // eslint-disable-line
  }
};
</script>
