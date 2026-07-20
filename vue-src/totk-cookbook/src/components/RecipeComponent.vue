<script setup lang="ts">
defineProps<{
  name: string
  makes?: string
  img?: string
  game_ingredients: string[]
}>()
</script>

<template>
  <h1>{{ name }}</h1>
  <p v-if="makes">Makes: {{ makes }}</p>

  <h4>In-game Ingredients</h4>
  <ul>
    <li v-for="idx in game_ingredients.length" :key="idx">{{ game_ingredients[idx - 1] }}</li>
  </ul>

  <slot v-if="$slots.notes" name="notes"></slot>

  <div v-if="img !== undefined">
    <img :src="img" alt="Image of {{ name }}" />
  </div>

  <h2>Ingredients</h2>
  <slot name="ingredients"></slot>

  <h2>Directions</h2>
  <slot></slot>

  <div v-if="$slots.credits">
    <h3>Credits</h3>
    <slot name="credits"></slot>
  </div>
</template>
