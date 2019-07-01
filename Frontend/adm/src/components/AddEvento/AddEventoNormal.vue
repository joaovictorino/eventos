<template>
  <div>
    <div class="row">
      <div class="input-field col s12">
        <input type="text" id="autocomplete-input" class="autocomplete">
        <label for="autocomplete-input">Autocomplete</label>
      </div>
    </div>
    <div class="row">
      <div class="col s12">capacidade</div>
    </div>
    <div class="row">
      <div class="col s12">atração</div>
    </div>
    <div class="row">
      <div class="col s12">programação</div>
    </div>
    <div class="row">
      <div class="col s12">categoria</div>
    </div>
    <div class="row">
      <div class="col s12">tag e hashtag</div>
    </div>
    <div class="row">
      <div class="col s12">URL</div>
    </div>
    <div class="row">
      <div class="col s12">inscrição e evento pago</div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  components: {},
  created() {
    var Autoel;
    var Autoinst;
  },
  methods: {
    locaisData() {
      var locais = this.$store.state.locais.local;
      var obj = {};
      for (var i in locais) {
        obj[locais[i].nome] = null;
      }
      this.Autoinst[0].updateData(obj);
    }
  },
  mounted: function() {
    this.Autoel = document.querySelectorAll(".autocomplete");
    this.Autoinst = M.Autocomplete.init(this.Autoel);
    this.locaisData();
  }
};
</script>

<style scoped>
</style>
