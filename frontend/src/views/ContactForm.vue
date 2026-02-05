<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useContactStore } from '../stores/contacts'

const route = useRoute()
const router = useRouter()
const store = useContactStore()

const isEdit = computed(() => !!route.params.id)
const form = ref({
  name: '',
  phone_number: '',
  email: '',
  address: ''
})
const localError = ref(null)

onMounted(async () => {
  if (isEdit.value) {
    const contact = await store.getOne(route.params.id)
    if (contact) {
      form.value = { ...contact }
    }
  }
})

const validatePhone = (phone) => {
    return /^\+?[1-9]\d{1,14}$/.test(phone)
}

const handleSubmit = async () => {
  localError.value = null
  if (!form.value.name || !form.value.phone_number) {
    localError.value = "Name and Phone are required."
    return
  }
  if (!validatePhone(form.value.phone_number)) {
      localError.value = "Invalid phone format (E.164 or digits)."
      return
  }

  try {
    if (isEdit.value) {
      await store.update(route.params.id, form.value)
    } else {
      await store.create(form.value)
    }
    router.push('/')
  } catch (err) {
      // Error is handled in store, but we display it below
  }
}
</script>

<template>
  <div class="contact-form-container">
    <h1>{{ isEdit ? 'Edit Contact' : 'Create Contact' }}</h1>
    
    <div v-if="localError || store.error" class="error">
      {{ localError || store.error }}
    </div>
    
    <form @submit.prevent="handleSubmit" class="form-card">
      <div class="form-group">
        <label>Name *</label>
        <input v-model="form.name" required placeholder="John Doe" />
      </div>
      
      <div class="form-group">
        <label>Phone Number *</label>
        <input v-model="form.phone_number" required placeholder="+1234567890" />
        <small>Format: +1234567890</small>
      </div>
      
      <div class="form-group">
        <label>Email</label>
        <input v-model="form.email" type="email" placeholder="john@example.com" />
      </div>
      
      <div class="form-group">
        <label>Address</label>
        <textarea v-model="form.address" rows="3" placeholder="123 Main St"></textarea>
      </div>
      
      <div class="form-actions">
        <button type="submit" :disabled="store.loading" class="btn primary">
          {{ store.loading ? 'Saving...' : 'Save Contact' }}
        </button>
        <router-link to="/" class="btn secondary">Cancel</router-link>
      </div>
    </form>
  </div>
</template>

<style scoped>
.contact-form-container { max-width: 600px; margin: 0 auto; }
.form-card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
.form-group { margin-bottom: 20px; }
label { display: block; margin-bottom: 8px; font-weight: 500; }
input, textarea { width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 4px; box-sizing: border-box; font-family: inherit; }
input:focus, textarea:focus { border-color: #42b883; outline: none; }
small { color: #666; font-size: 12px; }
.form-actions { display: flex; gap: 15px; margin-top: 30px; }
.btn { padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; text-decoration: none; font-size: 16px; text-align: center; }
.btn.primary { background-color: #42b883; color: white; flex: 1; }
.btn.secondary { background-color: #e0e0e0; color: #333; }
.btn:disabled { opacity: 0.7; cursor: not-allowed; }
.error { background: #fee; color: #c00; padding: 15px; border-radius: 4px; margin-bottom: 20px; }
</style>
