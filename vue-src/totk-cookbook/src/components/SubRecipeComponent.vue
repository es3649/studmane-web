<script setup lang="ts">
defineProps<{
  id?: string
  name: string
  img?: string
  game_ingredients: string[]
  ingredients: string[]
}>()
</script>

<template>
  <h2 :id="id">{{ name }}</h2>
  <h4>In-game Ingredients</h4>
  <ul>
    <li v-for="idx in game_ingredients.length" :key="idx">{{ game_ingredients[idx - 1] }}</li>
  </ul>

  <div v-if="$slots.notes">
    <h3>Notes</h3>
    <slot name="notes"></slot>
  </div>

  <div v-if="img != undefined">
    <img :src="img" alt="Image of {{ name }}" />
  </div>

  <h3>Ingredients</h3>
  <ul>
    <li v-for="idx in ingredients.length" :key="idx">{{ ingredients[idx - 1] }}</li>
  </ul>

  <h3>Directions</h3>
  <slot></slot>
</template>
