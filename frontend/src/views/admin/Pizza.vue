<template>
  <div class="pizza-details">
    <h1>Pizza Details for admin</h1>

    <div v-if="pizza" class="pizza-card">
      <h2>{{ pizza.name }}</h2>
      <p><strong>Toppings:</strong> {{ pizza.toppings }}</p>
    </div>

    <p v-else-if="loading" class="loading">Loading pizza details...</p>
    <p v-else class="error">{{ message }}</p>
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
        } else if (response.status === 401 || response.status === 422) {
          alert('Unauthorized access. Please log in again.')
          this.$router.push('/login')
        } else if (response.status === 404) {
          this.message = 'Pizza not found.'
        } else {
          this.message = 'Unexpected error. Please try again later.'
        }
      } catch (error) {
        console.error('Error:', error)
        this.message = 'Network error. Please try again later.'
      } finally {
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

<style scoped>
.pizza-details {
  max-width: 600px;
  margin: 60px auto;
  padding: 30px;
  background-color: #fffaf3;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  font-family: 'Poppins', sans-serif;
  text-align: center;
}

h1 {
  font-size: 2rem;
  color: #d35400;
  margin-bottom: 20px;
}

.pizza-card {
  background: #fff;
  border: 2px solid #f5c26b;
  border-radius: 10px;
  padding: 20px;
  box-shadow: 0 2px 6px rgba(243, 156, 18, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.pizza-card:hover {
  transform: scale(1.03);
  box-shadow: 0 4px 12px rgba(243, 156, 18, 0.3);
}

.pizza-card h2 {
  color: #e67e22;
  font-size: 1.6rem;
  margin-bottom: 10px;
}

.pizza-card p {
  font-size: 1rem;
  color: #444;
}

.loading {
  color: #555;
  font-style: italic;
  font-size: 1.1rem;
}

.error {
  color: #e74c3c;
  font-weight: bold;
  font-size: 1.1rem;
}
</style>
