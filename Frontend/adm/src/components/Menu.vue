<template>
  <nav id="menu" class="col m3 l2">
    <div class="row">
      <div class="col s12">
        <div id="app-title" class="logo">
          <a id="logo-site" href="/">
            <icon-base icon-name="logo" :width="64" :height="64" :view="'0 0 48 48'">
              <logo/>
            </icon-base>
            <h1>{{$store.state.appName}}</h1>
          </a>
        </div>
        <div class="menu-content">
          <ul class="menu-list collapsible">
            <li v-for="(menu,key) in $store.state.menus" :key="key">
              <div class="collapsible-header">
                <router-link :to="menu.Link" class="menu-item" :data-target="menu.Target">
                  <icon-base :key="key" icon-name="box">
                    <component :is="menu.SVG"/>
                  </icon-base>
                  {{menu.Text}}
                </router-link>
              </div>
              <div class="collapsible-body">
                <div v-for="(submenu,key) in menu.submenus" :key="key">
                  <router-link :to="submenu.Link" class="menu-item">
                    <icon-base :key="key" icon-name="box">
                      <component :is="submenu.SVG"/>
                    </icon-base>
                    {{submenu.Text}}
                  </router-link>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import iconBase from '@/components/iconBase.vue'

import logo from '@/components/Logo.vue'

import iconUser from '@/components/Icons/iconUser.vue'
import iconBox from '@/components/Icons/iconBox.vue'
import iconCalendar from '@/components/Icons/iconCalendar.vue'
import iconEnvelope from '@/components/Icons/iconEnvelope.vue'
import iconGarbage from '@/components/Icons/iconGarbage.vue'
import iconImage from '@/components/Icons/iconImage.vue'
import iconMoon from '@/components/Icons/iconMoon.vue'
import iconWrite from '@/components/Icons/iconWrite.vue'

export default {
  data () {
    return {}
  },
  components: {
    logo,
    iconBase,
    iconUser,
    iconBox,
    iconCalendar,
    iconEnvelope,
    iconGarbage,
    iconImage,
    iconMoon,
    iconWrite
  },
  methods: {},
  mounted: function () {
    document.addEventListener('DOMContentLoaded', function () {
      var melems = document.querySelectorAll('.collapsible')
      M.Collapsible.init(melems, { accordion: true }); // eslint-disable-line
    })
  }
}
</script>

<style scoped>
</style>
