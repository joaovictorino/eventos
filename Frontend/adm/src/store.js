import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    appName: 'Plataforma de Evenstos',
    appLogo: '',
    isOpen: '',
    isCOpen: '',
    logado: 0,
    user: 'Daniel Niemietz Braz',
    menus: [
      {
        Text: 'Hotsite',
        Link: '/hotsite',
        SVG: 'iconCalendar',
        Target: 'hotsite',
        Color: '',
        submenus: []
      },
      {
        Text: 'Cadastros básicos',
        Link: '',
        SVG: 'iconUser',
        Target: 'cadbasicos',
        Color: '',
        submenus: [
          {
            Text: 'Local',
            Link: '/cadastros-basicos/local',
            SVG: 'iconUser',
            Target: 'local',
            Color: ''
          },
          {
            Text: 'Grupo de categoria',
            Link: '/cadastros-basicos/grupo-categoria',
            SVG: 'iconUser',
            Target: 'grupo-categoria',
            Color: ''
          },
          {
            Text: 'Categoria',
            Link: '/cadastros-basicos/categoria',
            SVG: 'iconBox',
            Target: 'categoria',
            Color: ''
          }
        ]
      },
      {
        Text: 'Eventos',
        Link: '/eventos',
        SVG: 'iconBox',
        Target: 'eventos',
        Color: '',
        submenus: []
      },
      {
        Text: 'Comentários',
        Link: '/comments',
        SVG: 'iconEnvelope',
        Target: 'comments',
        Color: '',
        submenus: []
      },
      {
        Text: 'Notificações',
        Link: '/notification',
        SVG: 'iconGarbage',
        Target: 'notification',
        Color: '',
        submenus: []
      },
      {
        Text: 'Grupos e usuários',
        Link: '/groups-users',
        SVG: 'iconImage',
        Target: 'groups-users',
        Color: '',
        submenus: [
          {
            Text: 'Grupos',
            Link: '/groups',
            SVG: 'iconUser',
            Target: 'groups',
            Color: ''
          },
          {
            Text: 'Usuários',
            Link: '/users',
            SVG: 'iconUser',
            Target: 'users',
            Color: ''
          }
        ]
      }
    ],
    eventos: {
      count: 1000,
      grid: [
        {
          col: 'Título'
        },
        {
          col: 'Megaevento'
        },
        {
          col: 'Subcategoria'
        },
        {
          col: 'Local'
        },
        {
          col: 'Dt evento'
        },
        {
          col: 'Dt publicação'
        },
        {
          col: 'Status'
        },
        {
          col: 'QRCode'
        }
      ],
      item: [
        {
          titulo: 'Nome evento',
          megaevento: 'Sim',
          subcategoria: 'sub',
          local: 'Sé',
          dataevento: '01/01/2012',
          datapublicacao: '02/02/2012',
          statuspublicacao: 'Ativo',
          qrcode: '3232323232'
        },
        {
          titulo: 'Nome evento',
          megaevento: 'Sim',
          subcategoria: 'sub',
          local: 'Sé',
          dataevento: '01/01/2012',
          datapublicacao: '02/02/2012',
          statuspublicacao: 'Ativo',
          qrcode: '3232323232'
        },
        {
          titulo: 'Nome evento',
          megaevento: 'Sim',
          subcategoria: 'sub',
          local: 'Sé',
          dataevento: '01/01/2012',
          datapublicacao: '02/02/2012',
          statuspublicacao: 'Ativo',
          qrcode: '3232323232'
        },
        {
          titulo: 'Nome evento',
          megaevento: 'Sim',
          subcategoria: 'sub',
          local: 'Sé',
          dataevento: '01/01/2012',
          datapublicacao: '02/02/2012',
          statuspublicacao: 'Ativo',
          qrcode: '3232323232'
        },
        {
          titulo: 'Nome evento',
          megaevento: 'Sim',
          subcategoria: 'sub',
          local: 'Sé',
          dataevento: '01/01/2012',
          datapublicacao: '02/02/2012',
          statuspublicacao: 'Ativo',
          qrcode: '3232323232'
        }
      ]
    }
  },
  mutations: {

  },
  actions: {

  }
})
