import { describe, it, expect, vi, beforeEach } from 'vitest'
import { mount } from '@vue/test-utils'
import { createPinia, setActivePinia, defineStore } from 'pinia'
import ContactListView from '../views/ContactListView.vue'
import { useContactStore } from '../stores/contacts'
import { ref, reactive } from 'vue'

// Mocking the store
vi.mock('../stores/contacts', () => ({
    useContactStore: vi.fn()
}))

describe('ContactListView.vue', () => {
    let pinia

    beforeEach(() => {
        pinia = createPinia()
        setActivePinia(pinia)
    })

    it('renders "No contacts found" when list is empty', () => {
        // Create a real store for the test
        const useTestStore = defineStore('contacts-test', () => {
            return {
                contacts: ref([]),
                loading: ref(false),
                error: ref(null),
                fetchAll: vi.fn()
            }
        })

        // Inject the mock store into the component's import
        vi.mocked(useContactStore).mockReturnValue(useTestStore())

        const wrapper = mount(ContactListView, {
            global: {
                plugins: [pinia],
                stubs: ['router-link']
            }
        })
        expect(wrapper.text()).toContain('No contacts found')
    })

    it('renders contacts table when data is present', () => {
        const useTestStore = defineStore('contacts-test-2', () => {
            return {
                contacts: ref([{ id: 1, name: 'John Doe', phone_number: '12345', email: 'john@example.com' }]),
                loading: ref(false),
                error: ref(null),
                fetchAll: vi.fn()
            }
        })
        vi.mocked(useContactStore).mockReturnValue(useTestStore())

        const wrapper = mount(ContactListView, {
            global: {
                plugins: [pinia],
                stubs: ['router-link']
            }
        })
        expect(wrapper.text()).toContain('John Doe')
        expect(wrapper.text()).toContain('12345')
    })

    it('calls fetchAll on mount', () => {
        const fetchAllSpy = vi.fn()
        const useTestStore = defineStore('contacts-test-3', () => {
            return {
                contacts: ref([]),
                loading: ref(false),
                error: ref(null),
                fetchAll: fetchAllSpy
            }
        })
        vi.mocked(useContactStore).mockReturnValue(useTestStore())

        mount(ContactListView, {
            global: {
                plugins: [pinia],
                stubs: ['router-link']
            }
        })
        expect(fetchAllSpy).toHaveBeenCalled()
    })
})
