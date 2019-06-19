<template>
  <div id="grideventos">
    <div class="row">
      <div class="col s12">
        <div class="grid-block t8">
          <div class="grid-header">
            <div
              class="grid-item"
              v-for="(header,key) in $store.state.eventos.grid"
              :key="key"
            >{{header.col}}</div>
          </div>
          <div class="grid-body">
            <div class="grid-item" v-for="(item,key) in $store.state.eventos.item" :key="key">
              <div>{{item.titulo}}</div>
              <div>{{item.megaevento}}</div>
              <div>{{item.subcategoria}}</div>
              <div>{{item.local}}</div>
              <div>{{item.dataevento}}</div>
              <div>{{item.datapublicacao}}</div>
              <div>{{item.statuspublicacao}}</div>
              <div>{{item.qrcode}}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col s12 center">
        <a @click.prevent="loadMore()" class="btn btn-flat grey white-text">Carregar mais</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "grideventos",
  methods: {
    loadMore() {}
  }
};
</script>

<style>
.grid-block {
  width: 100%;
  float: left;
}

.grid-header {
  background: transparent;
  font-weight: bold;
  width: 100%;
  height: 2rem;
  float: left;
}

.grid-header .grid-item {
  padding: 0 4px;
  background: transparent;
  line-height: 2rem;
  float: left;
}

.grid-body {
  background: #cccccc;
  width: 100%;
  float: left;
  border-radius: 2px;
  overflow: hidden;
}

.grid-body .grid-item {
  width: 100%;
  padding: 0 4px;
  background: #cccccc;
  line-height: 2rem;
  float: left;
}
.grid-body .grid-item:nth-child(odd) {
  width: 100%;
  padding: 0 4px;
  background: #ffffff;
  line-height: 2rem;
  float: left;
}
.grid-body .grid-item div {
  float: left;
  padding: 0 4px;
}

.grid-block.t8 .grid-header .grid-item {
  width: calc(12.5% - 8px);
}

.grid-block.t8 .grid-body .grid-item div {
  width: calc(12.5% - 8px);
}
</style>
