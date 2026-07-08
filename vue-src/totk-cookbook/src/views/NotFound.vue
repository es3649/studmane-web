<script setup lang="ts"></script>

<template>
  <h1>That's...an error</h1>
  <img src="@/res/dubious_food.png" alt="game sprite of dubious food" />
  <p>
    Either the Recipe you're looking for hasn't been prepared yet, or the page you're trying to
    access has been moved or doesn't exist.
  </p>
  <RouterLink to="/">&lt; Back to Home</RouterLink>
</template>
