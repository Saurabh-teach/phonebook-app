import { createRouter, createWebHistory } from 'vue-router'
import ContactListView from '../views/ContactListView.vue'
import ContactForm from '../views/ContactForm.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', name: 'home', component: ContactListView },
        { path: '/create', name: 'create', component: ContactForm },
        { path: '/:id', name: 'detail', component: ContactForm },
        { path: '/:id/edit', name: 'edit', component: ContactForm }
    ]
})

export default router
