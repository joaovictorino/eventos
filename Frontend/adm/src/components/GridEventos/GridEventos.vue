<template>
  <div id="grideventos">
    <div class="row">
      <div class="col s12">
        <div>
          <div
            class="grid-header left"
            v-for="(header,key) in $store.state.eventos.grid"
            :key="key"
          >{{header.col}}</div>
        </div>
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
    <div class="row">
      <div class="col s12">
        <a class="btn btn-flat grey">Carregar mais</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'grideventos'
}
</script>

<style>
.grid-header {
  padding: 8px;
  background: #fafafa;
  font-weight: bold;
  width: 128px;
}
.grid-item {
  padding: 8px;
  background: #ccc;
  float: left;
}
.grid-item div {
  float: left;
  width: 128px;
}
</style>
