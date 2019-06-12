<template>
  <header id="header" class="row">
    <div class="menu-button col s2 l2 left">
      <a
        id="menu-open"
        href="#!"
        :class="{active: $store.state.isOpen}"
        @click.prevent="updateMenu('openmenu', 'expcontent')"
      >
        <icon-base icon-name="menu" :width="24" icon-color="#ffffff">
          <icon-menu/>
        </icon-base>
      </a>
    </div>
    <div v-if="$store.state.logado" class="col s5 l5 header-auth right right-align">
      <p>
        <span class="header-user">{{$store.state.user}}</span> |
        <span class="header-settings">
          <a href="#">Conta</a>
        </span> |
        <span class="header-logoff">
          <a @click="$store.state.logado = !$store.state.logado">Sair</a>
        </span>
      </p>
    </div>
    <div v-else class="col s5 l5 header-auth right right-align">
      <p class="header-login">
        <a @click="$store.state.logado = !$store.state.logado">Logar</a>
      </p>
    </div>
  </header>
</template>

<script>
import iconBase from "@/components/iconBase.vue";

import iconMenu from "@/components/Icons/iconMenu.vue";

export default {
  data() {
    return {};
  },
  components: {
    iconBase,
    iconMenu
  },
  methods: {
    updateMenu(menu, content) {
      this.$store.state.isOpen =
        this.$store.state.isOpen === menu ? null : menu;
      this.$store.state.isCOpen =
        this.$store.state.isCOpen === content ? null : content;
      Menuinst.close();
    }
  },
  mounted: function() {}
};
</script>

<style scoped>
</style>
