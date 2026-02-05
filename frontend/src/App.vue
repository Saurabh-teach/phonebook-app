<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <router-link to="/">Contacts</router-link> |
      <router-link to="/create">Add Contact</router-link>
    </nav>
  </header>

  <main>
    <RouterView />
  </main>
</template>

<style>
header {
  line-height: 1.5;
  background-color: #f8f9fa;
  padding: 1rem;
  margin-bottom: 2rem;
  border-bottom: 1px solid #dee2e6;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  text-decoration: none;
  color: #2c3e50;
  font-weight: 500;
}

nav a.router-link-active {
  color: #42b883;
  font-weight: bold;
}

main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

@media (prefers-color-scheme: dark) {
  header {
    background-color: #1a1a1a;
    border-bottom: 1px solid #333;
  }
  nav a {
    color: #e1e1e1;
  }
  nav a.router-link-active {
    color: #42b883;
  }
}
</style>
