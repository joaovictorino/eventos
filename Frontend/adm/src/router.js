import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/hotsite',
      name: 'hotsite',
      component: function () {
        return import('./views/Hotsite.vue')
      }
    },
    {
      path: '/cadastros-basicos',
      name: 'cadbasicos',
      component: function () {
        return import('./views/CadastrosBasicos.vue')
      }
    },
    {
      path: '/cadastros-basicos/local',
      name: 'local',
      component: function () {
        return import('./views/Local.vue')
      }
    },
    {
      path: '/cadastros-basicos/grupo-categoria',
      name: 'grupo-categoria',
      component: function () {
        return import('./views/GrupoCategoria.vue')
      }
    },
    {
      path: '/cadastros-basicos/categoria',
      name: 'categoria',
      component: function () {
        return import('./views/Categoria.vue')
      }
    },
    {
      path: '/eventos',
      name: 'eventos',
      component: function () {
        return import('./views/BuscaEventos.vue')
      }
    },
    {
      path: '/comments',
      name: 'comments',
      component: function () {
        return import('./views/Comments.vue')
      }
    },
    {
      path: '/notification',
      name: 'notification',
      component: function () {
        return import('./views/Notification.vue')
      }
    },
    {
      path: '/groups',
      name: 'groups',
      component: function () {
        return import('./views/Groups.vue')
      }
    },
    {
      path: '/users',
      name: 'users',
      component: function () {
        return import('./views/Users.vue')
      }
    }
  ]
})
