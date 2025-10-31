<template>
  <h1>Admin Dashboard</h1>

  <h3>Create New Pizza</h3>

  <form @submit.prevent="create_pizza">
    <label for="name">Pizza Name:</label>
    <input v-model="name" type="text" id="name" required />

    <br />

    <label for="toppings">Toppings:</label>
    <input v-model="toppings" type="radio" id="toppings" required />

    <br />

    <button type="submit">Add Pizza</button>
  </form>

  <p :style="{ color: status ? 'green' : 'red' }" v-html="message"></p>

  <h3>Pizza List</h3>
  <ol>
    <li v-for="pizza in pizzas" :key="pizza.id">
      <a :href="'/admin/pizza/' + pizza.id"> {{ pizza.name }} - ${{ pizza.toppings }} </a>

      <button @click="deletePizza(pizza.id)">Delete</button>
    </li>
  </ol>
</template>

<script>
export default {
  data() {
    return {
      pizzas: [],
      name: '',
      toppings: '',
      message: '',
      status: null, // true = success, false = error
    }
  },
  methods: {
    // 🍕 Load all pizzas
    load_pizzas() {
      let token = localStorage.getItem('token')
      fetch('http://127.0.0.1:5000/pizza', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
      })
        .then(async (response) => {
          const data = await response.json()
          console.log('Response status:', response.status)

          if (response.status === 200) {
            this.pizzas = data.pizzas || []
            console.log('Loaded pizzas:', this.pizzas)
          } else if (response.status === 401 || response.status === 422) {
            alert('Unauthorized access. Please log in.')
            this.$router.push('/login')
          } else {
            console.log('Error:', data)
            this.status = false
            this.message = 'Something went wrong while loading pizzas.'
          }
        })
        .catch((error) => {
          console.error('Error:', error)
          this.status = false
          this.message = 'Network error. Please try again later.'
        })
    },

    // 🍕 Create a new pizza
    create_pizza() {
      let token = localStorage.getItem('token')

      fetch('http://127.0.0.1:5000/pizza', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          name: this.name,
          toppings: this.toppings === 'on' ? true : false,
        }),
      })
        .then(async (response) => {
          const data = await response.json()
          console.log('Response status:', response.status)

          if (response.status === 201) {
            // ✅ success
            this.status = true
            this.message = `Pizza "${this.name}" added successfully!`
            this.name = ''
            this.toppings = ''
            this.load_pizzas() // refresh list
          } else if (response.status === 400) {
            this.status = false
            this.message = 'Please fill in all pizza details.'
          } else if (response.status === 401 || response.status === 422) {
            alert('Unauthorized access. Please log in again.')
            this.$router.push('/login')
          } else {
            this.status = false
            this.message = 'Error adding pizza. Try again later.'
          }
        })
        .catch((error) => {
          console.error('Error:', error)
          this.status = false
          this.message = 'Network error. Please try again later.'
        })
    },
    // 🍕 Delete a pizz
    deletePizza(pizzaId) {
      let token = localStorage.getItem('token')

      fetch(`http://127.0.0.1:5000/pizza/${pizzaId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
      })
        .then(async (response) => {
          const data = await response.json()
          console.log('Response status:', response.status)

          if (response.status === 200) {
            // ✅ success
            this.status = true
            this.message = `Pizza deleted successfully!`
            this.load_pizzas() // refresh list
          } else if (response.status === 401 || response.status === 422) {
            alert('Unauthorized access. Please log in again.')
            this.$router.push('/login')
          } else {
            this.status = false
            this.message = 'Error deleting pizza. Try again later.'
          }
        })
        .catch((error) => {
          console.error('Error:', error)
          this.status = false
          this.message = 'Network error. Please try again later.'
        })
    },
  },
  mounted() {
    console.log('Admin Dashboard mounted.')
    this.load_pizzas()
  },
}
</script>
