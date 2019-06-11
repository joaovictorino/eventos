<template>
  <div id="app">
    <div id="main" class="row">
      <Header></Header>
      <Menu :class="{ openmenu: $store.state.isOpen == 'openmenu' }"></Menu>
      <Content :class="{ expcontent: $store.state.isCOpen == 'expcontent' }"></Content>
    </div>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Menu from "./components/Menu.vue";
import Content from "./components/Content.vue";

export default {
  data() {
    return {};
  },
  name: "app",
  components: {
    Header,
    Menu,
    Content
  },
  methods: {}
};
</script>

<style>
#app {
}
</style>
