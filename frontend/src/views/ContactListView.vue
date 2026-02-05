<script setup>
import { onMounted, ref, watch } from 'vue'
import { useContactStore } from '../stores/contacts'
import { storeToRefs } from 'pinia'

const store = useContactStore()
const { contacts, loading, error } = storeToRefs(store)
const search = ref('')

onMounted(() => {
  store.fetchAll()
})

watch(search, (newVal) => {
    store.fetchAll(newVal)
})

const deleteContact = async (id) => {
    if(confirm('Are you sure you want to delete this contact?')) {
        await store.remove(id)
    }
}
</script>

<template>
  <div class="contact-list">
    <div class="header-actions">
      <h1>Contacts</h1>
      <router-link to="/create" class="btn primary">Add New</router-link>
    </div>
    
    <input v-model="search" placeholder="Search contacts..." class="search-bar" />
    
    <div v-if="loading" class="loading">Loading...</div>
    <div v-if="error" class="error">{{ error }}</div>
    
    <div class="table-container" v-if="contacts.length">
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Phone</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="contact in contacts" :key="contact.id">
            <td>{{ contact.name || 'No Name' }}</td>
            <td>{{ contact.phone_number || 'No Phone' }}</td>
            <td>{{ contact.email || 'No Email' }}</td>
            <td class="actions">
              <router-link :to="`/${contact.id}`" class="btn small outline">Edit</router-link>
              <button @click="deleteContact(contact.id)" class="btn small danger-outline">
                <span>🗑️ Delete</span>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else-if="!loading" class="empty-state">No contacts found.</div>
  </div>
</template>

<style scoped>
.contact-list { max-width: 800px; margin: 0 auto; }
.header-actions { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.search-bar { width: 100%; padding: 10px; margin-bottom: 20px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; }
.table-container { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 1px 3px rgba(0,0,0,0.1); color: #333; }
th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
th { background-color: #f8f9fa; font-weight: 600; color: #333; }
.actions { display: flex; gap: 10px; }
.btn { display: inline-flex; align-items: center; gap: 4px; padding: 8px 16px; border-radius: 6px; text-decoration: none; cursor: pointer; border: 1px solid transparent; font-size: 14px; transition: all 0.2s; white-space: nowrap; }
.btn.primary { background-color: #42b883; color: white; border-color: #42b883; }
.btn.small { padding: 4px 10px; font-size: 12px; }
.btn.outline { background: transparent; border-color: #ddd; color: #666; }
.btn.outline:hover { border-color: #42b883; color: #42b883; }
.btn.danger-outline { background: #fff5f5; border-color: #ff4444; color: #ff4444; font-weight: 600; }
.btn.danger-outline:hover { background-color: #ff4444; color: white; }
.btn:hover { transform: translateY(-1px); box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
@media (prefers-color-scheme: dark) {
  table { background: #2c2c2c; color: #e1e1e1; }
  th { background-color: #1a1a1a; color: #e1e1e1; border-bottom: 1px solid #444; }
  td { border-bottom: 1px solid #444; }
  .btn.outline { border-color: #555; color: #aaa; }
}
.error { background: #fee; color: #c00; padding: 10px; border-radius: 4px; margin-bottom: 10px; }
.empty-state { text-align: center; color: #666; padding: 20px; }
</style>
