<template>
  <div id="addevento">
    <div class="row">
      <div class="col s12">
        <h2>Adicionar evento</h2>
      </div>
    </div>

    <ActionBar/>

    <div class="row">
      <div class="col s12 blue-grey lighten-3 section">
        <p>Publicação</p>
        <div class="row">
          <div class="input-field col s12 m4">
            <p>
              <span class="radio-title">Tipo de evento</span>
              <label>
                <input name="tipo_evento" type="radio" @click="$store.state.tipoEvento = 'evento'">
                <span>Evento</span>
              </label>
              <label>
                <input
                  name="tipo_evento"
                  type="radio"
                  @click="$store.state.tipoEvento = 'megaevento'"
                >
                <span>Mega Evento</span>
              </label>
            </p>
          </div>

          <div class="input-field col s5 m2">
            <label for="data_inicial">Data inicial</label>
            <input type="text" name="data_inicial">
          </div>
          <div class="col m0 center-align">
            <p>a</p>
          </div>
          <div class="input-field col s5 m2">
            <label for="data_final">Data final</label>
            <input type="text" name="data_final">
          </div>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col s12 m2">
        <label v-if="$store.state.tipoEvento === 'evento'">Imagem de destaque</label>
        <label v-else-if="$store.state.tipoEvento === 'megaevento'">Logotipo</label>
        <label v-else>Imagem de destaque</label>
        <img
          class="materialboxed"
          data-caption="A picture of a way with a group of trees in a park"
          src="https://lorempixel.com/800/400/nature/4"
        >
      </div>

      <div class="input-field col s12 m5">
        <label for="imglegenda">Legenda</label>
        <input id="imglegenda" type="text" class="validate">

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

    <div class="row">
      <div class="input-field col s12">
        <label for="evento_titulo">Título do evento</label>
        <input type="text" name="evento_titulo">
      </div>
    </div>

    <div class="row">
      <div class="input-field col s12">
        <label for="evento_descricao">Descrição</label>
        <textarea id="evento_descricao" class="materialize-textarea"></textarea>
      </div>
    </div>

    <div class="row">
      <div class="input-field col s4 m2">
        <label for="evento_data_inicial">Data inicial</label>
        <input type="text" name="evento_data_inicial">
      </div>
      <div class="input-field col s4 m2">
        <label for="evento_data_final">Data final</label>
        <input type="text" name="evento_data_final">
      </div>
      <div class="input-field col s4 m2">
        <label for="evento_hora_inicio">Horário início</label>
        <input type="text" name="evento_hora_inicio">
      </div>
      <div class="input-field col s4 m2">
        <label for="evento_hora_fim">Horário fim</label>
        <input type="text" name="evento_hora_fim">
      </div>
    </div>

    <div v-if="$store.state.tipoEvento === 'evento'">
      <add-evento-normal/>
    </div>
    <div v-else-if="$store.state.tipoEvento === 'megaevento'">
      <add-mega-evento/>
    </div>
  </div>
</template>

<script>
import ActionBar from "@/components/ActionBar/ActionBar.vue";

import AddEventoNormal from "@/components/AddEvento/AddEventoNormal.vue";
import AddMegaEvento from "@/components/AddEvento/AddMegaEvento.vue";

export default {
  name: "addevento",
  components: {
    ActionBar,
    AddEventoNormal,
    AddMegaEvento
  },
  methods: {},
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
