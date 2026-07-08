<script setup lang="ts">
defineProps<{
  name: string
  img?: string
  game_ingredients: string[]
  ingredients: string[]
}>()
</script>

<template>
  <h2>{{ name }}</h2>
  <h4>In-game Ingredients</h4>
  <ul>
    <li v-for="idx in game_ingredients.length" :key="idx">{{ game_ingredients[idx - 1] }}</li>
  </ul>

  <slot v-if="$slots.notes" name="notes"></slot>

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
