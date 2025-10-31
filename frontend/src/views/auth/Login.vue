<template>
  <h1>User Login Page</h1>

  <form @submit.prevent="login">
    <label for="email">Email:</label>
    <input v-model="email" type="email" id="email" name="email" required />

    <br />

    <label for="password">Password:</label>
    <input v-model="password1" type="password" id="password1" name="password" required />

    <br />

    <button type="submit">Login</button>
  </form>

  <p :style="{ color: status ? 'green' : 'red' }" v-html="message"></p>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password1: '',
      password2: '',
      message: '',
      status: null, // true = success, false = error
    }
  },
  methods: {
    login() {
      fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password1,
        }),
      })
        .then(async (response) => {
          console.log('Response status:', response.status)
          const data = await response.json()

          if (response.status === 200) {
            // ✅ success
            console.log('Login successful:', data)

            localStorage.setItem('token', data.token)

            this.status = true
            this.message = `${data.message} redirecting to dashboard...`

            setTimeout(() => {
              if (data.user.role === 'admin') {
                this.$router.push('/admin/dashboard')
              } else {
                this.$router.push('/user/dashboard')
              }
            }, 3000) // 3000 milliseconds = 3 seconds

            console.log('Redirecting to dashboard...')
          } else if (response.status === 400) {
            // ⚠️ missing input
            this.status = false
            this.message = 'Please fill in both email and password.'
          } else if (response.status === 401) {
            // ❌ already exists
            this.status = false
            this.message = 'Invalid credentials! Check and try again.'
          } else {
            // 🧯 unexpected error
            this.status = false
            this.message = 'Something went wrong. Please try again.'
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
    console.log('Login component mounted.')
  },
}
</script>
