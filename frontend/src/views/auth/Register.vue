<template>
  <h1>User Registration Page</h1>

  <form @submit.prevent="register">
    <label for="email">Email:</label>
    <input v-model="email" type="email" id="email" name="email" required />

    <br />

    <label for="password">Password:</label>
    <input v-model="password1" type="password" id="password1" name="password" required />

    <br />

    <label for="password">Confirm the Password:</label>
    <input v-model="password2" type="password" id="password2" name="password" required />

    <br />

    <button type="submit">Register</button>
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
    passwordCheck() {
      if (this.password1 !== this.password2) {
        this.message = 'Passwords do not match!'
        return false
      }
      this.message = ''
      return true
    },
    register() {
      if (!this.passwordCheck()) {
        return
      }

      fetch('http://127.0.0.1:5000/register', {
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

          if (response.status === 201) {
            // ✅ success
            this.status = true
            this.message = `${data.message} <a href="/login">Click here to login</a>.`
          } else if (response.status === 400) {
            // ⚠️ missing input
            this.status = false
            this.message = 'Please fill in both email and password.'
          } else if (response.status === 409) {
            // ❌ already exists
            this.status = false
            this.message = 'User already exists! Try logging in.'
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
    console.log('Register component mounted.')
  },
}
</script>
