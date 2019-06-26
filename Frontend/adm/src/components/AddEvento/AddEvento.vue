<template>
  <div id="addevento">
    <div class="row">
      <div class="col s12">
        <h2>Adicionar evento</h2>
      </div>
    </div>

    <div class="row">
      <div class="col s12 blue-grey lighten-3 section">
        <p>Publicação</p>
        <div class="row">
          <div class="col s5 m2">
            <label for="data_inicial">Data inicial</label>
            <input type="text" name="data_inicial">
          </div>
          <div class="col m0 center-align">
            <p>a</p>
          </div>
          <div class="col s5 m2">
            <label for="data_final">Data final</label>
            <input type="text" name="data_final">
          </div>

          <div class="col s12 m2">
            <label>Imagem de destaque</label>
            <img
              class="materialboxed"
              data-caption="A picture of a way with a group of trees in a park"
              src="https://lorempixel.com/800/400/nature/4"
            >
          </div>

          <div class="col s12 m5">
            <label for="imglegenda">Legenda</label>
            <input
              placeholder="Digite a legenda da imagem"
              id="imglegenda"
              type="text"
              class="validate"
            >

            <div class="file-field">
              <div class="btn">
                <span>Adicionar</span>
                <input type="file">
              </div>
              <div class="btn red">
                <span>Remover</span>
              </div>
              <div class="file-path-wrapper">
                <input class="file-path validate" type="text">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col s12">
        <label for="titulo">Título do evento</label>
        <input type="text" name="titulo">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "addevento",
  components: {},
  mounted: function() {
    var Imageelems = document.querySelectorAll(".materialboxed");
    var Imageinstances = M.Materialbox.init(Imageelems); // eslint-disable-line
  }
};
</script>

<style>
.materialboxed {
  border-radius: 4px;
  width: 100%;
}
</style>
