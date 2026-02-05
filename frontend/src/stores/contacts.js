import { defineStore } from 'pinia'
import axios from 'axios'
import { ref } from 'vue'

// Using direct URL as CORS is enabled. 
// For production/docker with no mapped ports, one would use a proxy or env var.
// Required: http://localhost:8000 in dev.
const API_URL = 'http://localhost:8000';

export const useContactStore = defineStore('contacts', () => {
    const contacts = ref([])
    const loading = ref(false)
    const error = ref(null)

    const fetchAll = async (search = '') => {
        loading.value = true
        try {
            const response = await axios.get(`${API_URL}/contacts`, { params: { search } })
            contacts.value = response.data
            error.value = null
        } catch (err) {
            error.value = err.message
        } finally {
            loading.value = false
        }
    }

    const getOne = async (id) => {
        loading.value = true
        try {
            const response = await axios.get(`${API_URL}/contacts/${id}`)
            error.value = null
            return response.data
        } catch (err) {
            error.value = err.message
            return null
        } finally {
            loading.value = false
        }
    }

    const create = async (contact) => {
        loading.value = true
        try {
            await axios.post(`${API_URL}/contacts`, contact)
            error.value = null
        } catch (err) {
            error.value = err.response?.data?.detail || err.message
            throw err
        } finally {
            loading.value = false
        }
    }

    const update = async (id, contact) => {
        loading.value = true
        try {
            await axios.put(`${API_URL}/contacts/${id}`, contact)
            error.value = null
        } catch (err) {
            error.value = err.response?.data?.detail || err.message
            throw err
        } finally {
            loading.value = false
        }
    }

    const remove = async (id) => {
        loading.value = true
        try {
            await axios.delete(`${API_URL}/contacts/${id}`)
            contacts.value = contacts.value.filter(c => c.id !== id)
            error.value = null
        } catch (err) {
            error.value = err.message
        } finally {
            loading.value = false
        }
    }

    return { contacts, loading, error, fetchAll, getOne, create, update, remove }
})
