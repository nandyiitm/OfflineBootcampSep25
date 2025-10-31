<script setup>
function loadMessage() {
  fetch('http://localhost:5000/')
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      document.getElementById('message').innerText = data.message
    })
    .catch((error) => {
      document.getElementById('message').innerText = 'Error fetching message'
      console.log(error)
      console.error('Error fetching message:', error)
    })
}
</script>

<template>
  <div class="pizza-home">
    <h1>Welcome to MAD2 Project</h1>

    <p id="message">Click below button to load message</p>

    <button @click="loadMessage()">Get message from backend</button>

    <br />
    <a href="/login">Login to your account</a>
    <br />
    <span>Don't have an account? <a href="/register">Click here to create!</a></span>
  </div>
</template>

<style scoped>
.pizza-home {
  position: relative;
  text-align: center;
  color: #fff8e7;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: 'Poppins', sans-serif;
  overflow: hidden;
}

.pizza-home::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('https://upload.wikimedia.org/wikipedia/commons/9/91/Pizza-3007395.jpg');
  background-size: cover;
  background-position: center;
  filter: blur(6px) brightness(0.6);
  z-index: -1;
}

.pizza-home > * {
  position: relative;
  z-index: 1;
}

h1 {
  font-size: 3rem;
  color: #ffcc33;
  text-shadow: 2px 2px 6px #000;
  margin-bottom: 20px;
}

p {
  font-size: 1.2rem;
  background-color: rgba(0, 0, 0, 0.5);
  padding: 10px 20px;
  border-radius: 10px;
}

button {
  background-color: #e63946;
  color: white;
  font-size: 1rem;
  border: none;
  padding: 12px 25px;
  border-radius: 25px;
  cursor: pointer;
  margin: 15px 0;
  transition: all 0.3s ease;
}

button:hover {
  background-color: #ff5733;
  transform: scale(1.05);
}

a {
  color: #ffcc33;
  text-decoration: none;
  font-weight: bold;
  margin-top: 5px;
}

a:hover {
  text-decoration: underline;
}
</style>
