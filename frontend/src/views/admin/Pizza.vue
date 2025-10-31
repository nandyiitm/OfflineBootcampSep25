<template>
  <div>
    <h1>Pizza Details</h1>

    <div v-if="pizza">
      <h2>{{ pizza.name }}</h2>
      <p><strong>Toppings:</strong> {{ pizza.toppings }}</p>
    </div>

    <p v-else-if="loading">Loading pizza details...</p>
    <p v-else :style="{ color: 'red' }">{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pizza: null,
      message: '',
      loading: true,
    }
  },
  methods: {
    async loadPizza() {
      const id = this.$route.params.id
      const token = localStorage.getItem('token')

      try {
        const response = await fetch(`http://127.0.0.1:5000/pizza/${id}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${token}`,
          },
        })

        const data = await response.json()
        console.log('Response status:', response.status)

        if (response.status === 200) {
          this.pizza = data
          this.loading = false
        } else if (response.status === 401 || response.status === 422) {
          alert('Unauthorized access. Please log in again.')
          this.$router.push('/login')
        } else if (response.status === 404) {
          this.message = 'Pizza not found.'
          this.loading = false
        } else {
          this.message = 'Unexpected error. Please try again later.'
          this.loading = false
        }
      } catch (error) {
        console.error('Error:', error)
        this.message = 'Network error. Please try again later.'
        this.loading = false
      }
    },
  },
  mounted() {
    console.log('Pizza detail component mounted for ID:', this.$route.params.id)
    this.loadPizza()
  },
}
</script>
